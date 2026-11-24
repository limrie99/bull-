# Portfolio

**Last updated:** 2026-11-24 ~09:33 ET (**MARKET-OPEN routine**, Tue — **NO TRADES**). Clock gate: winter cron `30 14 UTC` rang 09:32 ET (on time, 2 min after bell); `market_clock.py --slot market-open --wait` **DUE** → Alpaca `/v2/clock` **is_open=true** (next_close 16:00) → confirmed DUE → **CLAIMED** (owner market-open, no prior claim today), claim committed + pushed `HEAD:main` (7a32df2..57f0e91) BEFORE any order check. 4 required keys non-empty; EQUIBLES empty. Inbox **no Pending**; Astra **no proposals**. **No stock buy** (no clean gate-clearer: PANW live $353.17, well below its ~$367 50dMA buy-STOP trigger → stand down; CLS $203.56 watch-only). **No sell** (all 4 theses intact, no stops fired overnight — positions + open-orders match Mon close exactly). **No hard→trailing conversion** (FERG +0.69% / NOC +0.62% from entry, both below the +5% line). **SPY sweep `action:none`** (cash $10,495 within one SPY share of the $10k cushion; excess ~$495 < 1 share @ $713). Day −0.44% (base = Alpaca last_equity) — loss cap not in play. See research-log 2026-11-24 market-open.

---
**Prior update:** 2026-11-24 ~07:05 ET (**PRE-MARKET routine**, Tue — NO TRADES, market closed; research + plan only). 4-agent fan-out: all 4 theses INTACT, relief rally FADING (tech/semis giving back, rotation into industrials/financials = FERG tailwind), Dec FOMC ~93% HIKE, Wed 11/25 PCE print. No clean gate-clearer for the open slot — PANW (73 B+, 3 sig) a buy-STOP on a ~$367 50dMA reclaim, not a buy; ADSK (72) in earnings blackout (reported Tue AMC) → defer. SPY sweep `action:none`. Corrected Thanksgiving calendar (Alpaca-verified): closed Thu 11/26, half-day Fri 11/27. See research-log 2026-11-24 pre-market.

## Live snapshot (2026-11-24 09:33 ET — MARKET-OPEN)
- **Equity:** $95,493.75 · cash $10,495.23 (10.99%) · long_mv $84,998.52 · buying_power $279,976.78 (margin figure — this book does not borrow). status ACTIVE, trading_blocked false.
- **Day P/L (so far, intraday):** **−$420.23 / −0.44%** (base = Alpaca `last_equity` $95,913.98 = Mon 11/23 close equity). The real daily scorecard is the close routine's.
- **SPY day (so far):** 713.41 vs Mon close 722.56 → SPY **−1.27%** — the relief-rally bounce fading, exactly as the pre-market flagged (tech/semis giving back).
- **Day alpha (so far):** **+0.83 pp** — our defensive book (staples PG, waste RSG) + ~11% cash cushion is holding up better than SPY on a down open, the mirror of last Monday's lag on a sharp up day.

## Open positions (4 conviction stocks + 1 index-floor sleeve) — LIVE marks 2026-11-24 09:33 ET
| Symbol | Shares | Avg Cost | Cur Px | P/L % | MV | Stop | Entry Date | Thesis (1 line) |
|---|---|---|---|---|---|---|---|---|
| FERG | 44 | 250.12 | 251.855 | +0.69% | $11,081.62 | **−7% HARD (GTC)** `232.61` | 2026-11-18 | Ferguson — plumbing/HVAC/industrial distributor. Q1 FY27 beat+raise (11/9) + onshoring/data-center demand + BofA PT $320 / Bernstein PT $325 Buy. Non-defensive (beta ~1.11). Convert to trailing at +5% from entry (~$262.63). Day 5, thesis intact. |
| NOC | 18 | 544.37 | 547.77 | +0.62% | $9,859.86 | **−7% HARD (GTC)** `506.26` | 2026-10-23 | Northrop Grumman, defense/aerospace. Q3 beat+raise + record backlog; $1.6B PAC-3 MSE order (11/16); B-21 weapons test (11/22); BNP PT $630. Convert to trailing at +5% (~$571.59). INTACT. |
| PG | 65 | 148.06 | 170.89 | +15.42% | $11,107.85 | **10% TRAILING (GTC)** floor `156.231` | 2026-10-08 | Procter & Gamble — staples diversifier. 11/20 Investor Day supportive (up to $10B productivity savings FY27–30). Floor above entry (profit locked). HOLD — stop handles both outcomes. |
| RSG | 44 | 218.00 | 247.285 | +13.43% | $10,880.54 | **10% TRAILING (GTC)** floor `231.111` | 2026-09-18 | Republic Services — defensive waste. Argus Buy PT $275 + JPM OW $295. Q3 beat + raised FY26, $5B buyback. HOLD. |
| SPY | 59 | 759.746 | 713.41 | −6.10% | $42,091.19 | **NONE — index-floor sleeve, deliberate no-stop carve-out** | 2026-08-10→11-06 | S&P 500 market floor (Lauren-approved Option B + same-day sweep). Own sleeve, EXEMPT from ≤20%/max-5/max-3-per-week; NO stop. ~44% of book. It IS the benchmark. |

**Conviction sleeve: 4 of 5 — one open slot.** **Conviction buys used this week (11/23–11/27): 0 of 3.** **Cash buffer: 10.99%** ($10,495.23 — at the ~$10k cushion). Largest non-index single name PG $11,107.85 (11.63% of equity — well under the 20% cap; FERG 11.60%, RSG 11.39%, NOC 10.33%). Conviction stock mv $42,929.87 (44.96%); SPY sleeve $42,091.19 (44.08%). **Defensive count: 2 of 4** (PG, RSG) — FERG and NOC non-defensive, so the defensive cap still has room.

## Today's fills (2026-11-24)
- **MARKET-OPEN: NONE.** No buy (no clean gate-clearer; PANW $353.17 below its $367 50dMA buy-STOP trigger). No sell (all four theses intact, zero stops fired — open-orders match Mon close exactly). No conversion (FERG/NOC below +5% from entry). No SPY sweep (`action:none`, cash within one share of cushion).

## Risk checks (MARKET-OPEN 2026-11-24)
- **(a) Any position −7% or worse un-stopped?** NO. FERG +0.69%, NOC +0.62%, PG +15.42%, RSG +13.43% (all from entry); SPY −6.10% (index, no stop by design).
- **(b) Any position +5%+ (from entry) needing hard→trailing conversion?** NO. FERG +0.69% / NOC +0.62% from entry, both below the +5% line (FERG convert ~$262.63; NOC ~$571.59). PG/RSG already trail.
- **(c) Daily loss cap:** day is **−0.44%** — not breached (cap is −3%). New buys still allowed today.
- **(d) Sell signals?** NONE. All four theses INTACT; no −7% breach, no thesis break, no guidance cut; no stops fired.

## Stop-management state (open-orders — VERIFIED live 2026-11-24 OPEN, exactly 4)
- **FERG −7% HARD** `ea91d0f9-6f6d-46c1-a665-b77c6efdc0ec` — stop **232.61**, GTC, resting. qty 44. Convert at +5% from entry (~$262.63). ~7.6% above stop.
- **NOC −7% HARD** `59a67c62-0ec7-4d59-8315-66d94b9d3d7c` — stop **506.26**, GTC, resting. qty 18. Convert at +5% (~$571.59). ~7.6% above stop.
- **PG 10% TRAILING** `272e2864-58a7-471f-93ad-acf3914e5a18` — floor **156.231**, trail 10%, GTC, resting. qty 65.
- **RSG 10% TRAILING** `135c200e-fc09-4a37-95c1-f940b57ae0e3` — floor **231.111**, trail 10%, GTC, resting. qty 44.
- **SPY — NO STOP by design** (index-floor sleeve carve-out). qty 59 unencumbered.
- Confirmed **exactly 4 open orders total** — 2 hard stops (FERG, NOC) + 2 trailing (PG/RSG). SPY unencumbered. None fired.

## Strategy status (MARKET-OPEN 2026-11-24)
- **Regime:** relief-rally fade — SPY −1.27% so far today after Monday's +4.62% bounce. Rates stay elevated; Dec 9–10 FOMC the next big event (~93% priced for a 25bp HIKE). Do NOT chase.
- **Traded this week:** nothing yet (new week 11/23–11/27). Buy budget 0/3; one open slot (sleeve 4/5).
- **★ One open slot** — next buy must clear 2+ signals AND Conviction ≥70 at a clean, non-extended entry on a settled tape. Defensive cap has room (2/4) but prefer a non-defensive gate-clearer. **Watch-list triggers:** PANW on a decisive ~$367 50dMA reclaim on a settled tape (currently $353, below trend — stand down); CLS ($203.56) watch-only pending 50dMA confirm + high-beta ≤10% cap; SCHW on a ~$95 50dMA reclaim + 2nd signal; DIS on a genuine pullback.
- **Events runway:** midday Tue 11/24 (1:00 PM ET) next. **Wed 11/25 PCE inflation print** (week's key Fed test) + **Deere (DE) Wed BMO** (industrial read for FERG). **ADSK reported Tue 11/24 AMC** — check the print before any re-look. **Thanksgiving: closed Thu 11/26; half-day Fri 11/27 (close 13:00 ET).** Dec 9–10 FOMC (~93% priced for a 25bp HIKE).

## Handoff → midday (Tue 2026-11-24, 1:00 PM ET)
- **Clock gate first:** `market_clock.py --slot midday --wait --claim --owner midday`; confirm Alpaca `/v2/clock` is_open=true before any order.
- **Re-verify live:** account/positions/open-orders/clock; confirm **exactly 4** open orders (FERG hard 232.61 `ea91d0f9`; NOC hard 506.26 `59a67c62`; RSG trail 231.111 `135c200e`; PG trail 156.231 `272e2864`); SPY (59) unencumbered; daily loss-cap check.
- **No stock buy planned** — no clean gate-clearer on a settled tape. **Lead buy-STOP idea: PANW** — engage ONLY on a decisive ~$367 50dMA reclaim on a SETTLED (non-gap) tape (Conviction ~73, 3 signals, non-defensive; size B+ 10–15%, −7% hard GTC, fund via SPY trim). Do NOT buy below the 50-day. CLS (69) watch-only pending 50dMA confirm + high-beta cap.
- **SPY same-day sweep (standing):** run `scripts/spy_floor.py` live; expect `action:none` (cash ~$495 above cushion = <1 share) UNLESS a stop fires and frees cash → then sweep SAME session. No margin.
- **FERG** +0.69% — hold on hard stop 232.61; convert to trailing only at +5% from entry (~$262.63). **NOC** +0.62%, convert at +5% (~$571.59). PG/RSG floors ratchet automatically.
- **What would change the plan:** any held name hitting a stop (then same-day SPY sweep of freed cash); PANW decisively reclaiming $367 on a settled tape; the Wed 11/25 PCE print; the Dec 9–10 FOMC setup.
- **Calendar (Alpaca-verified):** Wed 11/25 normal full day; **Thu 11/26 CLOSED (Thanksgiving)**; **Fri 11/27 half-day (close 13:00 ET)**; Mon 11/30 normal.
