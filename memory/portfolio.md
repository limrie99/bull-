# Portfolio

**Last updated:** 2026-11-18 ~15:00 CT display (**4:00 PM ET, MARKET-CLOSE routine**, Wed — **STEADY, no close trades**). Clock gate: wake fired on the SUMMER cron (`0 20 UTC`, 3:02 PM ET) = daylight-saving early ring; `market_clock.py --slot market-close --wait` held 55 min to the real 4:00 PM ET bell, then `--claim --owner market-close` → **CLAIMED** (stamp 2026-11-18, no prior claim today). Alpaca `/v2/clock` **is_open=false, next_close=2026-11-19 16:00** → the bell has rung, the close is genuine. 4 required keys non-empty; EQUIBLES empty → filing data skipped. Inbox **no Pending**; Astra **no proposals**. Risk checks all clear (no −7% breach, no +5% hard→trailing conversion due, loss cap far off). SPY sweep `spy_floor.py` → **action:none** (cash within one share of cushion) AND market now closed → no sweep. No new buys. Sleeve **4/5** (one open slot); weekly conviction buys **1/3** (week 11/16–11/20). Open orders **exactly 4** unchanged. See research-log 2026-11-18 day summary.

## Daily scorecard (2026-11-18 close)
- **Close equity:** $96,410.02 · cash $10,495.47 (10.89%) · long_mv $85,914.55.
- **Day P/L:** **−$551.66 / −0.57%** (base 11/17 close equity $96,961.68, from Alpaca `last_equity`).
- **SPY day:** **−0.28%** (731/730 band: 732.41 close 11/17 → 730.33 close 11/18).
- **Alpha today:** **−0.29 pp** — we lagged the market by about a quarter-point today (PG & RSG gave back a little of their big gains while SPY was only mildly down).
- **Week-to-date (from Fri 11/13 close $98,340.65):** **−1.96% / −$1,930.63**; SPY week **−3.17%** (754.27 → 730.33); **week alpha +1.21 pp — we are BEATING the market this week.** Loss-cap (−3% intraday) never near.

## Open positions (4 conviction stocks + 1 index-floor sleeve) — CLOSE marks 2026-11-18 4:00 PM ET
| Symbol | Shares | Avg Cost | Px (close) | P/L % | MV | Stop | Entry Date | Thesis (1 line) |
|---|---|---|---|---|---|---|---|---|
| FERG | 44 | 250.12 | 251.23 | +0.44% | $11,054.12 | **−7% HARD (GTC)** `232.61` | 2026-11-18 | Ferguson — plumbing/HVAC/industrial distributor. Q1 FY27 beat+raise (11/9) + onshoring/data-center demand + Nov PT-raise wave (BofA $320 Buy 11/18). Non-defensive (beta ~1.11). Convert to trailing at +5% (~$267.63). NEW — closed modestly green day 1. |
| NOC | 18 | 544.37 | 542.99 | −0.25% | $9,773.82 | **−7% HARD (GTC)** `506.26` | 2026-10-23 | Northrop Grumman, defense/aerospace. Q3 beat+raise + record backlog; $1.6B PAC-3 MSE order (11/16); BTIG Buy PT $815. Convert to trailing at +5% (~$571.59). INTACT. |
| PG | 65 | 148.06 | 170.30 | +15.02% | $11,069.50 | **10% TRAILING (GTC)** floor `156.231` | 2026-10-08 | Procter & Gamble — staples diversifier. **Investor Day Thu Nov 19 (TOMORROW)** = near catalyst. Floor above entry (profit locked). HOLD. |
| RSG | 44 | 218.00 | 249.16 | +14.29% | $10,963.04 | **10% TRAILING (GTC)** floor `231.111` | 2026-09-18 | Republic Services — defensive waste. Argus Buy PT $275 + JPM OW $295. Q3 beat + raised FY26, $5B buyback. HOLD. |
| SPY | 59 | 761.083 | 729.90 | −4.10% | $43,064.10 | **NONE — index-floor sleeve, deliberate no-stop carve-out** | 2026-08-10→11-06 | S&P 500 market floor (Lauren-approved Option B + same-day sweep). Own sleeve, EXEMPT from ≤20%/max-5/max-3-per-week; NO stop. ~44.7% of book. It IS the benchmark. |

**Conviction sleeve: 4 of 5 — one open slot.** **Conviction buys used this week (11/16–11/20): 1 of 3.** **Cash buffer: 10.89%** ($10,495.47 — at the ~$10k cushion). Largest non-index single name PG $11,069.50 (11.48% of equity — well under the 20% cap). Conviction stock mv FERG+NOC+PG+RSG $42,860.48 (44.46%); SPY sleeve $43,064.10 (44.67%). **Defensive count: 2 of 4** (PG, RSG) — FERG and NOC non-defensive, so the sleeve defensive cap still has room.

## Today's fills (2026-11-18)
- **At CLOSE: NONE.** No sells (no −7% breach, no broken thesis), no hard→trailing conversions (neither hard-stop name is +5% yet), no SPY sweep (`action:none` + market closed), no new buys.
- **Earlier today (market-open):** SPY trim 15 @ 732.602 (funds the buy), FERG buy 44 @ 250.12 (1st conviction buy of the week, sleeve 3→4).

## Risk checks (CLOSE 2026-11-18)
- **(a) Any position −7% or worse un-stopped?** NO. FERG +0.44%, NOC −0.25%, PG +15.02%, RSG +14.29% (all in range); SPY −4.10% (index, no stop by design). Nothing near −7%.
- **(b) Any position +5%+ needing hard→trailing conversion?** NO. The two HARD-stop names (FERG +0.44%, NOC −0.25%) are below the +5% line (FERG convert ~$267.63; NOC ~$571.59). PG/RSG already trail.
- **(c) Daily loss cap:** day **−0.57%** — NOT breached (cap is >3% down). Full buffer intact.
- **(d) Sell signals?** NONE. All four theses INTACT; no −7% breach, no thesis break, no guidance cut.

## Stop-management state (open-orders — VERIFIED live 2026-11-18 CLOSE, exactly 4)
- **FERG −7% HARD** `ea91d0f9-6f6d-46c1-a665-b77c6efdc0ec` — stop **232.61**, GTC, resting. qty 44. Convert at +5% (~$267.63).
- **NOC −7% HARD** `59a67c62-0ec7-4d59-8315-66d94b9d3d7c` — stop **506.26**, GTC, resting. qty 18. Convert at +5% (~$571.59).
- **PG 10% TRAILING** `272e2864-58a7-471f-93ad-acf3914e5a18` — floor **156.231**, trail 10%, GTC, resting. qty 65.
- **RSG 10% TRAILING** `135c200e-fc09-4a37-95c1-f940b57ae0e3` — floor **231.111**, trail 10%, GTC, resting. qty 44.
- **SPY — NO STOP by design** (index-floor sleeve carve-out). qty 59 unencumbered.
- Confirmed **exactly 4 open orders total** — 2 hard stops (FERG, NOC) + 2 trailing (PG/RSG). SPY unencumbered.

## Strategy status (CLOSE 2026-11-18)
- **Regime:** measured risk-off into the close; SPY has slid four straight sessions (757→730) on narrow megacap-tech leadership and rate nerves. FOMC Oct minutes were released 2:00 PM ET today (no close-breaking surprise — orderly tape). Dec 9–10 FOMC ahead (25bp move near-priced).
- **Traded this week:** FERG (1 of 3 conviction buys). One open slot (sleeve 4/5).
- **★ One open slot** — next buy must still clear 2+ signals AND Conviction ≥70 at a clean entry; defensive cap has room (2/4) but prefer a non-defensive gate-clearer. ADSK (B+ 72) stays DEFERRED on its own 11/24 earnings fence.
- **Events runway:** **PG Investor Day Thu 11/19 (tomorrow)**; Dec 9–10 FOMC.

## Handoff → pre-market (Thu 2026-11-19, winter cron `0 12 UTC`; summer `0 11` rings ~57 min early → `--wait` holds to 7:00 AM ET)
- **Clock gate first:** `market_clock.py --slot pre-market --wait --claim --owner pre-market`.
- **Re-verify live:** account/positions/open-orders/clock; confirm **exactly 4** open orders (FERG hard 232.61; NOC hard 506.26; RSG trail 231.111; PG trail 156.231); SPY (59 sh) unencumbered; daily loss-cap check.
- **PG Investor Day Thu 11/19** — our biggest single catalyst tomorrow; PG is +15% and on a trailing stop (floor 156.231), so an Investor-Day pop ratchets the floor, a disappointment trails out mechanically. Don't pre-trade it.
- **FERG** closed +0.44% day 1 — hold on its hard stop; convert to trailing only at +5% (~$267.63). **NOC** −0.25%, hard→trailing only at +5% (~$571.59). PG/RSG floors ratchet automatically.
- **SPY sweep:** cash $10,495 is ~$495 above the $10k cushion = less than one SPY share → expect `action:none` unless a stop fires and frees cash.
- **What would change the plan:** a four-day SPY slide extending into a sharper risk-off (watch the loss cap); any held name hitting a stop; a strong/weak PG Investor Day.
