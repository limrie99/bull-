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

## 2026-05-04 10:21 CT | SELL | NVDA | 25 @ $195.0184 | order d42471e7-5c13-45b4-a365-6117602b1eac
Thesis: Trailing-stop exit. Bought 4/22 at $201.38; ran to HWM $216.73 (+7.6%); then 10% trailing stop pulled the trigger at $195.02.
Signals matched: Sell signal #2 (trailing stop, 10%).
Stop set: N/A (this IS the stop fill)
Research reference: 2026-04-21 19:00 CT pre-market — NVDA AI-infra thesis, starter tranche plan.
Notes: **Backfilled 2026-05-18 from Alpaca order history — was not logged at the time.** Round-trip P/L = (195.02 − 201.38) × 25 = **−$159.05** (−3.16%). Position never made it to +5%-and-out territory; trailing-stop activation happened only because Bull (or the cloud routine that ran between 4/23 and 4/27) replaced the −7% hard stop with a 10% trailing stop on 4/27. By 5/4 NVDA had pulled back from $216.73 to ~$195 and the trail triggered. Net: small loss, but trailing-stop discipline worked as designed — gave the position room to breathe up to $216 before locking in protection.

## 2026-04-22 10:07 CT | BUY | NVDA | 25 @ $201.38 | order 2b923034-96f2-4166-8d53-10b5b9a967b8
Thesis: AI-infra leader, Blackwell ramp + capex cycle. Starter tranche (~5% of portfolio) per 4/21 pre-market plan.
Signals matched: (3) secular AI-infra tailwind. (Only 1 verified hard signal — entered as a starter, not a full position.)
Stop set: $187.12 (-7% from $201.38). Initial stop was DAY-only and expired same day — replaced 4/23 with GTC stop at $187.28; then converted 4/27 to 10% trailing stop.
Research reference: 2026-04-21 19:00 CT pre-market re-run.
Notes: **Backfilled 2026-05-18 from Alpaca order history — was not logged at the time.** Routine context says this morning's market-open and midday routines halted on missing secrets, but the order on Alpaca shows the buy went through at 10:07 CT — so something ran successfully between the halted routines. Gap in our memory.
