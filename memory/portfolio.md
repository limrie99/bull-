# Portfolio

**Last updated:** 2026-07-10 15:00 CT (16:00 ET) — **MARKET-CLOSE routine (official daily scorecard).** Market CLOSED (`is_open:false`, next_open Mon 2026-07-13 09:30 ET). Account live via Alpaca: equity **$101,813.69**, cash **$44,663.50** (~43.9%), long_market_value **$57,150.19** (~56.1%), status ACTIVE. Book **4 of 5 positions** (one slot OPEN). **NO trades today** (0 closed orders). **All 4 stops RESTING `status:new`, IDs/floors/hwm unchanged & re-verified** — 3 on 10% trailing (LLY, GE, DE), JPM on its −7% hard stop. **JPM +5%→trailing conversion NOT triggered** (close 336.47 = +2.05%, trigger $346.18). **Weekly buys 0/3.** **Inbox: nothing pending.** All 4 theses INTACT.

## Daily scorecard (OFFICIAL — close 7/10)
- **Day P/L: −$493.69 / −0.48%** (equity $101,813.69 vs 7/9 close $102,307.38).
- **SPY day: +0.45%** (754.94 vs 7/9 close 751.55).
- **Alpha today: −0.93 pts** (we lagged the market on a green tape — mostly ~44% idle cash giving no cushion, plus DE dipping negative and LLY/GE giving a little back).
- **Week-to-date (baseline 7/2 close $103,686.56):** port **−1.81%** vs **SPY +1.35%** → **week alpha −3.16 pts.**
- **Total since $100K start: +1.81%** (equity $101,813.69).

## Macro backdrop (carried, VERIFIED 7/8–7/9; re-verify near the print)
The 7/8 FOMC minutes read HAWKISH — 2026 PCE forecast raised 2.7%→3.6%, a 2026 net hike back on the table (Sept priced on CME FedWatch), cuts pushed to 2027–28, 9-8 split. 10Y ~4.56–4.58%, drifting up. **Tuesday Jul 14 stacks TWO pre-open events: JPM Q2 (~7am ET, IR-confirmed) + June CPI (8:30am ET, VERIFIED).** Near-term skew toward a hike = a headwind for risk assets and a reason for patience on fresh buys into the print.

**Cash:** $44,663.50 (~43.9%).
**Equity:** **$101,813.69** (cash $44,663.50 + long_market_value $57,150.19), 7/10 official close mark.
**SPY reference:** 754.94 (7/10 close).

## Open positions (4 of 5 — one slot OPEN) — marks = Alpaca 7/10 official close

| Symbol | Shares | Avg Cost | Close | P/L $ | P/L % | Stop | Entry Date | Thesis (1 line) |
|---|---|---|---|---|---|---|---|---|
| LLY | 14 | 1078.46 | 1188.01 | +1,533.70 | +10.16% | **10% TRAILING (GTC)**, floor **1124.505**, hwm **1249.45** | 2026-06-01 | Eli Lilly — Q1 beat + raised guide + oral GLP-1 (orforglipron, EBGLYSS). CMS Medicare GLP-1 "Bridge" ~$50/mo LIVE. No fresh dated catalyst. Thesis INTACT sev 1; cushion ~5.3% to floor. |
| GE | 45 | 329.63 | 359.27 | +1,333.80 | +8.99% | **10% TRAILING (GTC)**, floor **344.673**, hwm 382.97 | 2026-06-08 | GE Aerospace — record commercial-aircraft demand + high-margin engine aftermarket + defense; lower beta. Q2 ~Jul 16 (provisional). Citi Street-high PT→$431 (7/8, single-source). INTACT sev 1; cushion ~4.1% to floor. |
| JPM | 34 | 329.695588 | 336.47 | +230.33 | +2.05% | **−7% HARD STOP (GTC)** @ **306.62** | 2026-06-29 | JPMorgan — $50B buyback (eff Jul 1) + Q3 div hike; largest US bank. STARTER (~11%). **Q2 earnings IR-CONFIRMED Tue Jul 14 (~7am ET), straight into June CPI (8:30am)** — the one near-term event-risk. Far above stop. INTACT sev 1. |
| DE | 22 | 589.82 | 586.86 | −65.12 | −0.50% | **10% TRAILING (GTC)**, floor **575.073**, hwm 638.97 | 2026-06-04 | Deere — RE-RATED UP: big Q2 beat (May 21), FY26 guide raised, JPM PT $560→$590. **Off-cycle fiscal — next report fiscal Q3 ~mid-AUGUST.** 7/8 FTC right-to-repair SETTLEMENT = overhang cleared. INTACT sev 1; cushion tightest ~2.0% to floor. |

**Open positions: 4 of 5 (one slot OPEN).** **Buys used this week: 0 of 3.** **Cash buffer: ~43.9%** (~56.1% invested, ~$57,150 market value — above the 10–20% target; redeploy priority, gated on verifiable data at the Jul 14 JPM print + CPI). Net open unrealized **≈ +$3,032.71** (LLY +1,533.70, GE +1,333.80, JPM +230.33, DE −65.12) at close.

## Stop-management state (all 4 confirmed RESTING via open-orders query, status `new`, IDs unchanged)

- **LLY 10% trailing** `6016a7e7-faac-4e93-82e7-851abf30eca8` — floor **1124.505**, hwm **1249.45**. Close 1188.01 (below hwm, no ratchet), cushion ~5.3%.
- **GE 10% trailing** `b9dadf2d-b6f5-49e7-8cc9-b3eb8b07aa6c` — floor **344.673**, hwm 382.97. Close 359.27 (below hwm, no ratchet), cushion ~4.1%.
- **DE 10% trailing** `dcdd84e5-6b94-4943-aa5b-3d3a299cbfce` — floor **575.073**, hwm 638.97. Close 586.86 (below hwm, no ratchet), cushion ~2.0% (tightest in book).
- **JPM −7% HARD STOP** `3e8fe4ea-d95c-4e6c-82e1-ff66f0d56670` — stop **306.62** (GTC), entry 329.695588. Converts to a 10% trailing the moment JPM tags +5% ($346.18); close 336.47 = +2.05%, so ~2.9% away.

## Watch / next (next routine: **pre-market Mon 7/13**)

- **JPM +5% → trailing conversion (standing task):** the moment JPM tags **$346.18** (+5%), cancel the −7% hard stop `3e8fe4ea` and place a **10% trailing GTC**. Close 336.47 = +2.05%, ~2.9% away.
- **DE:** cushion tightest at ~2.0% and now fractionally red (−0.50%); off-cycle (next report mid-Aug), governed by the trailing stop — no discretionary action, just watch the 575.073 floor.
- **GE:** cushion ~4.1%; thesis intact into Q2 ~Jul 16 (provisional).
- **LLY:** cushion ~5.3%, book's strongest name (+10.16%), most room.
- **PRIORITY #1: redeploy cash — GATED on verifiable data.** ~43.9% cash, 4/5 positions. Key re-scan = the **Jul 14 JPM Q2 print** (the one IR-confirmed date) **+ June CPI 8:30am**. Do NOT buy an unverifiable catalyst; hawkish-Fed/rising-10Y adds a reason for patience.
- **ESCALATION WATCH (elevated):** **week alpha −3.16 pts** — a real miss, driven mostly by cash drag into a rising tape (SPY +1.35% WTD while we sat ~44% cash). Per the 7/3 strategy note, the gate/cash question stays parked behind the forward trigger: **re-evaluate only if, post-Jul-14, verifiable data returns and STILL nothing clears 2 signals + Conviction ≥70 while SPY keeps rising.** **Surface this explicitly at Friday's weekly review.**

## Recent closes (last 5)

| Symbol | Exit Date | Shares | Entry | Exit | P/L $ | P/L % | Reason |
|---|---|---|---|---|---|---|---|
| ETN | 2026-07-02 | 24 | 401.5425 | 392.75 | −211.02 | −2.19% | 10% trailing stop fired (beta/thin pre-holiday tape, not thesis break) |
| NVDA | 2026-06-05 | 55 | 220.15 | 204.7158 | −848.88 | −7.01% | −7% hard stop fired (macro/NFP semis selloff, not thesis break) |
| NVDA | 2026-05-04 | 25 | 201.38 | ~195.02 | −159.04 | −3.16% | 10% trailing stop fired (round-trip) |

---
*Overwrite this file every routine. Keep it a live snapshot, not a log.*
