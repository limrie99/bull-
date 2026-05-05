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

## 2026-04-22 10:07 CT | BUY | NVDA | 25 @ $201.38 | order_id 2b923034-96f2-4166-8d53-10b5b9a967b8
Thesis: AI-infra leader with verified secular tailwind (Blackwell ramp); next earnings 2026-05-20 AMC, 21 trading days out — clear of 3-day blackout. Starter ~5% of portfolio.
Signals matched: (3) secular tailwind. Single-signal entry as a starter tranche per 4/21 19:00 CT pre-market scout.
Stop set: $187.12 hard stop (DAY child of OTO order; expired unfilled). GTC stop at $187.28 placed 4/23, later canceled 4/27 when trailing-stop replaced it (likely after position crossed +5%).
Research reference: memory/research-log.md 2026-04-21 19:00 CT entry.
Notes: Reconstructed from Alpaca order history at 2026-05-05 market-close — Bull's 4/22 routines were halted (missing env vars) so this trade was not logged in real time. Cost basis: $5,034.50.

## 2026-05-04 10:21 CT | SELL | NVDA | 25 @ $195.0184 | order_id d42471e7-5c13-45b4-a365-6117602b1eac
Thesis: Position closed by 10% trailing stop after NVDA retraced from hwm $216.73.
Signals matched: Sell signal #2 (10% trailing stop activated when position was +5% in profit — strategy.md exit rule).
Stop set: N/A (this IS the stop fill).
Research reference: memory/research-log.md 2026-05-05 15:00 CT entry.
Notes: Reconstructed at 2026-05-05 close. Trail percent 10, hwm $216.73, fill $195.0184. Proceeds $4,875.46. Realized P/L: -$159.04 (-3.16%). Trailing-stop mechanic worked as designed.

---
