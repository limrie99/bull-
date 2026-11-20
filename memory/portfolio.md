# Portfolio

**Last updated:** 2026-11-20 ~12:00 CT (**1:00 PM ET, MIDDAY routine**, Fri — **NO TRADES**). Clock gate: summer cron `0 17 UTC` rang ~60 min early; `market_clock.py --slot midday --wait` → **DUE** ("0 min after the bell", wait 0) → Alpaca `/v2/clock` **is_open=true** (13:00 ET, next_close 16:00) → `--clock-is-open true` DUE → **CLAIMED** (owner midday, no prior claim today), claim pushed `HEAD:main` before any order. 4 required keys non-empty; EQUIBLES empty → filing data skipped. Inbox **no Pending**; Astra **no proposals**. Risk checks all clear (no −7% breach, no +5% hard→trailing conversion due, loss cap far off — intraday −0.85%). SPY sweep `action:none` (cash within one SPY share of the $10k cushion). Open orders **exactly 4** unchanged — no stops fired. Sleeve **4/5** (one open slot); weekly conviction buys **1/3** (week 11/16–11/20, day 5). **DIS stays watch-only** (stood down at the open as an extended chase). **★ Weekly review (5:00 PM ET today) owns the official full-week scorecard + its mandatory Telegram; the 4:00 PM ET close owns the mandatory daily "How we're doing" push.** See research-log 2026-11-20 midday.

## Live snapshot (2026-11-20 13:00 ET — MIDDAY, intraday)
- **Equity:** $94,326.16 · cash $10,495.23 (11.13%) · long_mv $83,830.93 · buying_power $276,707.52 (margin figure — this book does not borrow). status ACTIVE, trading_blocked false.
- **Intraday P/L:** **−$807.95 / −0.85%** (base 11/19 close equity $95,134.11 = Alpaca `last_equity`). DOWN modestly, full loss-cap buffer (−3% far off).
- **SPY intraday:** ~700.09 last trade (vs 715.84 official close 11/19) → SPY **−2.20%** intraday — the soft/risk-off tape deepened through the week.
- **Intraday alpha:** **≈ +1.35 pp** — BEATING the market intraday (defensive book + cash cushion hold up while the index keeps bleeding). WTD alpha ≈ +3.10 pp. Official scorecard is the weekly review / close's job.

## Open positions (4 conviction stocks + 1 index-floor sleeve) — MIDDAY marks 2026-11-20 13:00 ET
| Symbol | Shares | Avg Cost | Px | P/L % | MV | Stop | Entry Date | Thesis (1 line) |
|---|---|---|---|---|---|---|---|---|
| FERG | 44 | 250.12 | 243.695 | −2.57% | $10,722.58 | **−7% HARD (GTC)** `232.61` | 2026-11-18 | Ferguson — plumbing/HVAC/industrial distributor. Q1 FY27 beat+raise (11/9) + onshoring/data-center demand + BofA PT $320 Buy (11/18). Non-defensive (beta ~1.11). Convert to trailing at +5% (~$267.63). Day 3, slipped with the soft tape (~4.6% of room above its 232.61 stop), thesis intact. |
| NOC | 18 | 544.37 | 540.405 | −0.73% | $9,727.29 | **−7% HARD (GTC)** `506.26` | 2026-10-23 | Northrop Grumman, defense/aerospace. Q3 beat+raise + record backlog; $1.6B PAC-3 MSE order (11/16); BTIG Buy PT $815. Convert to trailing at +5% (~$571.59). INTACT. |
| PG | 65 | 148.06 | 170.055 | +14.85% | $11,053.58 | **10% TRAILING (GTC)** floor `156.231` | 2026-10-08 | Procter & Gamble — staples diversifier. Investor Day 11/19 was a non-event for the stock; now firming. Floor above entry (profit locked). HOLD — stop handles both outcomes. |
| RSG | 44 | 218.00 | 249.370 | +14.39% | $10,972.28 | **10% TRAILING (GTC)** floor `231.111` | 2026-09-18 | Republic Services — defensive waste. Argus Buy PT $275 + JPM OW $295. Q3 beat + raised FY26, $5B buyback. HOLD. |
| SPY | 59 | 759.746 | 700.390 | −7.81% | $41,323.01 | **NONE — index-floor sleeve, deliberate no-stop carve-out** | 2026-08-10→11-06 | S&P 500 market floor (Lauren-approved Option B + same-day sweep). Own sleeve, EXEMPT from ≤20%/max-5/max-3-per-week; NO stop. ~44% of book. It IS the benchmark. |

**Conviction sleeve: 4 of 5 — one open slot.** **Conviction buys used this week (11/16–11/20): 1 of 3.** **Cash buffer: 11.13%** ($10,495.23 — at the ~$10k cushion). Largest non-index single name PG $11,053.58 (11.72% of equity — well under the 20% cap; RSG 11.63%, FERG 11.37%, NOC 10.31%). Conviction stock mv FERG+NOC+PG+RSG $42,475.73 (45.03%); SPY sleeve $41,323.01 (43.81%). **Defensive count: 2 of 4** (PG, RSG) — FERG and NOC non-defensive, so the defensive cap still has room.

## Today's fills (2026-11-20)
- **At MARKET-OPEN: NONE.** DIS (the pre-market CONDITIONAL lead) stood down as an extended chase into a soft tape.
- **At MIDDAY: NONE.** No buy (no breaking catalyst; nothing clears the ≥70 gate on a clean entry in the soft tape), no sell (no −7% breach, no broken thesis), no hard→trailing conversion (neither hard-stop name is +5% yet), no SPY sweep (`action:none`, cash within one share of cushion). Alpaca open-orders unchanged at exactly 4; no stop fired.

## Risk checks (MIDDAY 2026-11-20)
- **(a) Any position −7% or worse un-stopped?** NO. FERG −2.57%, NOC −0.73%, PG +14.85%, RSG +14.39% (all in range); SPY −7.81% (index, no stop by design). Nothing near the −7% hard → no Perplexity news check triggered.
- **(b) Any position +5%+ needing hard→trailing conversion?** NO. The two HARD-stop names (FERG −2.57%, NOC −0.73%) are below the +5% line (FERG convert ~$267.63; NOC ~$571.59). PG/RSG already trail.
- **(c) Daily loss cap:** intraday **−0.85%** — NOT breached. New buys would be allowed if a clean setup appeared; none did.
- **(d) Sell signals?** NONE. All four theses INTACT; no −7% breach, no thesis break, no guidance cut.

## Stop-management state (open-orders — VERIFIED live 2026-11-20 MIDDAY, exactly 4)
- **FERG −7% HARD** `ea91d0f9-6f6d-46c1-a665-b77c6efdc0ec` — stop **232.61**, GTC, resting. qty 44. Convert at +5% (~$267.63).
- **NOC −7% HARD** `59a67c62-0ec7-4d59-8315-66d94b9d3d7c` — stop **506.26**, GTC, resting. qty 18. Convert at +5% (~$571.59).
- **PG 10% TRAILING** `272e2864-58a7-471f-93ad-acf3914e5a18` — floor **156.231**, trail 10%, GTC, resting. qty 65.
- **RSG 10% TRAILING** `135c200e-fc09-4a37-95c1-f940b57ae0e3` — floor **231.111**, trail 10%, GTC, resting. qty 44.
- **SPY — NO STOP by design** (index-floor sleeve carve-out). qty 59 unencumbered.
- Confirmed **exactly 4 open orders total** — 2 hard stops (FERG, NOC) + 2 trailing (PG/RSG). SPY unencumbered. None fired.

## Strategy status (MIDDAY 2026-11-20)
- **Regime:** soft/risk-off deepened — SPY −2.20% intraday and bleeding all week (754→700, six down sessions in seven) after hawkish Fedspeak; yields near cycle highs. Dec 9–10 FOMC ahead.
- **Traded this week:** FERG (1 of 3 conviction buys). One open slot (sleeve 4/5).
- **★ One open slot** — next buy must clear 2+ signals AND Conviction ≥70 at a **clean, non-extended** entry on a settled tape; defensive cap has room (2/4) but prefer a non-defensive gate-clearer. **DIS watch-only** — re-check for a genuine pullback / settled tape; do not chase. NVDA extended; PANW needs a ~$366 50-day reclaim; ADSK DEFERRED on its 11/24 earnings fence.
- **Events runway:** **★ Fri 11/20 close (4:00 PM ET) owns the mandatory daily push; weekly review (5:00 PM ET) owns the official full-week scorecard + its own mandatory Telegram.** Dec 9–10 FOMC.

## Handoff → market-close / weekly review (Fri 2026-11-20; close winter cron `0 21 UTC`, weekly `0 22 UTC`; summer `0 20`/`0 21` ring early → `--wait` holds to 4:00/5:00 PM ET)
- **Clock gate first:** `market_clock.py --slot market-close --wait --claim --owner market-close`; confirm Alpaca `next_close` ≤20 min before treating it as the close.
- **MANDATORY daily "How we're doing" message + Telegram push** at the close — never skipped. **Weekly review owns the official full-week scorecard + its own mandatory Telegram** — week alpha is the headline (+3.10 pp intraday and widening).
- **Re-verify live:** account/positions/open-orders/clock; confirm **exactly 4** open orders (FERG hard 232.61; NOC hard 506.26; RSG trail 231.111; PG trail 156.231); SPY (59 sh) unencumbered; daily loss-cap check.
- **FERG** −2.57% day 3 — hold on its hard stop 232.61 (~4.6% room above it); convert to trailing only at +5% (~$267.63). **NOC** −0.73%, convert at +5% (~$571.59). PG/RSG floors ratchet automatically.
- **DIS watch-only** — only re-engage on a genuine pullback into a clean entry on a settled tape; do NOT chase.
- **SPY sweep:** cash $10,495 is ~$495 above the $10k cushion = less than one SPY share → expect `action:none` unless a stop fires and frees cash (then sweep same day).
- **What would change the plan:** any held name hitting a stop; the soft tape extending into a sharper risk-off that pressures the loss cap (watch SPY and FERG's 232.61); a fresh Conviction ≥70 gate-clearer at a clean entry for the open slot.
