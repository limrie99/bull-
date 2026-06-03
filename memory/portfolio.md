# Portfolio

**Last updated:** 2026-06-03 15:05 CT (market-close routine — verified live against Alpaca; market CLOSED, next open 2026-06-04 09:30 ET)
**Cash:** $72,634.26
**Total equity:** $99,617.82 (official closing marks)
**Day P/L:** −$191.47 (−0.19%) vs 6/2 close ($99,809.29, per 6/2 research-log EOD). SPY −0.70% today → **alpha today +0.51%** — we beat the market on a down day (defensive ~73% cash + LLY strength cushioned us).
**Week P/L (week started Mon 6/1, baseline $99,840.95 = 5/29 close):** −0.22% | SPY −0.29% WTD (756.34 → 754.18) | **Alpha WTD +0.07%** — nudged ahead of the benchmark for the first time this week.

> Note: Alpaca `last_equity` read $100,124.86 (stale = 6/1 EOD, didn't roll to 6/2), and portfolio-history was flat/unreliable this pull — so yesterday's close was taken from the 6/2 research-log EOD value ($99,809.29), which is the correct day-over-day baseline.

## Open positions

| Symbol | Shares | Avg Cost | Current | P/L $ | P/L % | Day % | Stop | Entry Date | Thesis (1 line) |
|---|---|---|---|---|---|---|---|---|---|
| LLY | 14 | 1078.46 | 1083.54 | +71.12 | +0.47% | +1.82% | 1002.57 (−7%, **GTC**) | 2026-06-01 | Q1 beat + raised FY guidance + oral GLP-1 (orforglipron/Foundayo) approval; all 3 PBMs now cover obesity portfolio; GLP-1 tailwind; clean uptrend |
| NVDA | 55 | 220.15 | 214.80 | −294.25 | −2.43% | −3.60% | 204.74 (−7%, **GTC**) | 2026-06-01 | May 20 earnings beat; AI-infra tailwind; Computex/GTC-Taipei AI-PC TAM expansion; Vera Rubin in full production; Morningstar FV→$280; thesis intact |

**Open positions: 2 of 5.** **Buys used this week: 2 of 3** (LLY + NVDA, Mon 6/1). **Cash buffer: ~72.9%.** One weekly buy still in reserve — GOOGL remains the lead candidate, still stood down (see history below); re-arm on stabilization.

## Stop-management state (market-close)

- Both −7% hard stops live and **GTC** (confirmed via open-orders query, status `new`, expires 2026-08-28): LLY `6c4d0225-ae01-42a9-95a6-af790a87d286` @ 1002.57, NVDA `b55fb743-57a8-48b1-8b53-221b358eb2ea` @ 204.74. No expiry-at-close gap.
- (a) **−7% drawdown check:** worst is NVDA −2.43% (mark 214.80, stop 204.74 is ~4.7% lower) — nowhere near. No sells. NVDA's −3.60% day = broad semiconductor/market weakness + investor selling (Perplexity: no company-specific bad news, no downgrade); thesis intact.
- (b) **+5% → trailing stop:** LLY +0.47%, NVDA −2.43%; neither at +5% (NVDA trigger ~$231.16). No conversion. **Standing task: if NVDA ≥ +5%, cancel hard stop b55fb743 and place a 10% trailing stop GTC.**
- (c) **Daily loss cap:** day −0.19% vs prior close — well inside the −3% cap. (Moot — no buys planned.)
- daytrade_count 0.

## GOOGL execution note (carried from market-open 6/3)

Stood down — did NOT buy. GOOGL fell 4 straight sessions into 6/2 (~−7%) incl. a −3.83% high-volume distribution day, failing buy signal #6 ("clear uptrend — we don't catch knives"). Fundamental thesis intact; re-arm once it stabilizes/reclaims (~$370 / 5-day base after ISM + AVGO digest). On a broad −0.70% SPY down day today, standing down looks correct.

## Recent closes (last 5)

| Symbol | Exit Date | Shares | Entry | Exit | P/L $ | P/L % | Reason |
|---|---|---|---|---|---|---|---|
| NVDA | 2026-05-04 | 25 | 201.38 | ~195.02 | −159.04 | −3.16% | 10% trailing stop fired (round-trip) |

---
*Overwrite this file every routine. Keep it a live snapshot, not a log.*
