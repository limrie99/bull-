# Portfolio

**Last updated:** 2026-08-14 08:50 CT — **MARKET OPEN (Fri).** Market CONFIRMED OPEN via /v2/clock (is_open:true, 09:50 ET, next_close 16:00 ET). Account: equity **$101,483.96**, cash **$36,641.95** (~36.11%), long_market_value **$64,842.01** (~63.89%), buying_power $328,125.43, status ACTIVE. `last_equity` (Thu 8/13 close) $101,860.21 → **today −$376.25 / −0.37%** intraday (LLY-driven, see below). **NO TRADES THIS OPEN** — nothing cleared the ≥70 buy-gate (per today's pre-market scan), no position at a risk trigger, no hard→trailing conversion pending. July Retail Sales (8:30 ET binary) already released before the 09:50 snapshot; irrelevant to action since no name qualified regardless. All three stops re-confirmed RESTING (open-orders nested=true). Conviction sleeve **3 of 5 stocks (two slots OPEN); weekly conviction buys 1/3** (SPY floor exempt). **Inbox: nothing pending.**

## Scorecard (intraday — market OPEN 2026-08-14 09:50 ET)
- **Equity $101,483.96.** Total since $100K start: **+1.48%.**
- **Today −$376.25 / −0.37%** intraday vs Thu 8/13 close $101,860.21.
- **The drag is LLY-specific:** LLY −2.85% on the day (day-3 re-entry giving back), while SPY is ~flat (777.89 vs 777.88 prior close) and JPM (+0.34%) / DE (~flat) are steady. On a flat tape our one soft name pulled the book down; not a market move.
- **Net open unrealized: +$1,405.95** (JPM +1,177.40, DE +492.36, SPY +159.07, LLY −422.88).
- **Cash 36.11%** — well above the 10–20% minimum buffer.
- *(Official daily scorecard vs SPY is owned by the market-close routine.)*

## Open positions (3 conviction stocks + 1 index-floor sleeve) — intraday marks 8/14 09:50 ET

| Symbol | Shares | Avg Cost | Price | P/L $ | P/L % | Stop | Entry Date | Thesis (1 line) |
|---|---|---|---|---|---|---|---|---|
| JPM | 34 | 329.695588 | 364.325 | +1,177.40 | +10.50% | **10% TRAILING (GTC)**, floor **329.85**, hwm 366.5 | 2026-06-29 | JPMorgan — $50B buyback + div hike; largest US bank; Q2 beat; DB Buy PT $375. +0.34% today, below hwm so no ratchet. Thesis intact; next earnings ~Oct. **Cushion ~9.46%.** |
| DE | 22 | 589.82 | 612.20 | +496.32→+492.36 | +3.79% | **10% TRAILING (GTC)**, floor **579.591**, hwm 643.99 | 2026-06-04 | Deere — Q2 beat, FY26 guide raised, ag/onshoring tailwind. ~Flat today. **PRINT RISK: Q3 Thu Aug 20 9:00 CT (~4 trading days out)** — AGCO missed −11% 8/6; DE ~238 layoffs; Evercore trimmed PT 641→632 but MAINTAINED. Do NOT add ahead. **Cushion ~5.33%.** |
| LLY | 12 | 1209.84 | 1174.60 | −422.88 | −2.91% | **−7% HARD STOP (GTC) @ 1125.15** | 2026-08-12 | Eli Lilly — Q2 beat-and-raise (rev $22.974B, adj EPS $8.38, RAISED FY26 EPS $35.50–36.50) + GLP-1/obesity secular tailwind. Day 3, **−2.85% today** giving back the re-entry pop (no company news — normal wiggle; 3 firms hiked PTs 8/13: Truist $1,376 / Cantor $1,410 / Wells $1,330). Conviction ~73 (B+). Hard stop converts to 10% trailing once +5% (~$1,270.33). **Cushion ~4.21% — now TIGHTEST in book.** |
| SPY | 32 | 772.921250 | 777.8923 | +159.07 | +0.64% | **NONE — index-floor sleeve, deliberate no-stop carve-out** | 2026-08-10 (t1) / 2026-08-11 (t2) | S&P 500 market floor (Lauren-approved Option B), COMPLETE. ~Flat today, tracking the index. Own sleeve, EXEMPT from ≤20%/max-5/max-3-per-week caps; NO −7%/trailing stop. Buy-and-hold-the-market. |

**Conviction sleeve: 3 of 5 (two slots OPEN).** **Conviction buys used this week: 1 of 3** (the SPY floor does NOT consume this budget). **Cash buffer: ~36.11%.** Position sizes (on equity $101,483.96): JPM ~12.21%, DE ~13.27%, LLY ~13.89%, SPY ~24.53% (index sleeve — exempt from the 20% single-position cap by policy).

## Closed THIS WEEK
- **None** (week began Mon 8/10). Last close: LLY trailing-stop exit 7/31 (+$627.34 / +4.15%) — RE-ENTERED 8/12 on the fresh verified beat-and-raise catalyst.

## Stop-management state (re-confirmed RESTING via open-orders, nested=true — 8/14 09:50 ET)
- **JPM 10% trailing** `8a937ff6-164c-4384-8cf8-c000d4106a60` — hwm **366.5**, floor (stop_price) **329.85**, status new (resting). Mark 364.325, cushion ~9.46%. Below hwm → no ratchet. qty 34.
- **DE 10% trailing** `dcdd84e5-6b94-4943-aa5b-3d3a299cbfce` — hwm **643.99**, floor (stop_price) **579.591**, status new (resting). Mark 612.20, cushion ~5.33%. Below hwm → no ratchet. qty 22.
- **LLY −7% hard stop** `f50e3c39-0719-497e-8ccc-6006e6afa290` — stop_price **1125.15** (=1209.84×0.93), GTC, status new (resting). Mark 1174.60 (−2.91% from entry, −2.85% today). **Converts to a 10% trailing stop once LLY is +5% in profit** (trigger ~$1,270.33). Cushion to stop ~4.21% — tightest in book, watch it. qty 12.
- **SPY — NO STOP by design** (index-floor sleeve carve-out). qty_available 32 (unencumbered). Intentional per the 8/7 policy; do NOT place a stop on the floor.

## Risk checks (open)
- **(a) Any position −7% or worse un-stopped?** NO. JPM +10.50%, DE +3.79%, LLY −2.91% (well above its −7% hard stop @ 1125.15), SPY +0.64%. **→ No sell triggered.**
- **(b) Any position +5%+ needing hard→trailing conversion?** NO conversion pending. JPM & DE already on 10% trailing GTC; LLY −2.91% (below +5%) on its −7% hard stop as designed; SPY carries no stop by policy. **(Standing task: convert LLY's hard stop → 10% trailing once it tags ~+5% / ~$1,270.33.)**
- **(c) Daily loss cap:** today −0.37% intraday → not tripped (well inside the −3% cap). Moot — no buys placed.

## Watch / next (next routine: **midday Fri 8/14**)
- **LLY — day 3, −2.85% today, now UNDERWATER −2.91%** on no company news — normal early-position wiggle, and PT hikes yesterday support the thesis. **But it's now the tightest cushion (~4.21%)** — watch it holds; the −7% hard stop @ 1125.15 is the safety net. Standing task: convert to 10% trailing at +5% (~$1,270.33).
- **DE — cushion ~5.33%.** **Q3 Thu Aug 20 9:00 CT (~4 trading days out)** — approaching the 3-trading-day earnings window. AGCO miss + DE layoffs raise gap-through-cushion odds on a Q3 miss. **Pre-commit hold-through-print vs tighten/exit decision due early next week.** Do NOT add ahead.
- **JPM — cushion ~9.46%**, healthy; below hwm so floor unchanged; thesis intact; next earnings ~Oct.
- **SPY floor COMPLETE** (cash ~36%). Rebalance rule fires only if a new ≥70 conviction buy would push cash below the 10–20% buffer (trim floor first). Two conviction slots remain, cash ~36% — room for ~1 more conviction buy before the floor would need trimming.
- **Conviction gate:** empty at last scan. Bench top: PWR ~68 (grid/power, best news stale — needs a fresh verified catalyst), AMGN ~70 EXTENDED (+13.5% vs 50dMA → bench-for-pullback), ABT ~64, MRK ~60 (FDA PDUFA Aug 17 — do-not-buy-pre-event). Next pre-market re-scores.

## Recent closes (last 5)

| Symbol | Exit Date | Shares | Entry | Exit | P/L $ | P/L % | Reason |
|---|---|---|---|---|---|---|---|
| LLY | 2026-07-31 | 14 | 1078.46 | 1123.27 | +627.34 | +4.15% | 10% trailing stop fired (give-back from ~1249 hwm; no thesis break; also removed Aug 5 earnings risk). **RE-ENTERED 8/12 on the verified beat-and-raise.** |
| GE | 2026-07-16 | 45 | 329.63 | 344.54 | +670.95 | +4.52% | 10% trailing stop fired (post-Q2-earnings give-back caught the profit; no verified thesis break) |
| ETN | 2026-07-02 | 24 | 401.5425 | 392.75 | −211.02 | −2.19% | 10% trailing stop fired (beta/thin pre-holiday tape, not thesis break) |
| NVDA | 2026-06-05 | 55 | 220.15 | 204.7158 | −848.88 | −7.01% | −7% hard stop fired (macro/NFP semis selloff, not thesis break) |
| NVDA | 2026-05-04 | 25 | 201.38 | ~195.02 | −159.04 | −3.16% | 10% trailing stop fired (round-trip) |

---
*Overwrite this file every routine. Keep it a live snapshot, not a log.*
