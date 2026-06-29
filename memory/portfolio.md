# Portfolio

**Last updated:** 2026-06-29 ~15:00 CT (16:04 ET) — **MARKET-CLOSE routine. Market CLOSED** (`is_open:false`, next_open 2026-06-30 09:30 ET). **No trades at the close** (today's only trade was the JPM starter buy at the open, already logged). All 5 positions GREEN from entry, none near −7%, 4 of 5 on 10% trailing stops, JPM on its −7% hard stop (+0.52%, not yet at the +5% conversion trigger ~$346.18). **Book AT the 5-position cap (5 of 5). Weekly buys 1 of 3** (JPM at the open). daytrade_count 0.

**Cash:** $35,237.53 (33.85%).
**Equity (official 6/29 close):** **$104,097.79** (cash $35,237.53 + long_market_value $68,860.26). last_equity **$103,121.46** = Alpaca's 6/26 official close (today's base).
**Day P/L:** **+$976.33 / +0.95%.** SPY day **+1.58%** (729.35 → 740.86). **Alpha today −0.63%** (we lagged on a strong up-day — the expected cash-drag flip-side; we cushion on down-days, lag on up-days).
**Week-to-date (today is Mon = day 1 of the week):** P/L **+0.95%**, SPY **+1.58%**, **alpha WTD −0.63%.**
**Buys used this week:** **1 of 3.** **0 open slots — AT the 5-position cap.** ~66% invested.

## Open positions (5 of 5 — AT CAP) — official 6/29 closing marks

| Symbol | Shares | Avg Cost | Close | P/L $ | P/L % | Day % | Stop | Cushion | Entry Date | Thesis (1 line) |
|---|---|---|---|---|---|---|---|---|---|---|
| LLY | 14 | 1078.46 | 1227.99 | +2,093.42 | +13.87% | +1.65% | **10% TRAILING (GTC)**, floor **1114.2** (above entry → locks a profit), hwm **1238** | ~9.3% | 2026-06-01 | Eli Lilly — Q1 beat + raised guide + oral GLP-1 (orforglipron/Foundayo); late-stage weight-loss trial WIN reported 6/24. Biggest winner. Earnings ~early Aug (UNVERIFIED). Thesis INTACT. |
| GE | 45 | 329.63 | 373.71 | +1,983.60 | +13.37% | +1.28% | **10% TRAILING (GTC)**, floor 341.703, hwm 379.67 | ~8.6% | 2026-06-08 | GE Aerospace — record commercial-aircraft demand + high-margin engine aftermarket + defense; pure industrial, ZERO AI overlap, lower beta. Book's anchor. Earnings ~Jul 16 (UNVERIFIED). Thesis INTACT. |
| DE | 22 | 589.82 | 626.63 | +809.82 | +6.24% | +2.18% | **10% TRAILING (GTC)**, floor 568.737, hwm 631.93 | ~9.2% | 2026-06-04 | Deere — Q2 beat (5/21); ag-equipment/onshoring; NON-AI diversifier. **WATCH (book's weakest thesis — soft, not broken):** Jefferies Sell/$550 + weak ag volumes unchanged (not worsened); no fresh news. Today's best level since entry (+2.18% on the day). HOLD on trailing. |
| ETN | 24 | 401.5425 | 408.26 | +161.22 | +1.67% | +1.39% | **10% TRAILING (GTC)**, floor 393.066, hwm 436.74 | ~3.7% | 2026-06-08 | Eaton — electrical "picks-and-shovels" for AI data-center power + electrification. Highest-beta name, thinnest cushion. No ETN-specific news, no downgrade. Earnings ~late July (UNVERIFIED). Thesis INTACT. |
| JPM | 34 | 329.695588 | 331.3925 | +57.70 | +0.52% | +0.71% | **−7% HARD STOP (GTC)** @ **306.62** | ~7.5% | 2026-06-29 | JPMorgan — post-CCAR capital return: $50B buyback (eff Jul 1) + div hike $1.50→$1.65/qtr (+10%); largest US bank, near ATH. **NEW STARTER** (~10.8%). Q2 earnings **CONFIRMED Tue Jul 14** = binary print ~11 trading days out → kept it a starter, not full size. Green day 1. Thesis INTACT. |

**Open positions: 5 of 5 (AT CAP).** **Buys used this week: 1 of 3** (0 free slots). **Cash buffer: ~33.85%** (~66% invested, ~$68,860.26 market value). Net open unrealized **+$5,105.76** (LLY +2,093.42, GE +1,983.60, DE +809.82, ETN +161.22, JPM +57.70) — whole book GREEN from entry.

## Stop-management state (all 5 confirmed RESTING via open-orders query, status `new`)

- **LLY 10% trailing** `6016a7e7-faac-4e93-82e7-851abf30eca8` — floor **1114.2**, hwm **1238** (above entry 1078.46 → locks a profit). ~9.3% below the 1227.99 close.
- **GE 10% trailing** `b9dadf2d-b6f5-49e7-8cc9-b3eb8b07aa6c` — floor **341.703**, hwm **379.67**. ~8.6% below the 373.71 close.
- **DE 10% trailing** `dcdd84e5-6b94-4943-aa5b-3d3a299cbfce` — floor **568.737**, hwm **631.93**. ~9.2% below the 626.63 close.
- **ETN 10% trailing** `cc843666-7e63-462a-82d4-57cc3e826ead` — floor **393.066**, hwm **436.74**. ~3.7% below the 408.26 close (thinnest cushion).
- **JPM −7% HARD STOP** `3e8fe4ea-d95c-4e6c-82e1-ff66f0d56670` — stop **306.62** (GTC), entry 329.695588. Converts to a 10% trailing the moment JPM tags +5% (~$346.18). ~7.5% below the 331.39 close.
- (a) **−7% drawdown check (net from entry):** worst is JPM +0.52% — all five GREEN, none near −7%. HOLD. No sells, no news check needed.
- (b) **+5% → trailing:** 4 of 5 already on trailing; **JPM is the lone name on a −7% hard stop** (+0.52%, converts at ~$346.18 — ~4.5% above today's close).
- (c) **Daily loss cap:** equity +0.95% on the day — nowhere near the −3% cap. (Moot for new buys — at the position cap.)
- daytrade_count 0. No trailing floors ratcheted today (all closing marks below their hwm: LLY 1227.99<1238, GE 373.71<379.67, DE 626.63<631.93, ETN 408.26<436.74).

## Watch / next (next routine: **pre-market Tue 6/30**)

- **JPM +5% → trailing conversion (standing task):** the moment JPM tags **~$346.18** (+5% from entry 329.695588), cancel the −7% hard stop `3e8fe4ea` and place a **10% trailing GTC** (same workflow as the other four). Until then the −7% hard stop @ 306.62 protects it.
- **At the 5-position cap, 1 of 3 weekly buys used.** No new buys possible without a sell first. Any new idea this week is a *candidate swap* to reason about (does it out-score a held name?), not an automatic action. DE (book's weakest, soft thesis) is the natural swap target if a higher-conviction name appears.
- **Stops to watch:** ETN thinnest cushion (~3.7% above floor 393.066); JPM on the only hard stop; DE the lone WATCH (soft thesis, unrefuted Jefferies Sell, but at its best level since entry). LLY/GE/DE ≥8.6%. Let them work.
- **Day-shape note:** SPY had a strong green day (+1.58%) vs our +0.95% — the expected cash-drag flip-side (we lag on up-days, cushion on down-days). Not a concern. Worth noting our spread of winners (DE +2.18%, LLY +1.65%, ETN +1.39%, GE +1.28%) all participated; the gap to SPY is purely the ~34% cash drag, not weak stocks.
- **Macro week ahead (6/29–7/2; CLOSED Fri 7/3):** **June JOBS REPORT Thu 7/2 8:30 ET** (the swing event, thin pre-holiday liquidity). ISM Manufacturing Wed 7/1. **Do NOT initiate fresh size Wed 7/1** — moot at the cap. **JPM Q2 earnings Tue Jul 14** is the key position-level event.
- **Data flags:** Powell-vs-Warsh Fed-chair identity UNRESOLVED (don't build rate assumptions on it). SPY close 740.86 (the official benchmark mark for today's scorecard).

## Recent closes (last 5)

| Symbol | Exit Date | Shares | Entry | Exit | P/L $ | P/L % | Reason |
|---|---|---|---|---|---|---|---|
| NVDA | 2026-06-05 | 55 | 220.15 | 204.7158 | −848.88 | −7.01% | −7% hard stop fired (macro/NFP semis selloff, not thesis break) |
| NVDA | 2026-05-04 | 25 | 201.38 | ~195.02 | −159.04 | −3.16% | 10% trailing stop fired (round-trip) |

---
*Overwrite this file every routine. Keep it a live snapshot, not a log.*
