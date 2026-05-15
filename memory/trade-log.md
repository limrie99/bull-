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
Thesis: AI-infra leader entering a clean earnings runway (next print 2026-05-20 AMC); starter tranche to express conviction without overcommitting.
Signals matched: (3) secular AI-infra tailwind (Blackwell ramp, capex cycle); (1) verified runway to a near-term earnings catalyst.
Stop set: $187.12 (−7.08%, OTO bracket leg, day-only)
Research reference: research-log 2026-04-21 19:00 CT — pre-market (re-run)
Notes: Reconciliation entry — logged late from Alpaca activity feed during 2026-05-15 midday routine. Memory was halted on 4/22 (missing env vars) but the order executed in a prior session. Position sizing ≈ 5% of portfolio ($5,034.50), matched the planned starter tranche.

## 2026-04-27 12:16 CT | STOP-CONVERT | NVDA | 25 shares | d42471e7-5c13-45b4-a365-6117602b1eac
Thesis: position crossed +5% in profit → cancel −7% hard stop and replace with 10% trailing stop per strategy.
Signals matched: N/A (risk-management action)
Stop set: trailing 10% (gtc), high-water-mark eventually reached $216.73
Research reference: strategy.md "Risk rules" — trailing stop at +5%
Notes: Reconciliation entry — also logged late from Alpaca activity feed. Strategy executed cleanly even though memory didn't capture it at the time.

## 2026-05-04 10:21 CT | SELL | NVDA | 25 @ $195.02 (avg) | d42471e7-5c13-45b4-a365-6117602b1eac
Thesis: trailing stop triggered — exit per rules, no override.
Signals matched: sell signal (2) — 10% trailing stop hit ($195.057 stop, filled $195.0184)
Stop set: N/A (sell)
Research reference: strategy.md "Sell signals" — trailing stop
Notes: Reconciliation entry. Filled in three slices (7 @ $195.04, 12 @ $195.01, 6 @ $195.01). Realized P/L: −$159.04 (−3.16% on the position, ~−0.16% of total equity). NVDA peaked at $216.73 hwm (+7.6%) before reversing; trailing-stop math did exactly what it was designed to do — cap downside at ~10% from the peak, not from the entry. NVDA has since rebounded to $227.92 intraday on 5/15 (would've been +13% from entry if held); accept the discipline, don't relitigate.
