#!/usr/bin/env python3
"""Deterministic checks for Astra's committee voices and the code-enforced buy gate."""

from __future__ import annotations

import os
import sys
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import runner


FIXTURE = Path(__file__).resolve().parent / "fixture.json"
CONFIG = runner.load_json(runner.CONFIG_PATH, {})
VOICES = runner.load_json(runner.VOICES_PATH, {})


def voice(bench: str, stance: str, conviction: int, symbols=("MSFT",), name=None) -> dict:
    return runner.voice_record(
        {"id": name or f"{bench}-1", "name": name or f"{bench} voice", "bench": bench},
        {"stance": stance, "conviction": conviction, "symbols": list(symbols),
         "argument": "test", "evidence": [], "risk_flags": [], "sources": []},
    )


def committee(*records: dict, **overrides) -> dict:
    voices = {**VOICES, **overrides}
    return runner.committee_record("entry-check", list(records), voices, "test-model")


class RosterTests(unittest.TestCase):
    def test_every_bench_is_staffed(self):
        benches = {v["bench"] for v in VOICES["voices"]}
        self.assertEqual(benches, {"researchers", "buyers", "skeptics"})

    def test_entry_check_hears_all_three_benches(self):
        roster = runner.roster_for_routine(VOICES, "entry-check")
        self.assertEqual(
            {v["bench"] for v in roster}, {"researchers", "buyers", "skeptics"},
        )

    def test_risk_shutdown_hears_no_buyers(self):
        roster = runner.roster_for_routine(VOICES, "risk-shutdown")
        self.assertTrue(roster)
        self.assertNotIn("buyers", {v["bench"] for v in roster})

    def test_voices_declare_mandate_and_routines(self):
        for entry in VOICES["voices"]:
            self.assertTrue(entry.get("mandate"), entry.get("id"))
            self.assertTrue(entry.get("routines"), entry.get("id"))

    def test_voice_instructions_carry_bench_and_mandate(self):
        entry = VOICES["voices"][0]
        text = runner.voice_instructions(entry, VOICES)
        self.assertIn(entry["mandate"], text)
        self.assertIn(VOICES["benches"][entry["bench"]], text)

    def test_committee_can_be_switched_off_by_env(self):
        with patch.dict(os.environ, {"ASTRA_VOICES_ENABLED": "false"}, clear=False):
            self.assertFalse(runner.committee_enabled(VOICES))
            self.assertIsNone(runner.fixture_committee("entry-check"))


class VoiceRecordTests(unittest.TestCase):
    def test_symbols_are_normalized_and_stance_is_validated(self):
        record = runner.voice_record(
            {"id": "x", "name": "X", "bench": "buyers"},
            {"stance": "buy", "conviction": 140, "symbols": [" msft ", ""],
             "argument": "a", "evidence": [], "risk_flags": [], "sources": []},
        )
        self.assertEqual(record["stance"], "BUY")
        self.assertEqual(record["conviction"], 100)
        self.assertEqual(record["symbols"], ["MSFT"])

    def test_unknown_stance_falls_back_to_hold(self):
        record = runner.voice_record({"id": "x", "bench": "buyers"}, {"stance": "YOLO"})
        self.assertEqual(record["stance"], "HOLD")

    def test_failed_voice_abstains_and_is_excluded_from_the_transcript(self):
        failed = runner.failed_voice_record({"id": "x", "name": "X", "bench": "skeptics"}, "boom")
        self.assertEqual(failed["stance"], "ABSTAIN")
        self.assertEqual(runner.transcript([failed]), [])


class BuyGateTests(unittest.TestCase):
    def test_backed_buy_passes(self):
        gate = runner.committee_buy_gate(
            committee(voice("buyers", "BUY", 80), voice("skeptics", "HOLD", 40)), "MSFT",
        )
        self.assertIsNone(gate)

    def test_high_conviction_skeptic_vetoes(self):
        gate = runner.committee_buy_gate(
            committee(voice("buyers", "BUY", 95),
                      voice("skeptics", "BLOCK", 90, name="The Bear Case")), "MSFT",
        )
        self.assertEqual(gate["status"], "REJECTED")
        self.assertIn("The Bear Case", gate["reason"])

    def test_low_conviction_block_does_not_veto(self):
        gate = runner.committee_buy_gate(
            committee(voice("buyers", "BUY", 80), voice("skeptics", "BLOCK", 60)), "MSFT",
        )
        self.assertIsNone(gate)

    def test_book_wide_block_without_symbols_vetoes(self):
        gate = runner.committee_buy_gate(
            committee(voice("buyers", "BUY", 80), voice("skeptics", "BLOCK", 90, symbols=())), "MSFT",
        )
        self.assertEqual(gate["status"], "REJECTED")

    def test_block_on_another_ticker_does_not_veto(self):
        gate = runner.committee_buy_gate(
            committee(voice("buyers", "BUY", 80), voice("skeptics", "BLOCK", 99, symbols=("AAPL",))), "MSFT",
        )
        self.assertIsNone(gate)

    def test_unbacked_ticker_is_rejected(self):
        gate = runner.committee_buy_gate(
            committee(voice("buyers", "BUY", 80, symbols=("AAPL",)), voice("skeptics", "HOLD", 30)), "MSFT",
        )
        self.assertEqual(gate["status"], "REJECTED")
        self.assertIn("buyer voices", gate["reason"])

    def test_silent_skeptic_bench_blocks_the_buy(self):
        silent = runner.failed_voice_record({"id": "s", "name": "S", "bench": "skeptics"}, "timeout")
        gate = runner.committee_buy_gate(committee(voice("buyers", "BUY", 80), silent), "MSFT")
        self.assertEqual(gate["status"], "REJECTED")
        self.assertIn("skeptic", gate["reason"].lower())

    def test_routine_without_a_buy_bench_cannot_buy(self):
        gate = runner.committee_buy_gate(committee(voice("skeptics", "HOLD", 20)), "MSFT")
        self.assertEqual(gate["status"], "REJECTED")
        self.assertIn("buy bench", gate["reason"])

    def test_raised_support_requirement_needs_two_buyers(self):
        one_buyer = committee(
            voice("buyers", "BUY", 80, name="Quality Compounder"),
            voice("buyers", "HOLD", 40, name="Margin of Safety"),
            voice("skeptics", "HOLD", 30),
            min_buyer_support=2,
        )
        self.assertEqual(runner.committee_buy_gate(one_buyer, "MSFT")["status"], "REJECTED")


class ExecutionIntegrationTests(unittest.TestCase):
    def setUp(self):
        self.snapshot = runner.load_json(FIXTURE, {})
        self.alpaca = runner.FixtureAlpaca(self.snapshot)
        self.decision = runner.fixture_decision("entry-check")

    def execute(self, committee_record):
        with patch.dict(os.environ, {"ASTRA_EXECUTION_ENABLED": "true"}, clear=False):
            return runner.validate_and_execute(
                self.decision, self.snapshot, CONFIG, self.alpaca,
                "entry-check", [], committee_record,
            )

    def test_fixture_committee_lets_the_fixture_buy_through(self):
        result = self.execute(runner.fixture_committee("entry-check"))
        self.assertEqual(result["status"], "SUBMITTED")

    def test_veto_stops_execution_before_any_order(self):
        vetoed = committee(voice("buyers", "BUY", 90), voice("skeptics", "BLOCK", 99))
        self.assertEqual(self.execute(vetoed)["status"], "REJECTED")

    def test_missing_committee_keeps_legacy_behaviour(self):
        self.assertEqual(self.execute(None)["status"], "SUBMITTED")

    def test_sell_is_not_subject_to_the_buy_gate(self):
        snapshot = {**self.snapshot, "positions": [{"symbol": "MSFT", "qty": "10"}]}
        decision = {**self.decision, "action": "SELL"}
        vetoed = committee(voice("skeptics", "BLOCK", 99))
        with patch.dict(os.environ, {"ASTRA_EXECUTION_ENABLED": "true"}, clear=False):
            result = runner.validate_and_execute(
                decision, snapshot, CONFIG, runner.FixtureAlpaca(snapshot),
                "entry-check", [], vetoed,
            )
        self.assertEqual(result["status"], "SUBMITTED")


class StateShapeTests(unittest.TestCase):
    def test_state_copy_summarizes_voices_and_drops_raw_evidence(self):
        record = {
            "timestamp": "2026-09-18T14:00:00+00:00",
            "routine": "entry-check",
            "decision": runner.fixture_decision("entry-check"),
            "execution": {"status": "SUBMITTED"},
            "committee": committee(voice("buyers", "BUY", 80), voice("skeptics", "HOLD", 40)),
        }
        trimmed = runner.state_decision(record)
        self.assertEqual(len(trimmed["committee"]["voices"]), 2)
        self.assertNotIn("evidence", trimmed["committee"]["voices"][0])

    def test_summary_of_no_committee_is_none(self):
        self.assertIsNone(runner.committee_summary(None))


if __name__ == "__main__":
    unittest.main()
