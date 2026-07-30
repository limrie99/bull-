# Portfolio

**Last updated:** 2026-07-30 15:00 CT — **MARKET CLOSE (Thu, official daily number).** Closing marks from Alpaca. Account: equity **$101,483.02**, cash **$60,167.78** (~59.29%), long_market_value **$41,315.24** (~40.71%), buying_power $356,353.79, status ACTIVE. **NB:** Alpaca `last_equity`/`sma`/portfolio-history all still read the STALE **$103,482.04** (7/28 close — never rolled to the 7/29 official close), so day-P/L off Alpaca fields is wrong. Against the real 7/29 close $102,256.39 (from yesterday's research-log EOD), today closed **−$773.37 / −0.76%**. Book **3 of 5 positions (two slots OPEN)**. **ACTIONS THIS RUN: NONE** — no buys (~38th straight empty scan on the 2-signal + Conviction≥70 gate), no sells, no stop conversions, 0 fills. All 3 stops confirmed RESTING (10% trailing GTC). **Inbox: nothing pending.**

## Scorecard (CLOSE 2026-07-30 — OFFICIAL)
- **Closing equity $101,483.02.** Total since $100K start: **+1.48%.**
- **Day P/L −$773.37 / −0.76%** vs the real 7/29 close $102,256.39 (do NOT use the stale `last_equity` $103,482.04).
- **SPY day +1.65%** (close 741.63 vs 7/29 close 729.57; IEX daily bars, matches latest trade 741.63 @ 15:59 ET). **Alpha today −2.41 pts** — our worst-lag day of the stretch: SPY ripped a tech-led recovery while our pharma/ag book sat it out (LLY −4.38%, DE −1.88%; only JPM +1.78%).
- **WTD (base Fri 7/24 close eq $102,740.86 / SPY 738.90):** port **−1.22%**, SPY **+0.37%**, **alpha WTD −1.59 pts.** Official WTD lands Friday's weekly review.
- **Cumulative alpha since 5/29 resume ~+3.3 pts** (the SPY bounce two days running has chewed through most of the cushion).
- **Net open unrealized: +$2,031.11** (LLY +1,099.56, JPM +719.25, DE +212.30 — closing marks).
- **SPY refs:** 741.63 (7/30 close), 729.57 (7/29 close), 740.795 (7/28 close); new-week base 738.90 (7/24 close).

## Open positions (3 of 5 — two slots OPEN) — CLOSING marks 7/30

| Symbol | Shares | Avg Cost | Mark (close) | P/L $ | P/L % | Stop | Entry Date | Thesis (1 line) |
|---|---|---|---|---|---|---|---|---|
| LLY | 14 | 1078.46 | 1157.00 | +1099.56 | +7.28% | **10% TRAILING (GTC)**, floor **1124.505**, hwm 1249.45 | 2026-06-01 | Eli Lilly — Q1 beat + raised guide + oral GLP-1 (orforglipron) pipeline; retatrutide Ph3. Earnings **~Aug 5**. sev 1, intact. **Cushion ~2.81% (tightest).** Fell −4.38% today on a rotation OUT of defensive pharma INTO tech — price/sentiment, no thesis break. |
| JPM | 34 | 329.695588 | 350.85 | +719.25 | +6.42% | **10% TRAILING (GTC)**, floor **323.307**, hwm 359.23 | 2026-06-29 | JPMorgan — $50B buyback + div hike; largest US bank; Q2 (7/14) beat; DB UPGRADE Hold→Buy PT $375. sev 1, quiet. **Cushion ~7.85%.** +1.78% today — only green name; firmed with the risk-on tape. Next earnings ~Oct. |
| DE | 22 | 589.82 | 599.47 | +212.30 | +1.64% | **10% TRAILING (GTC)**, floor **579.591**, hwm 643.99 | 2026-06-04 | Deere — Q2 beat, FY26 guide raised, right-to-repair settlement cleared. $1.62 div payable Aug 10. Off-cycle; next report ~Aug 20. −1.88% today (ag softness), no thesis break. **Cushion ~3.32%** (floor ~1.7% below entry → a stop exits near break-even). |

**Open positions: 3 of 5 (two slots OPEN).** **Buys used this week: 0 of 3.** **Cash buffer: ~59.29%.** Position sizes (on closing equity $101,483.02): LLY 15.96%, DE 13.00%, JPM 11.75% — all under the 20% cap.

## Stop-management state (all 3 confirmed RESTING via open-orders query, nested=true) — ALL 10% TRAILING GTC, floors/hwm unchanged (no new highs today → no ratchet)
- **LLY 10% trailing** `6016a7e7-faac-4e93-82e7-851abf30eca8` — floor **1124.505**, hwm 1249.45. Close 1157.00, **cushion ~2.81% (tightest).**
- **JPM 10% trailing** `8a937ff6-164c-4384-8cf8-c000d4106a60` — floor **323.307**, hwm 359.23. Close 350.85, cushion ~7.85%.
- **DE 10% trailing** `dcdd84e5-6b94-4943-aa5b-3d3a299cbfce` — floor **579.591**, hwm 643.99. Close 599.47, cushion ~3.32%. All shares show qty_available:0 → reserved by their resting stops.

## +5% conversion check (close)
- LLY +7.28% and JPM +6.42% both ≥+5% but ALREADY on 10% trailing stops → **trailing stops are never reverted to hard stops.** DE +1.64% below +5% but also already trailing. **Zero hard stops remain → no −7%→trailing conversion needed.** No action.

## Watch / next (next routine: **Fri 7/31 pre-market**, then Friday **weekly review** — owns the cash-drag/gate decision)
- **LLY — tightest cushion ~2.81%** after a −4.38% pharma-rotation day, and **earnings ~Aug 5** (within the 3-day earnings window soon). No thesis break — this is money rotating out of defensives into tech, not a Lilly-specific problem. The trailing floor 1124.505 handles any real break automatically. Do NOT pre-empt on a price move; act only on a verified thesis break.
- **Two-sided cash lesson, in the open:** the ~59% cash barbell that beat SPY on the 7/29 down day (+0.33 alpha) cost us today (−2.41 alpha) as SPY rallied and we didn't participate. That's the whole trade-off of dry powder — it dampens both directions.
- **Cash-drag re-eval (ARMED — this IS the pre-committed test week):** DECISION at **Friday's weekly review.** Today is exactly the "SPY rising while we sit in cash and lag" half of the trigger firing — carry it into the review. Weekly buy cap resets 0/3 Monday; still 0/3 this week.
- **Bench (from pre-market):** LMT ~63, UNH 64, NOW 63, GS 63, DLR 60, DOV 58, JNJ 58, ETN 56, ABT 55, OXY 55, STX 53, MS 52, AXP/V ~50, AMGN/CB/CVS/VST 50, PANW 35. None clears ≥70.

## Recent closes (last 5)

| Symbol | Exit Date | Shares | Entry | Exit | P/L $ | P/L % | Reason |
|---|---|---|---|---|---|---|---|
| GE | 2026-07-16 | 45 | 329.63 | 344.54 | +670.95 | +4.52% | 10% trailing stop fired (post-Q2-earnings give-back caught the profit; no verified thesis break) |
| ETN | 2026-07-02 | 24 | 401.5425 | 392.75 | −211.02 | −2.19% | 10% trailing stop fired (beta/thin pre-holiday tape, not thesis break) |
| NVDA | 2026-06-05 | 55 | 220.15 | 204.7158 | −848.88 | −7.01% | −7% hard stop fired (macro/NFP semis selloff, not thesis break) |
| NVDA | 2026-05-04 | 25 | 201.38 | ~195.02 | −159.04 | −3.16% | 10% trailing stop fired (round-trip) |

---
*Overwrite this file every routine. Keep it a live snapshot, not a log.*
