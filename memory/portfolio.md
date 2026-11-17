# Portfolio

**Last updated:** 2026-11-17 ~08:34 CT (**09:34 ET, MARKET-OPEN routine**, Tue — **NO TRADES**, stand-pat into the NVDA 11/17 AMC binary + chip-export risk-off). Clock gate: `market_clock.py --slot market-open --wait` → **DUE** (09:32 ET, "~3 min after the bell"), winter cron `30 14` on time; Alpaca `/v2/clock` **is_open=true** (09:32 ET; next_close 11/17 16:00, next_open 11/18 09:30) → **CLAIMED** (stamp 2026-11-17 market-open, owner market-open) and pushed to main (commit 06bb54d) before any order. 4 required keys non-empty; EQUIBLES empty → filing data skipped. Inbox **no Pending**; Astra **no proposals**. Sleeve **3/5 (two open slots)**; weekly conviction buys **0/3** (week 11/16–11/20). Open orders **exactly 3** (NOC hard 506.26, RSG trail **231.111** hwm 256.79, PG trail **156.213** hwm 173.57); SPY unencumbered. **NO TRADES this run.** SPY sweep: `spy_floor.py` → **action:none** (cash within one SPY share of the $10k cushion). **The feared hard-red open moderated** — ES futures were ~−1.9% pre-market on new US chip-export curbs, but SPY opened only ~−0.25% on the day. Executed the pre-market plan exactly: do NOT initiate fresh beta into the NVDA complex-binary tonight. See research-log 2026-11-17 market-open.

## Open positions (3 conviction stocks + 1 index-floor sleeve) — LIVE marks 2026-11-17 09:34 ET
| Symbol | Shares | Avg Cost | Px | P/L % | MV | Stop | Entry Date | Thesis (1 line) |
|---|---|---|---|---|---|---|---|---|
| NOC | 18 | 544.37 | 547.10 | +0.50% | $9,847.80 | **−7% HARD (GTC)** `506.26` | 2026-10-23 | Northrop Grumman, defense/aerospace. Q3 beat+raise + record backlog; fresh $1.6B PAC-3 MSE order (11/16); BTIG reiterated Buy PT $815. Convert to trailing at +5% (~$571.59). INTACT→STRENGTHENING. |
| PG | 65 | 148.06 | 172.285 | +16.36% | $11,198.52 | **10% TRAILING (GTC)** floor `156.213` | 2026-10-08 | Procter & Gamble — staples diversifier. Relative winner. **Investor Day Thu Nov 19** (near catalyst). Floor above entry (profit locked). HOLD. |
| RSG | 44 | 218.00 | 254.25 | +16.63% | $11,187.00 | **10% TRAILING (GTC)** floor `231.111` | 2026-09-18 | Republic Services — defensive waste. Argus Buy PT $275 (11/12) stacking JPM OW PT $295. Q3 beat + raised FY26, $5B buyback. HOLD/STRENGTHENING. |
| SPY | 74 | 761.083 | 738.20 | −3.01% | $54,626.80 | **NONE — index-floor sleeve, deliberate no-stop carve-out** | 2026-08-10→11-06 | S&P 500 market floor (Lauren-approved Option B + same-day sweep). Own sleeve, EXEMPT from ≤20%/max-5/max-3-per-week; NO stop. ~56.1% of book. It IS the benchmark. |

**Conviction sleeve: 3 of 5 — two open slots.** **Conviction buys used this week (11/16–11/20): 0 of 3.** **Cash buffer: 10.73%** ($10,440.97 — at the ~$10k cushion). Largest non-index single name PG $11,198.52 (11.51% of equity — well under the 20% cap). Conviction stock mv NOC+PG+RSG $32,233.32 (33.1%); SPY sleeve $54,626.80 (56.1%).

## Today's fills (2026-11-17 — market-open run)
- **NONE (0 orders placed/filled).** No buy, no sell, no stop trigger, no stop conversion, no SPY sweep (cash at cushion → spy_floor action:none). All three conviction stocks green; nothing near −7%; NOC (+0.50%) not yet at the +5% hard→trailing conversion line (~$571.59). NVDA 11/17 AMC complex-binary near-veto active on fresh high-beta/semi longs.

## Live snapshot (MARKET-OPEN 2026-11-17 09:34 ET)
- **Equity:** $97,301.10 · cash $10,440.97 (10.73%) · long_mv $86,860.13.
- **Intraday P/L:** −$208.81 / **−0.214%** (base Alpaca last_equity $97,509.91 = 11/16 close) — NOT near the −3% loss cap; full buffer intact.
- **SPY day:** ~**−0.25%** (last 738.20 vs 11/16 close 740.04) → book marginally ahead intraday (~+0.03 pt). Weekly review (Fri) owns the official weekly number.

## Risk checks (MARKET-OPEN 2026-11-17 09:34 ET)
- **(a) Any position −7% or worse un-stopped?** NO. NOC +0.50%, PG +16.36%, RSG +16.63% (all green); SPY −3.01% (index, no stop by design). Nothing near −7%.
- **(b) Any position +5%+ needing hard→trailing conversion?** NO. NOC (only HARD-stop name) is +0.50% — not yet +5% (convert at ~$571.59). PG/RSG already trail. Nothing to convert.
- **(c) Daily loss cap:** intraday **−0.214%** — NOT breached (cap is >3% down). Full buffer intact.
- **(d) Sell signals?** NONE. NOC/PG/RSG theses all INTACT→STRENGTHENING; no −7% breach, no thesis break, no guidance cut, no "better opportunity at the 5-cap" (two slots OPEN).

## Stop-management state (open-orders — VERIFIED live 2026-11-17 OPEN, exactly 3)
- **NOC −7% HARD** `59a67c62-0ec7-4d59-8315-66d94b9d3d7c` — stop **506.26**, GTC, resting. qty 18. Convert at +5% (~$571.59).
- **PG 10% TRAILING** `272e2864-58a7-471f-93ad-acf3914e5a18` — floor **156.213**, trail 10%, hwm 173.57, GTC, resting. qty 65.
- **RSG 10% TRAILING** `135c200e-fc09-4a37-95c1-f940b57ae0e3` — floor **231.111**, trail 10%, hwm 256.79, GTC, resting. qty 44.
- **SPY — NO STOP by design** (index-floor sleeve carve-out). qty 74 unencumbered.
- Confirmed **exactly 3 open orders total** — 1 hard stop (NOC) + 2 trailing (PG/RSG). SPY unencumbered. 0 orders placed this run. **Positions held with their stops — we do NOT flatten intraday.**

## Strategy status (MARKET-OPEN 2026-11-17)
- **Regime:** RISK-OFF / HAWKISH into the NVDA binary, but the open was far calmer than futures feared (ES ~−1.9% pre-mkt → SPY ~−0.25% at the open). **NVDA reports Tue 11/17 AMC = THE binary event** for the whole AI/semi complex; reaction hits semis/index Wed AM. **Dec 9–10 FOMC near-priced for a 25bp HIKE.** Favor quality; do NOT chase.
- **Traded this week:** **NOTHING yet** (0 of 3 conviction buys). ADSK is the #1 non-defensive bench name (~72 B+) but its own Nov 24 earnings + the NVDA binary = entry-timing near-veto; revisit after NVDA clears on a clean base. AMD/semis DEFERRED pre-NVDA. FERG watchlist (needs a genuine pullback, not a 52-wk-high chase).
- **★ Two open slots (sleeve 3/5)** — book is NOC/PG/RSG = defensive-tilted (at the 2-of-5 defensive cap). Next buys MUST be NON-defensive (beta ≥1.0) with a CLEAN entry. No bench name clears the gate on a clean entry right now.
- **Events runway:** **NVDA 11/17 AMC** (the complex-wide binary); retail prints Tue–Thu; **PG Investor Day Thu 11/19**; Dec 9 FOMC (25bp hike near-priced).
