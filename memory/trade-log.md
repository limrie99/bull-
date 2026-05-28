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
Thesis: AI-infra leader — Blackwell ramp / cap-ex cycle tailwind. Next earnings 2026-05-20 AMC, 21 trading days out (outside the 3-day blackout). Starter tranche (~5% of portfolio).
Signals matched: (3) secular AI-infra tailwind
Stop set: $187.28 (-7% hard stop, attached as OTO leg; the day-TIF leg expired EOD 4/22 and was re-placed GTC on 4/23)
Research reference: 2026-04-21 19:00 CT pre-market re-run
Notes: Filled via OTO market+stop order. The -7% hard stop was later replaced with a 10% trailing stop on 4/27 once NVDA was +5% (per strategy).

## 2026-05-04 10:21 CT | SELL | NVDA | 25 @ $195.0184 | d42471e7-5c13-45b4-a365-6117602b1eac
Thesis: 10% trailing stop triggered after NVDA pulled back from a $216.73 high water mark.
Signals matched: Sell signal (2) — trailing-stop hit
Stop set: N/A (this was the stop)
Research reference: 2026-04-21 19:00 CT pre-market re-run
Notes: P/L -$159.04 (-3.16%). Position peaked at +7.6% ($216.73) before the pullback. Trailing stop did its job — capped the round-trip at a small loss instead of a -7% hit. **Reconciled retroactively in 2026-05-28 market-open routine** (the 4/22 and 5/4 routines were halted at the time so these fills were never logged live; reconstructed from Alpaca order history).

