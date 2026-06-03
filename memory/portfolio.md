# Portfolio

**Last updated:** 2026-06-03 08:32 CT (market-open routine — verified live against Alpaca; market OPEN, closes 15:00 CT)
**Cash:** $72,634.26
**Total equity:** $99,614.93 (live marks)
**Since last close:** −$509.93 (−0.51%) vs 6/2 close ($100,124.86, account `last_equity`). Inside the −3% daily loss cap. Early-session softness: LLY −0.74% on the day, NVDA −0.48% on the day.
**Week P/L (week started Mon 6/1, baseline $99,840.95 = 5/29 close):** −0.23% | SPY +0.31% intraday (5/29 close 756.34 → live ~758.69) | **Alpha: ≈ −0.54% WTD** — still trailing on day-3 of exposure; positions only 2 days old, theses intact and need time. (Official benchmark recomputed at the close.)

## Open positions

| Symbol | Shares | Avg Cost | Current | P/L $ | P/L % | Stop | Entry Date | Thesis (1 line) |
|---|---|---|---|---|---|---|---|---|
| LLY | 14 | 1078.46 | 1056.27 | −310.72 | −2.06% | 1002.57 (−7%, **GTC**) | 2026-06-01 | Q1 beat + raised FY guidance + oral GLP-1 (orforglipron/Foundayo) approval; all 3 PBMs now cover obesity portfolio (CVS live 6/1); GLP-1 tailwind; clean uptrend |
| NVDA | 55 | 220.15 | 221.75 | +87.95 | +0.73% | 204.74 (−7%, **GTC**) | 2026-06-01 | May 20 earnings beat; AI-infra tailwind; Computex/GTC-Taipei AI-PC (RTX Spark, N1X) TAM expansion; Vera Rubin in full production; Morningstar FV→$280; healthy uptrend |

**Open positions: 2 of 5.** **Buys used this week: 2 of 3** (LLY + NVDA filled Mon 6/1). **Cash buffer: ~72.9%.** One buy held in reserve — **GOOGL remains the lead candidate** but was **STOOD DOWN at this open** (see below); the final weekly buy is still available.

## Stop-management state (market-open)

- Both −7% hard stops live and **GTC** (re-confirmed via open-orders query, status `new`): LLY `6c4d0225-ae01-42a9-95a6-af790a87d286` @ 1002.57, NVDA `b55fb743-57a8-48b1-8b53-221b358eb2ea` @ 204.74. (Shares show qty_available=0 because they're reserved by these protective stops — expected.)
- **NVDA at +0.73% (mark 221.75) — well below the +5% (~$231.16) trailing trigger.** No conversion. **Standing task: if NVDA ≥ +5%, cancel hard stop b55fb743 and place a 10% trailing stop GTC.**
- LLY (−2.06%) nowhere near +5% or −7%; thesis intact, sector/tape softness only.
- Daily loss cap: intraday −0.51% vs last close — inside the −3% cap. New buys allowed (none placed).

## GOOGL execution note (market-open 6/3)

Stood down — did NOT buy. GOOGL fell 4 straight sessions (5/28 c390.15 → 6/2 c361.84, ~−7%) including a **−3.83% high-volume distribution day on 6/2** (1.8× normal volume), and is only bouncing +0.9% intraday today, 25 min before the 10:00 ET ISM print with AVGO reporting tonight. That fails buy signal #6 ("clear uptrend — we don't catch knives") and the plan's "if it opens/holds constructively" condition. Fundamental thesis intact; re-arm once it stabilizes/reclaims (~$370 / 5-day, or a base after ISM + AVGO digest).

## Recent closes (last 5)

| Symbol | Exit Date | Shares | Entry | Exit | P/L $ | P/L % | Reason |
|---|---|---|---|---|---|---|---|
| NVDA | 2026-05-04 | 25 | 201.38 | ~195.02 | −159.04 | −3.16% | 10% trailing stop fired (round-trip) |

---
*Overwrite this file every routine. Keep it a live snapshot, not a log.*
