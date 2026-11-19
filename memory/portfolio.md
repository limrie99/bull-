# Portfolio

**Last updated:** 2026-11-19 ~08:34 CT display (**9:34 AM ET, MARKET-OPEN routine**, Thu — **NO TRADES**). Clock gate: `market_clock.py --slot market-open --claim` → **DUE** (09:33 ET, "3 min after the bell") → **CLAIMED** (stamp 2026-11-19, owner bull, no prior claim today). Alpaca `/v2/clock` **is_open=true** (next_close 2026-11-19 16:00) → open genuine. 4 required keys non-empty; EQUIBLES empty → filing data skipped. Inbox **no Pending**; Astra **no proposals**. Risk checks all clear (no −7% breach, no +5% hard→trailing conversion due, loss cap far off — intraday +0.22%, UP). SPY sweep `spy_floor.py` → **action:none** (cash within one SPY share of cushion). No new buys (no gate-clearer; PANW ~63, below ≥70 gate — would be chasing the relief bounce). Sleeve **4/5** (one open slot); weekly conviction buys **1/3** (week 11/16–11/20). Open orders **exactly 4** unchanged. See research-log 2026-11-19 market-open entry.

## Daily scorecard (2026-11-19 market-open snapshot — intraday, official number is the close's)
- **Equity:** $96,647.92 · cash $10,495.23 (10.86%) · long_mv $86,152.69.
- **Intraday P/L:** **+$211.06 / +0.22%** (base 11/18 close equity $96,436.86, from Alpaca `last_equity`). UP — loss cap far off.
- **SPY today:** **+1.18%** (730.33 close 11/18 → 738.98 now) — tech-led relief bounce.
- **Intraday alpha:** **−0.96 pp** — lagging the bounce (defensive book has no megacap-tech beta; SPY floor captures ~45% of the index move).
- **Week-to-date (from Fri 11/13 close $98,340.65):** **−1.72%**; SPY week **−2.03%** (754.27 → 738.98); **week alpha +0.31 pp — still BEATING the market this week** (lead narrowed from +1.21 as the index bounced).

## Open positions (4 conviction stocks + 1 index-floor sleeve) — live marks 2026-11-19 ~09:34 ET
| Symbol | Shares | Avg Cost | Px (live) | P/L % | MV | Stop | Entry Date | Thesis (1 line) |
|---|---|---|---|---|---|---|---|---|
| FERG | 44 | 250.12 | 250.80 | +0.27% | $11,035.20 | **−7% HARD (GTC)** `232.61` | 2026-11-18 | Ferguson — plumbing/HVAC/industrial distributor. Q1 FY27 beat+raise (11/9) + onshoring/data-center demand + BofA PT $320 Buy (11/18). Non-defensive (beta ~1.11). Convert to trailing at +5% (~$267.63). Day 2, modestly green. |
| NOC | 18 | 544.37 | 542.05 | −0.43% | $9,756.90 | **−7% HARD (GTC)** `506.26` | 2026-10-23 | Northrop Grumman, defense/aerospace. Q3 beat+raise + record backlog; $1.6B PAC-3 MSE order (11/16); BTIG Buy PT $815. Convert to trailing at +5% (~$571.59). INTACT. |
| PG | 65 | 148.06 | 167.63 | +13.22% | $10,895.95 | **10% TRAILING (GTC)** floor `156.231` | 2026-10-08 | Procter & Gamble — staples diversifier. **Investor Day TODAY Thu Nov 19, 2:00 PM ET.** Floor above entry (profit locked). HOLD — don't pre-trade; stop handles both outcomes. |
| RSG | 44 | 218.00 | 247.10 | +13.35% | $10,872.40 | **10% TRAILING (GTC)** floor `231.111` | 2026-09-18 | Republic Services — defensive waste. Argus Buy PT $275 + JPM OW $295. Q3 beat + raised FY26, $5B buyback. HOLD. |
| SPY | 59 | 759.75 | 738.98 | −2.73% | $43,599.81 | **NONE — index-floor sleeve, deliberate no-stop carve-out** | 2026-08-10→11-06 | S&P 500 market floor (Lauren-approved Option B + same-day sweep). Own sleeve, EXEMPT from ≤20%/max-5/max-3-per-week; NO stop. ~45% of book. It IS the benchmark. |

**Conviction sleeve: 4 of 5 — one open slot.** **Conviction buys used this week (11/16–11/20): 1 of 3.** **Cash buffer: 10.86%** ($10,495.23 — at the ~$10k cushion). Largest non-index single name PG $10,895.95 (11.27% of equity — well under the 20% cap). Conviction stock mv FERG+NOC+PG+RSG $42,560.45 (44.03%); SPY sleeve $43,599.81 (45.11%). **Defensive count: 2 of 4** (PG, RSG) — FERG and NOC non-defensive, so the sleeve defensive cap still has room.

## Today's fills (2026-11-19)
- **At MARKET-OPEN: NONE.** No buys (no name clears 2 signals AND ≥70; PANW ~63), no sells (no −7% breach, no broken thesis), no hard→trailing conversions (neither hard-stop name is +5% yet), no SPY sweep (`action:none` — cash within one share of cushion).

## Risk checks (MARKET-OPEN 2026-11-19)
- **(a) Any position −7% or worse un-stopped?** NO. FERG +0.27%, NOC −0.43%, PG +13.22%, RSG +13.35% (all in range); SPY −2.73% (index, no stop by design). Nothing near −7%.
- **(b) Any position +5%+ needing hard→trailing conversion?** NO. The two HARD-stop names (FERG +0.27%, NOC −0.43%) are below the +5% line (FERG convert ~$267.63; NOC ~$571.59). PG/RSG already trail.
- **(c) Daily loss cap:** intraday **+0.22%** (UP) — NOT breached. Full buffer intact; new buys would be allowed if a setup appeared.
- **(d) Sell signals?** NONE. All four theses INTACT; no −7% breach, no thesis break, no guidance cut.

## Stop-management state (open-orders — VERIFIED live 2026-11-19 MARKET-OPEN, exactly 4)
- **FERG −7% HARD** `ea91d0f9-6f6d-46c1-a665-b77c6efdc0ec` — stop **232.61**, GTC, resting. qty 44. Convert at +5% (~$267.63).
- **NOC −7% HARD** `59a67c62-0ec7-4d59-8315-66d94b9d3d7c` — stop **506.26**, GTC, resting. qty 18. Convert at +5% (~$571.59).
- **PG 10% TRAILING** `272e2864-58a7-471f-93ad-acf3914e5a18` — floor **156.231**, trail 10%, GTC, resting. qty 65.
- **RSG 10% TRAILING** `135c200e-fc09-4a37-95c1-f940b57ae0e3` — floor **231.111**, trail 10%, GTC, resting. qty 44.
- **SPY — NO STOP by design** (index-floor sleeve carve-out). qty 59 unencumbered.
- Confirmed **exactly 4 open orders total** — 2 hard stops (FERG, NOC) + 2 trailing (PG/RSG). SPY unencumbered.

## Strategy status (MARKET-OPEN 2026-11-19)
- **Regime:** tech-led relief bounce after four down sessions (SPY ~+1.2% intraday); narrow megacap-tech leadership, not a confirmed reversal. 10Y eased a touch. Dec 9–10 FOMC ahead (~25bp move near-priced).
- **Traded this week:** FERG (1 of 3 conviction buys). One open slot (sleeve 4/5).
- **★ One open slot** — next buy must clear 2+ signals AND Conviction ≥70 at a clean entry; defensive cap has room (2/4) but prefer a non-defensive gate-clearer. PANW stays watch-only (~63, below gate) — only interesting on a 50dMA reclaim (~$366); don't chase the bounce. ADSK (B+ 72) stays DEFERRED on its own 11/24 earnings fence.
- **Events runway:** **PG Investor Day Thu 11/19, 2:00 PM ET (today)**; Dec 9–10 FOMC.

## Handoff → midday (Thu 2026-11-19, winter cron `0 18 UTC`; summer `0 17` rings ~57 min early → `--wait` holds to 1:00 PM ET)
- **Clock gate first:** `market_clock.py --slot midday --wait --claim --owner midday`; confirm Alpaca is_open=true before claiming.
- **Re-verify live:** account/positions/open-orders/clock; confirm **exactly 4** open orders (FERG hard 232.61; NOC hard 506.26; RSG trail 231.111; PG trail 156.231); SPY (59 sh) unencumbered; daily loss-cap check.
- **★ PG Investor Day 2:00 PM ET** — our biggest single catalyst; PG +13% on a trailing stop (floor 156.231), so an up readout ratchets the floor, a disappointment trails out mechanically. Don't pre-trade it; watch the readout.
- **FERG** +0.27% day 2 — hold on its hard stop; convert to trailing only at +5% (~$267.63). **NOC** −0.43%, hard→trailing only at +5% (~$571.59). PG/RSG floors ratchet automatically.
- **SPY sweep:** cash $10,495 is ~$495 above the $10k cushion = less than one SPY share → expect `action:none` unless a stop fires and frees cash.
- **What would change the plan:** any held name hitting a stop; a strong/weak PG Investor Day; a sharp reversal of the relief bounce (watch the loss cap). **Market-close owns the mandatory "How we're doing" message + Telegram, written only when `market_clock.py --slot market-close` says DUE (winter `0 21`, not early summer `0 20`).**
