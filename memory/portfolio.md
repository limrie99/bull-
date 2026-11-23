# Portfolio

**Last updated:** 2026-11-23 ~08:33 CT (**9:32 AM ET, MARKET-OPEN routine**, Mon — **NO TRADES**). Clock gate: winter cron `30 14 UTC` rang on time (09:32 ET); `market_clock.py --slot market-open --wait --claim` → **DUE** ("2.7 min after the bell") → Alpaca `/v2/clock` **is_open=true** (next_close 16:00 ET) → confirmed DUE → **CLAIMED** (owner market-open, no prior claim today), claim committed with this run's memory push `HEAD:main`. 4 required keys non-empty; EQUIBLES empty → filing data skipped. Inbox **no Pending**; Astra **no proposals**. No stock buy (pre-market handoff = no gate-clearer; today is a sharp relief-rally gap-up, the opposite of a clean non-extended entry — do NOT chase). No SPY sweep (`spy_floor.py` → `action:none`, cash ~$495 above cushion = <1 share). Risk checks all clear (no −7% breach un-stopped, no +5% hard→trailing conversion due, loss cap not in play — day is UP +2.15%). Open orders **exactly 4** unchanged — **no stops fired** (positions match Fri close exactly). Sleeve **4/5** (one open slot); weekly conviction buys **0/3** (new week 11/23–11/28). No Telegram push (market-open no-trade is not a push event). See research-log 2026-11-23 market-open.

## Live snapshot (2026-11-23 09:32 ET — MARKET-OPEN)
- **Equity:** $95,263.97 · cash $10,495.23 (11.02%) · long_mv $84,768.74 · buying_power $279,333.38 (margin figure — this book does not borrow). status ACTIVE, trading_blocked false.
- **Day P/L:** **+$2,006.08 / +2.15%** (base = Fri 11/20 close equity $93,257.89 = Alpaca `last_equity`).
- **SPY day:** 721.46 (vs 690.68 Fri close) → SPY **+4.46%** — a sharp relief-rally bounce after last week's rout.
- **Day alpha:** **−2.31 pp** — LAGGING today. The mirror image of Friday: our defensive book + cash cushion trails on a strong up day, exactly the sleeve-balance trade-off. The index floor (44% of book) is the main catch-up lever on green days.
- **Week-to-date (new week, day 1):** today's numbers are the week so far.

## Open positions (4 conviction stocks + 1 index-floor sleeve) — MARKET-OPEN marks 2026-11-23 09:32 ET
| Symbol | Shares | Avg Cost | Px | P/L % | MV | Stop | Entry Date | Thesis (1 line) |
|---|---|---|---|---|---|---|---|---|
| FERG | 44 | 250.12 | 248.255 | −0.75% | $10,923.22 | **−7% HARD (GTC)** `232.61` | 2026-11-18 | Ferguson — plumbing/HVAC/industrial distributor. Q1 FY27 beat+raise (11/9) + onshoring/data-center demand + BofA PT $320 Buy (11/18). Non-defensive (beta ~1.11). Convert to trailing at +5% (~$262.63). Day 4, bounced with the tape, thesis intact (~6.7% room above its 232.61 stop). |
| NOC | 18 | 544.37 | 534.785 | −1.76% | $9,626.13 | **−7% HARD (GTC)** `506.26` | 2026-10-23 | Northrop Grumman, defense/aerospace. Q3 beat+raise + record backlog; $1.6B PAC-3 MSE order (11/16); BTIG Buy PT $815. Convert to trailing at +5% (~$571.59). INTACT. |
| PG | 65 | 148.06 | 167.83 | +13.35% | $10,908.95 | **10% TRAILING (GTC)** floor `156.231` | 2026-10-08 | Procter & Gamble — staples diversifier. Floor above entry (profit locked). HOLD — stop handles both outcomes. |
| RSG | 44 | 218.00 | 244.2422 | +12.04% | $10,746.66 | **10% TRAILING (GTC)** floor `231.111` | 2026-09-18 | Republic Services — defensive waste. Argus Buy PT $275 + JPM OW $295. Q3 beat + raised FY26, $5B buyback. HOLD. |
| SPY | 59 | 759.746 | 721.46 | −5.04% | $42,566.14 | **NONE — index-floor sleeve, deliberate no-stop carve-out** | 2026-08-10→11-06 | S&P 500 market floor (Lauren-approved Option B + same-day sweep). Own sleeve, EXEMPT from ≤20%/max-5/max-3-per-week; NO stop. ~45% of book. It IS the benchmark. |

**Conviction sleeve: 4 of 5 — one open slot.** **Conviction buys used this week (11/23–11/28): 0 of 3.** **Cash buffer: 11.02%** ($10,495.23 — at the ~$10k cushion). Largest non-index single name FERG $10,923.22 (11.47% of equity — well under the 20% cap; PG 11.45%, RSG 11.28%, NOC 10.11%). Conviction stock mv FERG+NOC+PG+RSG $42,204.96 (44.30%); SPY sleeve $42,566.14 (44.68%). **Defensive count: 2 of 4** (PG, RSG) — FERG and NOC non-defensive, so the defensive cap still has room.

## Today's fills (2026-11-23)
- **At MARKET-OPEN: NONE.** No buy (no gate-clearer; relief-rally gap-up is not a clean non-extended entry — do not chase). No sell (all four theses intact, nothing near a stop). No conversion (FERG/NOC below +5%). No SPY sweep (`action:none`). **No stops fired** — positions and open-orders match Fri close exactly.

## Risk checks (MARKET-OPEN 2026-11-23)
- **(a) Any position −7% or worse un-stopped?** NO. FERG −0.75%, NOC −1.76%, PG +13.35%, RSG +12.04% (all in range); SPY −5.04% (index, no stop by design). FERG has ~6.7% room above its 232.61 stop.
- **(b) Any position +5%+ needing hard→trailing conversion?** NO. The two HARD-stop names (FERG −0.75%, NOC −1.76%) are below the +5% line (FERG convert ~$262.63; NOC ~$571.59). PG/RSG already trail.
- **(c) Daily loss cap:** day is **UP +2.15%** — not in play. New buys would be allowed on the cap basis, but none clears the gate.
- **(d) Sell signals?** NONE. All four theses INTACT; no −7% breach, no thesis break, no guidance cut, no overnight sell trigger.

## Stop-management state (open-orders — VERIFIED live 2026-11-23 MARKET-OPEN, exactly 4)
- **FERG −7% HARD** `ea91d0f9-6f6d-46c1-a665-b77c6efdc0ec` — stop **232.61**, GTC, resting. qty 44. Convert at +5% (~$262.63).
- **NOC −7% HARD** `59a67c62-0ec7-4d59-8315-66d94b9d3d7c` — stop **506.26**, GTC, resting. qty 18. Convert at +5% (~$571.59).
- **PG 10% TRAILING** `272e2864-58a7-471f-93ad-acf3914e5a18` — floor **156.231**, trail 10%, GTC, resting. qty 65.
- **RSG 10% TRAILING** `135c200e-fc09-4a37-95c1-f940b57ae0e3` — floor **231.111**, trail 10%, GTC, resting. qty 44.
- **SPY — NO STOP by design** (index-floor sleeve carve-out). qty 59 unencumbered.
- Confirmed **exactly 4 open orders total** — 2 hard stops (FERG, NOC) + 2 trailing (PG/RSG). SPY unencumbered. None fired.

## Strategy status (MARKET-OPEN 2026-11-23)
- **Regime:** sharp relief rally — SPY +4.46% at the open (721.46 vs Fri 690.68) after last week's rout (754→690). A bounce, not an all-clear: rates stay elevated and the Dec 9–10 FOMC is the next big event. Do NOT chase the gap.
- **Traded this week:** nothing yet (new week 11/23–11/28). Buy budget 0/3; one open slot (sleeve 4/5).
- **★ One open slot** — next buy must clear 2+ signals AND Conviction ≥70 at a **clean, non-extended** entry on a **settled** tape; today's gap-up is the opposite. Defensive cap has room (2/4) but prefer a non-defensive gate-clearer. **Watch-list triggers:** SCHW on a ~$95 50-day reclaim + a 2nd clean signal; DIS on a genuine pullback (not a chase); PANW on a ~$366 50-day reclaim (verify the Q1 print). ADSK deferred past its Tue 11/24 earnings.
- **Events runway:** Next routine midday (1:00 PM ET). Dec 9–10 FOMC.

## Handoff → midday (today 1:00 PM ET)
- **Clock gate first:** `market_clock.py --slot midday --wait --claim --owner midday`; confirm Alpaca is_open=true before claiming.
- **Re-verify live:** account/positions/open-orders/clock; confirm **exactly 4** open orders (FERG hard 232.61; NOC hard 506.26; RSG trail 231.111; PG trail 156.231); SPY (59) unencumbered; daily loss-cap check.
- **SPY same-day sweep (standing action):** run `scripts/spy_floor.py` live; cash ~$495 above cushion = <1 SPY share → expect `action:none` unless a stop fires and frees cash (then sweep SAME day).
- **FERG** −0.75% day 4 — hold on its hard stop 232.61 (~6.7% room); convert to trailing only at +5% (~$262.63). **NOC** −1.76%, convert at +5% (~$571.59). PG/RSG floors ratchet automatically.
- **DIS / SCHW / PANW watch-only** — only engage on a clean, non-extended entry on a SETTLED tape with 2+ verified signals AND Conviction ≥70; do NOT chase the relief bounce.
- **What would change the plan:** any held name hitting a stop; the relief rally reversing hard and pressuring FERG's 232.61 / the loss cap; a non-defensive name verifying clean at a non-extended entry for the open slot; the Dec 9–10 FOMC setup.
