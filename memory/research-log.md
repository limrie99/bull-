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

## 2026-05-04 06:15 CT — pre-market (for 5/4 open)

**Timing note:** First successful research routine after the 4/22 halt sequence. Account state recovered: equity $99,928, cash $94,965.50, one open position (NVDA, 25 sh @ $201.38 from 4/22 fill). APIs verified live (Alpaca 200, Perplexity 200). Four sub-agents fanned out in parallel — macro, earnings, NVDA position-watch, opportunity scout.

**Trade-log gap flagged:** NVDA buy filled 2026-04-22 15:07 UTC @ $201.38 (Alpaca order id confirms) was never written to `trade-log.md` because the 4/22 routines halted on missing secrets. Reconstructing the entry retrospectively in `trade-log.md` for future-Bull's continuity. The trailing stop conversion (orig -7% bracket → 10% trailing, hwm $216.73, current stop $195.057) also happened during the gap and is reconstructed.

### Market context

**Mildly risk-on, light data day, single-name event risk = PLTR AMC.**
- **ES (Jun'26):** ~7,262.50, **+0.06%** overnight. **NQ:** **+0.85%** overnight. NQ outperformance = AI/semis bid into the cash open.
- **US 10Y, DXY, WTI/Brent, Asia/Europe levels:** `n/a` from Perplexity tonight — sub-agent flagged data gap. Pull from Alpaca/quote feed at the open before sizing rate-sensitive trades.
- **Tape backdrop:** S&P 500 reportedly +4.5% since the late-Feb US-Iran strike, Nasdaq leading. Wartime risk premium continues to fade. Q1 2026 S&P 500 blended earnings growth running ~15.1% YoY (Tech ~46%) — earnings the dominant bullish driver.
- **US data today:** Factory Orders (March) at 10:00 ET — second-tier print, not a tape-mover unless extreme. No confirmed Fed speakers.
- **Headlines:** Berkshire annual meeting Sat 5/2 — no market-moving items surfaced. Quiet weekend.
- **Net:** mildly risk-on, but markets near record highs → chase risk is the live tactical concern. Tape is light-data; will be driven by single-name flow today and PLTR AMC tonight.

### Portfolio watch

**NVDA — 25 sh @ $201.38, current $198.50 (-1.43%, -$72). Trailing stop: 10%, hwm $216.73, stop $195.057.**
- **No material news in the last 72h** (Fri close → Mon AM). No analyst PT changes (Benchmark $250 from 3/31 and Tigress $360 from 3/5 are stale). No Blackwell pre-announce, no fresh China/H20 export-control news, no AMD/AVGO competitive launch.
- **Sector:** SOXX flat Friday (~$465, -0.16%). AI-semi cohort in wait-and-see mode ahead of NVDA's 5/20 print.
- **Earnings prep:** 5/20 AMC, 16 trading days out. Outside the 3-day blackout. Whisper / options-implied move not surfaced. Pre-print PT-bump cycle typically starts ~2 weeks out — watch for analyst preview notes this week.
- **Thesis status:** intact. Recent $216.73 → $198.50 pullback (-8.4% from hwm) reads as positioning/profit-taking, not a fundamentals break.
- **Risk for today's open:** trailing stop is at $195.057 → only **1.7% cushion** below Friday's close. A gap-down >1.7% on broad SOXX/macro weakness would auto-flush 16 days before earnings. Watch SOXX pre-market and any AMD/AVGO headline pressure. If hit, accept the exit — the trailing stop is doing its job.

### Earnings calendar (2026-05-04)

- **BMO:** No confirmed $10B+ mega-cap prints. Tape will be macro / single-name flow until the AH wave.
- **AMC:** **PLTR (Palantir)** — confirmed 5:00 PM ET webcast, company IR sourced. Watch: AI-platform commercial growth, government segment guide. **CRITICAL:** earlier research had assumed PLTR was 5/5 — corrected to 5/4. Tonight's print is the AI-software cohort tape-setter into Tuesday (PLTR, AI, SNOW, NOW, MDB).
- **Friday 5/1 AMC prints:** unconfirmed by Perplexity — flag for the market-open routine to re-check via Alpaca calendar API + a second source.
- **This week (rest):** unconfirmed by tonight's pull — re-scan needed.

### Buy candidates

Selective scan returned **one high-conviction name** plus several rejected for failing verification. Per strategy ("be selective rather than pad"), not forcing low-conviction picks.

- **CAT (Caterpillar) — Industrials / heavy equipment — ~$890.32.** **Conviction: HIGH.**
  - **Signals matched:**
    - **(1) Beat-and-raise on Apr 30:** adj EPS $5.54 vs $4.62 cons (+19.9%), revenue $17.4B vs $16.43B (+5.9% beat, +22% YoY), **raised full-year guidance.**
    - **(3) Secular tailwind:** onshoring / industrials, AND data-center power demand flowing into CAT's Energy & Transportation segment (engines/turbines for hyperscaler buildout).
    - **(6) Clear uptrend:** $890.32 vs 50DMA ~$751 (+18.5% above). Gapped up ~9.9% on print (Apr 29 close $810.5 → Apr 30 $890.58) and held into Friday.
  - **Catalyst:** post-earnings drift + analyst PT-bump cycle still unfolding; data-center read-through is the new bullish narrative for the name.
  - **Next earnings:** ~Aug 4, 2026 — well outside the 3-day blackout.
  - **Position-size suggestion:** **15% of portfolio (~$15K, ~17 shares).** High-band; lower end of the high-conviction range because it's a day-after-earnings entry (some giveback risk).
  - **Entry tactic:** limit near $885–890 at the open, NOT market-on-open chase. Bracket with -7% hard stop at ~$828.
  - **Risk to thesis:** day-after-earnings buyers can give back 3–5% on broad-tape wobble; macro flip risk-off on Iran/oil headline; CAT historically beta to global growth — watch China/EU industrial PMI for next catalyst.

- **REJECTED:**
  - **GE Aerospace** — beat Q1 EPS/rev on 4/21 but only **maintained** guidance (no raise → fails signal #1). At $286.53, **below 50DMA ~$307** (fails signal #6). Reject.
  - **MSFT, GOOGL, META, AMZN, AAPL, LLY, V, MA, AMD, PLTR, CRWD, PANW, NOW, LMT** — Perplexity returned UNCONFIRMED on whether they beat-and-raised in the 4/28–5/2 window. Strategy punishes fabricated data → not proposing names that can't be verified. Re-scan Wed AM with fresher news indexing.
  - **VRT, ETN, GEV** — could not confirm earnings results / prices / trend status.

**Net for the open:** CAT is the single clean idea. NVDA is the existing risk to manage.

### Sell candidates

None outright. Watch NVDA at the open for trailing-stop trigger ($195.057, only 1.7% cushion). If the stop hits naturally, let it work — do not intervene. Thesis intact, but stop discipline > thesis sentiment.

### Plan for the 5/4 market-open routine

1. **Confirm pre-open futures still constructive.** If ES/NQ flip risk-off (>0.5% drop) or 10Y rips above key threshold, defer CAT entry.
2. **NVDA:** no action. Trailing stop is in place; let it work. Monitor SOXX pre-open as a tell.
3. **CAT entry:** if futures hold, place a **limit-buy** for ~17 shares near $890 with a bracket -7% stop at ~$828 (per strategy: hard stop until +5%, then convert to 10% trailing). Target sizing **~15% of portfolio (~$15K)**.
4. **Buy budget:** 1 of 3 weekly buys would be used; 4 → 3 open slots; cash falls from $94.9K to ~$80K (still well above the 10–20% buffer rule).
5. **PLTR AMC tonight (5pm ET):** informational — no action, but the result will color Tuesday's open for the AI-software cohort. Note it for the midday and market-close routines.

### Notes / research gaps to close next routine

1. Pull live US 10Y, DXY, WTI/Brent, Asia/Europe close levels at the market-open routine (Perplexity sparse on these tonight).
2. Verify Friday 5/1 AMC mega-cap print list (Perplexity returned n/a — check Alpaca calendar API).
3. Verify the rest-of-week earnings calendar (Tue–Fri) before Wednesday's pre-market.
4. After NVDA's 5/20 print, if held, take profit consideration if up >20% (per strategy rule).

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
