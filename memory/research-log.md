# Research Log

**Append-only by date.** Most recent entries at the top.

Each routine appends its research here. Use this as thinking space. The weekly review reads back over this to identify patterns.

Format:

```
## YYYY-MM-DD HH:MM CT — {routine name}

### Market context
Futures, overnight moves, major headlines, macro prints.

### Portfolio watch
Each open position: any news, catalyst, red flags.

### Buy candidates
Symbol — thesis — which strategy signals hit — conviction (high/med/low).

### Sell candidates
Symbol — which sell signal — urgency.

### Day summary (market-close routine only)
Portfolio close value, day P/L, SPY day P/L, alpha, trades placed, what worked / what didn't.
```

---

## 2026-05-27 06:00 CT — pre-market

**Timing note:** First live routine since secrets were restored (the 4/22 market-open and midday routines both HALTED on missing keys, so the planned NVDA starter was never executed — and that context is now ~5 weeks stale, so this is a clean-slate scout, not a resume). APIs verified live: Alpaca 200 (account, positions, clock, market data), Perplexity 200 (3 sub-agents). Market closed, next_open 2026-05-27 09:30 ET. Account: **equity $99,840.95, all cash, 0 positions** (essentially the full ~$100K seed still uninvested). Three sub-agents fanned out in parallel — macro, earnings, opportunity scout.

**⚠️ Price-source discrepancy (important):** The scout's Perplexity prices came back anchored near training-era levels and were badly stale on several names. I re-pulled Alpaca latest-trade as the authoritative tradeable price. Use ALPACA numbers below. Re-verify all next-earnings dates against IR pages before any order.

| Symbol | Scout (Perplexity, stale) | Alpaca latest trade (authoritative) |
|---|---|---|
| LLY | ~$840 | **$1,066.70** |
| GOOGL | ~$175 | **$388.13** |
| AVGO | ~$424 | **$422.82** (matched) |
| AMD | ~$165 | **$504.51** |
| NOW | ~$760 | $99.98 — **ANOMALOUS, distrust** (ServiceNow trades ~$900+; bad/stale tick) |
| SPY | — | $750.46 |

### Market context
Tape is **mildly risk-on** into the open, but thin conviction and a couple of cross-currents.
- **Futures:** ES +0.10%, NQ +0.07% — flat-to-slightly-green.
- **Rates:** 10Y ~4.56% (−1 bp), 2Y ~4.8–4.9% (mild curve inversion). Levels approximate per Perplexity — not exact intraday stamps.
- **FX/Commodities:** DXY softer (~104–105, drifting lower). **WTI crude ~$113.70, +1.15% — elevated; this is the inflation/energy cross-current to watch.** Gold ~$4,669, +0.4%.
- **Global:** Asia mixed-to-up (Hang Seng +2.04%, Nikkei flat). Europe green (DAX +0.69%, FTSE +0.71%).
- **Headlines:** (1) Indices drifting near records on AI/chip strength; (2) easing Middle-East tension / US-Iran negotiation optimism lifting risk appetite; (3) hawkish Fed backdrop — April FOMC minutes flagged sticky inflation, further tightening on the table; (4) inflation expectations sticky (UMich 1yr 4.8%); (5) firm crude keeps energy/inflation watch alive.
- **Scheduled US data today:** none firmly confirmed for 2026-05-27 (Perplexity pattern-guessed Durable Goods / Pending Home Sales / EIA — treat as indicative, not verified).
- **Net:** mildly risk-on; biggest swing factor is geopolitics (US-Iran headlines) against a still-hawkish Fed; high oil is the cross-current.

### Portfolio watch
No open positions. $99,840.95 cash, 0 positions, daytrade_count 0. Nothing to manage, no stops to roll. Buying capacity for up to 5 positions; week-buy counter resets fresh (max 3 new buys this week).

### Earnings calendar (2026-05-27)
- **No large-cap ($10B+) US name confirmed reporting today**, BMO or AMC. Two independent Perplexity passes both failed to confirm any megacap for 5/27. Today is **macro-driven, not earnings-driven.**
- **COST (Costco) confirmed for TOMORROW 2026-05-28 AMC** — not today. A consumer-spend tape-setter to watch Thursday; do NOT open COST inside its 3-day earnings blackout.
- Names that *historically* print late-May/early-June but were **NOT confirmed for today** (do not treat as fact): SNPS, HPE, PANW, AVGO, CRWD, MDT, NTAP. These feed into the blackout checks below.

### Buy candidates (signals matched + conviction)
Signal key: 1=earnings beat last wk, 2=catalyst <30d, 3=secular tailwind, 4=upgrades/insider buys <2wk, 5=sector rotation, 6=clear uptrend. Need ≥2. (Note: no name hits signal 1 today — there were no recent prints — so these lean on 3/4/6.)

1. **LLY — $1,066.70 — signals 3, 4, 6 — conviction HIGH.** GLP-1/obesity secular tailwind (Zepbound/Mounjaro demand), multiple analyst price-target hikes in May, strong uptrend near record highs. Next earnings **Aug 5 — well clear of the 3-day blackout.** Cleanest fit on the board; the only name simultaneously hitting tailwind + upgrades + price-trend with zero near-term earnings landmine. At ~$1,067/share a 15% target (~$15K) ≈ 14 shares.
2. **GOOGL — $388.13 — signals 3, 4, 6 — conviction MED-HIGH.** AI/Cloud + Gemini momentum + ad strength; bulge-bracket PT hikes post-Q1; near highs. Next earnings **Jul 23 — clear.** No near-term earnings risk.
3. **AVGO — $422.82 — signals 3, 4, 6 — conviction MED.** AI accelerator/custom-silicon + networking demand; mid-May target hike; uptrend above 50-day. Next earnings **~Jun 12 (VERIFY) — ~12 trading days out, outside blackout for now**, but would need to be exited or consciously held before that print.
4. **AMD — $504.51 — signals 3, 4, 6 — conviction MED.** Data-center GPU pipeline ramp; mid-May upgrades/PT hikes; uptrend. Next earnings **~Jul 30 — clear.**
5. **NOW — price ANOMALOUS — conviction LOW / PARKED.** Enterprise-AI/workflow tailwind thesis is fine, but Alpaca returned $99.98 for NOW which can't be right for ServiceNow — drop until price is re-verified. Weakest of the five regardless.

**Excluded:** PLTR (signal strength unverified), CRWD (no recent beat + next ER ~Jun 4 leaves a thin window), PANW (3-month trend flat — fails uptrend signal 6 — and ER ~Jun 3 near), NVDA (reported May 20, now drifting lower — fails uptrend signal 6).

**Net plan for the 09:30 open (market-open routine):** No clean signal-1 (fresh-beat) name today, but **LLY is a genuine ≥3-signal HIGH-conviction setup with a clean earnings runway.** Recommend the market-open routine: (a) re-pull live Alpaca quotes for LLY/GOOGL/AVGO/AMD and re-verify AVGO's Jun-12 date; (b) if macro tone is still constructive at the open (ES not sharply red, oil not spiking hard), **initiate LLY at ~15% (~$15K, target-size for high conviction) with the −7% hard stop** as the first position; (c) optionally add GOOGL as a second med-high name at ~10–12% if it confirms; (d) keep ≥2 of the 3 weekly buys in reserve and hold the 10–20% cash buffer. If futures flip sharply risk-off or oil gaps up hard pre-open, scale back to LLY-only or pass.

### Sell candidates
None — no open positions.

### Notes / research gaps to close next routine
1. **Re-verify earnings dates** for AVGO (~Jun 12), CRWD (~Jun 4), PANW (~Jun 3), ORCL (~Jun 10) against IR pages — these June reporters drive blackout timing.
2. **Confirm NOW's real price** — the $99.98 Alpaca tick is almost certainly bad/stale; don't act on it.
3. Perplexity data quality was weak this run (two of three follow-up calls partially refused; prices stale). Anchor all prices to Alpaca latest-trade, not Perplexity.
4. Watch crude — WTI ~$114 is high enough to be an inflation cross-current; a further spike flips the risk-on tone.

---

## 2026-04-22 12:00 CT — midday (HALTED)

### Halt reason
Same as this morning's market-open: `ALPACA_API_KEY`, `ALPACA_SECRET_KEY`, `ALPACA_BASE_URL`, `PERPLEXITY_API_KEY` all empty and no `./.env`. Per CLAUDE.md guardrail, halted before any API call.

### No actions taken
- No Alpaca calls (positions, prices, orders, stop-management).
- No Perplexity news-check on any drawdown (there's no live positions data to know if there's a drawdown anyway).
- No new buys (moot — can't confirm price, daily-loss cap, or position count without Alpaca).
- Portfolio unchanged: assumed still $100K cash / 0 positions from 2026-04-21 19:00 CT.

### Pattern note
Second halt in a row (market-open 08:30 also halted for the same reason). If this keeps up through market-close, the whole 4/22 session is a no-op — fine, since we have no open risk, but the user needs to restore secrets before any routine can actually trade.

### Next steps
Once secrets are set: run a fresh pre-market-style scout before executing the old NVDA starter plan. Don't trade off last night's context — tape will have moved.

---

## 2026-04-22 08:30 CT — market-open (HALTED)

### Halt reason
Required env vars missing: `ALPACA_API_KEY`, `ALPACA_SECRET_KEY`, `ALPACA_BASE_URL`, `PERPLEXITY_API_KEY`. No `./.env` file and no env vars set in the cloud environment. Per CLAUDE.md guardrail ("If a required var is empty, halt, write a clear error to `memory/messages.md`, and stop"), aborted before any API call.

### No actions taken
- No Alpaca calls (clock, account, positions, orders).
- No Perplexity calls.
- Portfolio snapshot unchanged (no live data to refresh it with). Paper account assumed still $100K cash / 0 positions from last known state.
- Planned NVDA starter ($5K) from last night's scout re-run is deferred — will need a fresh pre-market re-validation once secrets are back, since "if futures risk-off, pass" was part of the plan and we have no way to check futures from this routine.

### Next steps
Once secrets are set, the next routine (midday-check or next pre-market) should re-scout — don't blindly execute last night's NVDA plan on stale context.

---

## 2026-04-21 19:00 CT — pre-market (for 2026-04-22 open) — re-run

**Timing note:** Second pass for the Wed 4/22 open, after the 17:00 CT pass flagged too many `n/a`s to act on. APIs verified live (Alpaca 200, Perplexity 200). Three sub-agents fanned out in parallel — macro, earnings, opportunity scout. Account unchanged: $100K cash, 0 positions.

### Market context
Tape shifted **mildly risk-off** vs the earlier bullish futures read.
- **ES (Jun'26):** ~7,165.75, **−0.13%** evening session (was ~+0.35% at 17:00 CT — faded).
- **NQ (Jun'26):** ~flat to +0.05% evening.
- **US 10Y Treasury:** 4.294%, **+4.4 bps** on the day (range 4.236 – 4.319). Bonds sold off.
- **Crude:** direction up on "Iran concerns" headlines; WTI/Brent exact levels `n/a`.
- **DXY, Nikkei, Hang Seng, European closes:** `n/a` — Perplexity sparse on these; not actionable.
- **Headline flow:** Iran/Middle East risk premium flipped the intraday tone — early equity gains erased, crude spiked, rates up. No Fed speaker, CPI/PPI, or tariff print surfaced in this window.
- **Net:** mildly risk-off. Iran/oil is the live wire. Secondary watch: does 10Y hold above 4.30% at Wed open.

### Portfolio watch
No open positions. $100K cash, $200K buying power (cash-only / no leverage per strategy).

### Earnings calendar (2026-04-22)
Contradicts the 17:00 CT pass — worth flagging.
- **Fresh Perplexity (sonar-pro) returned no confirmed $10B+ US earnings for 4/22, BMO or AMC.** Names that *may* report BMO per an Interactive Investor preview dated 4/17 (unconfirmed for 4/22 specifically): **MMM, GE, UNH, EL, XOM, MRNA**. Consensus EPS/rev not supplied.
- **TSLA AMC 4/22** was asserted in the 17:00 CT pass but was NOT confirmed in tonight's fresh pull. Source contradiction — do not treat TSLA as a confirmed tape-setter until verified tomorrow morning.
- **4/21 AMC mega-cap prints (MSFT / GOOGL / META / AMZN / NVDA):** none reported per tonight's pull.
- **Guidance-risk call:** low-conviction — with no confirmed mega-cap print, Wednesday is more likely to be macro-driven (Iran / rates) than earnings-driven.

### Buy candidates

Scout verified next-earnings dates on 3 of 10 seed names; the rest came back `n/a` on critical fields — strategy says do not propose without verification. Documenting honestly.

- **NVDA — AI-infra leader, clean earnings runway.** Signals: (3) secular AI-infra tailwind (Blackwell ramp, cap-ex cycle). Next earnings **2026-05-20 AMC (confirmed)** — ~21 trading days out, outside the 3-day blackout. **Conviction: med.** Only 1 hard signal verified tonight; the earnings date is inbound catalyst but not near-term. Prefer a pullback entry; do not chase.
- **AVGO — AI ASIC/networking play, widest earnings window.** Signals: (3) custom-silicon + VMware AI tailwind. Next earnings **2026-06-03 (confirmed)** — 6+ weeks out. **Conviction: low–med.** Single verified signal; would upgrade with a verified upgrade or insider-buy tomorrow.
- **PLTR — AI/defense software, earnings in 9 trading days.** Signals: (3) AI + gov tailwind. Next earnings **2026-05-04 AMC (confirmed)** — 9 trading days out (clear of 3-day blackout but close). **Conviction: low.** High multiple risk into the print; any entry now must be size-to-trim-before-5/1 OR hold-through willingness.
- **GOOGL, MSFT, CRWD, PANW, BE, LLY, NOW** — earnings dates and fresh catalysts unverified in tonight's 3 Perplexity calls. **MSFT and GOOGL historically print late April** — treat as likely inside/adjacent 3-day blackout until a date is confirmed. **Do not open GOOGL or MSFT at Wed open without an explicit earnings-date check.**

**Net:** no clean ≥2-signal-verified buy tonight. **NVDA is the only name with verified runway + a real tailwind.** Strategy explicitly prefers patience; recommend at most a **starter tranche (1/3 of target size, ~5% of portfolio ≈ $5K)** in NVDA at Wed open IF macro tone is constructive, and re-run the scout after tomorrow night's close with a better-pulled watchlist. If pre-open futures are still risk-off (ES < flat, 10Y > 4.30, WTI gapped up), **pass entirely.**

### Sell candidates
None — no positions.

### Notes / research gaps to close next routine
1. Verify TSLA 4/22 AMC print — source contradiction between 17:00 and 19:00 CT passes.
2. Pull MSFT and GOOGL next-earnings dates explicitly (likely inside late-April blackout window).
3. Get WTI/Brent cash levels and DXY at open — macro still has too many `n/a`s to size rate-sensitive names.
4. Perplexity sonar-pro with low search context was thin tonight. Consider raising context size for the scout call (`search_context_size: "medium"`) if budget allows — but batch tickers to keep the call count down.

---

## 2026-04-21 17:00 CT — pre-market (for 2026-04-22 open)

**Timing note:** Routine fired ad-hoc, not at scheduled 6:00 AM CT slot. Alpaca clock confirms market closed; next_open = 2026-04-22 09:30 ET. Treating this as pre-market prep for Wednesday's session. Account is fresh ($100K cash, no positions) — this is Bull's first research pass.

### Market context
Mildly **risk-on** into Wed 4/22 open, low conviction.
- **ES ~+0.35%, NQ ~+0.05 to +0.40%** late Tuesday (E-mini S&P/Nasdaq). Earlier-session weakness (-0.4%) faded on Mid-East peace-deal progress headlines.
- **Dominant narrative:** US–Iran / Middle East de-escalation hopes lifting futures. Oil moves are the swing factor — a re-spike would flip sentiment to mixed.
- **Data gaps:** Perplexity returned n/a for 10Y yield, DXY, WTI/Brent levels, and Asia/Europe indices. Not confident on rate direction — avoid sizing up rate-sensitive names until a fresh cash-session print.
- No Fed commentary, CPI/PPI, tariff, or mega-cap earnings surprise surfaced since Tuesday's close.

### Portfolio watch
No open positions. Nothing to watch. $100K cash, $200K buying power (2× margin, but strategy is cash-only / no leverage).

### Earnings calendar (2026-04-22)
- **BMO:** BSX (Boston Scientific) — consensus EPS ~$0.555. Watch Farapulse / PFA adoption, Watchman utilization, hospital capex commentary. Med-tech tone-setter.
- **AMC:** TSLA — consensus EPS ~$2.61, revenue ~$10.81B (directional — source numbers were noisy). Key watches: auto gross margin ex-credits, delivery trajectory, Optimus / FSD / robotaxi commentary, AI infra capex. Biggest single tape-setter for Thursday sentiment.
- **Calendar unconfirmed:** IBM, T, NOW, CMG, LRCX, GD are commonly on this slate historically — sub-agent could not verify. Cross-reference needed before treating as tradeable.
- **Post-close 4/21 reports:** data thin; no confirmed mega-cap AMC prints to front-run tomorrow.

### Buy candidates

Research pass was sparse — two Perplexity calls yielded only one fully specified candidate, and that one is blocked by strategy rules. Documenting the state honestly rather than forcing low-conviction picks.

- **AMZN (~$205, ~$2.2T mcap)** — Signals hit: (3) secular AI/AWS tailwind; partial (1) Q4 beat with AWS +24% YoY. Next earnings ~2026-04-30. **EXCLUDED** — inside the 3-trading-day earnings window per strategy rule. Revisit post-print on May 1.
- **BE (Bloom Energy)** — Signals (6) strong uptrend, (3) fuel-cells-for-AI-data-center narrative. Earnings date unverified. **LOW/MED conviction**, catalyst is generic. Needs a verified earnings date and a specific near-term catalyst (contract announcement, capacity expansion) before entering.
- **CAR (Avis)** — Up ~+382% in 30 days per scout. **SKIP.** Momentum-alone, no catalyst, smells short-squeeze / meme-adjacent. Strategy explicitly forbids.
- **NVDA, AVGO, PLTR, GOOGL, CRWD, PANW** — scout returned n/a on critical fields (catalysts, earnings dates, current price confirms). Insufficient to propose. Next pre-market routine should pull NVDA/AVGO earnings dates directly from Alpaca and query Perplexity more narrowly.

**Net:** no high-conviction buy for 4/22 open from this scan. Better to wait and do a better-focused scan tomorrow than to force a mediocre entry on Bull's first trade.

### Sell candidates
None — no positions.

### Notes / research gaps to close next routine
1. Get actual 10Y yield, DXY, WTI, Brent levels at open — macro digest had too many n/a's.
2. Pull next-earnings dates directly from Alpaca calendar API before asking Perplexity for thesis — avoids wasting calls.
3. Build a small seed watchlist (NVDA, AVGO, GOOGL, MSFT, PLTR, CRWD, PANW, BE, LLY, NOW) so the opportunity scout has a concrete set to research rather than fishing open-universe.
