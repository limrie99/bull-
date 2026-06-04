# Portfolio

**Last updated:** 2026-06-04 08:40 CT (market-open routine — verified live against Alpaca; market OPEN, next close 16:00 ET)
**Cash:** $59,658.22
**Total equity:** $99,949.10
**Day P/L:** +$400.67 (+0.40%) vs 6/3 close ($99,548.43, Alpaca `last_equity`). SPY −0.11% intraday (754.18 → 753.34) → **alpha today +0.51%** — ahead of the market again on a soft tape, helped by LLY strength + the cash buffer cushioning the AVGO-driven semi wobble.
**Week P/L (week started Mon 6/1, baseline $99,840.95 = 5/29 close):** +0.11% | SPY −0.40% WTD (756.34 → 753.34) | **Alpha WTD +0.50%** — comfortably ahead of the benchmark on a down week.

## Open positions

| Symbol | Shares | Avg Cost | Current | P/L $ | P/L % | Stop | +5% trail trigger | Entry Date | Thesis (1 line) |
|---|---|---|---|---|---|---|---|---|---|
| LLY | 14 | 1078.46 | 1107.25 | +403.06 | +2.67% | 1002.57 (−7%, **GTC**) | ~1132.38 | 2026-06-01 | Q1 beat + raised FY guidance + oral GLP-1 (orforglipron/Foundayo) approval; all 3 PBMs now cover obesity portfolio; GLP-1 tailwind; clean uptrend |
| NVDA | 55 | 220.15 | 215.48 | −257.13 | −2.12% | 204.74 (−7%, **GTC**) | ~231.16 | 2026-06-01 | May 20 earnings beat; AI-infra tailwind; Vera Rubin in full production; Morningstar FV→$280; thesis intact (recent dip = AVGO-spillover sentiment, not company news) |
| DE | 22 | 589.82 | 588.12 | −37.51 | −0.29% | 548.53 (−7%, **GTC**) | ~619.31 | 2026-06-04 | Q2 beat (5/21: EPS $6.55 vs $5.76, rev $13.37B vs $11.48B); ag-equipment/onshoring tailwind; clean accelerating uptrend; NON-AI diversifier |

**Open positions: 3 of 5.** **Buys used this week: 3 of 3** (LLY + NVDA Mon 6/1; DE today 6/4) — **weekly buy cap now reached.** **Cash buffer: ~59.7%.**

## Stop-management state (market-open)

- All three −7% hard stops live and **GTC** (confirmed via open-orders query, status `new`):
  - LLY `6c4d0225-ae01-42a9-95a6-af790a87d286` @ 1002.57
  - NVDA `b55fb743-57a8-48b1-8b53-221b358eb2ea` @ 204.74
  - DE `a150583a-a58c-42c9-8d12-9d7ece773841` @ 548.53
- (a) **−7% drawdown check:** worst is NVDA −2.12% (mark 215.48, stop 204.74 is ~5.0% lower) — nowhere near. No sells.
- (b) **+5% → trailing stop:** LLY +2.67% (trigger ~1132.38), NVDA −2.12% (trigger ~231.16), DE −0.29% (trigger ~619.31); none at +5%. No conversion. **Standing tasks: if LLY ≥ +5% cancel 6c4d0225 and place a 10% trailing GTC; if NVDA ≥ +5% cancel b55fb743 and place a 10% trailing GTC; if DE ≥ +5% cancel a150583a and place a 10% trailing GTC.**
- (c) **Daily loss cap:** day +0.40% — green, not near the −3% cap. (Moot — weekly buy cap reached anyway.)
- daytrade_count 0.

## DE execution note (this routine)

Deployed the 3rd/final weekly buy in DE — the pre-market lead candidate — on a settle (DE opened ~flat vs its prior close after a steep +8.5% 3-session run, so this was not chasing the spike). Sized conservatively at ~13% (not the full 15–20% high-conviction band) to respect the steep run + NFP-Friday event risk; the −7% GTC stop is the backstop. This brings the book to 3 names / ~60% cash — closer to the strategy's target of 3–4 names with a 10–20% buffer (we had been notably under-invested at ~73% cash). Fill came in fragments due to thin paper liquidity; final avg 589.82.

## GOOGL note (carried)

Still stood down — DE was the cleaner setup (industrial beat + uptrend, non-AI). GOOGL thesis intact but it kept sliding (6/3 ~359, ~363 today); re-arm only on a base + reclaim of ~$370. With the weekly buy cap now reached, GOOGL is a candidate for *next* week if it stabilizes.

## Recent closes (last 5)

| Symbol | Exit Date | Shares | Entry | Exit | P/L $ | P/L % | Reason |
|---|---|---|---|---|---|---|---|
| NVDA | 2026-05-04 | 25 | 201.38 | ~195.02 | −159.04 | −3.16% | 10% trailing stop fired (round-trip) |

---
*Overwrite this file every routine. Keep it a live snapshot, not a log.*
