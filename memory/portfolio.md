# Portfolio

**Last updated:** 2026-07-31 16:00 CT — **WEEKLY REVIEW complete (Fri; market CONFIRMED CLOSED via /v2/clock, next_open 2026-08-03 09:30 ET).** Official end-of-day marks from Alpaca. Account: equity **$100,893.16** (official close scorecard), cash **$75,893.56** (~75.22%), long_market_value ~**$25,000**, status ACTIVE. **OFFICIAL WTD (base Fri 7/24 close $102,740.86 / SPY 738.90 → Fri 7/31 close $100,893.16 / SPY 746.79): port −1.80%, SPY +1.07% → WTD alpha −2.87% ❌** (2nd-worst week of run; cause = ~75% cash on a rising tape). Cumulative alpha since 5/29 now **+2.32 pts** (halved from +5.22). **Grade C.** Book **2 of 5 positions (three slots OPEN).** Only trade this week = LLY trailing-stop exit 7/31 (+$627 WIN). Both remaining stops re-confirmed RESTING. **ESCALATION: the pre-committed cash trigger FIRED (empty gate WHILE SPY rose) → I sent Lauren a forced A/B cash decision (A: hold; B: add S&P 500 market floor) in messages.md; awaiting her reply in inbox.md; default A (hold) if no answer by Mon.** **Inbox: nothing pending.**

## Scorecard (CLOSE 2026-07-31 — OFFICIAL end-of-day number)
- **Closing equity $100,893.16.** Total since $100K start: **+0.89%.**
- **Day P/L −$561.44 / −0.55%** vs yesterday's close $101,454.60 — mild give-back (DE −1.13% on the day was the main drag; JPM +0.27% steady).
- **SPY day +0.70%** (741.63 → 746.79). **Alpha today −1.25%** — we lagged. Cash drag: with ~75% in cash we can't keep pace on a broad up day, and DE softened.
- **WTD (base Fri 7/24 close eq $102,740.86 / SPY 738.90 → 7/31 close $100,893.16 / SPY 746.79):** port **−1.80%**; SPY **+1.07%** → **WTD alpha −2.87% ❌ — FINALIZED by the weekly review (grade C).** Cumulative alpha since 5/29 halved +5.22 → **+2.32**.
- **Realized this week: LLY +$627.34** (7/31 trailing-stop exit). **Net open unrealized: +$813.91** (JPM +751.21, DE +62.70 — official close marks).
- **SPY refs:** 746.79 (close 7/31), 741.63 (7/30 close), new-week base 738.90 (7/24 close).

## Open positions (2 of 5 — three slots OPEN) — OFFICIAL CLOSE marks 7/31

| Symbol | Shares | Avg Cost | Mark (close) | P/L $ | P/L % | Stop | Entry Date | Thesis (1 line) |
|---|---|---|---|---|---|---|---|---|
| JPM | 34 | 329.695588 | 351.79 | +751.21 | +6.70% | **10% TRAILING (GTC)**, floor **323.307**, hwm 359.23 | 2026-06-29 | JPMorgan — $50B buyback + div hike; largest US bank; Q2 (7/14) beat; DB UPGRADE Hold→Buy PT $375. sev 2 (macro sector noise, not company). **Cushion ~8.10% (widest).** Next earnings ~Oct. |
| DE | 22 | 589.82 | 592.67 | +62.70 | +0.48% | **10% TRAILING (GTC)**, floor **579.591**, hwm 643.99 | 2026-06-04 | Deere — Q2 beat, FY26 guide raised, right-to-repair settlement cleared (reaffirmed). $1.62 div payable Aug 10. Off-cycle; next report ~Aug 20. sev 2 (ag-commodity softness = sentiment; net-income outlook MAINTAINED). **Cushion ~2.21% (tightest); DE fell −1.13% today.** |

**Open positions: 2 of 5 (three slots OPEN).** **Buys used this week: 0 of 3.** **Cash buffer: ~75.22%.** Position sizes (on closing equity $100,893.16): DE 12.92%, JPM 11.85% — both well under the 20% cap.

## Closed THIS WEEK
- **LLY — 10% trailing stop AUTO-FIRED, sold 14 @ 1123.27 (order 6016a7e7), 10:08 ET 7/31.** Realized **+$627.34 / +4.15%** (entry 1078.46, 2026-06-01). LLY ran to hwm 1249.45, pulled back 10% to floor 1124.505, executed 1123.27. Bounced to ~1143 same day → **normal give-back, NOT a thesis break.** Bonus: removed LLY's ~Aug 5 earnings risk with a locked gain. Freed ~$15,726 cash. (Recorded in full at midday.)

## Stop-management state (both remaining re-confirmed RESTING via open-orders query, nested=true) — ALL 10% TRAILING GTC, floors/hwm UNCHANGED (no new highs today → no ratchet)
- **JPM 10% trailing** `8a937ff6-164c-4384-8cf8-c000d4106a60` — floor **323.307**, hwm 359.23, status new (resting). Close 351.79, cushion ~8.10% (widest).
- **DE 10% trailing** `dcdd84e5-6b94-4943-aa5b-3d3a299cbfce` — floor **579.591**, hwm 643.99, status new (resting). Close 592.67, cushion ~2.21% (tightest). Both positions show qty_available:0 → shares reserved by their resting stops.
- **LLY stop `6016a7e7`** — FILLED/closed earlier today (see above); no longer resting.

## Risk checks (close)
- **(a) Any position −7% or worse un-stopped?** NO. JPM +6.70%, DE +0.48%. Nothing near a hard-stop trigger; both on trailing stops above their floors.
- **(b) Any position +5%+ needing hard→trailing conversion?** JPM +6.70% ≥ +5% but ALREADY on a 10% trailing stop → trailing stops are never reverted. DE +0.48% below +5% and also already trailing. **Zero hard stops in book → no conversion needed.**
- **(c) Daily loss cap:** day P/L −0.55% vs yesterday's close — well within the −3% cap. (Moot for new buys anyway — nothing clears the gate.)

## Watch / next (next routine: **weekly review** — owns cash-drag/gate/deployment decision + official WTD alpha)
- **Cash-drag decision (ARMED — this IS the pre-committed test week):** the LLY exit + no redeployment leaves us **~75% cash, 2 positions, three open slots.** This week we lagged (WTD alpha ≈ −2.87%) precisely because cash can't ride a rising tape — the exact pattern the review must weigh. The gate is functioning (correctly held chase-entry LMT and fell-on-print NOC); the open question is deployment/sizing, NOT lowering the ≥70 bar. **Weekly review (owned by that routine) decides.** Weekly buy cap resets Monday 8/3 (0/3 → fresh 3).
- **DE — cushion ~2.21% (tightest, tightened today on the −1.13% move)**, floor 579.591 sits ~1.7% BELOW the 589.82 entry (a continued slide exits near break-even). No thesis break (ag-commodity softness = sentiment; right-to-repair already settled/reaffirmed). Trailing floor handles any real break automatically; do NOT pre-empt on price. $1.62 div payable Aug 10; next report ~Aug 20.
- **JPM — cushion ~8.10% (widest)**, healthy and quiet; thesis intact (record Q2, $50B buyback, DB Buy PT $375). Next earnings ~Oct.
- **No buy candidate cleared the gate (~38th straight empty scan).** LMT ~62 (extended, wants a pullback to low-$540s) and NOC ~55 (fell on print, near 52-wk lows — fails uptrend/no-knife-catch) both fail on entry. ETN reported 7/31 BMO — re-check post-print at weekly review.
- **Bench:** UNH ~64, NOW 63, GS 63, LMT ~62, DLR 60, DOV 58, JNJ 58, ETN 56, NOC ~55, ABT 55, OXY 55, STX 53, MS 52, AXP/V ~50, AMGN/CB/CVS/VST 50, PANW 35. None clears ≥70.

## Recent closes (last 5)

| Symbol | Exit Date | Shares | Entry | Exit | P/L $ | P/L % | Reason |
|---|---|---|---|---|---|---|---|
| LLY | 2026-07-31 | 14 | 1078.46 | 1123.27 | +627.34 | +4.15% | 10% trailing stop fired (give-back from ~1249 hwm; no thesis break — bounced to ~1143 same day; also removed Aug 5 earnings risk) |
| GE | 2026-07-16 | 45 | 329.63 | 344.54 | +670.95 | +4.52% | 10% trailing stop fired (post-Q2-earnings give-back caught the profit; no verified thesis break) |
| ETN | 2026-07-02 | 24 | 401.5425 | 392.75 | −211.02 | −2.19% | 10% trailing stop fired (beta/thin pre-holiday tape, not thesis break) |
| NVDA | 2026-06-05 | 55 | 220.15 | 204.7158 | −848.88 | −7.01% | −7% hard stop fired (macro/NFP semis selloff, not thesis break) |
| NVDA | 2026-05-04 | 25 | 201.38 | ~195.02 | −159.04 | −3.16% | 10% trailing stop fired (round-trip) |

---
*Overwrite this file every routine. Keep it a live snapshot, not a log.*
