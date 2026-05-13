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

## 2026-04-22 10:07 CT | BUY | NVDA | 25 @ $201.38 | d03cf15d-43a9-4945-b088-2d71c6e7b054 [backfill 2026-05-13]
Thesis: Starter tranche in AI-infra leader ahead of 5/20 earnings, secular Blackwell cap-ex tailwind.
Signals matched: (3) secular AI-infra tailwind. Single verified signal — entry was below strategy's "≥2 signals" bar; flagging in weekly review.
Stop set: $187.28 (-7% hard stop, GTC, placed 4/22 20:24 UTC after the original day-stop expired)
Research reference: 2026-04-21 19:00 CT pre-market scout
Notes: Routines on 4/22 logged as "halted" but the buy actually executed in Alpaca at 15:07 UTC. This entry is being backfilled from broker history on 5/13 — memory was out of sync. order_id 2b923034-96f2-4166-8d53-10b5b9a967b8 (market buy), follow-on stop 850689f1-6bb1-4894-8f5b-1f1ac40ad867 (cancelled 4/27 when switched to trailing).

## 2026-05-04 10:21 CT | SELL | NVDA | 25 @ $195.0184 | 1d34237d-0822-428c-a48f-864dea1d0847 [backfill 2026-05-13]
Thesis: N/A (exit).
Signals matched: Sell signal #2 — 10% trailing stop, triggered from high-water mark $216.73 (which itself was ~+7.6% from entry).
Stop set: N/A
Research reference: order_id d42471e7-5c13-45b4-a365-6117602b1eac (trailing stop, trail_percent=10, placed 4/27 17:16 UTC after thesis hit +5% and we converted from hard stop)
Notes: Realized P/L -$159.04 (-3.16%). NVDA ran from $201.38 → $216.73 (~+7.6%) which triggered the +5% trailing-stop activation, then reversed -10% from hwm and filled at $195.02. Trailing-stop machinery worked as designed — the loss came from a short-lived rally before the reversal. Backfilled from broker on 5/13.

