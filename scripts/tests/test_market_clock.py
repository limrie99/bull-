#!/usr/bin/env python3
"""Daylight saving must not make the open or the close look due an hour early."""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import market_clock


ROOT = Path(__file__).resolve().parents[2]


def at(iso: str) -> datetime:
    return market_clock.parse_now(iso)


class MarketClockTests(unittest.TestCase):
    def test_winter_open_alarm_that_actually_fired_is_early(self):
        # 2026-11-04 13:36 UTC is 8:36 AM ET / 7:36 AM CT. The open is 9:30 ET.
        result = market_clock.evaluate("market-open", at("2026-11-04T13:36:00Z"))
        self.assertEqual(result["status"], "EARLY")
        self.assertGreater(result["wait_seconds"], 50 * 60)
        self.assertLess(result["wait_seconds"], 60 * 60)

    def test_winter_open_at_the_real_bell_is_due(self):
        result = market_clock.evaluate("market-open", at("2026-11-04T14:30:00Z"))
        self.assertEqual(result["status"], "DUE")

    def test_summer_open_uses_the_other_utc_hour(self):
        summer = market_clock.evaluate("market-open", at("2026-07-15T13:30:00Z"))
        self.assertEqual(summer["status"], "DUE")
        # The winter alarm must not also run the open in July.
        late = market_clock.evaluate("market-open", at("2026-07-15T14:30:00Z"))
        self.assertEqual(late["status"], "NOT_DUE")

    def test_today_close_was_not_the_close(self):
        # Commit market-close 2026-11-04 20:06 UTC, book marked ~20:03 UTC / 3:03 PM ET.
        early = market_clock.evaluate("market-close", at("2026-11-04T20:03:00Z"), {
            "is_open": True,
            "next_close": "2026-11-04T21:00:00Z",
        })
        self.assertEqual(early["status"], "EARLY")
        real = market_clock.evaluate("market-close", at("2026-11-04T21:00:00Z"), {
            "is_open": False,
            "next_close": "2026-11-05T21:00:00Z",
        })
        self.assertEqual(real["status"], "DUE")

    def test_exchange_clock_cannot_promote_an_early_close(self):
        # Even if a caller ignored EARLY, an open market with the bell an hour
        # away is not the close.
        allowed, reason = market_clock.exchange_allows("market-close", at("2026-11-04T20:03:00Z"), {
            "is_open": True,
            "next_close": "2026-11-04T21:00:00Z",
        })
        self.assertFalse(allowed)
        self.assertIn("closing bell", reason)

    def test_summer_close_and_its_winter_alarm(self):
        self.assertEqual(market_clock.evaluate("market-close", at("2026-07-15T20:00:00Z"))["status"], "DUE")
        self.assertEqual(market_clock.evaluate("market-close", at("2026-07-15T21:00:00Z"))["status"], "NOT_DUE")

    def test_premarket_and_midday_follow_new_york(self):
        self.assertEqual(market_clock.evaluate("pre-market", at("2026-11-04T11:13:00Z"))["status"], "EARLY")
        self.assertEqual(market_clock.evaluate("pre-market", at("2026-11-04T12:00:00Z"))["status"], "DUE")
        self.assertEqual(market_clock.evaluate("pre-market", at("2026-07-15T11:00:00Z"))["status"], "DUE")
        self.assertEqual(market_clock.evaluate("midday", at("2026-11-04T17:08:00Z"))["status"], "EARLY")
        self.assertEqual(market_clock.evaluate("midday", at("2026-11-04T18:00:00Z"))["status"], "DUE")
        self.assertEqual(market_clock.evaluate("midday", at("2026-07-15T17:00:00Z"))["status"], "DUE")

    def test_weekly_review_is_friday_new_york_evening(self):
        self.assertEqual(market_clock.evaluate("weekly-review", at("2026-11-06T21:00:00Z"))["status"], "EARLY")
        self.assertEqual(market_clock.evaluate("weekly-review", at("2026-11-06T22:00:00Z"))["status"], "DUE")
        self.assertEqual(market_clock.evaluate("weekly-review", at("2026-07-17T21:00:00Z"))["status"], "DUE")
        # Thursday evening is not the Friday review.
        self.assertEqual(market_clock.evaluate("weekly-review", at("2026-11-05T22:00:00Z"))["status"], "NOT_DUE")

    def test_weekend_is_idle(self):
        self.assertEqual(market_clock.evaluate("market-open", at("2026-11-07T14:30:00Z"))["status"], "NOT_DUE")

    def test_holiday_open_does_not_trade(self):
        result = market_clock.evaluate("market-open", at("2026-11-04T14:30:00Z"), {
            "is_open": False,
            "next_open": "2026-11-05T14:30:00Z",
        })
        self.assertEqual(result["status"], "HOLIDAY")

    def test_crons_are_summer_and_winter_not_a_one_hour_edit(self):
        crons = market_clock.utc_crons("market-open")
        self.assertEqual(crons["summer_utc"], "30 13 * * 1-5")
        self.assertEqual(crons["winter_utc"], "30 14 * * 1-5")
        close = market_clock.utc_crons("market-close")
        self.assertEqual(close["summer_utc"], "0 20 * * 1-5")
        self.assertEqual(close["winter_utc"], "0 21 * * 1-5")

    def test_routine_files_publish_both_utc_crons(self):
        clocks = (ROOT / "routines" / "CLOCKS.md").read_text(encoding="utf-8")
        for slot, filename in market_clock.ROUTINE_FILES.items():
            text = (ROOT / filename).read_text(encoding="utf-8")
            crons = market_clock.utc_crons(slot)
            self.assertIn(crons["summer_utc"], text)
            self.assertIn(crons["winter_utc"], text)
            self.assertIn(crons["summer_utc"], clocks)
            self.assertIn(crons["winter_utc"], clocks)

    def test_cli_exit_code_for_the_early_close(self):
        completed = subprocess.run(
            [
                sys.executable, str(ROOT / "scripts" / "market_clock.py"),
                "--slot", "market-close", "--now", "2026-11-04T20:03:00Z",
                "--clock-is-open", "true", "--next-close", "2026-11-04T21:00:00Z",
            ],
            capture_output=True, text=True,
        )
        self.assertEqual(completed.returncode, 4)
        self.assertEqual(json.loads(completed.stdout)["status"], "EARLY")

    def test_claim_lets_the_first_wake_win(self):
        with tempfile.TemporaryDirectory() as tmp:
            stamp = Path(tmp) / "slot-stamp.json"
            now = at("2026-11-04T14:30:00Z")
            first = market_clock.claim_slot(stamp, "market-open", now, "early-sleeper")
            second = market_clock.claim_slot(stamp, "market-open", now, "winter-alarm")
            self.assertEqual(first["status"], "CLAIMED")
            self.assertEqual(second["status"], "ALREADY_CLAIMED")


if __name__ == "__main__":
    unittest.main()
