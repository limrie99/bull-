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
Thesis: AI-infra leader with confirmed 2026-05-20 earnings runway and Blackwell ramp tailwind; starter tranche per 2026-04-21 19:00 CT scout plan.
Signals matched: (3) secular AI-infra tailwind
Stop set: ~$187.28 (−7% hard stop placed via OTO bracket)
Research reference: research-log 2026-04-21 19:00 CT pre-market re-run
Notes: Retroactively logged 2026-05-29 from Alpaca order history — routines were halted (missing env vars) for the period 4/22 PM through ~5/27, so this trade was never recorded in the log when it happened. Order class OTO; the bracketed stop order expired 4/22 EOD before reactivation. A replacement GTC stop @ $187.28 was placed 4/23, then canceled 4/27 when trailing-stop took over (see next entry).

## 2026-05-04 10:21 CT | SELL | NVDA | 25 @ $195.0184 | d42471e7-5c13-45b4-a365-6117602b1eac
Thesis (exit): Trailing stop triggered — position had reached HWM $216.73 (+7.6%), then retraced to $195.02 (−10% from HWM).
Signals matched: Sell signal (2) — trailing stop hit
Stop set: N/A (this was the stop fill)
Research reference: original buy log 2026-04-22; trailing stop installed via Alpaca trailing_stop GTC, trail_percent 10
Notes: Retroactively logged 2026-05-29 from Alpaca order history. Net trade P/L: −$159.04 (−3.16%). Trade worked exactly as the strategy intended — let it run to +7.6%, trailing stop locked in a partial give-back rather than letting it round-trip to the −7% hard stop. Lesson: trailing stops did their job; the underlying entry timing was a touch early (NVDA peaked just 5.7% above entry before reversing).

