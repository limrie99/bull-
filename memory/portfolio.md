# Portfolio

**Last updated:** 2026-08-13 08:45 CT — **MARKET OPEN (Thu).** Market CONFIRMED OPEN via /v2/clock (is_open:true, 09:35 ET, next_close 16:00 ET). Account: equity **$102,173.09**, cash **$36,641.95** (~35.86%), long_market_value **$65,531.14** (~64.14%), buying_power $330,054.99, status ACTIVE. `last_equity` (Wed 8/12 close) $102,056.05 → **today +$117.04 / +0.115%**. **NO TRADES THIS ROUTINE** — pre-market's full 4-agent scan found nothing clearing the ≥70 gate (AMGN extended, others unverified); July PPI is out with no risk-off shock but no qualifying setup either. All three stops re-confirmed RESTING (JPM trailing hwm ratcheted to 366.5 on a fresh high). No position at/through a risk trigger; no hard→trailing conversion pending. Conviction sleeve **3 of 5 stocks (two slots OPEN); weekly conviction buys 1/3** (SPY floor exempt). **Inbox: nothing pending.**

## Scorecard (OPEN 2026-08-13 — unofficial; close routine owns official daily number)
- **Equity $102,173.09.** Total since $100K start: **+2.17%.**
- **Today +$117.04 / +0.115%** vs Wed 8/12 close $102,056.05 (early-session, will move).
- **SPY intraday:** 8/12 close 772.49 → live 775.70 = **+0.42%**. Intraday book +0.115% → **intraday alpha ~−0.30 pt** (JPM/DE slightly red intraday, SPY up; two-sided — close routine computes the official number).
- **Week-to-date (from Fri 8/7 close $101,707.48):** **+$465.61 / +0.458%** (unofficial, open marks).
- **Net open unrealized: +$2,095.63** (JPM +1,156.49, DE +581.90, LLY +268.32, SPY +88.92).
- **Cash 35.86%** — well above the 10–20% minimum buffer.

## Open positions (3 conviction stocks + 1 index-floor sleeve) — OPEN marks 8/13

| Symbol | Shares | Avg Cost | Mark | P/L $ | P/L % | Stop | Entry Date | Thesis (1 line) |
|---|---|---|---|---|---|---|---|---|
| JPM | 34 | 329.695588 | 363.71 | +1,156.49 | +10.32% | **10% TRAILING (GTC)**, floor **329.85**, hwm 366.5 | 2026-06-29 | JPMorgan — $50B buyback + div hike; largest US bank; Q2 beat; DB Buy PT $375. Made a **fresh high** overnight (hwm 366.06→366.5, floor→329.85). Thesis intact; next earnings ~Oct. **Cushion ~9.31%.** |
| DE | 22 | 589.82 | 616.27 | +581.90 | +4.48% | **10% TRAILING (GTC)**, floor **579.591**, hwm 643.99 | 2026-06-04 | Deere — Q2 beat, FY26 guide raised, ag/onshoring tailwind. On a 10% trailing stop already (no conversion needed). **PRINT RISK into Q3 Thu Aug 20 9:00 CT** (AGCO missed −11% on 8/6; DE announced ~238 layoffs; Evercore trimmed PT 641→632 but MAINTAINED). Do NOT add ahead. **Cushion ~5.95%** (tightest name; dipped intraday). |
| LLY | 12 | 1209.84 | 1232.20 | +268.32 | +1.85% | **−7% HARD STOP (GTC) @ 1125.15** | 2026-08-12 | Eli Lilly — Q2 beat-and-raise (rev $22.974B, adj EPS $8.38, RAISED FY26 EPS $35.50–36.50) + GLP-1/obesity secular tailwind. Day 2, +1.85%. Conviction ~73 (B+). Hard stop converts to 10% trailing once +5% (~$1,270.33). Next earnings ~Nov. |
| SPY | 32 | 772.921250 | 775.70 | +88.92 | +0.36% | **NONE — index-floor sleeve, deliberate no-stop carve-out** | 2026-08-10 (t1) / 2026-08-11 (t2) | S&P 500 market floor (Lauren-approved Option B), COMPLETE. Idle cash parked in the index so it MATCHES the benchmark. Own sleeve, EXEMPT from ≤20%/max-5/max-3-per-week caps; NO −7%/trailing stop. Buy-and-hold-the-market. |

**Conviction sleeve: 3 of 5 (two slots OPEN).** **Conviction buys used this week: 1 of 3** (the SPY floor does NOT consume this budget). **Cash buffer: ~35.86%.** Position sizes (on equity $102,173.09): JPM ~12.10%, DE ~13.27%, LLY ~14.47%, SPY ~24.29% (index sleeve — exempt from the 20% single-position cap by policy).

## Closed THIS WEEK
- **None** (week began Mon 8/10). Last close: LLY trailing-stop exit 7/31 (+$627.34 / +4.15%) — RE-ENTERED 8/12 on the fresh verified beat-and-raise catalyst.

## Stop-management state (re-confirmed RESTING via open-orders, nested=true — open 8/13)
- **JPM 10% trailing** `8a937ff6-164c-4384-8cf8-c000d4106a60` — hwm **366.5**, floor (stop_price) **329.85**, status new (resting). Mark 363.71, cushion ~9.31%. hwm ratcheted up on a fresh high (was 366.06/329.454). qty 34.
- **DE 10% trailing** `dcdd84e5-6b94-4943-aa5b-3d3a299cbfce` — hwm **643.99**, floor (stop_price) **579.591**, status new (resting). Mark 616.27, cushion ~5.95%. Below hwm → no ratchet. qty 22.
- **LLY −7% hard stop** `f50e3c39-0719-497e-8ccc-6006e6afa290` — stop_price **1125.15** (=1209.84×0.93), GTC, status new (resting). Mark 1232.20 (+1.85%). **Converts to a 10% trailing stop once LLY is +5% in profit** (trigger ~$1,270.33). qty 12.
- **SPY — NO STOP by design** (index-floor sleeve carve-out). qty_available 32 (unencumbered). Intentional per the 8/7 policy; do NOT place a stop on the floor.

## Risk checks (open)
- **(a) Any position −7% or worse un-stopped?** NO. JPM +10.32%, DE +4.48%, LLY +1.85%, SPY +0.36%. **→ No sell, no news check triggered.**
- **(b) Any position +5%+ needing hard→trailing conversion?** NO conversion pending. JPM ≥+5% but already on 10% trailing GTC; DE +4.48% already on 10% trailing GTC; LLY +1.85% (below +5%) on its −7% hard stop as designed; SPY carries no stop by policy. **(Standing task: convert LLY's hard stop → 10% trailing once it tags ~+5% / ~$1,270.33.)**
- **(c) Daily loss cap:** today +0.115% (up) → not tripped.

## Watch / next (next routine: **midday Thu 8/13**)
- **LLY — day 2, +1.85%.** Watch it holds above the 50dMA (~$1,165); −7% hard stop at 1125.15 is the safety net. Standing task: convert to 10% trailing at +5% (~$1,270.33 — another ~+3.1% away).
- **DE — cushion ~5.95%** (tightest, dipped intraday). **Q3 Aug 20 is the dominant event** — AGCO miss + DE layoffs raise gap-through-cushion odds on a Q3 miss. Pre-commit hold-through-print vs tighten/exit by early next week. Do NOT add ahead.
- **JPM — cushion ~9.31%**, healthy; fresh high ratcheted the floor up; thesis intact; next earnings ~Oct.
- **SPY floor COMPLETE** (cash ~36%). Rebalance rule fires only if a new ≥70 conviction buy would push cash below the 10–20% buffer (trim floor first). Two conviction slots remain, cash ~36% — room for ~1 more conviction buy before the floor would need trimming.
- **Conviction gate:** empty this scan. AMGN (~70) ran EXTENDED (+13.5% vs 50dMA) → bench-for-a-pullback, not a buy. Bench (all UNVERIFIED this run, carry stale): DDOG ~70, ABT ~69, NET ~68, TDG ~65, ETN ~64 (chase, high-beta ≤10% cap), NOC ~60.

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
