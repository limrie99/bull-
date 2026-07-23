# Portfolio

**Last updated:** 2026-07-23 15:05 CT (16:01 ET) — **MARKET-CLOSE routine (Thu, market CLOSED, `is_open:false`, next open Fri 7/24 09:30 ET). OFFICIAL EOD SCORECARD.** Closing Alpaca: equity **$102,079.16**, cash **$60,167.78** (~58.9%), long_market_value **$41,911.38** (~41.1%). Baseline = 7/22 close of record **$101,673.76** (`last_equity` returned "0" again — Alpaca quirk; portfolio-history API is lagging one day, its last settled value $101,272.70 is the **7/21** close per memory, NOT 7/22, so carrying the 7/22 close routine's recorded $101,673.76 as authoritative baseline). Book **3 of 5 positions** (two slots OPEN). **Weekly buys 0 of 3.** **ACTIONS THIS RUN: NONE — no buys, no sells, no stops fired, no stop changes.** Closed-orders query today = **0**; all 3 stops confirmed RESTING (open-orders `status:new`, ALL 10% TRAILING, zero hard stops), IDs unchanged. **Inbox: nothing pending.** **28th straight effectively-empty scan on the strict 2-signal + Conviction≥70 gate** (AXP Q2 tomorrow 7/24 BMO = the decision point — do NOT pre-position into the binary).

## Scorecard (OFFICIAL — market-close owns the daily number)
- **Day P/L: +$405.40 / +0.40%** (equity $102,079.16 vs 7/22 close $101,673.76).
- **SPY: 738.06 close vs 747.49 (7/22 close) = −1.26%.** **Alpha today = +1.66%** — we were UP while a tech-led tape fell hard (GOOGL/TSLA/IBM AI-capex selloff, none of it ours); ~59% cash + zero tech + LLY strengthening on its own = the defensive posture doing exactly its job on a down day.
- **Total since $100K start: +2.08%.**
- **Week-to-date (base 7/17 close eq $101,411.58 / SPY 743.28):** port **+0.66%**, SPY **−0.70%**, **alpha WTD +1.36%** — we now LEAD SPY on the week. The down-tech week rewards our cash-heavy, non-tech posture (the mirror image of grind-up weeks when cash costs us).
- **SPY refs:** 738.06 (7/23 close); 747.49 (7/22 close); 748.155 (7/21 close); 743.28 (7/17 close = week base); 742.15 (7/20 close).
- Net open unrealized **+$2,627.25** (LLY +1,495.90, JPM +686.95, DE +444.40).

## Open positions (3 of 5 — two slots OPEN) — CLOSING marks 7/23

| Symbol | Shares | Avg Cost | Close Mark | P/L $ | P/L % | Stop | Entry Date | Thesis (1 line) |
|---|---|---|---|---|---|---|---|---|
| LLY | 14 | 1078.46 | 1185.31 | +1495.90 | +9.91% | **10% TRAILING (GTC)**, floor **1124.505**, hwm **1249.45** | 2026-06-01 | Eli Lilly — Q1 beat + raised guide + oral GLP-1 (orforglipron, EBGLYSS). **STRENGTHENED 7/23: retatrutide Phase 3 data + Q1-2027 FDA filing plan [VERIFIED]** — biggest single-name mover, closed +9.91%. Earnings ~Aug 5. sev 3. Most macro-insulated. **Cushion ~5.13% above floor** (hwm 1249.45 unchanged; mark below prior high, floor static — mechanics only). |
| JPM | 34 | 329.695588 | 349.90 | +686.95 | +6.13% | **10% TRAILING (GTC)**, floor **316.116**, hwm **351.24** | 2026-06-29 | JPMorgan — $50B buyback + div hike; largest US bank. Q2 (7/14) VERIFIED BEAT. Higher 10Y (~4.63%) mild NIM+. Thesis INTACT sev 3. Cushion ~9.66% (widest). Next earnings ~Oct. |
| DE | 22 | 589.82 | 610.02 | +444.40 | +3.42% | **10% TRAILING (GTC)**, floor **575.073**, hwm 638.97 | 2026-06-04 | Deere — big Q2 beat, FY26 guide raised, right-to-repair settlement cleared. $1.62 div payable Aug 10. Off-cycle; next report ~Aug 20. INTACT **sev 2 (watch)**. **Most tariff-exposed — Section 122 blanket tariff auto-expires 12:01am 7/24 tonight (base case SUNSET = mild tailwind, mechanism unconfirmed); cushion ~5.73%.** |

**Open positions: 3 of 5 (two slots OPEN).** **Buys used this week: 0 of 3.** **Cash buffer: ~58.9%.** Position sizes: LLY 16.3%, DE 13.1%, JPM 11.7% — all under the 20% cap.

## Stop-management state (all 3 confirmed RESTING via open-orders query, status `new`) — ALL 10% TRAILING

- **LLY 10% trailing** `6016a7e7-faac-4e93-82e7-851abf30eca8` — floor **1124.505**, hwm **1249.45**. Mark 1185.31, **cushion ~5.13% above floor** (mark below recorded hwm, so floor static — a tag would sell +9.9% above cost; thesis strengthened either way).
- **JPM 10% trailing** `8a937ff6-164c-4384-8cf8-c000d4106a60` — floor **316.116**, hwm **351.24**. Mark 349.90, cushion ~9.66% (widest).
- **DE 10% trailing** `dcdd84e5-6b94-4943-aa5b-3d3a299cbfce` — floor **575.073**, hwm 638.97. Mark 610.02, cushion ~5.73% (watch into 7/24 Section 122 tariff expiry).

## +5% conversion check (close)
- LLY +9.91% and JPM +6.13% — both ALREADY on 10% trailing stops. DE +3.42% (below +5% but already trailing since prior entry-management). **Zero hard stops remain in the book → no −7%→trailing conversion needed this run.** All three resting/trailing; no action.

## Watch / next (next routine: **Fri 7/24 pre-market — then market-open owns the AXP re-score**)

- **AXP Q2 Fri 7/24 BMO = THE decision point for the bench** (cons EPS ~$4.40 / rev ~$19.7B). A clean beat-and-raise adds signal #1 and could lift it over 70. Do NOT pre-position into the binary; let it resolve, then re-score.
- **Section 122 tariff auto-expires 12:01am 7/24 (tonight)** — watch DE headlines Fri (base case sunset = mild tailwind). Cushion ~5.73%, mechanics only.
- **LLY strengthened +9.91%** on retatrutide follow-through; cushion ~5.13% above floor — mechanics only, a floor tag sells itself well above cost.
- **FOMC 7/28–29** (hold priced, hike tail). Keep dry powder into week's end.
- **Bench:** UNH 65 (7/16 beat-raise spent + regulatory overhang), AXP 65 (JPMorgan upgrade 7/13; 7/24 earnings = binary decision point), GS 63 (blowout Q2 + uptrend but chasing near ATH, ~1.5 signals), JNJ 58, ABT 55 (clean beat-raise but downtrend/knife-catch), OXY 55, STX 53 (2 soft signals but high-beta + earnings within days), MS 52, V/AMGN/CB/CVS/VST 50; PANW 35.

## Recent closes (last 5)

| Symbol | Exit Date | Shares | Entry | Exit | P/L $ | P/L % | Reason |
|---|---|---|---|---|---|---|---|
| GE | 2026-07-16 | 45 | 329.63 | 344.54 | +670.95 | +4.52% | 10% trailing stop fired (post-Q2-earnings give-back caught the profit; no verified thesis break) |
| ETN | 2026-07-02 | 24 | 401.5425 | 392.75 | −211.02 | −2.19% | 10% trailing stop fired (beta/thin pre-holiday tape, not thesis break) |
| NVDA | 2026-06-05 | 55 | 220.15 | 204.7158 | −848.88 | −7.01% | −7% hard stop fired (macro/NFP semis selloff, not thesis break) |
| NVDA | 2026-05-04 | 25 | 201.38 | ~195.02 | −159.04 | −3.16% | 10% trailing stop fired (round-trip) |

---
*Overwrite this file every routine. Keep it a live snapshot, not a log.*
