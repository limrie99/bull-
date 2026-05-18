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

## 2026-05-18 06:10 CT — pre-market (for Monday 5/18 open)

**Timing:** First routine after the ~26-day API-key outage. Secrets verified live. APIs verified: Alpaca 200, Perplexity 200. Account fetched: **$99,840.95 cash, $99,840.95 equity, 0 positions**, `balance_asof = 2026-05-15`. ~$159 below the $100K paper default — small drift, likely a stale-balance carry; no positions, so no risk leak. Three sub-agents fanned out in parallel (macro, earnings, opportunity scout) plus two direct Perplexity gap-fill calls. Perplexity was patchy today on macro index levels and the 5/18 earnings slate — falling back on Alpaca price snapshots and historical earnings patterns where I had to.

### Market context

Friday 5/15 closed **risk-off**, semis-led. Pre-market today is **flat-to-slightly-green on equity futures but with a Middle-East oil spike** that's keeping the tone defensive.

- **ES (Jun '26):** +0.10% overnight.
- **NQ (Jun '26):** +0.07% overnight.
- **WTI crude:** ~$113.70, **+1.15%** on reports of a strike on a UAE nuclear facility (per Benzinga).
- **Brent:** ~$110.25, +0.44%.
- **Gold futures:** ~$4,669 (+0.4%).
- **US 10Y / DXY / Asia closes / Europe early:** `n/a` — Perplexity declined to give live numbers, and Alpaca doesn't quote them in equity APIs. Last confirmed 10Y was ~4.59% at the 5/15 close per YCharts (up ~12 bps Thu→Fri). Treat rate direction as elevated and unknown intraday — avoid sizing rate-sensitive names hard.

**Friday's tape (Alpaca snapshot prev-close → last-trade):**
| Ticker | Thu close | Fri close | Day % |
|---|---|---|---|
| SPY | 748.10 | 737.71 | **−1.39%** |
| QQQ | 719.75 | 707.55 | **−1.69%** |
| NVDA | 235.78 | 225.08 | **−4.54%** |
| AMD | 449.70 | 424.18 | **−5.67%** |
| MU | 775.91 | 724.40 | **−6.64%** |
| ANET | 147.78 | 141.95 | **−3.94%** |
| AVGO | 439.34 | 425.03 | **−3.26%** |
| META | 618.51 | 614.38 | −0.67% |
| GOOGL | 401.12 | 396.31 | −1.20% |
| LLY | 1007.78 | 1004.69 | −0.31% |
| ORCL | 195.65 | 192.47 | −1.63% |
| MSFT | 409.44 | 420.80 | **+2.77%** |
| CRWD | 579.84 | 594.23 | **+2.48%** |
| PANW | 238.23 | 242.85 | **+1.94%** |
| PLTR | 133.73 | 133.79 | flat |

**Read:** clear **semis-down, software/cyber-up rotation** Friday — NVDA/AMD/MU/AVGO/ANET dumped together while MSFT/CRWD/PANW absorbed the rotation. SPY −1.4% / QQQ −1.7% with semis down 4–7% says the index move *was* the semis. Cyber outperforming on a red tape is a real tell.

**Net tone:** Mixed / cautious. Oil is the live wire today. Index futures slightly green is not a green light — semis still have to prove they've stopped bleeding, and the 10Y at 4.59% is unfriendly for high-multiple growth.

### Portfolio watch
No open positions. $99,840.95 cash, $199,681.90 buying power (cash-only / no leverage per strategy). No risk, no stops to manage.

### Earnings calendar (2026-05-18)
- **BMO Mon 5/18:** Perplexity returned `unconfirmed` for the full BMO and AMC slate. **No confirmed large-cap reporters today.** Need to re-verify at market-open routine via a tighter Perplexity call or a Polygon/financialmodelingprep cross-check.
- **NVDA next earnings: 2026-05-20 AMC (CONFIRMED via Perplexity).** That puts NVDA in the **3-trading-day blackout** (5/18, 5/19, 5/20). **No new NVDA position can be opened this week** under strategy rule.
- **Other watchlist next-earnings dates:** all `unconfirmed` from Perplexity today (AVGO, MSFT, GOOGL, META, AMD, PLTR, CRWD, PANW, ANET, MU, ORCL, NOW, LLY). Need a second source — Alpaca doesn't expose a calendar API for free, so this stays a Perplexity-with-citation problem. Historical patterns (for soft inference only, NOT a tradeable signal): MSFT/GOOGL/META/AMZN reported late April (likely outside blackout now); AVGO typically early June; CRWD typically late May (could be near blackout); PANW typically mid-May (could be inside blackout); LLY late April / early May; PLTR confirmed last pass as 5/04 AMC, so already reported.

### Buy candidates

No verified ≥2-signal name today. Documenting the shortlist honestly with the data I do have:

- **CRWD ($594, ~$140B mcap) — cyber leader, outperformed Friday's red tape.** Signals possibly hit: (3) cybersecurity secular tailwind, (5) sector rotation into cyber (clear from Fri tape), (6) above 50DMA per casual chart-shape inference. **BLOCKER:** next earnings date unverified — CRWD historically reports late May / very early June, which could put us inside the 3-day blackout window any day this week. **Cannot open without verifying the date.** If verified outside the blackout, this is the cleanest med-conviction name. Conviction held back to **low** until date is confirmed.
- **PANW ($243, ~$160B mcap) — cyber, same rotation read as CRWD.** Signals: (3) secular cyber, (5) sector rotation, (6) above 50DMA. **Same blocker:** PANW historically reports mid-May Q3 (e.g., 5/19 in prior years). Materially more likely to be inside the blackout than CRWD. **Skip until date is verified.**
- **MSFT ($421, ~$3.1T mcap) — only mega-cap green on Friday's red tape (+2.8%).** Signals: (3) AI/cloud secular, (5) rotation into mega-cap quality on Friday. Probably already reported (late-April pattern). **Conviction: low–med, pending date verification.** This is a "if I have to put cash to work this week, MSFT is the safest defensive pick" candidate, not a high-conviction buy.
- **NVDA — EXCLUDED** by 3-day earnings blackout (5/20 AMC confirmed). Friday's −4.5% drop into the print also tells you positioning is jittery. Revisit post-print on 5/21.
- **AMD, MU, AVGO, ANET — pass.** Semis broke Friday; trying to catch the dip here without a fresh catalyst is averaging-down-on-momentum-shift behavior the strategy explicitly forbids.
- **LLY ($1,005, ~$960B mcap) — GLP-1 secular intact, traded flat Friday.** Signals: (3) GLP-1 tailwind. Single signal verified; needs an earnings-date check before opening. Conviction **low**.

**Net call:** **No buy at Monday open.** The cleanest setup (cyber rotation) requires an earnings-date verification I couldn't get in this pass. The next-cleanest (MSFT defensive AI mega-cap) is fine but doesn't clear 2 verified signals. Strategy says don't force a trade — do the work.

**Plan for the market-open routine (9:30 ET / 8:30 CT):**
1. **First action: verify next-earnings dates** for CRWD, PANW, MSFT, GOOGL, META, AVGO, ANET, LLY via a tight Perplexity call asking each name's *most recent* reported quarter date AND next confirmed date with citations.
2. If CRWD's next earnings is ≥4 trading days out, open a **starter 5–7% position** ($5K–$7K) with the −7% hard stop, signals (3) + (5) + (6).
3. If CRWD is blackout-blocked but PANW is verified ≥4 days out, same play in PANW.
4. If both blackout-blocked, open a **smaller 5% MSFT starter** ($5K) as a defensive AI/cloud foothold — accept the conviction is only low-medium.
5. If oil spikes another 2%+ pre-open or ES turns red, **pass entirely**.

### Sell candidates
None — no positions.

### Notes / research gaps to close next routine
1. **Earnings-date verification is the bottleneck.** Without it I can't deploy. The market-open routine needs to lead with a single Perplexity call that asks ONLY for next-earnings dates of the cyber/AI watchlist, with citations required.
2. **NOW shows ~$95 on Alpaca snapshot** — that's almost certainly a stale/wrong feed (ServiceNow typically trades $700–1,000). Don't act on that number. If we ever consider NOW, pull `latestTrade` directly.
3. **Perplexity sparse on this date.** Two of three sub-agents got thin returns. Consider tagging Perplexity calls with explicit "use only sources dated within the last 14 days" framing.
4. **10Y / DXY / Asia / Europe still `n/a`.** If a separate macro feed is available, wire it up — making blind size decisions on oil-spike days without rates context is dangerous.
5. **Long gap since last routine (~26 days).** The strategy timing rules (e.g. "3 buys per week") effectively reset — no prior buys this week. The −7% / +5% trailing stop rules are moot since there are no positions to manage.

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
