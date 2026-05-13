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

## 2026-05-13 06:00 CT — pre-market (for today's open)

**Timing:** 6:00 AM CT, Wed 2026-05-13. US market opens 8:30 CT / 9:30 ET (~3.5h to go). Alpaca clock confirms `is_open=false`, `next_open=2026-05-13T09:30-04:00`. APIs verified live. Account: **$99,840.95 cash, 0 positions, equity $99,840.95** (small ~$159 drift from $100K base — Alpaca paper adjustment, no positions, no trades booked since 4/21). Three sub-agents fanned out in parallel — macro, earnings, opportunity scout. No position analyst spawned (no holdings).

### Market context

Tape tone: **mixed-to-slightly-constructive, low conviction** — futures are quiet, and most rates / FX / commodity inputs came back `n/a` from Perplexity tonight.

- **ES (S&P 500 e-mini):** ~7,452.75, **+0.14% to +0.35%** vs Tue 5/12 cash close (7,425.75).
- **NQ (Nasdaq-100 e-mini):** ~29,132.25, **~−0.13%** (cash-close reference n/a).
- **US 10Y yield, DXY, WTI, Brent:** `n/a` — Perplexity sparse on these tonight. Will supplement with TLT / UUP / USO quote pulls intraday if any of today's candidates are rate-sensitive (LLY healthcare semi-sensitive, RTX defense relatively immune).
- **Asia / Europe (Nikkei, Hang Seng, Stoxx 600, DAX):** `n/a`.
- **Macro headlines / Fed / data:** `n/a` — no scheduled US data, Fed speakers, or auctions surfaced. **Caveat:** the macro signal is thin tonight; weight this digest accordingly.
- **Net read:** ES mildly bid + NQ flat-to-soft = an undecided, slightly risk-on-leaning tape. Safe enough to act on a high-conviction single name at **partial (starter) size**, but do NOT chase or size up at the open. Re-check rates and dollar from a cash-session quote before pulling a trigger.

### Portfolio watch

No open positions. **$99,840.95 cash, $199,681.90 RegT buying power** (cash-only / no leverage per strategy). Nothing to manage, no stops to adjust.

### Earnings calendar (2026-05-13)

- **BMO 2026-05-13:** No confirmed large-cap ($10B+) US prints surfaced by Perplexity tonight. ~204 total reports today (per Stock Analysis), but nothing in our universe.
- **AMC 2026-05-13:** **CSCO (Cisco)** is historically expected this slot but Perplexity could **not confirm a 5/13 AMC date** — treat as expected-but-unconfirmed. Wall Street focus historically: networking demand, Splunk integration, AI-infra orders, gross margin guide. If it prints, networking/enterprise-software peers (ANET, JNPR, NTAP) will react after 4 PM ET. **No size in CSCO or peers today** — 3-day earnings blackout applies to any name *we'd buy* with a print inside the window, but more importantly CSCO is the only tape-setter and we don't want to be long it pre-print.
- **Yesterday AMC (2026-05-12):** No mega-cap US prints. NVDA is calendared **5/20 AMC** (next week, still 5 trading days out — outside our 3-day blackout but close).

**Tape implication:** Today is **macro-driven, not earnings-driven**. Open should trade on overall risk flow; real single-name catalyst (if it happens) is CSCO AMC.

### Buy candidates

Opportunity scout returned 5 names; all clear the 3-trading-day earnings blackout. I'm flagging conviction levels and which buy signals are *independently verified* by the scout.

- **RTX (RTX Corp, Defense/Aerospace)** — ~$115, ~$155B mcap
  - Signals matched: **(1) earnings beat + raised guide** (Q1 beat, FY26 guide +$500M), **(3) secular defense tailwind**, **(4) analyst upgrades** (MS Overweight $145, Citi Buy $150 on 5/8), **(6) clear uptrend**. **Four signals — strongest of the list.**
  - Next earnings: ~2026-07-22 (~10 weeks out — clear).
  - Conviction: **high**.
  - Risk: Pratt engine inspection overhang; a surprise cost disclosure could shave a few percent.
- **AVGO (Broadcom, Semis / AI infra)** — ~$422, ~$1.95T mcap
  - Signals matched: **(3) AI-infra secular tailwind** ($15B+ AI revenue run-rate via custom ASIC), **(4) analyst upgrades** (Goldman Buy, JPM Overweight in early May), **(5) AI-infra sector rotation**, **(6) uptrend near highs**. Four signals.
  - Next earnings: 2026-06-03 (21 days out — clear).
  - Conviction: **high**.
  - Risk: AI capex narrative crowded — any hyperscaler capex cut headline tags the whole basket.
- **LLY (Eli Lilly, Healthcare / GLP-1)** — ~$825, ~$785B mcap
  - Signals matched: **(2) near-term catalyst** (orforglipron oral GLP-1 PDUFA **2026-06-15**), **(3) GLP-1 tailwind**, **(6) uptrend near highs**. Three signals.
  - Next earnings: ~2026-08-06 (~12 weeks out — clear of blackout, but PDUFA inside the swing window is the real event).
  - Conviction: **high but binary** — treat as catalyst trade, size accordingly (half-size).
  - Risk: FDA outcome is binary; delay or label restriction could be a 5–8% gap.
- **PLTR (Palantir, AI software)** — ~$28, ~$65B mcap
  - Signals matched: **(3) AI/gov tailwind**, **(4) CEO insider buy** (Karp 500K shares 5/7) + Wedbush Outperform PT $55, **(6) uptrend near 52-wk high**. Three signals, plus insider buying which is rare and high-quality.
  - Next earnings: ~2026-08-04 (~12 weeks out — clear).
  - Conviction: **high**, but extended — prefer a pullback entry.
  - Risk: high beta / multiple; a tech risk-off day amplifies drawdown.
- **LMT (Lockheed Martin, Defense)** — ~$465, ~$110B mcap
  - Signals matched: **(2) catalyst** ($4.2B Army F-35 / hypersonics contract 5/6), **(3) defense tailwind**. Two signals, but **fails (6) uptrend** — below 50DMA, >10% off highs.
  - Conviction: **low — skip.** Strategy says we don't catch knives. Re-check after a chart base.

**Net plan for today's open:**
- **If macro is constructive at 8:30 CT cash open** (ES still green, no fresh geopolitical/rates shock):
  - **Lead with RTX as the size-first name** (~12–15% of equity, ~$12K–$15K) — beat+raise + upgrades + tailwind + uptrend is the cleanest 4-signal setup we've seen since Bull v2 began. Place with a hard −7% stop bracket.
  - **Pair with AVGO** (~10–12%, ~$10K–$12K) for AI-infra exposure that isn't NVDA-concentrated.
  - That uses **2 of 3 weekly buys** and ~$25K of $100K — leaves dry powder for LLY (catalyst trade) later in the week or for a pullback in PLTR.
- **If futures roll over** (ES < flat, or a rates/oil shock prints overnight): **pass entirely**; better to do nothing than chase.
- **Do NOT** open CSCO, ANET, JNPR, NTAP, or other networking names today — CSCO print risk.
- **Do NOT** open LMT today — fails uptrend rule.

### Sell candidates

None — no positions.

### Notes / research gaps to close next routine

1. Verify CSCO 2026-05-13 AMC print before close routine — if it does report, watch networking complex for any post-close move.
2. Confirm RTX and AVGO current prices and 50DMA position via Alpaca quotes at the market-open routine (8:30 CT) before sizing.
3. Pull 10Y, DXY, WTI directly from Alpaca proxies (TLT, UUP, USO) tomorrow morning — macro signal was thin tonight.
4. Re-check LLY PDUFA date (2026-06-15) via official FDA calendar — Perplexity is fine for thesis but a binary catalyst date deserves a primary-source check before sizing.

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
