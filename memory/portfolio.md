# Portfolio

**Last updated:** 2026-08-12 15:00 CT — **MARKET CLOSE (Wed).** Market CONFIRMED CLOSED via /v2/clock (is_open:false, 16:01 ET, next_open 8/13 09:30 ET). Account: equity **$102,075.14**, cash **$36,641.96** (~35.90%), long_market_value **$65,433.18** (~64.10%), buying_power $329,780.74, status ACTIVE. `last_equity` (Tue 8/11 close) $101,722.22 → **today +$352.92 / +0.347%**. **NO TRADES THIS ROUTINE** (the day's only trade was the LLY buy at the open). All three stops re-confirmed RESTING (JPM trailing hwm ratcheted to 366.06 on a fresh high). No position at/through a risk trigger; no hard→trailing conversion pending. Conviction sleeve **3 of 5 stocks (two slots OPEN); weekly conviction buys 1/3** (SPY floor exempt). **Inbox: nothing pending.**

## Scorecard (CLOSE 2026-08-12)
- **Equity $102,075.14.** Total since $100K start: **+2.08%.**
- **Today +$352.92 / +0.347%** vs Tue 8/11 close $101,722.22.
- **SPY today (official, Alpaca daily bars):** 8/11 close 770.56 → 8/12 close **772.47** = **+0.25%**. **Alpha today +0.10 pt** (book +0.35% vs SPY +0.25%).
- **Week-to-date (from Fri 8/7 close $101,707.48):** **+$367.66 / +0.36%.** SPY WTD: 8/7 close 773.26 → 772.47 = **−0.10%**. **WTD alpha +0.46 pt** — ahead of the market for the week.
- **Net open unrealized: +$1,995.93** (JPM +1,206.47, DE +658.90, LLY +128.04, SPY +2.52).
- **Cash 35.90%** — well above the 10–20% minimum buffer.

## Open positions (3 conviction stocks + 1 index-floor sleeve) — CLOSE marks 8/12

| Symbol | Shares | Avg Cost | Mark | P/L $ | P/L % | Stop | Entry Date | Thesis (1 line) |
|---|---|---|---|---|---|---|---|---|
| JPM | 34 | 329.695588 | 365.18 | +1,206.47 | +10.76% | **10% TRAILING (GTC)**, floor **329.454**, hwm 366.06 | 2026-06-29 | JPMorgan — $50B buyback + div hike; largest US bank; Q2 beat; DB Buy PT $375. Made a **fresh high** today (hwm 365.84→366.06, floor→329.454). Thesis intact; next earnings ~Oct. **Cushion ~9.78%.** |
| DE | 22 | 589.82 | 619.77 | +658.90 | +5.08% | **10% TRAILING (GTC)**, floor **579.591**, hwm 643.99 | 2026-06-04 | Deere — Q2 beat, FY26 guide raised, ag/onshoring tailwind. On a 10% trailing stop already (no conversion needed). **PRINT RISK into Q3 Thu Aug 20 9:00 CT** (AGCO missed −11% on 8/6; DE announced ~238 layoffs; Evercore trimmed PT 641→632 but MAINTAINED). Do NOT add ahead. **Cushion ~6.48%** (tightest name). |
| LLY | 12 | 1209.84 | 1220.51 | +128.04 | +0.88% | **−7% HARD STOP (GTC) @ 1125.15** | 2026-08-12 | Eli Lilly — Q2 beat-and-raise (rev $22.974B, adj EPS $8.38, RAISED FY26 EPS $35.50–36.50) + GLP-1/obesity secular tailwind. Fresh entry today, closed green. Conviction ~73 (B+). Hard stop converts to 10% trailing once +5% (~$1,270.33). Next earnings ~Nov. |
| SPY | 32 | 772.921200 | 773.00 | +2.52 | +0.01% | **NONE — index-floor sleeve, deliberate no-stop carve-out** | 2026-08-10 (t1) / 2026-08-11 (t2) | S&P 500 market floor (Lauren-approved Option B), COMPLETE. Idle cash parked in the index so it MATCHES the benchmark. Own sleeve, EXEMPT from ≤20%/max-5/max-3-per-week caps; NO −7%/trailing stop. Buy-and-hold-the-market. |

**Conviction sleeve: 3 of 5 (two slots OPEN).** **Conviction buys used this week: 1 of 3** (the SPY floor does NOT consume this budget). **Cash buffer: ~35.90%.** Position sizes (on equity $102,075.14): JPM ~12.16%, DE ~13.36%, LLY ~14.35%, SPY ~24.23% (index sleeve — exempt from the 20% single-position cap by policy).

## Closed THIS WEEK
- **None** (week began Mon 8/10). Last close: LLY trailing-stop exit 7/31 (+$627.34 / +4.15%) — RE-ENTERED 8/12 on the fresh verified beat-and-raise catalyst.

## Stop-management state (re-confirmed RESTING via open-orders, nested=true — close 8/12)
- **JPM 10% trailing** `8a937ff6-164c-4384-8cf8-c000d4106a60` — hwm **366.06**, floor (stop_price) **329.454**, status new (resting). Mark 365.18, cushion ~9.78%. hwm ratcheted up on a fresh intraday high. qty 34.
- **DE 10% trailing** `dcdd84e5-6b94-4943-aa5b-3d3a299cbfce` — hwm **643.99**, floor (stop_price) **579.591**, status new (resting). Mark 619.77, cushion ~6.48%. Below hwm → no ratchet. qty 22.
- **LLY −7% hard stop** `f50e3c39-0719-497e-8ccc-6006e6afa290` — stop_price **1125.15** (=1209.84×0.93), GTC, status new (resting). Mark 1220.51 (+0.88%). **Converts to a 10% trailing stop once LLY is +5% in profit** (trigger ~$1,270.33). qty 12.
- **SPY — NO STOP by design** (index-floor sleeve carve-out). qty_available 32 (unencumbered). Intentional per the 8/7 policy; do NOT place a stop on the floor.

## Risk checks (close)
- **(a) Any position −7% or worse un-stopped?** NO. JPM +10.76%, DE +5.08%, LLY +0.88%, SPY +0.01%. **→ No sell, no news check triggered.**
- **(b) Any position +5%+ needing hard→trailing conversion?** NO conversion pending. JPM ≥+5% but already on 10% trailing GTC; DE +5.08% but already on 10% trailing GTC; LLY +0.88% (below +5%) on its −7% hard stop as designed; SPY carries no stop by policy. **(Standing task: convert LLY's hard stop → 10% trailing once it tags ~+5% / ~$1,270.33.)**
- **(c) Daily loss cap:** today +0.347% (up) → not tripped.

## Watch / next (next routine: **pre-market Thu 8/13**)
- **LLY — fresh position, closed +0.88%.** Watch it holds above the 50dMA (~$1,160); −7% hard stop at 1125.15 is the safety net. Standing task: convert to 10% trailing at +5% (~$1,270.33).
- **DE — cushion ~6.48%** (tightest). **Q3 Aug 20 is the dominant event** — AGCO miss + DE layoffs raise gap-through-cushion odds on a Q3 miss. Pre-commit hold-through-print vs tighten/exit by early next week. Do NOT add ahead.
- **JPM — cushion ~9.78%**, healthy; fresh high ratcheted the floor up; thesis intact; next earnings ~Oct.
- **SPY floor COMPLETE** (cash ~36%). Rebalance rule fires only if a new ≥70 conviction buy would push cash below the 10–20% buffer (trim floor first). Two conviction slots remain, cash ~36% — room for ~1 more conviction buy before the floor would need trimming.
- **Conviction gate:** AMGN ~71 is the pre-market runner-up (backup). Bench: TDG ~65, ETN ~64 (chase, high-beta ≤10% cap), NOC ~60 (below 50dMA).

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
