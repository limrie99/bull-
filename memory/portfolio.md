# Portfolio

**Last updated:** 2026-11-19 ~12:00 CT display (**1:00 PM ET, MIDDAY routine**, Thu — **NO TRADES**). Clock gate: fired on the SUMMER cron (`0 17 UTC` = 12:05 PM ET, the daylight-saving early ring); `market_clock.py --slot midday` returned `status:EARLY` (wait ~24 min). Held via `--wait` to 18:00 UTC = 1:00 PM ET, then `--claim --owner midday` → **CLAIMED** (2026-11-19, owner midday, no prior claim). Did NOT shift the cron. Alpaca `/v2/clock` **is_open=true** (13:00 ET, next_close 16:00 ET) → open genuine. 4 required keys non-empty; EQUIBLES empty → filing data skipped. Inbox **no Pending**; Astra **no proposals**. Risk checks all clear (no −7% breach, no +5% hard→trailing conversion due, loss cap far off — intraday −0.93%, DOWN but well inside). SPY sweep `spy_floor.py` → **action:none** (cash within one SPY share of cushion). No new buys (no breaking catalyst; nothing clears the ≥70 gate). Sleeve **4/5** (one open slot); weekly conviction buys **1/3** (week 11/16–11/20). Open orders **exactly 4** unchanged. See research-log 2026-11-19 midday entry.

## Daily scorecard (2026-11-19 midday snapshot — intraday, official number is the close's)
- **Equity:** $95,540.99 · cash $10,495.23 (10.99%) · long_mv $85,045.76.
- **Intraday P/L:** **−$895.87 / −0.93%** (base 11/18 close equity $96,436.86, from Alpaca `last_equity`). DOWN but far from the −3% loss cap.
- **SPY today:** **−1.25%** (730.33 close 11/18 → 721.23 now) — this morning's relief bounce faded; tech gave back most of the pop.
- **Intraday alpha:** **+0.32 pp** — BEATING the market today (defensive book held while the index slid; PG/RSG barely budged). A reversal from the open, when we lagged the bounce.
- **Week-to-date (from Fri 11/13 close $98,340.65):** **−2.85%**; SPY week **−4.38%** (754.27 → 721.23); **week alpha +1.53 pp — still BEATING the market this week** (lead widened from +0.31 at the open as the bounce reversed).

## Open positions (4 conviction stocks + 1 index-floor sleeve) — live marks 2026-11-19 ~13:00 ET
| Symbol | Shares | Avg Cost | Px (live) | P/L % | MV | Stop | Entry Date | Thesis (1 line) |
|---|---|---|---|---|---|---|---|---|
| FERG | 44 | 250.12 | 248.63 | −0.60% | $10,939.72 | **−7% HARD (GTC)** `232.61` | 2026-11-18 | Ferguson — plumbing/HVAC/industrial distributor. Q1 FY27 beat+raise (11/9) + onshoring/data-center demand + BofA PT $320 Buy (11/18). Non-defensive (beta ~1.11). Convert to trailing at +5% (~$267.63). Day 2, flat. |
| NOC | 18 | 544.37 | 543.16 | −0.22% | $9,776.88 | **−7% HARD (GTC)** `506.26` | 2026-10-23 | Northrop Grumman, defense/aerospace. Q3 beat+raise + record backlog; $1.6B PAC-3 MSE order (11/16); BTIG Buy PT $815. Convert to trailing at +5% (~$571.59). INTACT. |
| PG | 65 | 148.06 | 168.26 | +13.64% | $10,936.90 | **10% TRAILING (GTC)** floor `156.231` | 2026-10-08 | Procter & Gamble — staples diversifier. **Investor Day TODAY Thu Nov 19, 2:00 PM ET.** Floor above entry (profit locked). HOLD — don't pre-trade; stop handles both outcomes. |
| RSG | 44 | 218.00 | 246.37 | +13.01% | $10,840.28 | **10% TRAILING (GTC)** floor `231.111` | 2026-09-18 | Republic Services — defensive waste. Argus Buy PT $275 + JPM OW $295. Q3 beat + raised FY26, $5B buyback. HOLD. |
| SPY | 59 | 759.75 | 721.23 | −5.07% | $42,552.57 | **NONE — index-floor sleeve, deliberate no-stop carve-out** | 2026-08-10→11-06 | S&P 500 market floor (Lauren-approved Option B + same-day sweep). Own sleeve, EXEMPT from ≤20%/max-5/max-3-per-week; NO stop. ~45% of book. It IS the benchmark. |

**Conviction sleeve: 4 of 5 — one open slot.** **Conviction buys used this week (11/16–11/20): 1 of 3.** **Cash buffer: 10.99%** ($10,495.23 — at the ~$10k cushion). Largest non-index single name FERG $10,939.72 (11.45% of equity — well under the 20% cap). Conviction stock mv FERG+NOC+PG+RSG $42,493.78 (44.48%); SPY sleeve $42,552.57 (44.54%). **Defensive count: 2 of 4** (PG, RSG) — FERG and NOC non-defensive, so the sleeve defensive cap still has room.

## Today's fills (2026-11-19)
- **At MARKET-OPEN: NONE.** At **MIDDAY: NONE.** No buys (no name clears 2 signals AND ≥70; no breaking catalyst), no sells (no −7% breach, no broken thesis), no hard→trailing conversions (neither hard-stop name is +5% yet), no SPY sweep (`action:none` — cash within one share of cushion).

## Risk checks (MIDDAY 2026-11-19)
- **(a) Any position −7% or worse un-stopped?** NO. FERG −0.60%, NOC −0.22%, PG +13.64%, RSG +13.01% (all in range); SPY −5.07% (index, no stop by design). Nothing near −7% → no Perplexity news check triggered.
- **(b) Any position +5%+ needing hard→trailing conversion?** NO. The two HARD-stop names (FERG −0.60%, NOC −0.22%) are below the +5% line (FERG convert ~$267.63; NOC ~$571.59). PG/RSG already trail.
- **(c) Daily loss cap:** intraday **−0.93%** (DOWN) — NOT breached (far inside the −3% cap). New buys would be allowed if a setup appeared.
- **(d) Sell signals?** NONE. All four theses INTACT; no −7% breach, no thesis break, no guidance cut.

## Stop-management state (open-orders — VERIFIED live 2026-11-19 MIDDAY, exactly 4)
- **FERG −7% HARD** `ea91d0f9-6f6d-46c1-a665-b77c6efdc0ec` — stop **232.61**, GTC, resting. qty 44. Convert at +5% (~$267.63).
- **NOC −7% HARD** `59a67c62-0ec7-4d59-8315-66d94b9d3d7c` — stop **506.26**, GTC, resting. qty 18. Convert at +5% (~$571.59).
- **PG 10% TRAILING** `272e2864-58a7-471f-93ad-acf3914e5a18` — floor **156.231**, trail 10%, GTC, resting. qty 65.
- **RSG 10% TRAILING** `135c200e-fc09-4a37-95c1-f940b57ae0e3` — floor **231.111**, trail 10%, GTC, resting. qty 44.
- **SPY — NO STOP by design** (index-floor sleeve carve-out). qty 59 unencumbered.
- Confirmed **exactly 4 open orders total** — 2 hard stops (FERG, NOC) + 2 trailing (PG/RSG). SPY unencumbered.

## Strategy status (MIDDAY 2026-11-19)
- **Regime:** this morning's tech-led relief bounce faded by midday — SPY round-tripped from +1.2% at the open to −1.25% now. Still narrow megacap-tech leadership, no confirmed reversal. Dec 9–10 FOMC ahead (~25bp move near-priced).
- **Traded this week:** FERG (1 of 3 conviction buys). One open slot (sleeve 4/5).
- **★ One open slot** — next buy must clear 2+ signals AND Conviction ≥70 at a clean entry; defensive cap has room (2/4) but prefer a non-defensive gate-clearer. PANW stays watch-only (~63, below gate) — only interesting on a 50dMA reclaim (~$366); don't chase. ADSK (B+ 72) stays DEFERRED on its own 11/24 earnings fence.
- **Events runway:** **PG Investor Day Thu 11/19, 2:00 PM ET (today, ~1h out)**; Dec 9–10 FOMC.

## Handoff → market-close (Thu 2026-11-19, winter cron `0 21 UTC`; summer `0 20` rings ~57 min early → `--wait` holds to 4:00 PM ET)
- **Clock gate first:** `market_clock.py --slot market-close --wait --claim --owner market-close`; the close is not the close while Alpaca `next_close` >20 min away.
- **MANDATORY daily "How we're doing" message + Telegram push** — never skipped, even on a quiet no-trade day.
- **Re-verify live:** account/positions/open-orders/clock; confirm **exactly 4** open orders (FERG hard 232.61; NOC hard 506.26; RSG trail 231.111; PG trail 156.231); SPY (59 sh) unencumbered; daily loss-cap check.
- **★ PG Investor Day 2:00 PM ET** — our biggest single catalyst; PG +13.6% on a trailing stop (floor 156.231), so an up readout ratchets the floor, a disappointment trails out mechanically. Don't pre-trade it; watch the readout into the close.
- **FERG** −0.60% day 2 — hold on its hard stop; convert to trailing only at +5% (~$267.63). **NOC** −0.22%, hard→trailing only at +5% (~$571.59). PG/RSG floors ratchet automatically.
- **SPY sweep at close:** cash $10,495 is ~$495 above the $10k cushion = less than one SPY share → expect `action:none` unless a stop fires intraday and frees cash (then sweep same day).
- **What would change the plan:** any held name hitting a stop; a strong/weak PG Investor Day; the faded bounce extending into a sharper risk-off that pressures the loss cap (watch SPY and FERG's 232.61).
