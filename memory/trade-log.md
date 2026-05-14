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
Thesis: AI-infra leader with verified secular tailwind (Blackwell ramp) and clear earnings runway (next print 5/20, outside 3-day blackout) — starter tranche per pre-market plan.
Signals matched: [3] secular AI-infra tailwind (verified)
Stop set: $187.28 (hard stop, −7% from $201.38 — placed as separate OTO stop order)
Research reference: research-log 2026-04-21 19:00 CT pre-market re-run
Notes: Backfilled from Alpaca records on 2026-05-14 — original routine that placed this order did not log to trade-log before the env-var halts began. Fills: 17 @ 201.38, 2 @ 201.38, 6 @ 201.38 (single fill price). $5,034.50 total. Initial bracket-style stop expired 4/22; replaced 4/23 with a GTC stop at $187.28.

## 2026-05-04 10:21 CT | SELL | NVDA | 25 @ $195.02 avg | order_id d42471e7-5c13-45b4-a365-6117602b1eac
Thesis: Position previously crossed +5% profit threshold and the GTC stop was upgraded to a 10% trailing stop (per strategy). Trailing stop tracked the rally to a high-water of $216.73 (~+7.6% above entry), then pulled back >10% and the stop fired automatically.
Signals matched: Sell signal [2] — 10% trailing stop triggered.
Stop set: N/A (closed position)
Research reference: no live research-log entry — routines halted from 2026-04-22 midday through early May. Backfilled 2026-05-14 from Alpaca order/activity records.
Notes: Fills: 7 @ 195.04, 12 @ 195.01, 6 @ 195.01 → $4,875.46 proceeds. Net loss vs $5,034.50 cost basis = −$159.04 (−3.16% on position, −0.16% on portfolio). High-water was $216.73 so the trailing stop captured most of the run-up before the pullback. Lesson: stop-management worked exactly as the playbook intended — but Bull was offline (halted routines), so this happened without any supervisory check on whether the thesis had actually broken. Reconcile the routine-uptime gap before the next live entry.
