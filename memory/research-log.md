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

## 2026-05-28 06:15 CT — pre-market

**Timing:** scheduled 6:00 AM CT pre-market routine, ~2h15m to open. APIs verified live: Alpaca account 200, Perplexity 200. Three sub-agents fanned out in parallel — macro, earnings, opportunity scout. Account: $99,840.95 cash, $99,840.95 equity, 0 positions, 0 open orders. (Minor $159 drift below the $100K start since 4/21 — likely a paper-account adjustment during the long quiet period; no trades have been placed yet.)

**Recovery note:** First real routine since the 4/22 secrets outage. .env now restored. Treating today as Bull's first live trade-eligible session.

### Market context

Tone: **mildly mixed / cautious risk-off-lite**, no panic.

- **ES (Jun'26):** ~7,525, **−0.2%** vs prior close.
- **NQ (Jun'26):** **−0.4 to −0.5%** — tech leading lower.
- **US 10Y:** ~**4.45%**, **lower** on the day (yields easing on softer oil / inflation expectations). Constructive for duration-sensitive growth — partial offset to the tech weakness.
- **DXY:** level n/a, inferred flat-to-slightly-stronger.
- **WTI / Brent:** levels n/a, both **down**; recent −3%+ on Middle East supply normalization / US–Iran peace-deal headlines.
- **Equity Wed close (5/27):** Dow at record high, S&P barely up, Nasdaq 100 slightly down. Mixed but not broken.
- **Headlines:** AI enthusiasm continues, lower oil, easing yields. No fresh Fed shocks, no new China/tariff escalations identified by macro sub-agent.
- **Europe / Asia:** mixed to slightly lower; specific levels n/a.
- **US data today:** weekly initial jobless claims (typical Thursday). PCE is **not** today per the macro pull — Friday this week.

**Net read:** tape probably opens slightly red, tech-led; supportive rates partially offset. Nothing today screams "size up" or "stay out" — it's a *normal trading day*, lean on stock-specific catalysts.

### Portfolio watch

No open positions. $99,840.95 cash, $199,681.90 buying power (we don't use the 2× leverage — cash-only per strategy).

### Earnings calendar (2026-05-28)

- **No confirmed today-dated US large-cap earnings** from Perplexity. Names commonly in this calendar week (COST, DELL, MRVL, ULTA, BBY, DG, HPQ, ADSK, WDAY, ZS, VEEV) are **all unconfirmed** for 5/28 specifically — Perplexity did not return verified dates or consensus EPS/revenue.
- **NVDA already printed: Wed 2026-05-20 AMC** — fiscal Q1 2027. **Beat:** EPS $1.87 vs $1.76 est (+6.3%), revenue $81.62B vs $78.42B est (+4.1%). Next NVDA print **~Aug 26, 2026** — full 90-day runway.
- **Wed 5/27 AMC mega-cap prints:** none confirmed by Perplexity — pull pre-market movers from Alpaca/news scan before market-open routine to catch any unflagged movers.
- **Guidance-risk call:** **low** today. No confirmed mega-cap print is set to whipsaw the tape this morning.

### Buy candidates

Sub-agent verdict: most of the watchlist came back with thin/unknown data from Perplexity (consistent with the v1 lesson that Perplexity's coverage of specific catalysts can be patchy — needs corroboration). Only one name clears the strategy bar with verified evidence tonight.

- **NVDA — AI infra leader, fresh clean beat.** Signals matched:
  - **(1) Positive earnings surprise:** 5/20/2026 AMC, EPS $1.87 vs $1.76 (+6.3%), rev $81.62B vs $78.42B (+4.1%). Within the "last week" window ✓.
  - **(3) Secular tailwind:** AI infrastructure / Blackwell ramp — strategy explicitly names this as one of our themes.
  - Earnings blackout: **CLEAR** — next print ~Aug 26, 2026.
  - Unverified by sub-agent: (2) near-term catalyst, (4) recent analyst upgrades, (6) trend vs 50-day MA. Market-open routine should sanity-check trend via Alpaca quote vs IEX bars before sizing the entry.
  - **Conviction: medium.** Two solid verified signals (not 3+). Strategy says medium-conviction = 10–15% sizing. Lean toward the lower end (~10–12%, ~$10–12K) on day one of a fresh-slate account — preserve room to scale up later.

- **PANW — cybersecurity tailwind.** Only signal (3) confirmed; insufficient for entry. **Defer.**

- **AVGO — DISQUALIFIED.** Reports 2026-06-03 AMC — squarely inside the 3-trading-day earnings blackout. Revisit post-print.

- **CRWD — insufficient data.** Earnings appear to have just dropped in late May — sub-agent could not confirm date or beat/miss. Top priority to verify in next routine.

- **GOOGL, MSFT, META, LLY, COST, AMZN, AAPL, NOW, PLTR** — Perplexity returned unknowns on most fields. Do not propose today. AAPL note: WWDC historically early June — potential signal #2 if a date confirms; not actionable today.

### Sell candidates

None — no positions.

### Plan for market-open (08:30 CT)

1. Re-verify pre-market futures tone — if ES gaps down >0.75% or NQ down >1%, **stand down** (daily-loss-cap spirit + don't open into a fade).
2. Pull NVDA latest quote and confirm price > 50-day MA (i.e., uptrend signal #6 alive).
3. If clear, place a **bracket buy on NVDA, ~10–12% sizing (~$10–12K)**, market order, day TIF, with stop_loss stop_price = fill × 0.93 (−7% hard stop per strategy). No take_profit.
4. Log fill price, write to trade-log, update portfolio.md.
5. Hold the other two weekly buy slots in reserve; do not force a second trade today.

### Notes / research gaps to close next routine

1. **CRWD** late-May earnings result — verify beat/miss/guide. Could be a top candidate by next pre-market.
2. **AAPL WWDC 2026 date** — typically June 9-13 window. If confirmable, that's a signal #2 catalyst.
3. **5/27 AMC movers** — sub-agent couldn't confirm; pull pre-market top-movers from Alpaca data feed before placing NVDA order.
4. **DELL / MRVL / COST exact earnings dates** this week — they're AI-server / AI-silicon / consumer bellwethers and the day-of moves will color sentiment.
5. Consider raising Perplexity `search_context_size` to "medium" for the scout call — same gap as flagged 4/21, still hurting coverage.

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
