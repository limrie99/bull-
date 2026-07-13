# Portfolio

**Last updated:** 2026-07-13 12:00 CT (13:02 ET) — **MIDDAY routine (Mon, market OPEN).** Clock `is_open:true`, next_close 16:00 ET. **NO TRADES / NO CHANGES** — steady midday. Risk sweep clean: (a) no position at/below −7% (worst is DE −0.86%); (b) both +5% names (LLY +10.24%, GE +7.32%) already on 10% trailing stops — no conversion needed; JPM +1.47% still ~3.5% below its +5% trigger; (c) daily loss cap NOT hit (portfolio −0.34% intraday vs −3% cap). Live Alpaca: equity **$101,475.58**, cash **$44,663.50** (~44.0%), long_market_value **$56,812.08** (~56.0%), last_equity (7/10 close) $101,821.67 → **day −$346.09 / −0.34%**. Book **4 of 5 positions** (one slot OPEN). **All 4 stops RE-VERIFIED RESTING** (open-orders `status:new`, IDs/floors/hwm unchanged). **Weekly buys 0/3.** **Inbox: nothing pending.** All 4 theses INTACT. Zero closed orders today.

## Intraday scorecard (midday — official belongs to the close routine)
- **Day P/L: −$346.09 / −0.34%** (equity $101,475.58 vs 7/10 close $101,821.67, per Alpaca last_equity).
- **SPY intraday: −0.64%** (750.14 live 13:02 ET vs 754.94 7/10 close). **Alpha so far ≈ +0.30 pts** — we're falling less than the market on a red tape (the ~44% cash cushion is doing its job today; the invested sleeve is roughly flat-to-soft).
- **Total since $100K start: +1.48%** (equity $101,475.58).
- (Week-to-date reconciliation belongs to the Friday close/weekly routines — early in the week, one-plus sessions in.)

## Macro backdrop (carried, VERIFIED 7/8–7/9; re-verify near the print)
7/8 FOMC minutes read HAWKISH — 2026 PCE forecast raised 2.7%→3.6%, a 2026 net hike back on the table (Sept priced on CME FedWatch), 9-8 split. 10Y ~4.57–4.58%, drifting up into CPI. **KEY EVENT — Tue Jul 14 (TOMORROW):** June CPI 8:30am ET (VERIFIED date; consensus UNVERIFIED) + **JPM Q2 ~7am release / 8:30 call (IR-CONFIRMED)** [cons EPS ~$5.58–5.59, rev ~$49–51B, PLAUSIBLE] + possible Warsh testimony. Wed 7/15 PPI. This is the pre-committed re-scan gate for redeploying cash. Near-term skew toward a hike = a headwind for risk assets and a reason for patience on fresh buys into the print.

**Cash:** $44,663.50 (~44.0%).
**Equity:** **$101,475.58** (cash $44,663.50 + long_market_value $56,812.08), live midday mark.
**SPY reference:** 750.14 (live 13:02 ET; 754.94 was the 7/10 close).

## Open positions (4 of 5 — one slot OPEN) — marks = Alpaca live midday 13:02 ET

| Symbol | Shares | Avg Cost | Mark | P/L $ | P/L % | Stop | Entry Date | Thesis (1 line) |
|---|---|---|---|---|---|---|---|---|
| LLY | 14 | 1078.46 | 1188.88 | +1,545.88 | +10.24% | **10% TRAILING (GTC)**, floor **1124.505**, hwm **1249.45** | 2026-06-01 | Eli Lilly — Q1 beat + raised guide + oral GLP-1 (orforglipron, EBGLYSS). CMS Medicare GLP-1 "Bridge" ~$50/mo LIVE. No fresh dated catalyst. Thesis INTACT sev 1; cushion ~5.4% to floor (book's strongest name). |
| GE | 45 | 329.63 | 353.775 | +1,086.53 | +7.32% | **10% TRAILING (GTC)**, floor **344.673**, hwm 382.97 | 2026-06-08 | GE Aerospace — record commercial-aircraft demand + high-margin engine aftermarket + defense; lower beta. Q2 ~Jul 16 (ESTIMATE). INTACT sev 2 (earnings binary this week); cushion ~2.6% to floor. |
| JPM | 34 | 329.695588 | 334.54 | +164.71 | +1.47% | **−7% HARD STOP (GTC)** @ **306.62** | 2026-06-29 | JPMorgan — $50B buyback (eff Jul 1) + Q3 div hike; largest US bank. STARTER (~11%). **Q2 earnings IR-CONFIRMED Tue Jul 14 (~7am ET), into June CPI (8:30am)** — the one near-term event-risk. Far above stop. INTACT sev 2 (reports tomorrow). |
| DE | 22 | 589.82 | 584.74 | −111.76 | −0.86% | **10% TRAILING (GTC)**, floor **575.073**, hwm 638.97 | 2026-06-04 | Deere — RE-RATED UP: big Q2 beat (May 21), FY26 guide raised, JPM PT $560→$590. **Off-cycle fiscal — next report fiscal Q3 ~mid-AUGUST.** 7/8 FTC right-to-repair SETTLEMENT = overhang cleared. INTACT sev 1; cushion tightest ~1.7% to floor. |

**Open positions: 4 of 5 (one slot OPEN).** **Buys used this week: 0 of 3.** **Cash buffer: ~44.0%** (~56.0% invested, ~$56,812 market value — above the 10–20% target; redeploy priority, gated on verifiable data at the Jul 14 JPM print + CPI). Net open unrealized **≈ +$2,685.36** (LLY +1,545.88, GE +1,086.53, JPM +164.71, DE −111.76) at midday. Position sizes: LLY 16.4%, GE 15.7%, DE 12.7%, JPM 11.2% — all under the 20% cap.

## Stop-management state (all 4 confirmed RESTING via open-orders query, status `new`, IDs unchanged)

- **LLY 10% trailing** `6016a7e7-faac-4e93-82e7-851abf30eca8` — floor **1124.505**, hwm **1249.45**. Mark 1188.88 (below hwm, no ratchet), cushion ~5.4%.
- **GE 10% trailing** `b9dadf2d-b6f5-49e7-8cc9-b3eb8b07aa6c` — floor **344.673**, hwm 382.97. Mark 353.775 (below hwm, no ratchet), cushion ~2.6%.
- **DE 10% trailing** `dcdd84e5-6b94-4943-aa5b-3d3a299cbfce` — floor **575.073**, hwm 638.97. Mark 584.74 (below hwm, no ratchet), cushion ~1.7% (tightest in book).
- **JPM −7% HARD STOP** `3e8fe4ea-d95c-4e6c-82e1-ff66f0d56670` — stop **306.62** (GTC), entry 329.695588. Converts to a 10% trailing the moment JPM tags +5% ($346.18); mark 334.54 = +1.47%, so ~3.5% away.

## Watch / next (next routine: **market-close Mon 7/13**)

- **JPM +5% → trailing conversion (standing task):** the moment JPM tags **$346.18** (+5%), cancel the −7% hard stop `3e8fe4ea` and place a **10% trailing GTC**. Mark 334.54 = +1.47%, ~3.5% away. Likely to move on tomorrow's Q2 print — watch at the close and at/around the Tue open.
- **DE:** cushion tightest at ~1.7% and fractionally red (−0.86%); off-cycle (next report mid-Aug), governed by the trailing stop — no discretionary action, just watch the 575.073 floor.
- **GE:** cushion ~2.6%; thesis INTACT into Q2 ~Jul 16 (ESTIMATE — verify vs GE IR mid-week). Earnings are the real near-term risk to the cushion.
- **LLY:** cushion ~5.4%, book's strongest name (+10.24%), most room.
- **PRIORITY #1: redeploy cash — GATED on verifiable data.** ~44.0% cash, 4/5 positions. Key re-scan = the **Jul 14 JPM Q2 print** (the one IR-confirmed date) **+ June CPI 8:30am**. Do NOT buy an unverifiable catalyst; hawkish-Fed/rising-10Y adds a reason for patience.
- **ESCALATION WATCH (elevated — SURFACED at the 7/10 weekly review):** 2 straight sub-SPY weeks, cumulative cushion halved. **NO rule changed** (pre-committed: the gate/cash re-evaluation is gated to POST-Jul-14). **Escalation teed up for Lauren:** if the Jul 14–17 bank-earnings wave + CPI passes and STILL nothing clears 2 signals + Conviction ≥70 while SPY keeps rising, put a plain-English A/B decision in the **inbox** (deploy idle ~44% cash into a broad/index-like holding vs. hold the defensive posture). Already flagged to her in the 7/10 weekly message.

## Recent closes (last 5)

| Symbol | Exit Date | Shares | Entry | Exit | P/L $ | P/L % | Reason |
|---|---|---|---|---|---|---|---|
| ETN | 2026-07-02 | 24 | 401.5425 | 392.75 | −211.02 | −2.19% | 10% trailing stop fired (beta/thin pre-holiday tape, not thesis break) |
| NVDA | 2026-06-05 | 55 | 220.15 | 204.7158 | −848.88 | −7.01% | −7% hard stop fired (macro/NFP semis selloff, not thesis break) |
| NVDA | 2026-05-04 | 25 | 201.38 | ~195.02 | −159.04 | −3.16% | 10% trailing stop fired (round-trip) |

---
*Overwrite this file every routine. Keep it a live snapshot, not a log.*
