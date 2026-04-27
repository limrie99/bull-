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
Thesis: AI-infra leader; Blackwell ramp + cap-ex cycle into 5/20 earnings; entered as the ~5% starter from the 4/21 19:00 CT pre-market plan.
Signals matched: secular AI-infra tailwind (signal #3); inbound near-term earnings catalyst on 2026-05-20 AMC (signal #2).
Stop set: $187.28 (-7% hard stop, bracket leg). Replaced 2026-04-27 12:00 CT with 10% trailing stop (see research-log).
Research reference: memory/research-log.md 2026-04-21 19:00 CT pre-market.
Notes: Backfilled on 2026-04-27 12:00 CT — the original buy routine on 4/22 did not append to this log; reconstructed from Alpaca order history (id 2b923034). Going forward, every routine that places an order must append here in real time.
