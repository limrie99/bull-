# Strategy

```
mode: paper
benchmark: SPY
style: fundamentals-driven swing / position trading (hold days to months)
NOT: day trading, options, technical-analysis scalping, crypto
starting_capital: $100,000 (Alpaca paper default)
framing: you are the user's wealth advisor — treat this account like a client's serious portfolio, not a casino
```

## Thesis

Beat SPY by being **selective, long-only, and fundamentals-driven**. Opus 4.7 is strong at digesting earnings, filings, and catalysts into coherent theses — we play to that strength. We do **not** try to day-trade candlesticks or time short-term technicals. We hold a concentrated basket of 3–5 large-cap US equities with visible near-term catalysts (earnings, product launches, guidance raises, secular tailwinds) and we let them run with trailing stops.

You are the user's **wealth advisor with a team of sub-advisor sub-agents at your disposal.** In research-heavy routines (pre-market, weekly-review), spin up sub-agents in parallel — one per ticker, one for macro, one for sector rotation — and synthesize their digests into a single decision. You have **autonomy within these guardrails** to pick the best ideas. If you think the guardrails themselves should change based on what you're seeing, say so in the weekly review — don't silently bend them.

## Learnings carried forward from v1 (30-day live run)

These were paid-for lessons. Don't relitigate them:

- **Never touch short-dated options.** One bad option trade in v1 cost $550; without it the account would have finished +5.3% vs SPY's -8.46%. Options are excluded, period.
- **10% trailing stops work.** v1 initially tried 2% stops (too tight, scalped out of winners). 10% lets theses breathe.
- **Momentum bias within a fundamentals frame is OK.** v1's real winners (NVDA, PLTR, Google, MSTR) all had secular AI / defense / crypto catalysts. Don't chase momentum without a catalyst, but don't fight a momentum name whose fundamentals are intact.
- **Concentration beat diversification at 30 days.** 3–5 conviction names outperformed spray-and-pray. Max 5 open, target 3–4.
- **Alpaca has trade limits.** v1 hit a rate limit once and had to adjust. Don't churn unless you really mean to.
- **High-beta AI/semis entry discipline (added 2026-06-05, advisory — NOT a guardrail change).** NVDA round-tripped to a stop-out *twice* in five weeks (5/4 −$159, 6/5 −$849), both times on macro/sector moves with the thesis fully intact. Root cause is beta, not the thesis: a 2–3× beta name carrying a −7% hard stop gets shaken out on a normal macro pullback before the fundamentals can express, especially when entered within a few days of a sharp run or into a known event (NFP). So for high-beta AI/semiconductor names: **size as a smaller starter (≤10%, not the full 12–15%)** and **prefer entering on a confirmed base, not chasing a multi-day spike or initiating fresh beta the day before a binary macro print.** This does not touch any guardrail (the −7% stop and 10% trailing stay exactly as-is). It is a 2nd-occurrence refinement on **probation**: a 3rd same-pattern stop-out escalates this to a hard sizing/entry rule.
  - **Update 2026-07-03 — the sizing half GRADUATES to a standing rule.** ETN (a high-beta AI-power name, sized as a **9.6% starter per this rule**) trailing-stopped on 7/2 for **−$211 / −2.19%**, thesis fully intact (sector/tape shake-out) — the **3rd high-beta shake-out of the run** (NVDA ×2, ETN). Honest nuance: ETN was *not* the identical pattern (NVDA was a fresh-entry −7% *hard*-stop shake-out; ETN was a matured position giving back a gain via its *trailing* stop). So only the **mechanism-agnostic half graduates: the ≤10% starter SIZING cap for high-beta AI/semis is now a STANDING RULE, off probation** — validated 3× because smaller size → smaller loss regardless of which stop fires (−$211 vs NVDA's −$849 is the whole argument). The **entry-timing guidance** (enter on a confirmed base; don't initiate fresh beta into a binary macro print) **stays advisory** — that specific fresh-entry-into-macro pattern hasn't recurred to test it. Changes nothing about how sizing already happens; it makes the written rule match proven behavior.

## Universe

- US-listed large-cap equities ($10B+ market cap)
- Liquid (avg daily volume > 1M shares)
- Price > $5
- Focus sectors: technology, healthcare, consumer, financials, industrials
- Avoid: speculative biotech, pre-revenue names, OTC, meme stocks, recent IPOs (< 30 days)

## Buy signals — need at least **2**

1. Positive earnings surprise in the last week (beat on both EPS and revenue, raised guidance)
2. Favorable catalyst in next 30 days (product launch, FDA approval, major contract, regulatory win)
3. Secular tailwind confirmed by Perplexity research (e.g. AI infra buildout, GLP-1 demand, onshoring)
4. Analyst upgrades or insider buying in the last 2 weeks
5. Sector rotation into the name's sector, confirmed by research
6. Price in a clear uptrend (not at fresh 52-week lows — we don't catch knives)

## Conviction Score (0–100) — the buy-gate (added 2026-06-15)

Every buy candidate gets one number before any order is placed. This converts "I have a good feeling" into a disciplined, comparable score and is the primary defense against the analysis-paralysis that left v2 in cash. Score is the **weighted sum of 5 dimensions**. Weights are deliberately fundamentals-and-catalyst heavy (60%) — technicals are timing only, never the reason to buy (see *What we will NOT do*).

| Dimension | Weight | What it measures | Scored 0–100 by the sub-agent that owns it |
|-----------|--------|------------------|---------------------------------------------|
| **Fundamental quality** | **30%** | Valuation vs sector, revenue/EPS growth, margins, balance sheet, moat | fundamental analyst |
| **Thesis & catalyst** | **30%** | Catalyst clarity, timeline (sooner = higher), risk/reward asymmetry, edge | synthesized by you (Bull) |
| **Sentiment** | **20%** | News tone, analyst upgrades/targets, insider buying, institutional flow | sentiment analyst |
| **Risk profile** | **12%** | Volatility/beta, drawdown history, liquidity, correlation (higher score = SAFER) | risk analyst |
| **Technical timing** | **8%** | Trend intact, *not* at fresh 52-wk lows (no knife-catching), near support not resistance | position/scout analyst |

**Conviction = 0.30·Fund + 0.30·Thesis + 0.20·Sent + 0.12·Risk + 0.08·Tech**

| Score | Grade | Action |
|-------|-------|--------|
| 80–100 | A | **Strong buy** — top conviction, size at high end |
| 70–79 | B+ | **Buy** — clears the gate |
| 55–69 | B | Watchlist only — wait for confirmation, do not buy |
| 40–54 | C | Sideline |
| < 40 | D/F | Avoid |

**Buy-gate rule (both conditions required, neither replaces the other):**
1. **≥ 2 buy signals** from the list above (unchanged), AND
2. **Conviction Score ≥ 70.**

A high score with only 1 signal does **not** buy. Two signals with a score of 64 do **not** buy — they go on the watchlist. When at the 5-position cap and a new name scores higher than a held name, that's a *candidate* swap to reason about in the message, not an automatic action.

## Sell signals — any one triggers

1. **Hard stop: -7% from entry.** (Placed as a stop order at buy via Alpaca bracket.)
2. **Trailing stop: 10%** — activated once position is +5% or more in profit (cancel the -7% hard stop, place a 10% trailing stop).
3. Thesis broken — the specific catalyst that prompted the buy reversed or was invalidated by news.
4. Fundamentals deterioration (guidance cut, major litigation, key exec departure).
5. Better opportunity exists and we're at the 5-position cap.

## Position sizing

Tie the size to the Conviction Score (above), which already folds in the buy-signal count:

- **Grade A (score 80–100):** 15–20% of portfolio
- **Grade B+ (score 70–79):** 10–15%
- **High-beta override (STANDING RULE as of 2026-07-03, graduated from probation):** for high-beta AI/semiconductor names, the **≤10% starter cap** wins over the band above, even at Grade A. Beta sizing beats conviction sizing for shake-out-prone names. Validated 3× (NVDA ×2, ETN): the smaller size is exactly why ETN's 7/2 shake-out cost −$211 vs NVDA's −$849. This is now a hard sizing rule, not advisory.
- Never more than 20% in any single position
- Keep 10–20% cash buffer at all times

## Risk rules

- Hard stop: **-7% from entry** (bracket order placed at buy)
- Trailing stop: **10%**, activated once position is **+5%** in profit
- Daily loss cap: portfolio down >3% intraday → no new buys rest of day
- Weekly buy cap: max 3 new positions per week
- Max 5 open positions
- Earnings risk: do not open a new position within 3 trading days of its earnings unless the thesis specifically depends on the print

## Cold-start / anti-paralysis rule (added 2026-06-01)

**"Don't trade a stale plan" must never collapse into "never trade."** A flat, all-cash book is not a safe default — for a beat-SPY mandate it is a bet *against* the benchmark, and it cost a full month of exposure in the v2 run.

- If a routine wakes to **empty or stale memory** (no fresh research log for today, or the last plan predates the current session) **and** the market is open **and** keys are valid: **do not defer to "the next pre-market."** Generate a fresh thesis *within this run* using the sub-agent team, then act on it under the normal guardrails. The pre-market and market-open routines are both allowed to originate a buy this way.
- Treat the **stale-plan / reconcile-from-Alpaca** state as a bug to escalate, not a normal resting state. If you find yourself reconciling the same round-trip or refusing to trade for more than ~2 consecutive sessions, write a flagged message to the user — something in the plumbing is wrong (this is exactly what masked the lost month).
- **Cash-drag check:** if the book has been 100% cash for **3+ trading days** with no position and no valid 2-signal setup found, say so explicitly in the message and treat finding a qualifying setup as the run's priority. Holding cash is allowed; *defaulting* into it for weeks is not.
- None of this lowers the bar: still require **2+ buy signals**, still respect the −7% stop, position caps, and weekly buy cap. Bootstrapping a thesis ≠ forcing a trade — if nothing clears the bar after a genuine fresh scan, cash is fine *for that day*.

## What we will NOT do

- Day trade
- Trade options, futures, crypto, forex
- Short
- Use margin leverage
- Buy IPOs in their first 30 days
- Average down on losers
- Rely on technical indicators (MACD, RSI, candlesticks) as primary signal — fundamentals drive entries; trailing stops handle exits
- Hold through earnings on a position already up >20% (take profit first)

## Changelog

- **2026-04-21** — Initial seed. Paper mode. $100K paper default. Tuned to Nate's rules: -7% hard stop, 10% trailing stop activated at +5%, fundamentals-driven swing only, wealth-advisor framing with sub-agent team. Carried forward v1 30-day learnings: no short-dated options (cost $550 in v1), 10% trailing beats 2%, concentration > diversification, watch Alpaca rate limits.
- **2026-06-15** — Added the **Conviction Score (0–100) buy-gate** and a persistent scored **`memory/watchlist.md`**, ported (and reweighted) from an external trading-analysis skill pack. The skills weighted technicals 25–40%; rebalanced to 60% fundamentals+catalyst / 20% sentiment / 12% risk / 8% technical-timing to match our fundamentals-first mandate. Pre-market sub-agents now each return a 0–100 score on their dimension and the opportunity scout runs defined screens (growth / momentum / earnings-beat) instead of ad-hoc idea generation. Buy now requires **2+ signals AND score ≥ 70** — the numeric gate is meant to give a clear trigger to *act* (fighting cash-drag) while keeping the bar disciplined. No change to stops, caps, or the no-options/no-shorts guardrails.
- **2026-06-01** — Added the **cold-start / anti-paralysis rule** after a post-mortem of the 4/22→6/1 run. Root cause was infrastructure, not strategy: memory never persisted across routines (every run read 4/22 state and pushed to throwaway branches), so the agent sat 100% cash for ~18 trading days after a single −$159 NVDA round-trip, never executing any of its researched candidates. Fixed the persistence bug in CLAUDE.md (push `HEAD:main`, sync from `origin/main` at run start) and added the rule above so a stale plan can no longer mean indefinite inaction. Core guardrails left unchanged — they had no fair test.
- **2026-07-03** — **Graduated the ≤10% high-beta AI/semis starter SIZING cap from advisory/probation to a STANDING RULE** (updated the "High-beta override" bullet in Position sizing + the 2026-06-05 learning note). Trigger: the pre-committed 3rd-strike condition set on 6/05 effectively fired — ETN (high-beta AI-power, sized as a 9.6% starter *because of* this rule) trailing-stopped on 7/2 for −$211/−2.19% with thesis intact, the 3rd high-beta shake-out of the run (NVDA ×2, ETN). Kept it honest and surgical: ETN was a *trailing*-stop giveback on a matured position, not the identical NVDA *hard*-stop fresh-entry shake-out, so only the **mechanism-agnostic sizing half** graduates (smaller size → smaller loss regardless of stop type — −$211 vs −$849 proves it). The **entry-timing half stays advisory** (the fresh-beta-into-macro pattern hasn't recurred). No other change — the −7% hard stop, 10% trailing, position caps, weekly buy cap, Conviction ≥70 gate, cold-start, and cash rules all held and were untouched. Deliberately did NOT touch the gate or cash level despite a −1.58-alpha week, because the same book won +4.44 the week before (one sub-SPY week is noise, not signal); the gate/cash question is parked behind a specific forward trigger (re-evaluate only if the Jul 14 data wave still yields no qualifier while SPY keeps rising).
- **2026-06-05** — Added a **high-beta AI/semis entry-discipline learning** (see "Learnings carried forward" above) after the week-ending-6/5 review. NVDA round-tripped to a stop-out a 2nd time in five weeks (−$849 on 6/5, macro/NFP semis flush, thesis intact). The pattern is beta-driven, not thesis-driven: a high-beta name on a −7% hard stop gets shaken out on macro noise before the thesis expresses. The refinement (smaller ≤10% starter, enter on a confirmed base, don't initiate beta into a binary macro print) is **advisory and on probation** — it changes no guardrail. The −7% hard stop, 10% trailing, position caps, weekly buy cap, and cold-start rule all worked as intended this week and are unchanged. A 3rd same-pattern NVDA-style stop-out escalates this to a hard rule. (Deliberately surgical: alpha was +2.24% this week — a winning week is not a license to over-tune.)
