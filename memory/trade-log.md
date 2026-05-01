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

## 2026-04-22 10:07 CT | BUY | NVDA | 25 @ $201.38 | a3057559-0031-4402-9011-e75601d5320e
Thesis: AI-infra leader, starter tranche per 4/21 19:00 CT scout (Blackwell ramp, secular AI cap-ex cycle); next earnings 5/20 outside the 3-day blackout.
Signals matched: 3 (secular AI-infra tailwind)
Stop set: −7% hard stop initially ($187.28, GTC) per bracket plan; replaced 2026-04-27 with 10% trailing stop after position crossed +5% (HWM reached $216.73, current trailing stop $195.057).
Research reference: memory/research-log.md — 2026-04-21 19:00 CT pre-market entry
Notes: **BACKFILL** — buy filled and stop ladder managed via Alpaca during the 4/22–5/1 memory gap (no routines wrote to trade-log between 4/22 halt and 5/1 open). Reconstructed from Alpaca order history (orders a3057559…, d42471e7…). Position fully covered by trailing stop throughout.

