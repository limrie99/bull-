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
7. **Smart-money accumulation, confirmed by filing data** (Equibles, `scripts/equibles.md`; requires `EQUIBLES_API_KEY`, silently unavailable otherwise): at least TWO of — (a) insider cluster buying (multiple distinct insiders, open-market Form 4 buys), (b) institutions adding quarter-over-quarter (13F), (c) short interest flat or falling while (a)/(b) accumulate. **No double-counting with #4:** if insider buying is the only evidence, it counts once, as #4 — #7 needs the multi-source confirmation. Corroborating signal only: it never buys alone and changes nothing about the 2-signal + Conviction ≥70 gate.

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

## Cash-deployment / market-floor policy (added 2026-08-07 — Lauren APPROVED Option B; cash-band amended 2026-08-27)

**Standing decision (Lauren, 2026-08-07): "go forward" with Option B — add an S&P 500 market floor for idle cash.** This resolves the cash-drag question escalated on 7/31 and re-escalated 8/7. Rationale on the record: for a beat-SPY mandate, holding ~75% idle cash while SPY rises is a structural bet *against* the benchmark — it turned a +2.32-pt cumulative lead into −0.35 in two up-weeks. The floor makes idle cash *match* the index instead of dragging against it, while the conviction sleeve still hunts alpha.

**Standing decision (Lauren, 2026-08-27 ~20:20 CT): "start spending some cash" / "keep a safe 10k" / "your job is to invest."** Same class as the 8/7 "go forward" approval — explicit owner instruction, not a silent edit. The 8/7 Option B *instrument* (SPY/VOO floor) stays; the *cash-band* does not. Official policy had been targeting ~50–55% cash, which is why ~$49k / ~49% at the 8/27 close looked "in band" even though it is cash-drag vs the beat-SPY mandate. Unmerged PR 119 proposed 30–40% cash; Lauren's number supersedes both: keep about **$10,000 cash** (~10% of a ~$100k book) — the low end of the existing 10–20% whole-book buffer — and deploy the rest.

**Rules for the market floor:**
- **Instrument:** SPY (preferred) or VOO — a broad S&P 500 index ETF. Long-only, large-cap, liquid — breaks no guardrail.
- **Target:** whole-book cash of about **$10,000, i.e. ~10% of equity.** Never hold ~50% idle by default. Never deploy so much that total cash falls below the **10% floor** of the existing **10–20% minimum buffer**. Idle cash above that band is authorized for the existing SPY market-floor sleeve. Size the next tranche from **live prices**. A further small add is fine if cash is still above ~$10k after the first fill.
- **The floor is its OWN sleeve, NOT a conviction pick.** Therefore it is **exempt** from: (a) the ≤20%-per-single-position cap (it is a diversified index, not single-company risk — a single SPY lot may exceed 20% of equity), (b) the max-5-positions cap, and (c) the max-3-buys/week cap. Those three caps govern individual stock picks; the index floor does not consume their budget. The **10–20% minimum cash buffer still applies** to the whole book (target the ~10% / ~$10k low end; never breach it).
- **NO stop on the floor.** Do **not** place a −7% hard stop or a 10% trailing stop on the index floor. Stopping out of the benchmark just re-creates the cash drag we are fixing and locks in a low. The floor is buy-and-hold-the-market; it is meant to track SPY through drawdowns, not exit them. (This is the one deliberate carve-out from the −7%/trailing-stop guardrails, and it applies ONLY to the index-floor sleeve — every individual stock keeps its stops exactly as before.)
- **The ≥70 Conviction gate is UNCHANGED and was NOT lowered.** The floor is explicitly the alternative to loosening the quality bar: idle cash matches the market via the index while the stock sleeve keeps requiring 2+ signals AND Conviction ≥70. We do not force-buy mediocre individual names — or falling knives — to deploy cash. If a stock (e.g. BJ) independently clears the gate on a **clean entry**, it may use some of the deploy budget; any idle remainder still goes to SPY.
- **Execution (next session that can actually trade: Fri 2026-08-28):** enlarge the existing SPY floor so whole-book cash lands near ~$10k. Compute exact shares at the live price; log the fill to trade-log.md like any buy (note "MARKET-FLOOR / index sleeve, no stop"). **Jackson Hole:** Fed Chair Warsh's keynote is Fri 8/28 ~10:00 ET / 9:00 CT. Prefer placing the tranche at midday after the speech if the open is chaotic; if the tape is orderly, market-open Fri is allowed. If Lauren countermands in inbox first, stand down. Weekend/overnight veto window is open until then. Do not invent fills; paper only.
- **Rebalance:** if the stock sleeve later grows (new ≥70 buys) such that total cash would drop below the 10–20% buffer (i.e. below the ~10% / ~$10k floor), trim the floor first to make room — the floor is the shock-absorber, conviction picks take priority for the alpha budget.

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

- **2026-08-27 (evening CT, per Lauren: "start spending some cash" / "keep a safe 10k" / "your job is to invest") — RULE CHANGE: cash-deployment target moves from ~50–55% to about $10k / ~10% of equity.** Same class as the 8/7 "Edit strat to go forward" approval — explicit owner instruction, not a silent edit. Why cash looked high: the official 8/7 Option B band still targeted ~50–55% cash, so ~$49k / ~49% at the 8/27 close was "in band" even though it is cash-drag vs the beat-SPY mandate; unmerged PR 119 ("Put more idle cash into the S&P 500 floor") proposed 30–40% and is superseded. What this changes: (1) target cash is now about **$10,000 (~10% of a ~$100k book)** — the low end of the existing 10–20% whole-book buffer — never hold ~50% idle by default, never go below the 10% floor; (2) idle cash above that band is authorized into the existing SPY market-floor sleeve, sized from live prices at the next session that can trade (Fri 8/28); prefer midday after Warsh's Jackson Hole keynote (~10:00 ET) if the open is chaotic, otherwise market-open Fri is allowed; a further small add is fine if still above ~$10k after the first fill. What this deliberately does NOT change: the **≥70 Conviction gate and 2-signal rule are untouched** (do not force-buy BJ/ROST or any falling knife to "spend cash"; a name that independently clears the gate on a clean entry may use some of the deploy budget, idle remainder goes to SPY); the floor remains its own sleeve (no stop; still exempt from ≤20% / max-5 / max-3-per-week); JPM/LLY stops, conviction rubric, and all other guardrails unchanged. Paper only — this edit places no Alpaca order.
- **2026-08-24 (per Lauren, in-session: "great add that") — ADDITIVE CHANGE: new data source (Equibles) + buy signal #7 (smart-money accumulation).** Added `scripts/equibles.md` (filing-grade data: insider Form 4s, 13F institutional holdings, FINRA short interest, XBRL fundamentals, congressional trades — free tier, 100 requests/day, with a keyless SEC EDGAR fallback), wired it into the pre-market sub-agent team (fundamental analyst, sentiment analyst, opportunity scout + a new smart-money screen), and added **signal #7** above. Why: the Fundamental and Sentiment conviction dimensions and signal #4's insider-buying half were previously scored off Perplexity web searches — this replaces guesses with filing-cited primary data, mirroring how sibling Maverick added its #7/#8 signals. What this deliberately does NOT change: the buy-gate (2+ signals AND Conviction ≥70) is untouched; #7 is corroborating-only, can never buy alone, and cannot double-count with #4; all stops, caps, and sizing rules unchanged. The integration is inert until `EQUIBLES_API_KEY` is set in the routine environment (optional var — routines skip it silently when empty).
- **2026-08-07 (later, per Lauren's live reply "Edit strat to go forward") — RULE CHANGE: adopted Option B, the S&P 500 market-floor policy.** Added the new "Cash-deployment / market-floor policy" section above. Lauren approved deploying idle cash into a broad S&P 500 ETF (SPY/VOO) so it *matches* the benchmark instead of dragging against it — the fix for the cash-drag pattern that erased the cumulative lead (see the governance record immediately below). What this changes: (1) idle cash gets parked in an index floor targeting ~50–55% total cash, initial tranche ≈20% of equity; (2) the floor is its own sleeve, **exempt** from the ≤20%-single-position / max-5-positions / max-3-buys-per-week caps (those govern conviction stock picks, not a diversified index); (3) the floor carries **no −7% or trailing stop** — the one deliberate stop carve-out, index-sleeve only, because stopping out of the benchmark just re-creates cash drag. What this deliberately does NOT change: the **≥70 Conviction gate and 2-signal rule are untouched** (the floor is the alternative to lowering the bar, not a lowering of it); every individual stock keeps its −7% hard stop / 10% trailing stop exactly as before; the 10–20% minimum whole-book cash buffer still holds. Execution deferred to the **Mon 2026-08-10 market-open** routine (market was closed at the time of this edit), with a weekend veto window for Lauren. This is a genuine philosophy shift (owning the index we aim to beat) and it was made by the account owner's explicit instruction, not a silent edit.
- **2026-08-07** — **NO rule changed. Governance record: the cash/deployment escalation FIRED a 2nd time (worse), cumulative alpha went NEGATIVE for the first time, and I RE-ESCALATED the A/B decision to Lauren rather than acting unilaterally.** Week ending 8/7: SPY melted up +3.53% (soft-NFP rate-cut rally) while our ~75%-cash book made only +0.81% → **−2.72 alpha, the 2nd CONSECUTIVE down-alpha week** (7/31 −2.87) and 4th same-cause week (7/3, 7/10, 7/31, 8/7). The invested sleeve (JPM +1.62%, DE +4.79%) roughly MATCHED SPY — the entire miss is the ~75% cash, not stock-picking. **Cumulative alpha since the 5/29 base flipped from +2.32 to −0.35** — for the first time in the run we are behind SPY, which retires the "lumpy but net ahead" defense that has held the cash question at bay for four reviews. The 7/31 A/B escalation went unanswered, so per my own pre-commitment the default held (Option A — hold); holding ~75% cash into a +3.53% SPY week is exactly what erased the lead, so I updated the honest framing: **Option A is no longer costless — on an up-tape it actively loses the mandate.** Deliberately did NOT lower the ≥70 gate (it correctly benched TXN at ~63: post-beat fall + heavy insider selling = knife-catch) and deliberately did NOT unilaterally execute Option B (buying SPY/VOO is a genuine philosophy shift — owning the index we aim to beat — that belongs to the account owner; silence is not consent, and manufacturing consent by flipping the default to auto-buy would be a governance breach). Instead I re-escalated the same A/B with the new, worse facts and a stronger recommendation for a limited B, pushed as a user-decision-needed Telegram alert, keeping the default at A. This entry records the re-escalation and the negative-alpha milestone, not a strategy change. Default if still no reply: A (hold), now flagged as a costly choice, not a neutral one.
- **2026-07-31** — **NO rule changed. Governance record: the pre-committed cash/deployment escalation trigger FIRED this week and I escalated a forced A/B decision to Lauren.** Since 7/03 the cash question has been parked behind a specific forward trigger: bring Lauren a forced deploy-or-hold decision *only if the ≥70 gate stays empty WHILE SPY keeps rising*. For four weeks the second half never fired (SPY fell 7/17 and 7/24). Week ending 7/31 fired BOTH halves at once — gate empty (~38th scan) AND SPY rose +1.07% AND we lagged −2.87 (2nd-worst alpha of the run), with cash at a run-high ~75% after LLY's trailing-stop exit. Per the standing pre-commitment I did not park it again; I wrote Lauren a two-option decision (A: stay gated/cash dry; B: add an S&P 500 "market floor" for idle cash so it matches rather than drags against the benchmark) in `messages.md`, awaiting her answer in `inbox.md`. **Explicitly did NOT lower the ≥70 Conviction gate or any guardrail** — reacting to one bad week by loosening the quality bar is the over-tuning this strategy warns against; the gate correctly rejected LMT/NOC this week. The *deployment/cash-level* judgment (a genuine philosophy question — whether to own the index we aim to beat) belongs to the account owner, not a silent edit. Default if Lauren doesn't respond: **A (hold)** — it breaks no rule and changes nothing. This entry records the escalation, not a strategy change.
- **2026-04-21** — Initial seed. Paper mode. $100K paper default. Tuned to Nate's rules: -7% hard stop, 10% trailing stop activated at +5%, fundamentals-driven swing only, wealth-advisor framing with sub-agent team. Carried forward v1 30-day learnings: no short-dated options (cost $550 in v1), 10% trailing beats 2%, concentration > diversification, watch Alpaca rate limits.
- **2026-06-15** — Added the **Conviction Score (0–100) buy-gate** and a persistent scored **`memory/watchlist.md`**, ported (and reweighted) from an external trading-analysis skill pack. The skills weighted technicals 25–40%; rebalanced to 60% fundamentals+catalyst / 20% sentiment / 12% risk / 8% technical-timing to match our fundamentals-first mandate. Pre-market sub-agents now each return a 0–100 score on their dimension and the opportunity scout runs defined screens (growth / momentum / earnings-beat) instead of ad-hoc idea generation. Buy now requires **2+ signals AND score ≥ 70** — the numeric gate is meant to give a clear trigger to *act* (fighting cash-drag) while keeping the bar disciplined. No change to stops, caps, or the no-options/no-shorts guardrails.
- **2026-06-01** — Added the **cold-start / anti-paralysis rule** after a post-mortem of the 4/22→6/1 run. Root cause was infrastructure, not strategy: memory never persisted across routines (every run read 4/22 state and pushed to throwaway branches), so the agent sat 100% cash for ~18 trading days after a single −$159 NVDA round-trip, never executing any of its researched candidates. Fixed the persistence bug in CLAUDE.md (push `HEAD:main`, sync from `origin/main` at run start) and added the rule above so a stale plan can no longer mean indefinite inaction. Core guardrails left unchanged — they had no fair test.
- **2026-07-03** — **Graduated the ≤10% high-beta AI/semis starter SIZING cap from advisory/probation to a STANDING RULE** (updated the "High-beta override" bullet in Position sizing + the 2026-06-05 learning note). Trigger: the pre-committed 3rd-strike condition set on 6/05 effectively fired — ETN (high-beta AI-power, sized as a 9.6% starter *because of* this rule) trailing-stopped on 7/2 for −$211/−2.19% with thesis intact, the 3rd high-beta shake-out of the run (NVDA ×2, ETN). Kept it honest and surgical: ETN was a *trailing*-stop giveback on a matured position, not the identical NVDA *hard*-stop fresh-entry shake-out, so only the **mechanism-agnostic sizing half** graduates (smaller size → smaller loss regardless of stop type — −$211 vs −$849 proves it). The **entry-timing half stays advisory** (the fresh-beta-into-macro pattern hasn't recurred). No other change — the −7% hard stop, 10% trailing, position caps, weekly buy cap, Conviction ≥70 gate, cold-start, and cash rules all held and were untouched. Deliberately did NOT touch the gate or cash level despite a −1.58-alpha week, because the same book won +4.44 the week before (one sub-SPY week is noise, not signal); the gate/cash question is parked behind a specific forward trigger (re-evaluate only if the Jul 14 data wave still yields no qualifier while SPY keeps rising).
- **2026-06-05** — Added a **high-beta AI/semis entry-discipline learning** (see "Learnings carried forward" above) after the week-ending-6/5 review. NVDA round-tripped to a stop-out a 2nd time in five weeks (−$849 on 6/5, macro/NFP semis flush, thesis intact). The pattern is beta-driven, not thesis-driven: a high-beta name on a −7% hard stop gets shaken out on macro noise before the thesis expresses. The refinement (smaller ≤10% starter, enter on a confirmed base, don't initiate beta into a binary macro print) is **advisory and on probation** — it changes no guardrail. The −7% hard stop, 10% trailing, position caps, weekly buy cap, and cold-start rule all worked as intended this week and are unchanged. A 3rd same-pattern NVDA-style stop-out escalates this to a hard rule. (Deliberately surgical: alpha was +2.24% this week — a winning week is not a license to over-tune.)
