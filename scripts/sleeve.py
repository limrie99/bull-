#!/usr/bin/env python3
"""Keep the 5-stock sleeve from becoming all defensive ballast.

This applies to future buys only. It never recommends selling something
already held. The Conviction >= 70 gate is unchanged: the participation
bonus only breaks ties among names that already cleared the gate.
"""

from __future__ import annotations

# Below this, the stock rises meaningfully less than the market on up days.
LOW_BETA_BELOW = 0.85
# At or above this, the stock keeps up with the market (or outruns it).
PARTICIPATION_BETA = 1.0
# Added only when sorting names that already cleared Conviction >= 70.
PARTICIPATION_RANK_BONUS = 5
MAX_DEFENSIVE_SLOTS = 2
CONVICTION_GATE = 70

# Sector words that count as defensive even if a beta print is missing.
# "Communication services" is intentionally not here: that bucket also holds
# growth companies. Healthcare is not here either; a low-beta distributor is
# caught by the beta test, and a high-beta health name is not ballast.
DEFENSIVE_SECTOR_KEYWORDS = (
    "consumer staples",
    "staples",
    "utilities",
    "utility",
    "waste",
    "environmental services",
    "telecom",
    "telecommunications",
    "defense",
    "defence",
    "aerospace",
)


def _sector_text(sector: str | None) -> str:
    return " ".join(str(sector or "").casefold().replace("_", " ").replace("/", " ").split())


def is_defensive(beta: float | None, sector: str | None = None) -> bool:
    if beta is not None and float(beta) < LOW_BETA_BELOW:
        return True
    text = _sector_text(sector)
    if not text:
        return False
    return any(keyword in text for keyword in DEFENSIVE_SECTOR_KEYWORDS)


def participation_bonus(beta: float | None) -> int:
    """Ranking points only. Never added into the number that must clear 70."""
    if beta is None:
        return 0
    if float(beta) >= PARTICIPATION_BETA:
        return PARTICIPATION_RANK_BONUS
    return 0


def defensive_count(held: list[dict]) -> int:
    return sum(1 for name in held if is_defensive(name.get("beta"), name.get("sector")))


def evaluate_candidate(held: list[dict], candidate: dict) -> dict:
    """Say whether a NEW name may be bought. Never emits a sell of a holding."""
    conviction = float(candidate.get("conviction") or 0)
    signals = int(candidate.get("signals") or 0)
    beta = candidate.get("beta")
    beta_value = None if beta is None else float(beta)
    defensive = is_defensive(beta_value, candidate.get("sector"))
    bonus = participation_bonus(beta_value)
    held_defensive = defensive_count(held)
    gate_ok = conviction >= CONVICTION_GATE and signals >= 2
    blocked = None
    if not gate_ok:
        blocked = (
            f"Conviction gate stays at {CONVICTION_GATE} with 2 signals. "
            f"This name is {conviction:g} with {signals} signal(s). "
            "The participation bonus is not added to that score."
        )
    elif defensive and held_defensive >= MAX_DEFENSIVE_SLOTS:
        blocked = (
            f"The sleeve already holds {held_defensive} defensive or low-beta names "
            f"(cap is {MAX_DEFENSIVE_SLOTS} for future buys). "
            "Leave this name on the watchlist. Do not sell a current holding to make room."
        )
    return {
        "symbol": candidate.get("symbol"),
        "buy_allowed": blocked is None,
        "blocked_reason": blocked,
        "defensive": defensive,
        "conviction": conviction,
        "signals": signals,
        "participation_bonus": bonus,
        "rank_score": conviction + bonus,
        "held_defensive_count": held_defensive,
        "force_sell": False,
    }


def main(argv: list[str] | None = None) -> int:
    """Print buy / wait decisions. Does not place an order."""
    import argparse
    import json
    import sys

    parser = argparse.ArgumentParser(description="Check the defensive-sleeve cap. Does not place an order.")
    parser.add_argument("--json", help="JSON object with 'held' and 'candidates' lists. Default: stdin.")
    args = parser.parse_args(argv)
    raw = open(args.json, encoding="utf-8").read() if args.json else sys.stdin.read()
    payload = json.loads(raw)
    result = rank_candidates(payload.get("held") or [], payload.get("candidates") or [])
    json.dump(result, sys.stdout, indent=2)
    sys.stdout.write("\n")
    return 0


def rank_candidates(held: list[dict], candidates: list[dict]) -> dict:
    """Split a bench into names that may be bought and names that wait."""
    allowed = []
    blocked = []
    for candidate in candidates:
        decision = evaluate_candidate(held, candidate)
        (allowed if decision["buy_allowed"] else blocked).append(decision)
    allowed.sort(key=lambda row: (-row["rank_score"], str(row["symbol"])))
    return {
        "held_defensive_count": defensive_count(held),
        "cap": MAX_DEFENSIVE_SLOTS,
        "allowed": allowed,
        "blocked": blocked,
        "sells": [],
    }


if __name__ == "__main__":
    raise SystemExit(main())
