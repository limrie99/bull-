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
Thesis: Starter tranche on AI-infra leader with confirmed earnings runway (next print 5/20, 21 trading days out at entry). Played as ~5% of portfolio per pre-market scout plan.
Signals matched: (3) secular AI-infra tailwind (Blackwell ramp, hyperscaler cap-ex cycle).
Stop set: $187.28 (-7% hard stop, GTC replacement after the bracket day-stop expired same day).
Research reference: research-log 2026-04-21 19:00 CT pre-market re-run.
Notes: Bracket OTO market-order filled clean, but the attached stop was placed `time_in_force: day` and expired with the close. Stop was re-placed GTC the next morning (4/23) — process gap to fix in the buy template (always GTC the protective stop).

## 2026-04-27 12:16 CT | STOP-CONVERT | NVDA | 25 shares | order_id d42471e7-5c13-45b4-a365-6117602b1eac
Thesis: Position crossed +5% in profit (HWM tracking near $216 area), strategy says cancel the -7% hard stop and replace with a 10% trailing stop.
Signals matched: Strategy rule (trailing-stop activation at +5%).
Stop set: trailing_stop, trail_percent 10, GTC.
Research reference: strategy.md risk rules.
Notes: Old GTC stop @ $187.28 cancelled cleanly before placing the trailing.

## 2026-05-04 10:21 CT | SELL | NVDA | 25 @ $195.0184 (avg) | order_id d42471e7-5c13-45b4-a365-6117602b1eac
Thesis: 10% trailing stop fired automatically. HWM $216.73 → stop trigger $195.057 → filled $195.0184 across three partials.
Signals matched: Sell signal (2) — trailing stop, working as designed.
Stop set: N/A (closed position).
Research reference: research-log 2026-05-04 12:00 CT midday.
Notes: Held 12 calendar days. Realized P/L -$159.04 (-3.16%). Position peaked at +7.6% intraday on 4/27 before fading on pre-earnings de-risking (5/20 print) and hyperscaler ASIC competition headlines. Thesis not broken — exit was mechanical risk discipline, not a thesis sell.
