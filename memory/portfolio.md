# Portfolio

**Last updated:** 2026-11-24 16:00 ET (**MARKET-CLOSE routine**, Tue — **NO TRADES**). Clock gate: summer alarm `0 20 UTC` rang 15:02 ET (DST miss, ~58 min early); `market_clock.py --slot market-close --wait --claim --owner market-close` → **EARLY** (−58 min) → slept to 16:00:04 ET → **DUE** ("0 min after the bell") → **CLAIMED** (owner market-close, no prior claim). Alpaca `/v2/clock` is_open=false (bell rang 16:00 ET, next_open 11/25 09:30) → genuine close. 4 required keys non-empty; EQUIBLES empty. Inbox **no Pending**; Astra **no proposals**. **No stock buy**, **no sell**, **no hard→trailing conversion** (FERG +0.85% / NOC +1.19% from entry, both below +5%). **SPY sweep N/A** (market closed at the close run; also cash $495 within one SPY share of the $10k cushion). **Day +0.32%** (base = Mon 11/23 close $95,913.98) — loss cap not in play. Closed-orders today = 0. Open orders verified **exactly 4**. See research-log 2026-11-24 Day summary.

---
**Prior update:** 2026-11-24 ~13:00 ET (**MIDDAY routine**, Tue — NO TRADES). All 4 theses intact; no stops fired; FERG/NOC below +5% (no conversion); SPY sweep `action:none`; day +0.42% intraday. PANW $353 below $367 trigger → stand down. See research-log 2026-11-24 midday.

## Daily scorecard (2026-11-24 CLOSE — official)
- **Equity (close):** **$96,217.78** · cash $10,495.23 (10.91%) · long_mv $85,722.55 · status ACTIVE, trading_blocked false. (buying_power $282,004.06 is a margin figure — this book does not borrow.)
- **Day P/L:** **+$303.80 / +0.32%** (base = Alpaca `last_equity` $95,913.98 = Mon 11/23 close equity).
- **SPY day:** 722.56 (Mon 11/23 close) → **718.91** (today's IEX close / latest trade 15:59:59 ET) = SPY **−0.51%**.
- **Day alpha:** **+0.82 pp** — we beat the market today. Defensive book (PG +16.53%, RSG +15.67%) + ~11% cash held firm while SPY drifted off its Monday-bounce highs.
- **Week-to-date (baseline Fri 11/20 close $93,257.89; SPY 690.68):** equity **+3.17% / +$2,959.89** vs **SPY +4.09%** → **week alpha −0.91 pp** (behind WTD, the mirror of last week's +3.37 pp defensive lead as the market snaps back off the 11/20 low — by design).

## Open positions (4 conviction stocks + 1 index-floor sleeve) — CLOSE marks 2026-11-24 16:00 ET
| Symbol | Shares | Avg Cost | Close Px | P/L % | MV | Stop | Entry Date | Thesis (1 line) |
|---|---|---|---|---|---|---|---|---|
| FERG | 44 | 250.12 | 252.24 | +0.85% | $11,098.56 | **−7% HARD (GTC)** `232.61` | 2026-11-18 | Ferguson — plumbing/HVAC/industrial distributor. Q1 FY27 beat+raise (11/9) + onshoring/data-center demand + BofA PT $320 / Bernstein PT $325 Buy. Non-defensive (beta ~1.11). Convert to trailing at +5% from entry (~$262.63). Day 5, thesis intact. |
| NOC | 18 | 544.37 | 550.84 | +1.19% | $9,915.12 | **−7% HARD (GTC)** `506.26` | 2026-10-23 | Northrop Grumman, defense/aerospace. Q3 beat+raise + record backlog; $1.6B PAC-3 MSE order (11/16); B-21 weapons test (11/22); BNP PT $630. Convert to trailing at +5% (~$571.59). INTACT. |
| PG | 65 | 148.06 | 172.54 | +16.53% | $11,215.10 | **10% TRAILING (GTC)** floor `156.231` | 2026-10-08 | Procter & Gamble — staples diversifier. 11/20 Investor Day supportive (up to $10B productivity savings FY27–30). Floor above entry (profit locked). HOLD — stop handles both outcomes. |
| RSG | 44 | 218.00 | 252.15 | +15.67% | $11,094.60 | **10% TRAILING (GTC)** floor `231.111` (hwm 256.79) | 2026-09-18 | Republic Services — defensive waste. Argus Buy PT $275 + JPM OW $295. Q3 beat + raised FY26, $5B buyback. HOLD. |
| SPY | 59 | 759.746 | 718.91 | −5.41% | $42,399.17 | **NONE — index-floor sleeve, deliberate no-stop carve-out** | 2026-08-10→11-06 | S&P 500 market floor (Lauren-approved Option B + same-day sweep). Own sleeve, EXEMPT from ≤20%/max-5/max-3-per-week; NO stop. ~44% of book. It IS the benchmark. |

**Conviction sleeve: 4 of 5 — one open slot.** **Conviction buys used this week (11/23–11/27): 0 of 3.** **Cash buffer: 10.91%** ($10,495.23 — at the ~$10k cushion). Largest non-index single name PG $11,215.10 (11.66% of equity — well under the 20% cap; FERG 11.53%, RSG 11.53%, NOC 10.30%). Conviction stock mv $43,323.38 (45.03%); SPY sleeve $42,399.17 (44.07%). **Defensive count: 2 of 4** (PG, RSG) — FERG and NOC non-defensive, so the defensive cap still has room.

## Today's fills (2026-11-24)
- **NONE.** MARKET-OPEN, MIDDAY, MARKET-CLOSE: no trades. Closed-orders API for 2026-11-24 = 0. No buy (nothing cleared 2 signals AND ≥70; PANW below its $367 trigger), no sell (all four theses intact, zero stops fired), no conversion (FERG/NOC below +5%), no SPY sweep (market closed at the close; cash within one share of cushion).

## Risk checks (CLOSE 2026-11-24)
- **(a) Any position −7% or worse un-stopped?** NO. FERG +0.85%, NOC +1.19%, PG +16.53%, RSG +15.67% (all from entry); SPY −5.41% (index, no stop by design).
- **(b) Any position +5%+ (from entry) needing hard→trailing conversion?** NO. FERG +0.85% / NOC +1.19% from entry, both below the +5% line (FERG convert ~$262.63; NOC ~$571.59). PG/RSG already trail.
- **(c) Daily loss cap:** day was **+0.32%** — never breached (cap −3%).
- **(d) Sell signals?** NONE. All four theses INTACT; no −7% breach, no thesis break, no guidance cut; no stops fired.

## Stop-management state (open-orders — VERIFIED live 2026-11-24 CLOSE, exactly 4)
- **FERG −7% HARD** `ea91d0f9-6f6d-46c1-a665-b77c6efdc0ec` — stop **232.61**, GTC, resting. qty 44. Convert at +5% from entry (~$262.63). ~8.6% above stop.
- **NOC −7% HARD** `59a67c62-0ec7-4d59-8315-66d94b9d3d7c` — stop **506.26**, GTC, resting. qty 18. Convert at +5% (~$571.59). ~8.1% above stop.
- **PG 10% TRAILING** `272e2864-58a7-471f-93ad-acf3914e5a18` — floor **156.231**, trail 10%, GTC, resting. qty 65. hwm 173.59.
- **RSG 10% TRAILING** `135c200e-fc09-4a37-95c1-f940b57ae0e3` — floor **231.111**, trail 10%, GTC, resting. qty 44. hwm 256.79.
- **SPY — NO STOP by design** (index-floor sleeve carve-out). qty 59 unencumbered.
- Confirmed **exactly 4 open orders total** — 2 hard stops (FERG, NOC) + 2 trailing (PG/RSG). SPY unencumbered. None fired today.

## Strategy status (CLOSE 2026-11-24)
- **Regime:** Monday's +4.62% relief bounce is cooling — SPY −0.51% today after two sharp up days (690.68 on 11/20 → 718.91 now, ~+4% off the low). Rates stay elevated; Dec 9–10 FOMC the next big event (~25bp HIKE near-priced). **Wed 11/25 PCE** is the week's key Fed test. Do NOT chase.
- **Traded this week:** nothing (week 11/23–11/27). Buy budget 0/3; one open slot (sleeve 4/5).
- **★ One open slot** — next buy must clear 2+ signals AND Conviction ≥70 at a clean, non-extended entry on a settled tape. Defensive cap has room (2/4) but prefer a non-defensive gate-clearer. **Watch-list triggers:** PANW on a decisive ~$367 50dMA reclaim on a settled tape (currently ~$353, below trend — stand down); CLS watch-only pending 50dMA confirm + high-beta ≤10% cap; SCHW on a ~$95 50dMA reclaim + 2nd signal; DIS on a genuine pullback.
- **Events runway:** **Wed 11/25 PCE inflation print** (week's key Fed test) + **Deere (DE) Wed BMO** (industrial read for FERG). **Thanksgiving: closed Thu 11/26; half-day Fri 11/27 (close 13:00 ET).** Dec 9–10 FOMC (~25bp HIKE near-priced).

## Handoff → pre-market (Wed 2026-11-25, 7:00 AM ET)
- **Clock gate first:** `market_clock.py --slot pre-market --wait --claim --owner pre-market`; summer alarm `0 11 UTC` rings early → `--wait` holds to 7:00 AM ET. Pre-market is research-only (market closed) — no orders.
- **Re-verify live:** account/positions/open-orders/clock; confirm **exactly 4** open orders (FERG hard 232.61 `ea91d0f9`; NOC hard 506.26 `59a67c62`; RSG trail 231.111 `135c200e`; PG trail 156.231 `272e2864`); SPY (59) unencumbered.
- **Wed 11/25 PCE inflation print** is the headline catalyst — the Fed's preferred gauge; a hot number pressures rates and risk, a cool one supports the bounce. **Deere (DE) reports BMO** — an industrial read-through for FERG. Watch but don't pre-trade a print.
- **No stock buy planned** — PANW only on a decisive ~$367 50dMA reclaim on a SETTLED tape (below trend now → stand down). CLS watch-only.
- **SPY same-day sweep (standing):** on market-open/midday with the market open and cash > cushion, run `scripts/spy_floor.py`; expect `action:none` (cash ~$495 above cushion = <1 share) UNLESS a stop fires and frees cash → then sweep SAME session. No margin.
- **FERG** +0.85% — hold on hard stop 232.61; convert to trailing only at +5% from entry (~$262.63). **NOC** +1.19%, convert at +5% (~$571.59). PG/RSG floors ratchet automatically.
- **Calendar (Alpaca-verified):** Wed 11/25 normal full day; **Thu 11/26 CLOSED (Thanksgiving)**; **Fri 11/27 half-day (close 13:00 ET)**; Mon 11/30 normal.
