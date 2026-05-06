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

## 2026-05-04 10:21 CT | SELL | NVDA | 25 @ $195.0184 | d42471e7-5c13-45b4-a365-6117602b1eac
Thesis exit: 10% trailing stop triggered after position rolled over from a +7.6% peak.
Sell signal: #2 (10% trailing stop activated at +5%, then triggered).
Stop set: N/A (this WAS the stop).
Research reference: reconstructed post-hoc from Alpaca order history (cloud routines were halted 4/22–5/05 due to missing env vars; local memory missed both legs).
Notes: HWM $216.73 (peak +7.62% from $201.38 entry). Trailing stop was placed 2026-04-27 (replacing the original -7% hard stop at $187.28) once NVDA moved into +5% profit territory per strategy. Net P/L: -$159.04 (-3.16%) on the position. Followed strategy exactly; got run over by a normal pullback near the highs but the trail did its job. NVDA earnings still ahead (5/20).

## 2026-04-22 10:07 CT | BUY | NVDA | 25 @ $201.38 | 974cc142-ce34-4ed4-902d-58f04c9b58a3
Thesis: AI-infra leader, Blackwell ramp / hyperscaler cap-ex secular tailwind; next earnings 5/20 well outside the 3-day blackout.
Signals matched: #3 (secular AI-infra tailwind). Single hard signal — sized as a starter (~5% of portfolio, $5K target) per pre-market plan.
Stop set: $187.28 (-7% hard stop, GTC after the day-stop expired).
Research reference: 2026-04-21 19:00 CT pre-market re-run.
Notes: reconstructed post-hoc from Alpaca order history (cloud routines were halted 4/22–5/05 due to missing env vars; this entry never got logged in real time). OTO bracket placed a same-day stop at $187.12 which expired at the close; a fresh GTC stop at $187.28 went in 4/22 evening and was later cancelled and replaced with a 10% trailing stop on 4/27.
