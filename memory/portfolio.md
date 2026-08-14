# Portfolio

**Last updated:** 2026-08-14 15:05 CT — **MARKET CLOSE (Fri).** Market CONFIRMED CLOSED via /v2/clock (is_open:false, 16:01 ET, next_open Mon 8/17 09:30 ET). Account: equity **$101,375.07**, cash **$36,641.95** (~36.14%), long_market_value **$64,733.12** (~63.85%), buying_power $327,820.54, status ACTIVE. `last_equity` (Thu 8/13 close) $101,860.21 → **today −$485.14 / −0.48%.** **SPY −0.20%** today → **alpha today −0.28 pt** (we lagged the market by a hair). **NO TRADES today** (all four 8/14 routines — pre-market, open, midday, close — were no-trade; closed-orders empty). **The whole day's drag is LLY** (−$343 of the −$485). All three stops RESTING (open-orders nested=true). Conviction sleeve **3 of 5 stocks (two slots OPEN); weekly conviction buys 1/3** (SPY floor exempt; week ends today — resets Mon). **Inbox: nothing pending.**

## Daily scorecard (official — market CLOSE 2026-08-14)
- **Equity $101,375.07.** Total since $100K start: **+1.38%.**
- **Today −$485.14 / −0.48%** vs Thu 8/13 close $101,860.21.
- **SPY today −0.20%** (776.34 close vs 777.88 prior close) → **alpha today −0.28 pt.** A quiet down-day; we trailed SPY by a fraction because LLY (which SPY doesn't feel the way we do) sagged.
- **Week-to-date (from Fri 8/7 close $101,707.48):** book **−0.33%** (−$332.41) vs **SPY +0.40%** (773.26→776.34) → **alpha WTD −0.73 pt.** Behind the market this week; the drag is almost entirely LLY's paper loss since the 8/12 re-entry. *(Full weekly benchmark breakdown is owned by the Friday weekly-review routine.)*
- **Net open unrealized: +$1,297.15** (JPM +1,126.91, DE +418.66, SPY +104.92, LLY −353.34).
- **Cash 36.14%** — well above the 10–20% minimum buffer.

## Open positions (3 conviction stocks + 1 index-floor sleeve) — CLOSING marks 8/14
| Symbol | Shares | Avg Cost | Close | P/L $ | P/L % | Stop | Entry Date | Thesis (1 line) |
|---|---|---|---|---|---|---|---|---|
| JPM | 34 | 329.695588 | 362.84 | +1,126.91 | +10.05% | **10% TRAILING (GTC)**, floor **329.85**, hwm 366.5 | 2026-06-29 | JPMorgan — $50B buyback + div hike; largest US bank; Q2 beat; DB Buy PT $375. Flat today (−0.07%). Below hwm → no ratchet. Thesis intact; next earnings ~Oct. **Cushion ~9.09%.** |
| DE | 22 | 589.82 | 608.85 | +418.66 | +3.23% | **10% TRAILING (GTC)**, floor **579.591**, hwm 643.99 | 2026-06-04 | Deere — Q2 beat, FY26 guide raised, ag/onshoring tailwind. Soft today (−0.58%). **PRINT RISK: Q3 Thu Aug 20 9:00 CT (~3 trading days out)** — AGCO missed −11% 8/6; DE ~238 layoffs; Evercore trimmed PT 641→632 but MAINTAINED. Do NOT add ahead. **Pre-commit hold-through-print vs tighten/exit decision due Mon/Tue. Cushion ~4.81% (tightest trailing).** |
| LLY | 12 | 1209.84 | 1180.395 | −353.34 | −2.43% | **−7% HARD STOP (GTC) @ 1125.15** | 2026-08-12 | Eli Lilly — Q2 beat-and-raise (rev $22.974B, adj EPS $8.38, RAISED FY26 EPS $35.50–36.50) + GLP-1/obesity secular tailwind. Day 3, **−2.37% today** (the day's whole drag); −2.43% from entry. No dated company news; thesis intact (3 firms hiked PTs 8/13: Truist $1,376 / Cantor $1,410 / Wells $1,330). Conviction ~73 (B+). Hard stop converts to 10% trailing once +5% (~$1,270.33). **Cushion ~4.68% — tightest in book; watch Monday.** |
| SPY | 32 | 772.921250 | 776.20 | +104.92 | +0.42% | **NONE — index-floor sleeve, deliberate no-stop carve-out** | 2026-08-10 (t1) / 2026-08-11 (t2) | S&P 500 market floor (Lauren-approved Option B), COMPLETE. Tracked the tape's small dip (−0.20%). Own sleeve, EXEMPT from ≤20%/max-5/max-3-per-week caps; NO −7%/trailing stop. Buy-and-hold-the-market. |

**Conviction sleeve: 3 of 5 (two slots OPEN).** **Conviction buys used this week: 1 of 3** (resets Mon 8/17; the SPY floor does NOT consume this budget). **Cash buffer: ~36.14%.** Position sizes (on equity $101,375.07): JPM ~12.17%, DE ~13.21%, LLY ~13.97%, SPY ~24.50% (index sleeve — exempt from the 20% single-position cap by policy).

## Closed THIS WEEK
- **None** (week of Mon 8/10–Fri 8/14). Buys this week: SPY floor ×2 (8/10, 8/11 — exempt) + LLY re-entry 8/12 (1 conviction buy). No sells, no stop-fires.

## Stop-management state (re-confirmed RESTING via open-orders, nested=true — 8/14 close)
- **JPM 10% trailing** `8a937ff6-164c-4384-8cf8-c000d4106a60` — hwm **366.5**, floor (stop_price) **329.85**, status new (resting). Close 362.84, cushion ~9.09%. Below hwm → no ratchet. qty 34.
- **DE 10% trailing** `dcdd84e5-6b94-4943-aa5b-3d3a299cbfce` — hwm **643.99**, floor (stop_price) **579.591**, status new (resting). Close 608.85, cushion ~4.81%. Below hwm → no ratchet. qty 22.
- **LLY −7% hard stop** `f50e3c39-0719-497e-8ccc-6006e6afa290` — stop_price **1125.15** (=1209.84×0.93), GTC, status new (resting). Close 1180.395 (−2.43% from entry). **Converts to a 10% trailing stop once LLY is +5% in profit** (trigger ~$1,270.33). Cushion to stop ~4.68% — tightest in book. qty 12.
- **SPY — NO STOP by design** (index-floor sleeve carve-out). qty_available 32 (unencumbered). Intentional per the 8/7 policy; do NOT place a stop on the floor.

## Risk checks (close)
- **(a) Any position −7% or worse un-stopped?** NO. JPM +10.05%, DE +3.23%, LLY −2.43% (well above its −7% hard stop @ 1125.15), SPY +0.42%. **→ No sell triggered; no Perplexity news-check required (trigger is −7%).**
- **(b) Any position +5%+ needing hard→trailing conversion?** NO conversion pending. JPM & DE already on 10% trailing GTC; LLY −2.43% (below +5%) on its −7% hard stop as designed; SPY carries no stop by policy. **(Standing task: convert LLY's hard stop → 10% trailing once it tags ~+5% / ~$1,270.33.)**
- **(c) Daily loss cap:** today −0.48% → not tripped (well inside the −3% cap). Moot — no buys placed.

## Watch / next (next routine: **pre-market Mon 8/17**)
- **LLY — day 3, −2.43% from entry, the entire day's and week's drag.** Tightest cushion (~4.68%); the −7% hard stop @ 1125.15 is the safety net. No dated company news; PT hikes 8/13 support the thesis. Standing task: convert to 10% trailing at +5% (~$1,270.33). If it keeps drifting Monday, re-verify the thesis is intact (not a break) — but there is no trigger yet.
- **DE — cushion ~4.81% (tightest trailing).** **Q3 Thu Aug 20 9:00 CT (~3 trading days out)** — now inside the earnings window. AGCO miss + DE layoffs raise gap-through-cushion odds on a Q3 miss. **Pre-commit hold-through-print vs tighten/exit decision due Mon/Tue.** Do NOT add ahead.
- **JPM — cushion ~9.09%**, healthy; below hwm so floor unchanged; thesis intact; next earnings ~Oct.
- **SPY floor COMPLETE** (cash ~36%). Rebalance rule fires only if a new ≥70 conviction buy would push cash below the 10–20% buffer (trim floor first). Two conviction slots remain; cash ~36% — room for ~1 more conviction buy before the floor would need trimming.
- **Conviction gate:** empty at last scan. Bench top: PWR ~68 (grid/power, best news stale — needs a fresh verified catalyst), AMGN ~70 EXTENDED (+13.5% vs 50dMA → bench-for-pullback), ABT ~64, MRK ~60 (FDA PDUFA Aug 17 — do-not-buy-pre-event). Weekly conviction budget resets to 0/3 Monday.

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
