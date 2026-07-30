# Portfolio

**Last updated:** 2026-07-30 08:35 CT — **MARKET-OPEN (Thu, market OPEN, is_open:true).** Live open marks from Alpaca. Account: equity **$101,485.17**, cash **$60,167.78** (~59.3%), long_market_value **$41,317.39** (~40.7%), buying_power $356,359.80, status ACTIVE. **NB:** Alpaca `last_equity` still reads the STALE **$103,482.04** (7/28 close — not yet rolled to the 7/29 official close $102,256.39), so a day-P/L off `last_equity` (−1.93%) is misleading. Against the real 7/29 close, open equity is **−$771.22 / −0.75%** = modest early give-back on thin open marks (**market-close owns the official daily number**). Book **3 of 5 positions (two slots OPEN)**. **ACTIONS THIS RUN: NONE** — executed the pre-market HOLD plan; nothing clears the gate (36th straight empty scan), no buys, no sells, no stop conversions, no fills. All 3 stops confirmed RESTING (10% trailing GTC) via open-orders query. **Inbox: nothing pending.**

## Scorecard (MARKET-OPEN 2026-07-30 — provisional, thin open marks)
- **Open equity $101,485.17.** Total since $100K start: **+1.49%.**
- **Intraday −$771.22 / −0.75%** vs the real 7/29 close $102,256.39 (do NOT use the stale `last_equity` $103,482.04).
- **vs SPY today:** SPY ~735.52 = **+0.82%** off its 7/29 close (729.57). So intraday we're **lagging SPY ~1.6 pts** (our pharma/ag names giving back while SPY bounces) — early-session noise, close owns the official read.
- **WTD (base Fri 7/24 close eq $102,740.86 / SPY 738.90):** our book WTD ~−1.22%; SPY WTD ~−0.46% (SPY 735.52). Official WTD lands at the close.
- **Cumulative alpha since 5/29 resume ~+5.7 pts** (SPY bounce narrowed it intraday).
- **Net open unrealized: ~+$2,039.17** (LLY +1,391.32, JPM +610.45, DE +37.40 — live open marks).
- **SPY refs:** ~735.52 (live open), 729.57 (7/29 close), 740.795 (7/28 close); new-week base 738.90 (7/24 close).

## Open positions (3 of 5 — two slots OPEN) — LIVE OPEN marks 7/30

| Symbol | Shares | Avg Cost | Mark (open) | P/L $ | P/L % | Stop | Entry Date | Thesis (1 line) |
|---|---|---|---|---|---|---|---|---|
| LLY | 14 | 1078.46 | 1177.84 | +1391.32 | +9.22% | **10% TRAILING (GTC)**, floor **1124.505**, hwm 1249.45 | 2026-06-01 | Eli Lilly — Q1 beat + raised guide + oral GLP-1 (orforglipron) pipeline; retatrutide Ph3. Earnings ~Aug 5. sev 1, quiet, intact. **Cushion ~4.53%.** Intraday −2.66%. ("Foundayo" fake-drug confab caught & discarded again.) |
| JPM | 34 | 329.695588 | 347.6499 | +610.45 | +5.45% | **10% TRAILING (GTC)**, floor **323.307**, hwm 359.23 | 2026-06-29 | JPMorgan — $50B buyback + div hike; largest US bank; Q2 (7/14) beat; DB UPGRADE Hold→Buy PT $375. Crossed +5% today but already trailing (never reverted). sev 1, quiet. **Cushion ~7.00%.** Next earnings ~Oct. |
| DE | 22 | 589.82 | 591.52 | +37.40 | +0.29% | **10% TRAILING (GTC)**, floor **579.591**, hwm 643.99 | 2026-06-04 | Deere — Q2 beat, FY26 guide raised, right-to-repair settlement cleared. $1.62 div payable Aug 10. Off-cycle; next report ~Aug 20. **sev 2 WATCH: −3.18% today, round-tripped its whole run (peak +9.2%→+0.29%); trailing floor 579.591 now ~1.7% BELOW entry so a stop-out would lock a small loss. NO thesis break — sentiment/ag-softness only.** Cushion ~2.02% (tightest — watch at midday). |

**Open positions: 3 of 5 (two slots OPEN).** **Buys used this week: 0 of 3.** **Cash buffer: ~59.3%.** Position sizes (on open equity $101,485.17): LLY 16.25%, DE 12.82%, JPM 11.65% — all under the 20% cap.

## Stop-management state (all 3 confirmed RESTING via open-orders query, nested=true) — ALL 10% TRAILING GTC, floors/hwm unchanged from 7/29 close
- **LLY 10% trailing** `6016a7e7-faac-4e93-82e7-851abf30eca8` — floor **1124.505**, hwm 1249.45. Live 1177.84, **cushion ~4.53%.**
- **JPM 10% trailing** `8a937ff6-164c-4384-8cf8-c000d4106a60` — floor **323.307**, hwm 359.23. Live 347.6499, cushion ~7.00%.
- **DE 10% trailing** `dcdd84e5-6b94-4943-aa5b-3d3a299cbfce` — floor **579.591**, hwm 643.99. Live 591.52, cushion ~2.02% (tightest; DE −3.18% today). All shares show qty_available:0 → reserved by their resting stops.

## +5% conversion check (market-open)
- JPM +5.45% (crossed +5% intraday) but ALREADY on a 10% trailing stop → **trailing stops are never reverted to hard stops.** LLY +9.22% and DE +0.29% both already trailing. **Zero hard stops remain → no −7%→trailing conversion needed.** No action.

## Watch / next (next routine: **Thu 7/30 midday ~12:05 CT**)
- **DE — tightest cushion ~2.02%.** Round-tripped its run on ag softness + negative right-to-repair re-framing (sentiment, NOT a new legal/guidance/exec event). Trailing stop 579.591 handles a break automatically (would exit ~−1.7% from entry). Only act manually on a real thesis break — none present. THE name to watch at midday.
- **Tonight: AAPL + AMZN report AMC.** We own neither — a read on tape sentiment, not a catalyst for our non-tech book.
- **Intraday divergence:** SPY bouncing (+0.82%) while our pharma/ag give back → we're lagging SPY intraday today, opposite of yesterday. Early-session noise; the close owns the number.
- **Bench (from pre-market):** UNH 64, LMT 63, NOW 63, GS 63, DLR 60, DOV 58, JNJ 58, ETN 56, ABT 55, OXY 55, STX 53, MS 52, AXP ~50, V ~50, AMGN/CB/CVS/VST 50, PANW 35. LMT 7/23 beat-and-raise to re-verify next scan; at ~63 it does not buy (chasing a +14%-week pop).
- **Cash-drag re-eval (ARMED — this IS the pre-committed test week):** today's PCE/GDP is the input; DECISION at **Friday's weekly review.** Carry the full week's tape, not one session.

## Recent closes (last 5)

| Symbol | Exit Date | Shares | Entry | Exit | P/L $ | P/L % | Reason |
|---|---|---|---|---|---|---|---|
| GE | 2026-07-16 | 45 | 329.63 | 344.54 | +670.95 | +4.52% | 10% trailing stop fired (post-Q2-earnings give-back caught the profit; no verified thesis break) |
| ETN | 2026-07-02 | 24 | 401.5425 | 392.75 | −211.02 | −2.19% | 10% trailing stop fired (beta/thin pre-holiday tape, not thesis break) |
| NVDA | 2026-06-05 | 55 | 220.15 | 204.7158 | −848.88 | −7.01% | −7% hard stop fired (macro/NFP semis selloff, not thesis break) |
| NVDA | 2026-05-04 | 25 | 201.38 | ~195.02 | −159.04 | −3.16% | 10% trailing stop fired (round-trip) |

---
*Overwrite this file every routine. Keep it a live snapshot, not a log.*
