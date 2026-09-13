#!/usr/bin/env python3
"""Run one independent GPT-6 Astra paper-trading committee check."""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from zoneinfo import ZoneInfo


ROOT = Path(__file__).resolve().parent
CONFIG_PATH = ROOT / "config.json"
PROMPT_PATH = ROOT / "prompt.md"
DECISION_LOG = ROOT / "memory" / "decision-log.jsonl"
TRADE_LOG = ROOT / "memory" / "trade-log.jsonl"
STATE_PATH = ROOT / "dashboard" / "state.json"
NY = ZoneInfo("America/New_York")
PAPER_URL = "https://paper-api.alpaca.markets"

ROUTINE_TIMES = {
    (8, 0): "premarket-research",
    (9, 25): "opening-plan",
    (10, 15): "entry-check",
    (12, 30): "portfolio-check",
    (15, 0): "closing-decision",
    (15, 50): "risk-shutdown",
}

DECISION_SCHEMA = {
    "type": "object",
    "additionalProperties": False,
    "required": [
        "action", "symbol", "confidence", "thesis", "contrary_evidence",
        "invalidation", "entry_condition", "holding_period", "sources",
    ],
    "properties": {
        "action": {"type": "string", "enum": ["BUY", "SELL", "HOLD", "WATCH"]},
        "symbol": {"type": ["string", "null"]},
        "confidence": {"type": "integer", "minimum": 0, "maximum": 100},
        "thesis": {"type": "string"},
        "contrary_evidence": {"type": "string"},
        "invalidation": {"type": "string"},
        "entry_condition": {"type": "string"},
        "holding_period": {"type": "string"},
        "sources": {"type": "array", "items": {"type": "string"}, "maxItems": 8},
    },
}


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


def load_json(path: Path, default):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (FileNotFoundError, json.JSONDecodeError):
        return default


def read_jsonl(path: Path, limit: int = 30) -> list[dict]:
    if not path.exists():
        return []
    rows = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        try:
            rows.append(json.loads(line))
        except json.JSONDecodeError:
            continue
    return rows[-limit:]


def append_jsonl(path: Path, row: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(row, separators=(",", ":")) + "\n")


def request_json(url: str, *, headers=None, method="GET", body=None, timeout=60):
    payload = None if body is None else json.dumps(body).encode("utf-8")
    req = urllib.request.Request(url, data=payload, method=method)
    for key, value in (headers or {}).items():
        req.add_header(key, value)
    if body is not None:
        req.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(req, timeout=timeout) as response:
            raw = response.read().decode("utf-8")
            return json.loads(raw) if raw else {}
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"HTTP {exc.code} from {url}: {detail[:1000]}") from exc


class Alpaca:
    def __init__(self):
        self.base = os.environ.get("ASTRA_ALPACA_BASE_URL", PAPER_URL).rstrip("/")
        self.key = os.environ.get("ASTRA_ALPACA_API_KEY", "")
        self.secret = os.environ.get("ASTRA_ALPACA_SECRET_KEY", "")
        if self.base != PAPER_URL:
            raise RuntimeError("Astra is paper-only; ASTRA_ALPACA_BASE_URL must be the Alpaca paper URL")
        if not self.key or not self.secret:
            raise RuntimeError("Missing dedicated ASTRA_ALPACA_API_KEY or ASTRA_ALPACA_SECRET_KEY")
        self.headers = {
            "APCA-API-KEY-ID": self.key,
            "APCA-API-SECRET-KEY": self.secret,
        }

    def get(self, path: str):
        return request_json(self.base + path, headers=self.headers)

    def data_get(self, path: str):
        return request_json("https://data.alpaca.markets" + path, headers=self.headers)

    def account_snapshot(self) -> dict:
        account = self.get("/v2/account")
        positions = self.get("/v2/positions")
        orders = self.get("/v2/orders?status=open&limit=100&nested=true")
        clock = self.get("/v2/clock")
        return {"account": account, "positions": positions, "open_orders": orders, "clock": clock}

    def latest_price(self, symbol: str) -> float:
        data = self.data_get(f"/v2/stocks/{urllib.parse.quote(symbol)}/trades/latest")
        return float(data["trade"]["p"])

    def asset(self, symbol: str) -> dict:
        return self.get(f"/v2/assets/{urllib.parse.quote(symbol)}")

    def submit_buy(self, symbol: str, qty: int, stop_price: float) -> dict:
        return request_json(
            self.base + "/v2/orders", headers=self.headers, method="POST",
            body={
                "symbol": symbol, "qty": str(qty), "side": "buy", "type": "market",
                "time_in_force": "day", "order_class": "oto",
                "stop_loss": {"stop_price": f"{stop_price:.2f}"},
            },
        )

    def close_position(self, symbol: str) -> dict:
        return request_json(
            self.base + f"/v2/positions/{urllib.parse.quote(symbol)}",
            headers=self.headers, method="DELETE",
        )


def scheduled_routine(now: datetime | None = None) -> str | None:
    local = (now or utc_now()).astimezone(NY)
    if local.weekday() >= 5:
        return None
    for (hour, minute), name in ROUTINE_TIMES.items():
        if local.hour == hour and minute <= local.minute <= minute + 20:
            return name
    return None


def openai_decision(routine: str, snapshot: dict, history: list[dict], config: dict) -> dict:
    api_key = os.environ.get("OPENAI_API_KEY", "")
    if not api_key:
        raise RuntimeError("Missing OPENAI_API_KEY")
    model = os.environ.get("ASTRA_MODEL", config["model"])
    context = {
        "routine": routine,
        "timestamp_utc": utc_now().isoformat(),
        "risk_rules": config,
        "account": snapshot,
        "astra_prior_decisions": history[-12:],
    }
    body = {
        "model": model,
        "reasoning": {"effort": config.get("reasoning_effort", "high")},
        "tools": [{"type": "web_search"}],
        "instructions": PROMPT_PATH.read_text(encoding="utf-8"),
        "input": "Research the current market as needed, then make this routine's decision.\n\n" + json.dumps(context),
        "text": {
            "format": {
                "type": "json_schema",
                "name": "astra_trade_decision",
                "strict": True,
                "schema": DECISION_SCHEMA,
            }
        },
    }
    response = request_json(
        "https://api.openai.com/v1/responses",
        headers={"Authorization": f"Bearer {api_key}"},
        method="POST", body=body, timeout=300,
    )
    text = response.get("output_text")
    if not text:
        chunks = []
        for item in response.get("output", []):
            for content in item.get("content", []):
                if content.get("type") in {"output_text", "text"}:
                    chunks.append(content.get("text", ""))
        text = "".join(chunks)
    if not text:
        raise RuntimeError("OpenAI response contained no decision text")
    return json.loads(text)


def weekly_buy_count(rows: list[dict], now: datetime) -> int:
    local = now.astimezone(NY)
    monday = local.date().toordinal() - local.weekday()
    count = 0
    for row in rows:
        if row.get("side") != "BUY" or not row.get("timestamp"):
            continue
        try:
            day = datetime.fromisoformat(row["timestamp"]).astimezone(NY).date().toordinal()
        except ValueError:
            continue
        if day >= monday:
            count += 1
    return count


def validate_and_execute(decision: dict, snapshot: dict, config: dict, alpaca: Alpaca,
                         routine: str, trade_rows: list[dict]) -> dict:
    result = {"status": "NO_ORDER", "reason": "Decision did not request an order"}
    action = decision.get("action")
    symbol = (decision.get("symbol") or "").upper().strip()
    positions = {p.get("symbol", "").upper(): p for p in snapshot.get("positions", [])}
    pending_buys = {
        o.get("symbol", "").upper() for o in snapshot.get("open_orders", [])
        if o.get("side") == "buy" and o.get("status") not in {"filled", "canceled", "expired", "rejected"}
    }
    account = snapshot.get("account", {})
    equity = float(account.get("equity", 0))
    last_equity = float(account.get("last_equity", equity or 1))
    day_pct = ((equity / last_equity) - 1) * 100 if last_equity else 0

    if action not in {"BUY", "SELL"}:
        return result
    if not re.fullmatch(r"[A-Z][A-Z0-9.\-]{0,9}", symbol):
        return {"status": "REJECTED", "reason": "Invalid or missing ticker"}
    if not snapshot.get("clock", {}).get("is_open"):
        return {"status": "REJECTED", "reason": "Market is closed"}
    if os.environ.get("ASTRA_EXECUTION_ENABLED", "false").lower() != "true":
        return {"status": "PROPOSED_ONLY", "reason": "ASTRA_EXECUTION_ENABLED is not true"}

    if action == "SELL":
        if symbol not in positions:
            return {"status": "REJECTED", "reason": "Cannot sell a position Astra does not own"}
        order = alpaca.close_position(symbol)
        return {"status": "SUBMITTED", "reason": "Existing position close submitted", "order": order}

    if routine == "risk-shutdown":
        return {"status": "REJECTED", "reason": "New buys are forbidden during risk shutdown"}
    if int(decision.get("confidence", 0)) < int(config["min_buy_confidence"]):
        return {"status": "REJECTED", "reason": "Confidence is below the buy gate"}
    if symbol in positions:
        return {"status": "REJECTED", "reason": "No averaging down or adding to an existing position"}
    if symbol in pending_buys:
        return {"status": "REJECTED", "reason": "A buy order for this ticker is already open"}
    if len(positions) + len(pending_buys) >= int(config["max_positions"]):
        return {"status": "REJECTED", "reason": "Maximum open positions reached"}
    if day_pct <= -float(config["max_daily_loss_pct"]):
        return {"status": "REJECTED", "reason": "Daily loss cap reached"}
    if weekly_buy_count(trade_rows, utc_now()) >= int(config["max_weekly_buys"]):
        return {"status": "REJECTED", "reason": "Weekly buy cap reached"}

    asset = alpaca.asset(symbol)
    if asset.get("class") != "us_equity" or not asset.get("tradable"):
        return {"status": "REJECTED", "reason": "Only tradable US equities and ETFs are allowed"}
    price = alpaca.latest_price(symbol)
    if price < float(config["min_price"]):
        return {"status": "REJECTED", "reason": "Ticker is below the minimum price"}
    stop_pct = float(config["hard_stop_pct"]) / 100
    max_position_dollars = equity * float(config["max_position_pct"]) / 100
    max_risk_dollars = equity * float(config["max_trade_risk_pct"]) / 100
    qty_by_size = int(max_position_dollars // price)
    qty_by_risk = int(max_risk_dollars // (price * stop_pct))
    qty_by_cash = int(float(account.get("cash", 0)) // price)
    qty = max(0, min(qty_by_size, qty_by_risk, qty_by_cash))
    if qty < 1:
        return {"status": "REJECTED", "reason": "Risk-sized quantity is below one share"}
    stop_price = round(price * (1 - stop_pct), 2)
    order = alpaca.submit_buy(symbol, qty, stop_price)
    return {
        "status": "SUBMITTED", "reason": "Passed deterministic risk checks",
        "price_checked": price, "qty": qty, "stop_price": stop_price, "order": order,
    }


def normalized_positions(snapshot: dict) -> list[dict]:
    result = []
    for p in snapshot.get("positions", []):
        result.append({
            "symbol": p.get("symbol"),
            "qty": float(p.get("qty", 0)),
            "avg_cost": float(p.get("avg_entry_price", 0)),
            "current": float(p.get("current_price", 0)),
            "pl_pct": float(p.get("unrealized_plpc", 0)) * 100,
        })
    return result


def update_state(routine: str, snapshot: dict, record: dict, config: dict,
                 benchmark_price: float | None) -> None:
    previous = load_json(STATE_PATH, {})
    account = snapshot.get("account", {})
    equity = float(account.get("equity", 0))
    cash = float(account.get("cash", 0))
    last_equity = float(account.get("last_equity", equity or 1))
    start = float(config["starting_capital"])
    benchmark_baseline = previous.get("spy_baseline_price") or benchmark_price
    spy_return = None
    if benchmark_price and benchmark_baseline:
        spy_return = ((benchmark_price / float(benchmark_baseline)) - 1) * 100
    portfolio_return = ((equity / start) - 1) * 100 if start else None
    decisions = [record] + previous.get("recent_decisions", [])
    trades = read_jsonl(TRADE_LOG, 10)
    state = {
        "last_update": utc_now().astimezone(NY).strftime("%Y-%m-%d %H:%M ET"),
        "last_routine": routine,
        "status": record["execution"]["status"],
        "mode": "paper",
        "model": os.environ.get("ASTRA_MODEL", config["model"]),
        "equity": round(equity, 2),
        "cash": round(cash, 2),
        "day_pl": round(equity - last_equity, 2),
        "day_pl_pct": round(((equity / last_equity) - 1) * 100, 4) if last_equity else None,
        "return_pct": round(portfolio_return, 4) if portfolio_return is not None else None,
        "spy_baseline_price": benchmark_baseline,
        "spy_current_price": benchmark_price,
        "spy_return_pct": round(spy_return, 4) if spy_return is not None else None,
        "alpha_pct": round(portfolio_return - spy_return, 4) if portfolio_return is not None and spy_return is not None else None,
        "positions": normalized_positions(snapshot),
        "recent_decisions": decisions[:12],
        "recent_trades": trades,
    }
    STATE_PATH.parent.mkdir(parents=True, exist_ok=True)
    STATE_PATH.write_text(json.dumps(state, indent=2) + "\n", encoding="utf-8")


def fixture_decision(routine: str) -> dict:
    return {
        "action": "BUY" if routine == "entry-check" else "HOLD",
        "symbol": "MSFT" if routine == "entry-check" else None,
        "confidence": 82,
        "thesis": "Fixture decision for deterministic validation.",
        "contrary_evidence": "Fixture only.",
        "invalidation": "Fixture only.",
        "entry_condition": "Fixture only.",
        "holding_period": "weeks",
        "sources": [],
    }


class FixtureAlpaca:
    def __init__(self, data: dict):
        self.data = data

    def account_snapshot(self):
        return self.data

    def latest_price(self, symbol: str) -> float:
        return float(self.data.get("prices", {}).get(symbol, 100))

    def asset(self, symbol: str) -> dict:
        return {"class": "us_equity", "tradable": True}

    def submit_buy(self, symbol: str, qty: int, stop_price: float) -> dict:
        return {"id": "fixture-buy", "symbol": symbol, "qty": qty, "stop_price": stop_price}

    def close_position(self, symbol: str) -> dict:
        return {"id": "fixture-sell", "symbol": symbol}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--routine", choices=list(ROUTINE_TIMES.values()))
    parser.add_argument("--scheduled", action="store_true")
    parser.add_argument("--fixture", type=Path)
    args = parser.parse_args()
    routine = scheduled_routine() if args.scheduled else args.routine
    if not routine:
        print("No Astra routine is due; exiting without changes.")
        return 0
    config = load_json(CONFIG_PATH, {})
    alpaca = FixtureAlpaca(load_json(args.fixture, {})) if args.fixture else Alpaca()
    snapshot = alpaca.account_snapshot()
    history = read_jsonl(DECISION_LOG, 30)
    decision = fixture_decision(routine) if args.fixture else openai_decision(routine, snapshot, history, config)
    execution = validate_and_execute(decision, snapshot, config, alpaca, routine, read_jsonl(TRADE_LOG, 200))
    try:
        benchmark_price = alpaca.latest_price(config["benchmark"])
    except Exception as exc:
        print(f"Benchmark update skipped safely: {exc}", file=sys.stderr)
        benchmark_price = None
    record = {
        "timestamp": utc_now().isoformat(), "routine": routine,
        "decision": decision, "execution": execution,
    }
    append_jsonl(DECISION_LOG, record)
    if execution.get("status") == "SUBMITTED":
        append_jsonl(TRADE_LOG, {
            "timestamp": record["timestamp"], "side": decision["action"],
            "symbol": decision["symbol"], "qty": execution.get("qty"),
            "order_id": execution.get("order", {}).get("id"), "status": "submitted",
        })
    update_state(routine, snapshot, record, config, benchmark_price)
    print(json.dumps(record, indent=2))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:  # fail closed and make CI output useful
        print(f"Astra halted safely: {exc}", file=sys.stderr)
        raise SystemExit(1)
