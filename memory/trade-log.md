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

## 2026-04-27 12:16 CT | STOP-CONVERT | NVDA | 25 shares | order 1d34237d
Action: canceled GTC hard stop @ $187.28 (order a3057559) and replaced with 10% trailing stop, GTC. HWM at placement: $216.73 (NVDA was up ~+7.6% from $201.38 entry, crossing the +5% threshold the strategy requires for trailing-stop activation).
Trailing stop trigger price at placement: $195.057 (10% off HWM).
Research reference: per strategy.md sell rule #2.
Notes: Backfilled 2026-05-01 from Alpaca order history — this conversion happened during the API-key outage and was never logged in trade-log/research-log at the time.

## 2026-04-22 10:07 CT | BUY | NVDA | 25 @ $201.38 | order 2b923034
Thesis: AI-infra leader, Blackwell ramp + clean ~21-day runway to 5/20 AMC earnings (outside the 3-day blackout) — starter position.
Signals matched: (3) secular AI-infra tailwind. Conviction: med (single hard signal). Sized as a starter (~5% of portfolio, $5,034.50 cost basis).
Stop set: $187.12 (-7% hard stop, OTO bracket day order — expired EOD; replaced 4/23 with $187.28 GTC stop).
Research reference: 2026-04-21 19:00 CT pre-market re-run.
Notes: Backfilled 2026-05-01 from Alpaca order history — this trade and the subsequent stop management were not logged at the time because of the API-key outage that halted the 4/22 routines.
