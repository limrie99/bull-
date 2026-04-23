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
Thesis: Starter tranche in AI-infra leader ahead of 2026-05-20 earnings, per 4/21 19:00 CT pre-market plan.
Signals matched: (3) secular AI-infra tailwind (Blackwell ramp, data-center capex cycle). Conviction: med — single verified signal, sized as a 5% starter not a full position.
Stop set: $187.12 (-7% from entry) — this was an OTO day-stop that expired at Wed close; re-placed as GTC stop at $187.28 on 2026-04-23 08:00 UTC (covers all 25 shares).
Research reference: memory/research-log.md entry 2026-04-21 19:00 CT.
Notes: Fill happened on 4/22 but was never logged to memory because both scheduled 4/22 routines halted on missing env vars. Back-filled in the 2026-04-23 market-open routine once we could see the position. filled_avg_price $201.38.
