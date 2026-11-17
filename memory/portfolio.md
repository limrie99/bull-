# Portfolio

**Last updated:** 2026-11-17 ~15:00 CT (**4:00 PM ET, MARKET-CLOSE routine**, Tue — **NO TRADES**; mandatory daily close scorecard written + Telegram pushed). Clock gate: `market_clock.py --slot market-close --wait --claim --owner market-close` → summer alarm (`0 20`) rang ~56 min early (15:04 ET) → `--wait` held to **4:00 PM ET** → **status DUE** ("0 min after the bell"); Alpaca `/v2/clock` **is_open=false** (market just closed; next_open 11/18 09:30) → **CLAIMED** (stamp 2026-11-17 market-close, owner market-close). 4 required keys non-empty; EQUIBLES empty → filing data skipped. Inbox **no Pending**; Astra **no proposals**. Sleeve **3/5 (two open slots)**; weekly conviction buys **0/3** (week 11/16–11/20). Open orders **exactly 3** (NOC hard 506.26, RSG trail **231.111** hwm 256.79, PG trail **156.231** hwm 173.59); SPY unencumbered. **NO TRADES this run** (closed-orders today = 0). SPY sweep: market closed + cash within one SPY share of the $10k cushion → `spy_floor.py` **action:none** (no sweep; close run, market shut). Down-day defense held: book **−0.658%** vs SPY **−1.031%** → **+0.37 pt alpha today**; week-to-date **+1.40 pt alpha**. ★ **NVDA reports TONIGHT 11/17 AMC** — the AI/semi-complex binary; reaction lands Wed AM. See research-log 2026-11-17 Day summary.

## Open positions (3 conviction stocks + 1 index-floor sleeve) — CLOSING marks 2026-11-17 4:00 PM ET
| Symbol | Shares | Avg Cost | Px (close) | P/L % | MV | Stop | Entry Date | Thesis (1 line) |
|---|---|---|---|---|---|---|---|---|
| NOC | 18 | 544.37 | 553.26 | +1.63% | $9,958.68 | **−7% HARD (GTC)** `506.26` | 2026-10-23 | Northrop Grumman, defense/aerospace. Q3 beat+raise + record backlog; fresh $1.6B PAC-3 MSE order (11/16); BTIG reiterated Buy PT $815. Convert to trailing at +5% (~$571.59). INTACT→STRENGTHENING. |
| PG | 65 | 148.06 | 171.79 | +16.03% | $11,166.35 | **10% TRAILING (GTC)** floor `156.231` | 2026-10-08 | Procter & Gamble — staples diversifier. Relative winner. **Investor Day Thu Nov 19** (near catalyst). Floor above entry (profit locked). HOLD. |
| RSG | 44 | 218.00 | 252.93 | +16.02% | $11,128.92 | **10% TRAILING (GTC)** floor `231.111` | 2026-09-18 | Republic Services — defensive waste. Argus Buy PT $275 (11/12) stacking JPM OW PT $295. Q3 beat + raised FY26, $5B buyback. HOLD/STRENGTHENING. |
| SPY | 74 | 761.083 | 732.12 | −3.81% | $54,176.88 | **NONE — index-floor sleeve, deliberate no-stop carve-out** | 2026-08-10→11-06 | S&P 500 market floor (Lauren-approved Option B + same-day sweep). Own sleeve, EXEMPT from ≤20%/max-5/max-3-per-week; NO stop. ~55.9% of book. It IS the benchmark. |

**Conviction sleeve: 3 of 5 — two open slots.** **Conviction buys used this week (11/16–11/20): 0 of 3.** **Cash buffer: 10.78%** ($10,440.97 — at the ~$10k cushion). Largest non-index single name PG $11,166.35 (11.53% of equity — well under the 20% cap). Conviction stock mv NOC+PG+RSG $32,253.95 (33.3%); SPY sleeve $54,176.88 (55.9%).

## Today's fills (2026-11-17 — whole day: pre-market, open, midday, close)
- **NONE (0 orders placed/filled all day).** No buy, no sell, no stop trigger, no stop conversion, no SPY sweep (close run with market shut + cash at cushion → spy_floor action:none). All three conviction stocks closed green; nothing near −7%; NOC (+1.63%) not yet at the +5% hard→trailing conversion line (~$571.59). NVDA 11/17 AMC complex-binary near-veto held on fresh high-beta/semi longs all day.

## Live snapshot (CLOSE 2026-11-17 4:00 PM ET)
- **Equity:** $96,868.10 · cash $10,440.97 (10.78%) · long_mv $86,427.13.
- **Day P/L:** −$641.81 / **−0.658%** (base 11/16 close equity $97,509.91).
- **SPY day:** **−1.031%** (close 732.41 vs 11/16 close 740.04) → **alpha today +0.37 pt** (down-day defense).
- **Week-to-date:** book **−1.497%** (base Fri 11/13 close $98,340.65) vs SPY **−2.898%** (732.41 vs 11/13 close 754.27) → **alpha WTD +1.40 pt** (Fri review owns the official weekly number).

## Risk checks (CLOSE 2026-11-17 4:00 PM ET)
- **(a) Any position −7% or worse un-stopped?** NO. NOC +1.63%, PG +16.03%, RSG +16.02% (all green); SPY −3.81% (index, no stop by design). Nothing near −7% → no Perplexity news check triggered.
- **(b) Any position +5%+ needing hard→trailing conversion?** NO. NOC (only HARD-stop name) is +1.63% — not yet +5% (convert at ~$571.59). PG/RSG already trail. Nothing to convert.
- **(c) Daily loss cap:** day **−0.658%** — NOT breached (cap is >3% down). Full buffer intact.
- **(d) Sell signals?** NONE. NOC/PG/RSG theses all INTACT→STRENGTHENING; no −7% breach, no thesis break, no guidance cut, no "better opportunity at the 5-cap" (two slots OPEN).

## Stop-management state (open-orders — VERIFIED live 2026-11-17 CLOSE, exactly 3)
- **NOC −7% HARD** `59a67c62-0ec7-4d59-8315-66d94b9d3d7c` — stop **506.26**, GTC, resting. qty 18. Convert at +5% (~$571.59).
- **PG 10% TRAILING** `272e2864-58a7-471f-93ad-acf3914e5a18` — floor **156.231**, trail 10%, hwm 173.59, GTC, resting. qty 65.
- **RSG 10% TRAILING** `135c200e-fc09-4a37-95c1-f940b57ae0e3` — floor **231.111**, trail 10%, hwm 256.79, GTC, resting. qty 44.
- **SPY — NO STOP by design** (index-floor sleeve carve-out). qty 74 unencumbered.
- Confirmed **exactly 3 open orders total** — 1 hard stop (NOC) + 2 trailing (PG/RSG). SPY unencumbered. 0 orders placed this run. **Positions held with their stops.**

## Strategy status (CLOSE 2026-11-17)
- **Regime:** RISK-OFF into the NVDA binary — SPY closed ~−1.03% (chip-export curbs + hawkish Fed). **NVDA reports TONIGHT 11/17 AMC = THE binary event** for the whole AI/semi complex; reaction hits semis/index Wed AM. **Dec 9–10 FOMC near-priced for a 25bp HIKE.** Favor quality; do NOT chase.
- **Traded this week:** **NOTHING (0 of 3 conviction buys).** ADSK is the #1 non-defensive bench name (~72 B+) but its own Nov 24 earnings + the NVDA binary = entry-timing near-veto; revisit after NVDA clears on a clean base. AMD/semis DEFERRED pre-NVDA. FERG watchlist (needs a genuine low-$240s pullback, not a 52-wk-high chase).
- **★ Two open slots (sleeve 3/5)** — book is NOC/PG/RSG = defensive-tilted (at the 2-of-5 defensive cap). Next buys MUST be NON-defensive (beta ≥1.0) with a CLEAN entry. No bench name clears the gate on a clean entry right now.
- **Events runway:** **NVDA 11/17 AMC** (TONIGHT, complex-wide binary); retail prints Tue–Thu; **PG Investor Day Thu 11/19**; Dec 9–10 FOMC (25bp hike near-priced).

## Handoff → pre-market (Wed 2026-11-18, 6:00 AM CT / 7:00 AM ET)
- **★ NVDA reported 11/17 AMC — READ THE REACTION FIRST.** The after-hours/pre-market move in NVDA + semis + ES sets Wednesday's regime. If semis gap up and hold on a clean base, the NVDA near-veto lifts and ADSK/non-defensive bench names can be re-scored for a clean entry. If NVDA disappoints and the complex sells off, stay defensive and let our stops do their job.
- **Clock gate first:** `market_clock.py --slot pre-market --wait --claim --owner pre-market`; summer ring (`0 11`) lands ~56 min early → `--wait` holds to 7:00 AM ET.
- **Re-verify live:** account/positions/open-orders/clock; confirm exactly 3 open orders; daily loss-cap check.
- **Sleeve 3/5 — two open slots**, 0/3 weekly buys. Next buy must be NON-defensive (beta ≥1.0) on a CLEAN entry.
- **Events:** PG Investor Day Thu 11/19; retail prints through the week; Dec 9–10 FOMC (25bp hike near-priced).
