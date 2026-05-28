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
Thesis: AI-infra leader, clean earnings runway (next print 2026-05-20). Starter tranche per pre-market scout.
Signals matched: (3) secular AI-infra tailwind (Blackwell ramp, cap-ex cycle)
Stop set: $187.12 (−7% hard stop via OTO bracket; replaced 2026-04-27 with separate GTC stop at $187.28; upgraded to 10% trailing on 2026-04-27 once position hit +5%)
Research reference: memory/research-log.md — 2026-04-21 19:00 CT pre-market entry
Notes: Back-filled 2026-05-28. Position value at fill $5,034.50 (~5% of portfolio). Routines went silent after this fill (env-var halts), so the journaling lapsed in real time.

## 2026-05-04 10:21 CT | SELL | NVDA | 25 @ $195.0184 | d42471e7-5c13-45b4-a365-6117602b1eac
Thesis: Position closeout via trailing stop (sell signal #2).
Signals matched: sell signal #2 — 10% trailing stop triggered. HWM was $216.73 (+7.6% from entry), trailed back through the 10% band to $195.02.
Stop set: N/A (sell leg)
Research reference: back-filled 2026-05-28 — routines were stale during this period
Notes: Net loss −$159.04 (−3.16% on the trade) — this is what brings the account to $99,840.95 today. Lessons: trailing stop did its job (let the +7.6% peak breathe, locked in some buffer before reversing), but we didn't reach the 5/20 earnings catalyst the thesis was built on. Re-examine NVDA in tomorrow's pre-market: did the 5/20 print confirm or break the thesis?
