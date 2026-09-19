#!/usr/bin/env python3
"""Run one independent ChatGPT Astra paper-trading committee check."""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path
from zoneinfo import ZoneInfo


ROOT = Path(__file__).resolve().parent
CONFIG_PATH = ROOT / "config.json"
PROMPT_PATH = ROOT / "prompt.md"
VOICES_PATH = ROOT / "voices.json"
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
        "invalidation", "entry_condition", "holding_period", "committee_notes", "sources",
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
        "committee_notes": {"type": "string"},
        "sources": {"type": "array", "items": {"type": "string"}, "maxItems": 8},
    },
}

VOICE_STANCES = ("BUY", "SELL", "HOLD", "WATCH", "BLOCK")

VOICE_SCHEMA = {
    "type": "object",
    "additionalProperties": False,
    "required": ["stance", "conviction", "symbols", "argument", "evidence", "risk_flags", "sources"],
    "properties": {
        "stance": {"type": "string", "enum": list(VOICE_STANCES)},
        "conviction": {"type": "integer", "minimum": 0, "maximum": 100},
        "symbols": {"type": "array", "items": {"type": "string"}, "maxItems": 3},
        "argument": {"type": "string"},
        "evidence": {"type": "array", "items": {"type": "string"}, "maxItems": 5},
        "risk_flags": {"type": "array", "items": {"type": "string"}, "maxItems": 5},
        "sources": {"type": "array", "items": {"type": "string"}, "maxItems": 5},
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


def openai_json(*, model: str, instructions: str, input_text: str, schema_name: str,
                schema: dict, effort: str, web_search: bool = True, timeout: int = 300) -> dict:
    api_key = os.environ.get("OPENAI_API_KEY", "")
    if not api_key:
        raise RuntimeError("Missing OPENAI_API_KEY")
    body = {
        "model": model,
        "reasoning": {"effort": effort},
        "tools": [{"type": "web_search"}] if web_search else [],
        "instructions": instructions,
        "input": input_text,
        "text": {
            "format": {
                "type": "json_schema",
                "name": schema_name,
                "strict": True,
                "schema": schema,
            }
        },
    }
    response = request_json(
        "https://api.openai.com/v1/responses",
        headers={"Authorization": f"Bearer {api_key}"},
        method="POST", body=body, timeout=timeout,
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
        raise RuntimeError("OpenAI response contained no text")
    return json.loads(text)


def chair_model(config: dict) -> str:
    return os.environ.get("ASTRA_MODEL") or config.get("model", "")


def voice_model(config: dict) -> str:
    return os.environ.get("ASTRA_VOICE_MODEL") or chair_model(config)


def committee_enabled(voices: dict) -> bool:
    flag = os.environ.get("ASTRA_VOICES_ENABLED", "").strip().lower()
    if flag in {"false", "0", "no", "off"}:
        return False
    if flag in {"true", "1", "yes", "on"}:
        return True
    return bool(voices.get("enabled", True))


def roster_for_routine(voices: dict, routine: str) -> list[dict]:
    return [v for v in voices.get("voices", []) if routine in v.get("routines", [])]


def voice_instructions(voice: dict, voices: dict) -> str:
    bench = voice.get("bench", "")
    return "\n\n".join(filter(None, [
        voices.get("preamble", ""),
        f"Your bench: {bench}. {voices.get('benches', {}).get(bench, '')}",
        f"You are {voice.get('name', voice.get('id', 'a voice'))}. {voice.get('mandate', '')}",
        "Answer only as this voice. Set conviction to how strongly your own lane supports your stance, "
        "not to how certain you are that the trade will work.",
    ]))


def account_metrics(snapshot: dict) -> dict:
    account = snapshot.get("account", {})
    equity = float(account.get("equity", 0) or 0)
    cash = float(account.get("cash", 0) or 0)
    last_equity = float(account.get("last_equity", equity) or equity or 1)
    return {
        "equity": equity,
        "cash": cash,
        "last_equity": last_equity,
        "day_pct": ((equity / last_equity) - 1) * 100 if last_equity else 0.0,
    }


def committee_context(routine: str, snapshot: dict, history: list[dict], config: dict) -> dict:
    metrics = account_metrics(snapshot)
    return {
        "routine": routine,
        "timestamp_utc": utc_now().isoformat(),
        "market_open": bool(snapshot.get("clock", {}).get("is_open")),
        "equity": round(metrics["equity"], 2),
        "cash": round(metrics["cash"], 2),
        "day_change_pct": round(metrics["day_pct"], 2),
        "positions": normalized_positions(snapshot),
        "open_buy_orders": sorted({
            (o.get("symbol") or "").upper() for o in snapshot.get("open_orders", [])
            if o.get("side") == "buy"
        }),
        "risk_rules": config,
        "astra_prior_decisions": [
            {
                "routine": row.get("routine"),
                "action": (row.get("decision") or {}).get("action"),
                "symbol": (row.get("decision") or {}).get("symbol"),
            }
            for row in history[-5:]
        ],
    }


def voice_record(voice: dict, payload: dict) -> dict:
    stance = str(payload.get("stance", "HOLD")).upper()
    conviction = int(payload.get("conviction", 0) or 0)
    return {
        "id": voice.get("id"),
        "name": voice.get("name", voice.get("id")),
        "bench": voice.get("bench"),
        "status": "ok",
        "stance": stance if stance in VOICE_STANCES else "HOLD",
        "conviction": max(0, min(100, conviction)),
        "symbols": [str(s).upper().strip() for s in payload.get("symbols", []) if str(s).strip()],
        "argument": payload.get("argument", ""),
        "evidence": payload.get("evidence", []),
        "risk_flags": payload.get("risk_flags", []),
        "sources": payload.get("sources", []),
    }


def failed_voice_record(voice: dict, error: str) -> dict:
    return {
        "id": voice.get("id"),
        "name": voice.get("name", voice.get("id")),
        "bench": voice.get("bench"),
        "status": "error",
        "error": error[:400],
        "stance": "ABSTAIN",
        "conviction": 0,
        "symbols": [],
        "argument": "",
        "evidence": [],
        "risk_flags": [],
        "sources": [],
    }


def call_voice(voice: dict, voices: dict, context: dict, config: dict, prior: list[dict]) -> dict:
    payload = dict(context)
    if prior:
        payload["committee_so_far"] = transcript(prior)
    return openai_json(
        model=voice.get("model") or voice_model(config),
        instructions=voice_instructions(voice, voices),
        input_text="Research what your mandate needs, then answer for this routine.\n\n" + json.dumps(payload),
        schema_name="astra_committee_voice",
        schema=VOICE_SCHEMA,
        effort=voice.get("reasoning_effort", "medium"),
        web_search=bool(voice.get("web_search", True)),
        timeout=int(voice.get("timeout_seconds", 240)),
    )


def transcript(records: list[dict]) -> list[dict]:
    rows = []
    for record in records:
        if record.get("status") != "ok":
            continue
        rows.append({
            "voice": record["name"],
            "bench": record["bench"],
            "stance": record["stance"],
            "conviction": record["conviction"],
            "symbols": record["symbols"],
            "argument": record["argument"],
            "evidence": record["evidence"],
            "risk_flags": record["risk_flags"],
        })
    return rows


def run_wave(wave: list[dict], voices: dict, context: dict, config: dict, prior: list[dict]) -> list[dict]:
    results: list[dict | None] = [None] * len(wave)
    workers = min(max(1, int(voices.get("max_parallel", 4))), len(wave))
    with ThreadPoolExecutor(max_workers=workers) as pool:
        futures = {pool.submit(call_voice, voice, voices, context, config, prior): i
                   for i, voice in enumerate(wave)}
        for future in as_completed(futures):
            index = futures[future]
            try:
                results[index] = voice_record(wave[index], future.result())
            except Exception as exc:  # one silent voice must not cancel the routine
                print(f"Voice {wave[index].get('id')} failed: {exc}", file=sys.stderr)
                results[index] = failed_voice_record(wave[index], str(exc))
    return [r for r in results if r]


def committee_record(routine: str, records: list[dict], voices: dict, model: str) -> dict:
    return {
        "enabled": True,
        "routine": routine,
        "voice_model": model,
        "min_buyer_support": int(voices.get("min_buyer_support", 1)),
        "skeptic_veto_conviction": int(voices.get("skeptic_veto_conviction", 85)),
        "voices": records,
    }


def run_committee(routine: str, snapshot: dict, history: list[dict], config: dict,
                  voices: dict | None = None) -> dict | None:
    """Poll the research, buy and skeptic benches. Researchers speak first so the
    other benches argue over the same evidence."""
    voices = load_json(VOICES_PATH, {}) if voices is None else voices
    if not committee_enabled(voices):
        return None
    roster = roster_for_routine(voices, routine)
    if not roster:
        return None
    context = committee_context(routine, snapshot, history, config)
    researchers = [v for v in roster if v.get("bench") == "researchers"]
    deciders = [v for v in roster if v.get("bench") != "researchers"]
    records: list[dict] = []
    for wave in (researchers, deciders):
        if wave:
            records.extend(run_wave(wave, voices, context, config, records))
    return committee_record(routine, records, voices, voice_model(config))


def committee_summary(committee: dict | None) -> dict | None:
    if not committee:
        return None
    return {
        "routine": committee.get("routine"),
        "voice_model": committee.get("voice_model"),
        "voices": [
            {
                "name": v["name"],
                "bench": v["bench"],
                "stance": v["stance"],
                "conviction": v["conviction"],
                "symbols": v["symbols"],
                "argument": v.get("argument", "")[:400],
                "status": v["status"],
            }
            for v in committee.get("voices", [])
        ],
    }


def committee_buy_gate(committee: dict, symbol: str) -> dict | None:
    """Deterministic committee rules. The chair proposes; these lines refuse."""
    heard = [v for v in committee.get("voices", []) if v.get("status") == "ok"]
    buyers = [v for v in heard if v.get("bench") == "buyers"]
    skeptics = [v for v in heard if v.get("bench") == "skeptics"]
    if not skeptics:
        return {"status": "REJECTED", "reason": "No skeptic voice was available to challenge this buy"}
    floor = int(committee.get("skeptic_veto_conviction", 85))
    for voice in skeptics:
        if voice["stance"] != "BLOCK" or voice["conviction"] < floor:
            continue
        if not voice["symbols"] or symbol in voice["symbols"]:
            return {
                "status": "REJECTED",
                "reason": f"{voice['name']} vetoed this buy at conviction {voice['conviction']}",
            }
    if not buyers:
        return {"status": "REJECTED", "reason": "The buy bench does not sit in this routine"}
    required = int(committee.get("min_buyer_support", 1))
    support = [v["name"] for v in buyers if v["stance"] == "BUY" and symbol in v["symbols"]]
    if len(support) < required:
        return {
            "status": "REJECTED",
            "reason": f"Only {len(support)} of {required} required buyer voices backed {symbol}",
        }
    return None


def openai_decision(routine: str, snapshot: dict, history: list[dict], config: dict,
                    committee: dict | None = None) -> dict:
    context = {
        "routine": routine,
        "timestamp_utc": utc_now().isoformat(),
        "risk_rules": config,
        "account": snapshot,
        "astra_prior_decisions": [
            {"timestamp": row.get("timestamp"), "routine": row.get("routine"),
             "decision": row.get("decision"), "execution_status": (row.get("execution") or {}).get("status")}
            for row in history[-12:]
        ],
        "committee": {
            "voices": transcript(committee.get("voices", [])) if committee else [],
            "silent_voices": [v["name"] for v in (committee or {}).get("voices", [])
                              if v.get("status") != "ok"],
            "min_buyer_support": (committee or {}).get("min_buyer_support"),
            "skeptic_veto_conviction": (committee or {}).get("skeptic_veto_conviction"),
        },
    }
    return openai_json(
        model=chair_model(config),
        instructions=PROMPT_PATH.read_text(encoding="utf-8"),
        input_text="Read your committee, research anything still missing, then make this routine's decision.\n\n"
                   + json.dumps(context),
        schema_name="astra_trade_decision",
        schema=DECISION_SCHEMA,
        effort=config.get("reasoning_effort", "high"),
    )


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
                         routine: str, trade_rows: list[dict],
                         committee: dict | None = None) -> dict:
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
    if committee and committee.get("enabled"):
        blocked = committee_buy_gate(committee, symbol)
        if blocked:
            return blocked
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


def state_decision(record: dict) -> dict:
    """Keep the dashboard copy of a decision small: summarized voices, no raw evidence."""
    trimmed = {key: value for key, value in record.items() if key != "committee"}
    summary = committee_summary(record.get("committee"))
    if summary:
        trimmed["committee"] = summary
    return trimmed


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
    decisions = [state_decision(record)] + previous.get("recent_decisions", [])
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
        "committee": committee_summary(record.get("committee")),
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
        "committee_notes": "Fixture only.",
        "sources": [],
    }


FIXTURE_STANCES = {
    "researchers": {"stance": "WATCH", "conviction": 60},
    "buyers": {"stance": "BUY", "conviction": 80},
    "skeptics": {"stance": "HOLD", "conviction": 45},
}


def fixture_committee(routine: str, voices: dict | None = None) -> dict | None:
    voices = load_json(VOICES_PATH, {}) if voices is None else voices
    if not committee_enabled(voices):
        return None
    roster = roster_for_routine(voices, routine)
    if not roster:
        return None
    records = []
    for voice in roster:
        stance = FIXTURE_STANCES.get(voice.get("bench", ""), {"stance": "HOLD", "conviction": 50})
        records.append(voice_record(voice, {
            **stance,
            "symbols": ["MSFT"],
            "argument": f"Fixture argument from {voice.get('name')}.",
            "evidence": [],
            "risk_flags": [],
            "sources": [],
        }))
    return committee_record(routine, records, voices, "fixture")


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
    if args.fixture:
        committee = fixture_committee(routine)
        decision = fixture_decision(routine)
    else:
        committee = run_committee(routine, snapshot, history, config)
        decision = openai_decision(routine, snapshot, history, config, committee)
    execution = validate_and_execute(
        decision, snapshot, config, alpaca, routine, read_jsonl(TRADE_LOG, 200), committee,
    )
    try:
        benchmark_price = alpaca.latest_price(config["benchmark"])
    except Exception as exc:
        print(f"Benchmark update skipped safely: {exc}", file=sys.stderr)
        benchmark_price = None
    record = {
        "timestamp": utc_now().isoformat(), "routine": routine,
        "decision": decision, "execution": execution, "committee": committee,
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
