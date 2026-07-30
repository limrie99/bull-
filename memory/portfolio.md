# Portfolio

**Last updated:** 2026-07-30 12:05 CT — **MIDDAY (Thu, market OPEN, is_open:true).** Live midday marks from Alpaca. Account: equity **$101,688.72**, cash **$60,167.78** (~59.17%), long_market_value **$41,520.94** (~40.83%), buying_power $356,929.75, status ACTIVE. **NB:** Alpaca `last_equity` still reads the STALE **$103,482.04** (7/28 close — not yet rolled to the 7/29 official close $102,256.39), so a day-P/L off `last_equity` (−1.73%) is misleading. Against the real 7/29 close, midday equity is **−$567.67 / −0.56%** = modest give-back on a tech-led SPY bounce we don't share (**market-close owns the official daily number**). Book **3 of 5 positions (two slots OPEN)**. **ACTIONS THIS RUN: NONE** — executed the pre-market/open HOLD plan; nothing clears the gate (~37th straight empty scan), no buys, no sells, no stop conversions, no fills. All 3 stops confirmed RESTING (10% trailing GTC) via open-orders query. **Inbox: nothing pending.**

## Scorecard (MIDDAY 2026-07-30 — provisional, live marks)
- **Midday equity $101,688.72.** Total since $100K start: **+1.69%.**
- **Intraday −$567.67 / −0.56%** vs the real 7/29 close $102,256.39 (do NOT use the stale `last_equity` $103,482.04). Recovered ~$203.55 from the 8:35 open mark ($101,485.17).
- **vs SPY today:** SPY ~740.00 = **+1.43%** off its 7/29 close (729.57). So intraday we're **lagging SPY ~2.0 pts** (our pharma/ag names sit out a tech-led bounce after a benign PCE/GDP) — early-session noise, close owns the official read.
- **WTD (base Fri 7/24 close eq $102,740.86 / SPY 738.90):** our book WTD ~−1.02%; SPY WTD ~+0.15% (SPY 740.00) → alpha WTD ~−1.17 pts. Official WTD lands Friday.
- **Cumulative alpha since 5/29 resume ~+5.7 pts** (SPY bounce narrowing it intraday).
- **Net open unrealized: ~+$2,232.48** (LLY +1,188.53, JPM +752.23, DE +291.72 — live midday marks).
- **SPY refs:** ~740.00 (live midday), 729.57 (7/29 close), 740.795 (7/28 close); new-week base 738.90 (7/24 close).

## Open positions (3 of 5 — two slots OPEN) — LIVE MIDDAY marks 7/30

| Symbol | Shares | Avg Cost | Mark (midday) | P/L $ | P/L % | Stop | Entry Date | Thesis (1 line) |
|---|---|---|---|---|---|---|---|---|
| LLY | 14 | 1078.46 | 1163.355 | +1188.53 | +7.87% | **10% TRAILING (GTC)**, floor **1124.505**, hwm 1249.45 | 2026-06-01 | Eli Lilly — Q1 beat + raised guide + oral GLP-1 (orforglipron) pipeline; retatrutide Ph3. Earnings ~Aug 5. sev 1, quiet, intact. **Cushion ~3.34%.** Pulled back from +9.22% open mark; well above floor. |
| JPM | 34 | 329.695588 | 351.82 | +752.23 | +6.71% | **10% TRAILING (GTC)**, floor **323.307**, hwm 359.23 | 2026-06-29 | JPMorgan — $50B buyback + div hike; largest US bank; Q2 (7/14) beat; DB UPGRADE Hold→Buy PT $375. Already trailing (never reverted). sev 1, quiet. **Cushion ~8.10%.** Firmed from +5.45% at open. Next earnings ~Oct. |
| DE | 22 | 589.82 | 603.08 | +37.40→+291.72 | +2.25% | **10% TRAILING (GTC)**, floor **579.591**, hwm 643.99 | 2026-06-04 | Deere — Q2 beat, FY26 guide raised, right-to-repair settlement cleared. $1.62 div payable Aug 10. Off-cycle; next report ~Aug 20. **RECOVERED: the open's −3.18%/+0.29% scare eased — now +2.25%, floor 579.591 ~2.2% below entry. NO thesis break — sentiment/ag-softness only.** Cushion ~3.90% (tightest but restored). |

**Open positions: 3 of 5 (two slots OPEN).** **Buys used this week: 0 of 3.** **Cash buffer: ~59.17%.** Position sizes (on midday equity $101,688.72): LLY 16.02%, DE 13.05%, JPM 11.76% — all under the 20% cap.

## Stop-management state (all 3 confirmed RESTING via open-orders query, nested=true) — ALL 10% TRAILING GTC, floors/hwm unchanged from 7/29 close (no new highs today → no ratchet)
- **LLY 10% trailing** `6016a7e7-faac-4e93-82e7-851abf30eca8` — floor **1124.505**, hwm 1249.45. Live 1163.355, **cushion ~3.34%.**
- **JPM 10% trailing** `8a937ff6-164c-4384-8cf8-c000d4106a60` — floor **323.307**, hwm 359.23. Live 351.82, cushion ~8.10%.
- **DE 10% trailing** `dcdd84e5-6b94-4943-aa5b-3d3a299cbfce` — floor **579.591**, hwm 643.99. Live 603.08, cushion ~3.90% (tightest; DE recovered to +2.25% today). All shares show qty_available:0 → reserved by their resting stops.

## +5% conversion check (midday)
- LLY +7.87% and JPM +6.71% both ≥+5% but ALREADY on 10% trailing stops → **trailing stops are never reverted to hard stops.** DE +2.25% below +5% but also already trailing. **Zero hard stops remain → no −7%→trailing conversion needed.** No action.

## Watch / next (next routine: **Thu 7/30 market-close ~15:00 CT** — owns the mandatory daily "How we're doing" update + Telegram)
- **DE — cushion restored to ~3.90%** after the open scare. Round-tripped and re-recovered on ag sentiment (NOT a new legal/guidance/exec event). Trailing stop 579.591 handles any break automatically. Only act manually on a real thesis break — none present.
- **LLY — pulled back from +9.22% (open) to +7.87%**, cushion ~3.34%. Quiet, intact, ~Aug 5 earnings. No action.
- **Tonight: AAPL + AMZN report AMC.** We own neither — a read on tape sentiment, not a catalyst for our non-tech book.
- **Intraday divergence:** SPY bounced (+1.43%) on a benign PCE/GDP while our pharma/ag lag → we're behind SPY intraday today. Early-session noise; the close owns the number.
- **Bench (from pre-market):** LMT ~63 (VERIFIED 7/23 beat-and-raise but chasing a +14%-week pop — do not chase), UNH 64, NOW 63, GS 63, DLR 60, DOV 58, JNJ 58, ETN 56, ABT 55, OXY 55, STX 53, MS 52, AXP ~50, V ~50, AMGN/CB/CVS/VST 50, PANW 35. None clears ≥70.
- **Cash-drag re-eval (ARMED — this IS the pre-committed test week):** DECISION at **Friday's weekly review.** Carry the full week's tape. Nuance: SPY fell −1.52% on 7/29, so cash has been *beating* the market this week — the "while SPY keeps rising" half of the trigger is not cleanly firing.

## Recent closes (last 5)

| Symbol | Exit Date | Shares | Entry | Exit | P/L $ | P/L % | Reason |
|---|---|---|---|---|---|---|---|
| GE | 2026-07-16 | 45 | 329.63 | 344.54 | +670.95 | +4.52% | 10% trailing stop fired (post-Q2-earnings give-back caught the profit; no verified thesis break) |
| ETN | 2026-07-02 | 24 | 401.5425 | 392.75 | −211.02 | −2.19% | 10% trailing stop fired (beta/thin pre-holiday tape, not thesis break) |
| NVDA | 2026-06-05 | 55 | 220.15 | 204.7158 | −848.88 | −7.01% | −7% hard stop fired (macro/NFP semis selloff, not thesis break) |
| NVDA | 2026-05-04 | 25 | 201.38 | ~195.02 | −159.04 | −3.16% | 10% trailing stop fired (round-trip) |

---
*Overwrite this file every routine. Keep it a live snapshot, not a log.*
