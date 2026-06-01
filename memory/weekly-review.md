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

## Consolidated review: 2026-04-22 → 2026-06-01 (the lost month)

_Written 2026-06-01 during a manual repair, reconstructed from Alpaca fills + the ~130 orphaned routine branches. The five weekly reviews that "ran" (5/1, 5/8, 5/15, 5/22, 5/29) all read memory frozen at 4/22 and so learned nothing — this entry replaces them._

**Metrics**
- Starting equity: $100,000.00 (2026-04-22)
- Ending equity: $99,840.95 (2026-06-01)
- Period return: **−0.16%**
- SPY same period: not reliably captured (memory never persisted) — but the tape rose; sitting in cash means we almost certainly trailed the benchmark badly.
- **Alpha vs SPY: negative by omission** — the cardinal sin for a "beat SPY" mandate.
- Trades placed: 1 buy / 1 sell (a single NVDA round-trip)
- Win rate on closed trades: 0% (1 loss)

**What actually happened**
- 4/22: bought 25 NVDA @ 201.38. Held ~2 weeks, went +6%, hard stop → 10% trailing.
- 5/4: trailing stop fired at −3.16% → −$159.04. NVDA round-tripped.
- 5/4 → 6/1 (~18 trading days): **100% cash, zero trades.** Pre-market scouts floated GOOGL, MSFT, PLTR, LLY, AMAT, WMT, TXN — none ever bought.

**Root cause (this is the real lesson, not the NVDA trade)**
1. **Memory never persisted.** Every routine branched fresh from a frozen `main` and pushed to a throwaway `claude/*` branch (`git push origin main` pushed the unmoved local `main` ref, not `HEAD`). So every wake-up read 4/22 memory. Fixed 2026-06-01 by pushing `HEAD:main` and syncing from `origin/main` at the start of each run (see CLAUDE.md steps 2 & 6).
2. **Paralysis loop.** Reading stale memory, every market-open concluded "the plan is stale, don't trade, wait for the next pre-market" — which also read stale memory. Result: a well-researched watchlist every morning and never a single execution. Fixed by the cold-start rule added to strategy.md.
3. **API-key outages.** Multiple multi-day halts (early/mid May) compounded the gaps.

**Lessons**
- One losing trade is noise; **a month of unintended cash is a strategy failure.** For a beat-SPY mandate, being flat is a bet against the benchmark.
- "Don't trade a stale plan" must never collapse into "never trade." If memory is empty/stale and the market is open, generate a fresh thesis *within the run*.
- Infrastructure (state persistence, key availability) is part of the strategy. A correct strategy that can't remember anything is a random one.

**Strategy adjustments** — see strategy.md changelog 2026-06-01: added the cold-start / anti-paralysis rule. Core guardrails unchanged (they barely got to run; no evidence to retune them).

**Grade: D** — capital was preserved (−0.16%) but the entire mandate (beat SPY) was abandoned by accident for six weeks. Not an F only because nothing was lost recklessly; the failure was omission and broken plumbing, both now fixed.

---

(no reviews yet)
