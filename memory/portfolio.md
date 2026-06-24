# Portfolio

**Last updated:** 2026-06-24 15:00 CT (16:00 ET) — **MARKET-CLOSE routine (OFFICIAL day-vs-SPY scorecard).** Market **CLOSED** (clock `is_open:false`, next_open 2026-06-25 09:30 ET). **NO trades today** (Alpaca closed-orders query for 6/24 returned 0 fills) — open/pre-market defensive plan held all day: nothing cleared 2 signals + Conviction ≥70, all 4 positions green, no stop triggers, daily loss cap clean (up day). **Official close: equity $101,683.58, day P/L +$946.73 / +0.94%; SPY +0.12% → day alpha +0.82 pts, AHEAD.** Week-to-date (base 6/18 close $101,006.72 / SPY 746.75) portfolio **+0.67%** vs SPY **−1.64%** → **week alpha +2.31 pts, AHEAD** (day 3 of 4 this week; Fri 6/19 was Juneteenth). All 4 GTC stops re-verified RESTING `status:new` via open-orders query; daytrade_count 0. **DE did NOT reach its +5% conversion trigger** (mark 610.00 vs ~619.31, ~1.5% away) → DE stays on the −7% hard stop; convert the moment it tags ~619.31. ETN pulled back into the close (404.59 vs 407.90 midday) — narrowest cushion (~2.85%) into MU's AMC print tonight; trailing stop handles it automatically.

**Cash:** $46,447.18 (unchanged — no trades).
**Equity (Alpaca official close):** **$101,683.58** (cash $46,447.18 + long_market_value $55,236.40). last_equity **$100,736.85** = Alpaca's 6/23 official close (6/23 base).
**Day:** P/L **+$946.73 / +0.94%** | SPY **+0.12%** (734.50 latest-trade/close vs 733.62 6/23 close; IEX daily bar read 733.32/−0.04% — using the 16:02 ET closing print) | **day alpha +0.82 pts, AHEAD.**
**Week-to-date** (base 6/18 close $101,006.72 / SPY 746.75): portfolio **+0.67%** vs SPY **−1.64%** → **week alpha +2.31 pts, AHEAD.**
**Buys used this week:** **0 of 3** (same week as 6/22). **NO trades today.** Nothing cleared 2 signals + Conviction ≥70.

## Open positions (4 of 5) — official closing marks (6/24 16:00 ET)

| Symbol | Shares | Avg Cost | Close (6/24) | P/L $ | P/L % | Stop | Cushion | Entry Date | Thesis (1 line) |
|---|---|---|---|---|---|---|---|---|---|
| GE | 45 | 329.63 | 365.88 | +1,631.25 | +11.00% | **10% TRAILING (GTC)**, floor 332.325, hwm 369.25 | ~9.2% | 2026-06-08 | GE Aerospace — record commercial-aircraft demand + high-margin engine aftermarket + defense; pure industrial, ZERO AI overlap, lower beta. Book's anchor and best-positioned name on a risk-off/tech-down tape; carried the book today again (+11.00%). Earnings ~Jul 16 (no blackout). Thesis intact. |
| LLY | 14 | 1078.46 | 1117.26 | +543.20 | +3.60% | **10% TRAILING (GTC)**, floor 1064.457, hwm 1182.73 | ~4.7% | 2026-06-01 | Eli Lilly — Q1 beat + raised guide + oral GLP-1 (orforglipron/Foundayo, FDA-approved Apr 1). Most rate-sensitive (long-duration growth) → most exposed to a hawkish/yields-up turn, but no company-specific issue. **CAVEAT:** $50/mo Medicare + July 1 Part D date remain UNVERIFIED (documented $25/mo insured / $149 cash). Floor ~4.7% below. |
| DE | 22 | 589.82 | 610.00 | +443.96 | +3.42% | 548.53 (−7%, **GTC**) | ~10.1% | 2026-06-04 | Deere — Q2 beat (5/21); ag-equipment/onshoring tailwind; NON-AI diversifier (ballast alongside GE on a tech-down tape). Lone name still on a −7% hard stop; **+5% conversion trigger ~619.31 — close 610.00 is ~$9.31 / ~1.5% away** (closed near its midday level). HOLD; convert to a 10% trailing GTC the moment it tags ~619.31. |
| ETN | 24 | 401.5425 | 404.59 | +73.14 | +0.76% | **10% TRAILING (GTC)**, floor 393.066, hwm 436.74 | **~2.85% (narrowest)** | 2026-06-08 | Eaton — electrical "picks-and-shovels" for AI data-center power + electrification (orders +55%/rev +50%). 6/23's −7.06% was VERIFIED sector/macro (SOX −7.9% AI/semis de-rating), NOT company-specific; thesis intact. Highest-beta name on the narrowest trailing cushion. Faded from +1.58% midday to +0.76% into the close. **MU reports AMC tonight** → watch for continued semis vol Thursday; if it slides the trailing stop auto-sells at 393.066 (locks net gain above 401.54 entry), no manual action. Earnings ~late July. |

**Open positions: 4 of 5.** **Buys used this week: 0 of 3** (1 free slot). **Cash buffer: ~45.7%** (~54.3% invested, $55,236.40 market value). Net open unrealized **+$2,691.55** (GE +1,631.25, LLY +543.20, DE +443.96, ETN +73.14).

## Stop-management state (all 4 confirmed RESTING as GTC, status `new` — re-verified this routine via open-orders query)

- **GE 10% trailing** `b9dadf2d-b6f5-49e7-8cc9-b3eb8b07aa6c` — floor **332.325**, hwm **369.25**. ~9.2% below the 365.88 close.
- **LLY 10% trailing** `6016a7e7-faac-4e93-82e7-851abf30eca8` — floor **1064.457**, hwm **1182.73**. ~4.7% below the 1117.26 close.
- **ETN 10% trailing** `cc843666-7e63-462a-82d4-57cc3e826ead` — floor **393.066**, hwm **436.74**. ~2.85% below the 404.59 close (narrowest cushion). Trailing never reverts to a hard stop — no action; if ETN falls to 393.066 it auto-sells, locking a gain above entry.
- **DE −7% hard** `a150583a-a58c-42c9-8d12-9d7ece773841` @ **548.53** (~10.1% cushion). The only name still on a hard stop; +5% trailing-conversion trigger ~619.31, ~1.5% above the close.
- (a) **−7% drawdown check (net from entry):** worst is ETN +0.76% — all four green net, none near −7%. HOLD. No sells.
- (b) **+5% → trailing:** GE, ETN, LLY all converted. DE +3.42%, ~1.5% below its +5% (~619.31) — did NOT tag it today. Nothing converted.
- (c) **Daily loss cap:** portfolio **UP +0.94%** on the day — nowhere near the −3% no-buy trigger. Clean.
- daytrade_count 0. No trades today. Stops all resting.

## Watch / next (next routine: pre-market 2026-06-25)

- **No new buys** — nothing clears 2 signals + Conviction ≥70. PANW (66, lead — STILL no fresh <2wk upgrade/insider buy; catalyst ~22d stale) and JPM (65, clean uptrend, next catalyst earnings Jul 14) both below the gate. 5th slot stays open. **AVGO (58, high-beta semis, overlaps ETN) explicitly OFF the table into the semis rout + MU print.**
- **DE conversion watch (#1 near-term action):** close 610.00 is ~$9.31 / ~1.5% below the +5% trigger (~619.31). When DE tags ~619.31, cancel the −7% hard stop `a150583a` and place a 10% trailing GTC stop (cancel-then-place sequence in scripts/alpaca.md). Most likely near-term action.
- **ETN watch (#2):** narrowest cushion (~2.85%, floor 393.066) into a confirmed AI/semis rout + MU's AMC print tonight (results land after today's close → semis vol Thursday). Thesis intact (6/23 −7% was sector/macro, VERIFIED). If it keeps sliding the trailing stop does its job automatically; no manual action.
- **This week's calendar:** **core PCE Thu 6/25 8:30 ET (VERIFIED)** — week's marquee event and the deploy-or-defer pivot for the idle 5th slot (prior 3.3% YoY, ~3.2% expected, still well above target). **MU 6/24 AMC (VERIFIED)** → read its print + semis reaction pre-market Thursday. **Blackout soft-clear** for all our names this week (verify at IR before any buy).
- **Macro:** risk-off backdrop persists (global tech/semis rout 6/23: SOX −7.9%, KOSPI −10% circuit breaker; hawkish Fed under new Chair Warsh ~2 hikes priced by Dec; DXY 1-yr high) — but the feared follow-through never hit; book closed up +0.94%, two straight days beating SPY on a down-for-the-market tape. GE/DE/LLY ballast cushions the AI-led selloff; ETN carries the de-rating but is on a trailing stop. ~46% cash is a cushion. Waiting for Thu PCE before a fresh rate-sensitive entry remains prudent.

## Recent closes (last 5)

| Symbol | Exit Date | Shares | Entry | Exit | P/L $ | P/L % | Reason |
|---|---|---|---|---|---|---|---|
| NVDA | 2026-06-05 | 55 | 220.15 | 204.7158 | −848.88 | −7.01% | −7% hard stop fired (macro/NFP semis selloff, not thesis break) |
| NVDA | 2026-05-04 | 25 | 201.38 | ~195.02 | −159.04 | −3.16% | 10% trailing stop fired (round-trip) |

---
*Overwrite this file every routine. Keep it a live snapshot, not a log.*
