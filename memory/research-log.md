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

## 2026-05-05 06:00 CT — pre-market (for 5/5 open)

**Timing:** Scheduled 6:00 AM CT pre-market. Alpaca clock confirms market closed; next_open 2026-05-05 09:30 ET (~3h out). Secrets all present (Alpaca + Perplexity). Account: **$99,840.96 cash, 0 positions, last_equity $99,926.75 (drift -$85.79 since 5/1 reconcile, no trades).** Four sub-agents fanned out in parallel — macro, earnings, sectors, opportunity scout.

### Market context

Tape leans **quietly green into the open, low conviction** because most macro fields came back `n/a`.

- **ES (Jun'26):** ~7,243.00, **+0.18%** overnight (only confirmed futures level).
- **NQ:** `n/a` — Perplexity could not return level.
- **10Y Treasury:** `n/a` — bp move unknown.
- **DXY, WTI, Brent:** all `n/a`.
- **Asia / Europe:** `n/a` (no confirmed Nikkei / Hang Seng / FTSE / DAX prints returned).
- **Headlines (since Mon close):** none dated and verifiable in this pull.
- **Sector tape (last 5 sessions):** Technology still leads (April +2% on the month). Energy weak (April -14%). S&P 500 closed ~7,200.75 on 5/4 (-0.41% on the day).

**Net:** treat today as a **normal-volatility, modestly risk-on session with too many `n/a`s to size aggressively off macro alone.** ES +0.18% is the only hard datapoint. Intraday breadth + 10Y direction will tell the real story — re-check live levels at 9:30 ET before any sizing decision. If futures fade red pre-open, downsize.

### Portfolio watch

No open positions. $99,840.96 cash, $199,681.92 buying power (cash-only / no margin per strategy). Day drift -$85.79 vs last_equity is balance-reconciliation noise — no risk on the book. Nothing to babysit.

### Earnings calendar (2026-05-05)

- **BMO:** no $10B+ US large-caps confirmed by Perplexity for today's BMO. Smaller names (IBTA, MDRX, BORR) below universe threshold. Cross-check Earnings Whispers / Briefing live before open if anything material surfaces.
- **AMC:** no large-caps confirmed for today AMC. PINS and VRTX surfaced but the May-5 date was not verified.
- **Yesterday AMC (5/4) — relevant gap:** **PLTR blew out the print.** Q1 rev $1.633B vs ~$1.54B est (+85% YoY), adj EPS $0.33 vs $0.27–$0.28, GAAP EPS $0.34. **Raised FY26 guide:** rev $7.650–$7.662B, US commercial $3.224B+ (+120%), adj op income $4.440–$4.452B, adj FCF $4.2–$4.4B. Adj op margin ~60%. Latest print $146.96 (post-AH). **PLTR is the single earnings tape-setter going into today.**
- **Guidance-risk read:** with no confirmed BMO mega-caps, today is more macro/PLTR-spillover driven than print-driven.

### Buy candidates

**1. GOOGL — AI capex raise + Cloud blowout, fresh post-earnings strength** — **HIGH conviction**
- Last print **$383.21**, mcap ~$4.7T (post-Apr 30 +9.96% gap on earnings)
- Next earnings: ~late July 2026 (Q2) — **outside** 3-day blackout.
- Signals matched: **(1)** Apr 29 beat — rev $109.9B vs $106.8B est, EPS $5.11 vs $2.62, FY AI capex guide raised to **$180–190B**; **(3)** Google Cloud +63% YoY to $20B = AI infra secular tailwind; **(6)** clear uptrend off the gap.
- 3 verified signals, the strongest pairing in the framework. Defensible thesis even if tape gets ugly today.

**2. MSFT — Azure/AI beat, $190B FY26 capex, no print until Oct** — **HIGH conviction**
- Last print **$412.94**, mcap ~$3.1T.
- Next earnings: 2026-10-29 (Q1 FY27) — **far outside** blackout.
- Signals matched: **(1)** Apr 29 Q3 FY26 beat — EPS $4.27 vs $4.06, rev $82.89B vs $81.39B; **(3)** AI infra tailwind, $190B FY26 capex commitment; **(6)** post-beat uptrend (visible via 4/30 gap).
- Cleanest "long runway, no near-term print risk" name in the watchlist.

**3. AVGO — custom-silicon AI beneficiary, post-selloff entry** — **MEDIUM conviction**
- Price unverified pre-market, mcap ~$1T+, YTD +19% as of 5/1.
- Next earnings: early-June 2026 (est, Q2 FY26) — **outside** 3-day blackout, but watch the calendar.
- Signals matched: **(3)** named hyperscaler partner for Alphabet/Meta custom silicon = AI infra tailwind; **(5)** sector rotation back into AI infra after late-April OpenAI-leak selloff.
- Only 2 signals + price unverified. Fine as a watchlist add later in week, not a day-1 buy.

**4. NVDA — AI cornerstone but pulled back hard, earnings 5/20** — **LOW–MEDIUM conviction**
- Last sub-agent reference ~$171 (down from $213 on 4/28). Mcap ~$3.77T.
- Next earnings: **2026-05-20 AMC** — outside 3-day blackout but inside 15-day window. Per strategy, openable but small.
- Signals: **(3)** AI tailwind intact, **(5)** sector rotation. **Failed** signal **(6)** — not in clean uptrend, just made a lower low.
- Honest read: wait for the May-20 print or a confirmed higher-low before entering.

**5. PLTR — post-earnings momentum, fresh blowout guide** — **MEDIUM conviction (gap-chase risk)**
- Last print $146.96, mcap ~$340B.
- Next earnings: now ~3 months out post-print — **way outside** blackout.
- Signals matched: **(1)** massive Q1 beat-and-raise just hours ago; **(3)** AI/defense-software tailwind; arguably **(6)** uptrend, but it just gapped and chasing gaps is exactly what strategy v1 punished.
- **Caveat:** strategy says "don't chase momentum without a catalyst" — there IS a catalyst here, but the gap-chase risk is real and PLTR's multiple is rich. Consider as the third buy LATER in the week if it consolidates above $145, NOT at the open.

### Names considered & rejected

- **CRWD** — YTD -4.87% as of 5/1, fails signal (6); no recent earnings beat verified. Reject for now.
- **PANW, NOW, META, AMZN, AAPL, TSM, ORCL, LLY, BE** — could not verify ≥2 signals from this Perplexity budget. ORCL had directional AI-infra mention (OCI Supercluster) but no earnings/upgrade/price confirm. Re-pull case-by-case next routine.

### Sell candidates

None — no positions.

### Net plan for 9:30 ET open

If futures hold green and tape is constructive:

- **GOOGL ~15% of equity ≈ $15,000 → ~39 shares at $383** (high conviction band).
- **MSFT ~15% of equity ≈ $15,000 → ~36 shares at $413** (high conviction band).
- That's 2 of 3 weekly buys used, $30K deployed, ~70% cash retained.
- Place each as a **bracket buy with -7% hard stop** (GOOGL stop ~$356, MSFT stop ~$384). No take-profit — trailing stop handles upside per strategy.
- **Skip NVDA, AVGO, PLTR at open.** Re-evaluate AVGO + PLTR midweek.

If ES turns >0.5% red before open, or 10Y prints >4.40%, or GOOGL/MSFT take overnight bad headline: **pass and reassess at midday.**

### Notes / research gaps to close next routine

1. Re-pull macro fields properly — ES alone isn't enough. Need 10Y, DXY, WTI levels.
2. Cross-check live earnings calendar for any 5/5 BMO surprises before 9:30 ET.
3. Confirm AVGO current price + 50-day MA before any AVGO action.
4. Rebuild a 15-name watchlist with verified next-earnings dates so future scouts don't burn calls re-discovering basics.

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
