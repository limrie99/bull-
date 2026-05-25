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

## 2026-05-25 06:00 CT — pre-market (for Tue 2026-05-26 open)

**Timing note:** First successful routine since 2026-04-21. APIs verified live (Alpaca account/positions 200; Perplexity 200 selectively). Today is **Memorial Day — US market CLOSED**, so this pre-market view targets the Tue 5/26 reopen. Account: $99,840.95 cash, 0 positions (small ~$159 drift from $100K seed — likely Alpaca paper-account fee accrual). Four sub-agents fanned in parallel: macro, earnings, opportunity scout, sector rotation. Earnings and macro sub-agents returned mostly `n/a` from Perplexity on live tape numbers; Alpaca direct-bar pulls filled the most important gap (sector ETFs).

### Benchmark check
- SPY 2026-04-21 close: $704.08 → 2026-05-22 close: $745.64 → **+5.90% over the gap window**.
- Bull's portfolio: $99,841 vs $100,000 seed → **-0.16%**.
- **Alpha vs SPY since 4/21: -6.06%.** Bull missed the rally by sitting in cash through 23 trading days of halted/no-action routines. Not a reason to panic-deploy; IS a reason to act decisively on the next verified setup instead of re-running another "no high-conviction pick" pass.

### Market context
- **Today:** Memorial Day holiday, US equities and bond market closed. Next open: Tue 2026-05-26 09:30 ET.
- **Last full session (Fri 5/22):** SPY $745.64 (record-area). Risk-on with a soft-landing flavor.
- **Sector tape (5/15 → 5/22, week-over-week from Alpaca bars):**
  - Leaders: **SMH +3.59% (semis), XLU +3.37% (utilities), XLV +3.30% (healthcare), XLRE +3.08% (REITs), IWM +2.71% (small caps), XLK +2.34% (tech), XLY +2.27% (cons disc).**
  - Laggards: XLC -0.53% (comms — GOOGL drag), XLB -0.02%, XLE +0.08%, XLP +0.19%, XLI +0.22%.
  - SPY benchmark: +0.88%.
  - **Read:** Risk-on + soft-landing positioning. Yield-sensitive (XLU/XLRE/SMH) outperformance implies yields drifted lower into the PCE print. Small-cap broadening (IWM > SPY by 1.8pts) is a bullish breadth signal. Communication services the lone weak group.
- **Macro calendar this week:**
  - Tue 5/26 — Case-Shiller HPI 9:00 ET; **Consumer Confidence 10:00 ET**.
  - Thu 5/28 — **April PCE / Core PCE 8:30 ET (marquee print)**, Q1 GDP 2nd estimate, advance durable goods, jobless claims.
  - Fri 5/29 — Chicago PMI 9:45 ET; Fed Gov. Waller speech (TBD).
  - **Live wire: Thursday PCE.** A hot core PCE re-tightens conditions and pressures long-duration tech; a cool print extends the soft-landing bid the tape is already pricing in.
- **Futures / yields / FX / commodities Sunday-night levels:** Perplexity returned `n/a`. Will pull at Tue 6 AM CT before the open-routine fires.

### Portfolio watch
No open positions. $99,840.95 cash, $199,681.90 buying power (cash-only per strategy — ignore margin).

### Earnings — just-printed (key catalyst)
**NVDA — fiscal Q1 FY27 reported Wed 5/20 AMC. Confirmed beat-and-raise.**
- **Revenue: $81.6B vs consensus ~$78.5B (+4% beat).** Record. Data Center $75.2B, +92% YoY.
- Non-GAAP EPS $1.87 (GAAP $2.39). Non-GAAP gross margin 75.0%.
- **Q2 FY27 guide: $91.0B ±2%** — sequential +11–13% from a record Q1, explicitly **excluding any China Data Center compute revenue**. Well above prior consensus.
- **Stock reaction: SOLD THE NEWS.** 5/20 close $223.47 (pre-print) → 5/21 $219.51 (-1.77%) → 5/22 $215.33 (-1.91%). **-3.64% over the two post-earnings sessions** despite a blowout print. Reason: NVDA had run +57.7% since June 2025 / +16.3% from prior quarter — expectations were sky-high.
- **For Bull:** the sell-the-news drift is a gift on the entry, not a thesis killer. Earnings runway is now ~3 months (next print late Aug). Fundamentals are pristine. Entry at $215 is ~3.6% better than chasing the print itself.

### Earnings — this-week calendar
Perplexity refused this query. Will pull a fresh Alpaca-calendar query or targeted Perplexity tickers at Tue 6 AM CT before deciding on AMD / CRWD / PANW.

### Buy candidates

**TOP PICK — NVDA (~$215) — conviction MED-HIGH**
- Signals hit: **(1)** earnings beat + raised guidance, verified ✅; **(3)** secular AI infra tailwind, confirmed by the $91B Q2 guide ✅; **(5)** sector rotation into semis (SMH +3.59% week) ✅.
- Signal (6) uptrend is a yellow flag — short-term down 3.6% post-earnings, but still up >50% YTD. Not a fresh 52-week-low knife.
- Earnings runway: clear, next print ~late August.
- Proposed sizing: **starter ~10–12% of portfolio (~$10K–$12K, ~45–55 shares at $215)** with the strategy's **-7% hard stop at ~$200**.
- Why not full 15–20%: respect the sell-the-news tape; size up only if NVDA holds $215 area and PCE doesn't blow up Thursday.

**SECONDARY WATCH (need fresh verification at Tue 6 AM):**
- **AMD (~$467)** — closed +3.98% on 5/22 with semis leading. Signal (3) + likely (5). Need to verify next earnings date is outside 3-day blackout and identify a specific catalyst (analyst upgrade, OEM win, etc.) before sizing.
- **LLY (~$1,065)** — closed +2.24% on 5/22. GLP-1 secular thesis (signal 3) intact. Healthcare leadership confirmed (XLV +3.30% week). Verify next earnings date and any fresh catalyst.
- **CRWD (~$663)** — closed +2.35% on 5/22. **CRWD historically reports fiscal Q1 in early June — likely inside the 3-day blackout from Tue 5/26.** Hard verify before any entry; otherwise skip until post-print.
- **PANW (~$261)** — closed +3.03% on 5/22. **PANW historically reports fiscal Q3 in late May (~5/22 was a typical print window). May have just reported or be about to.** Hard verify before any entry.

**HARD SKIPS:**
- **COST** — -2.10% on 5/22 (defensive weakness, likely just reported and missed something).
- **GOOGL** — XLC was the only red sector last week; no fresh catalyst verified.
- **MSFT / META / AAPL / ORCL / AVGO** — no fresh ≥2-signal setup verified; all in the post-Q1-print quiet window.

### Sell candidates
None — no positions.

### Plan for Tue 2026-05-26 market-open routine
1. Pull live futures, 10Y, DXY, oil at 6 AM CT. If futures down >0.5% or 10Y back above 4.40%, **shrink NVDA starter to $5K or skip**.
2. Re-verify NVDA didn't gap >2% from Friday's $215 close.
3. **If constructive:** place NVDA bracket buy — market order ~50 shares (~$10.7K, ~10.7% of portfolio), stop_loss at $200.00 (-7%). Use the bracket flow in scripts/alpaca.md.
4. Targeted Perplexity / Alpaca-calendar check on AMD, CRWD, PANW, LLY next-earnings dates. If AMD or LLY clear the 3-day blackout AND have a verifiable second signal, consider a second 5–10% starter Tuesday. CRWD/PANW: default skip until earnings prints are confirmed past.
5. Daily-loss-cap not in play (no positions). Weekly buy cap: 0/3 used this week — comfortable with 1–2 fresh buys.
6. Keep ≥75% cash through Wed PM. Thursday PCE could move us 1–2% either way; want dry powder.

### Notes / research gaps for next routine
1. Earnings calendar refused by Perplexity — try Alpaca calendar API or per-ticker Perplexity queries at Tue 6 AM.
2. Verify CRWD and PANW exact next-earnings dates (historical late-May/early-June risk).
3. Pull live futures and 10Y at Tuesday 6 AM — sub-agents could not retrieve.
4. Build a sub-agent macro digest that batches the live-data query into one tight question rather than spreading across calls — Perplexity refused most spread-out asks but answered the focused NVDA-earnings call.

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
