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

## 2026-04-22 10:07 CT | BUY | NVDA | 25 @ 201.38 | order_id 2b923034-96f2-4166-8d53-10b5b9a967b8
Thesis: Starter tranche in NVDA — AI-infra Blackwell ramp with earnings 2026-05-20 AMC as primary catalyst. Patient 5% sizing, not a conviction-max entry.
Signals matched: (3) secular AI-infra tailwind verified; (6) clear uptrend off Alpaca bars — only one fully-verified hard signal at entry, second is soft-trend → med conviction per 4/21 19:00 CT scout.
Stop set: $187.28 (-7% from entry, GTC). First OTO stop was $187.12 DAY and expired at close; replaced with a GTC stop at $187.28 (201.38 × 0.93) at 15:24 UTC on 4/22. Trailing-stop flip trigger: close ≥ $211.45 (+5%).
Research reference: memory/research-log.md 2026-04-21 19:00 CT (pre-market re-run).
Notes: Entry executed during a routine that reported HALTED in messages/log — the fill is real on Alpaca but was not captured in 4/22 memory. Back-logging here from Alpaca order history for continuity.
