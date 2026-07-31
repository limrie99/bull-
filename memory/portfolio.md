# Portfolio

**Last updated:** 2026-07-31 12:00 CT (13:03 ET) — **MIDDAY (Fri, WEEKLY-REVIEW day; market CONFIRMED OPEN via /v2/clock, next_close 16:00 ET).** Live midday marks from Alpaca. Account: equity **$101,030.27**, cash **$75,893.56** (~75.12%), long_market_value **$25,136.71** (~24.88%), buying_power $373,957.03, status ACTIVE. Day P/L vs `last_equity` $101,454.60 = **−$424.33 / −0.42%** = mild give-back, nowhere near the −3% daily loss cap. Book **2 of 5 positions (three slots OPEN).** **ACTION THIS RUN: LLY 10% trailing stop AUTO-FIRED at 10:08 ET — sold 14 @ 1123.27, realized +$627.34 / +4.15% (a WIN).** No discretionary trades, no new buys (nothing clears the gate; midday has no breaking catalyst), no manual stop changes. Remaining 2 stops re-confirmed RESTING (10% trailing GTC). **Inbox: nothing pending.**

## Scorecard (MIDDAY 2026-07-31 — live marks; the CLOSE owns today's official number)
- **Midday equity $101,030.27.** Total since $100K start: **+1.03%.**
- **Day P/L −$424.33 / −0.42%** vs `last_equity` $101,454.60 — mild give-back (most of it is LLY easing from ~1146 to its 1123.27 stop before it sold); the close owns the official number.
- **WTD (base Fri 7/24 close eq $102,740.86 / SPY 738.90):** port **≈ −1.66%** so far; SPY 745.15 now ≈ **+0.85% WTD** → we're lagging WTD. Official WTD + alpha land at **today's weekly review** (Fri close).
- **Realized this run: +$627.34** (LLY trailing-stop exit). **Net open unrealized: +$951.02** (JPM +807.14, DE +143.88 — live midday marks).
- **SPY refs:** 745.15 (midday 7/31, ≈ +0.47% vs 7/30 close 741.63), 741.63 (7/30 close); new-week base 738.90 (7/24 close). Today's SPY closes at 16:00 ET.

## Open positions (2 of 5 — three slots OPEN) — LIVE MIDDAY marks 7/31

| Symbol | Shares | Avg Cost | Mark (midday) | P/L $ | P/L % | Stop | Entry Date | Thesis (1 line) |
|---|---|---|---|---|---|---|---|---|
| JPM | 34 | 329.695588 | 353.44 | +807.14 | +7.20% | **10% TRAILING (GTC)**, floor **323.307**, hwm 359.23 | 2026-06-29 | JPMorgan — $50B buyback + div hike; largest US bank; Q2 (7/14) beat; DB UPGRADE Hold→Buy PT $375. sev 2 (macro sector noise, not company). **Cushion ~8.53% (widest).** Next earnings ~Oct. |
| DE | 22 | 589.82 | 596.36 | +143.88 | +1.11% | **10% TRAILING (GTC)**, floor **579.591**, hwm 643.99 | 2026-06-04 | Deere — Q2 beat, FY26 guide raised, right-to-repair settlement cleared (reaffirmed, implementation not new litigation). $1.62 div payable Aug 10. Off-cycle; next report ~Aug 20. sev 2 (ag-commodity softness = sentiment, net-income outlook MAINTAINED). **Cushion ~2.81% (tightest).** |

**Open positions: 2 of 5 (three slots OPEN).** **Buys used this week: 0 of 3.** **Cash buffer: ~75.12%.** Position sizes (on midday equity $101,030.27): DE 12.99%, JPM 11.89% — both well under the 20% cap.

## Closed THIS RUN
- **LLY — 10% trailing stop AUTO-FIRED, sold 14 @ 1123.27 (order 6016a7e7), 10:08 ET.** Realized **+$627.34 / +4.15%** (entry 1078.46, 2026-06-01). LLY ran to hwm 1249.45, pulled back 10% to the floor 1124.505, stop executed 1123.27. LLY bounced to ~1143 within hours → **normal give-back, NOT a thesis break.** Bonus: exit removed LLY's ~Aug 5 earnings risk with a locked gain. Freed ~$15,726 cash.

## Stop-management state (both remaining re-confirmed RESTING via open-orders query, nested=true) — ALL 10% TRAILING GTC, floors/hwm unchanged (no new highs → no ratchet)
- **JPM 10% trailing** `8a937ff6-164c-4384-8cf8-c000d4106a60` — floor **323.307**, hwm 359.23. Midday 353.44, cushion ~8.53% (widest).
- **DE 10% trailing** `dcdd84e5-6b94-4943-aa5b-3d3a299cbfce` — floor **579.591**, hwm 643.99. Midday 596.36, cushion ~2.81% (tightest). All shares show qty_available:0 → reserved by their resting stops.
- **LLY stop `6016a7e7`** — FILLED/closed this run (see above); no longer resting.

## Risk checks (midday)
- **(a) Any position −7% or worse un-stopped?** NO. JPM +7.20%, DE +1.11%. Nothing near a hard-stop trigger; both on trailing stops well above their floors.
- **(b) Any position +5%+ needing hard→trailing conversion?** JPM +7.20% ≥ +5% but ALREADY on a 10% trailing stop → trailing stops are never reverted. DE +1.11% below +5% and also already trailing. **Zero hard stops in book → no conversion needed anywhere.**
- **(c) Daily loss cap:** day P/L −0.42% vs yesterday's close — well within the −3% cap. (Moot for new buys anyway — nothing clears the gate and midday has no breaking catalyst.)

## Watch / next (next routine: **weekly review** — owns the cash-drag/gate/deployment decision)
- **Cash-drag re-eval (ARMED — this IS the pre-committed test week), NOW SHARPER:** the LLY exit lifts us to **~75% cash with only 2 positions and three open slots.** DECISION at **today's weekly review** (owned by that routine). This run's exit is a clean WIN (+$627, gain protected, earnings risk removed), but it mechanically raises the cash level right as we're deciding whether ~59%→now-75% cash is too much dry powder for a market grinding up. The gate is functioning (correctly held chase-entry LMT and fell-on-print NOC); the open question is deployment/sizing, NOT lowering the ≥70 bar. Weekly buy cap still 0/3; resets Monday.
- **DE — cushion ~2.81% (tightest remaining)**, floor 579.591 sits ~1.7% BELOW the 589.82 entry (a continued slide exits near break-even). No thesis break (right-to-repair PR = reaffirmation of the already-settled order; ag-commodity softness = sentiment). Trailing floor handles any real break automatically; do NOT pre-empt on price.
- **JPM — cushion ~8.53% (widest)**, healthy and quiet; thesis intact (record Q2, $50B buyback, DB Buy PT $375). Next earnings ~Oct.
- **No buy candidate cleared the gate (~38th straight empty scan, per pre-market).** Two verified defense beat-and-raises on the bench but both fail on entry: **LMT ~62** (extended, +11–12%/week chase — wants a pullback to low-$540s) and **NOC ~55** (beat but FELL, near 52-wk lows — fails the uptrend/no-knife-catch signal; wants a base + 50dMA reclaim). ETN reported 7/31 BMO — re-check post-print at weekly review.
- **Bench (from pre-market):** UNH ~64, NOW 63, GS 63, LMT ~62, DLR 60, DOV 58, JNJ 58, ETN 56, NOC ~55, ABT 55, OXY 55, STX 53, MS 52, AXP/V ~50, AMGN/CB/CVS/VST 50, PANW 35. None clears ≥70.

## Recent closes (last 5)

| Symbol | Exit Date | Shares | Entry | Exit | P/L $ | P/L % | Reason |
|---|---|---|---|---|---|---|---|
| LLY | 2026-07-31 | 14 | 1078.46 | 1123.27 | +627.34 | +4.15% | 10% trailing stop fired (give-back from ~1249 hwm; no thesis break — bounced to ~1143 same day; also removed Aug 5 earnings risk) |
| GE | 2026-07-16 | 45 | 329.63 | 344.54 | +670.95 | +4.52% | 10% trailing stop fired (post-Q2-earnings give-back caught the profit; no verified thesis break) |
| ETN | 2026-07-02 | 24 | 401.5425 | 392.75 | −211.02 | −2.19% | 10% trailing stop fired (beta/thin pre-holiday tape, not thesis break) |
| NVDA | 2026-06-05 | 55 | 220.15 | 204.7158 | −848.88 | −7.01% | −7% hard stop fired (macro/NFP semis selloff, not thesis break) |
| NVDA | 2026-05-04 | 25 | 201.38 | ~195.02 | −159.04 | −3.16% | 10% trailing stop fired (round-trip) |

---
*Overwrite this file every routine. Keep it a live snapshot, not a log.*
