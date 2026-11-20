# Portfolio

**Last updated:** 2026-11-20 ~15:00 CT (**4:00 PM ET, MARKET-CLOSE routine**, Fri — **NO TRADES**). Clock gate: summer cron `0 20 UTC` rang ~56 min early; `market_clock.py --slot market-close --wait` held to **4:00 PM ET** → **DUE** ("0 min after the bell") → Alpaca `/v2/clock` **is_open=false** (bell rung, next_open 11/23) → confirmed DUE → **CLAIMED** (owner market-close, no prior claim today), claim pushed `HEAD:main` before the scorecard. 4 required keys non-empty; EQUIBLES empty → filing data skipped. Inbox **no Pending**; Astra **no proposals**. No last-chance SPY sweep (bell already rung → handed to next open; cash only ~$495 above cushion = <1 share anyway). Risk checks all clear (no −7% breach un-stopped, no +5% hard→trailing conversion due, loss cap −3% NOT hit — day −1.87%). Open orders **exactly 4** unchanged — **no stops fired today** (0 closed orders). Sleeve **4/5** (one open slot); weekly conviction buys **1/3** (week 11/16–11/20, done). **★ The weekly review (5:00 PM ET today) owns the official full-week scorecard + its own mandatory Telegram.** This close wrote + pushed the mandatory daily "How we're doing" scorecard. See research-log 2026-11-20 Day summary.

## Live snapshot (2026-11-20 16:00 ET — CLOSE, official)
- **Equity:** $93,360.13 · cash $10,495.23 (11.24%) · long_mv $82,864.90 · buying_power $274,002.63 (margin figure — this book does not borrow). status ACTIVE, trading_blocked false.
- **Day P/L:** **−$1,773.98 / −1.87%** (base 11/19 close equity $95,134.11 = Alpaca `last_equity`). DOWN, but loss cap (−3%) NOT breached.
- **SPY day:** 690.68 close (vs 715.84 on 11/19) → SPY **−3.52%** — a sharp risk-off session capped a brutal week for the index.
- **Day alpha:** **+1.65 pp** — BEATING the market today (defensive conviction names + cash cushion cushioned the fall while the index dropped harder).
- **Week-to-date (11/13 close base, official weekly is the 5pm review's job):** portfolio **−5.07% / −$4,980.52** vs SPY **−8.43%** → **WTD alpha +3.37 pp**. Losing, but losing far less than the market.

## Open positions (4 conviction stocks + 1 index-floor sleeve) — CLOSE marks 2026-11-20 16:00 ET
| Symbol | Shares | Avg Cost | Px | P/L % | MV | Stop | Entry Date | Thesis (1 line) |
|---|---|---|---|---|---|---|---|---|
| FERG | 44 | 250.12 | 240.620 | −3.80% | $10,587.28 | **−7% HARD (GTC)** `232.61` | 2026-11-18 | Ferguson — plumbing/HVAC/industrial distributor. Q1 FY27 beat+raise (11/9) + onshoring/data-center demand + BofA PT $320 Buy (11/18). Non-defensive (beta ~1.11). Convert to trailing at +5% (~$267.63). Day 3, slipped with the soft tape (~3.3% of room above its 232.61 stop), thesis intact. |
| NOC | 18 | 544.37 | 534.310 | −1.85% | $9,617.58 | **−7% HARD (GTC)** `506.26` | 2026-10-23 | Northrop Grumman, defense/aerospace. Q3 beat+raise + record backlog; $1.6B PAC-3 MSE order (11/16); BTIG Buy PT $815. Convert to trailing at +5% (~$571.59). INTACT. |
| PG | 65 | 148.06 | 169.545 | +14.51% | $11,020.42 | **10% TRAILING (GTC)** floor `156.231` | 2026-10-08 | Procter & Gamble — staples diversifier. Floor above entry (profit locked). HOLD — stop handles both outcomes. |
| RSG | 44 | 218.00 | 246.590 | +13.11% | $10,849.96 | **10% TRAILING (GTC)** floor `231.111` | 2026-09-18 | Republic Services — defensive waste. Argus Buy PT $275 + JPM OW $295. Q3 beat + raised FY26, $5B buyback. HOLD. |
| SPY | 59 | 759.746 | 691.280 | −9.01% | $40,785.52 | **NONE — index-floor sleeve, deliberate no-stop carve-out** | 2026-08-10→11-06 | S&P 500 market floor (Lauren-approved Option B + same-day sweep). Own sleeve, EXEMPT from ≤20%/max-5/max-3-per-week; NO stop. ~44% of book. It IS the benchmark. |

**Conviction sleeve: 4 of 5 — one open slot.** **Conviction buys used this week (11/16–11/20): 1 of 3 (week done).** **Cash buffer: 11.24%** ($10,495.23 — at the ~$10k cushion). Largest non-index single name PG $11,020.42 (11.80% of equity — well under the 20% cap; RSG 11.62%, FERG 11.34%, NOC 10.30%). Conviction stock mv FERG+NOC+PG+RSG $42,075.24 (45.07%); SPY sleeve $40,785.52 (43.69%). **Defensive count: 2 of 4** (PG, RSG) — FERG and NOC non-defensive, so the defensive cap still has room.

## Today's fills (2026-11-20)
- **At MARKET-OPEN: NONE.** DIS (the pre-market CONDITIONAL lead) stood down as an extended chase into a soft tape.
- **At MIDDAY: NONE.** No buy, no sell, no conversion, no sweep (`action:none`).
- **At CLOSE: NONE.** No last-chance sweep (bell already rung → handed to next open as a standing action; cash <1 SPY share above cushion anyway). **No stops fired** — Alpaca closed-orders count 0; open orders unchanged at exactly 4.

## Risk checks (CLOSE 2026-11-20)
- **(a) Any position −7% or worse un-stopped?** NO. FERG −3.80%, NOC −1.85%, PG +14.51%, RSG +13.11% (all in range); SPY −9.01% (index, no stop by design). Nothing near its −7% hard stop (FERG ~3.3% room above 232.61).
- **(b) Any position +5%+ needing hard→trailing conversion?** NO. The two HARD-stop names (FERG −3.80%, NOC −1.85%) are below the +5% line (FERG convert ~$267.63; NOC ~$571.59). PG/RSG already trail.
- **(c) Daily loss cap:** day **−1.87%** — NOT breached (−3% cap). Buffer held even on a sharp risk-off day.
- **(d) Sell signals?** NONE. All four theses INTACT; no −7% breach, no thesis break, no guidance cut.

## Stop-management state (open-orders — VERIFIED live 2026-11-20 CLOSE, exactly 4)
- **FERG −7% HARD** `ea91d0f9-6f6d-46c1-a665-b77c6efdc0ec` — stop **232.61**, GTC, resting. qty 44. Convert at +5% (~$267.63).
- **NOC −7% HARD** `59a67c62-0ec7-4d59-8315-66d94b9d3d7c` — stop **506.26**, GTC, resting. qty 18. Convert at +5% (~$571.59).
- **PG 10% TRAILING** `272e2864-58a7-471f-93ad-acf3914e5a18` — floor **156.231**, trail 10%, GTC, resting. qty 65.
- **RSG 10% TRAILING** `135c200e-fc09-4a37-95c1-f940b57ae0e3` — floor **231.111**, trail 10%, GTC, resting. qty 44.
- **SPY — NO STOP by design** (index-floor sleeve carve-out). qty 59 unencumbered.
- Confirmed **exactly 4 open orders total** — 2 hard stops (FERG, NOC) + 2 trailing (PG/RSG). SPY unencumbered. None fired today.

## Strategy status (CLOSE 2026-11-20)
- **Regime:** sharp risk-off — SPY −3.52% today, closing 690.68, the worst day of a brutal week (754→690, now seven down sessions in eight) after hawkish Fedspeak; yields near cycle highs. Dec 9–10 FOMC ahead.
- **Traded this week:** FERG (1 of 3 conviction buys). One open slot (sleeve 4/5). Week's buy budget done.
- **★ One open slot** — next buy must clear 2+ signals AND Conviction ≥70 at a **clean, non-extended** entry on a **settled** tape; defensive cap has room (2/4) but prefer a non-defensive gate-clearer. **DIS watch-only** — re-check for a genuine pullback / settled tape; do not chase. NVDA extended; PANW needs a ~$366 50-day reclaim; ADSK on its 11/24 earnings fence.
- **Events runway:** **★ Weekly review (5:00 PM ET today) owns the official full-week scorecard + its own mandatory Telegram.** Next trading day Mon 11/23. Dec 9–10 FOMC.

## Handoff → weekly review (today 5:00 PM ET) and next pre-market (Mon 2026-11-23)
- **Weekly review (5:00 PM ET, winter cron `0 22 UTC`; summer `0 21` rings early → `--wait` holds to 5:00 PM ET):** owns the OFFICIAL full-week scorecard + mandatory Telegram. WTD alpha **+3.37 pp** is the headline (port −5.07% vs SPY −8.43%, week base 11/13 close). Re-verify all numbers live.
- **Clock gate first (both):** `market_clock.py --slot <weekly-review|pre-market> --wait --claim`; Mon pre-market is research-only (market closed at wake).
- **Re-verify live Mon:** account/positions/open-orders/clock; confirm **exactly 4** open orders (FERG hard 232.61; NOC hard 506.26; RSG trail 231.111; PG trail 156.231); SPY (59 sh) unencumbered; daily loss-cap check.
- **FERG** −3.80% day 3 — hold on its hard stop 232.61 (~3.3% room above it); convert to trailing only at +5% (~$267.63). **NOC** −1.85%, convert at +5% (~$571.59). PG/RSG floors ratchet automatically.
- **DIS watch-only** — only re-engage on a genuine pullback into a clean entry on a settled tape; do NOT chase.
- **SPY sweep (standing action for Mon open):** cash $10,495 is ~$495 above the $10k cushion = less than one SPY share → expect `action:none` unless a stop fires and frees cash (then sweep same day).
- **What would change the plan:** any held name hitting a stop; the risk-off extending into a sharper drop that pressures the loss cap (watch SPY and FERG's 232.61); a fresh Conviction ≥70 gate-clearer at a clean entry for the open slot; the Dec 9–10 FOMC setup.
