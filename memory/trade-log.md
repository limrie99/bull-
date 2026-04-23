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
Thesis: AI-infra leader, Blackwell ramp, earnings 5/20 (~21 trading days out, outside 3-day blackout). Starter tranche (~5% of portfolio).
Signals matched: (3) secular AI-infra tailwind (Blackwell / cap-ex cycle). Single hard-verified signal — sub-2-signal, sized as starter per 4/21 pre-market plan.
Stop set: $187.28 (-7% hard stop, placed as OTO sell-stop, GTC, id a3057559-0031-4402-9011-e75601d5320e)
Research reference: memory/research-log.md 2026-04-21 19:00 CT pre-market re-run
Notes: Order class OTO (one-triggers-other) — market buy triggered the resting sell-stop leg. First trade in the account.

