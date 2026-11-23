# Portfolio

**Last updated:** 2026-11-23 ~13:00 CT (**1:00 PM ET, MIDDAY routine**, Mon — **NO TRADES, STEADY**). Clock gate: summer cron `0 17 UTC` rang ~55 min early (11:00 ET); `market_clock.py --slot midday --wait --claim --owner midday` held to **13:00 ET** → **DUE** ("0 min after the bell") → Alpaca `/v2/clock` **is_open=true** (next_close 16:00 ET) → confirmed DUE → **CLAIMED** (owner midday, no prior claim today), claim committed + pushed `HEAD:main` (1e439a5..7eddd3e) BEFORE any order. 4 required keys non-empty; EQUIBLES empty → filing data skipped. Inbox **no Pending**; Astra **no proposals**. No stock buy (no breaking catalyst; relief-rally continuation = do NOT chase). No SPY sweep (`spy_floor.py` → `action:none`, cash ~$495 above cushion = <1 share). Risk checks all clear (no −7% breach un-stopped; no +5% hard→trailing conversion due — FERG +1.28%, NOC −0.83% both below the +5% line; loss cap not in play, day is UP +2.76%). Open orders **exactly 4** unchanged — **no stops fired** (positions match the open exactly). Sleeve **4/5** (one open slot); weekly conviction buys **0/3** (new week 11/23–11/28). No Telegram push (quiet midday is not a push event; the close owns the mandatory daily message). See research-log 2026-11-23 midday.

## Live snapshot (2026-11-23 13:00 ET — MIDDAY)
- **Equity:** $95,835.91 · cash $10,495.23 (10.95%) · long_mv $85,340.68 · buying_power $280,934.82 (margin figure — this book does not borrow). status ACTIVE, trading_blocked false.
- **Day P/L:** **+$2,578.02 / +2.76%** (base = Fri 11/20 close equity $93,257.89 = Alpaca `last_equity`).
- **SPY day:** 722.58 latest trade (vs 690.68 Fri 11/20 close) → SPY **+4.62%** — the relief-rally bounce extending from the open.
- **Day alpha:** **−1.86 pp** — LAGGING today (narrowed from −2.31 at the open as FERG turned green). Same sleeve-balance trade-off as the open: our defensive book + cash cushion trails a strong up day. The SPY sleeve (44% of book) is the main catch-up lever on green days and is doing its job (SPY +4.6%).
- **Week-to-date (new week, day 1):** today's numbers are the week so far (+2.76% vs SPY +4.62%, alpha −1.86 pp).

## Open positions (4 conviction stocks + 1 index-floor sleeve) — MIDDAY marks 2026-11-23 13:00 ET
| Symbol | Shares | Avg Cost | Px | P/L % | MV | Stop | Entry Date | Thesis (1 line) |
|---|---|---|---|---|---|---|---|---|
| FERG | 44 | 250.12 | 253.32 | +1.28% | $11,146.08 | **−7% HARD (GTC)** `232.61` | 2026-11-18 | Ferguson — plumbing/HVAC/industrial distributor. Q1 FY27 beat+raise (11/9) + onshoring/data-center demand + BofA PT $320 Buy (11/18). Non-defensive (beta ~1.11). Convert to trailing at +5% (~$262.63). Day 4, turned green with the tape, thesis intact. |
| NOC | 18 | 544.37 | 539.86 | −0.83% | $9,717.48 | **−7% HARD (GTC)** `506.26` | 2026-10-23 | Northrop Grumman, defense/aerospace. Q3 beat+raise + record backlog; $1.6B PAC-3 MSE order (11/16); BTIG Buy PT $815. Convert to trailing at +5% (~$571.59). INTACT. |
| PG | 65 | 148.06 | 170.09 | +14.88% | $11,055.85 | **10% TRAILING (GTC)** floor `156.231` | 2026-10-08 | Procter & Gamble — staples diversifier. Floor above entry (profit locked). HOLD — stop handles both outcomes. |
| RSG | 44 | 218.00 | 245.38 | +12.56% | $10,796.72 | **10% TRAILING (GTC)** floor `231.111` | 2026-09-18 | Republic Services — defensive waste. Argus Buy PT $275 + JPM OW $295. Q3 beat + raised FY26, $5B buyback. HOLD. |
| SPY | 59 | 759.746 | 722.39 | −4.92% | $42,621.01 | **NONE — index-floor sleeve, deliberate no-stop carve-out** | 2026-08-10→11-06 | S&P 500 market floor (Lauren-approved Option B + same-day sweep). Own sleeve, EXEMPT from ≤20%/max-5/max-3-per-week; NO stop. ~44% of book. It IS the benchmark. |

**Conviction sleeve: 4 of 5 — one open slot.** **Conviction buys used this week (11/23–11/28): 0 of 3.** **Cash buffer: 10.95%** ($10,495.23 — at the ~$10k cushion). Largest non-index single name FERG $11,146.08 (11.63% of equity — well under the 20% cap; PG 11.54%, RSG 11.27%, NOC 10.14%). Conviction stock mv FERG+NOC+PG+RSG $42,716.13 (44.57%); SPY sleeve $42,621.01 (44.47%). **Defensive count: 2 of 4** (PG, RSG) — FERG and NOC non-defensive, so the defensive cap still has room.

## Today's fills (2026-11-23)
- **At MARKET-OPEN: NONE.** At **MIDDAY: NONE.** No buy (no breaking catalyst; relief-rally continuation is not a clean non-extended entry). No sell (all four theses intact, nothing near a stop). No conversion (FERG +1.28% / NOC −0.83% both below +5%). No SPY sweep (`action:none`). **No stops fired** — positions and open-orders match the open exactly.

## Risk checks (MIDDAY 2026-11-23)
- **(a) Any position −7% or worse un-stopped?** NO. FERG +1.28%, NOC −0.83%, PG +14.88%, RSG +12.56% (all in range); SPY −4.92% (index, no stop by design). No Perplexity 4-hr news check triggered.
- **(b) Any position +5%+ needing hard→trailing conversion?** NO. The two HARD-stop names (FERG +1.28%, NOC −0.83%) are below the +5% line (FERG convert ~$262.63; NOC ~$571.59). PG/RSG already trail.
- **(c) Daily loss cap:** day is **UP +2.76%** — not in play. New buys would be allowed on the cap basis, but none clears the gate.
- **(d) Sell signals?** NONE. All four theses INTACT; no −7% breach, no thesis break, no guidance cut.

## Stop-management state (open-orders — VERIFIED live 2026-11-23 MIDDAY, exactly 4)
- **FERG −7% HARD** `ea91d0f9-6f6d-46c1-a665-b77c6efdc0ec` — stop **232.61**, GTC, resting. qty 44. Convert at +5% (~$262.63).
- **NOC −7% HARD** `59a67c62-0ec7-4d59-8315-66d94b9d3d7c` — stop **506.26**, GTC, resting. qty 18. Convert at +5% (~$571.59).
- **PG 10% TRAILING** `272e2864-58a7-471f-93ad-acf3914e5a18` — floor **156.231**, trail 10%, GTC, resting. qty 65.
- **RSG 10% TRAILING** `135c200e-fc09-4a37-95c1-f940b57ae0e3` — floor **231.111**, trail 10%, GTC, resting. qty 44.
- **SPY — NO STOP by design** (index-floor sleeve carve-out). qty 59 unencumbered.
- Confirmed **exactly 4 open orders total** — 2 hard stops (FERG, NOC) + 2 trailing (PG/RSG). SPY unencumbered. None fired.

## Strategy status (MIDDAY 2026-11-23)
- **Regime:** relief rally extending — SPY +4.62% midday (722.58 vs Fri 690.68) after last week's rout (754→690). A bounce, not an all-clear: rates stay elevated and the Dec 9–10 FOMC is the next big event. Do NOT chase the gap.
- **Traded this week:** nothing yet (new week 11/23–11/28). Buy budget 0/3; one open slot (sleeve 4/5).
- **★ One open slot** — next buy must clear 2+ signals AND Conviction ≥70 at a **clean, non-extended** entry on a **settled** tape; a strong up day is the opposite. Defensive cap has room (2/4) but prefer a non-defensive gate-clearer. **Watch-list triggers:** SCHW on a ~$95 50-day reclaim + a 2nd clean signal; DIS on a genuine pullback (not a chase); PANW on a ~$366 50-day reclaim (verify the Q1 print). ADSK deferred past its Tue 11/24 earnings.
- **Events runway:** Next routine market-close (4:00 PM ET — owns the mandatory daily "How we're doing" message + Telegram). Dec 9–10 FOMC.

## Handoff → market-close (today 4:00 PM ET)
- **Clock gate first:** `market_clock.py --slot market-close --wait --claim --owner market-close`; the close is not the close while Alpaca `next_close` >20 min away.
- **MANDATORY daily "How we're doing" message + Telegram push** at the close — never skipped, even on this quiet no-trade day. Lead with the beginner scorecard (day $ and %, vs SPY, ahead/behind). Today's story: we're UP strongly (+2.76%) but LAGGING the market's bigger bounce (+4.6%) — the mirror image of last week, when our steadier book BEAT a falling market. Frame it as the deliberate trade-off.
- **Re-verify live:** account/positions/open-orders/clock; confirm **exactly 4** open orders (FERG hard 232.61; NOC hard 506.26; RSG trail 231.111; PG trail 156.231); SPY (59) unencumbered; daily loss-cap check.
- **SPY same-day sweep (standing action, if market still open):** run `scripts/spy_floor.py` live; cash ~$495 above cushion = <1 SPY share → expect `action:none` unless a stop fires and frees cash (then sweep SAME day).
- **FERG** +1.28% day 4 — hold on its hard stop 232.61; convert to trailing only at +5% (~$262.63). **NOC** −0.83%, convert at +5% (~$571.59). PG/RSG floors ratchet automatically.
- **DIS / SCHW / PANW watch-only** — only engage on a clean, non-extended entry on a SETTLED tape with 2+ verified signals AND Conviction ≥70; do NOT chase the relief bounce.
- **What would change the plan:** any held name hitting a stop; the relief rally reversing hard into the close and pressuring FERG's 232.61 / the loss cap; a non-defensive name verifying clean at a non-extended entry for the open slot; the Dec 9–10 FOMC setup.
