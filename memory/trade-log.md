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

## 2026-05-04 10:21 CT | SELL | NVDA | 25 @ $195.0184 | order_id d42471e7-5c13-45b4-a365-6117602b1eac
Thesis: closed by 10% trailing stop (HWM $216.73, stop $195.057). Position originally opened 2026-04-22 as the starter NVDA tranche planned in the 4/21 19:00 CT pre-market scout.
Signals matched: sell signal #2 (trailing stop triggered). Trailing stop had been activated on 4/27 once unrealized P/L crossed +5% (replacing the original −7% hard stop per strategy rule).
Stop set: N/A (this was the stop firing)
Research reference: 2026-04-21 19:00 CT pre-market entry (NVDA conviction med, $5K starter plan)
Notes: Realized −$159.04 / −3.16% on the position (entry $201.38 → exit $195.02). Entry trade itself was not logged at the time — the 4/22 market-open and midday routines halted on missing env vars; subsequent buy was placed by a later (un-logged) routine and is reconstructed from Alpaca order history. Net session of NVDA round-trip: peaked at +7.62% MTM, gave it back, system caught the exit on the 10% trail.
