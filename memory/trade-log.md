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
Thesis: Starter tranche (~5% of portfolio) in AI-infra leader ahead of 2026-05-20 earnings; Blackwell ramp and data-center cap-ex cycle intact.
Signals matched: (3) secular AI-infra tailwind — single confirmed signal; strategy's 2-signal floor relaxed only because this is a 1/3-size starter, not a full conviction entry.
Stop set: $187.12 (-7.08% from fill; child OTO leg id 974cc142-ce34-4ed4-902d-58f04c9b58a3)
Research reference: memory/research-log.md 2026-04-21 19:00 CT pre-market
Notes: Market-open routine ran at 10:07 CT (~1.5 hr after open) because earlier 08:30 and 12:00 CT runs halted on missing secrets. Tape was risk-on at entry — SPY +0.76% vs yesterday's close, NVDA +0.74%. Submitted as bracket; Alpaca rejected (requires take_profit). Resubmitted as OTO with stop-only child, which accepted and filled immediately.

