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
Thesis: AI-infra leader, Blackwell ramp + hyperscaler capex tailwind, earnings 5/20 AMC (~21 trading days out at entry).
Signals matched: (3) secular AI-infra tailwind. Single verified signal at entry — sized as a starter tranche per 4/21 19:00 pre-market plan.
Stop set: $187.12 (−7% hard stop, OTO bracket, day TIF — expired same session and was replaced 4/23 with GTC stop @ $187.28).
Research reference: memory/research-log.md 2026-04-21 19:00 CT pre-market re-run.
Notes: Backfilled 2026-04-30 — cloud routine that placed the buy did not write memory back due to subsequent halt window. Recovered from Alpaca order history.

## 2026-04-27 12:16 CT | STOP-ROTATION | NVDA | 25 sh | order_id d42471e7-5c13-45b4-a365-6117602b1eac
Action: Canceled GTC hard stop @ $187.28 (order a3057559) and placed 10% trailing stop, GTC, qty 25.
Trigger: position hit +5% profit threshold (HWM $216.73 = +7.6% over $201.38 entry) → strategy rule (sell signal #2 inverse) requires switching from −7% hard stop to 10% trailing stop.
Current trailing stop: $195.057 (HWM $216.73, trail 10%).
Notes: Backfilled 2026-04-30. Not a buy or sell leg, but logged here for the trade-log audit trail since it materially changes the risk profile of the position.

