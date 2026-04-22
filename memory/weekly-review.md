# Weekly Reviews

Most recent week at the top.

Format:

```
## Week ending YYYY-MM-DD (Friday)

**Metrics**
- Starting equity: $—
- Ending equity: $—
- Week return: —%
- SPY week return: —%
- **Alpha vs SPY: —%**
- Trades placed: — buys / — sells
- Win rate on closed trades this week: —%

**Wins**
- …

**Losses**
- …

**Lessons**
- …

**Strategy adjustments (if any)**
- …

**Grade: A / B / C / D / F** — short reason.
```

---

## Week ending 2026-04-22 (inception week — Tue funding → Wed)

**Timing note:** Routine invoked as the Friday weekly review, but the system date is Wed 2026-04-22 and the paper account was only funded Tue 2026-04-21. This is effectively a **2-day inception snapshot**, not a full Mon–Fri week. Flagging explicitly so the numbers aren't mistaken for a real five-session cycle.

**Metrics**
- Starting equity (4/21 funding): $100,000.00
- Ending equity (4/22, pulled from Alpaca portfolio/history): $100,000.00
- Week return: **0.00%**
- SPY week return (Mon 4/20 open $708.87 → Wed 4/22 $709.62, partial week): **+0.11%**
- **Alpha vs SPY: −0.11%** (immaterial — no capital deployed)
- Trades placed: **0 buys / 0 sells**
- Win rate on closed trades this week: n/a (no closes)

**Wins**
- No losses. Account is intact at $100K, zero drawdown, zero realized P/L.
- Pre-market research pass on Tue 4/21 (19:00 CT re-run) correctly flagged no clean ≥2-signal buy and recommended at most a starter NVDA tranche only if Wed futures were constructive. That discipline held — no forced first trade.
- Guardrails behaved exactly as written under missing-secrets halts: no API calls were made, no silent state changes, clear errors surfaced to `messages.md`.

**Losses**
- **Opportunity cost on the NVDA starter plan.** The 4/21 19:00 CT scout queued a ~$5K NVDA tranche contingent on a constructive Wed open. The 4/22 market-open routine halted on missing env vars before that decision could be made or executed. Small missed-alpha risk; no position is worse than a forced one.
- **Infrastructure halt, not a trading loss:** two of three 4/22 routines (08:30 market-open, 12:00 midday) aborted because `.env` was missing and the cloud env had no `ALPACA_*` / `PERPLEXITY_API_KEY` set. This isn't a strategy failure — it's an ops failure — but it's the single biggest drag on this week.
- Cannot grade signal accuracy yet: no signals fired into a trade, so there's nothing to backtest against outcomes.

**Lessons**
- **Patience paid.** First trade was not forced. Given how thin the 4/21 17:00 CT scout's data was (multiple `n/a`s on catalysts and earnings dates), pushing capital out would have been undisciplined. Strategy's "≥2 verified signals" rule did its job.
- **Research-call discipline matters.** The 17:00 vs 19:00 CT sub-agent passes produced contradictory earnings dates for TSLA (AMC 4/22 asserted, then not confirmed). Rule for next week: on any mega-cap earnings date a routine uses to gate a decision, re-verify with a second source before treating it as actionable.
- **Operational pattern to fix before trading resumes.** Two consecutive halts in one session for the same env-var reason. That's not a one-off — that's a deploy/runner configuration gap. Next user action that matters more than any trading call this week: restore the four required env vars in the cloud runner (or confirm `.env` will be present on each wake).

**Pattern check vs prior reviews**
- First weekly review — no prior baseline yet.
- Carried-forward v1 learnings (no options, 10% trailing stops, concentration > diversification) haven't been tested this week because no trade was placed. Nothing to update.

**Strategy adjustments (if any)**
- **None.** One incomplete inception week is not a signal. Three weeks of the same pattern would be. All rules in `memory/strategy.md` stand unchanged.
- Not elevating the "verify earnings dates from two sources" point into strategy yet — it's a research-call workflow habit, not a rule. If it repeats, codify it.

**Grade: C** — intact capital, disciplined no-trade, but two routines lost to a fixable infrastructure bug; no alpha generated. A real grade requires a real trading week.

---
