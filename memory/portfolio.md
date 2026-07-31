# Portfolio

**Last updated:** 2026-07-31 08:35 CT (09:33 ET) — **MARKET-OPEN (Fri, WEEKLY-REVIEW day; market CONFIRMED OPEN via /v2/clock, next_close 16:00 ET).** Live open marks from Alpaca. Account: equity **$101,339.04**, cash **$60,167.78** (~59.37%), long_market_value **$41,171.26** (~40.63%), buying_power $355,950.65, status ACTIVE. Day P/L vs `last_equity` $101,454.60 = **−$115.56 / −0.11%** = flat noise, nowhere near the −3% daily loss cap. Book **3 of 5 positions (two slots OPEN)**. **ACTIONS THIS RUN: NONE** — executed the pre-market plan as written; no buys (~38th straight empty scan on the 2-signal + Conviction≥70 gate), no sells, no stop conversions, 0 fills. All 3 stops re-confirmed RESTING (10% trailing GTC). **Inbox: nothing pending.**

## Scorecard (MARKET-OPEN 2026-07-31 — live open marks; the CLOSE owns today's official number)
- **Open equity $101,339.04.** Total since $100K start: **+1.34%.**
- **Day P/L ≈ flat** (−$115.56 / −0.11%) vs `last_equity` $101,454.60 — early-session noise; the close owns today's official number.
- **WTD (base Fri 7/24 close eq $102,740.86 / SPY 738.90):** port **≈ −1.36%** so far; official WTD + alpha land at **today's weekly review** (Fri close).
- **Net open unrealized: +$1,887.13** (LLY +945.70, JPM +752.23, DE +189.20 — live open marks).
- **SPY refs:** 741.63 (7/30 close), 729.57 (7/29 close); new-week base 738.90 (7/24 close). Today's SPY prints at the close.

## Open positions (3 of 5 — two slots OPEN) — LIVE OPEN marks 7/31

| Symbol | Shares | Avg Cost | Mark (open) | P/L $ | P/L % | Stop | Entry Date | Thesis (1 line) |
|---|---|---|---|---|---|---|---|---|
| LLY | 14 | 1078.46 | 1146.01 | +945.70 | +6.26% | **10% TRAILING (GTC)**, floor **1124.505**, hwm 1249.45 | 2026-06-01 | Eli Lilly — Q1 beat + raised guide + oral GLP-1 (orforglipron) pipeline; retatrutide Ph3. **Earnings ~Aug 5** (entering 3-day earnings window soon — do NOT add ahead of print). sev 3, quiet/intact. **Cushion ~1.88% (now tightest — mark eased from pre-mkt 1160.99).** |
| JPM | 34 | 329.695588 | 351.82 | +752.23 | +6.71% | **10% TRAILING (GTC)**, floor **323.307**, hwm 359.23 | 2026-06-29 | JPMorgan — $50B buyback + div hike; largest US bank; Q2 (7/14) beat; DB UPGRADE Hold→Buy PT $375. sev 2 (7/29 −3.25% macro slide, sector-wide not company). **Cushion ~8.10% (widest).** Next earnings ~Oct. |
| DE | 22 | 589.82 | 598.42 | +189.20 | +1.46% | **10% TRAILING (GTC)**, floor **579.591**, hwm 643.99 | 2026-06-04 | Deere — Q2 beat, FY26 guide raised, right-to-repair settlement cleared (PR this week REAFFIRMS it — implementation, not new litigation). $1.62 div payable Aug 10. Off-cycle; next report ~Aug 20. sev 2 (ag-commodity softness = sentiment, net-income outlook MAINTAINED). **Cushion ~3.15%.** |

**Open positions: 3 of 5 (two slots OPEN).** **Buys used this week: 0 of 3.** **Cash buffer: ~59.37%.** Position sizes (on open equity $101,339.04): LLY 15.83%, DE 12.99%, JPM 11.80% — all under the 20% cap.

## Stop-management state (all 3 re-confirmed RESTING via open-orders query, nested=true) — ALL 10% TRAILING GTC, floors/hwm unchanged from 7/30 close (no new highs at the open → no ratchet)
- **LLY 10% trailing** `6016a7e7-faac-4e93-82e7-851abf30eca8` — floor **1124.505**, hwm 1249.45. Open 1146.01, cushion ~1.88% (now tightest).
- **JPM 10% trailing** `8a937ff6-164c-4384-8cf8-c000d4106a60` — floor **323.307**, hwm 359.23. Open 351.82, cushion ~8.10% (widest).
- **DE 10% trailing** `dcdd84e5-6b94-4943-aa5b-3d3a299cbfce` — floor **579.591**, hwm 643.99. Open 598.42, cushion ~3.15%. All shares show qty_available:0 → reserved by their resting stops.

## +5% conversion check (market-open)
- LLY +6.26% and JPM +6.71% both ≥+5% but ALREADY on 10% trailing stops → **trailing stops are never reverted to hard stops.** DE +1.46% below +5% but also already trailing. **Zero hard stops remain → no −7%→trailing conversion needed.** No action.

## Watch / next (next routine: **Fri 7/31 midday**, then **weekly review** — owns the cash-drag/gate decision)
- **LLY — cushion tightened to ~1.88%** (mark eased from pre-mkt 1160.99 to 1146.01), now the tightest in the book. No thesis break — quiet name, no dated news. Floor 1124.505 sits above the +5% conversion line, so a trailing exit would still lock a gain, not a loss. **Earnings ~Aug 5** next week: entering the 3-trading-day earnings window soon; do NOT add ahead of the print — the existing position rides its trailing stop.
- **DE — cushion ~3.15%**, floor 579.591 sits ~1.7% BELOW the 589.82 entry (a continued slide exits near break-even). No thesis break (right-to-repair PR = reaffirmation of the already-settled order; ag-commodity softness = sentiment). Trailing floor handles any real break automatically; do NOT pre-empt on price.
- **No buy candidate cleared the gate (~38th straight empty scan).** Two verified defense beat-and-raises on the bench but both fail on entry: **LMT ~62** (extended, +11–12%/week chase — wants a pullback to low-$540s) and **NOC ~55** (beat but FELL, near 52-wk lows — fails the uptrend/no-knife-catch signal; wants a base + 50dMA reclaim).
- **Cash-drag re-eval (ARMED — this IS the pre-committed test week):** DECISION at **today's weekly review** (owned by that routine, NOT market-open/midday). Status genuinely MIXED this week: SPY fell −1.52% on 7/29 (our cash BEAT the market, +0.33 alpha) then rose +1.65% on 7/30 (cash LAGGED, −2.41 alpha) — so the "while SPY keeps rising" half fired only on 7/30, not all week. Carry the two-sided tape into the review. The gate is functioning (it correctly held a chase-entry LMT and a fell-on-print NOC); the open question is deployment/sizing (is 59% cash too high for a grinding-up market), NOT lowering the ≥70 bar. Weekly buy cap still 0/3; resets Monday.
- **Bench (from this pre-market):** UNH ~64, NOW 63, GS 63, LMT ~62, DLR 60, DOV 58, JNJ 58, ETN 56 (reports 7/31 BMO — re-check post-print), NOC ~55, ABT 55, OXY 55, STX 53, MS 52, AXP/V ~50, AMGN/CB/CVS/VST 50, PANW 35. None clears ≥70.

## Recent closes (last 5)

| Symbol | Exit Date | Shares | Entry | Exit | P/L $ | P/L % | Reason |
|---|---|---|---|---|---|---|---|
| GE | 2026-07-16 | 45 | 329.63 | 344.54 | +670.95 | +4.52% | 10% trailing stop fired (post-Q2-earnings give-back caught the profit; no verified thesis break) |
| ETN | 2026-07-02 | 24 | 401.5425 | 392.75 | −211.02 | −2.19% | 10% trailing stop fired (beta/thin pre-holiday tape, not thesis break) |
| NVDA | 2026-06-05 | 55 | 220.15 | 204.7158 | −848.88 | −7.01% | −7% hard stop fired (macro/NFP semis selloff, not thesis break) |
| NVDA | 2026-05-04 | 25 | 201.38 | ~195.02 | −159.04 | −3.16% | 10% trailing stop fired (round-trip) |

---
*Overwrite this file every routine. Keep it a live snapshot, not a log.*
