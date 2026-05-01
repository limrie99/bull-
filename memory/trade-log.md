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
Thesis: AI-infra leader with clean earnings runway (next print 2026-05-20 AMC, ~21 trading days out at entry); starter tranche per 4/21 pre-market plan.
Signals matched: (3) secular AI-infra tailwind (Blackwell ramp, cap-ex cycle).
Stop set: $187.12 (DAY stop, leg of OTO bracket — expired same day, replaced GTC at $187.28 later that day).
Research reference: 2026-04-21 19:00 CT pre-market re-run entry in research-log.md.
Notes: Filled as market order via OTO bracket. Day-only stop leg expired at 4 PM; GTC stop $187.28 placed separately at 15:24 CT same day. Position size ~5% of equity (starter tranche per plan, intended to add on confirmation).

## 2026-04-27 12:16 CT | STOP-ROTATION | NVDA | 25 sh | order_id d42471e7-5c13-45b4-a365-6117602b1eac
Thesis: NVDA crossed +5% in profit (HWM $216.73 = +7.6% from $201.38 entry); strategy says cancel hard stop and place 10% trailing.
Signals matched: Strategy risk-rule rotation (not a buy/sell signal).
Stop set: 10% trailing, current trigger $195.057 (HWM $216.73).
Research reference: rule-driven, no separate research entry.
Notes: Canceled prior GTC hard stop a3057559 ($187.28) at 12:16 CT and replaced with 10% trailing stop GTC. No share count change. Trailing has held through the 4/30 NVDA -4.7% reversal day; floor is $195.06.

---
