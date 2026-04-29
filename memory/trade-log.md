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
Thesis: Starter tranche in AI-infra leader; clean ~21-day runway to 5/20 earnings; secular Blackwell ramp / cap-ex tailwind.
Signals matched: (3) secular AI-infra tailwind verified
Stop set: -7% hard stop at $187.28 (placed via OTO, day-only stop expired same session; replaced 4/23 with GTC stop at $187.28)
Research reference: 2026-04-21 19:00 CT pre-market re-run
Notes: BACKFILLED 2026-04-29 — original buy was placed 4/22 but the routine that placed it did not write to trade-log. Reconstructed from Alpaca order history (id above; filled_at 2026-04-22T15:07:25Z = 10:07 CT). Sized ~$5,034 (~5% of portfolio), matching the starter plan in the 4/21 19:00 research log.

## 2026-04-27 12:16 CT | STOP-FLIP | NVDA | 25 sh trailing 10% | d42471e7-5c13-45b4-a365-6117602b1eac
Thesis: NVDA crossed +5% in profit; per strategy, cancel the -7% hard stop and replace with a 10% trailing stop.
Signals matched: N/A (risk-management action)
Stop set: 10% trailing stop, GTC. HWM at conversion = peak after entry; current HWM $216.73, current trail stop_price $195.057.
Research reference: strategy.md — "Sell signals" rule 2 (10% trailing stop activated once position is +5% in profit)
Notes: BACKFILLED 2026-04-29 — action was performed by a prior routine (cancel of GTC stop 187.28 + new trailing_stop order, both at 4/27 17:16 UTC) but not logged here. Trailing stop is currently live (status=new, active).
