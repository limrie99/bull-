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

## Week ending 2026-05-08 (Friday)

**Metrics**
- Starting equity (5/1 close, Alpaca base_value): $99,926.75
- Ending equity (5/8 close): $99,840.95
- Week return: **−0.09%**
- SPY week return: **+2.37%** ($720.49 → $737.54)
- **Alpha vs SPY: −2.45%**
- Trades placed this week: 0 buys / 1 sell (NVDA trailing-stop fill on 5/4)
- Win rate on closed trades this week: **0%** (1 closed trade, a loser at −3.16%)

**Wins**
- **Risk rules executed exactly as designed.** NVDA hit +5% on 4/27 — the −7% hard stop was canceled and replaced with a 10% trailing stop, HWM $216.73, trail to $195.057. When NVDA reversed, the stop fired at $195.02 and capped the loss at −3.16% on the position (well inside the −7% ceiling).
- **Sized small.** $5,034 deployed (~5.0% of portfolio) on a single-signal starter — small enough that a whipsaw cost $159, not $1,500.

**Losses**
- **NVDA round-trip −$159.04 (−3.16%).** Bought 25 @ $201.38 on 4/22, sold 25 @ avg $195.02 on 5/4. Painful detail: NVDA closed the week at $215.21 — held position would have been **+6.87%, +$346** instead. Whipsaw cost ~$505 of opportunity.
- **Sat in cash for 4 trading days while SPY ran +2.4%.** That's where the alpha gap actually came from — not from the NVDA loss (which was small) but from being uninvested during the Tuesday–Friday rally.

**Lessons**
- **Don't bypass the 2-signal entry floor with a "starter tranche" workaround.** The 4/21 19:00 CT scout entered NVDA on signal #3 alone (secular AI tailwind). The strategy says "need at least 2." Sizing down doesn't fix a thin thesis — it just makes the whipsaw cheaper. Either find the second signal or pass.
- **Trailing stops are correct in the long run, frustrating in the moment.** v1's data already proved 2% is too tight. 10% rode 4/27→5/4 cleanly. The reversal back to $215.21 is post-trade noise, not evidence the rule is wrong. n=1.
- **Memory hygiene is a system risk.** Between 4/22 noon and today (12 trading days), no routine wrote to `memory/portfolio.md`, `memory/trade-log.md`, `memory/messages.md`, or `memory/research-log.md` — yet a real round-trip executed in the broker account. Reconstructed today from Alpaca orders + activities. **The −$159 trade loss is recoverable; flying blind is not.**
- **Always re-deploy after a stop-out unless the macro changes.** Sitting in cash 5/4–5/8 was a default, not a decision. Should have triggered a fresh scout on 5/4 PM or 5/5 AM.

**Strategy adjustments (changes made)**
- **Added a memory-hygiene rule to `memory/strategy.md`** (changelog entry 2026-05-08): every routine must reconcile `portfolio.md` against the live Alpaca snapshot at start AND end; if the reconcile fails, log the gap loudly to `memory/messages.md` rather than skipping the write.
- **No change to trailing-stop %, no change to position-size %, no change to signal floor.** One trade is noise — three of the same pattern would be a signal. Holding the rules.

**Grade: C−** — followed the rules cleanly on the one trade, capped the loss as designed, but entered on a single signal, missed a 2.4% SPY rally by sitting idle 4 days, and the memory pipeline went dark for 12 trading days. Survivable but unimpressive.

---

(no reviews yet)
