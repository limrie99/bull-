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

## Week ending 2026-05-15 (Friday)

**Metrics**
- Starting equity (Mon 5/11 open): $99,840.95
- Ending equity (Fri 5/15 close): $99,840.95
- Week return: **0.00%**
- SPY week return: **+0.35%** (736.52 Mon open → 739.10 Fri close)
- **Alpha vs SPY: −0.35%**
- Trades placed this week: **0 buys / 0 sells**
- Win rate on closed trades this week: n/a (no trades closed)

**Wins**
- Capital preservation: $0 lost. Account is fully in cash, no risk on the book.
- No guardrail violations. No options, no leverage, no over-concentration, no stupid chases.

**Losses**
- **Opportunity cost.** SPY rose +0.35% this week and we earned 0%. Trailing the benchmark while doing nothing is the worst kind of loss — it's invisible on the P/L but it's the entire thing we're measured on.
- **Operational gap.** The trade log shows zero trades since the account was opened 2026-04-21, yet the 1-month portfolio history shows the equity did move between $100,000 and $99,840.95 between ~4/21 and ~4/30 (settling at $99,840.95 since then). Either there were unrecorded fills (trade-log discipline broken) or there's an Alpaca activity I can't see in the history. Equity has been flat as a board for ~2 weeks before this week, which strongly implies no routines ran for that window.
- **Lifetime: −$159.05 (−0.16%)** since account creation 4/21. Not material on its own, but symbolically bad: we are 24 days in and below the line we started at, with no theses tested.

**What worked**
- The strategy itself is intact — guardrails, signal-list, position sizing are all sound on paper.
- Today's routine confirmed APIs work end-to-end (Alpaca account, positions, history, SPY bars, clock — all 200). The pipes are clear.

**What didn't (root cause analysis)**
- **Signal selection wasn't the failure — routine execution was.** The last pre-market scout (2026-04-21 19:00 CT) correctly flagged NVDA as a med-conviction starter and *correctly* said "if futures are still risk-off at 6 AM CT, pass entirely." That decision-tree is fine.
- The actual failure was that the system halted on 4/22 for missing env vars (per the research log) and there is **no record of any routine running between 4/22 and today** — research-log, trade-log, and messages.md all stop at 4/22 12:00 CT. Whether the scheduler stopped firing or the routines fired and silently no-op'd, the user-facing record went dark for ~3 weeks. That is the real problem.

**Pattern check vs prior weekly reviews**
- No prior weekly reviews to compare against — this is the first. Cannot yet call this a pattern. But it is the only data point I have, and the data point is "we shipped nothing."

**Strategy adjustments**
- **None.** Per the routine rule — one bad week is not a signal, three weeks of the same pattern is. The strategy didn't fail this week; the runner did. Changing buy signals or sizing in response to an operational outage would be exactly the kind of noise-tweak we're trying to avoid. Strategy stays as-is.
- The one thing I want the user to see: if next week is another zero-trade, zero-research week, the right response is *not* to loosen the buy signals — it's to fix the scheduler.

**Action items for next week (operational, not strategic)**
1. Monday pre-market: run a full fresh scout. Don't blindly resurrect the 4/21 NVDA plan — 24 days of tape has moved, and NVDA's 5/20 earnings are now 3 trading days away, putting it INSIDE the earnings-blackout rule.
2. Build a fresh seed watchlist with current next-earnings dates for the May/June window so the scout has a real universe.
3. Treat the first successful trade as a litmus test for trade-log discipline — log it, prepend it, push it, dashboard it.

**Grade: F** — Underperformed SPY by 0.35% with 0 trades and 0 research output for the week. Capital preservation does not get a pass when the mandate is "beat SPY." We were absent.

---

(no prior reviews)
