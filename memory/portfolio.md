# Portfolio

**Last updated:** 2026-06-23 15:00 CT (MARKET-CLOSE routine — authoritative day-vs-SPY scorecard. Market CLOSED 16:00 ET. **NO trades today** (0 closed orders). Down day, but we **beat the market**: equity fell to **$100,701.25** (−$783.15 / **−0.77%**) while SPY fell **−1.43%** → **day alpha +0.66 pts, AHEAD** — the book lost roughly half what the index did. The loss was set at the open (a broad risk-off tape) and we actually drifted *up* ~$330 from the open mark ($100,371.21) into the close. **ETN was the day's pain point: −7.06% intraday** on a soft AI-power tape — but it's on a 10% trailing stop (floor 393.066, ~3% below the 405.01 close), never reverts to a hard stop, still **+0.86% net** from entry, thesis intact, no verifiable breaker → no action. GE (+0.38%), LLY (+0.27%), DE (−1.11%) all minor. All 4 GTC stops re-verified RESTING `status:new` via open-orders query; daytrade_count 0.)
**Cash:** $46,447.18 (unchanged — no trades).
**Equity (Alpaca authoritative close):** **$100,701.25**. last_equity **$101,484.40** = Alpaca's 6/22 official close (6/22 base).
**Day P/L:** **−$783.15 / −0.77%.** SPY day **−1.43%** → **day alpha +0.66 pts, AHEAD.**
**Week-to-date** (base 6/18 close $101,006.72 / SPY 746.75 — Fri 6/19 was the Juneteenth holiday): portfolio **−$305.47 / −0.30%** | SPY **−1.76%** | **week alpha +1.46 pts, AHEAD** (2 sessions in).
**Buys used this week:** **0 of 3** (same week as 6/22). **NO trades this routine.** Nothing clears 2 signals + Conviction ≥70.

## Open positions (4 of 5) — live closing marks (6/23)

| Symbol | Shares | Avg Cost | Mark (6/23 close) | P/L $ | P/L % | Day % | Stop | Entry Date | Thesis (1 line) |
|---|---|---|---|---|---|---|---|---|---|
| GE | 45 | 329.63 | 356.47 | +1,207.80 | +8.14% | +0.38% | **10% TRAILING (GTC)**, floor 328.23, hwm 364.7 | 2026-06-08 | GE Aerospace — record commercial-aircraft demand + high-margin engine aftermarket + defense; pure industrial, zero AI overlap, lower beta. Book's strongest, the day's anchor (green on a red tape). Earnings ~Jul 16 (no blackout). Thesis intact. |
| ETN | 24 | 401.5425 | 405.01 | +83.22 | +0.86% | **−7.06%** | **10% TRAILING (GTC)**, floor 393.066, hwm 436.74 | 2026-06-08 | Eaton — electrical "picks-and-shovels" for AI data-center power + electrification (orders +55%/rev +50%). **Fell −7.06% today** (broad AI-power de-risking, high beta) but on a 10% trailing stop — never reverts to a hard stop; floor 393.066 (~3.0% below the 405.01 close), still +0.86% net, thesis intact, no verifiable breaker. Earnings ~late July. Watch tomorrow: if it keeps sliding the trailing stop does its job; no manual action. |
| LLY | 14 | 1078.46 | 1105.00 | +371.56 | +2.46% | +0.27% | **10% TRAILING (GTC)**, floor 1064.457, hwm 1182.73 | 2026-06-01 | Eli Lilly — Q1 beat + raised guide + oral GLP-1 (orforglipron/Foundayo, FDA-approved Apr 1). Anchor; held green on a red day. **CAVEAT:** $50/mo Medicare + July 1 Part D date remain UNVERIFIED (documented $25/mo insured / $149 cash). Floor ~3.7% below. |
| DE | 22 | 589.82 | 591.94 | +46.64 | +0.36% | −1.11% | 548.53 (−7%, **GTC**) | 2026-06-04 | Deere — Q2 beat (5/21); ag-equipment/onshoring tailwind; NON-AI diversifier. Eased −1.11% on the tape but still fractionally green net and ~7.3% above its hard stop. Lone name still on a −7% hard stop; +5% conversion trigger ~619.31 (~$27 above mark, not yet). HOLD. |

**Open positions: 4 of 5.** **Buys used this week: 0 of 3** (1 free slot). **Cash buffer: ~46.1%** (~53.9% invested, $54,254.07 market value). Net open unrealized **+$1,709.22** (GE +1,207.80, LLY +371.56, ETN +83.22, DE +46.64).

## Stop-management state (all 4 confirmed RESTING as GTC, status `new` — re-verified this routine via open-orders query)

- **GE 10% trailing** `b9dadf2d-b6f5-49e7-8cc9-b3eb8b07aa6c` — floor **328.23**, hwm **364.7**. ~7.9% below the 356.47 close.
- **ETN 10% trailing** `cc843666-7e63-462a-82d4-57cc3e826ead` — floor **393.066**, hwm **436.74**. ~3.0% below the 405.01 close after the −7.06% day. Trailing never reverts to a hard stop — no action; if ETN keeps falling to 393.066 it auto-sells, locking the gain above entry.
- **LLY 10% trailing** `6016a7e7-faac-4e93-82e7-851abf30eca8` — floor **1064.457**, hwm **1182.73**. ~3.7% below the 1105.00 close.
- **DE −7% hard** `a150583a-a58c-42c9-8d12-9d7ece773841` @ **548.53** (~7.3% cushion). The only name still on a hard stop.
- (a) **−7% drawdown check (net from entry):** worst is DE +0.36% — all four green net, none near −7%. ETN's −7.06% was a *day* move (vs prior close), not from entry; net it's still +0.86%. HOLD. No sells.
- (b) **+5% → trailing:** GE, ETN, LLY all converted. DE +0.36%, far below its +5% (~619.31). Nothing pending.
- (c) **Daily loss cap:** day −0.77% — within the −3% cap (no buy ban; none planned anyway).
- daytrade_count 0. No trades this routine. Stops all resting.

## Watch / next (next check: pre-market 2026-06-24)

- **No new buys** — nothing clears 2 signals + Conviction ≥70. PANW (66, lead — catalyst ~21d stale, still no fresh <2wk upgrade/insider buy) and JPM (65, clean uptrend but no <2wk catalyst, earnings ~Jul 14) both below the gate. 5th slot stays open.
- **ETN watch:** the day's loser (−7.06%) on a soft AI-power tape; thesis intact, on a trailing stop with ~3.0% cushion (floor 393.066). If it keeps sliding the trailing stop does its job automatically; no manual action. The narrowest cushion of the four — watch first tomorrow.
- **DE conversion watch:** if DE tags +5% (~619.31), cancel the −7% hard stop and place a 10% trailing GTC stop. (Currently +0.36%.)
- **This week's calendar:** **core PCE Thu 6/25 8:30 ET (VERIFIED)** — week's marquee event and the deploy-or-defer pivot for the idle 5th slot. **MU Wed AMC** (if confirmed) → semis/AI vol Thu. **Blackout clean** for all our names this week (retrieval-gap caveat — verify at IR before any buy).
- **Macro:** risk-off today (SPY −1.43%) — yields/PCE overhang, AI-power names hit hardest. Waiting for Thu PCE before a fresh rate-sensitive entry remains prudent; the book's selection (industrial + healthcare ballast) cushioned the down day.

## Recent closes (last 5)

| Symbol | Exit Date | Shares | Entry | Exit | P/L $ | P/L % | Reason |
|---|---|---|---|---|---|---|---|
| NVDA | 2026-06-05 | 55 | 220.15 | 204.7158 | −848.88 | −7.01% | −7% hard stop fired (macro/NFP semis selloff, not thesis break) |
| NVDA | 2026-05-04 | 25 | 201.38 | ~195.02 | −159.04 | −3.16% | 10% trailing stop fired (round-trip) |

---
*Overwrite this file every routine. Keep it a live snapshot, not a log.*
