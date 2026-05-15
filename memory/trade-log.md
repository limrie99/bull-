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
Thesis: AI-infra leader, Blackwell ramp into 5/20 earnings — starter tranche (~5% of account).
Signals matched: (3) secular AI-infra tailwind — single verified signal, medium-low conviction starter sized to risk.
Stop set: $187.12 (initial -7% bracket leg, DAY tif — later replaced by GTC stop @ $187.28, then by 10% trailing stop on 4/27)
Research reference: memory/research-log.md 2026-04-21 19:00 CT pre-market re-run
Notes: Reconstructed retroactively from Alpaca order history — this routine fired before the secrets outage took the dashboard offline. Initial stop leg was DAY tif (mistake — should have been GTC); a fresh GTC stop was placed the same evening. On 4/27 the position had cleared +5%, so the -7% stop was canceled and replaced with a 10% trailing stop (per strategy.md).

## 2026-05-04 10:21 CT | SELL | NVDA | 25 @ $195.0184 | d42471e7-5c13-45b4-a365-6117602b1eac
Thesis: N/A (sell leg — trailing stop auto-trigger).
Signals matched: Sell signal (2) — 10% trailing stop triggered. HWM was $216.73 (+7.62% from entry).
Stop set: N/A (this IS the stop fill)
Research reference: memory/research-log.md 2026-04-21 19:00 CT pre-market re-run (entry thesis); no fresh research at exit (system was offline).
Notes: P/L = ($195.0184 - $201.38) × 25 = **-$159.04 (-3.16%)**. Position ran to $216.73, gave back ~10%, trailing stop took us out. Mechanical exit, no thesis broken — the stop did its job. Honest read: with no human/system oversight during the 4/22 → 5/15 outage, the trailing-stop rail is what kept this from being a worse loss. NVDA has since rebounded to ~$226 — opportunity cost is real, but re-entry without a fresh signal is not in the strategy.
