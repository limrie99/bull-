# Portfolio

**Last updated:** 2026-08-18 08:35 CT — **MARKET OPEN (Tue).** Market CONFIRMED OPEN via /v2/clock (is_open:true, 09:32 ET, next_close 16:00 ET). Live marks. Account (live): equity **$101,223.43**, cash **$36,641.95** (~36.20%), long_market_value **$64,581.48** (~63.80%), buying_power $327,395.94, status ACTIVE, trading_blocked false. `last_equity` (Mon 8/17 close) $101,036.19 → intraday **+$187.24 / +0.19%**. **NO TRADES this routine** — nothing clears the ≥70 gate at the live open (board entry-blocked, no fresh catalyst); no sell trigger; no hard→trailing conversion pending. Conviction sleeve **3 of 5 (two slots OPEN); weekly conviction buys 0/3.** All three stops re-confirmed RESTING (open-orders nested=true, exactly 3, SPY zero). Zero overnight fills (closed-orders since 8/17 = EMPTY). **Inbox: nothing pending.** **DE hold-through-print FINALIZED = HOLD (do NOT trim, do NOT add).**

## Benchmark scorecard (market-open intraday — 2026-08-18)
- **Intraday (vs Mon 8/17 close):** book **+0.19%** ($101,036.19 → $101,223.43) vs **SPY −0.52%** (Mon close 772.62 → latest 768.61) → **intraday alpha ~+0.70 pt.** Down-tape morning; we're green because JPM/DE firmed and LLY recovered.
- **WTD base = Fri 8/14 close, portfolio $101,378.01 / SPY 776.30.** WTD so far: book −0.15% vs SPY −0.99% → **WTD alpha ~+0.84 pt** (intraday, week young). Cumulative alpha since 5/29 base ≈ **−0.9 pt**.
- Macro this morning: **RISK-OFF LEANING** — semis-led futures pullback, 10Y ~4.74% near highs, oil ~$85. No binary print today; Jackson Hole is NEXT week.

## Snapshot (live marks — 2026-08-18 09:32 ET)
- **Equity $101,223.43.** Total since $100K start: **+1.22%.**
- **Net open unrealized: +$1,108.36** (JPM +1,096.48, DE +229.02, LLY −83.82, SPY −133.32).
- **Cash 36.20%** — well above the 10–20% minimum buffer.
- Quiet, constructive open; theses all intact. LLY recovered to −0.58% (from −1.82% pre-open). The day's read: HD earnings (consumer) digesting + a soft, yield-pressured tape.

## Open positions (3 conviction stocks + 1 index-floor sleeve) — live marks 8/18 09:32 ET
| Symbol | Shares | Avg Cost | Price | P/L $ | P/L % | Stop | Entry Date | Thesis (1 line) |
|---|---|---|---|---|---|---|---|---|
| JPM | 34 | 329.695588 | 361.94 | +1,096.48 | +9.78% | **10% TRAILING (GTC)**, floor **329.85**, hwm 366.5 | 2026-06-29 | JPMorgan — $50B buyback + div hike; largest US bank; Q2 beat. Consensus Buy avg PT ~$372–373; WF $390 OW stands. Next earnings ~Oct. **Cushion ~8.87%.** |
| DE | 22 | 589.82 | 600.23 | +229.02 | +1.76% | **10% TRAILING (GTC)**, floor **579.591**, hwm 643.99 | 2026-06-04 | Deere — Q2 beat, FY26 guide raised, ag/onshoring tailwind. **Q3 CONFIRMED Thu Aug 20 BMO 9:00 CT** (cons ~$4.72 EPS / ~$10.8B rev, rev DOWN YoY = low bar; base case = reaffirm FY26 $4.5–5.0B). Analyst trims into print (JPM $590→$570, Evercore $641→$632). **HOLD-THROUGH-PRINT FINALIZED = HOLD; do NOT trim/add. Cushion ~3.44% (tightest trailing).** |
| LLY | 12 | 1209.84 | 1202.86 | −83.82 | −0.58% | **−7% HARD STOP (GTC) @ 1125.15** | 2026-08-12 | Eli Lilly — Q2 beat-and-raise (RAISED FY26 EPS $35.50–36.50) + GLP-1/obesity tailwind. Recovered to −0.58% at open (from −1.82% pre-open); drift = post-earnings consolidation, no LLY-specific/Novo news. Conviction ~73 (B+). Hard stop converts to 10% trailing once +5% (~$1,270.33). **Cushion ~6.46%.** |
| SPY | 32 | 772.921250 | 768.75 | −133.32 | −0.54% | **NONE — index-floor sleeve, deliberate no-stop carve-out** | 2026-08-10 (t1) / 2026-08-11 (t2) | S&P 500 market floor (Lauren-approved Option B), COMPLETE. Own sleeve, EXEMPT from ≤20%/max-5/max-3-per-week caps; NO −7%/trailing stop. Buy-and-hold-the-market. |

**Conviction sleeve: 3 of 5 (two slots OPEN).** **Conviction buys used this week: 0 of 3** (the SPY floor does NOT consume this budget). **Cash buffer: ~36.20%.** Position sizes (on equity $101,223.43): JPM ~12.16%, DE ~13.05%, LLY ~14.26%, SPY ~24.30% (index sleeve — exempt from the 20% single-position cap by policy).

## Closed THIS WEEK
- **None** (week of Mon 8/17). Last close: LLY trailing-stop 7/31 (+$627), since re-entered 8/12.

## Stop-management state (re-confirmed RESTING via open-orders, nested=true — 8/18 09:32 ET)
- **JPM 10% trailing** `8a937ff6-164c-4384-8cf8-c000d4106a60` — hwm **366.5**, floor (stop_price) **329.85**, status new (resting). Price 361.94, cushion ~8.87%. Below hwm → no ratchet. qty 34.
- **DE 10% trailing** `dcdd84e5-6b94-4943-aa5b-3d3a299cbfce` — hwm **643.99**, floor (stop_price) **579.591**, status new (resting). Price 600.23, cushion ~3.44%. Below hwm → no ratchet. qty 22.
- **LLY −7% hard stop** `f50e3c39-0719-497e-8ccc-6006e6afa290` — stop_price **1125.15** (=1209.84×0.93), GTC, status new (resting). Price 1202.86 (−0.58% from entry). **Converts to a 10% trailing stop once LLY is +5% in profit** (trigger ~$1,270.33). Cushion to stop ~6.46%. qty 12.
- **SPY — NO STOP by design** (index-floor sleeve carve-out). qty_available 32 (unencumbered). Intentional per the 8/7 policy; do NOT place a stop on the floor.

## Risk checks (market-open, live)
- **(a) Any position −7% or worse un-stopped?** NO. JPM +9.78%, DE +1.76%, LLY −0.58% (well above its −7% hard stop @ 1125.15), SPY −0.54%. **→ No sell triggered.**
- **(b) Any position +5%+ needing hard→trailing conversion?** NO conversion pending. JPM & DE already on 10% trailing GTC; LLY −0.58% (below +5%) on its −7% hard stop as designed; SPY carries no stop by policy. **(Standing task: convert LLY's hard stop → 10% trailing once it tags ~+5% / ~$1,270.33.)**
- **(c) Daily loss cap:** intraday +0.19%, not tripped. Moot — no buys placed.

## Watch / next (next routine: **midday Tue 8/18**)
- **DE — Q3 Thu Aug 20 BMO. DECISION FINALIZED = HOLD through the print** (do NOT trim, do NOT add). De-risked expectations (analysts trimmed, rev down YoY = low bar), thesis intact, trailing floor 579.591 (~3.4% below) is the safety net. Tail risk = a severe guide miss gapping down through the stop overnight (one contained ~13% position, not book-threatening). Revisit only if a warning surfaces Wed.
- **LLY — recovered to −0.58%, thesis intact.** Cushion ~6.46% to the 1125.15 hard stop; convert to 10% trailing at +5% (~$1,270.33).
- **JPM — cushion ~8.87%**, healthy; below hwm so floor unchanged; next earnings ~Oct.
- **HD earnings today (BMO)** — the consumer read; watch the tape reaction.
- **Conviction gate: EMPTY (~52nd effectively-empty scan).** Board is entry-blocked, not thesis-blocked: AMGN/ANET/ABT/ETN/PWR all chases (extended); AMAT below-trend + high-beta semi into risk-off; ABBV cleanest (+2.2%) but only ~1 real signal. Two slots open, ~36% cash = room for ~1 buy before trimming the floor.

## Recent closes (last 5)
| Symbol | Exit Date | Shares | Entry | Exit | P/L $ | P/L % | Reason |
|---|---|---|---|---|---|---|---|
| LLY | 2026-07-31 | 14 | 1078.46 | 1123.27 | +627.34 | +4.15% | 10% trailing stop fired (give-back from ~1249 hwm; no thesis break). **RE-ENTERED 8/12 on the verified beat-and-raise.** |
| GE | 2026-07-16 | 45 | 329.63 | 344.54 | +670.95 | +4.52% | 10% trailing stop fired (post-Q2-earnings give-back caught the profit; no verified thesis break) |
| ETN | 2026-07-02 | 24 | 401.5425 | 392.75 | −211.02 | −2.19% | 10% trailing stop fired (beta/thin pre-holiday tape, not thesis break) |
| NVDA | 2026-06-05 | 55 | 220.15 | 204.7158 | −848.88 | −7.01% | −7% hard stop fired (macro/NFP semis selloff, not thesis break) |
| NVDA | 2026-05-04 | 25 | 201.38 | ~195.02 | −159.04 | −3.16% | 10% trailing stop fired (round-trip) |

---
*Overwrite this file every routine. Keep it a live snapshot, not a log.*
