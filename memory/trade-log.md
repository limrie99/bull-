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
Thesis: AI-infra leader with clean ~21-day earnings runway (next print 2026-05-20 AMC); enter starter tranche on constructive open per 4/21 19:00 CT scout.
Signals matched: [3 — secular AI/Blackwell tailwind] (only 1 hard-verified pre-trade; documented as low-conviction starter).
Stop set: $187.12 (initial day-only stop from OTO) — replaced 4/23 with GTC stop $187.28; replaced 4/27 with 10% trailing stop after position cleared +5%.
Research reference: research-log 2026-04-21 19:00 CT pre-market re-run.
Notes: OTO bracket — initial stop leg was day-only and expired the same evening; GTC replacement placed 4/23 morning.

## 2026-05-04 10:21 CT | SELL | NVDA | 25 @ $195.0184 | d42471e7-5c13-45b4-a365-6117602b1eac
Thesis: N/A — exit triggered by trailing-stop rule, not discretionary.
Signals matched: SELL #2 — 10% trailing stop activated at +5% in profit; HWM $216.73 trailed to $195.06.
Stop set: N/A (closed).
Research reference: trailing-stop placed 2026-04-27.
Notes: Realized P/L -$159.05 / -3.16% on the trade. Stop fired mid-session 5/4 — NVDA had given back ~10% from the $216.73 HWM. Mechanical exit, no discretion. Reconciled into memory at 2026-05-07 market-close routine after a stretch of halted routines (missing env vars).
