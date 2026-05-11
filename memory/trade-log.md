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
Thesis: trailing-stop exit, not discretionary — 10% trailing stop triggered from high-water $216.73.
Signals matched: Sell signal #2 (10% trailing stop, activated earlier when position went +5% in profit).
Stop set: N/A (this IS the stop fill).
Research reference: backfilled from Alpaca order history on 2026-05-11 close routine — no live research-log entry from 5/4 because routine was halted (missing secrets).
Notes: **Backfilled entry — discovered during 5/11 market-close routine.** Order ID d42471e7… filled 2026-05-04 15:21:29 UTC. Round-trip P/L: -$159.04 (-3.16%) vs entry. The trailing stop did its job — held the loss to within risk budget after the high-water mark drifted down. This is the only fill on the account between 2026-04-22 and 2026-05-11. The drift from $100K → $99,840.95 is fully explained by this single trade.

## 2026-04-22 10:07 CT | BUY | NVDA | 25 @ $201.38 | 2b923034-96f2-4166-8d53-10b5b9a967b8
Thesis: starter tranche in AI-infra leader per 2026-04-21 19:00 CT pre-market plan — Blackwell ramp, next earnings 5/20 (clear of 3-day blackout).
Signals matched: (3) secular AI-infra tailwind. Only one verified hard signal — undersized to ~5% as planned.
Stop set: OTO stop @ $187.12 (-7.08%) day order — expired same day unfilled; replaced 4/23 with GTC stop @ $187.28, then converted to 10% trailing stop on 4/27.
Research reference: backfilled — 2026-04-21 19:00 CT pre-market scout (re-run) flagged NVDA as the only clean ≥1-signal verified name.
Notes: **Backfilled entry — discovered during 5/11 market-close routine.** Order ID 2b923034… filled 2026-04-22 15:07:25 UTC. The 4/22 market-open and midday routines logged themselves as halted for missing secrets, but this fill exists on Alpaca with source "access_key" — so either secrets were restored mid-day and a routine traded without logging properly, or the user placed it manually. Either way, the account state is real. 25 sh × $201.38 = $5,034.50 cost basis. Subsequent stop management worked: hard stop placed 4/23, converted to 10% trailing 4/27 once position hit +5% (high-water $216.73 = +7.6%), exit 5/4 at -$159 loss vs cost.
