# Portfolio

**Last updated:** 2026-06-04 12:02 CT (midday routine — verified live against Alpaca; market OPEN, next close 16:00 ET)
**Cash:** $59,658.22
**Total equity:** $100,536.16
**Day P/L:** +$987.73 (+0.99%) vs 6/3 close ($99,548.43, Alpaca `last_equity`, balance_asof 6/3 — rolled correctly today, self-correcting the 6/3 stale-value flag). SPY +0.35% intraday (754.18 → 756.835) → **alpha today +0.64%** — ahead of the market on a *green* day this time, carried by LLY's +5.1% breakout (we participated in the up-tape, not just cushioned a down one).
**Week P/L (week started Mon 6/1, baseline $99,840.95 = 5/29 close):** +0.70% | SPY +0.07% WTD (756.34 → 756.835) | **Alpha WTD +0.63%** — extending the lead built on 6/3.

## Open positions

| Symbol | Shares | Avg Cost | Current | P/L $ | P/L % | Stop | +5% trail trigger | Entry Date | Thesis (1 line) |
|---|---|---|---|---|---|---|---|---|---|
| LLY | 14 | 1078.46 | 1133.825 | +775.11 | +5.13% | **10% TRAILING (GTC)**, floor 1019.70, hwm 1133 | converted ✅ | 2026-06-01 | Q1 beat + raised FY guidance + oral GLP-1 (orforglipron/Foundayo) approval; all 3 PBMs now cover obesity portfolio; GLP-1 tailwind; clean uptrend — now +5%, trailing stop activated |
| NVDA | 55 | 220.15 | 218.6253 | −83.86 | −0.69% | 204.74 (−7%, **GTC**) | ~231.16 | 2026-06-01 | May 20 earnings beat; AI-infra tailwind; Vera Rubin in full production; Morningstar FV→$280; thesis intact (recovering +1.81% today from the 6/3 chip-sector dip — sentiment, not company news) |
| DE | 22 | 589.82 | 590.00 | +3.96 | +0.03% | 548.53 (−7%, **GTC**) | ~619.31 | 2026-06-04 | Q2 beat (5/21: EPS $6.55 vs $5.76, rev $13.37B vs $11.48B); ag-equipment/onshoring tailwind; clean accelerating uptrend; NON-AI diversifier |

**Open positions: 3 of 5.** **Buys used this week: 3 of 3** (LLY + NVDA Mon 6/1; DE 6/4) — **weekly buy cap reached** (resets Mon 6/8). **Cash buffer: ~59.3%.**

## Stop-management state (midday)

- **LLY: −7% hard stop converted to 10% trailing stop this routine** (LLY hit +5.13%). Cancelled hard stop 6c4d0225 (HTTP 204, verified), placed trailing GTC stop `6016a7e7-faac-4e93-82e7-851abf30eca8` (trail_percent 10, floor 1019.70 at placement, hwm 1133). Floor ratchets up as LLY rises; currently below entry (1078.46) so not yet locking a profit, but ~$17 above the old hard stop.
- Other two −7% hard stops live and **GTC** (confirmed via open-orders query, status `new`):
  - NVDA `b55fb743-57a8-48b1-8b53-221b358eb2ea` @ 204.74
  - DE `a150583a-a58c-42c9-8d12-9d7ece773841` @ 548.53
- (a) **−7% drawdown check:** worst is NVDA −0.69% (mark 218.63, stop 204.74 ~6.4% lower) — nowhere near. No sells.
- (b) **+5% → trailing stop:** LLY +5.13% → **converted ✅**. NVDA −0.69% (trigger ~231.16, ~5.7% away), DE +0.03% (trigger ~619.31). **Standing tasks: if NVDA ≥ +5% cancel b55fb743 and place a 10% trailing GTC; if DE ≥ +5% cancel a150583a and place a 10% trailing GTC.**
- (c) **Daily loss cap:** day +0.99% — green, not near the −3% cap. (Moot — weekly buy cap reached anyway.)
- daytrade_count 0.

## GOOGL note (carried)

Still stood down — weekly buy cap reached, so GOOGL is a candidate for *next* week (cap resets Mon 6/8) if it bases and reclaims ~$370. Thesis intact.

## Recent closes (last 5)

| Symbol | Exit Date | Shares | Entry | Exit | P/L $ | P/L % | Reason |
|---|---|---|---|---|---|---|---|
| NVDA | 2026-05-04 | 25 | 201.38 | ~195.02 | −159.04 | −3.16% | 10% trailing stop fired (round-trip) |

---
*Overwrite this file every routine. Keep it a live snapshot, not a log.*
