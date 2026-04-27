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

## 2026-04-22 10:07 ET (09:07 CT) | BUY | NVDA | 25 @ $201.38 | 2b923034-96f2-4166-8d53-10b5b9a967b8
Thesis: AI-infra leader, Blackwell ramp & data-center capex cycle; 5/20 AMC earnings ~21 trading days out (outside 3-day blackout). Starter tranche per 4/21 19:00 CT pre-market plan.
Signals matched: (3) secular AI-infra tailwind. Single-signal entry — sub-target size used (~5% target).
Stop set: $187.12 (initial OTO -7% hard stop, day TIF; expired same day, replaced 4/23 with GTC stop at $187.28).
Research reference: memory/research-log.md 2026-04-21 19:00 CT entry.
Notes: Back-filled 2026-04-27 15:05 CT — entry was missing from log (routines on 4/22 had logged as halted). Fill price and order-id confirmed via Alpaca /v2/orders.

## 2026-04-23 03:00 ET (02:00 CT) | STOP-PLACE | NVDA | 25 @ $187.28 (GTC) | a3057559-0031-4402-9011-e75601d5320e
Thesis: Re-establish -7% hard stop after 4/22 day-TIF leg expired. Strategy rule 1.
Signals matched: N/A (risk-management).
Stop set: $187.28 (-7.00% from $201.38 entry).
Research reference: strategy.md "Hard stop: -7% from entry."
Notes: Back-filled 2026-04-27 15:05 CT. Was canceled today (4/27 12:16 CT) when position crossed +5% and trailing stop took over.

## 2026-04-27 12:16 CT | STOP-SWAP | NVDA | 25 @ 10% trail (stop_price $195.057, HWM $216.73, GTC) | d42471e7-5c13-45b4-a365-6117602b1eac
Thesis: NVDA at $216.56 = +7.54% from $201.38 entry — crossed the +5% threshold. Per strategy rule 2, cancel the -7% hard stop and replace with 10% trailing stop.
Signals matched: N/A (risk-management; trailing-stop activation).
Stop set: 10% trailing, current stop_price $195.057, HWM $216.73.
Research reference: strategy.md "Trailing stop: 10%, activated once position is +5% in profit."
Notes: Cancel of order a3057559 confirmed at 12:16 CT, trailing stop placed same minute. No new buys today. Position remains within size limits (5.4% of equity).
