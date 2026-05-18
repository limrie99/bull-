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

## 2026-04-22 10:07 CT | BUY | NVDA | 25 @ 201.38 | 974cc142-ce34-4ed4-902d-58f04c9b58a3 (parent)
Thesis: AI-infra leader, Blackwell ramp into 5/20 earnings — starter tranche per 2026-04-21 19:00 CT pre-market plan.
Signals matched: (3) secular AI-infra tailwind
Stop set: $187.28 (-7% hard stop, bracket OTO)
Research reference: 2026-04-21 19:00 CT pre-market entry
Notes: Logged retroactively on 2026-05-18 market-open — original 4/22 + 4/27 routines never wrote to trade-log. Bracket OTO stop expired same day (DAY tif), was re-placed 4/27 as GTC stop, then replaced 5/4 by 10% trailing stop after position crossed +5%. Position size $5,034.50 (~5.0% of portfolio).

## 2026-05-04 10:21 CT | SELL | NVDA | 25 @ 195.0184 | d42471e7-5c13-45b4-a365-6117602b1eac
Thesis exit: 10% trailing stop triggered after NVDA rolled over from $216.73 high-water mark.
Signals matched: Sell signal (2) — 10% trailing stop fired after position had qualified above +5%.
Stop set: N/A (sell leg)
Research reference: 2026-04-21 19:00 CT pre-market entry
Notes: Logged retroactively on 2026-05-18 market-open. Net P/L = 25 × ($195.0184 − $201.38) = −$159.04 (−3.16% on the position, −0.16% on the portfolio). Trailing stop worked exactly as designed — locked in a modest loss after the position had been a ~+7.6% winner intraday. v2's first round-trip closed red. Lesson: starter tranche sized correctly (5%) kept the damage trivial.

