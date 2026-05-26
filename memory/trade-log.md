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

## 2026-04-22 10:07 CT | BUY | NVDA | 25 @ 201.38 | order 2b923034
Thesis: AI-infra leader, ~21 trading days clear of next earnings (5/20). Starter tranche (~5% of account) per 4/21 19:00 CT pre-market plan, contingent on constructive open tone.
Signals matched: (3) secular AI-infra tailwind (Blackwell ramp / cap-ex cycle)
Stop set: −7% hard stop at $187.28
Research reference: memory/research-log.md — 2026-04-21 19:00 CT pre-market
Notes: Reconstructed from Alpaca order history during 2026-05-26 midday routine — original 4/22 routine memory entries had logged "halted on missing keys," but the BUY actually filled at 15:07:25 UTC. Memory was out of sync with broker state for ~5 weeks.

## 2026-05-04 10:21 CT | SELL | NVDA | 25 @ 195.0184 | order d42471e7
Thesis exit: 10% trailing stop triggered after NVDA rallied to hwm $216.73 (+7.62% over entry), then reversed.
Signals matched: sell signal (2) — 10% trailing stop hit (cancelled prior −7% hard stop on 4/27 when position cleared +5%, replaced with trailing per strategy)
Stop set: N/A (exit)
Research reference: memory/research-log.md — 2026-04-21 19:00 CT pre-market
Notes: Net P/L on round-trip = **−$159.04 (−3.16%)**. Reconstructed from Alpaca order history during 2026-05-26 midday routine. The trailing-stop mechanic worked exactly as the strategy designed — it just got tagged when NVDA gave back the rally. Behavior is correct; outcome is a small loss.

