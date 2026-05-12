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

## 2026-05-12 06:10 CT — pre-market

**Timing note:** First successful routine since the 4/22 halts. APIs verified live (Alpaca 200, Perplexity 200). Account: $99,840.95 cash, equity $99,840.95, 0 positions. Three sub-agents (macro, earnings, opportunity scout) plus one direct verification pull on a 10-name watchlist.

**Gap context — 3 weeks of inactivity:** Last live data was 4/21 (account opening, $100K cash). Today is 5/12. We have sat in cash through what looks like a strong rally — SPY now $738.29. We are -0.16% lifetime vs SPY moving sharply up. The mandate is to beat SPY; sitting in 100% cash with no opens is not the long-term plan. Today's open routine should plausibly place a first starter, conditional on macro tone.

### Market context

Mixed / mildly cautious into Tuesday 5/12 open.
- **ES (Jun '26):** ~7,434.25, **−0.03%** overnight (flat).
- **NQ (Jun '26):** **−0.04%** (flat).
- **US 10Y:** **4.41%, +5 bps.** Bonds soft on energy/inflation worry.
- **WTI / Brent:** rising (exact level n/a). Driver: US–Iran talks failed to produce a Mideast war end-terms framework — risk premium back on.
- **DXY, Gold, Asia, Europe:** n/a from Perplexity tonight.
- **Headlines:**
  1. US–Iran talks fail → oil up, yields up.
  2. SPY and QQQ hit fresh all-time highs Monday on continued AI/chips leadership.
  3. Global yields rising — central-bank-tightening tail risk back in chatter.
- **US data today:** none scheduled (no CPI/PPI/FOMC minutes flagged).
- **Net tone:** mixed. Flat futures after Monday's record close means the market is digesting, not extending. The 5 bp yield jump + oil bid is a real headwind for rate-sensitive longs. Not risk-off enough to pass on everything, but not the day to size up aggressively.

### Portfolio watch

No open positions. $99,841 cash. Nothing to manage. The only "watch" item is that we've been in cash through a SPY ATH run — opportunity cost is now the dominant risk, not drawdown risk.

### Earnings calendar (2026-05-12)

**Quiet day.** Perplexity returned no confirmed $10B+ US BMO or AMC reports for today. Monday 5/11 AMC also light (Fox Corp reported BMO, not AMC). Today's tape is macro-driven, not earnings-driven. Lower idiosyncratic risk for opening a position; higher macro/oil/yield sensitivity.

### Watchlist — last close from Alpaca (firm)

| Symbol | Last px | t (UTC) |
|---|---|---|
| NVDA | 219.04 | 5/11 20:12 |
| AVGO | 428.32 | 5/11 19:59 |
| MSFT | 412.62 | 5/11 19:59 |
| GOOGL | 389.21 | 5/11 20:16 |
| META | 599.26 | 5/11 20:58 |
| PLTR | 136.90 | 5/11 19:59 |
| CRWD | 542.59 | 5/11 19:59 |
| PANW | 213.71 | 5/11 19:59 |
| LLY | 967.16 | 5/11 19:59 |
| NOW | 91.48 | 5/11 19:59 |
| SPY | 738.29 | 5/11 20:11 |
| QQQ | 712.72 | 5/11 20:40 |

(NOW at $91 implies a post-split; older context had it triple-digit hundreds — flag for verification before sizing.)

### Buy candidates

Perplexity was thin again tonight (most fields n/a). Verified-data candidates:

- **NVDA — $219.04, 2.1% off 52-week high, above 50-DMA.** Signals: (3) secular AI/Blackwell tailwind, (6) clear uptrend. Last verified next earnings date from prior log: **2026-05-20 AMC**, which is **6 trading days out** (5/13, 5/14, 5/15, 5/18, 5/19, 5/20). That's **outside the 3-day blackout but tight** — opening today means we'll need a plan for the 5/20 print: either close before 5/15 (cutoff for 3-day rule), hold-through (only if thesis depends on the print), or trim. **Conviction: medium.** Cleanest name on the board, but earnings proximity reduces the "let it breathe" upside.
- **AVGO — $428.32.** Earnings ~2026-06-03 (prior log, unconfirmed tonight). Single signal (3 — secular AI ASIC) carried over from 4/21 scout. **Conviction: low–medium.** Best earnings window if confirmed, but needs a fresh signal (upgrade, contract win) to clear the ≥2 bar.
- **META — $599.26.** Reported in late April historically. No confirmed earnings date or fresh signal tonight. **Conviction: insufficient data.**
- **GOOGL, MSFT — $389.21 / $412.62.** Likely already reported (late-April pattern). Need a verified next-earnings date and a fresh signal before considering. **Skip until verified.**
- **PLTR — $136.90.** Prior log flagged 2026-05-04 AMC earnings — that print is already in the rearview. No data tonight on the result. **Skip until verified.**
- **LLY — $967.16.** GLP-1 leader, secular tailwind (3). No fresh signal or earnings date tonight. **Conviction: low — single signal.**
- **CRWD ($542.59), PANW ($213.71), NOW ($91.48):** no verified fresh data. **Skip.**

**Net recommendation for today's market-open routine:**
- **Primary plan:** open an NVDA starter at the open IF (a) ES/NQ remain at or above flat, (b) 10Y not above 4.45%, (c) WTI not gapping >2%. Size: **10% of equity (~$10,000, ~46 shares at $219).** That's medium-conviction sizing per strategy. Place bracket with stop at $219 × 0.93 ≈ $203.67.
- **Pre-earnings exit plan:** plan to close NVDA by **2026-05-15 close** (last day outside the 3-day earnings window) UNLESS thesis upgrade by then.
- **Fallback if macro deteriorates pre-open:** pass entirely, run a tighter verification scout midday.
- **Do NOT** open AVGO, META, GOOGL, MSFT, PLTR, CRWD, LLY, NOW today on tonight's data — insufficient verified signals.

### Sell candidates
None — no positions.

### Notes / research gaps to close next routine
1. Confirm NVDA 5/20 earnings date directly (Alpaca calendar or news pull) before sizing.
2. Pull MSFT, GOOGL, META, PLTR last-week earnings results — those prints already happened and the results would let us add fresh signals.
3. Verify NOW $91 print — looks split-adjusted; need confirmed reference price.
4. Perplexity is thin on price/earnings-date specifics in 2026 again. Consider biasing future scouts toward Alpaca-native data (latest trades, daily bars, calendar API) and using Perplexity only for narrative catalysts.

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
