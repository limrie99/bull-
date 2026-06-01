# Portfolio

**Last updated:** 2026-06-01 10:46 CT (market-open routine — verified live against Alpaca; reconciled with concurrent midday/weekly-review writes — see note)
**Cash:** $72,634.26
**Total equity:** $99,855.40
**Day P/L:** ~+$14 (~+0.01%) — just entered two positions, both fractionally green
**Week P/L:** +0.00% (week ending 5/29, pre-trade) | SPY week: +0.83% | Alpha: −0.83% (we were 100% cash for the measured week; today's re-entry is the start of next week's exposure)

## Open positions

| Symbol | Shares | Avg Cost | Current | P/L $ | P/L % | Stop | Entry Date | Thesis (1 line) |
|---|---|---|---|---|---|---|---|---|
| LLY | 14 | 1078.46 | 1079.61 | +16.10 | +0.11% | 1002.57 (−7%) | 2026-06-01 | Q1 beat + raised FY guidance + oral GLP-1 (orforglipron) approval; GLP-1 tailwind; clean uptrend |
| NVDA | 55 | 220.15 | 220.12 | −1.65 | −0.01% | 204.74 (−7%) | 2026-06-01 | May 20 earnings beat; AI-infra tailwind; healthy non-extended uptrend |

**Open positions: 2 of 5.** **Buys used this week: 2 of 3.** **Cash buffer: ~73%.**

## Recent closes (last 5)

| Symbol | Exit Date | Shares | Entry | Exit | P/L $ | P/L % | Reason |
|---|---|---|---|---|---|---|---|
| NVDA | 2026-05-04 | 25 | 201.38 | ~195.02 | −159.04 | −3.16% | 10% trailing stop fired (round-trip) |

---
**⚠ Concurrency note (2026-06-01):** Three routines fired near-simultaneously today. The `midday` (narrative 12:00 CT) and `weekly-review` (16:00 CT) routines snapshotted Alpaca *before* this market-open routine's orders filled (fills at 15:46 UTC; their commits at 15:42–15:43 UTC), so their memory shows a flat/all-cash book. That was true at the instant they looked. **The live broker account now holds the 2 positions above — this snapshot is the current truth.** The earlier all-cash narratives are preserved in the message/research logs as the history they are. The cash-drag those entries describe is now resolved.

*Overwrite this file every routine. Keep it a live snapshot, not a log.*
