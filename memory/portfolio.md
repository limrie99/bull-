# Portfolio

**Last updated:** 2026-08-13 15:00 CT — **MARKET CLOSE (Thu).** Market CONFIRMED CLOSED via /v2/clock (is_open:false, 16:01 ET, next_open 8/14 09:30 ET). Account: equity **$101,857.89**, cash **$36,641.95** (~35.97%), long_market_value **$65,215.94** (~64.03%), buying_power $329,172.43, status ACTIVE. `last_equity` (Wed 8/12 close) $102,056.05 → **today −$198.16 / −0.194%** (a small down day). **NO TRADES TODAY** — no position at a risk trigger, no hard→trailing conversion pending, nothing cleared the ≥70 buy-gate. All three stops re-confirmed RESTING (open-orders nested=true). Conviction sleeve **3 of 5 stocks (two slots OPEN); weekly conviction buys 1/3** (SPY floor exempt). **Inbox: nothing pending.**

## Scorecard (OFFICIAL — market close 2026-08-13)
- **Equity $101,857.89.** Total since $100K start: **+1.86%.**
- **Today −$198.16 / −0.194%** vs Wed 8/12 close $102,056.05 (small down day).
- **SPY today +0.686%** (8/12 close 772.54 → 8/13 close 777.84). **Alpha today = −0.88 pt** — we lagged. The whole miss is name-specific: all three conviction stocks softened on an up-tape (JPM −0.57%, DE −1.19%, LLY −0.92%) while the SPY floor rose +0.68% with the index. The ~24% index sleeve was the only green contributor today — it did exactly its job.
- **Week-to-date (from Fri 8/7 close $101,707.48):** **+$150.41 / +0.148%** vs **SPY WTD +0.605%** (8/7 close 773.16 → 777.84) → **week alpha −0.457 pt** (behind week-to-date; DE/LLY softness this week the main drag).
- **Net open unrealized: +$1,778.69** (JPM +1,136.09, DE +496.32, SPY +155.16, LLY −8.88).
- **Cash 35.97%** — well above the 10–20% minimum buffer.

## Open positions (3 conviction stocks + 1 index-floor sleeve) — CLOSING marks 8/13

| Symbol | Shares | Avg Cost | Close | P/L $ | P/L % | Stop | Entry Date | Thesis (1 line) |
|---|---|---|---|---|---|---|---|---|
| JPM | 34 | 329.695588 | 363.11 | +1,136.09 | +10.14% | **10% TRAILING (GTC)**, floor **329.85**, hwm 366.5 | 2026-06-29 | JPMorgan — $50B buyback + div hike; largest US bank; Q2 beat; DB Buy PT $375. Slipped −0.57% today, below hwm so no ratchet. Thesis intact; next earnings ~Oct. **Cushion ~9.16%.** |
| DE | 22 | 589.82 | 612.38 | +496.32 | +3.83% | **10% TRAILING (GTC)**, floor **579.591**, hwm 643.99 | 2026-06-04 | Deere — Q2 beat, FY26 guide raised, ag/onshoring tailwind. Weakest name today (−1.19%). **PRINT RISK into Q3 Thu Aug 20 9:00 CT (~4 trading days out)** — AGCO missed −11% on 8/6; DE announced ~238 layoffs; Evercore trimmed PT 641→632 but MAINTAINED. Do NOT add ahead. **Cushion ~5.35%** (tightest name). |
| LLY | 12 | 1209.84 | 1209.10 | −8.88 | −0.06% | **−7% HARD STOP (GTC) @ 1125.15** | 2026-08-12 | Eli Lilly — Q2 beat-and-raise (rev $22.974B, adj EPS $8.38, RAISED FY26 EPS $35.50–36.50) + GLP-1/obesity secular tailwind. Day 3, gave back to flat (−0.92% today, no news — normal wiggle). Conviction ~73 (B+). Hard stop converts to 10% trailing once +5% (~$1,270.33, ~+5.0% away). Next earnings ~Nov. **Cushion ~6.94%.** |
| SPY | 32 | 772.921250 | 777.77 | +155.16 | +0.63% | **NONE — index-floor sleeve, deliberate no-stop carve-out** | 2026-08-10 (t1) / 2026-08-11 (t2) | S&P 500 market floor (Lauren-approved Option B), COMPLETE. +0.68% today — the day's only green holding; idle cash parked in the index MATCHES the benchmark. Own sleeve, EXEMPT from ≤20%/max-5/max-3-per-week caps; NO −7%/trailing stop. Buy-and-hold-the-market. |

**Conviction sleeve: 3 of 5 (two slots OPEN).** **Conviction buys used this week: 1 of 3** (the SPY floor does NOT consume this budget). **Cash buffer: ~35.97%.** Position sizes (on equity $101,857.89): JPM ~12.12%, DE ~13.23%, LLY ~14.24%, SPY ~24.44% (index sleeve — exempt from the 20% single-position cap by policy).

## Closed THIS WEEK
- **None** (week began Mon 8/10). Last close: LLY trailing-stop exit 7/31 (+$627.34 / +4.15%) — RE-ENTERED 8/12 on the fresh verified beat-and-raise catalyst.

## Stop-management state (re-confirmed RESTING via open-orders, nested=true — close 8/13)
- **JPM 10% trailing** `8a937ff6-164c-4384-8cf8-c000d4106a60` — hwm **366.5**, floor (stop_price) **329.85**, status new (resting). Mark 363.11, cushion ~9.16%. Below hwm → no ratchet today. qty 34.
- **DE 10% trailing** `dcdd84e5-6b94-4943-aa5b-3d3a299cbfce` — hwm **643.99**, floor (stop_price) **579.591**, status new (resting). Mark 612.38, cushion ~5.35%. Below hwm → no ratchet. qty 22.
- **LLY −7% hard stop** `f50e3c39-0719-497e-8ccc-6006e6afa290` — stop_price **1125.15** (=1209.84×0.93), GTC, status new (resting). Mark 1209.10 (−0.06%). **Converts to a 10% trailing stop once LLY is +5% in profit** (trigger ~$1,270.33). qty 12.
- **SPY — NO STOP by design** (index-floor sleeve carve-out). qty_available 32 (unencumbered). Intentional per the 8/7 policy; do NOT place a stop on the floor.

## Risk checks (close)
- **(a) Any position −7% or worse un-stopped?** NO. JPM +10.14%, DE +3.83%, LLY −0.06%, SPY +0.63%. **→ No sell triggered.**
- **(b) Any position +5%+ needing hard→trailing conversion?** NO conversion pending. JPM ≥+5% but already on 10% trailing GTC; DE +3.83% already on 10% trailing GTC; LLY −0.06% (below +5%) on its −7% hard stop as designed; SPY carries no stop by policy. **(Standing task: convert LLY's hard stop → 10% trailing once it tags ~+5% / ~$1,270.33.)**
- **(c) Daily loss cap:** today −0.194% → not tripped (well inside the −3% cap). Moot — no buys placed.

## Watch / next (next routine: **pre-market Fri 8/14**)
- **DE — cushion ~5.35%** (tightest; weakest name today at −1.19%). **Q3 Thu Aug 20 9:00 CT is the dominant event, now ~4 trading days out** — approaching the 3-trading-day earnings window. AGCO miss + DE layoffs raise gap-through-cushion odds on a Q3 miss. **Pre-commit hold-through-print vs tighten/exit decision due early next week.** Do NOT add ahead.
- **LLY — day 3, drifted back to flat (−0.06%)** on no news — normal wiggle. Watch it holds above the 50dMA (~$1,165); −7% hard stop at 1125.15 is the safety net. Standing task: convert to 10% trailing at +5% (~$1,270.33, ~+5.0% away).
- **JPM — cushion ~9.16%**, healthy; below hwm so floor unchanged; thesis intact; next earnings ~Oct.
- **SPY floor COMPLETE** (cash ~36%). Rebalance rule fires only if a new ≥70 conviction buy would push cash below the 10–20% buffer (trim floor first). Two conviction slots remain, cash ~36% — room for ~1 more conviction buy before the floor would need trimming.
- **Conviction gate:** empty at last scan. AMGN (~70) ran EXTENDED (+13.5% vs 50dMA) → bench-for-a-pullback, not a buy. Bench (all UNVERIFIED, carry stale): DDOG ~70, ABT ~69, NET ~68, TDG ~65, ETN ~64 (chase, high-beta ≤10% cap), NOC ~60. Next pre-market re-scores.

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
