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

## 2026-04-22 09:07 CT | BUY | NVDA | 25 @ $201.38 | order_id 2b923034-96f2-4166-8d53-10b5b9a967b8
Thesis: AI-infra leader, clean runway to 5/20 earnings, Blackwell ramp + hyperscaler capex cycle
Signals matched: (3) secular AI-infra tailwind — single verified signal at entry; position sized as a starter tranche accordingly
Stop set: $187.28 (-7% hard stop, GTC, order_id a3057559-0031-4402-9011-e75601d5320e)
Research reference: memory/research-log.md 2026-04-21 19:00 CT pre-market entry
Notes: **Backfilled 2026-04-24 06:00 CT by pre-market routine.** The fill happened during the 4/22 session after env vars were restored mid-day; no routine between fill and now logged the trade. Fill confirmed via Alpaca orders endpoint (market buy, OTO order_class, filled_avg_price $201.38 at 2026-04-22T15:07:25Z = 10:07 ET = 09:07 CT). Position sized at ~5% of portfolio ($5,034.50 cost basis / $100K equity), the "starter tranche" per the 4/21 pre-market plan.

---
