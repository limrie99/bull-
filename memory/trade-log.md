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

## 2026-04-22 10:07 CT | BUY | NVDA | 25 @ $201.38 | 2b923034-96f2-4166-8d53-10b5b9a967b8
Thesis: Starter tranche in the AI-infra leader — clear Blackwell/cap-ex tailwind with earnings runway (5/20, outside 3-day blackout).
Signals matched: (3) secular AI-infra tailwind — only 1 hard signal verified pre-entry (conviction med); scout recommended a 5% starter, not full size.
Stop set: $187.12 (OTO day stop — expired 4/22 close). Replaced 2026-04-22 15:24 CT by GTC stop at $187.28 (order a3057559).
Research reference: memory/research-log.md 2026-04-21 19:00 CT pre-market re-run
Notes: Backfilled 2026-04-24 at market-open — the 4/22 open routine logs are missing (env vars were absent at 08:30 and 12:00 CT, then restored later). Order history on Alpaca shows the buy filled 4/22 at 15:07 UTC = 10:07 CT; the initial bracket stop expired at close and a fresh GTC stop was placed at $187.28 (= 201.38 × 0.93, the -7% hard stop). Starter size = $5,034.50 ≈ 5% of the $100K account, as planned.

