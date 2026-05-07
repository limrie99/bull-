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

## 2026-05-07 06:00 CT — pre-market (for 5/7 open)

**Timing note:** First successful routine since the 4/22 halt streak. Secrets are back. Account verified live: **$99,840.95 cash, 0 positions, equity $99,840.95** (paper-account starting balance is ~$99.8K, not $100K — minor variance carried from Alpaca's paper default). Alpaca clock confirms market closed; next_open 09:30 ET today. Three sub-agents fanned out (macro, earnings, opportunity scout). Note: Alpaca SIP data subscription not enabled — could not pull SPY bars from data API (`subscription does not permit querying recent SIP data`); will need IEX-tier endpoint or skip alpha calcs until upgraded.

### Market context

Tape **risk-on** into Thu 5/7 cash open.

- **ES (Jun'26):** **+~1.07%** at ~7,365.50. Gap-up resuming bull trend after Wed close.
- **NQ:** roughly flat to slight +; mixed signals overnight after a +2.08% Nasdaq cash close on 5/6.
- **Dominant overnight driver:** AI/semis momentum — **AMD +17%** (AMC 5/6 strong data-center forecast & beat), **SMCI +24%** (margin/profit guide raise). The two prints lit a fire under AI capex names.
- **10Y, DXY, WTI/Brent, Asia/Europe closes:** all `n/a` from Perplexity this run. Need a secondary check at open if rate-sensitive sizing matters.
- **No Fed speakers, CPI/PPI prints, jobless-claims surprises** flagged for the overnight window.
- **Net read:** risk-on. Swing factor = whether AMD/SMCI/AI-adjacent names hold their gap-up at 09:30 ET cash open. A fade would sap broad-market momentum.

### Portfolio watch

**No open positions.** $99,840.95 cash, $199,681.90 buying power (cash-only / no leverage per strategy). Nothing to manage; no stops, no thesis-break checks needed.

### Earnings calendar (2026-05-07)

Perplexity could not authoritatively confirm any large-cap reports for today (BMO or AMC). Honest read: today is more macro/momentum-driven than earnings-driven. If a position is moving sharply, run a per-ticker check before assuming earnings is the driver.

**Yesterday AMC (5/6):** **AMD** and **PLTR** both confirmed printers (per macro and scout digests respectively). AMD +17% reaction, PLTR raised FY26 guide to ~36% YoY (rev ~$3.75B). **NOW** printed 5/1 with a raised FY26 subscription guide. **MA** caught a JPM upgrade to Overweight on 5/4.

### Buy candidates

Scout returned 4 names; verifying earnings-blackout windows. **All four are post-print, so the "3-day before earnings" blackout does not apply** — each is now in fresh-print territory, the strongest signal in the playbook.

- **PLTR — Palantir | ~$42 | Conviction: HIGH.** Signals matched: (1) earnings beat 5/6 AMC + raised FY26 guide (~36% YoY rev, ~$3.75B); (3) secular AI/defense tailwind (AIP commercial + government). Next earnings ~Aug 4. Risk: stock often pops hard post-print and gives some back; consider not chasing the open gap — stage a starter on any pullback into 09:45–10:30 ET.
- **NOW — ServiceNow | ~$980 | Conviction: HIGH.** Signals: (1) earnings beat 5/1 + raised FY26 subscription guide ($13.46–13.49B); (3) secular enterprise-AI / agentic-workflow tailwind. Next earnings ~Jul 22–27. Cleanest "fresh beat + raised guide + durable subscription model" setup in the playbook. Bull should be a buyer.
- **AMD — Advanced Micro Devices | ~$148 | Conviction: MED.** Signals: (1) earnings beat 5/6 AMC + raised Q2 guide ($7.1–7.6B), MI300 demand strong; (3) AI-infra capex tailwind. Next earnings ~Aug 5. Caveat: stock already +17% on the print — chasing into a gap-up risks a -7% hard-stop in days. Wait for first 30-60 min volatility to settle, ideally enter on consolidation, not the open print.
- **MA — Mastercard | ~$515 | Conviction: MED.** Signals: (4) JPM upgrade 5/4 to Overweight, PT $620; (5) sector rotation diversifier (financials/payments outside our crowded AI book). Next earnings ~Jul 29. Single-signal-light, but real diversification value if we're going to load up on PLTR/NOW/AMD — would prefer this as the 4th name, not the 1st.

**Net plan for the 5/7 open (no trade in this routine — research only):**
- Best two ideas: **NOW** and **PLTR**. Both have the textbook "beat + raised guide" combo. NOW is the cleaner setup; PLTR is higher beta/momentum.
- **AMD** is real but already gapped — disciplined entry only.
- **MA** is the diversification candidate.
- Tentative size: 2 starters at the open ≈ 10–12% each (~$10K each), **NOW first** if we only place one. Hard -7% bracket on each. Re-validate at the 09:00 CT market-open routine before placing.

### Sell candidates

None — no positions.

### Notes / research gaps to close next routine

1. Get 10Y, DXY, WTI cash levels at the cash open (Perplexity gave `n/a` again — try a focused single query, or use a secondary source).
2. Check Alpaca SIP/IEX entitlements — can't pull SPY bars on current subscription, breaks alpha calc. Either upgrade or use last-trade endpoint and a rolling SPY snapshot from Perplexity.
3. Verify NOW / PLTR / AMD / MA quotes at open via Alpaca latest-trade endpoint before sizing.
4. Watch for AMD/SMCI fade at open as the macro swing factor.

### Sub-agent research caveats

- **Macro digest** thin on rates, FX, and overseas closes (`n/a`s). Got the futures direction and the AMD/SMCI catalysts — enough to call risk-on, not enough to size rate-sensitive names.
- **Earnings digest** could not authoritatively confirm any large-cap May 7 reporters. Source is incomplete — the macro and scout digests independently confirmed AMD reported 5/6, which the earnings digest missed. Treat the earnings digest as a floor, not a ceiling.
- **Scout digest** gave 4 actionable names with verifiable post-print catalysts, but flagged that Perplexity returned `n/a` on exact next-earnings dates in its verification call. The discovery-call dates above are approximate; confirm directly before trading.

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
