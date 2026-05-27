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

> Note: the two entries below were **reconstructed on 2026-05-27** from the Alpaca order history. The original 4/22 and 5/4 routines did not write them to this log (4/22 routines had halted on missing keys, and nothing ran between then and 5/27). Numbers confirmed via the `/v2/orders` API — not fabricated.

## 2026-04-22 10:07 CT | BUY | NVDA | 25 @ $201.38 | 2b923034-96f2-4166-8d53-10b5b9a967b8
Thesis: AI-infrastructure leader with a clean earnings runway (next print 5/20) and the Blackwell/cap-ex tailwind intact — ~5% starter tranche.
Signals matched: (3) secular AI-infra tailwind. (Med conviction — single verified signal; sized as a starter, not full conviction.)
Stop set: −7% hard stop @ ~$187 (day OTO stop expired same session; re-placed as a GTC stop @ $187.28 on 4/23).
Research reference: research-log 2026-04-21 19:00 CT pre-market scout.
Notes: OTO market buy. Day stop leg expired at 4/22 close; hard stop re-established 4/23 morning.

## 2026-05-04 10:21 CT | SELL | NVDA | 25 @ $195.0184 | d42471e7-5c13-45b4-a365-6117602b1eac
Thesis: Exit — risk rule, not a discretionary sell.
Signals matched: Sell signal #2 (10% trailing stop). Hard stop had been swapped for a 10% trailing stop on 4/27; NVDA peaked at HWM $216.73 then gave back 10%, triggering the fill @ $195.0184.
Stop set: N/A (this is the stop firing).
Research reference: research-log 2026-04-21 19:00 CT (entry thesis); reconstructed 2026-05-27.
Notes: Realized −$159.04 (−3.16%). Peak gain was only +7.6% over entry, so a 10% trail unavoidably closed below cost. Trail worked as designed; entry was just close to the top.
