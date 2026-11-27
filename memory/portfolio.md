# Portfolio

**Last updated:** 2026-11-27 09:33 ET (**MARKET-OPEN routine**, Fri — **BLACK FRIDAY HALF-DAY, close 13:00 ET**). Clock gate: winter cron `30 14 UTC` on time (14:32 UTC = 09:32 ET EST); `market_clock.py --slot market-open --wait` → **DUE** (wait 0s); Alpaca `/v2/clock` **is_open=true** (next_close 13:00 ET half-day; next_open 11/30 09:30); `--claim --owner market-open` → **CLAIMED** (owner market-open, stamp 2026-11-27); claim pushed `HEAD:main` with this write. **NO TRADES this run.** 4 required keys non-empty; EQUIBLES empty. Inbox **no Pending**; Astra **no proposals**. **No buy** — only armed trigger PANW still $346.81 (below its ~$367 50dMA, slipped from pre-open ~$356); nothing else cleared 2 signals AND ≥70. **No sell** (zero stops fired, all four theses intact). **No conversion** (FERG +4.35% / NOC +2.84%, both below +5% — FERG now the closest, convert ~$262.63). **No SPY sweep** (`spy_floor.py` → `action:none`, cash within one SPY share of cushion). Marks are live 09:33 ET. Open orders verified **exactly 4**. See research-log 2026-11-27 market-open.

---
**Prior update:** 2026-11-27 07:05 ET (PRE-MARKET, research only, market not yet open; all four theses intact; no buy/sell/conversion/sweep). See research-log 2026-11-27 pre-market.

## Daily scorecard (2026-11-27 MARKET-OPEN — live 09:33 ET)
- **Equity:** **$97,156.45** · cash $10,495.23 (10.80%) · long_mv $86,661.22 · status ACTIVE, trading_blocked false. (buying_power $284,632.34 is a margin figure — this book does not borrow.)
- **Day P/L:** **+$621.15 (+0.64%)** — Alpaca `last_equity` $96,535.30 → current equity $97,156.45. Green open, nowhere near the −3% loss cap. Today's final scorecard is owned by the market-close routine (half-day, close 13:00 ET).
- **SPY:** 724.35 (live mark). Benchmark window refreshes at Friday's half-day close.
- **Alpha:** standing week-to-date (from the 11/25 close): equity +3.42% vs SPY +3.77% → week alpha −0.35 pp; refreshes at the Fri 11/27 half-day close.

## Open positions (4 conviction stocks + 1 index-floor sleeve) — live marks 09:33 ET 2026-11-27
| Symbol | Shares | Avg Cost | Px | P/L % | MV | Stop | Entry Date | Thesis (1 line) |
|---|---|---|---|---|---|---|---|---|
| FERG | 44 | 250.12 | 261.00 | +4.35% | $11,484.00 | **−7% HARD (GTC)** `232.61` | 2026-11-18 | Ferguson — plumbing/HVAC/industrial distributor. Q1 FY27 beat+raise (11/9) + onshoring/data-center demand; BofA PT $315→$320 Buy (11/26), Bernstein PT $325. Beta ~1.11. **Convert to trailing at +5% (~$262.63) — now ~$1.63 away, midday watch.** Thesis intact/strengthened. |
| NOC | 18 | 544.37 | 559.83 | +2.84% | $10,076.85 | **−7% HARD (GTC)** `506.26` | 2026-10-23 | Northrop Grumman, defense/aerospace. Q3 beat+raise + record backlog; $1.6B PAC-3 (11/16); B-21 test (11/22); $1.13B Navy E-130J mod (11/25); Mizuho Outperform PT $680 (11/24). Convert at +5% (~$571.59). INTACT. |
| PG | 65 | 148.06 | 172.34 | +16.40% | $11,202.10 | **10% TRAILING (GTC)** floor `157.104` | 2026-10-08 | Procter & Gamble — staples diversifier. 11/20 Investor Day productivity/automation story; BofA $190 Buy (11/23), BNP PT $197 (11/25). Floor well above entry. HOLD. |
| RSG | 44 | 218.00 | 253.70 | +16.38% | $11,162.80 | **10% TRAILING (GTC)** floor `231.111` | 2026-09-18 | Republic Services — defensive waste. Argus Buy PT $275 + JPM OW $295; Q3 beat + raised FY26, $5B buyback. HOLD. |
| SPY | 59 | 759.746 | 724.35 | −4.66% | $42,736.65 | **NONE — index-floor sleeve, deliberate no-stop carve-out** | 2026-08-10→11-06 | S&P 500 market floor (Lauren-approved Option B + same-day sweep). Own sleeve, EXEMPT from ≤20%/max-5/max-3-per-week; NO stop. ~44% of book. It IS the benchmark. |

**Conviction sleeve: 4 of 5 — one open slot.** **Conviction buys used this week (11/23–11/27): 0 of 3.** **Cash buffer: 10.80%** ($10,495.23 — right at the ~$10k cushion). Largest non-index single name FERG $11,484.00 (11.82% of equity — well under the 20% cap; PG 11.53%, RSG 11.49%, NOC 10.37%). Conviction stock mv $43,925.75 (45.21%); SPY sleeve $42,736.65 (43.99%). **Defensive count: 2 of 4** (PG, RSG) — FERG and NOC non-defensive, so the defensive cap still has room.

## Today's fills (2026-11-27)
- **NONE — MARKET-OPEN routine, no trades.** No buy (PANW not triggered at $346.81; nothing else cleared 2 signals AND ≥70), no sell (all four theses intact, zero stops fired), no conversion (FERG +4.35% / NOC +2.84%, both below +5%), no SPY sweep (`spy_floor.py` → `action:none`; cash at cushion).

## Risk checks (MARKET-OPEN 2026-11-27)
- **(a) Any position −7% or worse un-stopped?** NO. FERG +4.35%, NOC +2.84%, PG +16.40%, RSG +16.38% (from entry); SPY −4.66% (index, no stop by design).
- **(b) Any position +5%+ (from entry) needing hard→trailing conversion?** NO. FERG +4.35% / NOC +2.84%, both below the +5% line (FERG convert ~$262.63 — closest, ~$1.63 away; NOC ~$571.59). PG/RSG already trail.
- **(c) Daily loss cap:** not hit — session GREEN +0.64%.
- **(d) Sell signals?** NONE. All four theses INTACT; no −7% breach, no thesis break, no guidance cut, no downgrade; zero stops fired.

## Stop-management state (open-orders — VERIFIED live 2026-11-27 market-open, exactly 4)
- **FERG −7% HARD** `ea91d0f9-6f6d-46c1-a665-b77c6efdc0ec` — stop **232.61**, GTC, resting. qty 44. Convert at +5% (~$262.63) — midday watch.
- **NOC −7% HARD** `59a67c62-0ec7-4d59-8315-66d94b9d3d7c` — stop **506.26**, GTC, resting. qty 18. Convert at +5% (~$571.59).
- **PG 10% TRAILING** `272e2864-58a7-471f-93ad-acf3914e5a18` — floor **157.104**, trail 10%, GTC, resting. qty 65.
- **RSG 10% TRAILING** `135c200e-fc09-4a37-95c1-f940b57ae0e3` — floor **231.111**, trail 10%, GTC, resting. qty 44.
- **SPY — NO STOP by design** (index-floor sleeve carve-out). qty 59 unencumbered.
- Confirmed **exactly 4 open orders total** — 2 hard stops (FERG, NOC) + 2 trailing (PG/RSG). SPY unencumbered.

## Strategy status (MARKET-OPEN 2026-11-27)
- **Regime:** Risk-on green open (book +0.64%) on a thin Black Friday half-day. SPY +1.07% intraday; our calmer book +0.64% as defensives (PG/RSG) are flat-to-down while FERG/NOC/SPY carry. Keep the bar for fresh risk high on thin holiday liquidity; do not chase gaps.
- **Traded this week:** nothing (week 11/23–11/27). Buy budget 0/3; one open slot (sleeve 4/5).
- **★ One open slot** — next buy must clear 2+ signals AND Conviction ≥70 at a clean, non-extended entry on a settled tape. **Watch-list:** PANW on a decisive ~$367 50dMA reclaim on a settled tape (currently $346.81, further below than pre-open; signals #1+#4 present — KeyBanc OW PT ~$450, Phillip Securities Buy PT $418 — needs the technical trigger + Conviction ≥70). **HPE and DELL are knife-catches — stay out despite strong fundamentals; wait for a base.**
- **Earnings blackout next week (3-trading-day rule) — OFF-LIMITS for new buys:** CRM (Mon 11/30), NTAP (Tue 12/1), MRVL (Wed 12/2), OKTA (Wed 12/2).
- **Events runway:** **Fri 11/27 half-day (close 13:00 ET)** — thin, low-volume. Light scheduled data week of 11/30. Dec 9–10 FOMC (prior ~97–98% priced 25bp HIKE — treat as stale pending reconfirmation).

## Handoff → midday (Fri 2026-11-27 — HALF-DAY, close 13:00 ET)
- **Clock gate first:** `market_clock.py --slot midday --wait --claim --owner midday` (winter cron `0 18 UTC`). Midday (~12:00 CT / 13:00 ET) lands right at/near the half-day close bell — **confirm `/v2/clock` is_open=true before any order; stand down if the market has already closed.**
- **★ FERG conversion watch (top priority):** FERG +4.35% at the open (px 261.00), ~$1.63 from the +5% line (~$262.63). If it printed ≥$262.63 by midday, **convert the −7% hard stop (232.61) to a 10% trailing stop**. Check this first.
- **Re-verify live:** account/positions/open-orders/clock; confirm **exactly 4** open orders (FERG hard 232.61 `ea91d0f9`; NOC hard 506.26 `59a67c62`; RSG trail 231.111 `135c200e`; PG trail 157.104 `272e2864`); SPY (59) unencumbered. NOC convert at +5% (~$571.59) — not close.
- **NO stock buy planned** — nothing cleared the gate. **Only live trigger:** PANW decisive ~$367 50dMA reclaim on a settled tape AND re-score to Conviction ≥70 ($346.81 now). HPE/DELL are knife-catches — do not buy.
- **SPY same-day sweep (standing):** expect `action:none` (cash within one share of cushion) UNLESS a stop fires and frees cash → sweep SAME session. No margin.
- **Calendar (Alpaca-verified):** **Fri 11/27 half-day (close 13:00 ET)**; Mon 11/30 normal.
