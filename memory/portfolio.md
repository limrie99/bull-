# Portfolio

**Last updated:** 2026-11-18 ~13:00 CT display (**1:00 PM ET, MIDDAY routine**, Wed — **STEADY, no trades**). Clock gate: wake fired on the SUMMER cron (`0 17 UTC`, 12:05 PM ET) = daylight-saving early ring; `market_clock.py --slot midday` returned EARLY (wait 54 min) → `--wait` held to 1:00 PM ET, then `--claim --owner midday` → **CLAIMED** (stamp 2026-11-18) and **pushed to main before any order** (commit 9110d46). Alpaca `/v2/clock` **is_open=true** (13:00 ET). 4 required keys non-empty; EQUIBLES empty → filing data skipped. Inbox **no Pending**; Astra **no proposals**. Risk checks all clear (no −7% breach, no +5% hard→trailing conversion due, loss cap far off). SPY sweep `spy_floor.py` → **action:none** (cash within one share of the $10k cushion). No new buys (no breaking catalyst; FOMC Oct minutes 2:00 PM ET = this afternoon's risk event). FERG recovered from −0.42% at open to **+1.03%**. Sleeve **4/5** (one open slot); weekly conviction buys **1/3** (week 11/16–11/20). Open orders **exactly 4** unchanged. See research-log 2026-11-18 midday.

## Open positions (4 conviction stocks + 1 index-floor sleeve) — live marks 2026-11-18 ~1:00 PM ET
| Symbol | Shares | Avg Cost | Px (live) | P/L % | MV | Stop | Entry Date | Thesis (1 line) |
|---|---|---|---|---|---|---|---|---|
| FERG | 44 | 250.12 | 252.69 | +1.03% | $11,118.36 | **−7% HARD (GTC)** `232.61` | 2026-11-18 | Ferguson — plumbing/HVAC/industrial distributor. Q1 FY27 beat+raise (11/9) + onshoring/data-center demand + Nov PT-raise wave (BofA $320 Buy 11/18). Non-defensive (beta ~1.11). Convert to trailing at +5% (~$267.63). NEW — recovered green intraday. |
| NOC | 18 | 544.37 | 542.29 | −0.38% | $9,761.22 | **−7% HARD (GTC)** `506.26` | 2026-10-23 | Northrop Grumman, defense/aerospace. Q3 beat+raise + record backlog; $1.6B PAC-3 MSE order (11/16); BTIG Buy PT $815. Convert to trailing at +5% (~$571.59). INTACT. |
| PG | 65 | 148.06 | 170.63 | +15.24% | $11,090.95 | **10% TRAILING (GTC)** floor `156.231` | 2026-10-08 | Procter & Gamble — staples diversifier. **Investor Day Thu Nov 19** (near catalyst). Floor above entry (profit locked). HOLD. |
| RSG | 44 | 218.00 | 250.87 | +15.08% | $11,038.06 | **10% TRAILING (GTC)** floor `231.111` | 2026-09-18 | Republic Services — defensive waste. Argus Buy PT $275 + JPM OW $295. Q3 beat + raised FY26, $5B buyback. HOLD. |
| SPY | 59 | 761.083 | 731.19 | −3.93% | $43,140.21 | **NONE — index-floor sleeve, deliberate no-stop carve-out** | 2026-08-10→11-06 | S&P 500 market floor (Lauren-approved Option B + same-day sweep). Own sleeve, EXEMPT from ≤20%/max-5/max-3-per-week; NO stop. ~44.6% of book. It IS the benchmark. |

**Conviction sleeve: 4 of 5 — one open slot.** **Conviction buys used this week (11/16–11/20): 1 of 3.** **Cash buffer: 10.86%** ($10,495.47 — at the ~$10k cushion). Largest non-index single name FERG $11,118.36 (11.50% of equity — well under the 20% cap). Conviction stock mv FERG+NOC+PG+RSG $43,008.59 (44.5%); SPY sleeve $43,140.21 (44.6%). **Defensive count: 2 of 5** (PG, RSG) — FERG and NOC are non-defensive, so the sleeve cap still has room.

## Today's fills (2026-11-18 — midday run)
- **NONE.** No trades at midday. No sells (no −7% breach, no broken thesis), no hard→trailing conversions (no hard-stop name is +5% yet), no SPY sweep (`action:none` — cash within one share of cushion), no new buys (no breaking catalyst; FOMC minutes 2pm = risk event). Earlier today (market-open): SPY trim 15 @ 732.602 + FERG buy 44 @ 250.12.

## Live snapshot (MIDDAY 2026-11-18 ~1:00 PM ET)
- **Equity:** $96,646.84 · cash $10,495.47 (10.86%) · long_mv $86,148.80.
- **Intraday P/L:** −$314.84 / **−0.33%** (base 11/17 close equity $96,961.68) — loss cap (−3%) far off, full buffer intact.
- Full daily scorecard vs SPY is owned by the market-close routine.

## Risk checks (MIDDAY 2026-11-18)
- **(a) Any position −7% or worse un-stopped?** NO. FERG +1.03%, NOC −0.38%, PG +15.24%, RSG +15.08% (all within range); SPY −3.93% (index, no stop by design). Nothing near −7% — no Perplexity news check triggered.
- **(b) Any position +5%+ needing hard→trailing conversion?** NO. The two HARD-stop names (FERG +1.03%, NOC −0.38%) are below the +5% line (FERG convert ~$267.63; NOC ~$571.59). PG/RSG already trail.
- **(c) Daily loss cap:** intraday **−0.33%** — NOT breached (cap is >3% down). New buys still allowed, but none qualify.
- **(d) Sell signals?** NONE. All four theses INTACT; no −7% breach, no thesis break, no guidance cut.

## Stop-management state (open-orders — VERIFIED live 2026-11-18 MIDDAY, exactly 4)
- **FERG −7% HARD** `ea91d0f9-6f6d-46c1-a665-b77c6efdc0ec` — stop **232.61**, GTC, resting. qty 44. Convert at +5% (~$267.63).
- **NOC −7% HARD** `59a67c62-0ec7-4d59-8315-66d94b9d3d7c` — stop **506.26**, GTC, resting. qty 18. Convert at +5% (~$571.59).
- **PG 10% TRAILING** `272e2864-58a7-471f-93ad-acf3914e5a18` — floor **156.231**, trail 10%, GTC, resting. qty 65.
- **RSG 10% TRAILING** `135c200e-fc09-4a37-95c1-f940b57ae0e3` — floor **231.111**, trail 10%, GTC, resting. qty 44.
- **SPY — NO STOP by design** (index-floor sleeve carve-out). qty 59 unencumbered.
- Confirmed **exactly 4 open orders total** — 2 hard stops (FERG, NOC) + 2 trailing (PG/RSG). SPY unencumbered.

## Strategy status (MIDDAY 2026-11-18)
- **Regime:** measured risk-on after NVDA's 11/17 AMC beat-and-raise. Narrow megacap-tech leadership. **FOMC Oct minutes 2:00 PM ET today** = this afternoon's macro risk event; Dec 9–10 FOMC (25bp hike near-priced).
- **Traded this week:** FERG (1 of 3 conviction buys). One open slot (sleeve 4/5).
- **★ One open slot** — next buy must still clear 2+ signals AND Conviction ≥70 at a clean entry; defensive cap has room (2/5) but prefer a non-defensive gate-clearer. ADSK (B+ 72) stays DEFERRED on its own 11/24 earnings fence.
- **Events runway:** FOMC Oct minutes 2:00 PM ET today; **PG Investor Day Thu 11/19**; Dec 9–10 FOMC.

## Handoff → market-close (Wed 2026-11-18, winter cron `0 21 UTC`; summer `0 20` rings ~57 min early → `--wait` holds to 4:00 PM ET)
- **Clock gate first:** `market_clock.py --slot market-close --wait --claim --owner market-close`; confirm Alpaca — the close is not the close while `next_close` is >20 min away.
- **MANDATORY daily "How we're doing" message + Telegram push** — never skipped, trade or no trade.
- **Re-verify live:** account/positions/open-orders/clock; confirm **exactly 4** open orders (FERG hard 232.61; NOC hard 506.26; RSG trail 231.111; PG trail 156.231); SPY (59 sh) unencumbered; daily loss-cap check.
- **FERG** +1.03% (recovered) — hold on its hard stop; convert to trailing only at +5% (~$267.63). Watch it isn't knifing below 232.61 on a 2pm-minutes whipsaw.
- **NOC hard→trailing conversion:** only at +5% (~$571.59); it's −0.38%, far off. PG/RSG floors ratchet automatically.
- **SPY sweep at close:** cash $10,495 is ~$495 above the $10k cushion = less than one SPY share → expect `action:none` unless a stop fires intraday and frees cash (then sweep same day).
- **★ FOMC Oct minutes 2:00 PM ET** = this afternoon's macro risk — could whipsaw into the close. **PG Investor Day Thu 11/19.**
- **What would change the plan:** FERG breaching its stop (let it fire mechanically); a hawkish 2pm minutes whipsaw; any held name hitting a stop.
