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

## 2026-04-22 10:07 ET (09:07 CT) | BUY | NVDA | 25 @ 201.38 | d03cf15d-43a9-4945-b088-2d71c6e7b054 (oto parent)
Thesis: Starter tranche in NVDA on AI-infra/Blackwell catalyst, ~21 days from 5/20 earnings, outside the 3-day blackout — sized to ~5% of $100K starter.
Signals matched: (3) secular AI-infra tailwind.
Stop set: $187.12 (day stop via oto parent; expired EOD; re-placed as GTC stop at $187.28 on 4/23, then replaced with a 10% trailing stop on 4/27)
Research reference: 2026-04-21 19:00 CT pre-market entry.
Notes: **Back-filled 2026-05-25 from Alpaca order history — the original buy routine on 4/22 did not commit a trade-log entry.** Trade is reconciled from order id d03cf15d-43a9-4945-b088-2d71c6e7b054 (filled 15:07:25Z).

## 2026-05-04 11:21 ET (10:21 CT) | SELL | NVDA | 25 @ 195.0184 | d42471e7-5c13-45b4-a365-6117602b1eac
Thesis: Trailing-stop exit. NVDA ran to a high-water mark of $216.73, then faded ~10% — trailing stop triggered automatically per strategy.
Signals matched: Sell signal (2) — trailing stop fired (10% trail, was placed 4/27 after we were briefly green by enough to warrant the conversion).
Stop set: N/A (sell)
Research reference: 2026-04-21 19:00 CT entry thesis; no exit-day research-log entry exists (routine did not commit).
Notes: **Back-filled 2026-05-25 from Alpaca order history.** Realized P/L = (195.0184 − 201.38) × 25 = **−$159.04** (−3.16% on the position). Peak unrealized was roughly +$383 (hwm $216.73) — trailing-stop give-back is the cost of letting the thesis breathe per strategy. Equity has been flat at $99,840.95 with 0 positions from 5/4 through today.
