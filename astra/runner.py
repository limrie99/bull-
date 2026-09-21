#!/usr/bin/env python3
"""Run one GPT-6 Astra research check and hand a proposal to Bull and Maverick."""

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
REPO_ROOT = ROOT.parent
CONFIG_PATH = ROOT / "config.json"
PROMPT_PATH = ROOT / "prompt.md"
DECISION_LOG = ROOT / "memory" / "decision-log.jsonl"
TRADE_LOG = ROOT / "memory" / "trade-log.jsonl"
PROPOSAL_LOG = ROOT / "memory" / "proposals.jsonl"
PROPOSALS_PATH = REPO_ROOT / "memory" / "astra-proposals.md"
STATE_PATH = ROOT / "dashboard" / "state.json"
NY = ZoneInfo("America/New_York")
PAPER_URL = "https://paper-api.alpaca.markets"

# Alpaca paper credentials, in precedence order. Dedicated Astra keys win when they
# exist; otherwise Astra borrows Bull's keys, which forces helper mode because both
# agents would then be looking at — and able to disturb — the same paper account.
CREDENTIAL_SOURCES = (
    ("dedicated", "ASTRA_ALPACA_API_KEY", "ASTRA_ALPACA_SECRET_KEY"),
    ("shared-bull", "ALPACA_API_KEY", "ALPACA_SECRET_KEY"),
    ("shared-bull", "APCA_API_KEY_ID", "APCA_API_SECRET_KEY"),
)

SHARED_ACCOUNT_REASON = (
    "Helper mode: Astra is reading Bull's shared paper account, so it proposes "
    "only and never places an order Bull did not authorize"
)

MAX_PROPOSAL_BLOCKS = 40

# Bull's files Astra reads (read-only) so its proposals fit the book Bull actually
# holds. Both are long-lived logs, so each is truncated to the current section.
TEAMMATE_FILES = (
    ("bull_portfolio", "portfolio.md", 8000),
    ("bull_watchlist", "watchlist.md", 8000),
)

ROUTINE_TIMES = {
    (8, 0): "premarket-research",
    (9, 25): "opening-plan",
    (10, 15): "entry-check",
    (12, 30): "portfolio-check",
    (15, 0): "closing-decision",
    (15, 50): "risk-shutdown",
}

# GitHub Actions cron is UTC-only and often starts 5–40 minutes late.
# Keep this under 50 minutes so the 15:00 and 15:50 ET slots cannot collide,
# and under 60 minutes so the EDT/EST candidate crons cannot double-fire.
SCHEDULE_GRACE_MINUTES = 45

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


def resolve_alpaca_credentials(env=None) -> tuple[str, str, str, str]:
    """Return (source, key, secret, key_var_name) for the first complete pair found."""
    env = os.environ if env is None else env
    for source, key_var, secret_var in CREDENTIAL_SOURCES:
        key = env.get(key_var, "").strip()
        secret = env.get(secret_var, "").strip()
        if key and secret:
            return source, key, secret, key_var
    return "", "", "", ""


class Alpaca:
    def __init__(self):
        # Never read Bull's ALPACA_BASE_URL — it may point at the live endpoint.
        self.base = os.environ.get("ASTRA_ALPACA_BASE_URL", PAPER_URL).rstrip("/")
        self.credential_source, self.key, self.secret, self.key_var = resolve_alpaca_credentials()
        if self.base != PAPER_URL:
            raise RuntimeError("Astra is paper-only; ASTRA_ALPACA_BASE_URL must be the Alpaca paper URL")
        if not self.credential_source:
            accepted = ", ".join(f"{k}/{s}" for _, k, s in CREDENTIAL_SOURCES)
            raise RuntimeError(f"Missing Alpaca paper credentials; set one pair of {accepted}")
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
    best_name = None
    best_delta = None
    for (hour, minute), name in ROUTINE_TIMES.items():
        start = local.replace(hour=hour, minute=minute, second=0, microsecond=0)
        delta_min = (local - start).total_seconds() / 60.0
        if 0 <= delta_min <= SCHEDULE_GRACE_MINUTES:
            if best_delta is None or delta_min < best_delta:
                best_name = name
                best_delta = delta_min
    return best_name


def teammate_context() -> dict:
    """Bounded read of Bull's current book and bench. Never blocks a run."""
    context = {}
    for name, filename, limit in TEAMMATE_FILES:
        try:
            text = (REPO_ROOT / "memory" / filename).read_text(encoding="utf-8")
        except OSError:
            continue
        context[name] = text[:limit]
    return context


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
        "bull_context": teammate_context(),
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
    if getattr(alpaca, "credential_source", "dedicated") == "shared-bull":
        return {"status": "PROPOSED_ONLY", "reason": SHARED_ACCOUNT_REASON}
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


PROPOSALS_HEADER = """# Astra proposals — research handoff to Bull and Maverick

Astra is Bull's research helper, not a rival book. Every entry below is a **proposal**:
Astra scored an idea and wrote it down. Nothing here is an order, and Astra does not
place orders on Bull's account.

- **Bull** reads this file at the start of pre-market, market-open, and midday. A proposal
  is one more research input — it must still clear Bull's own buy-gate (2+ buy signals AND
  Conviction >= 70) and Bull's Trader voice sizes and places anything it accepts.
- **Maverick** (`limrie99/maverick`, `limrie99/maverick-aggressive`) consumes the same
  blocks by hand or by bot — see `astra/handoff-maverick.md` for the copy-paste template.
- Newest on top. Written by `astra/runner.py`; the machine-readable mirror is
  `astra/memory/proposals.jsonl`. Paper only.

"""


def proposal_block(record: dict, credential_source: str) -> str:
    decision = record["decision"]
    execution = record["execution"]
    stamp = datetime.fromisoformat(record["timestamp"]).astimezone(NY).strftime("%Y-%m-%d %H:%M ET")
    symbol = decision.get("symbol") or "no ticker"
    sources = ", ".join(decision.get("sources") or []) or "none recorded"
    account = "Bull's shared paper account" if credential_source == "shared-bull" else "Astra's own paper account"
    lines = [
        f"## {stamp} · {record['routine']} · {decision.get('action')} {symbol} · confidence {decision.get('confidence')}",
        "",
        f"- **Status:** {execution.get('status')} — {execution.get('reason')}",
        f"- **Account Astra looked at:** {account}",
        f"- **Thesis:** {decision.get('thesis')}",
        f"- **Strongest counter-argument:** {decision.get('contrary_evidence')}",
        f"- **What would prove it wrong:** {decision.get('invalidation')}",
        f"- **Entry condition:** {decision.get('entry_condition')}",
        f"- **Intended holding period:** {decision.get('holding_period')}",
        f"- **Sources:** {sources}",
        "- **For Bull:** treat as research only. Re-score against Bull's own gate before acting.",
        "- **For Maverick:** copy this block into that repo's inbox if it fits its mandate.",
        "",
    ]
    return "\n".join(lines)


def write_proposal_handoff(record: dict, credential_source: str) -> None:
    """Prepend this run's proposal to the shared file Bull and Maverick read."""
    append_jsonl(PROPOSAL_LOG, {
        "timestamp": record["timestamp"],
        "routine": record["routine"],
        "action": record["decision"].get("action"),
        "symbol": record["decision"].get("symbol"),
        "confidence": record["decision"].get("confidence"),
        "thesis": record["decision"].get("thesis"),
        "invalidation": record["decision"].get("invalidation"),
        "entry_condition": record["decision"].get("entry_condition"),
        "status": record["execution"].get("status"),
        "account": credential_source or "unknown",
    })
    existing = PROPOSALS_PATH.read_text(encoding="utf-8") if PROPOSALS_PATH.exists() else ""
    previous = [b for b in re.split(r"(?m)^(?=## )", existing)[1:] if b.strip()]
    body = proposal_block(record, credential_source) + "\n" + "\n".join(previous[:MAX_PROPOSAL_BLOCKS - 1])
    PROPOSALS_PATH.parent.mkdir(parents=True, exist_ok=True)
    PROPOSALS_PATH.write_text(PROPOSALS_HEADER + body.rstrip() + "\n", encoding="utf-8")


def update_state(routine: str, snapshot: dict, record: dict, config: dict,
                 benchmark_price: float | None, credential_source: str = "") -> None:
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
    shared = credential_source == "shared-bull"
    # On Bull's account the equity is Bull's, so scoring an "Astra return" against
    # Astra's starting capital would invent a rival scorecard. Leave it blank instead.
    portfolio_return = None if shared or not start else ((equity / start) - 1) * 100
    decisions = [record] + previous.get("recent_decisions", [])
    trades = read_jsonl(TRADE_LOG, 10)
    state = {
        "last_update": utc_now().astimezone(NY).strftime("%Y-%m-%d %H:%M ET"),
        "last_routine": routine,
        "status": record["execution"]["status"],
        "mode": "paper",
        "role": config.get("role", "research-helper"),
        "account_scope": "shared-with-bull" if shared else "astra-own",
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
    def __init__(self, data: dict, credential_source: str = "fixture"):
        self.data = data
        self.credential_source = credential_source

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
    credential_source = getattr(alpaca, "credential_source", "")
    update_state(routine, snapshot, record, config, benchmark_price, credential_source)
    if not args.fixture:
        write_proposal_handoff(record, credential_source)
    print(json.dumps(record, indent=2))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:  # fail closed and make CI output useful
        print(f"Astra halted safely: {exc}", file=sys.stderr)
        raise SystemExit(1)
