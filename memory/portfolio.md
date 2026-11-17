# Portfolio

**Last updated:** 2026-11-17 ~12:00 CT (**1:00 PM ET, MIDDAY routine**, Tue — **NO TRADES**, steady into the NVDA 11/17 AMC binary). Clock gate: `market_clock.py --slot midday --wait --claim` → summer alarm rang ~53 min early (12:07 ET) → `--wait` held 3167s to **1:00 PM ET** → **DUE** ("0 min after the bell"); Alpaca `/v2/clock` **is_open=true** (next_close 11/17 16:00, next_open 11/18 09:30) → **CLAIMED** (stamp 2026-11-17 midday, owner midday). 4 required keys non-empty; EQUIBLES empty → filing data skipped. Inbox **no Pending**; Astra **no proposals**. Sleeve **3/5 (two open slots)**; weekly conviction buys **0/3** (week 11/16–11/20). Open orders **exactly 3** (NOC hard 506.26, RSG trail **231.111** hwm 256.79, PG trail **156.231** hwm 173.59); SPY unencumbered. **NO TRADES this run.** SPY sweep: `spy_floor.py` → **action:none** (cash within one SPY share of the $10k cushion). All three conviction stocks green; book out-defending a red tape (intraday −0.607% vs SPY −1.21% → +0.60 pt). See research-log 2026-11-17 midday.

## Open positions (3 conviction stocks + 1 index-floor sleeve) — LIVE marks 2026-11-17 1:00 PM ET
| Symbol | Shares | Avg Cost | Px | P/L % | MV | Stop | Entry Date | Thesis (1 line) |
|---|---|---|---|---|---|---|---|---|
| NOC | 18 | 544.37 | 554.40 | +1.84% | $9,979.20 | **−7% HARD (GTC)** `506.26` | 2026-10-23 | Northrop Grumman, defense/aerospace. Q3 beat+raise + record backlog; fresh $1.6B PAC-3 MSE order (11/16); BTIG reiterated Buy PT $815. Convert to trailing at +5% (~$571.59). INTACT→STRENGTHENING. |
| PG | 65 | 148.06 | 172.83 | +16.73% | $11,233.95 | **10% TRAILING (GTC)** floor `156.231` | 2026-10-08 | Procter & Gamble — staples diversifier. Relative winner. **Investor Day Thu Nov 19** (near catalyst). Floor above entry (profit locked). HOLD. |
| RSG | 44 | 218.00 | 253.545 | +16.31% | $11,155.98 | **10% TRAILING (GTC)** floor `231.111` | 2026-09-18 | Republic Services — defensive waste. Argus Buy PT $275 (11/12) stacking JPM OW PT $295. Q3 beat + raised FY26, $5B buyback. HOLD/STRENGTHENING. |
| SPY | 74 | 761.083 | 731.19 | −3.93% | $54,108.02 | **NONE — index-floor sleeve, deliberate no-stop carve-out** | 2026-08-10→11-06 | S&P 500 market floor (Lauren-approved Option B + same-day sweep). Own sleeve, EXEMPT from ≤20%/max-5/max-3-per-week; NO stop. ~55.8% of book. It IS the benchmark. |

**Conviction sleeve: 3 of 5 — two open slots.** **Conviction buys used this week (11/16–11/20): 0 of 3.** **Cash buffer: 10.77%** ($10,440.97 — at the ~$10k cushion). Largest non-index single name PG $11,233.95 (11.59% of equity — well under the 20% cap). Conviction stock mv NOC+PG+RSG $32,369.13 (33.4%); SPY sleeve $54,108.02 (55.8%).

## Today's fills (2026-11-17 — midday run)
- **NONE (0 orders placed/filled).** No buy, no sell, no stop trigger, no stop conversion, no SPY sweep (cash at cushion → spy_floor action:none). All three conviction stocks green; nothing near −7%; NOC (+1.84%) not yet at the +5% hard→trailing conversion line (~$571.59). NVDA 11/17 AMC complex-binary near-veto active on fresh high-beta/semi longs. (Market-open run earlier also NO TRADES.)

## Live snapshot (MIDDAY 2026-11-17 1:00 PM ET)
- **Equity:** $96,918.12 · cash $10,440.97 (10.77%) · long_mv $86,477.15.
- **Intraday P/L:** −$591.79 / **−0.607%** (base Alpaca last_equity $97,509.91 = 11/16 close) — NOT near the −3% loss cap; full buffer intact.
- **SPY day:** ~**−1.21%** (last 731.12 vs 11/16 close 740.04) → book ahead intraday (~+0.60 pt). Weekly review (Fri) owns the official weekly number.

## Risk checks (MIDDAY 2026-11-17 1:00 PM ET)
- **(a) Any position −7% or worse un-stopped?** NO. NOC +1.84%, PG +16.73%, RSG +16.31% (all green); SPY −3.93% (index, no stop by design). Nothing near −7% → no Perplexity news check triggered.
- **(b) Any position +5%+ needing hard→trailing conversion?** NO. NOC (only HARD-stop name) is +1.84% — not yet +5% (convert at ~$571.59). PG/RSG already trail. Nothing to convert.
- **(c) Daily loss cap:** intraday **−0.607%** — NOT breached (cap is >3% down). Full buffer intact.
- **(d) Sell signals?** NONE. NOC/PG/RSG theses all INTACT→STRENGTHENING; no −7% breach, no thesis break, no guidance cut, no "better opportunity at the 5-cap" (two slots OPEN).

## Stop-management state (open-orders — VERIFIED live 2026-11-17 MIDDAY, exactly 3)
- **NOC −7% HARD** `59a67c62-0ec7-4d59-8315-66d94b9d3d7c` — stop **506.26**, GTC, resting. qty 18. Convert at +5% (~$571.59).
- **PG 10% TRAILING** `272e2864-58a7-471f-93ad-acf3914e5a18` — floor **156.231**, trail 10%, hwm 173.59, GTC, resting. qty 65.
- **RSG 10% TRAILING** `135c200e-fc09-4a37-95c1-f940b57ae0e3` — floor **231.111**, trail 10%, hwm 256.79, GTC, resting. qty 44.
- **SPY — NO STOP by design** (index-floor sleeve carve-out). qty 74 unencumbered.
- Confirmed **exactly 3 open orders total** — 1 hard stop (NOC) + 2 trailing (PG/RSG). SPY unencumbered. 0 orders placed this run. **Positions held with their stops — we do NOT flatten intraday.**

## Strategy status (MIDDAY 2026-11-17)
- **Regime:** RISK-OFF into the NVDA binary — SPY ~−1.2% on the day (chip-export curbs + hawkish Fed). **NVDA reports Tue 11/17 AMC = THE binary event** for the whole AI/semi complex; reaction hits semis/index Wed AM. **Dec 9–10 FOMC near-priced for a 25bp HIKE.** Favor quality; do NOT chase.
- **Traded this week:** **NOTHING yet** (0 of 3 conviction buys). ADSK is the #1 non-defensive bench name (~72 B+) but its own Nov 24 earnings + the NVDA binary = entry-timing near-veto; revisit after NVDA clears on a clean base. AMD/semis DEFERRED pre-NVDA. FERG watchlist (needs a genuine low-$240s pullback, not a 52-wk-high chase).
- **★ Two open slots (sleeve 3/5)** — book is NOC/PG/RSG = defensive-tilted (at the 2-of-5 defensive cap). Next buys MUST be NON-defensive (beta ≥1.0) with a CLEAN entry. No bench name clears the gate on a clean entry right now.
- **Events runway:** **NVDA 11/17 AMC** (the complex-wide binary); retail prints Tue–Thu; **PG Investor Day Thu 11/19**; Dec 9 FOMC (25bp hike near-priced).
