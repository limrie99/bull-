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

## 2026-04-22 10:04 CT — pre-market (ran late — market already open)

**Timing note:** Routine was scheduled as "6:00 AM CT pre-market" but Alpaca clock at dispatch is `2026-04-22T11:04 ET` = **10:04 CT, market OPEN**. Earlier routines today halted on missing secrets; secrets are now live (`ALPACA_*`, `PERPLEXITY_API_KEY`, `TELEGRAM_*` all set). Per routine scope, **no trades** placed — research-only. Account re-verified via Alpaca: **$100,000 cash, 0 positions, equity $100,000, last_equity $100,000, daytrade_count 0**. Three sub-agents fanned out in parallel (macro, earnings, opportunity scout).

### Market context
Net tone: **cautiously risk-on, low confidence** — macro digest had too many `n/a`s again.
- **ES (Jun'26):** ~7,142.50 (+0.60%) on overnight snapshot (02:31 UTC) — stale by ~8h by the time this ran; real-time cash level not pulled. Tue cash closed −0.13%.
- **NQ:** +0.40% pre-market overnight on US–Iran diplomacy hopes; Tue closed ~flat.
- **10Y yield, DXY, WTI, Brent cash levels:** **n/a** — Perplexity sparse. WTI only confirmed as *direction up* Tue on Iran-concerns headlines.
- **Headlines since Tue close:**
  1. Crude spiked on fresh Iran concerns Tue, erasing early equity gains.
  2. US–Iran diplomacy hopes lifted futures +0.35–0.40% into Wed pre-market.
  3. Retail sales data and Warsh (Fed chair nominee) hearing on deck; no CPI/PPI/jobs, no Fed speakers, no tariff/China headlines overnight.
- **Net:** Middle East / crude remains the swing factor. No data-driven catalyst today.

### Earnings calendar (honest state — source returned mostly n/a)
- **4/22 BMO / AMC large-caps:** **n/a** — Perplexity did not confirm any large-cap $10B+ reporters for today. Contradicts the 4/21 17:00 CT pass's TSLA-AMC read, consistent with the 4/21 19:00 CT pass's "no confirmed mega-cap" read.
- **4/23 BMO likely (unconfirmed dates):** MMM, BA, GE, LMT, NOC, UAL, AAL — "this week" list, no firm date/EPS/rev.
- **4/23 AMC likely (unconfirmed):** TSLA, INTC — historical slot.
- **4/21 AMC:** no large-cap print surfaced in fresh pull. TSLA 4/21 AMC asserted in 17:00 CT pass on 4/21 has now contradicted itself twice — treat as unconfirmed until Alpaca/filings reflect it.
- **Implication for 4/22 session:** tape is macro-driven, not earnings-driven.

### Portfolio watch
No open positions — nothing to watch. $100K cash / $200K reg-T buying power (strategy cap = cash-only, no leverage). No sub-agent dispatched per-position (nothing to cover). Guardrail status: 0/5 position cap used, 0/3 weekly buys used, no daily-loss cap triggered (equity unchanged).

### Buy candidates
Scout verified very little today (2 Perplexity calls; most fields `n/a`). Honest take: **one low-med candidate, one pass-with-watch, rest are pass-until-dates-are-confirmed.**

- **NVDA** — (Semis / AI infra) ~$186 last print; mkt cap n/a. **Signals matched: (3) secular AI-infra tailwind — intact, dated** + **(1 partial) Feb 25 2026 Q4 FY26 print: rev $68.1B / +73% Y/Y, EPS $1.76 (>1wk stale, partial credit).** Next earnings **2026-05-20 AMC (confirmed prior pass)** — ~20 trading days out, clear of 3-day blackout. Catalyst window: Q1 FY27 print 5/20 is double-edged. **Conviction: MED.** Starter 5% ($5K), full 12% ($12K) max given print risk. Entering 4 weeks ahead of earnings is a known trap — prefer pullback.
- **AVGO** — (Semis / AI networking) price/mcap n/a. **Signals matched: (3) AI-networking + custom-silicon tailwind (undated in today's pull).** Next earnings **2026-06-03 (confirmed prior pass)** — safe window. **Conviction: LOW** — only 1 signal verified today. **Pass** until a second dated signal.
- **GOOGL, MSFT, AMZN, META, NOW** — **PASS TODAY.** Late-April is peak mega-cap earnings week; Perplexity did not confirm exact dates today. Opening any of these without a verified next-earnings date would risk the 3-trading-day blackout rule. Defer until dates are pulled directly (next routine: query the Alpaca calendar API or a cleaner source).
- **PLTR, CRWD, PANW, LLY, BE** — **PASS.** All `n/a` on earnings date + recent catalyst today. Cannot verify blackout compliance or ≥2 signals. Honest pass.

**Net:** still a **pass-and-wait morning** (same recommendation the last two research-log entries reached). If there were pre-market authority to trade, at most a **NVDA starter (~5% / $5K)** with the −7% hard stop — and only if the cash session opens constructive (SPY green, no crude spike). Since this routine is explicitly no-trade, deferring the NVDA entry decision to the next market-open or midday routine.

### Sell candidates
None — no positions.

### Notes / research gaps to close next routine
1. Scheduling drift: the 6 AM CT pre-market ran at 10 AM CT. Flag so scheduler can be fixed; if unfixable, rename this slot to "morning scan."
2. Still failing to pull 10Y / DXY / WTI cash levels from Perplexity. Consider a dedicated narrow query (single concept per call) for macro levels before the batched headline query, or raise `search_context_size` to `medium`.
3. Pull MSFT/GOOGL/AMZN/META/NOW/LLY/PLTR next-earnings dates from Alpaca's corporate-actions endpoint (or the free `/v2/calendar` if available) rather than asking Perplexity — faster and deterministic.
4. TSLA 4/21 AMC print status: still unresolved across three consecutive scans. Next routine should check directly on IR page or filings summary.

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
