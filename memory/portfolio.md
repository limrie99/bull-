# Portfolio

**Last updated:** 2026-06-03 12:02 CT (midday routine — verified live against Alpaca; market OPEN, closes 15:00 CT)
**Cash:** $72,634.26
**Total equity:** $99,735.56 (live marks)
**Since last close:** −$389.30 (−0.39%) vs 6/2 close ($100,124.86, account `last_equity`). Inside the −3% daily loss cap — new buys allowed. Intraday picture improved vs the open (was −0.51% at 08:32): LLY ticked into the green (+0.87%), NVDA softened (−1.95%) on broad semis de-risking into tonight's AVGO print.
**Week P/L (week started Mon 6/1, baseline $99,840.95 = 5/29 close):** −0.11% | SPY −0.21% WTD (5/29 close 756.34 → live 754.78; −0.62% intraday vs 6/2 close 759.47) | **Alpha: ≈ +0.10% WTD** — we flipped *ahead* of SPY at midday because the market sold off harder than we did today. (Official benchmark recomputed at the close.)

## Open positions

| Symbol | Shares | Avg Cost | Current | P/L $ | P/L % | Stop | Entry Date | Thesis (1 line) |
|---|---|---|---|---|---|---|---|---|
| LLY | 14 | 1078.46 | 1087.83 | +131.11 | +0.87% | 1002.57 (−7%, **GTC**) | 2026-06-01 | Q1 beat + raised FY guidance + oral GLP-1 (orforglipron/Foundayo) approval; all 3 PBMs now cover obesity portfolio (CVS live 6/1); GLP-1 tailwind; clean uptrend |
| NVDA | 55 | 220.15 | 215.85 | −236.50 | −1.95% | 204.74 (−7%, **GTC**) | 2026-06-01 | May 20 earnings beat; AI-infra tailwind; Computex/GTC-Taipei AI-PC (RTX Spark, N1X) TAM expansion; Vera Rubin in full production; Morningstar FV→$280; healthy uptrend |

**Open positions: 2 of 5.** **Buys used this week: 2 of 3** (LLY + NVDA filled Mon 6/1). **Cash buffer: ~72.8%.** One buy held in reserve — **GOOGL remains the lead candidate** but stays stood-down (still a short-term falling knife at the open; no fresh stabilization signal at midday). Final weekly buy still available.

## Stop-management state (midday)

- Both −7% hard stops live and **GTC** (re-confirmed via open-orders query, status `new`): LLY `6c4d0225-ae01-42a9-95a6-af790a87d286` @ 1002.57, NVDA `b55fb743-57a8-48b1-8b53-221b358eb2ea` @ 204.74. (Shares show qty_available=0 because they're reserved by these protective stops — expected.)
- **NVDA at −1.95% (mark 215.85) — well above its −7% stop ($204.74) and far below the +5% (~$231.16) trailing trigger.** No conversion, no stop action. **Standing task: if NVDA ≥ +5%, cancel hard stop b55fb743 and place a 10% trailing stop GTC.**
- **LLY at +0.87% (mark 1087.83)** — first time in the green, but nowhere near the +5% trailing trigger (~$1132.38) or the −7% stop. No action.
- Daily loss cap: intraday −0.39% vs last close — inside the −3% cap. New buys allowed (none placed).

## GOOGL execution note (carried from market-open 6/3)

Stood down — still not bought. GOOGL fell 4 straight sessions into 6/2 (−3.83% high-volume distribution day), failing buy signal #6 ("clear uptrend — we don't catch knives"). No midday Perplexity scan run (not required — no position at −7%, no breaking catalyst). Fundamental thesis intact; re-arm once it stabilizes/reclaims (~$370 / 5-day base, or after ISM + tonight's AVGO digest).

## Recent closes (last 5)

| Symbol | Exit Date | Shares | Entry | Exit | P/L $ | P/L % | Reason |
|---|---|---|---|---|---|---|---|
| NVDA | 2026-05-04 | 25 | 201.38 | ~195.02 | −159.04 | −3.16% | 10% trailing stop fired (round-trip) |

---
*Overwrite this file every routine. Keep it a live snapshot, not a log.*
