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

## 2026-05-04 09:21 CT | SELL | NVDA | 25 @ $195.0184 | d42471e7-5c13-45b4-a365-6117602b1eac
Thesis: Trailing-stop exit. Position had run to HWM $216.73 (+7.62% vs entry $201.38), activating the 10% trailing stop per strategy (kicks in at +5% profit). Tape faded, trail level $195.057 was breached, auto-sold.
Signals matched: sell signal (2) — 10% trailing stop triggered after position was >+5% in profit.
Stop set: N/A (this was the stop fill)
Research reference: 2026-04-21 19:00 CT pre-market scout (NVDA starter plan)
Notes: Backfilled from Alpaca order id d42471e7 during 2026-05-19 market-close routine — memory was stale from 4/22 through today. Round-trip P/L on NVDA: −$159.04 (−3.16%) on 25 shares.

## 2026-04-22 09:07 CT | BUY | NVDA | 25 @ $201.38 | 2b923034-96f2-4166-8d53-10b5b9a967b8
Thesis: AI-infra leader, clean earnings runway (next earnings 2026-05-20 AMC at the time — ~20 trading days out, outside the 3-day blackout). Starter tranche per the 4/21 19:00 CT re-scout — ~5% of portfolio.
Signals matched: (3) secular AI-infra tailwind (Blackwell ramp, cap-ex cycle). Single hard signal; pre-market scout flagged med conviction.
Stop set: $187.12 initially (−7% hard stop, DAY tif — expired same day), replaced 4/23 with GTC stop @ $187.28, later replaced with 10% trailing stop once position cleared +5%.
Research reference: 2026-04-21 19:00 CT pre-market (re-run for 4/22 open)
Notes: Backfilled from Alpaca order id 2b923034 during 2026-05-19 market-close routine. Notional ~$5,034.50 → ~5.0% of $100K starting equity. The 4/22 morning routine log says "halted on missing keys" but the BUY clearly did fill at 09:07 CT — discrepancy worth noting; subsequent stop management (cancel/replace, trail) also happened without memory writes.
