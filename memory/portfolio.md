# Portfolio

**Last updated:** 2026-06-29 ~12:05 CT (13:04 ET) — **MIDDAY routine. Market OPEN** (`is_open:true`, next_close 16:00 ET). **No trades — steady, no changes.** All 5 positions GREEN from entry, none near −7%, 4 of 5 on 10% trailing stops, JPM on its −7% hard stop (+0.65%, not yet at the +5% conversion trigger ~$346.18). **Book AT the 5-position cap (5 of 5). Weekly buys 1 of 3** (JPM at the open). daytrade_count 0.

**Cash:** $35,237.53 (34.0%).
**Equity (intraday 6/29 ~13:04 ET):** **$103,714.68** (cash $35,237.53 + long_market_value $68,477.15). last_equity **$103,121.46** = Alpaca's 6/26 official close (today's base). Day P/L so far **+$593.22 / +0.575%** (intraday; the close routine owns the official scorecard vs SPY).
**Buys used this week:** **1 of 3.** **0 open slots — AT the 5-position cap.** ~66% invested.

## Open positions (5 of 5 — AT CAP) — intraday marks ~13:04 ET

| Symbol | Shares | Avg Cost | Current | P/L $ | P/L % | Stop | Cushion | Entry Date | Thesis (1 line) |
|---|---|---|---|---|---|---|---|---|---|
| GE | 45 | 329.63 | 373.20 | +1,960.65 | +13.22% | **10% TRAILING (GTC)**, floor 341.703, hwm 379.67 | ~8.4% | 2026-06-08 | GE Aerospace — record commercial-aircraft demand + high-margin engine aftermarket + defense; pure industrial, ZERO AI overlap, lower beta. Book's anchor. Earnings ~Jul 16 (UNVERIFIED). Thesis INTACT. |
| LLY | 14 | 1078.46 | 1213.955 | +1,896.93 | +12.56% | **10% TRAILING (GTC)**, floor **1114.2** (above entry → locks a profit), hwm **1238** | ~8.2% | 2026-06-01 | Eli Lilly — Q1 beat + raised guide + oral GLP-1 (orforglipron/Foundayo); late-stage weight-loss trial WIN reported 6/24. Biggest winner. Earnings ~early Aug (UNVERIFIED). Thesis INTACT. |
| DE | 22 | 589.82 | 616.815 | +593.89 | +4.58% | **10% TRAILING (GTC)**, floor 568.737, hwm 631.93 | ~7.8% | 2026-06-04 | Deere — Q2 beat (5/21); ag-equipment/onshoring; NON-AI diversifier. **WATCH (book's weakest thesis — soft, not broken):** Jefferies Sell/$550 + weak ag volumes unchanged (not worsened); no fresh news. Best level since entry. HOLD on trailing. |
| ETN | 24 | 401.5425 | 409.805 | +198.30 | +2.06% | **10% TRAILING (GTC)**, floor 393.066, hwm 436.74 | ~4.1% | 2026-06-08 | Eaton — electrical "picks-and-shovels" for AI data-center power + electrification. Highest-beta name, thinnest cushion. No ETN-specific news, no downgrade. Earnings ~late July (UNVERIFIED). Thesis INTACT. |
| JPM | 34 | 329.695588 | 331.8392 | +72.88 | +0.65% | **−7% HARD STOP (GTC)** @ **306.62** | ~7.6% | 2026-06-29 | JPMorgan — post-CCAR capital return: $50B buyback (eff Jul 1) + div hike $1.50→$1.65/qtr (+10%); largest US bank, near ATH. **NEW STARTER** (~10.8%). Q2 earnings **CONFIRMED Tue Jul 14** = binary print ~11 trading days out → kept it a starter, not full size. Green day 1. Thesis INTACT. |

**Open positions: 5 of 5 (AT CAP).** **Buys used this week: 1 of 3** (0 free slots). **Cash buffer: ~34.0%** (~66% invested, ~$68,477.15 market value). Net open unrealized **+$4,722.65** (GE +1,960.65, LLY +1,896.93, DE +593.89, ETN +198.30, JPM +72.88) — whole book GREEN from entry.

## Stop-management state (all 5 confirmed RESTING via open-orders query, status `new`)

- **GE 10% trailing** `b9dadf2d-b6f5-49e7-8cc9-b3eb8b07aa6c` — floor **341.703**, hwm **379.67**. ~8.4% below the 373.20 mark.
- **LLY 10% trailing** `6016a7e7-faac-4e93-82e7-851abf30eca8` — floor **1114.2**, hwm **1238** (above entry 1078.46 → locks a profit). ~8.2% below the 1213.955 mark.
- **DE 10% trailing** `dcdd84e5-6b94-4943-aa5b-3d3a299cbfce` — floor **568.737**, hwm **631.93**. ~7.8% below the 616.815 mark.
- **ETN 10% trailing** `cc843666-7e63-462a-82d4-57cc3e826ead` — floor **393.066**, hwm **436.74**. ~4.1% below the 409.805 mark (thinnest cushion).
- **JPM −7% HARD STOP** `3e8fe4ea-d95c-4e6c-82e1-ff66f0d56670` — stop **306.62** (GTC), entry 329.695588. Converts to a 10% trailing the moment JPM tags +5% (~$346.18). ~7.6% below the 331.84 mark.
- (a) **−7% drawdown check (net from entry):** worst is JPM +0.65% — all five GREEN, none near −7%. HOLD. No sells, no news check needed.
- (b) **+5% → trailing:** 4 of 5 already on trailing; **JPM is the lone name on a −7% hard stop** (+0.65%, converts at ~$346.18 — ~4.3% above the current mark).
- (c) **Daily loss cap:** equity +0.575% on the day — not near the −3% cap. (Moot for new buys — at the position cap.)
- daytrade_count 0. No floors ratcheted this midday (all marks below their hwm).

## Watch / next (next routine: **market-close Mon 6/29**)

- **JPM +5% → trailing conversion (standing task):** the moment JPM tags **~$346.18** (+5% from entry 329.695588), cancel the −7% hard stop `3e8fe4ea` and place a **10% trailing GTC** (same workflow as the other four). Until then the −7% hard stop @ 306.62 protects it.
- **At the 5-position cap, 1 of 3 weekly buys used.** No new buys possible without a sell first. Any new idea this week is a *candidate swap* to reason about (does it out-score a held name?), not an automatic action. DE (book's weakest, soft thesis) is the natural swap target if a higher-conviction name appears.
- **Stops to watch:** ETN thinnest cushion (~4.1% above floor 393.066); JPM on the only hard stop; DE the lone WATCH (soft thesis, unrefuted Jefferies Sell, but at its best level since entry). GE/LLY ≥8%. Let them work.
- **Day-shape note:** SPY having a strong green day (~+1.3% intraday) vs our +0.575% — the expected cash-drag flip-side (we lag on up-days, cushion on down-days). Not a concern; close routine owns the official day-vs-SPY.
- **Macro week ahead (6/29–7/2; CLOSED Fri 7/3):** **June JOBS REPORT Thu 7/2 8:30 ET** (the swing event, thin pre-holiday liquidity). ISM Manufacturing Wed 7/1. **Do NOT initiate fresh size Wed 7/1** — moot at the cap. **JPM Q2 earnings Tue Jul 14** is the key position-level event.
- **Data flags:** Powell-vs-Warsh Fed-chair identity UNRESOLVED (don't build rate assumptions on it). SPY intraday ~738.97; close routine owns the official benchmark scorecard.

## Recent closes (last 5)

| Symbol | Exit Date | Shares | Entry | Exit | P/L $ | P/L % | Reason |
|---|---|---|---|---|---|---|---|
| NVDA | 2026-06-05 | 55 | 220.15 | 204.7158 | −848.88 | −7.01% | −7% hard stop fired (macro/NFP semis selloff, not thesis break) |
| NVDA | 2026-05-04 | 25 | 201.38 | ~195.02 | −159.04 | −3.16% | 10% trailing stop fired (round-trip) |

---
*Overwrite this file every routine. Keep it a live snapshot, not a log.*
