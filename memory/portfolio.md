# Portfolio

**Last updated:** 2026-08-17 12:05 CT — **MIDDAY (Mon).** Market CONFIRMED OPEN via /v2/clock (is_open:true, 13:02 ET, next_close 16:00 ET). Account (live): equity **$101,465.30**, cash **$36,641.95** (~36.11%), long_market_value **$64,823.35** (~63.89%), buying_power $328,073.18, status ACTIVE, trading_blocked false. `last_equity` (Fri 8/14 close) $101,378.01 → intraday **+$87.29 / +0.086%** (up on the day). **NO TRADES this routine** — no position at/through a stop, no +5% hard→trailing conversion pending, no thesis break, no breaking catalyst that clears the ≥70 gate. Conviction sleeve **3 of 5 (two slots OPEN); weekly conviction buys 0/3.** All three stops re-confirmed RESTING (open-orders nested=true, exactly 3, SPY zero). Zero fills since 8/15 (closed-orders empty). **Inbox: nothing pending.**

## Snapshot (live midday marks — 2026-08-17 13:02 ET)
- **Equity $101,465.30.** Total since $100K start: **+1.47%.**
- **Net open unrealized: +$1,386.10** (JPM +1,175.53, DE +347.05, SPY +56.60, LLY −193.08).
- **Cash 36.11%** — well above the 10–20% minimum buffer.
- Intraday **+$87.29 / +0.086%** — LLY recovering (+1.15% today) leads; SPY floor tracks the index dip. *(Daily/weekly benchmark scorecard is owned by the market-close & Friday weekly-review routines.)*

## Open positions (3 conviction stocks + 1 index-floor sleeve) — live marks 8/17 13:02 ET
| Symbol | Shares | Avg Cost | Price | P/L $ | P/L % | Stop | Entry Date | Thesis (1 line) |
|---|---|---|---|---|---|---|---|---|
| JPM | 34 | 329.695588 | 364.27 | +1,175.53 | +10.49% | **10% TRAILING (GTC)**, floor **329.85**, hwm 366.5 | 2026-06-29 | JPMorgan — $50B buyback + div hike; largest US bank; Q2 beat. Wells Fargo PT $390 OW (8/16); DB Buy $375. Thesis intact & reinforced; next earnings ~Oct. Below hwm → no ratchet. **Cushion ~9.45%.** |
| DE | 22 | 589.82 | 605.595 | +347.05 | +2.68% | **10% TRAILING (GTC)**, floor **579.591**, hwm 643.99 | 2026-06-04 | Deere — Q2 beat, FY26 guide raised, ag/onshoring tailwind. **Q3 CONFIRMED Thu Aug 20 BMO 9:00 CT** (base case = reaffirm FY26 $4.5–5.0B). JPMorgan cut PT $590→$570, MAINTAINED Neutral (8/14). Do NOT add ahead. **Hold-through-print pre-commit: LEAN HOLD (trailing stop is the safety net) — finalize at close/pre-market Tue. Cushion ~4.29% (tightest trailing).** |
| LLY | 12 | 1209.84 | 1193.75 | −193.08 | −1.33% | **−7% HARD STOP (GTC) @ 1125.15** | 2026-08-12 | Eli Lilly — Q2 beat-and-raise (RAISED FY26 EPS $35.50–36.50) + GLP-1/obesity tailwind. **Firming today (+1.15% intraday, was −3.35% at Fri close)** — early wobble was noise; no negative company/FDA news. Competitive read favorable (Berenberg cut Novo→Hold 8/12). Conviction ~73 (B+). Hard stop converts to 10% trailing once +5% (~$1,270.33). **Cushion ~5.75%.** |
| SPY | 32 | 772.921250 | 774.69 | +56.60 | +0.23% | **NONE — index-floor sleeve, deliberate no-stop carve-out** | 2026-08-10 (t1) / 2026-08-11 (t2) | S&P 500 market floor (Lauren-approved Option B), COMPLETE. Own sleeve, EXEMPT from ≤20%/max-5/max-3-per-week caps; NO −7%/trailing stop. Buy-and-hold-the-market. |

**Conviction sleeve: 3 of 5 (two slots OPEN).** **Conviction buys used this week: 0 of 3** (week of Mon 8/17; the SPY floor does NOT consume this budget). **Cash buffer: ~36.11%.** Position sizes (on equity $101,465.30): JPM ~12.21%, DE ~13.13%, LLY ~14.12%, SPY ~24.43% (index sleeve — exempt from the 20% single-position cap by policy).

## Closed THIS WEEK
- **None** (week of Mon 8/17). Last close: LLY trailing-stop 7/31 (+$627), since re-entered 8/12.

## Stop-management state (re-confirmed RESTING via open-orders, nested=true — 8/17 13:02 ET)
- **JPM 10% trailing** `8a937ff6-164c-4384-8cf8-c000d4106a60` — hwm **366.5**, floor (stop_price) **329.85**, status new (resting). Price 364.27, cushion ~9.45%. Below hwm → no ratchet. qty 34.
- **DE 10% trailing** `dcdd84e5-6b94-4943-aa5b-3d3a299cbfce` — hwm **643.99**, floor (stop_price) **579.591**, status new (resting). Price 605.595, cushion ~4.29%. Below hwm → no ratchet. qty 22.
- **LLY −7% hard stop** `f50e3c39-0719-497e-8ccc-6006e6afa290` — stop_price **1125.15** (=1209.84×0.93), GTC, status new (resting). Price 1193.75 (−1.33% from entry). **Converts to a 10% trailing stop once LLY is +5% in profit** (trigger ~$1,270.33). Cushion to stop ~5.75%. qty 12.
- **SPY — NO STOP by design** (index-floor sleeve carve-out). qty_available 32 (unencumbered). Intentional per the 8/7 policy; do NOT place a stop on the floor.

## Risk checks (live midday)
- **(a) Any position −7% or worse un-stopped?** NO. JPM +10.49%, DE +2.68%, LLY −1.33% (well above its −7% hard stop @ 1125.15), SPY +0.23%. **→ No sell triggered; no mandatory 4-hour news check required.**
- **(b) Any position +5%+ needing hard→trailing conversion?** NO conversion pending. JPM & DE already on 10% trailing GTC; LLY −1.33% (below +5%) on its −7% hard stop as designed; SPY carries no stop by policy. **(Standing task: convert LLY's hard stop → 10% trailing once it tags ~+5% / ~$1,270.33.)**
- **(c) Daily loss cap:** intraday **+0.086%** (up on the day, well inside −3%) → not tripped. Moot — no buys placed.

## Watch / next (next routine: **market-close Mon 8/17**)
- **DE — Q3 Thu Aug 20 BMO.** Hold-through-print pre-commit DUE Mon/Tue → **LEAN HOLD** (base case = reaffirmed FY26 guide; the 10% trailing floor at 579.591 is the safety net; exiting on earnings-timing fear contradicts the fundamentals-driven thesis). Finalize at today's close / Tue pre-market. Cushion ~4.29% (tightest); a hard gap-down miss is the tail risk. Do NOT add ahead.
- **LLY — firming.** Recovered to −1.33% (from −3.35% Fri close) on +1.15% intraday; thesis intact, competitive read favorable. Cushion ~5.75%. Standing task: convert to 10% trailing at +5% (~$1,270.33).
- **JPM — cushion ~9.45%**, healthy & reinforced (WF PT $390); below hwm so floor unchanged; next earnings ~Oct.
- **SPY floor COMPLETE** (cash ~36%). Two conviction slots remain; room for ~1 more conviction buy before the floor would need trimming.
- **Conviction gate:** empty. Bench top: ANET ~69, AMGN ~68, ABT ~66, ETN ~66 (wait for base), PWR ~62 (one signal), ABBV ~58 (one signal).

## Recent closes (last 5)
| Symbol | Exit Date | Shares | Entry | Exit | P/L $ | P/L % | Reason |
|---|---|---|---|---|---|---|---|
| LLY | 2026-07-31 | 14 | 1078.46 | 1123.27 | +627.34 | +4.15% | 10% trailing stop fired (give-back from ~1249 hwm; no thesis break). **RE-ENTERED 8/12 on the verified beat-and-raise.** |
| GE | 2026-07-16 | 45 | 329.63 | 344.54 | +670.95 | +4.52% | 10% trailing stop fired (post-Q2-earnings give-back caught the profit; no verified thesis break) |
| ETN | 2026-07-02 | 24 | 401.5425 | 392.75 | −211.02 | −2.19% | 10% trailing stop fired (beta/thin pre-holiday tape, not thesis break) |
| NVDA | 2026-06-05 | 55 | 220.15 | 204.7158 | −848.88 | −7.01% | −7% hard stop fired (macro/NFP semis selloff, not thesis break) |
| NVDA | 2026-05-04 | 25 | 201.38 | ~195.02 | −159.04 | −3.16% | 10% trailing stop fired (round-trip) |

---
*Overwrite this file every routine. Keep it a live snapshot, not a log.*
