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

## 2026-04-22 10:07 CT | BUY | NVDA | 25 @ $201.38 | order id d5...c1 (filled at 15:07:25 UTC)
Thesis: AI-infra leader / Blackwell ramp; starter tranche ahead of 5/20 earnings.
Signals matched: (3) secular AI-infra tailwind verified.
Stop set: $187.28 (-7% hard stop placed via OTO bracket at entry).
Research reference: 2026-04-21 19:00 CT pre-market entry — "starter ~5% NVDA tranche" plan.
Notes: Reconstructed retrospectively on 2026-05-04 — the 4/22 routines halted on missing API secrets and the trade-log entry was never written at fill time. Position later crossed +5% in profit and the -7% hard stop was canceled and replaced with a 10% trailing stop (verified active 5/4 pre-market: trail_percent 10, hwm $216.73, current stop $195.057).
