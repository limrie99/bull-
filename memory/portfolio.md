# Portfolio

**Last updated:** 2026-11-27 07:05 ET (**PRE-MARKET routine**, Fri — **BLACK FRIDAY HALF-DAY, close 13:00 ET**). Clock gate: winter cron `0 12 UTC` on time (12:03 UTC = 07:03 ET EST); `market_clock.py --slot pre-market --claim --owner pre-market` → **DUE** → **CLAIMED** (owner pre-market, stamp 2026-11-27); claim pushed `HEAD:main` (e852f17→97dc06d) before research. **Research-only routine — NO trades** (also confirmed `/v2/clock` is_open=false pre-open; next_open 11/27 09:30, next_close 13:00 = half-day). 4 required keys non-empty; EQUIBLES empty. Inbox **no Pending**; Astra **no proposals**. **4 parallel Perplexity sub-agents** (macro / earnings / holdings-news / opportunity-scout). **All 4 theses INTACT** (fresh thesis-confirming item: FERG BofA PT $315→$320 Buy, 11/26). **No buy** — lead scout pick HPE REJECTED on the tape as a knife-catch (−28% below 50dMA despite a beat-and-raise); PANW still −2.7% below its ~$367 50dMA (not triggered); DELL still broken. **No sell** (zero stops fired). **No conversion** (FERG +2.75% / NOC +2.10%, both below +5%). **No SPY sweep** (market closed; cash at cushion). Marks are latest-available pre-open (effectively 11/25 close). Open orders verified **exactly 4**. See research-log 2026-11-27 pre-market.

---
**Prior update:** 2026-11-26 07:05 ET (PRE-MARKET, Thu — THANKSGIVING, MARKET CLOSED, no trades). Holiday research-only; all 4 theses intact; no buy/sell/conversion/sweep. See research-log 2026-11-26.

## Daily scorecard (2026-11-27 PRE-MARKET — pre-open, marks latest-available)
- **Equity:** **$97,121.97** · cash $10,495.23 (10.81%) · long_mv $86,626.74 · status ACTIVE, trading_blocked false. (buying_power $284,535.79 is a margin figure — this book does not borrow.)
- **Day P/L:** **pending** — market not yet open (pre-market). Alpaca `last_equity` $96,535.30; current equity $97,121.97 on latest-available marks. The real session day P/L is set after the 9:30 ET open; today's scorecard is owned by the market-close routine.
- **SPY:** 727.58 (latest-available mark). Benchmark window refreshes at Friday's close.
- **Alpha:** standing week-to-date (from the 11/25 close): equity +3.42% vs SPY +3.77% → week alpha −0.35 pp; refreshes at the Fri 11/27 half-day close.

## Open positions (4 conviction stocks + 1 index-floor sleeve) — latest-available marks, pre-open 2026-11-27
| Symbol | Shares | Avg Cost | Px | P/L % | MV | Stop | Entry Date | Thesis (1 line) |
|---|---|---|---|---|---|---|---|---|
| FERG | 44 | 250.12 | 256.99 | +2.75% | $11,307.56 | **−7% HARD (GTC)** `232.61` | 2026-11-18 | Ferguson — plumbing/HVAC/industrial distributor. Q1 FY27 beat+raise (11/9) + onshoring/data-center demand; **BofA PT $315→$320 Buy (11/26)**, Bernstein PT $325. Beta ~1.11. Convert to trailing at +5% (~$262.63). Thesis intact/strengthened. |
| NOC | 18 | 544.37 | 555.79 | +2.10% | $10,004.22 | **−7% HARD (GTC)** `506.26` | 2026-10-23 | Northrop Grumman, defense/aerospace. Q3 beat+raise + record backlog; $1.6B PAC-3 (11/16); B-21 test (11/22); $1.13B Navy E-130J mod (11/25); Mizuho Outperform PT $680 (11/24). Convert at +5% (~$571.59). INTACT. |
| PG | 65 | 148.06 | 172.38 | +16.43% | $11,204.70 | **10% TRAILING (GTC)** floor `157.104` | 2026-10-08 | Procter & Gamble — staples diversifier. 11/20 Investor Day productivity/automation story; BofA $190 Buy (11/23), BNP PT $197 (11/25). Floor well above entry. HOLD. |
| RSG | 44 | 218.00 | 254.16 | +16.59% | $11,183.04 | **10% TRAILING (GTC)** floor `231.111` | 2026-09-18 | Republic Services — defensive waste. Argus Buy PT $275 + JPM OW $295; Q3 beat + raised FY26, $5B buyback. HOLD. |
| SPY | 59 | 759.746 | 727.58 | −4.23% | $42,927.22 | **NONE — index-floor sleeve, deliberate no-stop carve-out** | 2026-08-10→11-06 | S&P 500 market floor (Lauren-approved Option B + same-day sweep). Own sleeve, EXEMPT from ≤20%/max-5/max-3-per-week; NO stop. ~44% of book. It IS the benchmark. |

**Conviction sleeve: 4 of 5 — one open slot.** **Conviction buys used this week (11/23–11/27): 0 of 3.** **Cash buffer: 10.81%** ($10,495.23 — right at the ~$10k cushion). Largest non-index single name FERG $11,307.56 (11.64% of equity — well under the 20% cap; PG 11.54%, RSG 11.51%, NOC 10.30%). Conviction stock mv $43,699.52 (45.00%); SPY sleeve $42,927.22 (44.20%). **Defensive count: 2 of 4** (PG, RSG) — FERG and NOC non-defensive, so the defensive cap still has room.

## Today's fills (2026-11-27)
- **NONE — PRE-MARKET routine, research only, market not yet open.** No buy (nothing cleared 2 signals AND ≥70 on a clean entry — HPE is a knife-catch, PANW not triggered), no sell (all four theses intact, zero stops fired), no conversion (FERG/NOC below +5%), no SPY sweep (pre-open; cash at cushion).

## Risk checks (PRE-MARKET 2026-11-27)
- **(a) Any position −7% or worse un-stopped?** NO. FERG +2.75%, NOC +2.10%, PG +16.43%, RSG +16.59% (from entry); SPY −4.23% (index, no stop by design).
- **(b) Any position +5%+ (from entry) needing hard→trailing conversion?** NO. FERG +2.75% / NOC +2.10%, both below the +5% line (FERG convert ~$262.63; NOC ~$571.59). PG/RSG already trail.
- **(c) Daily loss cap:** n/a — pre-open (no intraday session yet).
- **(d) Sell signals?** NONE. All four theses INTACT; no −7% breach, no thesis break, no guidance cut, no downgrade; zero stops fired.

## Stop-management state (open-orders — VERIFIED live 2026-11-27 pre-market, exactly 4)
- **FERG −7% HARD** `ea91d0f9-6f6d-46c1-a665-b77c6efdc0ec` — stop **232.61**, GTC, resting. qty 44. Convert at +5% (~$262.63).
- **NOC −7% HARD** `59a67c62-0ec7-4d59-8315-66d94b9d3d7c` — stop **506.26**, GTC, resting. qty 18. Convert at +5% (~$571.59).
- **PG 10% TRAILING** `272e2864-58a7-471f-93ad-acf3914e5a18` — floor **157.104**, trail 10%, GTC, resting. qty 65.
- **RSG 10% TRAILING** `135c200e-fc09-4a37-95c1-f940b57ae0e3` — floor **231.111**, trail 10%, GTC, resting. qty 44.
- **SPY — NO STOP by design** (index-floor sleeve carve-out). qty 59 unencumbered.
- Confirmed **exactly 4 open orders total** — 2 hard stops (FERG, NOC) + 2 trailing (PG/RSG). SPY unencumbered.

## Strategy status (PRE-MARKET 2026-11-27)
- **Regime:** Risk-on, AI/semi-led bounce (NQ futures ~+2.63%) but on a thin Black Friday half-day with firmer oil (WTI ~$85.6) and yields (10Y ~4.9%) underneath — a "chase the bounce" tape. Keep the bar for fresh risk high; do not chase gaps on thin liquidity.
- **Traded this week:** nothing (week 11/23–11/27). Buy budget 0/3; one open slot (sleeve 4/5).
- **★ One open slot** — next buy must clear 2+ signals AND Conviction ≥70 at a clean, non-extended entry on a settled tape. **Watch-list:** PANW on a decisive ~$367 50dMA reclaim on a settled tape (currently ~$356, −2.7% below; signals #1+#4 present — KeyBanc OW PT ~$450, Phillip Securities Buy PT $418 — needs the technical trigger + Conviction ≥70). **HPE and DELL are knife-catches (−28% and ~−40% below 50dMA respectively) — stay out despite strong fundamentals; wait for a base.**
- **Earnings blackout next week (3-trading-day rule) — OFF-LIMITS for new buys:** CRM (Mon 11/30), NTAP (Tue 12/1), MRVL (Wed 12/2), OKTA (Wed 12/2).
- **Events runway:** **Fri 11/27 half-day (close 13:00 ET)** — thin, low-volume. Light scheduled data week of 11/30. Dec 9–10 FOMC (prior ~97–98% priced 25bp HIKE — note: that probability was NOT re-verifiable this morning; treat as stale pending reconfirmation).

## Handoff → market-open (Fri 2026-11-27, 9:30 AM ET — HALF-DAY, close 13:00 ET)
- **Clock gate first:** `market_clock.py --slot market-open --wait --claim --owner market-open`; summer alarm `30 13 UTC` would ring early → `--wait` holds to 9:30 ET. Then `/v2/clock` must be is_open=true before any order. **Half-day — thin liquidity, do not chase gaps.**
- **Re-verify live:** account/positions/open-orders/clock; confirm **exactly 4** open orders (FERG hard 232.61 `ea91d0f9`; NOC hard 506.26 `59a67c62`; RSG trail 231.111 `135c200e`; PG trail 157.104 `272e2864`); SPY (59) unencumbered.
- **NO stock buy planned** — nothing cleared the gate. **Only live trigger:** PANW decisive ~$367 50dMA reclaim on a settled tape AND re-score to Conviction ≥70. HPE/DELL are knife-catches — do not buy.
- **SPY same-day sweep (standing):** expect `action:none` (cash within one share of cushion) UNLESS a stop fires and frees cash → sweep SAME session. No margin.
- **Conversions:** FERG convert to trailing at +5% (~$262.63); NOC at +5% (~$571.59) — neither due. PG/RSG floors ratchet automatically.
- **Calendar (Alpaca-verified):** **Fri 11/27 half-day (close 13:00 ET)**; Mon 11/30 normal.
