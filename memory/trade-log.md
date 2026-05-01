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

## 2026-04-22 10:07 CT | BUY | NVDA | 25 @ $201.38 | order_id 2b923034-96f2-4166-8d53-10b5b9a967b8
Thesis: AI-infra leader; Blackwell ramp + cap-ex cycle, earnings 5/20 AMC.
Signals matched: (3) secular AI-infra tailwind. Med conviction starter (~5% sizing).
Stop set: $187.28 (−7% hard stop, OTO leg, order_id 974cc142-ce34-4ed4-902d-58f04c9b58a3 — later expired/replaced).
Research reference: 2026-04-21 19:00 CT pre-market re-run.
Notes: Backfilled from Alpaca order history during 2026-05-01 market-close routine — the original trade was placed in a window where the trade-log was not written (memory keys had been intermittent on 4/22). Fill confirmed via /v2/orders.

## 2026-04-27 12:16 CT | STOP-MGMT | NVDA | trailing 10% replaces hard stop | order_id d42471e7-5c13-45b4-a365-6117602b1eac
Thesis: Per strategy — once a position clears +5% in profit, cancel the −7% hard stop and place a 10% trailing stop.
Signals matched: N/A (risk-management action, not a buy/sell signal).
Trailing stop: 10% trail, GTC, HWM at placement $216.73 → initial trip price $195.057. Old hard stop $187.28 (order a3057559) canceled at the same time.
Research reference: strategy.md — sell signal #2.
Notes: Backfilled from Alpaca order history during 2026-05-01 market-close routine. Confirmed: old stop status=canceled, new trailing stop status=new.
