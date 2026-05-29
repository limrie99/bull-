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

## 2026-05-29 06:15 CT — pre-market

**Routine wake-up.** First successful research routine after a 5-week gap (4/22 → 5/29). Account is alive: Alpaca returns $99,840.95 cash / $99,840.95 equity / 0 positions. Tiny $159 drift from the original $100K start (likely a paper-account quirk; no trades on record). APIs healthy: Alpaca 200, Perplexity reachable. Three sub-agents fanned out (macro / earnings / opportunity scout); macro & earnings came back thin (Perplexity declined live quotes & calendar data), scout returned 5 ranked names with one critical caveat (stale price levels on AVGO and GOOGL).

### Market context
**Tone: risk-on, broad-based.** Pulled cash bars directly via Alpaca (IEX feed) since Perplexity wouldn't quote live levels.

Thursday 5/28 closes (confirmed via Alpaca):
- **SPY 754.68 (+0.59%)**, latest indication 755.36
- **QQQ 735.64 (+0.84%)**, latest 736.03
- **IWM 292.07 (+0.57%)** — small caps participating
- **TLT 85.72 (+0.50%)** — long bonds firm (yields easing)
- **GLD 412.80 (+1.04%)** — gold up alongside equities (mildly dovish lean)

Week-to-date (5/22 → 5/28):
- SPY +1.21%, QQQ +2.53%, IWM +2.44% — tech leading, breadth healthy
- TLT +1.24% — duration up means yields drifted lower on the week

Macro headline context (per macro sub-agent, partially verifiable):
- April PCE + Q1 GDP 2nd estimate released 5/28 — core PCE reportedly running >3% YoY into April → "higher for longer" risk remains the background concern, hostile to long-duration growth on any day they wake up.
- No top-tier US data print confirmed for today; Chicago PMI and UMich final are typical end-of-month Friday prints but couldn't verify. Treat as "no scheduled catalyst" until confirmed.
- Tariff-driven goods inflation remains an analyst overhang.
- Fed under Chair Warsh — any speakers today will be parsed against yesterday's PCE.

**Net read:** constructive open setup. Tech-led rally with bonds firm = a Goldilocks-ish tape into Memorial Day weekend follow-through Friday. Risk: light volume on a half-day-feel Friday can magnify moves either way.

### Portfolio watch
No open positions. $99,840.95 cash, $199,681.90 nominal buying power (strategy is cash-only / no leverage so usable is $99,840.95).

### Buy candidates

**Live prices re-verified via Alpaca — scout had stale levels on AVGO and GOOGL. Corrected below.**

- **NVDA — high conviction.** Recent beat-and-raise per scout (FY revenue guide reportedly lifted from ~$140B to ~$165–169B on AI data-center demand). Price ~$214.14 (Alpaca latest, 5/28 close $214.27). Off recent ~$219 high by 2.4%. Next earnings ~2026-08-26 AMC → ~60 trading days out, well clear of the 3-day blackout. Signals matched: (#1) recent EPS+rev beat with raised guidance, (#3) AI-infra secular tailwind, (#4) analyst target hikes post-print, (#6) clear uptrend (Apr→May trend up despite minor consolidation last 5 sessions). **Four signals → high conviction.** Risk: $5T mcap means slow position, extended valuation. Mitigation: long earnings runway + clearest catalyst chain in the book.

- **AVGO — med-high conviction.** AI-networking + custom ASIC pipeline. Price ~$431.94 (scout said ~$190 — that was wrong; corrected). Next earnings 2026-06-12 AMC → 10 trading days out, just outside blackout but the print is the catalyst & also a binary risk. Signals: (#2) earnings catalyst inside 30 days, (#3) AI-infra tailwind, (#4) multiple analyst target raises. **Three signals → med-high.** Best entry plan if taken: starter sizing (~7–10%) with explicit plan to trim or hold-through by 6/10. AMD's +15% weekly run-up (more on that below) is sympathetic-bullish for AVGO's AI-networking thesis.

- **GOOGL — med-high conviction.** Price ~$389.75 (scout said ~$181 — wrong; corrected). Near record highs after Google I/O AI updates. Next earnings 2026-07-28 AMC → ~40 trading days out, clear. Signals: (#3) AI tailwind, (#4) analyst target hikes post-I/O, (#5) sector rotation into mega-cap AI, (#6) uptrend. **Four signals → med-high.** Risk: entry timing near ATH; a 1-2% pullback day would be a better tactical entry than a green open.

- **LLY — med conviction, diversifier.** GLP-1/Mounjaro/Zepbound franchise. Price ~$1,127.36 (5/28 close, **+3.98% on the day vs prior** — single-day jump). Next earnings 2026-08-04 → ~46 trading days out. Signals: (#3) GLP-1 secular tailwind, (#4) maintained bullish targets, (#6) long-term uptrend. **Three signals → med.** Notes: $1,127 share price = odd-lot sizing; only buys ~13 shares per ~$15K slot. Pure healthcare diversifier away from the AI cluster.

- **META — pass.** $635 well-extended (+4.6% on 5/27 alone). Capex narrative + concentration risk argue against adding another mega-cap-AI beta to the basket alongside NVDA / AVGO / GOOGL.

**AMD wildcard.** Not in scout's top 5 but worth flagging: AMD +15.6% week (449 → 519), single-day +12% on 5/26. That's earnings-reaction-sized move — either AMD reported a blowout that I'm missing, or sector rotation is force-buying it. Need to verify the catalyst before sizing. Adds urgency to confirming the wider semis story.

**CRWD — EXCLUDED.** Earnings 6/3 AMC = 3 trading days out → inside the 3-day blackout per strategy.

**COST — EXCLUDED-ish.** Earnings 6/4 AMC = 4 trading days, edge of blackout. Compounded by COST being down -5.2% on the week (1,050 → 995) — no fresh-beat signal anyway. Pass.

### Sell candidates
None — no positions.

### Decision plan for 8:30 CT market-open routine

Bull is starting from 0/5 positions with full cash — this is the optimal moment to deploy thoughtfully. Recommended actions for the market-open routine (subject to a fresh check at the open):

1. **NVDA — primary deploy.** ~15% size (~$15K). High conviction. Set −7% hard stop via Alpaca bracket order. Will need ~70 shares at $214.
2. **GOOGL — secondary deploy.** ~10% size (~$10K) IF the open is not a vertical gap-up. ~25 shares at $390. Hard stop at −7%.
3. **AVGO — starter only (~7%, ~$7K).** Earnings risk in 10 trading days. Will need to trim or close before 6/10. ~16 shares at $432. Set stop.

Total deployed ~32% (~$32K) → leaves ~$67K cash for adds or to pick up LLY/the AMD story later in the week. Stays well inside the 3-new-buys-per-week cap and the 5-positions cap.

**Pass conditions for the open:**
- ES/NQ gap up >0.8% at open → buy half-size on NVDA only, no GOOGL/AVGO (chasing risk)
- ES/NQ gap down >0.8% → buy NVDA full size + GOOGL half-size, hold AVGO until later in day
- Macro shock headline overnight → pass entirely

### Research gaps to close at market-open
1. Verify NVDA's reported beat-and-raise date & guide figures with a fresh Perplexity call (scout's claims directionally sound but needs source confirmation).
2. Verify AMD's +15% week catalyst — was there an event I'm missing?
3. Confirm AVGO's 6/12 earnings date precisely (the 10-day count assumes no schedule change).
4. Pull DXY, WTI, 10Y at the open — macro digest was n/a-heavy, want a real level on rates before sizing.
5. Confirm whether any large-cap reported AMC 5/28 (earnings sub-agent returned nothing — possible they all reported earlier in the week).

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
