#!/usr/bin/env python3
"""Deterministic checks for Astra scheduling, paper-only guardrails, and fixtures."""

from __future__ import annotations

import os
import tempfile
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


NO_CREDENTIALS = {
    "ASTRA_ALPACA_API_KEY": "",
    "ASTRA_ALPACA_SECRET_KEY": "",
    "ALPACA_API_KEY": "",
    "ALPACA_SECRET_KEY": "",
    "APCA_API_KEY_ID": "",
    "APCA_API_SECRET_KEY": "",
}


class CredentialResolutionTests(unittest.TestCase):
    def test_dedicated_astra_keys_win(self):
        env = dict(NO_CREDENTIALS, **{
            "ASTRA_ALPACA_API_KEY": "PKASTRA", "ASTRA_ALPACA_SECRET_KEY": "astra-secret",
            "ALPACA_API_KEY": "PKBULL", "ALPACA_SECRET_KEY": "bull-secret",
        })
        source, key, _, key_var = runner.resolve_alpaca_credentials(env)
        self.assertEqual(source, "dedicated")
        self.assertEqual(key, "PKASTRA")
        self.assertEqual(key_var, "ASTRA_ALPACA_API_KEY")

    def test_falls_back_to_bull_paper_keys(self):
        env = dict(NO_CREDENTIALS, **{
            "ALPACA_API_KEY": "PKBULL", "ALPACA_SECRET_KEY": "bull-secret",
        })
        source, key, _, key_var = runner.resolve_alpaca_credentials(env)
        self.assertEqual(source, "shared-bull")
        self.assertEqual(key, "PKBULL")
        self.assertEqual(key_var, "ALPACA_API_KEY")

    def test_accepts_alpaca_native_naming(self):
        env = dict(NO_CREDENTIALS, **{
            "APCA_API_KEY_ID": "PKBULL", "APCA_API_SECRET_KEY": "bull-secret",
        })
        source, _, _, key_var = runner.resolve_alpaca_credentials(env)
        self.assertEqual(source, "shared-bull")
        self.assertEqual(key_var, "APCA_API_KEY_ID")

    def test_half_a_pair_is_not_enough(self):
        env = dict(NO_CREDENTIALS, **{"ALPACA_API_KEY": "PKBULL"})
        self.assertEqual(runner.resolve_alpaca_credentials(env)[0], "")


class PaperGuardrailTests(unittest.TestCase):
    def test_alpaca_rejects_missing_keys(self):
        with patch.dict(os.environ, dict(NO_CREDENTIALS, **{
            "ASTRA_ALPACA_BASE_URL": runner.PAPER_URL,
        }), clear=False):
            with self.assertRaises(RuntimeError) as ctx:
                runner.Alpaca()
        self.assertIn("ASTRA_ALPACA_API_KEY", str(ctx.exception))

    def test_bull_base_url_cannot_send_astra_live(self):
        # Bull's own ALPACA_BASE_URL may be live; Astra must ignore it entirely.
        with patch.dict(os.environ, dict(NO_CREDENTIALS, **{
            "ALPACA_BASE_URL": "https://api.alpaca.markets",
            "ALPACA_API_KEY": "PKBULL", "ALPACA_SECRET_KEY": "bull-secret",
        }), clear=False):
            os.environ.pop("ASTRA_ALPACA_BASE_URL", None)
            alpaca = runner.Alpaca()
        self.assertEqual(alpaca.base, runner.PAPER_URL)
        self.assertEqual(alpaca.credential_source, "shared-bull")

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


class HelperModeTests(unittest.TestCase):
    """On Bull's shared account Astra proposes; it never places an order."""

    def test_shared_account_blocks_buys_even_with_execution_enabled(self):
        snapshot = runner.load_json(FIXTURE, {})
        decision = runner.fixture_decision("entry-check")
        alpaca = runner.FixtureAlpaca(snapshot, credential_source="shared-bull")
        with patch.dict(os.environ, {"ASTRA_EXECUTION_ENABLED": "true"}, clear=False):
            result = runner.validate_and_execute(
                decision, snapshot, runner.load_json(runner.CONFIG_PATH, {}),
                alpaca, "entry-check", [],
            )
        self.assertEqual(result["status"], "PROPOSED_ONLY")
        self.assertIn("Helper mode", result["reason"])

    def test_shared_account_blocks_sells_too(self):
        snapshot = runner.load_json(FIXTURE, {})
        decision = dict(runner.fixture_decision("entry-check"), action="SELL", symbol="AAPL")
        alpaca = runner.FixtureAlpaca(snapshot, credential_source="shared-bull")
        with patch.dict(os.environ, {"ASTRA_EXECUTION_ENABLED": "true"}, clear=False):
            result = runner.validate_and_execute(
                decision, snapshot, runner.load_json(runner.CONFIG_PATH, {}),
                alpaca, "portfolio-check", [],
            )
        self.assertEqual(result["status"], "PROPOSED_ONLY")

    def test_shared_account_does_not_score_a_rival_return(self):
        snapshot = runner.load_json(FIXTURE, {})
        record = {
            "timestamp": runner.utc_now().isoformat(), "routine": "entry-check",
            "decision": runner.fixture_decision("entry-check"),
            "execution": {"status": "PROPOSED_ONLY", "reason": runner.SHARED_ACCOUNT_REASON},
        }
        with tempfile.TemporaryDirectory() as tmp:
            with patch.object(runner, "STATE_PATH", Path(tmp) / "state.json"):
                runner.update_state("entry-check", snapshot, record,
                                    runner.load_json(runner.CONFIG_PATH, {}), 700.0, "shared-bull")
                state = runner.load_json(runner.STATE_PATH, {})
        self.assertEqual(state["account_scope"], "shared-with-bull")
        self.assertEqual(state["role"], "research-helper")
        self.assertIsNone(state["return_pct"])
        self.assertIsNone(state["alpha_pct"])


class ProposalHandoffTests(unittest.TestCase):
    def _record(self, symbol: str) -> dict:
        return {
            "timestamp": runner.utc_now().isoformat(), "routine": "premarket-research",
            "decision": dict(runner.fixture_decision("entry-check"), symbol=symbol),
            "execution": {"status": "PROPOSED_ONLY", "reason": runner.SHARED_ACCOUNT_REASON},
        }

    def test_newest_proposal_is_on_top_and_history_is_capped(self):
        with tempfile.TemporaryDirectory() as tmp:
            proposals = Path(tmp) / "memory" / "astra-proposals.md"
            with patch.object(runner, "PROPOSALS_PATH", proposals), \
                 patch.object(runner, "PROPOSAL_LOG", Path(tmp) / "proposals.jsonl"), \
                 patch.object(runner, "MAX_PROPOSAL_BLOCKS", 3):
                for symbol in ["AAA", "BBB", "CCC", "DDD"]:
                    runner.write_proposal_handoff(self._record(symbol), "shared-bull")
                text = proposals.read_text(encoding="utf-8")
                rows = runner.read_jsonl(runner.PROPOSAL_LOG, 10)
        self.assertTrue(text.startswith("# Astra proposals"))
        self.assertLess(text.index("DDD"), text.index("CCC"))
        self.assertNotIn("AAA", text)
        self.assertEqual(text.count("\n## "), 3)
        self.assertEqual([r["symbol"] for r in rows], ["AAA", "BBB", "CCC", "DDD"])
        self.assertEqual(rows[-1]["account"], "shared-bull")


if __name__ == "__main__":
    unittest.main()
