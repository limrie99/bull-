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

## 2026-04-22 10:07 CT | BUY | NVDA | 25 @ $201.38 | a3057559-... (parent: 2b923034-96f2-4166-8d53-10b5b9a967b8)
Thesis: AI-infrastructure leader; Blackwell ramp + AI cap-ex cycle, next earnings 2026-05-20 AMC (outside the 3-day blackout). Starter sizing (~5% of $100K) per pre-market 4/21 19:00 CT plan.
Signals matched: (3) secular AI-infra tailwind, (6) clear uptrend (not at 52-week lows). Single hard signal verified pre-entry → starter sizing only, not full conviction.
Stop set: −7% hard stop at $187.28 GTC (placed 2026-04-22 15:24 CT). Replaced 2026-04-27 12:16 CT with 10% trailing stop GTC at $195.057 (HWM $216.73, position had crossed +5% in profit per strategy rule).
Research reference: research-log 2026-04-21 19:00 CT (pre-market re-run for 4/22 open).
Notes: **Retro-logged at 2026-04-30 market-close.** The 4/22 market-open and midday Bull routines both halted on missing API keys. The user (or a manual session) executed the planned starter, set the −7% bracket, and later swapped to the 10% trailing per strategy. All consistent with the strategy file; only the trade-log audit was missing — this entry closes the gap.
