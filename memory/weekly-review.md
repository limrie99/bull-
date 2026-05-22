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

## Week ending 2026-05-22 (Friday)

**Metrics**
- Starting equity (Mon 5/18 open): $99,840.95
- Ending equity (Fri 5/22 close): $99,840.95
- Week return: 0.00%
- SPY week return: +0.79% (Mon open $739.83 → Fri close $745.67)
- **Alpha vs SPY: -0.79%**
- Trades placed this week: 0 buys / 0 sells
- Open positions at close: 0
- Win rate on closed trades this week: N/A (no trades closed)
- Cash deployed during the week: 0% (100% cash all week)

**Wins**
- Capital preserved — no losses taken because no positions were on.
- No guardrail breaches. Risk rules held without being tested (because nothing was at risk).

**Losses**
- Lost 0.79% of alpha to SPY simply by sitting in cash. This is the entire P/L story of the week: an opportunity cost, not a trading loss. A flat week vs a benchmark that's drifting up is the same as a loss on the scorecard.
- Zero trades placed. Strategy allows up to 3 new buys/week and 5 open positions; we ran at 0/3 and 0/5. Pre-market scouts have been silent (or not running) so no fresh thesis was generated to act on.

**Lessons**
- **Cash is a position, and it carries SPY-shaped opportunity cost.** Holding 100% cash makes sense when there's no thesis, but it has to be a *chosen* state, not a default from missing routines. This week it was the latter.
- **Bookkeeping drift is a real risk.** Broker truth (Alpaca) and memory diverged: the one closed lifetime trade (NVDA, bought 4/22 $201.38, trailing-stopped 5/04 $195.02 → -$159.04 / -3.16%) is in Alpaca's order history but was never recorded in `trade-log.md`, and `portfolio.md` is frozen on the 4/21 snapshot. The weekly review has to live on broker data, not on stale local files — which is what I did. Backfilling the log this routine.
- **One trade is not a pattern.** The NVDA trailing-stop exit (after a +7.62% HWM at $216.73) gave back 10% from the high and locked in -3.16%. That's the *designed* behavior of a 10% trail and is consistent with v1's carried-forward learning that 10% beats 2%. Resist the urge to tighten on one data point.

**Pattern recognition vs. prior weeks**
- This is the first weekly review on file (`memory/weekly-review.md` had no prior entries), so no multi-week pattern to call out yet. **Setting up the watchpoint:** if next week is also flat cash with the scouts not producing a tradeable thesis, that's a process problem to investigate (are the pre-market routines actually firing? are they returning n/a too often to act on, as the 4/21 logs showed?).

**Strategy adjustments (if any)**
- **None.** It is too early to tweak rules. The 10% trailing stop fired as designed on the only closed trade. No guardrail breach. The right response to a quiet week is more research, not new rules.
- **Process note (not a rule change):** every routine, regardless of whether it trades, must reconcile `portfolio.md` against `/v2/account` and append any new fills to `trade-log.md`. That's already in CLAUDE.md ("write memory back") but it slipped this month; flagging it here so future-Bull treats reconciliation as non-optional.

**Grade: D** — flat while SPY ran +0.79%; 100% cash all five sessions; no scout output translated into a tradeable idea. Not a loss, but a missed week.
