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
Thesis: trailing-stop exit — HWM was $216.73, trail 10% = stop ~$195.06.
Signals matched: sell signal #2 (10% trailing stop after the position cleared +5%).
Stop set: N/A (this IS the stop fill).
Research reference: see 2026-04-21 19:00 CT pre-market for original entry thesis.
Notes: **Backfilled at 2026-05-12 midday.** Bull was halted (no env vars) from 4/22 12:00 CT through last week, so this fill was not logged in-session. Per Alpaca API: trailing_stop GTC, filled 2026-05-04 15:21 UTC. P/L: 25 × (195.0184 − 201.38) = **−$159.04 (−3.16%)** vs entry. NVDA had run up to ~$216.73 HWM, so we left a paper gain on the table when the trail tightened and got hit on the pullback — first lesson: 10% trail is wide but still bites a volatile mega-cap on a routine drawdown. Not a thesis break.

## 2026-04-22 10:07 CT | BUY | NVDA | 25 @ $201.38 | 2b923034-96f2-4166-8d53-10b5b9a967b8
Thesis: AI-infra leader, clean ~21-day runway to 5/20 AMC earnings, ride the Blackwell ramp.
Signals matched: (3) secular AI-infra tailwind. Single verified signal — entry sized as a starter (1/3 of target), conviction med.
Stop set: $187.12 hard stop (−7%) via OTO bracket — but TIF=day, so it expired same session (caught at 4/27 follow-up, replaced with GTC stop at $187.28).
Research reference: 2026-04-21 19:00 CT pre-market re-run.
Notes: **Backfilled at 2026-05-12 midday.** Stop-TIF bug: the bracket leg was placed `time_in_force: day` and expired at the 4/22 close, leaving the position un-stopped overnight. Replaced 4/27 with a GTC stop, then cancelled and replaced with a 10% trailing stop once position crossed +5%. **Lesson: bracket stop legs must be GTC, not day.** Position was ~5% of equity ($5,034.50 cost), within plan.
