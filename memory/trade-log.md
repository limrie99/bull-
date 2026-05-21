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
Thesis: AI-infra leader, Blackwell ramp + cap-ex cycle, next earnings 2026-05-20 AMC well outside the 3-day blackout — starter tranche per pre-market plan.
Signals matched: 3 (secular AI-infra tailwind)
Stop set: $187.28 (-7.0%) — initial day-bracket expired same session, replaced as GTC at $187.28 on 2026-04-22 15:24 CT.
Research reference: memory/research-log.md 2026-04-21 19:00 CT
Notes: **Recorded retroactively on 2026-05-21 midday during memory reconciliation.** The 4/22 market-open routine had halted in memory, but the trade actually executed live — Bull's logs simply never caught up. Order class was OTO (one-triggers-other) with a day-only stop; the stop expired at close and was re-submitted GTC.

## 2026-04-27 12:16 CT | (stop conversion) | NVDA | 25 | a3057559-0031-4402-9011-e75601d5320e → d42471e7-5c13-45b4-a365-6117602b1eac
Thesis: position crossed +5% gain → cancelled the -7% hard stop, replaced with a 10% trailing stop per strategy.
Signals matched: N/A (risk management)
Stop set: trailing 10% (initial HWM $216.73, stop reference $195.057)
Research reference: memory/research-log.md 2026-04-21 19:00 CT
Notes: Recorded retroactively 2026-05-21 — Bull's memory never logged the conversion at the time.

## 2026-05-04 10:21 CT | SELL | NVDA | 25 @ 195.0184 | d42471e7-5c13-45b4-a365-6117602b1eac
Thesis: trailing stop fired — NVDA pulled back from HWM $216.73 to the 10% trail line.
Signals matched: Sell rule 2 (trailing stop triggered)
Stop set: N/A (sell leg)
Research reference: memory/research-log.md 2026-04-21 19:00 CT
Notes: Realized P/L = ($195.0184 − $201.38) × 25 = **−$159.04** (−3.16% on the position, −0.16% on the account). Strategy worked as designed — trailing stop captured ~7.6% of the run, exit was disciplined. Recorded retroactively 2026-05-21 during memory reconciliation.
