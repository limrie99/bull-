# Portfolio

**Last updated:** 2026-11-18 ~08:37 CT (**9:37 AM ET, MARKET-OPEN routine**, Wed — **TRADED: bought FERG, trimmed SPY to fund it**). Clock gate: `market_clock.py --slot market-open --wait` → **DUE** (09:33 ET, "3 min after the bell"); Alpaca `/v2/clock` **is_open=true** → `--claim --owner market-open` → **CLAIMED** (stamp 2026-11-18) and **pushed to main before any order** (commit 5b04bf0). 4 required keys non-empty; EQUIBLES empty → filing data skipped. Inbox **no Pending**; Astra **no proposals**. Executed the pre-market LEAD BUY: **FERG 44 @ 250.12** (−7% hard GTC stop 232.61), funded by a **15-share SPY trim** (sold @ 732.602) per `spy_floor.py` (action:trim). Sleeve **3/5 → 4/5 (one open slot)**; weekly conviction buys **0/3 → 1/3** (week 11/16–11/20). Open orders **now exactly 4** (FERG hard 232.61, NOC hard 506.26, RSG trail 231.111, PG trail 156.231); SPY (59 sh) unencumbered. ★ NVDA 11/17 AMC beat-and-raise relaxed the high-beta near-veto → FERG (non-defensive, beta ~1.11) cleared on a clean non-extended entry. See research-log 2026-11-18 market-open.

## Open positions (4 conviction stocks + 1 index-floor sleeve) — live marks 2026-11-18 ~9:37 AM ET
| Symbol | Shares | Avg Cost | Px (live) | P/L % | MV | Stop | Entry Date | Thesis (1 line) |
|---|---|---|---|---|---|---|---|---|
| FERG | 44 | 250.12 | 249.08 | −0.42% | $10,959.52 | **−7% HARD (GTC)** `232.61` | 2026-11-18 | Ferguson — plumbing/HVAC/industrial distributor. Q1 FY27 beat+raise (11/9) + onshoring/data-center demand + Nov PT-raise wave (BofA $320 Buy 11/18). Non-defensive (beta ~1.11). Convert to trailing at +5% (~$267.63). NEW. |
| NOC | 18 | 544.37 | 542.71 | −0.30% | $9,768.78 | **−7% HARD (GTC)** `506.26` | 2026-10-23 | Northrop Grumman, defense/aerospace. Q3 beat+raise + record backlog; $1.6B PAC-3 MSE order (11/16); BTIG Buy PT $815. Convert to trailing at +5% (~$571.59). INTACT. |
| PG | 65 | 148.06 | 171.35 | +15.73% | $11,137.75 | **10% TRAILING (GTC)** floor `156.231` | 2026-10-08 | Procter & Gamble — staples diversifier. **Investor Day Thu Nov 19** (near catalyst). Floor above entry (profit locked). HOLD. |
| RSG | 44 | 218.00 | 251.785 | +15.50% | $11,078.54 | **10% TRAILING (GTC)** floor `231.111` | 2026-09-18 | Republic Services — defensive waste. Argus Buy PT $275 + JPM OW $295. Q3 beat + raised FY26, $5B buyback. HOLD. |
| SPY | 59 | 761.083 | 732.39 | −3.77% | $43,211.01 | **NONE — index-floor sleeve, deliberate no-stop carve-out** | 2026-08-10→11-06 | S&P 500 market floor (Lauren-approved Option B + same-day sweep). Own sleeve, EXEMPT from ≤20%/max-5/max-3-per-week; NO stop. ~44.7% of book. It IS the benchmark. Trimmed 74→59 today to fund FERG. |

**Conviction sleeve: 4 of 5 — one open slot.** **Conviction buys used this week (11/16–11/20): 1 of 3.** **Cash buffer: 10.86%** ($10,495.47 — at the ~$10k cushion). Largest non-index single name PG $11,137.75 (11.52% of equity — well under the 20% cap). Conviction stock mv FERG+NOC+PG+RSG $42,944.59 (44.4%); SPY sleeve $43,211.01 (44.7%). **Defensive count: 2 of 5** (PG, RSG) — FERG and NOC are non-defensive, so the sleeve cap still has room.

## Today's fills (2026-11-18 — market-open run)
- **SELL SPY 15 @ 732.602** (order 1791d67d) = $10,989.03 proceeds — index-floor trim to fund FERG, keep cash at cushion. Not a conviction sell; does NOT count vs 3 weekly buys. SPY 74 → 59.
- **BUY FERG 44 @ 250.12** (order c7eccb6e) = $11,005.28 (~11.4% of equity) — the pre-market LEAD BUY; Conviction 74 (B+), 4 signals, clean non-extended entry (~$249.5, ~6% off the $264.65 high — not a chase). −7% hard GTC stop 232.61 confirmed resting. Sleeve 3/5 → 4/5; weekly buys 0/3 → 1/3.
- Order sequencing: SPY trim filled FIRST, so cash never dipped under the $10k cushion before the FERG buy.

## Live snapshot (MARKET-OPEN 2026-11-18 ~9:37 AM ET)
- **Equity:** $96,651.07 · cash $10,495.47 (10.86%) · long_mv $86,155.60.
- **Intraday P/L:** −$310.61 / **−0.32%** (base 11/17 close equity $96,961.68) — loss cap (−3%) far off, full buffer intact.
- Full daily scorecard vs SPY is owned by the market-close routine.

## Risk checks (MARKET-OPEN 2026-11-18)
- **(a) Any position −7% or worse un-stopped?** NO. FERG −0.42%, NOC −0.30%, PG +15.73%, RSG +15.50% (all within range); SPY −3.77% (index, no stop by design). Nothing near −7%.
- **(b) Any position +5%+ needing hard→trailing conversion?** NO. The two HARD-stop names (FERG −0.42%, NOC −0.30%) are below the +5% line (FERG convert ~$267.63; NOC ~$571.59). PG/RSG already trail.
- **(c) Daily loss cap:** intraday **−0.32%** — NOT breached (cap is >3% down). New buys still allowed.
- **(d) Sell signals?** NONE. All four theses INTACT→STRENGTHENING; no −7% breach, no thesis break, no guidance cut.

## Stop-management state (open-orders — VERIFIED live 2026-11-18 OPEN, exactly 4)
- **FERG −7% HARD** `ea91d0f9-6f6d-46c1-a665-b77c6efdc0ec` — stop **232.61**, GTC, resting. qty 44. Convert at +5% (~$267.63).
- **NOC −7% HARD** `59a67c62-0ec7-4d59-8315-66d94b9d3d7c` — stop **506.26**, GTC, resting. qty 18. Convert at +5% (~$571.59).
- **PG 10% TRAILING** `272e2864-58a7-471f-93ad-acf3914e5a18` — floor **156.231**, trail 10%, hwm 173.59, GTC, resting. qty 65.
- **RSG 10% TRAILING** `135c200e-fc09-4a37-95c1-f940b57ae0e3` — floor **231.111**, trail 10%, hwm 256.79, GTC, resting. qty 44.
- **SPY — NO STOP by design** (index-floor sleeve carve-out). qty 59 unencumbered.
- Confirmed **exactly 4 open orders total** — 2 hard stops (FERG, NOC) + 2 trailing (PG/RSG). SPY unencumbered.

## Strategy status (MARKET-OPEN 2026-11-18)
- **Regime:** measured risk-on after NVDA's 11/17 AMC beat-and-raise (Q4 guide raised, China excluded = pure upside optionality). Narrow megacap-tech leadership; the AI/semi binary resolved bullish, relaxing the fresh-high-beta near-veto. Caveat: **FOMC Oct minutes 2:00 PM ET today** = this afternoon's macro risk event; Dec 9–10 FOMC (25bp hike near-priced).
- **Traded this week:** FERG (1 of 3 conviction buys). One open slot (sleeve 4/5).
- **★ One open slot** — next buy must still clear 2+ signals AND Conviction ≥70 at a clean entry; defensive cap has room (2/5) but prefer another non-defensive gate-clearer. ADSK (B+ 72) stays DEFERRED on its own 11/24 earnings fence.
- **Events runway:** FOMC Oct minutes 2:00 PM ET today; **PG Investor Day Thu 11/19**; China chip rule effective Thu; Dec 9–10 FOMC.

## Handoff → midday (Wed 2026-11-18, winter cron `0 18 UTC`; summer `0 17` rings ~57 min early → `--wait` holds to 1:00 PM ET)
- **Clock gate first:** `market_clock.py --slot midday --wait --claim --owner midday`; confirm Alpaca is_open=true before claiming.
- **Re-verify live:** account/positions/open-orders/clock; confirm **exactly 4** open orders (FERG hard 232.61; NOC hard 506.26; RSG trail 231.111; PG trail 156.231); SPY (59 sh) unencumbered; daily loss-cap check.
- **FERG is new and unprofitable** (−0.42%) — hold with its hard stop; convert to trailing only at +5% (~$267.63). Watch it isn't knifing below entry on a 2pm-minutes whipsaw.
- **NOC hard→trailing conversion:** only at +5% (~$571.59); it's −0.30%, far off. PG/RSG floors ratchet automatically.
- **SPY sweep at midday:** cash $10,495 is ~$495 above the $10k cushion = less than one SPY share → expect `spy_floor.py` **action:none**. Do not use buying power.
- **★ FOMC Oct minutes 2:00 PM ET** = this afternoon's macro risk — could whipsaw. **PG Investor Day Thu 11/19.**
- **What would change the plan:** FERG breaching its stop (let it fire mechanically); a hawkish 2pm minutes whipsaw; any held name hitting a stop.
