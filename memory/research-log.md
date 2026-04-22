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

## 2026-04-22 10:00 CT — pre-market (late-fired, for 2026-04-23 open)

**Timing / clock note:** Routine prompt framed as "6:00 AM CT pre-market with market opening in 3.5 hours," but Alpaca `/v2/clock` returned `is_open=true, timestamp 2026-04-22 11:00 ET (= 10:00 CT), next_open = 2026-04-23 09:30 ET`. Treating this as a **late-fired pre-market re-run, effectively prepping for tomorrow's (4/23) cash open**. Research-only per prompt (no trades). APIs live: Alpaca /account 200, /positions 200, Perplexity 200 (coverage thin). Account unchanged from 4/21 close: $100K cash, 0 positions. Inbox: no pending. Three sub-agents fanned out in parallel (macro, earnings, opportunity scout).

### Market context
Macro read is **neutral with low information**. Perplexity coverage for today was thin — several key fields `n/a`.
- **ES (Jun'26):** range ~7,154–7,231 recent sessions; today's pre-market % move `n/a`.
- **NQ (Jun'26):** level `n/a`, % move `n/a`.
- **US 10Y:** ~4.26% (Apr 20 print); today's bps change `n/a`. Had been 4.29% on 4/21 evening — suggests bonds bid back slightly.
- **DXY, WTI/Brent, Gold, Nikkei/Hang Seng/Shanghai, Europe opens:** all `n/a` from Perplexity.
- **Headlines:** only surfaced item was "US–Iran talks reportedly advancing toward a broader Middle East peace framework." No Fed, tariff, or China print.
- **Net:** no clear risk-on/risk-off read. Treat macro as neutral and weight idiosyncratic catalysts heavily. If a cleaner read is needed later, pull SPY/QQQ/TLT/UUP/USO/GLD bars directly from Alpaca at the market-open routine as a proxy.

### Portfolio watch
No open positions. $100K cash. Nothing to watch, nothing at risk.

### Earnings calendar (this week)
- **Today 2026-04-22 BMO large-caps:** none confirmed.
- **Today 2026-04-22 AMC large-caps:** none confirmed.
- **Tomorrow 2026-04-23 (target open) AMC cluster:** **TSLA + INTC + NOW + IBM + LRCX.** This is the week's tape-setter day — Thursday's cash session will be positioning into the print, Friday will be the reaction.
- **Last night (4/21 AMC):** no mega-cap prints.
- **Prior TSLA-contradiction RESOLVED:** TSLA reports **Thursday 2026-04-23 AMC**, not Wednesday. 17:00 CT pass on 4/21 had it wrong.
- **Guidance risk watch (for Fri reaction):** TSLA (auto cycle; guide-cut risk elevated), INTC (semis sentiment vehicle — weak guide would drag SOX).
- **Next week blackout list:** GOOGL 4/29, AMZN ~4/30, MSFT/META typical 4/29–5/1 — all currently within 3-trading-day blackout, EXCLUDED from new buys.

### Buy candidates

Scout pass was thin on fresh catalysts. Only one name cleanly stacks ≥2 verified signals. Documenting honestly rather than padding to fill the 3–5 slot target.

- **CRWD (Tech — cybersecurity).** Signals matched: **(4)** KeyBanc upgrade Sector Weight → Overweight, $525 PT on 2026-04-21; **(3)** cybersecurity secular tailwind. **Conviction: med.** Next earnings: historical early-June, **UNVERIFIED** in today's pull — must confirm via Alpaca calendar or a direct Perplexity earnings-date query before entering. Entry suggestion: **starter (≤5% ≈ $5K) once earnings date confirmed > 3 trading days out.** Risks: post-outage sentiment overhang; earnings-date risk until verified.
- **NVDA (Tech — AI infra).** Signals matched: **(3)** secular AI-infra tailwind (Blackwell ramp); **(6)** prior uptrend. **Conviction: med.** Next earnings: **2026-05-20 AMC (confirmed)** — ~20 trading days out, clear of blackout. Entry suggestion: **starter (~5% ≈ $5K) on constructive open**, let hyperscaler capex prints next week (GOOGL 4/29, MSFT/META/AMZN cluster) clarify the AI-capex picture before upsizing. Risks: hyperscaler capex commentary could cut either way; China export headline risk.
- **INTC.** Only a single signal (William Blair upgrade 4/21). Not a Bull-style fundamentals compounder — execution-dependent turnaround. **Pass.**
- **AVGO, GOOGL, MSFT, META, AMZN** — all inside or bordering the 3-trading-day earnings blackout (GOOGL confirmed 4/29; AMZN ~4/30; MSFT/META typical 4/29–5/1). **Skip all until post-print**, then revaluate.
- **PLTR.** Earnings 5/4 AMC (~8 trading days out — just outside blackout but tight). No fresh catalyst today. **Pass for now**; re-evaluate mid-next-week if a new signal appears.
- **TSLA.** Reports 4/23 AMC. Not a Bull-style name (momentum-heavy, high narrative). **Exclude.**

**Net:** at most **1–2 starters** worth considering for the Thursday 4/23 open, and only if pre-open tone is constructive AND TSLA/INTC hedge risk can be framed in ("both report AMC Thursday, so entries Thursday morning would be pre-reaction — size accordingly"). **CRWD is the cleaner setup on signals, but earnings-date blocker is unresolved**. **NVDA remains the default "always-a-good-time-unless-toppy" AI-infra proxy** with a verified runway (5/20). Cleanest play: **hold fire Thursday morning, watch the TSLA/INTC AMC reactions, and enter Friday pre-market if sentiment supports it.** Do NOT force a Thursday entry just to put cash to work.

### Sell candidates
None — no positions.

### Notes / research gaps to close next routine
1. **Verify CRWD next earnings date** — targeted Perplexity call or Alpaca calendar. Blocker for any CRWD entry.
2. At the next pre-market (Thursday 4/23 06:00 CT), confirm live ES/NQ % move and get actual cash-session SPY/QQQ close from today (4/22) to baseline macro tone.
3. Pull SPY/QQQ/TLT/UUP/USO/GLD bars directly from Alpaca as a macro-proxy when Perplexity is thin (pattern this week).
4. Consider raising Perplexity `search_context_size` to `medium` for scout calls — thin coverage is costing decision quality.
5. Pre-stage a Friday (4/24) pre-market watchlist keyed off Thursday's AMC cluster: (a) SOX names on INTC reaction (AVGO, AMD, MU, ANET, VRT), (b) auto/EV peers on TSLA reaction, (c) software names on NOW/IBM read-through (CRWD, PANW, ORCL).

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
