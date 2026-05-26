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

## 2026-04-22 10:07 CT | BUY | NVDA | 25 @ $201.38 | order 2b923034-96f2-4166-8d53-10b5b9a967b8
Thesis: ~5% starter tranche in NVDA — AI-infra leader with a clean earnings runway (next print 5/20), per the 4/21 pre-market scout.
Signals matched: (3) secular AI-infra tailwind. Conviction med — only buy of the week.
Stop set: $187.28 (-7% hard stop; placed GTC on 4/23 after the same-day OTO stop @ $187.12 expired). Converted to a 10% trailing stop on 4/27 once the position cleared +5%.
Research reference: research-log 2026-04-21 19:00 CT pre-market re-run.
Notes: BACKFILLED 2026-05-26 from Alpaca order history. This fill happened live but was never committed to this branch's memory (the 4/22 routines on this branch logged "halted — missing keys"). Cost basis $5,034.50.

## 2026-05-04 10:21 CT | SELL | NVDA | 25 @ $195.0184 | order d42471e7-5c13-45b4-a365-6117602b1eac
Thesis: exit — sold to close the NVDA starter.
Signals matched: Sell signal (2) — 10% trailing stop triggered. High-water mark was $216.73 (+7.6% above entry); NVDA fell ~10% off that peak and the trailing stop filled.
Stop set: N/A (this is the trailing-stop fill itself).
Research reference: trade opened 2026-04-22; see buy leg above.
Notes: BACKFILLED 2026-05-26 from Alpaca order history. Realized P/L −$159.04 (−3.16%). Proceeds $4,875.46. Trade worked as designed — let the winner breathe with a 10% trail, gave back the unrealized gain, exited small. All cash since.
