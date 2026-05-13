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

## 2026-04-22 10:07 CT | BUY | NVDA | 25 @ $201.38 | order_id 2b923034-96f2-4166-8d53-10b5b9a967b8
Thesis: AI-infra leader, Blackwell ramp + cap-ex cycle; starter tranche (~5% of portfolio) per 4/21 pre-market plan.
Signals matched: #3 (secular AI-infra tailwind verified); next earnings 5/20 (~21 trading days out, outside 3-day blackout).
Stop set: $187.12 (-7% hard stop as OTO sell-stop, DAY tif — expired same evening).
Research reference: memory/research-log.md 2026-04-21 19:00 CT (pre-market re-run).
Notes: OTO order class. Hard stop was DAY-only and expired 4/22 20:00 ET; trailing stop was placed manually 2026-04-27 12:16 CT (10% trail, GTC) — see next entry. Reconstructed from Alpaca activity log on 2026-05-13; was not journaled at the time.

---

## 2026-04-27 12:16 CT | STOP-UPDATE | NVDA | 25 @ trail 10% | order_id d42471e7-5c13-45b4-a365-6117602b1eac
Thesis: position appreciated past +5% threshold; per strategy, cancel hard stop and switch to 10% trailing stop.
Signals matched: N/A (risk-management action).
Stop set: 10% trailing, GTC. HWM reached $216.73 (≈ +7.6% above entry) before pulling back.
Research reference: strategy.md sell signal #2.
Notes: Reconstructed from Alpaca order detail on 2026-05-13; was not journaled at the time.

---

## 2026-05-04 10:21 CT | SELL | NVDA | 25 @ $195.0184 avg | order_id d42471e7-5c13-45b4-a365-6117602b1eac
Thesis: trailing-stop sell — strategy mechanics did their job, took us out before deeper drawdown.
Signals matched: Sell signal #2 (10% trailing stop). HWM $216.73 → stop at $195.057 → fill avg $195.0184.
Stop set: N/A (this was the stop firing).
Research reference: strategy.md sell signal #2.
Notes: Round-trip P/L = -$159.05 (-3.16%) on $5,034.50 cost basis. Reconstructed from Alpaca on 2026-05-13. NVDA has since recovered to ~$227 (2026-05-13) — so the trailing stop took us out on a normal pullback and we missed the rebound. Worth a note in the next weekly review: is 10% trail too tight for high-beta names with this much daily range, or is this just the cost of the rule working as designed?
