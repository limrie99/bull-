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

## 2026-05-04 10:21 CT | SELL | NVDA | 25 @ $195.02 | d42471e7-5c13-45b4-a365-6117602b1eac
Thesis: 10% trailing stop triggered (sell signal #2) — locked in the ~10% pullback off the high after the position had moved into +5% profit territory.
Signals matched: Sell signal #2 (trailing stop fill).
Stop set: N/A (this *is* the stop fill).
Research reference: 2026-04-21 19:00 CT pre-market scout, plus inferred trailing-stop conversion on/around 2026-04-27.
Notes: Filled in three partials (7 @ $195.04, 12 @ $195.01, 6 @ $195.01 — avg $195.02) on 2026-05-04 15:21 UTC. Trailing-stop sell order itself was opened 2026-04-27 13:16 ET, after NVDA crossed +5% from the $201.38 entry. Round-trip realized P/L: 25 × ($195.02 − $201.38) = **−$159.00 (−3.16%)**. Logged retroactively at midday 2026-05-07 because routines were halted on missing env vars during this window — Alpaca executed the orders that had already been placed/staged.

## 2026-04-22 10:07 CT | BUY | NVDA | 25 @ $201.38 | 2b923034-96f2-4166-8d53-10b5b9a967b8
Thesis: AI-infrastructure leader, ~21 trading days clear of next earnings — opening the planned ~5% starter tranche from the 2026-04-21 19:00 CT scout.
Signals matched: #3 (secular AI-infra tailwind — Blackwell ramp / hyperscaler cap-ex).
Stop set: ~$187.28 (−7% bracket child, time_in_force=day → expired at close; replaced and later canceled when position crossed +5% in profit).
Research reference: 2026-04-21 19:00 CT pre-market re-run.
Notes: Logged retroactively at midday 2026-05-07 — the live routines on 4/22 ran in halted mode (missing env vars) so this trade was not recorded in memory at the time. Reconstructed from Alpaca orders + activities feed.
