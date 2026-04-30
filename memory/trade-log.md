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

## 2026-04-27 12:16 CT | STOP-SWAP | NVDA | 25 shares | trailing-stop order d42471e7-5c13-45b4-a365-6117602b1eac
Thesis: Position +5% — strategy says cancel the -7% hard stop and switch to a 10% trailing stop.
Signals matched: N/A (risk-management swap, not a buy/sell)
Stop set: 10% trailing GTC. HWM at swap = $216.73 → trigger $195.057. Replaces canceled hard stop a3057559-0031-4402-9011-e75601d5320e ($187.28).
Research reference: see strategy.md "Sell signals" rule 2.
Notes: Backfilled into the log on 2026-04-30 — the 4/22 and 4/27 routines that placed/swapped these orders never wrote to memory because the harness halted on missing env vars at that time. Order itself confirmed live in Alpaca.

## 2026-04-22 10:07 CT | BUY | NVDA | 25 @ 201.38 | 2b923034-96f2-4166-8d53-10b5b9a967b8
Thesis: AI-infrastructure leader, Blackwell ramp + cap-ex cycle; clean ~21-trading-day runway to the 2026-05-20 earnings print.
Signals matched: (3) secular AI-infra tailwind (single hard signal — sized as a starter accordingly).
Stop set: $187.28 (-7% hard stop, GTC). [Later canceled and replaced by 10% trailing on 2026-04-27 — see entry above.]
Research reference: memory/research-log.md 2026-04-21 19:00 CT pre-market entry (NVDA starter tranche plan, ~5% of portfolio).
Notes: Backfilled on 2026-04-30 — buy filled cleanly at $201.38 on 4/22 but neither the 4/22 market-open routine (halted) nor the 4/22 midday (halted) wrote it to memory at the time. Order confirmed in Alpaca.
