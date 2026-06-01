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

## 2026-04-22 08:30 CT | BUY | NVDA | 25 @ 201.38 | (reconciled from Alpaca FILL activity)
Thesis: AI-infra secular tailwind; NVDA next earnings 5/20; constructive open.
Signals matched: #3 (secular tailwind), #6 (uptrend). Conviction: medium, ~5% starter.
Stop set: $187.28 (-7% hard stop at entry)
Research reference: research-log 2026-04-21 pre-market
Notes: 3 fills (6 + 2 + 17 sh) all @ 201.38 = $5,034.50. On 4/27 the +6% gain converted the hard stop to a 10% trailing stop per strategy.

## 2026-05-04 ~time CT | SELL | NVDA | 25 @ ~195.02 | (reconciled from Alpaca FILL activity)
Thesis (exit): trailing stop fired — NVDA gave back its gain and round-tripped through entry.
Signals matched: sell signal #2 (10% trailing stop triggered).
Stop set: N/A
Research reference: midday 2026-05-04 ("NVDA trailing stop fired")
Notes: 3 fills (6 + 12 + 7 sh) @ 195.01–195.04 = $4,875.46. Realized P/L = **−$159.04 (−3.16%)**. This is the only completed trade of the Apr 22 – Jun 1 period; account held 100% cash afterward.
