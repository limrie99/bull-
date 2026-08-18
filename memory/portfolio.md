# Portfolio

**Last updated:** 2026-08-18 12:05 CT — **MIDDAY (Tue).** Market CONFIRMED OPEN via /v2/clock (is_open:true, 13:02 ET, next_close 16:00 ET). Live marks. Account (live): equity **$101,162.91**, cash **$36,641.95** (~36.22%), long_market_value **$64,520.96** (~63.78%), buying_power $327,226.49, status ACTIVE. `last_equity` (Mon 8/17 close) $101,036.19 → intraday **+$126.72 / +0.125%** (up on the day). **NO TRADES this routine** — no sell trigger, no hard→trailing conversion pending, no midday buy (no breaking catalyst; board entry-blocked). Conviction sleeve **3 of 5 (two slots OPEN); weekly conviction buys 0/3.** All three stops re-confirmed RESTING (open-orders nested=true, exactly 3; SPY zero). Zero fills since the open (book unchanged from 09:32 snapshot). **Inbox: nothing pending.** **DE hold-through-print FINALIZED = HOLD (do NOT trim, do NOT add).**

## Benchmark scorecard (midday intraday — unofficial; close routine owns official)
- **Intraday (vs Mon 8/17 close):** book **+0.125%** ($101,036.19 → $101,162.91) vs **SPY −0.554%** (Mon close 772.67 → latest 768.39) → **intraday alpha ~+0.68 pt.** Down-tape day; we're green because JPM firmed (+9.23%), DE (+0.80%) and LLY (+0.63%) both green while the SPY floor tracks the index dip 1:1.
- **WTD base = Fri 8/14 close, portfolio $101,378.01 / SPY 776.30.** WTD so far: book **−0.212%** vs SPY **−1.019%** → **WTD alpha ~+0.81 pt** (intraday, week young). Cumulative alpha since 5/29 base ≈ **−0.9 pt**.
- Macro: soft, yield-pressured tape (10Y near highs); semis heavy. No binary print today; DE Q3 is Thu 8/20 BMO; Jackson Hole next week.

## Snapshot (live marks — 2026-08-18 13:02 ET)
- **Equity $101,162.91.** Total since $100K start: **+1.16%.**
- **Net open unrealized: +$1,083.79** (JPM +1,034.23, DE +103.40, LLY +90.84, SPY −144.68).
- **Cash 36.22%** — well above the 10–20% minimum buffer.
- Quiet, constructive midday; theses all intact. All three conviction stocks green on the day; SPY sleeve tracking the index dip. No name moved materially against us.

## Open positions (3 conviction stocks + 1 index-floor sleeve) — live marks 8/18 13:02 ET
| Symbol | Shares | Avg Cost | Price | P/L $ | P/L % | Stop | Entry Date | Thesis (1 line) |
|---|---|---|---|---|---|---|---|---|
| JPM | 34 | 329.695588 | 360.1142 | +1,034.23 | +9.23% | **10% TRAILING (GTC)**, floor **329.85**, hwm 366.5 | 2026-06-29 | JPMorgan — $50B buyback + div hike; largest US bank; Q2 beat. Consensus Buy avg PT ~$372–373; WF $390 OW stands. Next earnings ~Oct. **Cushion ~8.40%.** |
| DE | 22 | 589.82 | 594.52 | +103.40 | +0.80% | **10% TRAILING (GTC)**, floor **579.591**, hwm 643.99 | 2026-06-04 | Deere — Q2 beat, FY26 guide raised, ag/onshoring tailwind. **Q3 CONFIRMED Thu Aug 20 BMO 9:00 CT** (cons ~$4.72 EPS / ~$10.8B rev, rev DOWN YoY = low bar; base case = reaffirm FY26 $4.5–5.0B). Analyst trims into print (JPM $590→$570, Evercore $641→$632). **HOLD-THROUGH-PRINT FINALIZED = HOLD; do NOT trim/add. Cushion ~2.51% (tightest trailing).** |
| LLY | 12 | 1209.84 | 1217.41 | +90.84 | +0.63% | **−7% HARD STOP (GTC) @ 1125.15** | 2026-08-12 | Eli Lilly — Q2 beat-and-raise (RAISED FY26 EPS $35.50–36.50) + GLP-1/obesity tailwind. Green today (+0.63%), recovered from the early-week wobble; drift = post-earnings consolidation, no LLY-specific/Novo news. Conviction ~73 (B+). Hard stop converts to 10% trailing once +5% (~$1,270.33). **Cushion ~7.58%.** |
| SPY | 32 | 772.921250 | 768.40 | −144.68 | −0.58% | **NONE — index-floor sleeve, deliberate no-stop carve-out** | 2026-08-10 (t1) / 2026-08-11 (t2) | S&P 500 market floor (Lauren-approved Option B), COMPLETE. Own sleeve, EXEMPT from ≤20%/max-5/max-3-per-week caps; NO −7%/trailing stop. Buy-and-hold-the-market. |

**Conviction sleeve: 3 of 5 (two slots OPEN).** **Conviction buys used this week: 0 of 3** (the SPY floor does NOT consume this budget). **Cash buffer: ~36.22%.** Position sizes (on equity $101,162.91): JPM ~12.10%, DE ~12.93%, LLY ~14.44%, SPY ~24.31% (index sleeve — exempt from the 20% single-position cap by policy).

## Closed THIS WEEK
- **None** (week of Mon 8/17). Last close: LLY trailing-stop 7/31 (+$627), since re-entered 8/12.

## Stop-management state (re-confirmed RESTING via open-orders, nested=true — 8/18 13:02 ET)
- **JPM 10% trailing** `8a937ff6-164c-4384-8cf8-c000d4106a60` — hwm **366.5**, floor (stop_price) **329.85**, status new (resting). Price 360.1142, cushion ~8.40%. Below hwm → no ratchet. qty 34.
- **DE 10% trailing** `dcdd84e5-6b94-4943-aa5b-3d3a299cbfce` — hwm **643.99**, floor (stop_price) **579.591**, status new (resting). Price 594.52, cushion ~2.51%. Below hwm → no ratchet. qty 22.
- **LLY −7% hard stop** `f50e3c39-0719-497e-8ccc-6006e6afa290` — stop_price **1125.15** (=1209.84×0.93), GTC, status new (resting). Price 1217.41 (+0.63% from entry). **Converts to a 10% trailing stop once LLY is +5% in profit** (trigger ~$1,270.33). Cushion to stop ~7.58%. qty 12.
- **SPY — NO STOP by design** (index-floor sleeve carve-out). qty_available 32 (unencumbered). Intentional per the 8/7 policy; do NOT place a stop on the floor.

## Risk checks (midday, live)
- **(a) Any position −7% or worse un-stopped?** NO. JPM +9.23%, DE +0.80%, LLY +0.63%, SPY −0.58%. **→ No 4-hour news check triggered; no sell.** No discretionary check either — no name moved materially against us.
- **(b) Any position +5%+ needing hard→trailing conversion?** NO conversion pending. JPM & DE already on 10% trailing GTC; LLY +0.63% (below +5%) on its −7% hard stop as designed; SPY carries no stop by policy. **(Standing task: convert LLY's hard stop → 10% trailing once it tags ~+5% / ~$1,270.33.)**
- **(c) Daily loss cap:** intraday +0.125% (up), not tripped. Moot — no buys placed.

## Watch / next (next routine: **market-close Tue 8/18**)
- **DE — Q3 Thu Aug 20 BMO. DECISION FINALIZED = HOLD through the print** (do NOT trim, do NOT add). De-risked expectations (analysts trimmed, rev down YoY = low bar), thesis intact, trailing floor 579.591 (~2.5% below) is the safety net. Tail risk = a severe guide miss gapping down through the stop overnight (one contained ~13% position, not book-threatening). Revisit only if a warning surfaces Wed.
- **LLY — green +0.63%, thesis intact.** Cushion ~7.58% to the 1125.15 hard stop; convert to 10% trailing at +5% (~$1,270.33).
- **JPM — cushion ~8.40%**, healthy; below hwm so floor unchanged; next earnings ~Oct.
- **HD earnings today (BMO)** — the consumer read; watch the tape reaction into the close.
- **Conviction gate: EMPTY (~52nd effectively-empty scan).** Board is entry-blocked, not thesis-blocked: AMGN/ANET/ABT/ETN/PWR all chases (extended); AMAT below-trend + high-beta semi into risk-off; ABBV cleanest but only ~1 real signal. Two slots open, ~36% cash = room for ~1 buy before trimming the floor.

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
