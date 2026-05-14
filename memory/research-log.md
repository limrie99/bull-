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

## 2026-05-14 06:00 CT — pre-market (for 5/14 open)

**Timing:** Scheduled pre-market routine. Alpaca clock confirms market closed; next_open = 2026-05-14 09:30 ET. APIs verified live (Alpaca 200, Perplexity 200). Three sub-agents fanned out in parallel: macro, earnings, opportunity scout. Account fresh after a multi-week halt window: **$99,840.95 cash, 0 positions** (down $159.05 from $100K — likely tiny paper-account interest accrual or rounding, not a trade).

### Market context

Tape into Thursday cash open reads **mildly risk-on at record highs**, but data was thin.
- **ES (Jun'26):** +0.20% at ~7,484.25 overnight (prior cash session +0.62%).
- **NQ (Jun'26):** +0.55% overnight (prior session +1.09%). Nasdaq leading SPX = AI/semis bid intact.
- **SPY spot:** $742.77 (Alpaca last trade 5/13). At this price SPY implies SPX ~7,427 — consistent with ES at 7,484.
- **10Y yield, DXY, WTI, Brent, gold, Asia/Europe closes:** all came back **n/a** from Perplexity. Same data gap as the 4/21 passes — need a better macro source.
- **Headlines:** no fresh Fed/CPI/PPI/tariff/geopolitics driver named. Wednesday's S&P/Nasdaq prints made fresh record highs on continued AI-chip momentum.
- **Net read:** mildly risk-on but extended; path of least resistance is up into the open, but record-high tape is asymmetric — any surprise headline hurts more than it helps.

### Portfolio watch

No open positions. **$99,840.95 cash**, $199,681.90 buying power (cash-only per strategy). Nothing to manage.

### Earnings calendar (2026-05-14)

- **BMO and AMC: Perplexity returned no verified $10B+ US earnings for 5/14.** This is a Perplexity coverage limitation, not a market signal. Names like WMT and CSCO historically print mid-May — treat as **possible but unconfirmed**; verify against a structured calendar (Alpaca news / Nasdaq calendar) before Friday's routine.
- **Wed 5/13 AMC standouts:** none confirmed. Do not assume any specific print without verification.
- **Tape-setter call:** without confirmed mega-cap prints, Thursday is macro/flow-driven, not earnings-driven.

### Buy candidates

Scout returned a ranked table of **NVDA / LLY / AVGO / PLTR / MSFT**, but **flagged a serious data-quality problem:** Perplexity's quoted current prices were materially wrong vs. live Alpaca quotes. Documenting both for honesty:

| Ticker | Scout-quoted price | Alpaca last trade (5/13) | Delta | Implication |
|---|---|---|---|---|
| NVDA | ~$145.20 | **$226.41** | +56% | Scout price appears to be pre-split or stale by months |
| LLY  | ~$928.40 | **$1,015.64** | +9% | Closer, but still off |
| AVGO | ~$192.80 | **$417.50** | +117% | Likely pre-split / pre-2025 quote |
| PLTR | ~$38.90  | **$130.13** | +234% | Stale by many months |
| MSFT | ~$482.50 | **$404.35** | −16% | Off the other direction |

Because the scout's prices are unreliable, **its specific claims (insider buy 50K shares 5/10, FDA approval 5/11, $1.2B Army contract 5/8, Goldman upgrade dates) cannot be trusted without independent verification.** Treat the symbol list as a **watchlist**, not as verified buy theses.

What I can still defensibly say about each, using only confirmed Alpaca prices + strategy rules:

- **NVDA — $226.41.** Secular AI-infra tailwind (signal 3) is real and ongoing; that one alone has been a 2026 thesis. Next earnings date not verified tonight — historical pattern is **late May**, which would put us inside or near the 3-trading-day blackout. **Do not enter without confirming earnings date first.** If confirmed clear of blackout: med-conviction starter.
- **LLY — $1,015.64.** GLP-1 secular tailwind (signal 3) is intact. Specific FDA-approval claim from scout unverified. Notional cost of a single share is high — 5% position sizing means ~$5K = only 4-5 shares (fine, just sized small).
- **AVGO — $417.50.** Custom-silicon / AI-networking tailwind (signal 3). Earnings unverified; AVGO typically prints **early September**, so blackout less likely an issue now. Pullback-entry geometry tempting but unverified.
- **PLTR — $130.13.** AI + defense tailwind (signal 3). At all-time highs based on the price move; chasing a name up >3x in a year carries its own risk. Strategy explicitly tolerates momentum within a fundamentals frame, but I want a *verified* fresh catalyst before opening.
- **MSFT — $404.35.** Down ~16% from the scout's misquoted level. If MSFT is actually trading off recent highs while AI-cap-ex remains intact, that's a *better* setup than the scout described, not worse — but I need to confirm the price action isn't a thesis-breaker (e.g., Azure miss, antitrust headline). Earnings was late January cycle → next likely late July, well clear of blackout.

**Net call for 5/14 open:** **NO new buys.** This is a pre-market routine — no trades allowed anyway — but importantly, even if it were the open routine, the scout data is too unreliable to act on. The market-open routine should:
1. Verify next-earnings dates for NVDA, LLY, AVGO, PLTR, MSFT via Alpaca corporate actions or a per-ticker Perplexity query.
2. Confirm at least one concrete catalyst per name with a primary source (company IR, SEC filing) before opening anything.
3. If tape is still risk-on and at least 2 names clear ≥2 verified signals, open ONE starter (5% sizing, ~$5K), prefer AVGO or LLY for less-extended entry. NVDA only if blackout clears.

### Sell candidates

None — no positions.

### Notes / research gaps to close next routine

1. **Scout price-verification is mandatory.** Going forward, the scout must cross-check at least the current price for each proposed ticker via Alpaca before reporting — Perplexity alone is unreliable on quotes.
2. Pull next-earnings dates for NVDA, LLY, AVGO, PLTR, MSFT directly (Alpaca calendar or per-ticker Perplexity).
3. Macro digest is still missing 10Y yield, DXY, WTI/Brent, gold, Asia/Europe levels. Consider a different research path or a higher search-context setting.
4. The 22-day gap since the last successful routine (2026-04-22 halts) is large — tape has moved a lot. Rebuild the watchlist deliberately rather than relying on 4/21 priors.

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
