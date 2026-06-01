# Portfolio

**Last updated:** 2026-06-01 12:00 CT (midday routine — verified live against Alpaca)
**Cash:** $72,634.26
**Total equity:** $99,889.97
**Day P/L:** +$49.02 (+0.05%) vs yesterday's close ($99,840.95) — quiet, NVDA's gain offsetting LLY's small dip
**Week P/L (new week, started Mon 6/1):** ~+0.05% | SPY since 5/29 close: +0.18% | Alpha: ~−0.13% (first day of the week; positions just opened — noise-level)

## Open positions

| Symbol | Shares | Avg Cost | Current | P/L $ | P/L % | Stop | Entry Date | Thesis (1 line) |
|---|---|---|---|---|---|---|---|---|
| LLY | 14 | 1078.46 | 1074.89 | −49.98 | −0.33% | 1002.57 (−7%, **GTC**) | 2026-06-01 | Q1 beat + raised FY guidance + oral GLP-1 (orforglipron) approval; GLP-1 tailwind; clean uptrend |
| NVDA | 55 | 220.15 | 221.95 | +99.00 | +0.82% | 204.74 (−7%, **GTC**) | 2026-06-01 | May 20 earnings beat; AI-infra tailwind; healthy non-extended uptrend |

**Open positions: 2 of 5.** **Buys used this week: 2 of 3** (LLY + NVDA both filled today, Mon 6/1 — the start of this trading week, so they count against this week's cap). **Cash buffer: ~73%.**

## Stop-management actions this routine

- **Both hard stops re-issued as GTC.** The morning OTO entries created stop legs with `time_in_force: day` (expiring at today's 16:00 ET close) — they would have left both positions **unprotected overnight**, silently voiding the −7% hard-stop guardrail. Cancelled the two day-TIF stops (LLY 7748b65e, NVDA e2c1f2bb) and re-placed identical −7% stops as **GTC** so protection persists. New stop IDs: LLY `6c4d0225-ae01-42a9-95a6-af790a87d286` @ 1002.57, NVDA `b55fb743-57a8-48b1-8b53-221b358eb2ea` @ 204.74.

## Recent closes (last 5)

| Symbol | Exit Date | Shares | Entry | Exit | P/L $ | P/L % | Reason |
|---|---|---|---|---|---|---|---|
| NVDA | 2026-05-04 | 25 | 201.38 | ~195.02 | −159.04 | −3.16% | 10% trailing stop fired (round-trip) |

---
*Overwrite this file every routine. Keep it a live snapshot, not a log.*
