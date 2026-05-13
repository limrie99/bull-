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
Thesis: AI-infra leader with clean earnings runway (next print 2026-05-20), Blackwell ramp + cap-ex cycle as secular tailwind.
Signals matched: (3) secular AI-infra tailwind confirmed by research.
Stop set: $187.12 (-7% hard stop via OTO order, later replaced by GTC stop @ $187.28 on 4/23, then by 10% trailing stop on 4/27 once profit exceeded +5%).
Research reference: memory/research-log.md 2026-04-21 19:00 CT pre-market re-run (NVDA starter plan).
Notes: Recorded retroactively — the 4/22 market-open routine logged a halt but the trade was actually placed via Alpaca. The starter tranche came in at ~$5,034.50 of notional value (~5% of account).

## 2026-05-04 10:21 CT | SELL | NVDA | 25 @ $195.0184 | d42471e7-5c13-45b4-a365-6117602b1eac
Thesis: Trailing stop fired — NVDA ran to a high of $216.73 (+7.6% from entry), then gave back 10% from that high to trigger the trailing stop.
Signals matched: Sell signal (2) — 10% trailing stop hit after the position was activated at +5% profit.
Stop set: N/A (closing trade).
Research reference: memory/research-log.md 2026-04-21 19:00 CT (original buy thesis).
Notes: Recorded retroactively. Round-trip P/L = ($195.0184 − $201.38) × 25 = **−$159.04 (−3.16%)**. The trailing stop worked as designed: limited a worse drawdown after the run faded, but the conversion from −7% hard stop to 10% trailing happened at $216.73 HWM (4/27), so the stop sat at exactly $195.06 by the time it filled. Bigger lesson: a single 5%-of-account starter that round-trips is acceptable noise; we're learning the mechanics.
