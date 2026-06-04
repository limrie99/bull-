# Portfolio

**Last updated:** 2026-06-04 15:05 CT (market-close routine — verified live against Alpaca; market CLOSED, next open 2026-06-05 09:30 ET)
**Cash:** $59,658.22
**Total equity:** $100,451.62
**Day P/L:** +$903.19 (+0.91%) vs 6/3 close ($99,548.43, Alpaca `last_equity`, balance_asof 6/3 — authoritative). SPY +0.37% on the day (754.18 → 756.97 close) → **alpha today +0.54%** ✅ — ahead of the market on a green day, carried by LLY (+4.4% on the day) with NVDA recovering (+1.7%).
**Week P/L (week started Mon 6/1, baseline $99,840.95 = 5/29 close):** +0.61% | SPY +0.08% WTD (756.34 → 756.97) | **Alpha WTD +0.53%** ✅ — held the lead built 6/3→6/4 through the week.

## Open positions

| Symbol | Shares | Avg Cost | Close | P/L $ | P/L % | Stop | +5% trail trigger | Entry Date | Thesis (1 line) |
|---|---|---|---|---|---|---|---|---|---|
| LLY | 14 | 1078.46 | 1126.00 | +665.56 | +4.41% | **10% TRAILING (GTC)**, floor 1023.66, hwm 1137.4 | converted ✅ | 2026-06-01 | Q1 beat + raised FY guidance + oral GLP-1 (orforglipron/Foundayo) approval; all 3 PBMs cover obesity portfolio; GLP-1 tailwind; clean uptrend. Hit +5.1% midday → trailing stop activated; closed +4.4% (pulled back from intraday high but trailing stop stays — we never revert) |
| NVDA | 55 | 220.15 | 218.38 | −97.35 | −0.80% | 204.74 (−7%, **GTC**) | ~231.16 | 2026-06-01 | May 20 earnings beat; AI-infra tailwind; Vera Rubin in full production; Morningstar FV→$280; thesis intact (recovered +1.69% today from the 6/3 chip-sector dip — sentiment, not company news) |
| DE | 22 | 589.82 | 591.75 | +42.46 | +0.33% | 548.53 (−7%, **GTC**) | ~619.31 | 2026-06-04 | Q2 beat (5/21: EPS $6.55 vs $5.76, rev $13.37B vs $11.48B); ag-equipment/onshoring tailwind; clean accelerating uptrend; NON-AI diversifier. Bought today; quiet green first session (+0.59%) into NFP-Friday |

**Open positions: 3 of 5.** **Buys used this week: 3 of 3** (LLY + NVDA Mon 6/1; DE 6/4) — **weekly buy cap reached** (resets Mon 6/8). **Cash buffer: ~59.4%** (~40% invested, $40,793 market value).

## Stop-management state (close)

- All three protective stops confirmed RESTING as GTC (open-orders query, status `new`):
  - **LLY 10% trailing** `6016a7e7-faac-4e93-82e7-851abf30eca8` — stop_price ratcheted to **1023.66**, hwm **1137.4** (climbed from 1133 at midday as LLY pushed higher intraday before closing 1126). Floor still ~$102 below the mark — no stop risk near-term; ratchets up as LLY rises.
  - **NVDA −7% hard** `b55fb743-57a8-48b1-8b53-221b358eb2ea` @ 204.74.
  - **DE −7% hard** `a150583a-a58c-42c9-8d12-9d7ece773841` @ 548.53.
- (a) **−7% drawdown check:** worst is NVDA −0.80% (mark 218.38, stop 204.74 ~6.2% lower) — nowhere near. No sells.
- (b) **+5% → trailing stop:** LLY converted ✅ (stays even though it closed +4.41%). NVDA −0.80% (trigger ~231.16, ~5.8% away), DE +0.33% (trigger ~619.31). **Standing tasks: if NVDA ≥ +5% cancel b55fb743 → 10% trailing GTC; if DE ≥ +5% cancel a150583a → 10% trailing GTC.**
- (c) **Daily loss cap:** day +0.91% — green, nowhere near the −3% cap. (Moot — weekly buy cap reached anyway.)
- daytrade_count 0.

## GOOGL note (carried)

Still stood down — weekly buy cap reached, so GOOGL is the lead candidate for *next* week (cap resets Mon 6/8) if it bases and reclaims ~$370. Thesis intact.

## Watch tomorrow (Fri 6/5)

- **NFP (monthly US jobs report) lands pre-market** — sets the tape for the day; expect a jolt at the open. Nothing to do but be ready to read the reaction in the pre-market routine.
- LLY trailing stop floor (1023.66) climbs with any new high; watch the hwm.

## Recent closes (last 5)

| Symbol | Exit Date | Shares | Entry | Exit | P/L $ | P/L % | Reason |
|---|---|---|---|---|---|---|---|
| NVDA | 2026-05-04 | 25 | 201.38 | ~195.02 | −159.04 | −3.16% | 10% trailing stop fired (round-trip) |

---
*Overwrite this file every routine. Keep it a live snapshot, not a log.*
