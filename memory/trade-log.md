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
Thesis: AI-infra leader with confirmed earnings runway (next print 5/20, ~21 trading days out) and verified secular tailwind (Blackwell ramp, data-center cap-ex).
Signals matched: (3) secular AI-infra tailwind — single hard-verified signal; entered as a starter tranche (~5% of portfolio) per the 2026-04-21 19:00 CT pre-market plan.
Stop set: $187.12 (-7.0% from entry), placed as a day OTO sell-stop alongside the buy. Day order expired 4/22 20:00 UTC; replaced 4/23 with a GTC stop at $187.28 (-7.0%).
Research reference: memory/research-log.md, 2026-04-21 19:00 CT pre-market re-run.
Notes: Backfilled into the log on 2026-05-22 weekly-review — this fill is in Alpaca's order history but was never written to trade-log.md at the time. OTO bracket (market buy + day stop). Total cost $5,034.50 (~5.03% of portfolio at entry).

## 2026-04-27 12:16 CT | STOP-SWAP | NVDA | n/a | trail leg created
Thesis: Position crossed +5% in profit during the week of 4/27; per strategy, cancel the -7% hard stop and replace with a 10% trailing stop to let the winner run.
Signals matched: N/A — risk-management housekeeping, not a new entry.
Stop set: 10% trailing stop, GTC. Old GTC hard stop ($187.28) canceled at the same time.
Research reference: memory/research-log.md — no routine entry was logged on 4/27. Action is reconstructed from Alpaca order history only.
Notes: Backfilled 2026-05-22. HWM eventually marked at $216.73 (about +7.6% above entry) before the trail tracked NVDA down.

## 2026-05-04 10:21 CT | SELL | NVDA | 25 @ $195.0184 | d42471e7-5c13-45b4-a365-6117602b1eac
Thesis: Sell triggered by the 10% trailing stop after NVDA pulled back from a $216.73 HWM. Exit was mechanical, not discretionary.
Signals matched: Sell signal (2) — trailing-stop trigger.
Stop set: N/A (this IS the stop fill).
Research reference: memory/research-log.md — no routine entry logged on 5/04; reconstructed from Alpaca order history.
Notes: Backfilled 2026-05-22. Proceeds $4,875.46 vs cost basis $5,034.50 → realized P/L -$159.04 (-3.16%). HWM was +7.62% above entry; trail gave back 10.0% from the high as designed. Account flat in cash from 5/05 through 5/22.
