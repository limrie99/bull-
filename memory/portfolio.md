# Portfolio

**Last updated:** 2026-11-24 ~13:00 ET (**MIDDAY routine**, Tue — **NO TRADES**). Clock gate: early summer alarm `0 17 UTC` rang 12:06 ET (DST miss, 1h early); `market_clock.py --slot midday --wait --claim --owner midday` → **EARLY** (−54 min) → slept to 13:00:05 ET → **DUE** → **CLAIMED** (owner midday). Alpaca `/v2/clock` is_open=true (next_close 16:00) confirmed; no order placed before DUE. 4 required keys non-empty; EQUIBLES empty. Inbox **no Pending**; Astra **no proposals**. **No stock buy** (PANW live $353.14, still below its ~$367 50dMA buy-STOP trigger; no breaking catalyst → stand down). **No sell** (all 4 theses intact, no stops fired — positions + open-orders match open/Mon close exactly). **No hard→trailing conversion** (FERG +0.89% / NOC +2.16% from entry, both below the +5% line). **SPY sweep `action:none`** (cash $10,495 within one SPY share of the $10k cushion; excess ~$495 < 1 share @ ~$717). Day **+0.42%** (base = Alpaca last_equity $95,913.98) — loss cap not in play. See research-log 2026-11-24 midday.

---
**Prior update:** 2026-11-24 ~09:33 ET (**MARKET-OPEN routine**, Tue — NO TRADES). All 4 theses intact; no stops fired overnight; FERG/NOC below +5% (no conversion); SPY sweep `action:none`; day −0.44% at the open (SPY −1.27%, +0.83pp ahead). PANW $353 below $367 trigger → stand down. See research-log 2026-11-24 market-open.

## Live snapshot (2026-11-24 13:00 ET — MIDDAY)
- **Equity:** $96,317.49 · cash $10,495.23 (10.90%) · long_mv $85,821.75 · status ACTIVE, trading_blocked false. (buying_power $281,869.95 is a margin figure — this book does not borrow.)
- **Day P/L (so far, intraday):** **+$403.51 / +0.42%** (base = Alpaca `last_equity` $95,913.98 = Mon 11/23 close equity). The real daily scorecard is the close routine's.
- **SPY day (so far):** 719.56 vs Mon close 722.56 → SPY **−0.42%** — recovered from the −1.27% open low as the relief-rally fade firmed into a flat/mildly-green tape.
- **Day alpha (so far):** **+0.84 pp** — defensive book (staples PG, waste RSG) + ~11% cash cushion holding up better than SPY on a choppy session.

## Open positions (4 conviction stocks + 1 index-floor sleeve) — LIVE marks 2026-11-24 13:00 ET
| Symbol | Shares | Avg Cost | Cur Px | P/L % | MV | Stop | Entry Date | Thesis (1 line) |
|---|---|---|---|---|---|---|---|---|
| FERG | 44 | 250.12 | 252.34 | +0.89% | $11,102.96 | **−7% HARD (GTC)** `232.61` | 2026-11-18 | Ferguson — plumbing/HVAC/industrial distributor. Q1 FY27 beat+raise (11/9) + onshoring/data-center demand + BofA PT $320 / Bernstein PT $325 Buy. Non-defensive (beta ~1.11). Convert to trailing at +5% from entry (~$262.63). Day 5, thesis intact. |
| NOC | 18 | 544.37 | 556.10 | +2.16% | $10,009.80 | **−7% HARD (GTC)** `506.26` | 2026-10-23 | Northrop Grumman, defense/aerospace. Q3 beat+raise + record backlog; $1.6B PAC-3 MSE order (11/16); B-21 weapons test (11/22); BNP PT $630. Convert to trailing at +5% (~$571.59). INTACT. |
| PG | 65 | 148.06 | 172.53 | +16.53% | $11,214.45 | **10% TRAILING (GTC)** floor `156.231` | 2026-10-08 | Procter & Gamble — staples diversifier. 11/20 Investor Day supportive (up to $10B productivity savings FY27–30). Floor above entry (profit locked). HOLD — stop handles both outcomes. |
| RSG | 44 | 218.00 | 251.16 | +15.21% | $11,051.04 | **10% TRAILING (GTC)** floor `231.111` | 2026-09-18 | Republic Services — defensive waste. Argus Buy PT $275 + JPM OW $295. Q3 beat + raised FY26, $5B buyback. HOLD. |
| SPY | 59 | 759.746 | 719.39 | −5.31% | $42,444.01 | **NONE — index-floor sleeve, deliberate no-stop carve-out** | 2026-08-10→11-06 | S&P 500 market floor (Lauren-approved Option B + same-day sweep). Own sleeve, EXEMPT from ≤20%/max-5/max-3-per-week; NO stop. ~44% of book. It IS the benchmark. |

**Conviction sleeve: 4 of 5 — one open slot.** **Conviction buys used this week (11/23–11/27): 0 of 3.** **Cash buffer: 10.90%** ($10,495.23 — at the ~$10k cushion). Largest non-index single name PG $11,214.45 (11.64% of equity — well under the 20% cap; FERG 11.53%, RSG 11.47%, NOC 10.39%). Conviction stock mv $43,378.25 (45.04%); SPY sleeve $42,444.01 (44.07%). **Defensive count: 2 of 4** (PG, RSG) — FERG and NOC non-defensive, so the defensive cap still has room.

## Today's fills (2026-11-24)
- **NONE.** MARKET-OPEN: no trades. MIDDAY: no buy (PANW $353.14 below $367 trigger), no sell (all four theses intact, zero stops fired), no conversion (FERG/NOC below +5%), no SPY sweep (`action:none`).

## Risk checks (MIDDAY 2026-11-24)
- **(a) Any position −7% or worse un-stopped?** NO. FERG +0.89%, NOC +2.16%, PG +16.53%, RSG +15.21% (all from entry); SPY −5.31% (index, no stop by design).
- **(b) Any position +5%+ (from entry) needing hard→trailing conversion?** NO. FERG +0.89% / NOC +2.16% from entry, both below the +5% line (FERG convert ~$262.63; NOC ~$571.59). PG/RSG already trail.
- **(c) Daily loss cap:** day is **+0.42%** — not breached (cap is −3%). New buys still allowed today.
- **(d) Sell signals?** NONE. All four theses INTACT; no −7% breach, no thesis break, no guidance cut; no stops fired.

## Stop-management state (open-orders — VERIFIED live 2026-11-24 MIDDAY, exactly 4)
- **FERG −7% HARD** `ea91d0f9-6f6d-46c1-a665-b77c6efdc0ec` — stop **232.61**, GTC, resting. qty 44. Convert at +5% from entry (~$262.63). ~7.8% above stop.
- **NOC −7% HARD** `59a67c62-0ec7-4d59-8315-66d94b9d3d7c` — stop **506.26**, GTC, resting. qty 18. Convert at +5% (~$571.59). ~9.0% above stop.
- **PG 10% TRAILING** `272e2864-58a7-471f-93ad-acf3914e5a18` — floor **156.231**, trail 10%, GTC, resting. qty 65.
- **RSG 10% TRAILING** `135c200e-fc09-4a37-95c1-f940b57ae0e3` — floor **231.111**, trail 10%, GTC, resting. qty 44.
- **SPY — NO STOP by design** (index-floor sleeve carve-out). qty 59 unencumbered.
- Confirmed **exactly 4 open orders total** — 2 hard stops (FERG, NOC) + 2 trailing (PG/RSG). SPY unencumbered. None fired.

## Strategy status (MIDDAY 2026-11-24)
- **Regime:** relief-rally fade firming — SPY −0.42% on the day (off the −1.27% open low) after Monday's +4.62% bounce. Rates stay elevated; Dec 9–10 FOMC the next big event (~93% priced for a 25bp HIKE). Do NOT chase.
- **Traded this week:** nothing yet (new week 11/23–11/27). Buy budget 0/3; one open slot (sleeve 4/5).
- **★ One open slot** — next buy must clear 2+ signals AND Conviction ≥70 at a clean, non-extended entry on a settled tape. Defensive cap has room (2/4) but prefer a non-defensive gate-clearer. **Watch-list triggers:** PANW on a decisive ~$367 50dMA reclaim on a settled tape (currently $353, below trend — stand down); CLS watch-only pending 50dMA confirm + high-beta ≤10% cap; SCHW on a ~$95 50dMA reclaim + 2nd signal; DIS on a genuine pullback.
- **Events runway:** market-close Tue 11/24 (4:00 PM ET) next — owns the **mandatory daily "How we're doing" Telegram**. **Wed 11/25 PCE inflation print** (week's key Fed test) + **Deere (DE) Wed BMO** (industrial read for FERG). **Thanksgiving: closed Thu 11/26; half-day Fri 11/27 (close 13:00 ET).** Dec 9–10 FOMC (~93% priced for a 25bp HIKE).

## Handoff → market-close (Tue 2026-11-24, 4:00 PM ET)
- **Clock gate first:** `market_clock.py --slot market-close --wait --claim --owner market-close`; the close is not the close while Alpaca `next_close` >20 min away (summer alarm `0 20 UTC` rings early → `--wait` holds to 4:00 PM ET).
- **MANDATORY daily "How we're doing" message + Telegram push** — never skipped, trade or no trade. Lead with the plain-English scorecard (day $ and %, vs SPY, ahead/behind).
- **Re-verify live:** account/positions/open-orders/clock; confirm **exactly 4** open orders (FERG hard 232.61 `ea91d0f9`; NOC hard 506.26 `59a67c62`; RSG trail 231.111 `135c200e`; PG trail 156.231 `272e2864`); SPY (59) unencumbered; daily loss-cap check.
- **No stock buy planned** — PANW only on a decisive ~$367 50dMA reclaim on a SETTLED tape (below trend now → stand down). CLS watch-only.
- **SPY same-day sweep (standing):** run `scripts/spy_floor.py` live; expect `action:none` (cash ~$495 above cushion = <1 share) UNLESS a stop fires and frees cash → then sweep SAME session. No margin.
- **FERG** +0.89% — hold on hard stop 232.61; convert to trailing only at +5% from entry (~$262.63). **NOC** +2.16%, convert at +5% (~$571.59). PG/RSG floors ratchet automatically.
- **What would change the plan:** any held name hitting a stop (then same-day SPY sweep of freed cash); PANW decisively reclaiming $367 on a settled tape; a sharp risk-off into the close; the Wed 11/25 PCE print.
- **Calendar (Alpaca-verified):** Wed 11/25 normal full day; **Thu 11/26 CLOSED (Thanksgiving)**; **Fri 11/27 half-day (close 13:00 ET)**; Mon 11/30 normal.
