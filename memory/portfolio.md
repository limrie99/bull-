# Portfolio

**Last updated:** 2026-07-01 ~08:35 CT (09:35 ET) — **MARKET-OPEN routine. Market OPEN** (`is_open:true`, next_close 7/1 16:00 ET). **No trades** — book AT the 5-position cap (5 of 5), nothing on the bench clears the ≥70 gate, and no held name hit a sell signal. All 5 theses INTACT (all sev 3, re-confirmed at pre-market). **All 5 stops RESTING `status:new`, IDs unchanged** — 4 of 5 on 10% trailing, JPM on its −7% hard stop. **JPM not yet at its +5% conversion trigger (~$346.18); mark 326.96 = ~−0.83%.** **Weekly buys 1 of 3.** daytrade_count 0. **Inbox: nothing pending.**

**Cash:** $35,237.52 (~33.9%).
**Equity (open, live marks):** **$103,931.64** (cash $35,237.52 + long_market_value $68,694.12). last_equity **$104,158.75** = Alpaca's official 6/30 close (today's base).
**Day P/L (open, live):** **−$227.11 / −0.22%** vs the 6/30 base — modestly red at the bell on early/thin marks (ETN −2.6%, DE −1.0% the day-movers; GE/LLY green). Official scorecard reads at the close routine.
**Week context (base = 6/26 close):** through 6/30 close, P/L was **+0.97%** vs SPY **+2.37%** → **alpha WTD −1.40%** (structural cash-drag/low-beta lag). No fresh SPY today — the effective weekly review (Thu 7/2, Fri is the holiday) recomputes the official alpha.

## Open positions (5 of 5 — AT CAP) — market-open 7/1 live marks

| Symbol | Shares | Avg Cost | Mark | P/L $ | P/L % | Stop | Entry Date | Thesis (1 line) |
|---|---|---|---|---|---|---|---|---|
| GE | 45 | 329.63 | 374.64 | +2,025.45 | +13.66% | **10% TRAILING (GTC)**, floor 341.703 | 2026-06-08 | GE Aerospace — record commercial-aircraft demand + high-margin engine aftermarket + defense; pure industrial, ZERO AI overlap, lower beta. Book's anchor. Earnings ~Jul 16 (UNVERIFIED). Thesis INTACT. |
| LLY | 14 | 1078.46 | 1210.99 | +1,855.42 | +12.29% | **10% TRAILING (GTC)**, floor **1114.2** (locks a profit) | 2026-06-01 | Eli Lilly — Q1 beat + raised guide + oral GLP-1. CMS Medicare GLP-1 $50/mo demo = Jul 1 2026 (VERIFIED). Healthcare lagging the rotation. Thesis INTACT. |
| DE | 22 | 589.82 | 628.00 | +839.96 | +6.47% | **10% TRAILING (GTC)**, floor **572.661** | 2026-06-04 | Deere — RE-RATED UP: big Q2 beat, FY26 guide raised, JPM PT $560→$590. Buy consensus, 0 Sells. INTACT — not the swap target. |
| ETN | 24 | 401.5425 | 414.89 | +320.34 | +3.32% | **10% TRAILING (GTC)**, floor 393.066 | 2026-06-08 | Eaton — electrical "picks-and-shovels" for AI data-center power + electrification. Highest-beta name. Off ~2.6% today → cushion above floor narrowed to ~5.3%. Earnings ~late July. Thesis INTACT — watch beta. |
| JPM | 34 | 329.695588 | 326.96 | −93.01 | −0.83% | **−7% HARD STOP (GTC)** @ **306.62** | 2026-06-29 | JPMorgan — $50B buyback LIVE (eff Jul 1, VERIFIED) + div +10%; largest US bank. STARTER (~10.7%). Q2 earnings CONFIRMED Tue Jul 14. Day-5, slightly below entry, far above its stop. Thesis INTACT. |

**Open positions: 5 of 5 (AT CAP).** **Buys used this week: 1 of 3** (0 free slots without a sell). **Cash buffer: ~33.9%** (~66.1% invested, ~$68,694 market value). Net open unrealized **~+$4,948.16** (GE +2,025.45, LLY +1,855.42, DE +839.96, ETN +320.34, JPM −93.01) — book green except JPM (day-5 starter, −0.83%, far above its stop).

## Stop-management state (all 5 confirmed RESTING via open-orders query, status `new`, IDs unchanged)

- **LLY 10% trailing** `6016a7e7-faac-4e93-82e7-851abf30eca8` — floor **1114.2** (above entry → locks a profit). Mark 1210.99, cushion ~8.0%.
- **GE 10% trailing** `b9dadf2d-b6f5-49e7-8cc9-b3eb8b07aa6c` — floor **341.703**. Mark 374.64, cushion ~8.8%.
- **DE 10% trailing** `dcdd84e5-6b94-4943-aa5b-3d3a299cbfce` — floor **572.661**. Mark 628.00, cushion ~8.8%.
- **ETN 10% trailing** `cc843666-7e63-462a-82d4-57cc3e826ead` — floor **393.066**. Mark 414.89 → cushion **~5.3%** (narrowed on today's −2.6%; highest-beta name, watch).
- **JPM −7% HARD STOP** `3e8fe4ea-d95c-4e6c-82e1-ff66f0d56670` — stop **306.62** (GTC), entry 329.695588. Converts to a 10% trailing the moment JPM tags +5% (~$346.18); mark 326.96 = ~−0.83%, so ~5.9% away.
- (a) **−7% drawdown check (net from entry):** worst is JPM −0.83% — all theses intact, none near −7%. HOLD. No sells.
- (b) **+5% → trailing:** 4 of 5 already on trailing; **JPM is the lone name on a −7% hard stop** (−0.83%, converts at ~$346.18).
- (c) **Daily loss cap:** day −0.22%, well inside the −3% cap — moot anyway (at the cap, no buys possible).
- daytrade_count 0.

## Watch / next (next routine: **midday Wed 7/1**)

- **JPM +5% → trailing conversion (standing task):** the moment JPM tags **~$346.18** (+5% from entry 329.695588), cancel the −7% hard stop `3e8fe4ea` and place a **10% trailing GTC**. Until then the −7% hard stop @ 306.62 protects it. (Mark 326.96 — needs ~+5.9% from here.)
- **At the 5-position cap, 1 of 3 weekly buys used.** No new buys possible without a sell first. **Nothing on the bench clears ≥70** (GS 58 = 1 verified signal; AMGN 55; V 52 after the BofA upgrade was confabulated). Held book has no obvious weak link → no natural swap target.
- **ETN cushion to watch:** highest-beta name, cushion above its 393.066 floor narrowed to ~5.3% after today's −2.6% — the squeeze candidate if the tape rolls into Thursday's jobs print. Let the trailing stop do its job; no pre-emptive action.
- **Do NOT initiate fresh size into the Thu 7/2 jobs print** (moot at the cap, but the principle stands if a slot frees on a thin, pre-holiday tape).
- **Alpha gap to watch:** WTD alpha −1.40% through 6/30. Structural cash-drag/low-beta lag, not a thesis problem — revisit whether ~34% cash is too defensive at the effective weekly review (Thu 7/2; Fri is the holiday).
- **Macro:** **ISM Manufacturing (June) due today** (reading UNVERIFIED); **June JOBS REPORT Thu 7/2 8:30 ET** (THE swing event, thin pre-holiday liquidity); **market CLOSED Fri 7/3.** JPM Q2 earnings Tue Jul 14 = key position-level event.

## Recent closes (last 5)

| Symbol | Exit Date | Shares | Entry | Exit | P/L $ | P/L % | Reason |
|---|---|---|---|---|---|---|---|
| NVDA | 2026-06-05 | 55 | 220.15 | 204.7158 | −848.88 | −7.01% | −7% hard stop fired (macro/NFP semis selloff, not thesis break) |
| NVDA | 2026-05-04 | 25 | 201.38 | ~195.02 | −159.04 | −3.16% | 10% trailing stop fired (round-trip) |

---
*Overwrite this file every routine. Keep it a live snapshot, not a log.*
