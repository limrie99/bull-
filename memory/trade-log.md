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

## 2026-05-04 10:21 CT | SELL | NVDA | 25 @ $195.0184 | d42471e7-5c13-45b4-a365-6117602b1eac
Thesis: Trailing-stop exit — closed the entire NVDA position from 4/22.
Signals matched: Sell signal #2 (10% trailing stop, activated after position hit +5%).
Stop set: N/A (this WAS the stop).
Research reference: 2026-04-21 19:00 CT pre-market re-run (NVDA starter thesis).
Notes: Reconstructed retroactively from Alpaca records on 2026-05-08 weekly review — the original routine never wrote this entry. Fill was three partials at avg $195.0184 (HWM $216.73, trail 10% → stop $195.057). P/L on the round trip: −$159.04, −3.16%. NVDA closed the week at $215.21, so we got whipsawed at the bottom.

## 2026-04-22 10:07 CT | BUY | NVDA | 25 @ $201.38 | 2b923034-96f2-4166-8d53-10b5b9a967b8
Thesis: AI-infra leader, clean earnings runway (next print 5/20), starter tranche per pre-market plan.
Signals matched: (3) secular AI-infra tailwind. Single signal — entered as a starter (5% of portfolio) per the 4/21 19:00 CT scout's "small starter only if macro constructive" plan.
Stop set: $187.12 (day-TIF stop placed via OTO order).
Research reference: 2026-04-21 19:00 CT pre-market re-run.
Notes: Reconstructed retroactively from Alpaca records on 2026-05-08 weekly review — the original routine never wrote this entry. The OTO stop was day-TIF and expired same day; replaced 4/23 with a $187.28 GTC stop, then converted on 4/27 to a 10% trailing stop when position hit +5% (NVDA closed $216.54, +7.5%). $5,034.50 deployed (~5.0% of portfolio).
