# Portfolio

**Last updated:** 2026-11-20 ~08:34 CT (**9:34 AM ET, MARKET-OPEN routine**, Fri — **NO TRADES**). Clock gate: winter cron `30 14 UTC` rang; `market_clock.py --slot market-open --wait --claim --owner market-open` → **DUE** ("3 min after the bell", wait 0) → **CLAIMED** (stamp 2026-11-20, owner market-open, no prior claim today). Alpaca `/v2/clock` **is_open=true** (09:33 ET; next_close 11/20 16:00) → open genuine. 4 required keys non-empty; EQUIBLES empty → filing data skipped. Inbox **no Pending**; Astra **no proposals**. Risk checks all clear (no −7% breach, no +5% hard→trailing conversion due, loss cap far off — intraday +0.25%, UP). SPY sweep `action:none` (cash within one SPY share of the $10k cushion). Open orders **exactly 4** unchanged — no stops fired. Sleeve **4/5** (one open slot); weekly conviction buys **1/3** (week 11/16–11/20, day 5). **DIS (the pre-market CONDITIONAL lead buy) STOOD DOWN** — extended ~+4% over two sessions into a soft risk-off tape; not a clean entry, not a chase. **★ Weekly review (5:00 PM ET today) owns the official full-week scorecard + the mandatory Telegram push.** See research-log 2026-11-20 market-open.

## Live snapshot (2026-11-20 09:34 ET — MARKET-OPEN, intraday)
- **Equity:** $95,371.69 · cash $10,495.23 (11.00%) · long_mv $84,876.46 · buying_power $279,635.01 (margin figure — this book does not borrow). status ACTIVE, trading_blocked false.
- **Intraday P/L:** **+$237.58 / +0.25%** (base 11/19 close equity $95,134.11 = Alpaca `last_equity`). UP, full loss-cap buffer.
- **SPY intraday:** ~712.52 (vs 715.84 close 11/19) → SPY **−0.46%** intraday — soft/risk-off tape continues.
- **Intraday alpha:** **≈ +0.71 pp** — BEATING the market intraday (defensive book + SPY floor hold up while the index slips). Official scorecard is the weekly review / close's job.

## Open positions (4 conviction stocks + 1 index-floor sleeve) — MARKET-OPEN marks 2026-11-20 09:34 ET
| Symbol | Shares | Avg Cost | Px | P/L % | MV | Stop | Entry Date | Thesis (1 line) |
|---|---|---|---|---|---|---|---|---|
| FERG | 44 | 250.12 | 245.97 | −1.66% | $10,822.68 | **−7% HARD (GTC)** `232.61` | 2026-11-18 | Ferguson — plumbing/HVAC/industrial distributor. Q1 FY27 beat+raise (11/9) + onshoring/data-center demand + BofA PT $320 Buy (11/18). Non-defensive (beta ~1.11). Convert to trailing at +5% (~$267.63). Day 3, slipped with the soft tape, thesis intact. |
| NOC | 18 | 544.37 | 547.98 | +0.66% | $9,863.64 | **−7% HARD (GTC)** `506.26` | 2026-10-23 | Northrop Grumman, defense/aerospace. Q3 beat+raise + record backlog; $1.6B PAC-3 MSE order (11/16); BTIG Buy PT $815. Convert to trailing at +5% (~$571.59). INTACT. |
| PG | 65 | 148.06 | 171.20 | +15.63% | $11,128.00 | **10% TRAILING (GTC)** floor `156.231` | 2026-10-08 | Procter & Gamble — staples diversifier. Investor Day 11/19 was a non-event for the stock; now firming. Floor above entry (profit locked). HOLD — stop handles both outcomes. |
| RSG | 44 | 218.00 | 250.85 | +15.07% | $11,037.62 | **10% TRAILING (GTC)** floor `231.111` | 2026-09-18 | Republic Services — defensive waste. Argus Buy PT $275 + JPM OW $295. Q3 beat + raised FY26, $5B buyback. HOLD. |
| SPY | 59 | 759.746 | 712.17 | −6.26% | $42,018.03 | **NONE — index-floor sleeve, deliberate no-stop carve-out** | 2026-08-10→11-06 | S&P 500 market floor (Lauren-approved Option B + same-day sweep). Own sleeve, EXEMPT from ≤20%/max-5/max-3-per-week; NO stop. ~44% of book. It IS the benchmark. |

**Conviction sleeve: 4 of 5 — one open slot.** **Conviction buys used this week (11/16–11/20): 1 of 3.** **Cash buffer: 11.00%** ($10,495.23 — at the ~$10k cushion). Largest non-index single name PG $11,128.00 (11.67% of equity — well under the 20% cap; RSG 11.57%, FERG 11.35%, NOC 10.34%). Conviction stock mv FERG+NOC+PG+RSG $42,851.94 (44.93%); SPY sleeve $42,018.03 (44.06%). **Defensive count: 2 of 4** (PG, RSG) — FERG and NOC non-defensive, so the defensive cap still has room.

## Today's fills (2026-11-20)
- **At MARKET-OPEN: NONE.** No buy (DIS, the pre-market CONDITIONAL lead, stood down — see below), no sell (no −7% breach, no broken thesis), no hard→trailing conversion (neither hard-stop name is +5% yet), no SPY sweep (`action:none`, cash within one share of cushion). Alpaca open-orders unchanged at exactly 4; no stop fired overnight or at the open.

## DIS stand-down (the pre-market CONDITIONAL lead buy)
Pre-market handed DIS to market-open as a CONDITIONAL buy — buy only if it verified clean (above a rising 50-day, 2 signals standing, Conviction ≥70) on a **settled, non-risk-off** tape. Live check:
- DIS ~$121.75, 50-day ~$110.66 → technically ABOVE a rising 50-day (signal #6 holds on paper), PT-wave (#4) stands → 2 signals, ~72.
- **BUT extended, not clean:** DIS popped $116.94 → $122.36 → $121.75 over the last two sessions (~+4%) and sits at a local high — a chase, not a pullback entry.
- **Tape still soft/risk-off:** SPY −0.46% intraday — the hawkish backdrop the pre-market flagged.
- Pre-market rule was explicit: *"If it gaps/extends or the tape pukes → stand down, it's not a chase."* DIS has extended into a soft tape on a thin 2-signal (PT-wave + trend, no fresh earnings catalyst) setup that only barely clears ~72. **→ STAND DOWN. Keep the open slot.** DIS stays on watch for a genuine pullback / settled tape.

## Risk checks (MARKET-OPEN 2026-11-20)
- **(a) Any position −7% or worse un-stopped?** NO. FERG −1.66%, NOC +0.66%, PG +15.63%, RSG +15.07% (all in range); SPY −6.26% (index, no stop by design). Nothing near the −7% hard → no Perplexity news check triggered.
- **(b) Any position +5%+ needing hard→trailing conversion?** NO. The two HARD-stop names (FERG −1.66%, NOC +0.66%) are below the +5% line (FERG convert ~$267.63; NOC ~$571.59). PG/RSG already trail.
- **(c) Daily loss cap:** intraday **+0.25%** (UP) — NOT breached. New buys would be allowed if a setup appeared; none clean did.
- **(d) Sell signals?** NONE. All four theses INTACT; no −7% breach, no thesis break, no guidance cut.

## Stop-management state (open-orders — VERIFIED live 2026-11-20 OPEN, exactly 4)
- **FERG −7% HARD** `ea91d0f9-6f6d-46c1-a665-b77c6efdc0ec` — stop **232.61**, GTC, resting. qty 44. Convert at +5% (~$267.63).
- **NOC −7% HARD** `59a67c62-0ec7-4d59-8315-66d94b9d3d7c` — stop **506.26**, GTC, resting. qty 18. Convert at +5% (~$571.59).
- **PG 10% TRAILING** `272e2864-58a7-471f-93ad-acf3914e5a18` — floor **156.231**, trail 10%, GTC, resting. qty 65.
- **RSG 10% TRAILING** `135c200e-fc09-4a37-95c1-f940b57ae0e3` — floor **231.111**, trail 10%, GTC, resting. qty 44.
- **SPY — NO STOP by design** (index-floor sleeve carve-out). qty 59 unencumbered.
- Confirmed **exactly 4 open orders total** — 2 hard stops (FERG, NOC) + 2 trailing (PG/RSG). SPY unencumbered. None fired.

## Strategy status (MARKET-OPEN 2026-11-20)
- **Regime:** soft/risk-off continues — SPY −0.46% intraday after a hawkish-Fedspeak week; yields near cycle highs. 10:00a ET U. Michigan sentiment + inflation expectations is the swing print; Fed's Cook ~12:15p ET. No confirmed base. Dec 9–10 FOMC ahead.
- **Traded this week:** FERG (1 of 3 conviction buys). One open slot (sleeve 4/5).
- **★ One open slot** — next buy must clear 2+ signals AND Conviction ≥70 at a **clean, non-extended** entry on a settled tape; defensive cap has room (2/4) but prefer a non-defensive gate-clearer. **DIS watch-only** — re-check for a genuine pullback / settled tape; do not chase the local high. NVDA extended; PANW needs a ~$366 50-day reclaim; ADSK DEFERRED on its 11/24 earnings fence.
- **Events runway:** **★ Fri 11/20 is weekly-review day (5:00 PM ET)** — owns the official full-week scorecard + mandatory Telegram. 10:00a Michigan print; Dec 9–10 FOMC.

## Handoff → midday (Fri 2026-11-20; winter cron `0 18 UTC`; summer `0 17` rings ~57 min early → `--wait` holds to 1:00 PM ET)
- **Clock gate first:** `market_clock.py --slot midday --wait --claim --owner midday`; confirm Alpaca is_open=true before claiming/trading.
- **Re-verify live:** account/positions/open-orders/clock; confirm **exactly 4** open orders (FERG hard 232.61; NOC hard 506.26; RSG trail 231.111; PG trail 156.231); SPY (59 sh) unencumbered; daily loss-cap check.
- **FERG** −1.66% day 3 — hold on its hard stop; convert to trailing only at +5% (~$267.63). **NOC** +0.66%, hard→trailing only at +5% (~$571.59). PG/RSG floors ratchet automatically.
- **DIS watch-only** — only re-engage on a genuine pullback into a clean entry on a settled tape; do NOT chase the local high. Watch the 10:00a Michigan inflation-expectations print — a weak read re-ignites the hawkish selloff.
- **SPY sweep:** cash $10,495 is ~$495 above the $10k cushion = less than one SPY share → expect `action:none` unless a stop fires and frees cash (then sweep same day).
- **What would change the plan:** any held name hitting a stop; the soft tape extending into a sharper risk-off that pressures the loss cap (watch SPY and FERG's 232.61); a fresh Conviction ≥70 gate-clearer at a clean entry for the open slot.
