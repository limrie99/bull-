# Trade Log

**Append-only. Never edit past entries.** Each entry is a single trade (buy or sell leg).

Format:

```
## YYYY-MM-DD HH:MM CT | BUY|SELL | SYMBOL | qty @ price | order_id
Thesis: one sentence
Signals matched: [list from strategy.md buy signals, or sell signal number]
Stop set: $price (or N/A for sells)
Research reference: link or date of research-log entry
Notes: anything unusual about the fill or context
```

---

_Note: 2026-05-22 — Trade log was empty but Alpaca shows NVDA round-trip from 4/22→5/4 that prior routines never wrote here (memory was stale through the dormant period). Backfilling from Alpaca order history below for accuracy. From 2026-05-22 forward, every trade gets logged in the same routine it's placed._

## 2026-04-22 10:07 CT | BUY | NVDA | 25 @ $201.38 | order 2b923034-96f2-4166-8d53-10b5b9a967b8
Thesis: Starter ~5% tranche in NVDA — AI-infra leader on Blackwell ramp + cap-ex cycle, ~21 trading days to next earnings.
Signals matched: (3) secular AI-infra tailwind. Conviction med per 4/21 19:00 CT pre-market re-run.
Stop set: $187.12 (-7% hard stop, OTO leg — day-only TIF, expired same evening; replaced GTC 4/23).
Research reference: research-log 2026-04-21 19:00 CT.
Notes: OTO order. Stop leg was placed as DAY TIF and expired at 4 PM close — replaced 4/23 08:00 with a GTC stop at $187.28. Memory routines weren't writing through this period; reconciled from Alpaca on 2026-05-22.

## 2026-05-04 10:21 CT | SELL | NVDA | 25 @ $195.0184 | order d42471e7-5c13-45b4-a365-6117602b1eac
Thesis: Trailing-stop exit. The trailing stop was placed 4/27 (cancel of GTC -7% hard stop + new 10% trailing stop) once NVDA crossed the +5% profit threshold per strategy rule.
Signals matched: Sell signal #2 — 10% trailing stop triggered. HWM hit $216.73; trailing-stop price $195.057 was breached.
Stop set: N/A (this IS the stop being executed).
Research reference: research-log 2026-04-21 19:00 CT (entry thesis); no fresh research entry exists for the 4/27 stop-management or the 5/4 exit because memory routines were stale.
Notes: Round-trip P&L = ($195.0184 - $201.38) × 25 = -$159.04 (-3.16%). Reconciled from Alpaca on 2026-05-22.

