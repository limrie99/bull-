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

## 2026-04-24 06:00 CT — pre-market (for Fri 4/24 open)

**State reconciliation upfront:** Last logged research routine was 2026-04-22 12:00 CT (HALTED). Alpaca now shows an NVDA position (25 sh @ $201.38, filled 2026-04-22 10:07 ET) with a -7% stop at $187.28 GTC. The actual buy routine was not logged in research-log or trade-log — backfilling trade-log now. Account: equity $99,981.50, cash $94,965.50. No positions closed.

Four sub-agents fanned out in parallel (macro, earnings, position/NVDA, opportunity scout). APIs verified live (Alpaca 200, Perplexity 200).

### Market context
Tone is **mixed** into Fri 4/24 open — earnings-supportive but commodity/rate headwinds.
- **US equity futures (ES, NQ Jun'26):** specific overnight % change `n/a` from Perplexity. Context: Thu 4/23 cash close S&P 500 **7,137.90 (+1.1%)**, NDX **24,937.28 (+1.7%)**.
- **Rates:** 10Y ~4.30%, 2Y ~4.80% — mildly higher on crude rebound.
- **Commodities:** **WTI and Brent near $100** on Hormuz/Iran tensions — the single biggest macro mover. Gold range-bound $4,670–$4,875, soft as oil-driven dollar/yield bid saps safe-haven demand. DXY firmer.
- **Global:** Nikkei mixed (Japan AI supportive), Hang Seng resilient/mixed, European majors slipped on oil. Specific levels `n/a`.
- **Headlines:** Iran ceasefire holding loosely but Hormuz premium persists; Micron / Boeing / GE Vernova beat-and-guided; flash PMIs + jobless claims on deck this morning.
- **Net:** mixed. Expect sector rotation rather than clean beta. Crude > $100 sustained would hit duration-sensitive tech harder.

### Portfolio watch

**NVDA — 25 sh @ $201.38, current $200.64, unrealized −$18.50 (−0.37%). Stop $187.28 GTC. Cost basis $5,034.50 (~5% of portfolio).**
- **Thesis: INTACT.** Google Cloud announced AI-hypercomputer expansion on next-gen NVIDIA systems (4/22) — bullish read-through on hyperscaler demand. No material 4/23–4/24 news, no new analyst actions in-window (last prints early April: DBS $220, New Street $275, Benchmark $250).
- **Sector quiet.** TSMC 4/16 "exceptionally strong AI demand" remains the freshest sector datum. AVGO / AMD / ASML / MU / ARM: nothing material.
- **Correction to prior log:** mega-cap hyperscalers (GOOGL/AMZN/META/MSFT) report ~4/29, NOT 4/23 AMC as loosely implied earlier.
- **Flags:** RSI ~71.6 (stretched) per 4/21 — could pull back harder than peers on any sector de-risk. Watch SMH/SOXX relative strength today. Any late-week export-control / tariff headline = weekend gap risk.
- **Action:** HOLD. Stop stays at $187.28 until +5% unrealized ($211.45); no edits needed.

### Earnings calendar (2026-04-24)
- **BMO:** no verified large-cap ($10B+) US earnings confirmed. Friday calendar is typically thin.
- **AMC:** none (Fridays almost never see AMC prints of size).
- **Last night (4/23 AMC) movers:** none material verified at the $50B+ mega-cap level.
- **Season read:** ~81% EPS beat / ~76% rev beat through 4/23 per Perplexity. Mega-cap tech cluster is **4/29** (GOOGL/MSFT/META/AMZN) — that's the real tape-mover next week.

### Buy candidates
Scout ran 3 Perplexity passes across the 17-name watchlist (AVGO, GOOGL, MSFT, META, PLTR, CRWD, PANW, LLY, NOW, ANET, TSM, AMD, COST, V, MA, JPM, NFLX). Returns were near-uniformly `unknown` on the critical fields: next earnings dates, fresh analyst actions, near-term catalysts, recent upgrades/insider activity. The one fresh sector read was trailing-6-month (Energy +40.4%, IT −7.8%, Fin −7.5%) — too stale to anchor a buy per strategy rule "confirmed by fresh news."

**No name cleared the ≥2 verified-signal bar.** In particular:
- MSFT, GOOGL, META, AMD likely in the 3-day earnings blackout around 4/29 — cannot confirm dates, so conservatively treating as blocked.
- Secular-tailwind names I know-but-cannot-freshly-confirm (AVGO/ANET AI-infra, CRWD/PANW cyber, LLY GLP-1, PLTR defense-AI): single-signal only — strategy needs ≥2.

**Verdict: pass on new buys at 4/24 open.** Discipline > forcing a mediocre entry into a quiet Friday tape with macro headwinds. Cash stays at ~$94,965 (95% of account). Re-scan Monday 4/27 with a targeted per-ticker query approach for the watchlist and a fresh earnings-blackout check.

### Sell candidates
None. NVDA thesis intact, well above stop, no signal triggered.

### Notes / research gaps to close next routine
1. Per-ticker Perplexity queries instead of batch — the 17-way batch returns too much `unknown`.
2. Pull next-earnings dates via Alpaca's asset/calendar endpoint (if supported) before querying Perplexity for thesis context.
3. Broaden seed list beyond mega-cap tech (which is all in print-window right now) — consider industrials/defense/data-center-power names that already reported (e.g., GE Vernova after its constructive beat).
4. Confirm actual WTI/Brent/DXY cash levels and ES/NQ overnight % change at Monday's open — this pass had too many `n/a`s on spot macro levels.
5. Monitor SMH/SOXX vs SPY relative strength at today's open as an early tell on whether semis are rotating into or out of the 4/29 mega-cap hyperscaler print.

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
