#!/usr/bin/env python3
"""Decide whether a Bull routine woke at the right New York market time.

Cloud cron is UTC and does not follow daylight saving. A single UTC hour
chosen in the summer rings about an hour early after the clocks fall back
(the 2026-11-04 open ran at 13:36 UTC, which is 7:36 AM Central, not 8:30).
Shifting that one hour would be right in winter and wrong again in March.

Each slot therefore has two UTC alarms, summer and winter. This script is
the one that decides which ring is real, using America/New_York. The Alpaca
clock can veto a holiday or a "close" that is still an hour before the bell.
It cannot promote an early ring into the close: New York time has to agree.

The script does not place orders.
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path
from zoneinfo import ZoneInfo


NY = ZoneInfo("America/New_York")
GRACE_MINUTES = 45
EARLY_WAIT_MINUTES = 75
CLOSE_BELL_TOLERANCE_MINUTES = 20

# Wall-clock slots. Central is one hour earlier year-round; the anchor is New York
# because that is the exchange clock, and both zones change on the same Sunday.
SLOTS = {
    "pre-market": {"hour": 7, "minute": 0, "dows": {0, 1, 2, 3, 4}, "label": "7:00 AM ET / 6:00 AM CT"},
    "market-open": {"hour": 9, "minute": 30, "dows": {0, 1, 2, 3, 4}, "label": "9:30 AM ET / 8:30 AM CT"},
    "midday": {"hour": 13, "minute": 0, "dows": {0, 1, 2, 3, 4}, "label": "1:00 PM ET / 12:00 PM CT"},
    "market-close": {"hour": 16, "minute": 0, "dows": {0, 1, 2, 3, 4}, "label": "4:00 PM ET / 3:00 PM CT"},
    "weekly-review": {"hour": 17, "minute": 0, "dows": {4}, "label": "Friday 5:00 PM ET / 4:00 PM CT"},
}

ROUTINE_FILES = {
    "pre-market": "routines/pre-market.md",
    "market-open": "routines/market-open.md",
    "midday": "routines/midday.md",
    "market-close": "routines/market-close.md",
    "weekly-review": "routines/weekly-review.md",
}


def utc_crons(slot: str) -> dict:
    """Summer (EDT, UTC-4) and winter (EST, UTC-5) cron lines for a UTC-only scheduler."""
    spec = SLOTS[slot]
    dow = "5" if slot == "weekly-review" else "1-5"
    minute = spec["minute"]
    hour = spec["hour"]
    summer = f"{minute} {hour + 4} * * {dow}"
    winter = f"{minute} {hour + 5} * * {dow}"
    return {
        "slot": slot,
        "new_york": spec["label"],
        "summer_utc": summer,
        "winter_utc": winter,
        "do_not_shift_a_single_hour": True,
    }


def parse_now(value: str | None) -> datetime:
    if not value:
        return datetime.now(timezone.utc)
    text = value.strip().replace("Z", "+00:00")
    parsed = datetime.fromisoformat(text)
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc)


def parse_clock_time(value: str | None) -> datetime | None:
    if not value:
        return None
    return parse_now(value)


def timing_status(slot: str, now: datetime) -> dict:
    if slot not in SLOTS:
        raise KeyError(slot)
    spec = SLOTS[slot]
    local = now.astimezone(NY)
    crons = utc_crons(slot)
    base = {
        "slot": slot,
        "now_utc": now.astimezone(timezone.utc).isoformat(),
        "now_new_york": local.strftime("%Y-%m-%d %H:%M %Z"),
        "slot_label": spec["label"],
        "crons": crons,
        "wait_seconds": 0,
    }
    if local.weekday() not in spec["dows"]:
        return {**base, "status": "NOT_DUE", "reason": "This slot does not run on this New York weekday."}
    start = local.replace(hour=spec["hour"], minute=spec["minute"], second=0, microsecond=0)
    delta_min = (local - start).total_seconds() / 60.0
    if 0 <= delta_min <= GRACE_MINUTES:
        return {
            **base,
            "status": "DUE",
            "reason": f"America/New_York is inside the {spec['label']} window ({delta_min:.0f} min after the bell time).",
            "minutes_from_start": round(delta_min, 2),
        }
    if -EARLY_WAIT_MINUTES <= delta_min < 0:
        wait_seconds = int(round(-delta_min * 60.0)) + 5
        return {
            **base,
            "status": "EARLY",
            "reason": (
                f"This wake is {-delta_min:.0f} minutes before {spec['label']}. "
                "That is the daylight-saving miss: a summer UTC alarm ringing in winter. "
                "Do not treat it as the open or the close. Wait until New York time, "
                "or let the winter UTC alarm run this same check."
            ),
            "minutes_from_start": round(delta_min, 2),
            "wait_seconds": wait_seconds,
        }
    return {
        **base,
        "status": "NOT_DUE",
        "reason": (
            f"America/New_York is {delta_min:.0f} minutes from {spec['label']}, outside the window. "
            "Stand down. Do not trade and do not write this slot's scorecard. "
            "The other season's UTC alarm is supposed to no-op."
        ),
        "minutes_from_start": round(delta_min, 2),
    }


def exchange_allows(slot: str, now: datetime, clock: dict | None) -> tuple[bool, str]:
    """Alpaca's clock can block a holiday or a fake close. It cannot make an early wake due."""
    if not clock:
        return True, "No Alpaca clock supplied. New York time is the slot check."
    is_open = bool(clock.get("is_open"))
    if slot in {"market-open", "midday"}:
        if is_open:
            return True, "Alpaca clock says the market is open."
        nxt = parse_clock_time(clock.get("next_open"))
        if nxt is not None and abs((nxt - now).total_seconds()) <= 5 * 60:
            return True, "The opening bell is within 5 minutes."
        return False, "Alpaca clock says the market is closed (holiday or outside the session). Do not trade."
    if slot == "market-close":
        if not is_open:
            return True, "The bell has rung or there is no session. The scorecard can run."
        nxt = parse_clock_time(clock.get("next_close"))
        if nxt is not None and (nxt - now).total_seconds() > CLOSE_BELL_TOLERANCE_MINUTES * 60:
            return False, (
                "Alpaca clock says the closing bell is still more than 20 minutes away. "
                "This is not the close, even if a UTC alarm rang."
            )
        return True, "The closing bell is at hand."
    if slot == "pre-market" and is_open:
        return False, "Pre-market research runs before the open. The exchange is already open, so this wake is late."
    return True, "Alpaca clock does not block this slot."


def evaluate(slot: str, now: datetime | None = None, clock: dict | None = None) -> dict:
    now = now or datetime.now(timezone.utc)
    result = timing_status(slot, now)
    if result["status"] != "DUE":
        return result
    ok, reason = exchange_allows(slot, now, clock)
    if ok:
        result["exchange"] = reason
        return result
    status = "NOT_DUE" if slot == "market-close" else "HOLIDAY" if slot in {"market-open", "midday"} else "NOT_DUE"
    if slot == "pre-market":
        status = "NOT_DUE"
    return {**result, "status": status, "reason": reason, "exchange": reason}


def claim_slot(path: Path, slot: str, now: datetime, owner: str) -> dict:
    """Record that this New York date's slot is taken. First writer wins."""
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (FileNotFoundError, json.JSONDecodeError):
        data = {}
    if not isinstance(data, dict):
        data = {}
    day = now.astimezone(NY).date().isoformat()
    day_row = data.get(day)
    if not isinstance(day_row, dict):
        day_row = {}
        data[day] = day_row
    if slot in day_row:
        return {"status": "ALREADY_CLAIMED", "date": day, "slot": slot, "existing": day_row[slot]}
    day_row[slot] = {"at": now.astimezone(timezone.utc).isoformat(), "owner": owner}
    cutoff = (now.astimezone(NY).date() - timedelta(days=10)).isoformat()
    data = {key: value for key, value in data.items() if key >= cutoff}
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    return {"status": "CLAIMED", "date": day, "slot": slot, "owner": owner}


def _clock_from_args(args: argparse.Namespace) -> dict | None:
    if args.clock_is_open is None and not args.next_close and not args.next_open:
        return None
    clock = {}
    if args.clock_is_open is not None:
        clock["is_open"] = args.clock_is_open.lower() == "true"
    if args.next_close:
        clock["next_close"] = args.next_close
    if args.next_open:
        clock["next_open"] = args.next_open
    return clock


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="New York market-time gate for Bull routines.")
    parser.add_argument("--slot", required=True, choices=sorted(SLOTS))
    parser.add_argument("--now", help="ISO timestamp. Default: current UTC time.")
    parser.add_argument("--wait", action="store_true", help="If EARLY by at most 75 minutes, sleep until the slot.")
    parser.add_argument("--clock-is-open", choices=["true", "false"])
    parser.add_argument("--next-close")
    parser.add_argument("--next-open")
    parser.add_argument("--claim", action="store_true", help="Claim today's slot in memory/slot-stamp.json.")
    parser.add_argument("--stamp", default="memory/slot-stamp.json")
    parser.add_argument("--owner", default="bull")
    parser.add_argument("--print-crons", action="store_true", help="Print the summer and winter UTC crons and exit.")
    args = parser.parse_args(argv)
    if args.print_crons:
        json.dump(utc_crons(args.slot), sys.stdout, indent=2)
        sys.stdout.write("\n")
        return 0

    now = parse_now(args.now)
    clock = _clock_from_args(args)
    result = evaluate(args.slot, now, clock)
    if args.wait and result["status"] == "EARLY":
        time.sleep(int(result["wait_seconds"]))
        now = datetime.now(timezone.utc) if args.now is None else now + timedelta(seconds=int(result["wait_seconds"]))
        result = evaluate(args.slot, now, clock)
        result["waited"] = True
    if args.claim:
        if result["status"] != "DUE":
            result["claim"] = {"status": "NOT_CLAIMED", "reason": "Only a due slot can be claimed."}
        else:
            result["claim"] = claim_slot(Path(args.stamp), args.slot, now, args.owner)
            if result["claim"]["status"] == "ALREADY_CLAIMED":
                result["status"] = "NOT_DUE"
                result["reason"] = "Another wake already claimed this slot today. Stand down so the book is not traded twice."
    json.dump(result, sys.stdout, indent=2)
    sys.stdout.write("\n")
    return {"DUE": 0, "HOLIDAY": 2, "NOT_DUE": 3, "EARLY": 4}[result["status"]]


if __name__ == "__main__":
    raise SystemExit(main())
