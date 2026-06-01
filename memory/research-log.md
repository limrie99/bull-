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

## 2026-06-01 06:00 CT — pre-market (for 6/1 open)

**Timing:** Scheduled pre-market routine. APIs verified live (Alpaca 200, Perplexity 200 via 3 parallel sub-agents). Account: **$99,840.95 cash, 0 positions, $99,840.95 equity** (Alpaca balance_asof 2026-05-29). First live research routine since 4/21 — the 4/22 session and weeks since were halted-no-trades, so the slate is genuinely fresh.

**Sub-agent team fanned out in parallel:** macro analyst, earnings analyst, opportunity scout. No position analyst — no open positions to watch.

### Market context (macro digest)
Tone into the 6/1 open: **risk-on, but on a tight leash** for rate-sensitive names.
- **ES (Jun):** ~7,580–7,620 (level only — overnight % `n/a` from Perplexity).
- **NQ, 10Y, DXY, WTI/Brent, Nikkei, Hang Seng, DAX/FTSE:** levels `n/a` from Perplexity; will need to check live feed before any sizing.
- **Dominant tape-driver:** tentative **US–Iran 60-day ceasefire extension** reopening the Strait of Hormuz. Equities bid, crude under heavy pressure — Brent on pace for its worst month since 2020. WTI at multi-week lows.
- **Cross-current:** **April PCE came in hot at 3.8% YoY (3-year high)** while Q1 GDP was revised down to 1.6%. Fed speakers have turned modestly more hawkish — real policy rate may still be below neutral. This puts duration and rate-sensitive names (high-multiple tech, REITs, regional banks) on a tight leash even as the index drifts higher.
- **Asia:** firm overnight on soft Tokyo May CPI (eases BoJ hike pressure). Global equities at record highs into the US open.
- **Today's data:** no major US print or Fed speaker confirmed for Mon 6/1. **Week ahead:** ISM Manufacturing (Mon/Tue), JOLTS (Tue), ADP (Wed), ISM Services (Wed/Fri), Initial Claims (Thu), **NFP Fri (~+150–200k, U-rate ~3.8–4.0%, AHE +0.3% m/m)**.
- **Net:** risk-on for the index, but the hot-PCE / hawkish-Fed undercurrent says **don't size up rate-sensitive multiples today**. Iran/oil is the binary swing — a ceasefire wobble would flip the tape.

### Portfolio watch
No open positions. **$99,840.95 cash, $199,681.90 buying power** (2× margin offered, but strategy is cash-only / no leverage). Equity is essentially flat vs $100K seed (small ~$159 drift, likely accrued fees — not material). Nothing to manage, nothing bleeding.

### Earnings calendar
- **Mon 6/1:** **earnings-free day for $10B+ US names** per Nasdaq's published calendar (post-Memorial-Day weekend). The only 6/1 entry surfaced is sub-$10B (UEC). **Today's tape will be macro-driven, not earnings-driven.**
- **This week (June 2–6) — tape-setters to position around:**
  - **PANW — Tue 6/2 AMC (tentative)** — guidance on NGS ARR + platformization deal count; sets cyber tone for CRWD/ZS.
  - **AVGO — Wed 6/3 AMC (tentative)** — **THE dominant overhang for the entire AI complex this week.** AI semi revenue run-rate + custom-ASIC commentary. NVDA/AMD/MRVL/ANET ranges likely tighten Tue–Wed into this print.
  - **LULU — Thu 6/4 AMC (tentative)** — North America comp + China growth; consumer discretionary tell.
  - **HPE, MDT, CRWD, DOCU** — also in the early-June window; specific dates unconfirmed.
- Consensus EPS/rev: `n/a` — not verified by Perplexity this run.
- **Guidance-risk call:** **low today, high Wed.** AVGO Wednesday is the week's biggest event.

### Buy candidates
Honest read: the scout could not lock in ≥2 verified buy signals for any single name this run. **Signal #3 (secular tailwind) is the only one consistently verifiable** — that's one signal, the strategy requires two. No fresh upgrades, insider buys, contracts, or rotation reads were surfaced for the May 25–31 window in the time budget.

Live prices from Alpaca (last trade, close of Fri 5/29):

| Symbol | Last | Signals verified | Conviction | Notes |
|---|---|---|---|---|
| NVDA | $212.46 | #3 (AI infra secular) | **low** | Earnings ~late Aug 2026 → blackout-safe. **Hampered by AVGO Wed readthrough — entire AI semi complex on tight leash through Wed.** |
| GOOGL | $380.90 | #3 (cloud + Gemini secular) | **low** | Next earnings ~late July → blackout-safe. Less AVGO-readthrough risk than pure semis. |
| MSFT | $448.17 | #3 (Azure + AI secular) | **low** | Next earnings ~late July → blackout-safe. PCE-hot tape unfriendly to high-multiple mega-tech today. |
| META | $631.96 | #3 (ad + AI infra) | **low** | Single signal only. |
| LLY | $1,105.00 | #3 (GLP-1 secular) | **low** | Single signal; GLP-1 thematic intact but no fresh catalyst surfaced. |
| AMD, AMZN, PLTR | (n/a thesis) | — | — | No second signal verified. |

**Hard exclusions (earnings blackout — strategy rule: no new position within 3 trading days of print):**
- **PANW** ($281.97) — earnings Tue 6/2 AMC. Hard exclude all week pre-print.
- **AVGO** ($444.33) — earnings Wed 6/3 AMC. Hard exclude all week pre-print.
- **CRWD** ($731.09) — in early-June batch, date not pinned but in/adjacent to blackout. Exclude until exact date confirmed.

**Net call:** **No buys at Monday open.** Strategy explicitly says be patient — first trade should be a clean ≥2-signal setup, not a forced entry. With the AVGO print looming Wednesday night and the entire AI-semi complex likely to compress, **defer the NVDA/AMD/ANET decision until Thursday morning**, when AVGO's readthrough is in. GOOGL and MSFT are blackout-safe but didn't clear ≥2 signals this run — re-test them at the open and at midday once we have intraday tape and any fresh news.

### Sell candidates
None — no positions.

### Notes / research gaps to close next routine
1. Get verified pre-open levels for ES, NQ, 10Y, DXY, WTI, Brent at the 8:30 CT market-open routine — Perplexity was thin on numerics again. Consider raising `search_context_size: "medium"` for the macro call.
2. Verify exact 6/2–6/6 earnings dates for CRWD, HPE, MDT, DOCU — currently tentative. Use Alpaca calendar API if Perplexity stays vague.
3. Run a tighter, per-ticker scout on NVDA and GOOGL at the open: any analyst-action overnight, any contract announcement, any sector-rotation read into XLK or XLC.
4. Watch ISM Manufacturing print today — if it surprises high, bond yields likely pop and rate-sensitive multiples get hit; if low, the slowing-growth narrative dominates.

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
