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

## 2026-05-26 06:00 CT — pre-market (first session after Memorial Day)

**Timing note:** Routine fired on schedule. Alpaca clock confirms market closed, next_open = 2026-05-26 09:30 ET (~2.5h away). Account is back online — secrets restored after the 4/22 halt cluster. Cash $99,840.95, 0 positions, 0 open orders. Account effectively unchanged for ~5 weeks. **First real research pass in over a month.** Three sub-agents fanned out in parallel: macro, earnings, opportunity scout.

### Market context
Mildly **risk-on** into the Tuesday open, low-to-medium conviction. Asia outperformed (Hang Seng +2.04%), Europe firm (DAX +0.69%), futures slightly green.
- **ES futures:** indicative slightly green vs Friday close; exact overnight % `n/a` (sub-agent flagged sparse live data).
- **NQ futures:** indicative ~+0.07% overnight.
- **US 10Y:** 4.55%, **−3 bps** (modest bid for duration).
- **DXY:** 99.34, +0.08% — marginally firmer dollar.
- **WTI:** $96.48, +0.12%; **Brent:** ~$110, +0.4% — oil holds geopolitical risk premium.
- **Gold:** $4,669/oz, +0.40% — bid on Iran headlines.
- **Overseas:** Nikkei flat, Hang Seng **+2.04%** (standout), DAX +0.69%, FTSE `n/a`.
- **Long-weekend headlines:** US/Iran de-escalation signals (with Strait of Hormuz friction remaining); aluminum facility attacks pushed aluminum near 4-yr highs; UMich final May consumer sentiment ~48.2 (near record lows).
- **Today's US calendar:** Conference Board **Consumer Confidence (May)** is the marquee print. Fed speakers `n/a` for today.
- **Net:** mildly risk-on, but consumer-confidence risk on tap and geopolitics still the live wire. Not a "back up the truck" tape.

**SPY tape (from Alpaca):** $733.73 → $741.25 → $742.72 → **$745.64 (Fri 5/22 close)**. Up +1.6% over the week. Index is trending; we are NOT.

### Portfolio watch
No open positions. $99,840.95 cash (~$160 erosion vs $100K start — likely BP/data-fee dust, not a fill). Buying power $199.7K margin (we use cash only). Nothing to manage.

### Earnings calendar (2026-05-26)
- **BMO large-caps ($10B+):** `n/a` — sub-agent could not verify any. Calendar small-caps only (Ooma, Semtech, Champion Homes, VNET).
- **AMC large-caps:** `n/a` for today. The late-May enterprise-software gauntlet (CRM, DELL, MRVL, NTAP, ADSK, HPE) lands Wed 5/27 and Thu 5/28.
- **CRM Wed 5/27 AMC confirmed** — consensus EPS ~$3.05; will drag IGV/NOW/ADBE on Thursday read-through.
- **Fri 5/22 AMC tape-setters:** `n/a` — no verified mega-cap prints surfaced.
- **Net:** today is macro-/positioning-driven, not earnings-driven. The real risk is **tomorrow night's CRM**.

### Buy candidates

Scout's defensible 2-signal names are NVDA and PLTR. Both were stress-tested against Alpaca quote/trend data before deciding.

- **NVDA** — Signals: (1) clean beat-and-raise on 5/20 AMC (EPS $1.87 vs $1.76, rev $81.6B vs $78.4B, next Q guide $89.2–92.8B vs $86.4B Street), (3) AI-infra tailwind intact. **Signal 6 (trend) status:** last $215.33, 50-DMA ≈ $196.8 — yes, above 50-DMA. But the **post-earnings reaction was negative**: ran from $165 to $235 (+42%) into the print, then **faded −8.6% off the high** to $215.33 by Friday close. Two consecutive red days post-earnings (5/21 −1.8%, 5/22 −2%) is a textbook sell-the-news fade. A buy here at $215 with the −7% hard stop puts the stop at ~$200 — right at the 50-DMA. That's no margin of safety; we'd be one normal pullback from a flush. **Conviction: low-med. Pre-market call: PASS today; wait for a base.** Re-evaluate if NVDA closes back above $225 OR stabilizes 3 sessions above $210.
- **PLTR** — Signals: (1) raised FY26 revenue guide to **71% Y/Y, US commercial to 120% Y/Y** on 5/4, (3) AI + government-software tailwind. **Signal 6 (trend) status: FAIL.** Last $136.88, 50-DMA ≈ $140.6 — **below 50-DMA**, sideways since the print. Only 2 signals confirmed and one of the screens for "uptrend" is broken. PLTR's single-name vol also means the −7% stop trips on routine noise. **Conviction: low. Pre-market call: PASS.** Watchlist for a reclaim of $140 with volume.
- **AVGO, GOOGL, MSFT, META, AMZN, AAPL, COST, NFLX, AMD, ORCL** — scout could not verify earnings dates, recent upgrades, or specific near-30-day catalysts in this pass. **Earnings blackout risk on AVGO and CRWD** (typical early-to-mid-June prints — could be inside the 3-day window soon). Defer until verified.

**Net:** **no clean buy today.** Fresh paper portfolio is fine sitting on cash; strategy says concentration over forcing trades. Plan for the market-open routine in 2.5 hours: **likely no-trade**, just confirm tape tone and consumer-confidence reaction. The bigger setup is Wed CRM AMC — if CRM prints clean, the IGV complex (NOW, ADBE, MSFT) becomes a Thu-open opportunity.

### Sell candidates
None — no positions.

### Notes / research gaps to close next routine
1. Verify CRM Wed 5/27 AMC consensus revenue (only EPS ~$3.05 confirmed tonight). Pull guidance whisper.
2. Pull next-earnings dates for AVGO, CRWD, PANW, DELL, MRVL — blackout-risk names.
3. Get specific analyst upgrades / insider-buy data on NVDA, PLTR, COST, NFLX in last 10 days (Signal 4 was blank for all candidates).
4. Build conviction watchlist for the Thu post-CRM tape: NOW, MSFT, ADBE behavior + CRM reaction.
5. Watch NVDA price action today — does it base ~$215 or fade through to $210? Stabilization changes the calculus.

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
