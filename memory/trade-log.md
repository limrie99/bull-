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
Thesis: AI-infra leader, clean earnings runway (5/20 AMC), starter tranche per 4/21 pre-market plan.
Signals matched: (3) secular AI-infra tailwind (Blackwell ramp, cap-ex cycle).
Stop set: $187.28 (initial -7% hard stop placed as OTO leg; later upgraded to 10% trailing once position became profitable).
Research reference: memory/research-log.md 2026-04-21 19:00 CT entry.
Notes: Reconstructed from Alpaca order history — the routine that placed this never wrote to the trade log (likely halted on missing env vars between routines). $201.38 × 25 = $5,034.50 deployed (~5% of $100K).

## 2026-05-04 10:21 CT | SELL | NVDA | 25 @ 195.0184 | d42471e7-5c13-45b4-a365-6117602b1eac
Thesis: Trailing stop activated after profit milestone, then triggered on pullback from HWM.
Signals matched: Sell signal (2) — 10% trailing stop fired (HWM $216.73, stop $195.057).
Stop set: N/A (this is the exit).
Research reference: memory/research-log.md 2026-04-21 19:00 CT entry (original entry plan).
Notes: Reconstructed from Alpaca order history. Round-trip P/L: (195.0184 − 201.38) × 25 = −$159.04 (−3.16%). NVDA ran to ~$216.73 high-water mark before pulling back; trailing stop locked in the giveback. Net account impact reflected in current $99,840.95 cash.

