# Portfolio

**Last updated:** 2026-06-02 08:32 CT (market-open routine — verified live against Alpaca; market OPEN, marks are cash-open quotes)
**Cash:** $72,634.26
**Total equity:** $100,124.93
**Day P/L:** +$0.07 (~0.00%) vs yesterday's close ($100,124.86, account `last_equity`) — flat at the open; NVDA (+2.51%) offsetting LLY (−0.14%)
**Week P/L (week started Mon 6/1, baseline $99,840.95):** +0.28% | SPY +0.14% (5/29 close 756.34 → 757.40) | **Alpha: +0.14% WTD** — modestly ahead of the market; intraday marks, positions still young.

## Open positions

| Symbol | Shares | Avg Cost | Current | P/L $ | P/L % | Stop | Entry Date | Thesis (1 line) |
|---|---|---|---|---|---|---|---|---|
| LLY | 14 | 1078.46 | 1077.00 | −20.44 | −0.14% | 1002.57 (−7%, **GTC**) | 2026-06-01 | Q1 beat + raised FY guidance + oral GLP-1 (orforglipron) approval; GLP-1 tailwind; retatrutide + PBM coverage wins; clean uptrend |
| NVDA | 55 | 220.15 | 225.69 | +304.43 | +2.51% | 204.74 (−7%, **GTC**) | 2026-06-01 | May 20 earnings beat; AI-infra tailwind; Computex AI-PC TAM expansion; healthy uptrend |

**Open positions: 2 of 5.** **Buys used this week: 2 of 3** (LLY + NVDA filled Mon 6/1; 1 buy still in reserve through Fri). **Cash buffer: ~72.5%.** GOOGL — the planned 3rd buy — was PASSED at the open (gapped down ~4% into its AI-capex overhang = not a constructive entry); MSFT backup also passed (thin 2-signal, no fresh catalyst, soft tech morning ahead of Fri NFP).

## Stop-management state (market-open)

- Both −7% hard stops live and **GTC** (re-confirmed via `GET /v2/orders?status=open`): LLY `6c4d0225-ae01-42a9-95a6-af790a87d286` @ 1002.57, NVDA `b55fb743-57a8-48b1-8b53-221b358eb2ea` @ 204.74.
- **NVDA at +2.51% — ~$5.47 below the +5% (~$231.16) trailing-stop trigger** (cooled from the +3.23% pre-market mark). No conversion this run. If NVDA reaches +5% at a later routine: cancel hard stop b55fb743 and place a 10% trailing stop (GTC). LLY (−0.14%) nowhere near +5% or −7%.

## Recent closes (last 5)

| Symbol | Exit Date | Shares | Entry | Exit | P/L $ | P/L % | Reason |
|---|---|---|---|---|---|---|---|
| NVDA | 2026-05-04 | 25 | 201.38 | ~195.02 | −159.04 | −3.16% | 10% trailing stop fired (round-trip) |

---
*Overwrite this file every routine. Keep it a live snapshot, not a log.*
