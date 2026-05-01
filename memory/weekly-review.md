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

## Week ending 2026-05-01 (Friday)

**Metrics**
- Starting equity (Fri 4/24 close): $100,172.25
- Ending equity (Fri 5/1 close): $99,924.09
- Week return: **-0.25%**
- SPY week return: **+0.91%** (713.97 → 720.49, IEX feed)
- **Alpha vs SPY: -1.16%**
- Trades placed this week: 0 buys / 0 sells / 1 stop-management rotation
- Win rate on closed trades this week: N/A (0 closes)
- Cash at week-end: $94,965.50 (~95% of equity)
- Open positions: 1 / 5 max

**Activity log this week**
- Mon 2026-04-27 12:16 CT — NVDA crossed +5% in profit (HWM $216.73 = +7.6% from $201.38 entry). Canceled the original -7% hard stop at $187.28, placed a 10% trailing stop (currently $195.057). Strategy-correct rotation, fired automatically per the +5% threshold rule.
- Tue–Fri — no routine entries in `research-log.md`; no buys, sells, or further stop changes recorded against the account.
- The only filled order this week was that 4/27 stop swap. The NVDA buy itself (25 sh @ $201.38) executed Wed 2026-04-22 — last week, not this one — but is the only live position that drove this week's P/L.

**Wins**
- The +5%/trailing-stop rule executed correctly. NVDA peaked at $216.82 on Mon 4/27 (+7.7% intraday), the rotation locked in floor at $195.06, and when NVDA gave back the entire move on Thu 4/30 (-4.7% day) the trailing stop did NOT trigger — exactly the design (let it breathe).
- Position size was a starter ~5% tranche, so the -1.5% drawdown on NVDA cost the book ~$77 — small.
- No leverage, no options, no panic sells, no rule violations.

**Losses**
- **The big one: cash drag.** The book ran ~95% cash through a +0.91% SPY week. SPY notched five up-days into Friday's +0.99% close. We participated with ~5%, so we earned almost nothing on the rally and lost the spread to the index.
- NVDA round-tripped: +7.7% on Mon → -1.5% by Fri close. We owned the round-trip with no add and no scale-out. If the trailing stop had been wider OR the position larger, the round-trip mattered more; if it had been tighter, we'd have locked profit. Calling the round-trip itself a loss is harsh — the dollar damage was tiny — but the failure to **add a second name** while NVDA was working is the real loss.

**Lessons**
1. **Cash sitting in a paper account does nothing.** The strategy says "10–20% cash buffer at all times" — implication: 80–90% deployed. We are at 5%. That is a strategy violation by omission, not by overruling — it just never got executed.
2. **Routines visibly did not run this week.** `research-log.md` has zero new entries Mon–Fri. `messages.md` likewise stops at 4/22 12:00 CT halt notes. The 4/22 NVDA buy (10:07 CT) and the 4/27 stop rotation (12:16 CT) both happened against a quiet harness — meaning they were either fired ad-hoc by the user or by an unlogged routine. **Bull's memory chain is broken** — without research-log entries each routine, future-Bull cannot pattern-match. This is the dominant lesson of the week.
3. **A starter is the start, not the end.** The 4/21 pre-market plan explicitly said "starter NVDA, re-run scout next routine, add on confirmation." That follow-up scout never happened. We treated the starter as a complete trade.
4. **Risk-management logic works** — trailing stops behaved correctly. That is the one piece of evidence to keep building on.

**Pattern recognition vs. previous weekly reviews**
- This is the first weekly review — no prior pattern data. Establishing a baseline only.
- Cross-check vs v1 30-day learnings: "concentration > diversification" was a v1 insight. This week we're suffering the inverse failure mode — over-concentration **in cash**. The spirit of the v1 lesson (deploy capital with conviction) is being violated.

**Strategy adjustments**
- **None to the rule book.** One week is not a pattern, and no rule was bent — rules were simply not exercised. Bending rules off a single underperforming week would be exactly the over-reaction CLAUDE.md warns against.
- **Process note (not a rule edit):** the recurring routines need to actually run and log. If next week's research-log is again empty, that is a harness/scheduler problem the user needs to fix, not a strategy I can rewrite my way out of.
- **Operational note for next week (not in strategy.md):** if routines run, the pre-market scout's job Monday is a fresh watchlist with verified earnings dates and at least 2 names that pass the 2-signal bar. Target: deploy a second 5–10% position by mid-week if signals warrant. Do not force trades if signals don't.

**Grade: D** — underperformed SPY by 1.16% mostly because we sat in cash; risk-management rules executed correctly but the routines that source new ideas didn't run, so no follow-on deployment happened.

---
