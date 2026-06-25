# Portfolio

**Last updated:** 2026-06-25 12:05 CT (13:05 ET) — **MIDDAY routine.** Market **OPEN** (clock `is_open:true`, next_close 2026-06-25 16:00 ET). **ONE action this routine: converted DE's −7% hard stop → 10% trailing stop** (DE crossed +5% at +5.31%, the #1 flagged action from the open). **No buys/sells** — nothing cleared 2 signals + Conviction ≥70 (PANW 66 / JPM 65 below the gate). All 4 positions green; no −7% drawdowns; daily loss cap not in play (book UP +1.34%). **Milestone: with DE converted, all 4 names (GE, LLY, ETN, DE) are now on 10% trailing GTC stops — zero hard stops left in the book.** Strong tape: SPY ~flat/down (−0.04%) while the book is +1.34% → broad-based gains across all four names. daytrade_count 0.

**Cash:** $46,447.18 (unchanged — no trades; the DE conversion moves no shares).
**Equity (intraday):** **$102,835.99** (cash $46,447.18 + long_market_value $56,388.81). last_equity **$101,480.08** = Alpaca's 6/24 official close (6/24 base).
**Day:** P/L **+$1,355.91 / +1.34%** | SPY **−0.04%** (732.92 latest-trade vs 733.24 6/24 bar close) → **day alpha +1.38 pts, AHEAD** (intraday).
**Week-to-date** (base 6/18 close $101,006.72 / SPY 746.75): portfolio **+1.81%** vs SPY **−1.85%** → **week alpha +3.66 pts, AHEAD** (day 4 of 4 this week; intraday).
**Buys used this week:** **0 of 3** (same week as 6/22). **NO buys/sells this routine** (DE stop conversion only). Nothing cleared 2 signals + Conviction ≥70.

## Open positions (4 of 5) — intraday marks (6/25 ~13:05 ET)

| Symbol | Shares | Avg Cost | Mark (6/25) | P/L $ | P/L % | Stop | Cushion | Entry Date | Thesis (1 line) |
|---|---|---|---|---|---|---|---|---|---|
| GE | 45 | 329.63 | 373.87 | +1,990.80 | +13.42% | **10% TRAILING (GTC)**, floor 341.703, hwm 379.67 | ~8.7% | 2026-06-08 | GE Aerospace — record commercial-aircraft demand + high-margin engine aftermarket + defense; pure industrial, ZERO AI overlap, lower beta. Book's anchor; hwm ratcheted to 379.67. Earnings ~Jul 16 (no blackout). Thesis intact. |
| LLY | 14 | 1078.46 | 1129.10 | +708.92 | +4.70% | **10% TRAILING (GTC)**, floor 1064.457, hwm 1182.73 | ~5.7% | 2026-06-01 | Eli Lilly — Q1 beat + raised guide + oral GLP-1 (orforglipron/Foundayo, FDA-approved Apr 1). Most rate-sensitive (long-duration growth); steady today. **CAVEAT:** $50/mo Medicare + July 1 Part D date remain UNVERIFIED (documented $25/mo insured / $149 cash). Floor ~5.7% below. |
| DE | 22 | 589.82 | 621.12 | +688.60 | +5.31% | **10% TRAILING (GTC)**, floor 558.945, hwm 621.05 | ~10.0% | 2026-06-04 | Deere — Q2 beat (5/21); ag-equipment/onshoring tailwind; NON-AI diversifier (ballast alongside GE). **Crossed +5% at midday → converted from −7% hard stop to a 10% trailing GTC (new id `dcdd84e5`).** Was the last name on a hard stop. Thesis intact. |
| ETN | 24 | 401.5425 | 420.445 | +453.66 | +4.71% | **10% TRAILING (GTC)**, floor 393.066, hwm 436.74 | ~6.5% | 2026-06-08 | Eaton — electrical "picks-and-shovels" for AI data-center power + electrification (orders +55%/rev +50%). +3.9% today, riding MU's blowout AI-memory read-through. Highest-beta name; still below its 436.74 hwm so the trailing floor stays 393.066. Earnings ~late July. |

**Open positions: 4 of 5.** **Buys used this week: 0 of 3** (1 free slot). **Cash buffer: ~45.2%** (~54.8% invested, $56,388.81 market value). Net open unrealized **+$3,841.98** (GE +1,990.80, LLY +708.92, DE +688.60, ETN +453.66).

## Stop-management state (all 4 confirmed RESTING as 10% TRAILING GTC, status `new` — re-verified this routine via open-orders query)

- **GE 10% trailing** `b9dadf2d-b6f5-49e7-8cc9-b3eb8b07aa6c` — floor **341.703**, hwm **379.67**. ~8.7% below the 373.87 mark.
- **LLY 10% trailing** `6016a7e7-faac-4e93-82e7-851abf30eca8` — floor **1064.457**, hwm **1182.73**. ~5.7% below the 1129.10 mark.
- **DE 10% trailing** `dcdd84e5-6b94-4943-aa5b-3d3a299cbfce` — floor **558.945**, hwm **621.05** (NEW this routine; replaced −7% hard stop `a150583a` @ 548.53, cancelled HTTP 204). ~10.0% below the 621.12 mark.
- **ETN 10% trailing** `cc843666-7e63-462a-82d4-57cc3e826ead` — floor **393.066**, hwm **436.74**. ~6.5% below the 420.445 mark; still below the 436.74 hwm so floor unchanged.
- (a) **−7% drawdown check (net from entry):** worst is LLY +4.70% — all four green net, none anywhere near −7%. HOLD. No sells.
- (b) **+5% → trailing:** GE, ETN, LLY, **DE** all now converted. **Zero hard stops remain — entire book on trailing stops.**
- (c) **Daily loss cap:** portfolio **UP +1.34%** intraday — nowhere near the −3% no-buy trigger. Clean.
- daytrade_count 0. One stop-management action (DE conversion); no shares traded. All stops resting.

## Watch / next (next routine: market-close 2026-06-25)

- **Market-close owns the mandatory daily "How we're doing" Telegram + dashboard update** (non-negotiable, every trading day). Lead with the plain-English scorecard: book +1.34% vs SPY ~−0.04%, ahead today; week alpha ~+3.66 pts.
- **DE conversion DONE** — the standing #1 near-term action is complete. DE floor 558.945 now ratchets up with price; no further manual action unless it tags the floor.
- **No new buys** — nothing clears 2 signals + Conviction ≥70. PANW (66, lead — STILL no fresh <2wk upgrade/insider buy; catalyst ~23d stale) and JPM (65, clean uptrend, next catalyst earnings Jul 14) both below the gate. 5th slot stays open. **AVGO (58, high-beta semis, overlaps ETN) explicitly OFF the table.**
- **PCE reaction held constructive:** core PCE released pre-open did NOT produce the feared hawkish shock — the book is broadly green at midday and SPY is roughly flat. The idle 5th slot can be treated as "deploy-clear" once a genuine ≥70 setup appears on a constructive base (still none today).
- **Macro:** earlier-week risk-off backdrop (hawkish Fed under Chair Warsh, DXY 1-yr high, 6/23 semis rout) has not re-asserted today; book up +1.34% on broad gains. GE/DE/LLY ballast + ETN + ~45% cash, now with all four on trailing stops, is a clean defensive-but-participating posture. Still waiting for a genuine ≥70 setup before deploying the 5th slot.

## Recent closes (last 5)

| Symbol | Exit Date | Shares | Entry | Exit | P/L $ | P/L % | Reason |
|---|---|---|---|---|---|---|---|
| NVDA | 2026-06-05 | 55 | 220.15 | 204.7158 | −848.88 | −7.01% | −7% hard stop fired (macro/NFP semis selloff, not thesis break) |
| NVDA | 2026-05-04 | 25 | 201.38 | ~195.02 | −159.04 | −3.16% | 10% trailing stop fired (round-trip) |

---
*Overwrite this file every routine. Keep it a live snapshot, not a log.*
