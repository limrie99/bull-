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

## 2026-04-22 10:07 CT | BUY | NVDA | 25 @ $201.38 | order_id a3057559-... (stop leg), parent 2b923034-96f2-4166-8d53-10b5b9a967b8
Thesis: AI-infra leader with a clean earnings runway (next print 2026-05-20 AMC, 21 trading days out) and secular AI cap-ex tailwind.
Signals matched: (3) secular AI-infra tailwind (Blackwell ramp / data-center cap-ex cycle).
Stop set: $187.12 (day, original OTO stop, expired 4/22 close) → replaced by $187.28 GTC stop (−7% from entry) on 4/22 16:24 CT.
Research reference: memory/research-log.md 2026-04-21 19:00 CT pre-market re-run (starter tranche plan, ~5% sizing).
Notes: Back-filled by 2026-04-23 midday routine — 4/22 market-open message log claimed a halt, but Alpaca shows the buy filled at 10:07 CT 4/22 via OTO market + stop. Position size $5,034.50 cost basis ≈ 5.0% of equity — matches the starter-tranche plan. Stop was rebuilt as a standalone GTC after the original day-order expired.

