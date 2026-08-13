# Portfolio

**Last updated:** 2026-08-13 12:15 CT — **MIDDAY (Thu).** Market CONFIRMED OPEN via /v2/clock (is_open:true, 13:14 ET, next_close 16:00 ET). Account: equity **$101,942.96**, cash **$36,641.95** (~35.94%), long_market_value **$65,301.01** (~64.06%), buying_power $329,410.63, status ACTIVE. `last_equity` (Wed 8/12 close) $102,056.05 → **today −$113.09 / −0.111%** (essentially flat; stocks softened intraday while SPY floor tracks the index up). **NO TRADES THIS ROUTINE** — no position at a risk trigger, no hard→trailing conversion pending, nothing clears the ≥70 gate for a midday breaking-catalyst buy. All three stops re-confirmed RESTING (nested=true). Conviction sleeve **3 of 5 stocks (two slots OPEN); weekly conviction buys 1/3** (SPY floor exempt). **Inbox: nothing pending.**

## Scorecard (MIDDAY 2026-08-13 — unofficial; close routine owns official daily number)
- **Equity $101,942.96.** Total since $100K start: **+1.94%.**
- **Today −$113.09 / −0.111%** vs Wed 8/12 close $102,056.05 (essentially flat).
- **SPY intraday:** 8/12 close 772.49 → live 777.15 = **+0.603%**. Book −0.111% → **intraday alpha ~−0.71 pt** (JPM/DE/LLY all softened a touch intraday while SPY rose; the ~24% SPY floor tracks the index up 1:1 — the lag is name-specific stock noise, not the cash drag of prior weeks). Close routine computes the official number.
- **Week-to-date (from Fri 8/7 close $101,707.48):** **+$235.48 / +0.231%** (unofficial, midday marks).
- **Net open unrealized: +$1,870.43** (JPM +1,143.23, DE +509.08, SPY +135.32, LLY +82.80).
- **Cash 35.94%** — well above the 10–20% minimum buffer.

## Open positions (3 conviction stocks + 1 index-floor sleeve) — MIDDAY marks 8/13

| Symbol | Shares | Avg Cost | Mark | P/L $ | P/L % | Stop | Entry Date | Thesis (1 line) |
|---|---|---|---|---|---|---|---|---|
| JPM | 34 | 329.695588 | 363.32 | +1,143.23 | +10.20% | **10% TRAILING (GTC)**, floor **329.85**, hwm 366.5 | 2026-06-29 | JPMorgan — $50B buyback + div hike; largest US bank; Q2 beat; DB Buy PT $375. Softened slightly intraday (363.71→363.32), below hwm so no ratchet. Thesis intact; next earnings ~Oct. **Cushion ~9.21%.** |
| DE | 22 | 589.82 | 612.96 | +509.08 | +3.92% | **10% TRAILING (GTC)**, floor **579.591**, hwm 643.99 | 2026-06-04 | Deere — Q2 beat, FY26 guide raised, ag/onshoring tailwind. On a 10% trailing stop already (no conversion needed). **PRINT RISK into Q3 Thu Aug 20 9:00 CT** (AGCO missed −11% on 8/6; DE announced ~238 layoffs; Evercore trimmed PT 641→632 but MAINTAINED). Do NOT add ahead. **Cushion ~5.44%** (tightest name; dipped intraday). |
| LLY | 12 | 1209.84 | 1216.74 | +82.80 | +0.57% | **−7% HARD STOP (GTC) @ 1125.15** | 2026-08-12 | Eli Lilly — Q2 beat-and-raise (rev $22.974B, adj EPS $8.38, RAISED FY26 EPS $35.50–36.50) + GLP-1/obesity secular tailwind. Day 3, +0.57% (softened intraday from 1232 to 1217 — normal wiggle, no news). Conviction ~73 (B+). Hard stop converts to 10% trailing once +5% (~$1,270.33, ~+4.4% away). Next earnings ~Nov. |
| SPY | 32 | 772.921250 | 777.15 | +135.32 | +0.55% | **NONE — index-floor sleeve, deliberate no-stop carve-out** | 2026-08-10 (t1) / 2026-08-11 (t2) | S&P 500 market floor (Lauren-approved Option B), COMPLETE. Idle cash parked in the index so it MATCHES the benchmark. Own sleeve, EXEMPT from ≤20%/max-5/max-3-per-week caps; NO −7%/trailing stop. Buy-and-hold-the-market. |

**Conviction sleeve: 3 of 5 (two slots OPEN).** **Conviction buys used this week: 1 of 3** (the SPY floor does NOT consume this budget). **Cash buffer: ~35.94%.** Position sizes (on equity $101,942.96): JPM ~12.12%, DE ~13.23%, LLY ~14.32%, SPY ~24.40% (index sleeve — exempt from the 20% single-position cap by policy).

## Closed THIS WEEK
- **None** (week began Mon 8/10). Last close: LLY trailing-stop exit 7/31 (+$627.34 / +4.15%) — RE-ENTERED 8/12 on the fresh verified beat-and-raise catalyst.

## Stop-management state (re-confirmed RESTING via open-orders, nested=true — midday 8/13)
- **JPM 10% trailing** `8a937ff6-164c-4384-8cf8-c000d4106a60` — hwm **366.5**, floor (stop_price) **329.85**, status new (resting). Mark 363.32, cushion ~9.21%. Below hwm → no ratchet this run. qty 34.
- **DE 10% trailing** `dcdd84e5-6b94-4943-aa5b-3d3a299cbfce` — hwm **643.99**, floor (stop_price) **579.591**, status new (resting). Mark 612.96, cushion ~5.44%. Below hwm → no ratchet. qty 22.
- **LLY −7% hard stop** `f50e3c39-0719-497e-8ccc-6006e6afa290` — stop_price **1125.15** (=1209.84×0.93), GTC, status new (resting). Mark 1216.74 (+0.57%). **Converts to a 10% trailing stop once LLY is +5% in profit** (trigger ~$1,270.33). qty 12.
- **SPY — NO STOP by design** (index-floor sleeve carve-out). qty_available 32 (unencumbered). Intentional per the 8/7 policy; do NOT place a stop on the floor.

## Risk checks (midday)
- **(a) Any position −7% or worse un-stopped?** NO. JPM +10.20%, DE +3.92%, LLY +0.57%, SPY +0.55%. **→ No sell, no 4-hour news check triggered.**
- **(b) Any position +5%+ needing hard→trailing conversion?** NO conversion pending. JPM ≥+5% but already on 10% trailing GTC; DE +3.92% already on 10% trailing GTC; LLY +0.57% (below +5%) on its −7% hard stop as designed; SPY carries no stop by policy. **(Standing task: convert LLY's hard stop → 10% trailing once it tags ~+5% / ~$1,270.33.)**
- **(c) Daily loss cap:** today −0.111% (essentially flat) → not tripped. Moot — no buys planned at midday.

## Watch / next (next routine: **market-close Thu 8/13**)
- **Market-close owns the mandatory daily "how we're doing" Telegram push + official scorecard vs SPY.**
- **LLY — day 3, +0.57%.** Softened intraday (1232→1217) on no news — normal. Watch it holds above the 50dMA (~$1,165); −7% hard stop at 1125.15 is the safety net. Standing task: convert to 10% trailing at +5% (~$1,270.33, ~+4.4% away).
- **DE — cushion ~5.44%** (tightest, dipped intraday). **Q3 Aug 20 is the dominant event** — AGCO miss + DE layoffs raise gap-through-cushion odds on a Q3 miss. Pre-commit hold-through-print vs tighten/exit by early next week. Do NOT add ahead.
- **JPM — cushion ~9.21%**, healthy; below hwm so floor unchanged; thesis intact; next earnings ~Oct.
- **SPY floor COMPLETE** (cash ~36%). Rebalance rule fires only if a new ≥70 conviction buy would push cash below the 10–20% buffer (trim floor first). Two conviction slots remain, cash ~36% — room for ~1 more conviction buy before the floor would need trimming.
- **Conviction gate:** empty at last pre-market scan. AMGN (~70) ran EXTENDED (+13.5% vs 50dMA) → bench-for-a-pullback, not a buy. Bench (all UNVERIFIED, carry stale): DDOG ~70, ABT ~69, NET ~68, TDG ~65, ETN ~64 (chase, high-beta ≤10% cap), NOC ~60. Next pre-market re-scores.

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
