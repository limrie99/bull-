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

## 2026-05-04 10:21 CT | SELL | NVDA | 25 @ $195.0184 | d42471e7-5c13-45b4-a365-6117602b1eac
Thesis: trailing-stop exit on the NVDA AI-infra starter (held 8 trading days).
Signals matched: Sell signal #2 — 10% trailing stop activated after the position went +5% in profit; fired when price fell 10% off the high-water mark of $216.73.
Stop set: N/A (this is the sell leg).
Research reference: see research-log 2026-05-25 12:00 CT (backfill reconciliation entry); original buy thesis in 2026-04-21 19:00 CT pre-market.
Notes: BACKFILLED on 2026-05-25 from the Alpaca order record (status=filled, hwm=$216.73, trail_percent=10). The trade was placed and managed automatically by prior routines but never logged here; reconstructed from the broker side. Net round-trip P/L: −$159.04 (−3.16%), the only reason cash differs from the $100K seed.

## 2026-04-22 09:07 CT | BUY | NVDA | 25 @ $201.38 | 2b923034-96f2-4166-8d53-10b5b9a967b8
Thesis: ~5% starter tranche in the AI-infra leader heading into the 5/20 earnings runway (Blackwell ramp, cap-ex cycle tailwind).
Signals matched: (3) secular AI-infra tailwind — single verified signal, conviction medium. Sized small as a starter accordingly.
Stop set: $187.12 (-7% bracket leg, day TIF — expired same day, replaced 4/23 with GTC stop at $187.28, later canceled and converted to a 10% trailing stop on 4/27 once the position went +5%).
Research reference: research-log 2026-04-21 19:00 CT pre-market re-run.
Notes: BACKFILLED on 2026-05-25 from the Alpaca order record. OTO bracket-style entry: market buy + day stop leg. The day-stop leg expired without a fill on 4/22 close; a fresh GTC -7% stop was placed 4/23 and lived until 4/27 when it was canceled and replaced with the 10% trailing stop per strategy.
