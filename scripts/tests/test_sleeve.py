#!/usr/bin/env python3
"""Future picks cannot pile more defensive names onto the current book."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import sleeve


# The 2026-11-04 sleeve. Three of the four stocks are defensive. They stay.
HELD = [
    {"symbol": "PG", "beta": 0.40, "sector": "consumer staples"},
    {"symbol": "RSG", "beta": 0.55, "sector": "waste"},
    {"symbol": "NOC", "beta": 0.45, "sector": "defense/aerospace"},
    {"symbol": "CDNS", "beta": 1.15, "sector": "technology"},
]


class SleeveBalanceTests(unittest.TestCase):
    def test_current_book_is_over_the_cap_and_nothing_is_sold(self):
        self.assertEqual(sleeve.defensive_count(HELD), 3)
        self.assertFalse(sleeve.is_defensive(1.15, "technology"))
        ranked = sleeve.rank_candidates(HELD, [])
        self.assertEqual(ranked["sells"], [])
        self.assertGreater(ranked["held_defensive_count"], ranked["cap"])

    def test_another_low_beta_name_is_blocked_without_a_forced_sale(self):
        decision = sleeve.evaluate_candidate(HELD, {
            "symbol": "MCK", "beta": 0.50, "sector": "healthcare",
            "conviction": 72, "signals": 2,
        })
        self.assertTrue(decision["defensive"])
        self.assertFalse(decision["buy_allowed"])
        self.assertFalse(decision["force_sell"])
        self.assertIn("Do not sell", decision["blocked_reason"])

    def test_a_market_like_name_that_clears_70_is_allowed(self):
        decision = sleeve.evaluate_candidate(HELD, {
            "symbol": "EXAMPLE", "beta": 1.20, "sector": "technology",
            "conviction": 74, "signals": 2,
        })
        self.assertTrue(decision["buy_allowed"])
        self.assertFalse(decision["defensive"])
        self.assertEqual(decision["participation_bonus"], 5)
        self.assertEqual(decision["rank_score"], 79)

    def test_bonus_does_not_lower_the_conviction_gate(self):
        decision = sleeve.evaluate_candidate(HELD, {
            "symbol": "EXAMPLE", "beta": 1.30, "sector": "industrials",
            "conviction": 68, "signals": 2,
        })
        self.assertEqual(decision["rank_score"], 73)
        self.assertFalse(decision["buy_allowed"])
        self.assertIn("70", decision["blocked_reason"])

    def test_defensive_name_is_allowed_when_the_sleeve_has_room(self):
        held = [{"symbol": "CDNS", "beta": 1.15, "sector": "technology"}]
        decision = sleeve.evaluate_candidate(held, {
            "symbol": "PG", "beta": 0.40, "sector": "consumer staples",
            "conviction": 80, "signals": 2,
        })
        self.assertTrue(decision["buy_allowed"])

    def test_second_defensive_fills_the_cap_and_the_third_waits(self):
        held = [
            {"symbol": "CDNS", "beta": 1.15, "sector": "technology"},
            {"symbol": "PG", "beta": 0.40, "sector": "staples"},
        ]
        first = sleeve.evaluate_candidate(held, {
            "symbol": "RSG", "beta": 0.60, "sector": "waste",
            "conviction": 75, "signals": 2,
        })
        self.assertTrue(first["buy_allowed"])
        held_after = held + [{"symbol": "RSG", "beta": 0.60, "sector": "waste"}]
        third = sleeve.evaluate_candidate(held_after, {
            "symbol": "NOC", "beta": 0.50, "sector": "defense",
            "conviction": 77, "signals": 2,
        })
        self.assertFalse(third["buy_allowed"])

    def test_cli_blocks_a_fourth_defensive_name_and_sells_nothing(self):
        import json
        import subprocess
        payload = {
            "held": HELD,
            "candidates": [{
                "symbol": "MCK", "beta": 0.50, "sector": "healthcare",
                "conviction": 72, "signals": 2,
            }],
        }
        completed = subprocess.run(
            [sys.executable, str(Path(__file__).resolve().parents[2] / "scripts" / "sleeve.py")],
            input=json.dumps(payload), check=True, capture_output=True, text=True,
        )
        result = json.loads(completed.stdout)
        self.assertEqual(result["sells"], [])
        self.assertEqual(result["allowed"], [])
        self.assertFalse(result["blocked"][0]["buy_allowed"])

    def test_ranking_prefers_the_name_that_moves_with_the_market(self):
        held = [{"symbol": "CDNS", "beta": 1.1, "sector": "technology"}]
        ranked = sleeve.rank_candidates(held, [
            {"symbol": "SLOW", "beta": 0.9, "sector": "industrials", "conviction": 74, "signals": 2},
            {"symbol": "FAST", "beta": 1.2, "sector": "technology", "conviction": 72, "signals": 2},
        ])
        self.assertEqual([row["symbol"] for row in ranked["allowed"]], ["FAST", "SLOW"])


if __name__ == "__main__":
    unittest.main()
