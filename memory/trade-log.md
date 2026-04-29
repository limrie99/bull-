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
Thesis: AI-infra leader, Blackwell ramp into 5/20 earnings; clean ~21-day runway outside the 3-day blackout.
Signals matched: (3) secular AI-infra tailwind, partial (4) analyst sentiment.
Stop set: $187.28 (-7% hard stop at entry; later replaced with 10% trailing once +5%, hwm $216.73 → stop $195.06)
Research reference: 2026-04-21 19:00 CT pre-market re-run (research-log.md).
Notes: Logged retroactively on 2026-04-29 midday — original buy routine memory writes were missed. Reconstructed from Alpaca FILL activities (3 partial fills at $201.38 totaling 25 sh).

