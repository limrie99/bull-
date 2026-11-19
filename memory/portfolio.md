# Portfolio

**Last updated:** 2026-11-19 ~15:00 CT display (**4:00 PM ET, MARKET-CLOSE routine**, Thu — **NO TRADES**). Clock gate: fired on the SUMMER cron (`0 20 UTC` = 3:00 PM ET, the daylight-saving early ring ~58 min early); `market_clock.py --slot market-close --wait` held to 21:00 UTC = **4:00 PM ET**, then `--claim --owner market-close` → **CLAIMED** (2026-11-19, no prior claim today). Did NOT shift the cron. Alpaca `/v2/clock` **is_open=false** (bell rang 16:00 ET, next_open 11/20 09:30) → genuine close, scorecard runs. 4 required keys non-empty; EQUIBLES empty → filing data skipped. Inbox **no Pending**; Astra **no proposals**. Risk checks all clear (no −7% breach, no +5% hard→trailing conversion due, loss cap far off — day −1.40%, DOWN but inside the −3% cap). No SPY sweep (market closed at the close run; cash also within one share of cushion). Open orders **exactly 4** unchanged — no stops fired. Sleeve **4/5** (one open slot); weekly conviction buys **1/3** (week 11/16–11/20). See research-log 2026-11-19 Day summary.

## Daily scorecard (2026-11-19 CLOSE — official end-of-day number)
- **Equity:** $95,086.86 · cash $10,495.23 (11.04%) · long_mv $84,591.63.
- **Day P/L:** **−$1,350.00 / −1.40%** (base 11/18 close equity $96,436.86 = Alpaca `last_equity`). DOWN, inside the −3% loss cap.
- **SPY today:** **−1.98%** (730.33 close 11/18 → 715.84 close 11/19) — the faded relief bounce turned into a broad afternoon slide; fifth down session in six.
- **Day alpha:** **+0.58 pp** — **BEATING the market today** (defensive book + 11% cash held while the index dropped ~2%; PG/RSG barely moved). A clean reversal from the open, when we lagged the bounce.
- **Week-to-date (from Fri 11/13 close $98,340.65):** **−3.31% / −$3,253.79**; SPY week **−5.10%** (754.27 → 715.84); **week alpha +1.79 pp — still BEATING the market this week** (lead widened from +1.53 at midday).

## Open positions (4 conviction stocks + 1 index-floor sleeve) — CLOSE marks 2026-11-19 16:00 ET
| Symbol | Shares | Avg Cost | Px (close) | P/L % | MV | Stop | Entry Date | Thesis (1 line) |
|---|---|---|---|---|---|---|---|---|
| FERG | 44 | 250.12 | 247.39 | −1.09% | $10,885.16 | **−7% HARD (GTC)** `232.61` | 2026-11-18 | Ferguson — plumbing/HVAC/industrial distributor. Q1 FY27 beat+raise (11/9) + onshoring/data-center demand + BofA PT $320 Buy (11/18). Non-defensive (beta ~1.11). Convert to trailing at +5% (~$267.63). Day 2, slipped on the market slide, thesis intact. |
| NOC | 18 | 544.37 | 542.31 | −0.38% | $9,761.58 | **−7% HARD (GTC)** `506.26` | 2026-10-23 | Northrop Grumman, defense/aerospace. Q3 beat+raise + record backlog; $1.6B PAC-3 MSE order (11/16); BTIG Buy PT $815. Convert to trailing at +5% (~$571.59). INTACT. |
| PG | 65 | 148.06 | 167.94 | +13.43% | $10,916.10 | **10% TRAILING (GTC)** floor `156.231` | 2026-10-08 | Procter & Gamble — staples diversifier. **Investor Day 11/19 was a non-event for the stock** (flat on the day). Floor above entry (profit locked). HOLD — stop handles both outcomes. |
| RSG | 44 | 218.00 | 246.49 | +13.07% | $10,845.56 | **10% TRAILING (GTC)** floor `231.111` | 2026-09-18 | Republic Services — defensive waste. Argus Buy PT $275 + JPM OW $295. Q3 beat + raised FY26, $5B buyback. HOLD. |
| SPY | 59 | 759.746 | 714.97 | −5.89% | $42,183.23 | **NONE — index-floor sleeve, deliberate no-stop carve-out** | 2026-08-10→11-06 | S&P 500 market floor (Lauren-approved Option B + same-day sweep). Own sleeve, EXEMPT from ≤20%/max-5/max-3-per-week; NO stop. ~44% of book. It IS the benchmark. (Alpaca mark 714.97; official daily-bar close 715.84 used for the benchmark return.) |

**Conviction sleeve: 4 of 5 — one open slot.** **Conviction buys used this week (11/16–11/20): 1 of 3.** **Cash buffer: 11.04%** ($10,495.23 — at the ~$10k cushion). Largest non-index single name PG $10,916.10 (11.48% of equity — well under the 20% cap; FERG 11.45%, RSG 11.41%, NOC 10.27%). Conviction stock mv FERG+NOC+PG+RSG $42,408.40 (44.60%); SPY sleeve $42,183.23 (44.36%). **Defensive count: 2 of 4** (PG, RSG) — FERG and NOC non-defensive, so the defensive cap still has room.

## Today's fills (2026-11-19)
- **At MARKET-OPEN: NONE.** At **MIDDAY: NONE.** At **CLOSE: NONE.** No buys all day (no name cleared 2 signals AND ≥70; no breaking catalyst), no sells (no −7% breach, no broken thesis), no hard→trailing conversions (neither hard-stop name is +5% yet), no SPY sweep (close run with market closed; cash also within one share of cushion). Alpaca closed-orders for 2026-11-19 = **0**.

## Risk checks (CLOSE 2026-11-19)
- **(a) Any position −7% or worse un-stopped?** NO. FERG −1.09%, NOC −0.38%, PG +13.43%, RSG +13.07% (all in range); SPY −5.89% (index, no stop by design). Nothing near −7% → no Perplexity news check triggered.
- **(b) Any position +5%+ needing hard→trailing conversion?** NO. The two HARD-stop names (FERG −1.09%, NOC −0.38%) are below the +5% line (FERG convert ~$267.63; NOC ~$571.59). PG/RSG already trail.
- **(c) Daily loss cap:** day **−1.40%** (DOWN) — NOT breached (inside the −3% cap).
- **(d) Sell signals?** NONE. All four theses INTACT; no −7% breach, no thesis break, no guidance cut.

## Stop-management state (open-orders — VERIFIED live 2026-11-19 CLOSE, exactly 4)
- **FERG −7% HARD** `ea91d0f9-6f6d-46c1-a665-b77c6efdc0ec` — stop **232.61**, GTC, resting. qty 44. Convert at +5% (~$267.63).
- **NOC −7% HARD** `59a67c62-0ec7-4d59-8315-66d94b9d3d7c` — stop **506.26**, GTC, resting. qty 18. Convert at +5% (~$571.59).
- **PG 10% TRAILING** `272e2864-58a7-471f-93ad-acf3914e5a18` — floor **156.231**, trail 10%, GTC, resting. qty 65.
- **RSG 10% TRAILING** `135c200e-fc09-4a37-95c1-f940b57ae0e3` — floor **231.111**, trail 10%, GTC, resting. qty 44.
- **SPY — NO STOP by design** (index-floor sleeve carve-out). qty 59 unencumbered.
- Confirmed **exactly 4 open orders total** — 2 hard stops (FERG, NOC) + 2 trailing (PG/RSG). SPY unencumbered. None fired today.

## Strategy status (CLOSE 2026-11-19)
- **Regime:** the relief bounce fully unwound — SPY round-tripped from +1.2% at the open to a −1.98% close, its fifth down session in six. Still narrow megacap-tech leadership, no confirmed base. Dec 9–10 FOMC ahead (~25bp move near-priced).
- **Traded this week:** FERG (1 of 3 conviction buys). One open slot (sleeve 4/5).
- **★ One open slot** — next buy must clear 2+ signals AND Conviction ≥70 at a clean entry; defensive cap has room (2/4) but prefer a non-defensive gate-clearer. PANW stays watch-only (~63, below gate) — only interesting on a 50dMA reclaim (~$366); don't chase. ADSK (B+ 72) stays DEFERRED on its own 11/24 earnings fence.
- **Events runway:** **Fri 11/20 is weekly-review day**; Dec 9–10 FOMC.

## Handoff → pre-market (Fri 2026-11-20; winter cron `0 12 UTC`; summer `0 11` rings ~57 min early → `--wait` holds to 7:00 AM ET)
- **Clock gate first:** `market_clock.py --slot pre-market --wait --claim --owner pre-market`.
- **Fri 11/20 is also WEEKLY-REVIEW day** (winter cron `0 22 UTC` = 5:00 PM ET). The weekly review owns the full week scorecard + Telegram push.
- **Re-verify live:** account/positions/open-orders/clock; confirm **exactly 4** open orders (FERG hard 232.61; NOC hard 506.26; RSG trail 231.111; PG trail 156.231); SPY (59 sh) unencumbered; daily loss-cap check.
- **FERG** −1.09% day 2 — hold on its hard stop; convert to trailing only at +5% (~$267.63). **NOC** −0.38%, hard→trailing only at +5% (~$571.59). PG/RSG floors ratchet automatically.
- **SPY sweep next open:** cash $10,495 is ~$495 above the $10k cushion = less than one SPY share → expect `action:none` unless a stop fires and frees cash (then sweep same day).
- **What would change the plan:** any held name hitting a stop; the afternoon slide extending into a sharper risk-off that pressures the loss cap (watch SPY and FERG's 232.61); a fresh Conviction ≥70 gate-clearer for the open slot.
