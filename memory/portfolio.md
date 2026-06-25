# Portfolio

**Last updated:** 2026-06-25 08:36 CT (09:36 ET) — **MARKET-OPEN routine.** Market **OPEN** (clock `is_open:true`, next_close 2026-06-25 16:00 ET). **NO trades this routine** — pre-market defensive plan held: nothing cleared 2 signals + Conviction ≥70 (PANW 66 / JPM 65 both below the gate), all 4 positions green, no stop triggers, DE not at its +5% conversion trigger. Constructive open after core PCE (8:30 ET): SPY +~0.44% and all four names higher — the feared hawkish shock did NOT show up in the tape. **ETN bounced hard (+3.65% on the day to 419.37)** — MU's overnight blowout beat-and-raise gave the AI-memory/data-center complex a lift, supportive read-through for ETN's AI-power thesis. **Intraday equity $102,342.19, day P/L +$862.11 / +0.85% vs SPY +~0.44% → day alpha +0.41 pts, AHEAD** (intraday snapshot; official scorecard at close). All 4 GTC stops re-verified RESTING `status:new`; daytrade_count 0. **DE did NOT reach its +5% conversion trigger** (mark 609.185 vs ~619.31, ~1.66% away) → DE stays on the −7% hard stop; convert the moment it tags ~619.31.

**Cash:** $46,447.18 (unchanged — no trades).
**Equity (intraday):** **$102,342.19** (cash $46,447.18 + long_market_value $55,895.01). last_equity **$101,480.08** = Alpaca's 6/24 official close (6/24 base).
**Day:** P/L **+$862.11 / +0.85%** | SPY **+~0.44%** (737.70 latest-trade vs 734.50 6/24 close) → **day alpha +0.41 pts, AHEAD** (intraday).
**Week-to-date** (base 6/18 close $101,006.72 / SPY 746.75): portfolio **+1.32%** vs SPY **−1.21%** → **week alpha +2.53 pts, AHEAD** (day 4 of 4 this week; intraday).
**Buys used this week:** **0 of 3** (same week as 6/22). **NO trades this routine.** Nothing cleared 2 signals + Conviction ≥70.

## Open positions (4 of 5) — intraday marks (6/25 ~09:36 ET)

| Symbol | Shares | Avg Cost | Mark (6/25) | P/L $ | P/L % | Stop | Cushion | Entry Date | Thesis (1 line) |
|---|---|---|---|---|---|---|---|---|---|
| GE | 45 | 329.63 | 371.615 | +1,889.33 | +12.74% | **10% TRAILING (GTC)**, floor 335.178, hwm 372.42 | ~9.8% | 2026-06-08 | GE Aerospace — record commercial-aircraft demand + high-margin engine aftermarket + defense; pure industrial, ZERO AI overlap, lower beta. Book's anchor; ratcheted to a fresh hwm 372.42 today. Earnings ~Jul 16 (no blackout). Thesis intact. |
| LLY | 14 | 1078.46 | 1121.81 | +606.95 | +4.02% | **10% TRAILING (GTC)**, floor 1064.457, hwm 1182.73 | ~5.1% | 2026-06-01 | Eli Lilly — Q1 beat + raised guide + oral GLP-1 (orforglipron/Foundayo, FDA-approved Apr 1). Most rate-sensitive (long-duration growth); held up fine through PCE. **CAVEAT:** $50/mo Medicare + July 1 Part D date remain UNVERIFIED (documented $25/mo insured / $149 cash). Floor ~5.1% below. |
| DE | 22 | 589.82 | 609.185 | +426.03 | +3.28% | 548.53 (−7%, **GTC**) | ~10.0% | 2026-06-04 | Deere — Q2 beat (5/21); ag-equipment/onshoring tailwind; NON-AI diversifier (ballast alongside GE on a tech-down tape). Lone name still on a −7% hard stop; **+5% conversion trigger ~619.31 — mark 609.185 is ~$10.13 / ~1.66% away.** HOLD; convert to a 10% trailing GTC the moment it tags ~619.31. |
| ETN | 24 | 401.5425 | 419.37 | +427.86 | +4.44% | **10% TRAILING (GTC)**, floor 393.066, hwm 436.74 | ~6.3% | 2026-06-08 | Eaton — electrical "picks-and-shovels" for AI data-center power + electrification (orders +55%/rev +50%). Bounced **+3.65% today** to 419.37 on MU's blowout beat-and-raise (bullish AI-memory/data-center read). 6/23's −7.06% was VERIFIED sector/macro, NOT company-specific; thesis intact. Highest-beta name; still below its 436.74 hwm so the trailing floor stays 393.066. Earnings ~late July. |

**Open positions: 4 of 5.** **Buys used this week: 0 of 3** (1 free slot). **Cash buffer: ~45.4%** (~54.6% invested, $55,895.01 market value). Net open unrealized **+$3,350.17** (GE +1,889.33, LLY +606.95, ETN +427.86, DE +426.03).

## Stop-management state (all 4 confirmed RESTING as GTC, status `new` — re-verified this routine via open-orders query)

- **GE 10% trailing** `b9dadf2d-b6f5-49e7-8cc9-b3eb8b07aa6c` — floor **335.178**, hwm **372.42** (ratcheted up today). ~9.8% below the 371.615 mark.
- **LLY 10% trailing** `6016a7e7-faac-4e93-82e7-851abf30eca8` — floor **1064.457**, hwm **1182.73**. ~5.1% below the 1121.81 mark.
- **ETN 10% trailing** `cc843666-7e63-462a-82d4-57cc3e826ead` — floor **393.066**, hwm **436.74**. ~6.3% below the 419.37 mark; still below the 436.74 hwm so floor unchanged. Trailing never reverts to a hard stop — no action.
- **DE −7% hard** `a150583a-a58c-42c9-8d12-9d7ece773841` @ **548.53** (~10.0% cushion). The only name still on a hard stop; +5% trailing-conversion trigger ~619.31, ~1.66% above the mark.
- (a) **−7% drawdown check (net from entry):** worst is DE +3.28% — all four green net, none near −7%. HOLD. No sells.
- (b) **+5% → trailing:** GE, ETN, LLY all converted. DE +3.28%, ~1.66% below its +5% (~619.31) — did NOT tag it this routine. Nothing converted.
- (c) **Daily loss cap:** portfolio **UP +0.85%** intraday — nowhere near the −3% no-buy trigger. Clean.
- daytrade_count 0. No trades this routine. Stops all resting.

## Watch / next (next routine: midday 2026-06-25)

- **No new buys** — nothing clears 2 signals + Conviction ≥70. PANW (66, lead — STILL no fresh <2wk upgrade/insider buy; catalyst ~23d stale) and JPM (65, clean uptrend, next catalyst earnings Jul 14) both below the gate. 5th slot stays open. **AVGO (58, high-beta semis, overlaps ETN) explicitly OFF the table.**
- **DE conversion watch (#1 near-term action):** mark 609.185 is ~$10.13 / ~1.66% below the +5% trigger (~619.31). When DE tags ~619.31, cancel the −7% hard stop `a150583a` and place a 10% trailing GTC stop (cancel-then-place sequence in scripts/alpaca.md). Most likely near-term action — check at midday.
- **ETN watch (#2):** strong +3.65% bounce today on MU's blowout. Still highest-beta, but cushion widened to ~6.3% (floor 393.066). Trailing stop handles it automatically; no manual action. Earnings ~late July.
- **This week's calendar:** **core PCE Thu 6/25 8:30 ET** released pre-open — tape opened constructive (SPY +~0.44%), feared hawkish shock did not materialize in price; re-confirm the actual print and any Fed-pricing reaction at midday before treating the idle 5th slot as "deploy-clear." **MU 6/24 AMC blowout (VERIFIED)** lifting AI-memory complex. Blackout soft-clear for all our names this week (verify at IR before any buy).
- **Macro:** risk-off backdrop (hawkish Fed under Chair Warsh, DXY 1-yr high, 6/23 semis rout) had been the worry, but the book closed up 6/24 and opened green 6/25 on a constructive PCE reaction. GE/DE/LLY ballast + ETN on a trailing stop + ~45% cash remains the right posture. Still waiting for a genuine ≥70 setup on a constructive base before deploying the 5th slot.

## Recent closes (last 5)

| Symbol | Exit Date | Shares | Entry | Exit | P/L $ | P/L % | Reason |
|---|---|---|---|---|---|---|---|
| NVDA | 2026-06-05 | 55 | 220.15 | 204.7158 | −848.88 | −7.01% | −7% hard stop fired (macro/NFP semis selloff, not thesis break) |
| NVDA | 2026-05-04 | 25 | 201.38 | ~195.02 | −159.04 | −3.16% | 10% trailing stop fired (round-trip) |

---
*Overwrite this file every routine. Keep it a live snapshot, not a log.*
