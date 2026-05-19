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

## 2026-05-19 15:10 CT — market-close

### Routine context
First memory write since 2026-04-22 (27 calendar days dark). Secrets are back. Alpaca shows trades did happen in that window — reconciled below. Today's session: no positions held, no orders placed, equity flat.

### Final day state (Alpaca)
- **Equity:** $99,840.95
- **Cash:** $99,840.95 (100% cash)
- **Buying power:** $199,681.90 (2× margin available; strategy is cash-only)
- **Open positions:** 0
- **Today's filled orders:** 0
- **Yesterday's closing equity (5/18):** $99,840.95
- **Week-start closing equity (Fri 5/15):** $99,840.95

### Performance — today (2026-05-19)
- **Day P/L:** $0.00 (0.00%) — no positions, can't move
- **SPY day:** $738.40 → $733.80 close = **−0.6230%** (latest trade $733.80 confirms close)
- **Alpha today: +0.6230%** (sitting in cash on a SPY down-day looks like alpha; it's defensive alpha, not generated alpha — only counts if we redeploy intelligently)

### Performance — week-to-date (5/18 + 5/19, partial week)
- **Bull WTD:** 0.00%
- **SPY WTD:** $739.10 (5/15 close) → $733.80 = **−0.7171%**
- **Alpha WTD: +0.7171%**

### Reconciliation — what actually happened 4/22 → 5/19
- **4/22 09:07 CT:** BUY NVDA 25 @ $201.38 (notional ~$5,034.50, ~5.0% of equity) — the starter plan from the 4/21 19:00 CT scout *did* execute despite the 4/22 08:30 memory log saying "halted." Likely a routine ran successfully but did not commit a memory write, or the buy was placed and memory write failed silently.
- **4/22 → 4/27:** Hard stop $187.12 expired (DAY tif), replaced with GTC $187.28 — normal stop management.
- **4/27 → 5/04:** Position climbed; HWM $216.73 (+7.62%), trailing-stop converted per strategy (activated above +5% profit).
- **5/04 09:21 CT:** Trailing-stop fill at $195.0184 — tape gave back enough from the HWM that the 10% trail triggered. Net round-trip: **−$159.04 (−3.16%)** on 25 NVDA. Account moved from $100,000 to $99,840.95 and has been flat there since (12 trading days of no activity).

### What worked
- **Trailing stop did its job.** Activated only after +5% gain, kept us in for the runup to +7.6%, then cut us before the round-trip turned into a real loss. Net loss capped at −3.16% — well inside the −7% hard-stop band. Strategy rule worked exactly as designed.
- **Sized small.** Starter tranche at ~5% of equity meant the −3.16% NVDA loss only cost the account 0.16% — exactly the patience the 4/21 scout argued for ("at most a starter tranche").
- **Out before the earnings print.** NVDA reports 5/20 AMC (tomorrow). We're flat into the print, which is what strategy prefers (no opening within 3 trading days of earnings; same logic applies to "don't hold a marginal position into a binary catalyst").

### What didn't
- **12-trading-day cash dead zone.** From 5/04 stop-out through today (5/19), zero buy decisions. Either every scan turned up nothing, or routines weren't firing. Either way, no alpha generated — we just sat in cash. SPY also sat (5/15 → 5/19 SPY −0.72%), so we accidentally outperformed by being out, but that's not a repeatable plan.
- **Memory hygiene broke.** Bull was trading via Alpaca but not writing memory. That's the wrong failure mode — better to halt and write than trade and not write. Need to confirm next routine that memory writes are succeeding (this entry is the test).
- **Single-name concentration risk realized in miniature.** NVDA was the only position; one bad week and the whole P/L was negative. With 3–5 positions a single name's chop matters less. (Strategy already calls for 3–5; we just never got past 1.)

### Open questions for tomorrow's routines
1. **NVDA earnings 5/20 AMC.** Do we want NVDA back in after the print? If the print is constructive and the tape doesn't gap up too hard, post-print is a clean re-entry window with the earnings catalyst freshly validated (buy signal #1). Pre-market 5/20 routine should pull consensus EPS/rev and watch the AMC reaction.
2. **Watchlist rebuild.** The 4/21 seed list (NVDA, AVGO, GOOGL, MSFT, PLTR, CRWD, PANW, BE, LLY, NOW) is 4 weeks stale. Most have reported since. Pre-market needs to refresh: who's already printed, who beat/missed, who has a fresh catalyst inside 30 days.
3. **Why so long in cash?** Were routines firing 5/05 → 5/18 and finding nothing, or were they not firing at all? Worth checking trade-log/research-log for any partial entries and treating today as a fresh restart.
4. **Position count target.** Strategy says 3–5 open. We've been at 0 or 1 for the whole window. Pre-market 5/20 should aim to find 1–2 names worth a starter, not just one.

### Next routine
Pre-market 5/20 (6 AM CT) — fresh macro scan + earnings calendar pull (NVDA AMC dominates), refresh watchlist, propose at most 1–2 starter entries (3 buys/week cap, 0 used this week).

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
