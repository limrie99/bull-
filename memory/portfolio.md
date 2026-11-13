# Portfolio

**Last updated:** 2026-11-13 ~12:00 CT (**13:00 ET, MIDDAY routine**, Fri). Clock gate: `market_clock.py --slot midday` first rang **EARLY** at 17:00 UTC (summer cron `0 17` ringing ~54 min early in winter — the DST miss, status EARLY / wait_seconds 3216), so `--wait --claim --owner midday` held to the real **13:00 ET** (18:00 UTC, winter cron `0 18`), returned **DUE** (0 min after bell) and **CLAIMED** (stamp 2026-11-13, owner midday); claim pushed to main before any order. Alpaca `/v2/clock` **is_open=true** (ts 13:00:19 ET; next_close 2026-11-13 16:00; next_open 11/16 09:30). 4 required keys non-empty; EQUIBLES empty → filing data skipped. Inbox **no Pending**; Astra **no proposals**. Sleeve **3/5 (two open slots)**; weekly conviction buys **0/3** (day 5 of 5, last day). Open orders **exactly 3** (NOC hard 506.26, RSG trail 229.85064, PG trail 153.657 — both trails ratcheted UP intraday); SPY unencumbered. **NO TRADES this run** — all holdings green/healthy, nothing to convert, no sell signal; **FERG DECLINED** (live ~$256 = a chase near its 52-wk high, NOT the pre-market's approximate ~$228 pullback — Perplexity price error); **SPY sweep action:none** (cash at the ~$10k cushion). Live midday: equity **$98,105.61**, cash **$10,440.97 (~10.64%)**, intraday **−0.31%** (loss cap not hit). See research-log 2026-11-13 midday for the full handoff.

## Midday scorecard (2026-11-13 — 13:00 ET, intraday; CLOSE owns the official daily number)
- **Equity $98,105.61** · cash **$10,440.97 (10.64%)** · last_equity (Thu 11/12 settled close) $98,406.14 → **intraday P/L −$300.53 / −0.31%** (modestly red; daily loss cap NOT hit). long_mv $87,664.64; status ACTIVE.
- **SPY intraday −0.76%** (751.43 vs Thu 11/12 official close 757.16). **Book −0.31% vs SPY −0.76% → intraday alpha +0.45 pts (AHEAD).** Down tape: the defensive tilt + index floor under-participate on the way down, so the book holds up better than the market.
- **WTD (day 5 of 5; base Fri 11/6 settled close book $95,915.01 / SPY 735.40):** book **+2.28%** vs SPY **+2.18%** → **WTD alpha +0.10 pts (AHEAD, narrowly)** — today's relative gain on a down tape flipped the −0.35 pt gap carried into Fri. Close + weekly review own the final weekly number.
- **Conviction sleeve 3/5 — two slots open.** Cash at the ~$10k cushion.

## Open positions (3 conviction stocks + 1 index-floor sleeve) — live midday marks 2026-11-13 13:00 ET
| Symbol | Shares | Avg Cost | Px (13:00 ET) | P/L % | MV | Stop | Entry Date | Thesis (1 line) |
|---|---|---|---|---|---|---|---|---|
| NOC | 18 | 544.37 | 546.82 | +0.45% | $9,842.76 | **−7% HARD (GTC)** `506.26` | 2026-10-23 | Northrop Grumman, defense/aerospace. ~8% above its −7% hard. Q3 beat+raise + record backlog intact; consensus Moderate Buy, avg PT ~$644. Convert to trailing at +5% (~$571.59). INTACT. |
| PG | 65 | 148.06 | 170.085 | +14.88% | $11,055.53 | **10% TRAILING (GTC)** floor `153.657` (ratcheted up) | 2026-10-08 | Procter & Gamble — staples diversifier. Relative WINNER. **Investor Day Nov 19.** Floor above entry (profit locked). HOLD. |
| RSG | 44 | 218.00 | 253.865 | +16.45% | $11,170.06 | **10% TRAILING (GTC)** floor `229.85064` (ratcheted up) | 2026-09-18 | Republic Services — defensive waste. Relative WINNER. JPMorgan UPGRADE Neutral→Overweight PT $295 (11/11) + PT-raise wave. Q3 beat + raised FY26, $5B buyback. HOLD/STRENGTHENING. |
| SPY | 74 | 761.083 | 751.3013 | −1.29% | $55,596.30 | **NONE — index-floor sleeve, deliberate no-stop carve-out** | 2026-08-10→11-06 | S&P 500 market floor (Lauren-approved Option B + same-day sweep). Own sleeve, EXEMPT from ≤20%/max-5/max-3-per-week; NO stop. ~56.7% of book. It IS the benchmark. |

**Conviction sleeve: 3 of 5 — two open slots.** **Conviction buys used this week (11/09–11/13): 0 of 3** (last day). **Cash buffer: 10.64%** ($10,440.97 — at the ~$10k cushion). Largest non-index single name RSG $11,170.06 (11.4% of equity — well under the 20% cap). Conviction stock mv NOC+PG+RSG $32,068.35 (32.7%); SPY sleeve $55,596.30 (56.7%).

## Today's fills (2026-11-13, as of midday)
- **NONE (0 orders placed/filled at midday).** No buy, no sell, no stop trigger, no stop conversion, no SPY sweep. All three conviction stocks green; nothing near −7%; NOC (+0.45%) not yet at the +5% hard→trailing conversion line (~$571.59). **FERG declined** as a chase (live ~$256 near its 52-wk high, not a clean low-$240s pullback). SPY sweep `action:none` (cash within one SPY share of the cushion). Earlier slots today: pre-market research-only (no trades), market-open STOOD DOWN (clock NOT_DUE from a ~75-min-late firing — no un-handled risk; resting GTC stops fire automatically on Alpaca).

## Risk checks (MIDDAY 2026-11-13 13:00 ET)
- **(a) Any position −7% or worse un-stopped?** NO. NOC +0.45%, PG +14.88%, RSG +16.45% (all green); SPY −1.29% (index, no stop by design). Nothing near −7% → no Perplexity 4-hr news-check triggered.
- **(b) Any position +5%+ needing hard→trailing conversion?** NO. NOC (only HARD-stop name) is +0.45% — not yet +5% (convert at ~$571.59). PG/RSG already trail (floors ratcheted up intraday). Nothing to convert.
- **(c) Daily loss cap:** book **−0.31%** on the day — NOT breached (cap is >3% down).
- **(d) Sell signals?** NONE. NOC/PG/RSG theses all INTACT→STRENGTHENING; no −7% breach, no thesis break, no guidance cut, no "better opportunity at the 5-cap" (two slots OPEN).

## Stop-management state (open-orders — VERIFIED live 2026-11-13 MIDDAY, exactly 3)
- **NOC −7% HARD** `59a67c62-0ec7-4d59-8315-66d94b9d3d7c` — stop **506.26**, GTC, resting. qty 18. Convert at +5% (~$571.59).
- **PG 10% TRAILING** `272e2864-58a7-471f-93ad-acf3914e5a18` — floor **153.657** (ratcheted up from 153.468), trail 10%, GTC, resting. qty 65.
- **RSG 10% TRAILING** `135c200e-fc09-4a37-95c1-f940b57ae0e3` — floor **229.85064** (ratcheted up from 228.95469), trail 10%, GTC, resting. qty 44.
- **SPY — NO STOP by design** (index-floor sleeve carve-out). qty 74 unencumbered.
- Confirmed **exactly 3 open orders total** — 1 hard stop (NOC) + 2 trailing (PG/RSG). SPY unencumbered. 0 orders placed this run.

## Strategy status (MIDDAY 2026-11-13)
- **Regime:** RISK-OFF / HAWKISH. October PPI is OUT (8:30 ET); tape modestly risk-off (SPY ~−0.76%). **Dec 9 FOMC near-priced for a 25bp HIKE** (~85–90%); 10Y ~5%+. NVDA earnings 11/17 = semis whipsaw ahead. Favor quality; do NOT chase.
- **Traded today:** **NOTHING** across all slots so far. **FERG stays NEAR-TRIGGER/watchlist** (fundamentals fine — Q3 beat+raise, PT raises, beta 1.11, P/E ~22 — but ~$256 is a chase near the 52-wk high; re-arms ONLY on a genuine low-$240s hold). CDNS/AMD/XYZ rate-sensitive WATCH/DEFERRED.
- **★ Two open slots (sleeve 3/5)** — book is NOC/PG/RSG = defensive-tilted (at the 2-of-5 defensive cap). Next buys MUST be NON-defensive (beta ≥1.0) with a CLEAN entry. No bench name clears the gate on a clean entry right now.

## Watch / next (next routine: **market-close Fri 2026-11-13 ~15:00 CT / 16:00 ET**, then weekly-review ~16:00 CT / 17:00 ET)
- **Clock gate (close):** summer cron `0 20` rings ~55 min early in winter → `market_clock.py --slot market-close --wait --claim --owner market-close`; a close is NOT the close while `/v2/clock` says the bell is >20 min away. **★ The daily "How we're doing" close message + Telegram push is MANDATORY Fri regardless of trades.**
- **Risk checks:** re-verify (a)(b)(c)(d) at live marks; NOC convert to trailing ONLY at +5% (~$571.59); watch for any thesis-break headline. Re-read PG/RSG trailing floors live (ratcheting up).
- **SPY sweep:** cash at cushion → `action: none` carried forward. Re-run `spy_floor.py` only if a late stop frees fresh cash while the market is still open at the close ring.
- **Weekly review (Fri):** measure full-week book vs SPY (base Fri 11/6 close book $95,915.01 / SPY 735.40); WTD alpha +0.10 pts (narrowly ahead) at midday after flipping positive on the down tape; honest read on the defensive-tilt + ~10.6% cash drag on up-weeks vs its protection on down-days.
- **Events runway:** PPI OUT; Dec 9 FOMC near-priced for a 25bp HIKE; NVDA earnings 11/17. Keep caution on fresh rate-sensitive/high-beta beta while the 10Y is ~5%+.
- **Daily loss cap:** resets each day; a >3% intraday drop blocks new buys that day.
- **STANDING:** structural A/B default A (no Lauren reply). Astra: no proposals — keep reading the file each slot. Perplexity OPERATIONAL. Keep both UTC crons registered per slot (summer + winter).
