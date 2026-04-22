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
Thesis: AI-infra leader with Blackwell ramp; 2026-05-20 AMC earnings gives a ~21 trading-day runway outside the 3-day blackout.
Signals matched: (3) secular AI-infra tailwind. Pre-market scout flagged conviction med with one verified hard signal; entered as starter tranche (~5% of portfolio, not the full 15–20% target).
Stop set: $187.12 via OTO child (DAY). **This expired at 15:00 CT close** — re-placed as GTC stop at $187.28 post-close (order a3057559-0031-4402-9011-e75601d5320e).
Research reference: memory/research-log.md → 2026-04-21 19:00 CT pre-market re-run.
Notes: OTO-with-DAY-stop template is wrong — future buys must use bracket with GTC stop, or OTO with GTC child. Lesson logged.
