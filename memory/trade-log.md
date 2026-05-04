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

## 2026-04-22 10:07 CT | BUY | NVDA | 25 @ 201.38 | 2b923034-96f2-4166-8d53-10b5b9a967b8
Thesis: AI-infra leader with Blackwell ramp; verified earnings runway (next print 2026-05-20 AMC, ~21 trading days out at entry).
Signals matched: (3) secular AI-infra tailwind confirmed by Perplexity research
Stop set: $187.12 OTO bracket leg (DAY TIF — expired same day, see notes); replaced 2026-04-23 with GTC stop @ $187.28 (-7%); replaced 2026-04-27 with 10% trailing stop after position printed +7.6% intraday (HWM $216.73). Trailing trigger now $195.057.
Research reference: 2026-04-21 19:00 CT pre-market entry — "starter ~5% NVDA tranche ($5K) with -7% hard stop"
Notes: Backfilled retroactively on 2026-05-04 — trade log was empty because the 4/22 market-open and midday routines halted on missing env vars (the routine that actually placed this trade did not write to memory). $5,034.50 cost basis ≈ 5.0% of $100K starting equity. Bracket OTO stop expired same day due to DAY TIF; replaced next morning manually with GTC. Sub-agent had verified next earnings 2026-05-20, putting this trade outside the 3-day earnings blackout.
