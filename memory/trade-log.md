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

## 2026-04-22 10:07 CT | BUY | NVDA | 25 @ 201.38 | order_id 2b923034-96f2-4166-8d53-10b5b9a967b8
Thesis: AI-infra leader, Blackwell ramp + hyperscaler cap-ex cycle; starter tranche (~5% of portfolio).
Signals matched: (3) secular AI-infra tailwind verified; clean earnings runway (next print 2026-05-20 AMC, outside 3-day blackout).
Stop set: $187.12 (entry × 0.93, OTO leg, day TIF — expired same session; replaced 4/23 with GTC stop at $187.28).
Research reference: memory/research-log.md → 2026-04-21 19:00 CT pre-market entry.
Notes: _backfill 2026-04-28 by market-open — original buy was placed during a routine that did not write the log entry. Reconstructed from Alpaca order history._

## 2026-04-27 12:16 CT | STOP-SWAP | NVDA | 25 shares | order_id d42471e7-5c13-45b4-a365-6117602b1eac
Thesis: position crossed +5% threshold; per strategy, replace −7% hard stop with 10% trailing stop to let the winner run.
Signals matched: not a buy/sell — risk-management rule (strategy.md: "Trailing stop: 10% — activated once position is +5% or more in profit").
Stop set: trailing 10% GTC, hwm $216.73 → stop_price $195.057.
Research reference: strategy.md risk rules.
Notes: _backfill 2026-04-28 by market-open — original action by 4/27 routine was not logged. Reconstructed from Alpaca order history. Cancelled prior hard-stop order id a3057559-0031-4402-9011-e75601d5320e ($187.28)._
