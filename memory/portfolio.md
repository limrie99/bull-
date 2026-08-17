# Portfolio

**Last updated:** 2026-08-17 15:05 CT — **MARKET CLOSE (Mon, new week day 1).** Market CONFIRMED CLOSED via /v2/clock (is_open:false, 16:01 ET, next_open Tue 8/18 09:30 ET). Account (closing, live): equity **$101,060.19**, cash **$36,641.95** (~36.26%), long_market_value **$64,418.24** (~63.74%), buying_power $326,938.87, status ACTIVE, trading_blocked false. `last_equity` (Fri 8/14 close) $101,378.01 → **day −$317.82 / −0.313%** (down on the day). **NO TRADES this routine** — no position at/through a stop, no +5% hard→trailing conversion pending, no thesis break, no breaking catalyst that clears the ≥70 gate. Conviction sleeve **3 of 5 (two slots OPEN); weekly conviction buys 0/3.** All three stops re-confirmed RESTING (open-orders nested=true, exactly 3, SPY zero). Zero fills today (closed-orders empty). **Inbox: nothing pending.**

## Benchmark scorecard (closing — 2026-08-17)
- **Day: portfolio −0.313% vs SPY −0.474% → alpha +0.161 pt.** A down day, but we fell LESS than the market → we BEAT SPY today (alpha earned on defense — the index floor + a resilient book).
- **Week-to-date (week of Mon 8/17, day 1; base = Fri 8/14 close $101,378.01 / SPY 776.30):** portfolio −0.313% vs SPY −0.474% → **WTD alpha +0.161 pt.**
- SPY: Fri 8/14 close **776.30** → today close **772.62** (IEX daily bars; latest trade 772.64).

## Snapshot (closing marks — 2026-08-17 16:00 ET)
- **Equity $101,060.19.** Total since $100K start: **+1.06%.**
- **Net open unrealized: +$981.95** (JPM +1,062.99, DE +222.20, SPY −7.08, LLY −296.16).
- **Cash 36.26%** — well above the 10–20% minimum buffer.
- Day **−$317.82 / −0.313%** — whole book drifted down with a quiet risk-off tape; LLY the biggest drag (gave back its midday pop), SPY floor cushioned the fall so we still beat the index.

## Open positions (3 conviction stocks + 1 index-floor sleeve) — closing marks 8/17 16:00 ET
| Symbol | Shares | Avg Cost | Price | P/L $ | P/L % | Stop | Entry Date | Thesis (1 line) |
|---|---|---|---|---|---|---|---|---|
| JPM | 34 | 329.695588 | 360.96 | +1,062.99 | +9.48% | **10% TRAILING (GTC)**, floor **329.85**, hwm 366.5 | 2026-06-29 | JPMorgan — $50B buyback + div hike; largest US bank; Q2 beat. Wells Fargo PT $390 OW (8/16); DB Buy $375. Thesis intact & reinforced; next earnings ~Oct. Day −0.57%; below hwm → no ratchet. **Cushion ~8.62%.** |
| DE | 22 | 589.82 | 599.92 | +222.20 | +1.71% | **10% TRAILING (GTC)**, floor **579.591**, hwm 643.99 | 2026-06-04 | Deere — Q2 beat, FY26 guide raised, ag/onshoring tailwind. **Q3 CONFIRMED Thu Aug 20 BMO 9:00 CT** (base case = reaffirm FY26 $4.5–5.0B). JPMorgan cut PT $590→$570, MAINTAINED Neutral (8/14). Do NOT add ahead. **Hold-through-print pre-commit: LEAN HOLD (trailing floor 579.591 is the safety net) — finalize at Tue pre-market. Day −0.94%; cushion ~3.39% (tightest trailing).** |
| LLY | 12 | 1209.84 | 1185.16 | −296.16 | −2.04% | **−7% HARD STOP (GTC) @ 1125.15** | 2026-08-12 | Eli Lilly — Q2 beat-and-raise (RAISED FY26 EPS $35.50–36.50) + GLP-1/obesity tailwind. Round-tripped intraday (was +1.15% midday, closed −2.04%); still noise, no dated company/FDA news; competitive read favorable (Berenberg cut Novo→Hold 8/12). Conviction ~73 (B+). Hard stop converts to 10% trailing once +5% (~$1,270.33). **Cushion ~5.06%.** |
| SPY | 32 | 772.921250 | 772.70 | −7.08 | −0.03% | **NONE — index-floor sleeve, deliberate no-stop carve-out** | 2026-08-10 (t1) / 2026-08-11 (t2) | S&P 500 market floor (Lauren-approved Option B), COMPLETE. Own sleeve, EXEMPT from ≤20%/max-5/max-3-per-week caps; NO −7%/trailing stop. Buy-and-hold-the-market; day −0.47% tracked the index. |

**Conviction sleeve: 3 of 5 (two slots OPEN).** **Conviction buys used this week: 0 of 3** (week of Mon 8/17; the SPY floor does NOT consume this budget). **Cash buffer: ~36.26%.** Position sizes (on equity $101,060.19): JPM ~12.14%, DE ~13.06%, LLY ~14.07%, SPY ~24.47% (index sleeve — exempt from the 20% single-position cap by policy).

## Closed THIS WEEK
- **None** (week of Mon 8/17). Last close: LLY trailing-stop 7/31 (+$627), since re-entered 8/12.

## Stop-management state (re-confirmed RESTING via open-orders, nested=true — 8/17 16:00 ET)
- **JPM 10% trailing** `8a937ff6-164c-4384-8cf8-c000d4106a60` — hwm **366.5**, floor (stop_price) **329.85**, status new (resting). Price 360.96, cushion ~8.62%. Below hwm → no ratchet. qty 34.
- **DE 10% trailing** `dcdd84e5-6b94-4943-aa5b-3d3a299cbfce` — hwm **643.99**, floor (stop_price) **579.591**, status new (resting). Price 599.92, cushion ~3.39%. Below hwm → no ratchet. qty 22.
- **LLY −7% hard stop** `f50e3c39-0719-497e-8ccc-6006e6afa290` — stop_price **1125.15** (=1209.84×0.93), GTC, status new (resting). Price 1185.16 (−2.04% from entry). **Converts to a 10% trailing stop once LLY is +5% in profit** (trigger ~$1,270.33). Cushion to stop ~5.06%. qty 12.
- **SPY — NO STOP by design** (index-floor sleeve carve-out). qty_available 32 (unencumbered). Intentional per the 8/7 policy; do NOT place a stop on the floor.

## Risk checks (closing)
- **(a) Any position −7% or worse un-stopped?** NO. JPM +9.48%, DE +1.71%, LLY −2.04% (well above its −7% hard stop @ 1125.15), SPY −0.03%. **→ No sell triggered.**
- **(b) Any position +5%+ needing hard→trailing conversion?** NO conversion pending. JPM & DE already on 10% trailing GTC; LLY −2.04% (below +5%) on its −7% hard stop as designed; SPY carries no stop by policy. **(Standing task: convert LLY's hard stop → 10% trailing once it tags ~+5% / ~$1,270.33.)**
- **(c) Daily loss cap:** day **−0.313%** (well inside −3%) → not tripped. Moot — no buys placed.

## Watch / next (next routine: **pre-market Tue 8/18**)
- **DE — Q3 Thu Aug 20 BMO.** Finalize the hold-through-print pre-commit at Tue pre-market → **LEAN HOLD** (base case = reaffirmed FY26 guide; the 10% trailing floor at 579.591 is the safety net; exiting on earnings-timing fear contradicts the fundamentals-driven thesis). Softened into the print today (−0.94%); cushion now ~3.39% (tightest). A hard gap-down miss is the tail risk. Do NOT add ahead.
- **LLY — round-tripped intraday.** Closed −2.04% after a midday +1.15% pop; still noise, thesis intact, competitive read favorable. Cushion ~5.06%. Standing task: convert to 10% trailing at +5% (~$1,270.33).
- **JPM — cushion ~8.62%**, healthy & reinforced (WF PT $390); below hwm so floor unchanged; next earnings ~Oct.
- **SPY floor COMPLETE** (cash ~36%). Two conviction slots remain; room for ~1 more conviction buy before the floor would need trimming.
- **Conviction gate:** empty. Bench top: ANET ~69, AMGN ~68 (both need a clean non-extended entry), ABT ~66, ETN ~66 (wait for base), PWR ~62 (one signal), ABBV ~58 (one signal).

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
