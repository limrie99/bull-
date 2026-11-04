#!/usr/bin/env python3
"""Dry-run the same-day SPY sweep against the 2026-11-04 book."""

from __future__ import annotations

import json
import subprocess
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import spy_floor


ROOT = Path(__file__).resolve().parents[2]
FIXTURE = Path(__file__).resolve().parents[1] / "fixtures" / "2026-11-04.json"


class TodaySweepTests(unittest.TestCase):
    def setUp(self):
        self.snapshot = json.loads(FIXTURE.read_text(encoding="utf-8"))

    def test_about_22k_cash_buys_about_12k_of_spy(self):
        plan = spy_floor.plan_from_snapshot(self.snapshot)
        self.assertEqual(plan["action"], "buy")
        self.assertEqual(plan["symbol"], "SPY")
        self.assertEqual(plan["qty"], 15)
        self.assertGreaterEqual(plan["estimated_dollars"], 11_000)
        self.assertLessEqual(plan["estimated_dollars"], 12_500)
        self.assertAlmostEqual(plan["estimated_dollars"], 11_514.15, places=2)
        self.assertGreaterEqual(plan["cash_after"], 10_000)
        self.assertLess(plan["cash_after"], 11_000)
        self.assertAlmostEqual(plan["cash_after"], 10_482.86, places=2)
        self.assertEqual(plan["buffer"], 10_000)
        self.assertFalse(plan["counts_against_weekly_buy_cap"])
        self.assertEqual(plan["order"]["type"], "market")
        self.assertEqual(plan["order"]["time_in_force"], "day")
        self.assertEqual(plan["order"]["side"], "buy")
        self.assertIsNone(plan["order"]["stop"])
        self.assertAlmostEqual(plan["spy_target_dollars"], 48_842.88, places=2)
        self.assertGreater(plan["spy_target_pct"], 45)
        self.assertLess(plan["spy_target_pct"], 55)

    def test_cli_dry_run_matches_the_function(self):
        completed = subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "spy_floor.py"), "--fixture", str(FIXTURE)],
            check=True, capture_output=True, text=True,
        )
        plan = json.loads(completed.stdout)
        self.assertEqual(plan["qty"], 15)
        self.assertEqual(plan["action"], "buy")
        self.assertFalse(plan["counts_against_weekly_buy_cap"])

    def test_stock_buy_in_the_same_run_does_not_also_sweep(self):
        snapshot = dict(self.snapshot, qualifying_stock_buy_dollars=9_000)
        plan = spy_floor.plan_from_snapshot(snapshot)
        self.assertEqual(plan["action"], "none")
        self.assertEqual(plan["qty"], 0)

    def test_stock_buy_that_would_break_the_cushion_trims_spy(self):
        snapshot = dict(self.snapshot, qualifying_stock_buy_dollars=15_000)
        plan = spy_floor.plan_from_snapshot(snapshot)
        self.assertEqual(plan["action"], "trim")
        self.assertEqual(plan["order"]["side"], "sell")
        self.assertIsNone(plan["order"]["stop"])
        self.assertFalse(plan["counts_against_weekly_buy_cap"])
        self.assertGreaterEqual(plan["cash_after"], 10_000)
        self.assertGreaterEqual(plan["qty"], 1)

    def test_daily_loss_cap_blocks_the_sweep(self):
        snapshot = dict(self.snapshot, daily_loss_cap_hit=True)
        plan = spy_floor.plan_from_snapshot(snapshot)
        self.assertEqual(plan["action"], "none")

    def test_live_mode_is_refused(self):
        snapshot = dict(self.snapshot, mode="live")
        plan = spy_floor.plan_from_snapshot(snapshot)
        self.assertEqual(plan["action"], "none")
        self.assertIn("Paper", plan["reason"])

    def test_cash_already_at_the_cushion_buys_nothing(self):
        plan = spy_floor.plan_spy_floor(
            equity=100_000, cash=10_400, spy_price=700, spy_shares_held=80,
            stock_market_value=9_000,
        )
        self.assertEqual(plan["action"], "none")
        self.assertEqual(plan["qty"], 0)

    def test_buffer_never_drops_below_ten_percent_when_the_book_is_larger(self):
        self.assertEqual(spy_floor.cash_buffer(98_638.47), 10_000)
        self.assertEqual(spy_floor.cash_buffer(200_000), 20_000)


if __name__ == "__main__":
    unittest.main()
