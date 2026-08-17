# Portfolio

**Last updated:** 2026-08-17 08:35 CT — **MARKET OPEN (Mon).** Market CONFIRMED OPEN via /v2/clock (is_open:true, 09:33 ET, next_close 16:00 ET). Account (live): equity **$101,170.68**, cash **$36,641.95** (~36.22%), long_market_value **$64,528.73** (~63.78%), buying_power $327,248.24, status ACTIVE, trading_blocked false. `last_equity` (Fri 8/14 close) $101,378.01 → intraday **−$207.33 / −0.20%**. **NO TRADES this routine** — nothing cleared the ≥70 conviction gate (per pre-market plan; ETN still extended), no position at/through a stop, no thesis break. Conviction sleeve **3 of 5 (two slots OPEN); weekly conviction buys 0/3** (new week). All three stops re-confirmed RESTING (open-orders nested=true, exactly 3, SPY zero). Zero overnight fills (closed-orders since 8/15 = empty). **Inbox: nothing pending.**

## Snapshot (live open marks — 2026-08-17 09:33 ET)
- **Equity $101,170.68.** Total since $100K start: **+1.17%.**
- **Net open unrealized: +$1,090.84** (JPM +1,132.35, DE +347.05, SPY +97.56, LLY −486.12).
- **Cash 36.22%** — well above the 10–20% minimum buffer.
- Intraday −$207.33 / −0.20% (mostly LLY). *(Daily/weekly benchmark scorecard is owned by the market-close & Friday weekly-review routines.)*

## Open positions (3 conviction stocks + 1 index-floor sleeve) — live marks 8/17 09:33 ET
| Symbol | Shares | Avg Cost | Price | P/L $ | P/L % | Stop | Entry Date | Thesis (1 line) |
|---|---|---|---|---|---|---|---|---|
| JPM | 34 | 329.695588 | 363.00 | +1,132.35 | +10.10% | **10% TRAILING (GTC)**, floor **329.85**, hwm 366.5 | 2026-06-29 | JPMorgan — $50B buyback + div hike; largest US bank; Q2 beat. Wells Fargo PT $390 OW (8/16); DB Buy $375. Thesis intact & reinforced; next earnings ~Oct. **Cushion ~9.13%.** |
| DE | 22 | 589.82 | 605.595 | +347.05 | +2.68% | **10% TRAILING (GTC)**, floor **579.591**, hwm 643.99 | 2026-06-04 | Deere — Q2 beat, FY26 guide raised, ag/onshoring tailwind. **Q3 CONFIRMED Thu Aug 20 BMO 9:00 CT** (cons ~$4.71–4.85 EPS / ~$10.8B rev; FY26 $4.5–5.0B guide MAINTAINED → base case reaffirm). JPMorgan cut PT $590→$570, MAINTAINED Neutral (8/14). Do NOT add ahead. **Pre-commit hold-through-print vs tighten/exit due Mon/Tue. Cushion ~4.29% (tightest trailing).** |
| LLY | 12 | 1209.84 | 1169.33 | −486.12 | −3.35% | **−7% HARD STOP (GTC) @ 1125.15** | 2026-08-12 | Eli Lilly — Q2 beat-and-raise (RAISED FY26 EPS $35.50–36.50) + GLP-1/obesity tailwind. Day-4 drift; no negative company/FDA news [VERIFIED-as-absence]. Competitive read FAVORS us (Berenberg cut Novo→Hold 8/12: "Lilly is taking the oral market"). PT hikes 8/13 stand. Conviction ~73 (B+). Hard stop converts to 10% trailing once +5% (~$1,270.33). **Cushion ~3.78% — tightest in book; watch today.** |
| SPY | 32 | 772.921250 | 775.97 | +97.56 | +0.39% | **NONE — index-floor sleeve, deliberate no-stop carve-out** | 2026-08-10 (t1) / 2026-08-11 (t2) | S&P 500 market floor (Lauren-approved Option B), COMPLETE. Own sleeve, EXEMPT from ≤20%/max-5/max-3-per-week caps; NO −7%/trailing stop. Buy-and-hold-the-market. |

**Conviction sleeve: 3 of 5 (two slots OPEN).** **Conviction buys used this week: 0 of 3** (reset Mon 8/17; the SPY floor does NOT consume this budget). **Cash buffer: ~36.22%.** Position sizes (on equity $101,170.68): JPM ~12.20%, DE ~13.17%, LLY ~13.87%, SPY ~24.54% (index sleeve — exempt from the 20% single-position cap by policy).

## Closed THIS WEEK
- **None** (week of Mon 8/17). Last close: LLY trailing-stop 7/31 (+$627), since re-entered 8/12.

## Stop-management state (re-confirmed RESTING via open-orders, nested=true — 8/17 09:33 ET)
- **JPM 10% trailing** `8a937ff6-164c-4384-8cf8-c000d4106a60` — hwm **366.5**, floor (stop_price) **329.85**, status new (resting). Price 363.00, cushion ~9.13%. Below hwm → no ratchet. qty 34.
- **DE 10% trailing** `dcdd84e5-6b94-4943-aa5b-3d3a299cbfce` — hwm **643.99**, floor (stop_price) **579.591**, status new (resting). Price 605.595, cushion ~4.29%. Below hwm → no ratchet. qty 22.
- **LLY −7% hard stop** `f50e3c39-0719-497e-8ccc-6006e6afa290` — stop_price **1125.15** (=1209.84×0.93), GTC, status new (resting). Price 1169.33 (−3.35% from entry). **Converts to a 10% trailing stop once LLY is +5% in profit** (trigger ~$1,270.33). Cushion to stop ~3.78% — tightest in book. qty 12.
- **SPY — NO STOP by design** (index-floor sleeve carve-out). qty_available 32 (unencumbered). Intentional per the 8/7 policy; do NOT place a stop on the floor.

## Risk checks (live open)
- **(a) Any position −7% or worse un-stopped?** NO. JPM +10.10%, DE +2.68%, LLY −3.35% (well above its −7% hard stop @ 1125.15), SPY +0.39%. **→ No sell triggered.**
- **(b) Any position +5%+ needing hard→trailing conversion?** NO conversion pending. JPM & DE already on 10% trailing GTC; LLY −3.35% (below +5%) on its −7% hard stop as designed; SPY carries no stop by policy. **(Standing task: convert LLY's hard stop → 10% trailing once it tags ~+5% / ~$1,270.33.)**
- **(c) Daily loss cap:** intraday −0.20% (well inside −3%) → not tripped. Moot — no buys placed.

## Watch / next (next routine: **midday Mon 8/17**)
- **DE — Q3 Thu Aug 20 BMO.** Pre-commit hold-through-print vs tighten/exit DUE Mon/Tue. Base case = reaffirmed guide (hold), but AGCO −11% + DE layoffs + JPM $570 PT cut raise gap-through-cushion odds on a miss; cushion ~4.29%. Do NOT add ahead.
- **LLY — tightest cushion (~3.78%).** Drifted to −3.35% at the open; watch it holds well above the 1125.15 stop today; thesis intact, competitive read favorable. Standing task: convert to 10% trailing at +5% (~$1,270.33).
- **JPM — cushion ~9.13%**, healthy & reinforced (WF PT $390); below hwm so floor unchanged; next earnings ~Oct.
- **SPY floor COMPLETE** (cash ~36%). Two conviction slots remain; room for ~1 more conviction buy before the floor would need trimming.
- **Conviction gate:** empty. Bench top: ETN ~66 (extended, wait ~$420–430 base), ANET ~69 (50dMA unverified), AMGN ~68 (extended), ABT ~66 (borderline extended), PWR ~62 (one signal), ABBV ~58 (clean entry, one signal).

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
