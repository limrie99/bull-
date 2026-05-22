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
Thesis: AI-infra leader; Blackwell cap-ex cycle as ongoing secular tailwind. Entry sized as starter (~5% of portfolio) per pre-market plan.
Signals matched: 3 (secular AI-infra tailwind, confirmed in 4/21 19:00 CT scout).
Stop set: $187.28 (−7% hard stop, GTC stop order via OTO bracket; later replaced with 10% trailing stop after position cleared +5% — trail HWM eventually marked $216.73).
Research reference: memory/research-log.md 2026-04-21 19:00 CT pre-market re-run.
Notes: Recorded post-hoc on 2026-05-22. The 04/22 08:30 CT market-open routine reported "halted, missing secrets" in memory, but the buy did execute live at 10:07 CT (order_class OTO, market buy). Memory and reality diverged that day — fixing the log now.

## 2026-05-04 10:21 CT | SELL | NVDA | 25 @ $195.0184 | d42471e7-5c13-45b4-a365-6117602b1eac
Thesis: closed — trailing stop triggered.
Signals matched: Sell signal #2 — 10% trailing stop after the position cleared +5% in profit. HWM hit $216.73 (~+7.6%), then pulled back through the 10% trail.
Stop set: N/A (this is the stop fill).
Research reference: memory/research-log.md 2026-04-21 19:00 CT.
Notes: Realized P/L = (195.0184 − 201.38) × 25 = **−$159.04 (−3.16%)**. Stop fired 12 trading days after entry. Recorded post-hoc on 2026-05-22 alongside the buy. Account has been 100% cash since this fill.

