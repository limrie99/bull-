#!/usr/bin/env python3
"""Deterministic checks for Astra scheduling, paper-only guardrails, and fixtures."""

from __future__ import annotations

import os
import unittest
from datetime import datetime
from pathlib import Path
from unittest.mock import patch

import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import runner


FIXTURE = Path(__file__).resolve().parent / "fixture.json"


class ScheduledRoutineTests(unittest.TestCase):
    def test_weekend_is_idle(self):
        saturday = datetime(2026, 9, 12, 16, 36, tzinfo=runner.NY)
        self.assertIsNone(runner.scheduled_routine(saturday))

    def test_due_window_includes_github_cron_delay(self):
        # 16:36 UTC on a weekday is 12:36 ET in September — 6 minutes after 12:30.
        due = datetime(2026, 9, 16, 12, 36, tzinfo=runner.NY)
        self.assertEqual(runner.scheduled_routine(due), "portfolio-check")

    def test_closing_decision_survives_37_minute_actions_delay(self):
        # Observed 2026-09-16 19:37 UTC start (15:37 ET) previously missed the 20-minute window.
        delayed = datetime(2026, 9, 16, 15, 37, tzinfo=runner.NY)
        self.assertEqual(runner.scheduled_routine(delayed), "closing-decision")

    def test_risk_shutdown_still_wins_near_1550(self):
        near = datetime(2026, 9, 16, 15, 55, tzinfo=runner.NY)
        self.assertEqual(runner.scheduled_routine(near), "risk-shutdown")

    def test_est_candidate_does_not_double_fire_during_edt(self):
        # 13:00 UTC in September is 9:00 ET — the EST 8:00 candidate must not rematch.
        est_candidate = datetime(2026, 9, 16, 9, 0, tzinfo=runner.NY)
        self.assertIsNone(runner.scheduled_routine(est_candidate))

    def test_off_window_is_idle(self):
        # 11:10 ET is 55 minutes after 10:15 and still before the 12:30 slot.
        idle = datetime(2026, 9, 16, 11, 10, tzinfo=runner.NY)
        self.assertIsNone(runner.scheduled_routine(idle))


class PaperGuardrailTests(unittest.TestCase):
    def test_alpaca_rejects_missing_keys(self):
        with patch.dict(os.environ, {
            "ASTRA_ALPACA_BASE_URL": runner.PAPER_URL,
            "ASTRA_ALPACA_API_KEY": "",
            "ASTRA_ALPACA_SECRET_KEY": "",
        }, clear=False):
            with self.assertRaises(RuntimeError) as ctx:
                runner.Alpaca()
        self.assertIn("ASTRA_ALPACA_API_KEY", str(ctx.exception))

    def test_alpaca_rejects_live_url(self):
        with patch.dict(os.environ, {
            "ASTRA_ALPACA_BASE_URL": "https://api.alpaca.markets",
            "ASTRA_ALPACA_API_KEY": "PKTEST",
            "ASTRA_ALPACA_SECRET_KEY": "secret",
        }, clear=False):
            with self.assertRaises(RuntimeError) as ctx:
                runner.Alpaca()
        self.assertIn("paper-only", str(ctx.exception))

    def test_execution_stays_off_without_flag(self):
        snapshot = runner.load_json(FIXTURE, {})
        decision = runner.fixture_decision("entry-check")
        alpaca = runner.FixtureAlpaca(snapshot)
        with patch.dict(os.environ, {"ASTRA_EXECUTION_ENABLED": ""}, clear=False):
            result = runner.validate_and_execute(
                decision, snapshot, runner.load_json(runner.CONFIG_PATH, {}),
                alpaca, "entry-check", [],
            )
        self.assertEqual(result["status"], "PROPOSED_ONLY")


class FixtureRunTests(unittest.TestCase):
    def test_fixture_entry_check_proposes_only(self):
        snapshot = runner.load_json(FIXTURE, {})
        decision = runner.fixture_decision("entry-check")
        self.assertEqual(decision["action"], "BUY")
        self.assertEqual(decision["symbol"], "MSFT")
        alpaca = runner.FixtureAlpaca(snapshot)
        with patch.dict(os.environ, {"ASTRA_EXECUTION_ENABLED": "true"}, clear=False):
            result = runner.validate_and_execute(
                decision, snapshot, runner.load_json(runner.CONFIG_PATH, {}),
                alpaca, "entry-check", [],
            )
        self.assertEqual(result["status"], "SUBMITTED")
        self.assertEqual(result["qty"], 14)

    def test_fixture_risk_shutdown_blocks_buys(self):
        snapshot = runner.load_json(FIXTURE, {})
        decision = runner.fixture_decision("entry-check")
        alpaca = runner.FixtureAlpaca(snapshot)
        with patch.dict(os.environ, {"ASTRA_EXECUTION_ENABLED": "true"}, clear=False):
            result = runner.validate_and_execute(
                decision, snapshot, runner.load_json(runner.CONFIG_PATH, {}),
                alpaca, "risk-shutdown", [],
            )
        self.assertEqual(result["status"], "REJECTED")
        self.assertIn("risk shutdown", result["reason"].lower())


if __name__ == "__main__":
    unittest.main()
