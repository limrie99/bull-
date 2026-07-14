# Portfolio

**Last updated:** 2026-07-14 12:02 CT (13:02 ET) — **MIDDAY routine (Tue, market OPEN; next_close 16:00 ET).** Live Alpaca: equity **$101,066.19**, cash **$44,663.50** (~44.2%), long_market_value **$56,402.69** (~55.8%), last_equity (7/13 close) $101,371.68 → day **−$305.49 / −0.30%** (mild red vs a green tape). Book **4 of 5 positions** (one slot OPEN). **All 4 stops RE-VERIFIED RESTING** (open-orders `status:new`, IDs/floors/hwm unchanged). **Weekly buys 0/3.** **Zero fills / zero stops fired today.** **Inbox: nothing pending.** **Decision: NO TRADES, NO STOP CHANGES — steady midday.**

## Risk sweep (midday, in priority order)
- **(a) Any position −7% or worse?** NO. Worst is DE at **−1.73%** — nowhere near its −7% floor. DE dropped intraday (was +1.45% at open); Perplexity check → **no verifiable Jul 14 DE-specific catalyst; ag/farm-cycle sector noise (severity 2), thesis INTACT.** Governed by its 10% trailing stop — no discretionary action.
- **(b) Any position +5%+ needing a trailing conversion?** GE (+7.28%) and LLY (+7.00%) **already on 10% trailings**. **JPM +3.45% ($341.06) — still short of the +5% trigger $346.18 (~1.50% away)** → −7% hard stop stays; no conversion yet.
- **(c) Daily loss cap:** portfolio **−0.30%** intraday, well inside the −3% cap → **buys NOT blocked** by the cap (they're blocked by the no-qualifier gate, as always).

## Why NO TRADE at midday
- Midday only buys on a **high-conviction breaking catalyst** + caps OK. No such catalyst surfaced: the verification wall that blocked the JPM Q2 print + June CPI at the open persists; no bench name (AXP/GS) picked up a 2nd VERIFIED signal from the bank wave. Nothing clears **2 VERIFIED signals + Conviction ≥70**. Capacity exists (slot open, 0/3 buys, ~44% cash) — the block is the verification wall, not caps.

## Snapshot
- Day P/L **−$305.49 / −0.30%** (equity $101,066.19 vs 7/13 close $101,371.68). **SPY day +0.38%** (752.01 vs 749.13) → **alpha today ≈ −0.68 pts** (mild red on a green tape — DE the drag).
- **Week-to-date (baseline 7/10 close $101,821.67 / SPY 754.94):** port **−0.74%** vs SPY **−0.39%** → **week alpha ≈ −0.35 pts** (2 sessions in).
- **Total since $100K start: +1.07%.**
- Net open unrealized ≈ **+$2,299.34** (LLY +1,057.35, GE +1,079.78, JPM +386.39, DE −224.18).

**Cash:** $44,663.50 (~44.2%).
**Equity:** **$101,066.19.**
**SPY reference:** 752.01 (live 13:02 ET); 749.13 (7/13 close).

## Open positions (4 of 5 — one slot OPEN) — marks = Alpaca live ~13:02 ET

| Symbol | Shares | Avg Cost | Mark | P/L $ | P/L % | Stop | Entry Date | Thesis (1 line) |
|---|---|---|---|---|---|---|---|---|
| LLY | 14 | 1078.46 | 1153.985 | +1,057.35 | +7.00% | **10% TRAILING (GTC)**, floor **1124.505**, hwm **1249.45** | 2026-06-01 | Eli Lilly — Q1 beat + raised guide + oral GLP-1 (orforglipron, EBGLYSS). GLP-1 franchise unbroken. Earnings ~Aug 5 (est). Thesis INTACT sev 1. Up today; cushion ~2.6%. |
| GE | 45 | 329.63 | 353.625 | +1,079.78 | +7.28% | **10% TRAILING (GTC)**, floor **344.673**, hwm 382.97 | 2026-06-08 | GE Aerospace — record commercial-aircraft demand + engine aftermarket + defense; lower beta. **Q2 VERIFIED Thu Jul 16 7:30am EDT (GE IR).** INTACT sev 1; cushion ~2.5% — earnings the near-term risk. |
| JPM | 34 | 329.695588 | 341.06 | +386.39 | +3.45% | **−7% HARD STOP (GTC)** @ **306.62** | 2026-06-29 | JPMorgan — $50B buyback (eff Jul 1) + Q3 div hike; largest US bank. STARTER (~11%). Q2 reported 7/14 — actuals still UNVERIFIABLE via our tools; stock +3.45% since cost, drifting up. INTACT sev 2. +5%→trailing trigger $346.18, ~1.50% away. |
| DE | 22 | 589.82 | 579.63 | −224.18 | −1.73% | **10% TRAILING (GTC)**, floor **575.073**, hwm 638.97 | 2026-06-04 | Deere — big Q2 beat (May 21), FY26 guide raised, JPM PT $560→$590. 7/8 FTC right-to-repair settlement cleared. Off-cycle; next report ~Aug 20 (est). INTACT sev 1 (Jul 14 dip = ag-sector noise, no verifiable catalyst); DOWN today, cushion now TIGHTEST ~0.8%. |

**Open positions: 4 of 5 (one slot OPEN).** **Buys used this week: 0 of 3.** **Cash buffer: ~44.2%** (~55.8% invested — above the 10–20% target; redeploy still the priority but STILL no qualifier). Position sizes: LLY 16.0%, GE 15.7%, DE 12.6%, JPM 11.5% — all under the 20% cap.

## Stop-management state (all 4 confirmed RESTING via open-orders query, status `new`, IDs unchanged)

- **LLY 10% trailing** `6016a7e7-faac-4e93-82e7-851abf30eca8` — floor **1124.505**, hwm **1249.45**. Mark 1153.985 (below hwm, no ratchet), cushion **~2.6%**.
- **GE 10% trailing** `b9dadf2d-b6f5-49e7-8cc9-b3eb8b07aa6c` — floor **344.673**, hwm 382.97. Mark 353.625 (below hwm, no ratchet), cushion ~2.5%.
- **DE 10% trailing** `dcdd84e5-6b94-4943-aa5b-3d3a299cbfce` — floor **575.073**, hwm 638.97. Mark 579.63 (below hwm, no ratchet), cushion **~0.8% (TIGHTEST — DE −1.73% today on ag noise)**.
- **JPM −7% HARD STOP** `3e8fe4ea-d95c-4e6c-82e1-ff66f0d56670` — stop **306.62** (GTC), entry 329.695588. Converts to a 10% trailing the moment JPM tags +5% ($346.18); mark 341.06 = +3.45%, so ~1.50% away.

## Watch / next (next routine: **market-close Tue 7/14 ~15:00 CT**)

- **JPM +5% → trailing conversion (standing task):** the moment JPM tags **$346.18** (+5%), cancel the −7% hard stop `3e8fe4ea` and place a **10% trailing GTC**. Mark 341.06, ~1.50% away — closest yet; watch at the close.
- **DE:** cushion now TIGHTEST at ~0.8% (down −1.73% today on ag-sector noise, thesis intact). Purely governed by the 10% trailing floor 575.073 — if it slips ~$4.55 more the stop auto-fires; no discretionary action, just watch. A trailing-stop exit here would be a mechanical ~+1.5% giveback from cost basis proceeds, not a thesis break.
- **Redeploy ~44% idle cash — STILL GATED.** The gate day (JPM print, CPI) came and went with catalyst data unverifiable via our tools; the tape is calm-to-mildly-red (no risk-off flush) but that's not a confirmed green light. Close/tomorrow: re-scan bench (AXP/GS) for a 2nd verified signal once bank actuals are confirmable.
- **LLY / GE:** theses INTACT (LLY sev 1; GE sev 1 into Q2 VERIFIED Thu Jul 16 7:30am — earnings the near-term risk), both governed by their trailings, cushions ~2.5–2.6%.
- **Bench lead:** AXP 62 (VERIFIED JPMorgan upgrade 7/13) — 1 solid signal, below the gate; needs a 2nd (a confirmed bank beat-and-raise or its own Jul 24 print). GS 60 (Q2 reported 7/14, actuals unverifiable — re-check when confirmable).
- **ESCALATION WATCH (teed up 7/10) — HELD, still mid-window.** Trigger = "if the Jul 14–17 bank wave + CPI passes with STILL nothing clearing 2 signals + Conviction ≥70 while SPY keeps rising." Today's data was **unverifiable rather than confirmed-empty**, GE Q2 (Thu 7/16) is still pending, and SPY is only marginally green — so the escalation does NOT fire today. Stays teed up for the back half of this window (post-GE Thu / Fri weekly review). If the whole window closes empty with SPY higher, the A/B cash-deployment decision goes to Lauren's inbox then.

## Recent closes (last 5)

| Symbol | Exit Date | Shares | Entry | Exit | P/L $ | P/L % | Reason |
|---|---|---|---|---|---|---|---|
| ETN | 2026-07-02 | 24 | 401.5425 | 392.75 | −211.02 | −2.19% | 10% trailing stop fired (beta/thin pre-holiday tape, not thesis break) |
| NVDA | 2026-06-05 | 55 | 220.15 | 204.7158 | −848.88 | −7.01% | −7% hard stop fired (macro/NFP semis selloff, not thesis break) |
| NVDA | 2026-05-04 | 25 | 201.38 | ~195.02 | −159.04 | −3.16% | 10% trailing stop fired (round-trip) |

---
*Overwrite this file every routine. Keep it a live snapshot, not a log.*
