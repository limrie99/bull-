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

## 2026-04-22 08:30 CT | BUY | NVDA | 25 @ 201.38 | (reconciled from Alpaca FILL activity)
Thesis: AI-infra secular tailwind; NVDA next earnings 5/20; constructive open.
Signals matched: #3 (secular tailwind), #6 (uptrend). Conviction: medium, ~5% starter.
Stop set: $187.28 (-7% hard stop at entry)
Research reference: research-log 2026-04-21 pre-market
Notes: 3 fills (6 + 2 + 17 sh) all @ 201.38 = $5,034.50. On 4/27 the +6% gain converted the hard stop to a 10% trailing stop per strategy.

## 2026-05-04 ~time CT | SELL | NVDA | 25 @ ~195.02 | (reconciled from Alpaca FILL activity)
Thesis (exit): trailing stop fired — NVDA gave back its gain and round-tripped through entry.
Signals matched: sell signal #2 (10% trailing stop triggered).
Stop set: N/A
Research reference: midday 2026-05-04 ("NVDA trailing stop fired")
Notes: 3 fills (6 + 12 + 7 sh) @ 195.01–195.04 = $4,875.46. Realized P/L = **−$159.04 (−3.16%)**. This is the only completed trade of the Apr 22 – Jun 1 period; account held 100% cash afterward.

## 2026-06-01 10:46 CT | BUY | LLY | 14 @ 1078.46 | d79df0f3-584c-427c-aae5-bd0e7600df00
Thesis: Eli Lilly — Q1 beat with RAISED FY2026 guidance ($82–85B rev, $35.50–37.00 EPS) + FDA approval of Foundayo (orforglipron, oral GLP-1) = obesity-franchise expansion catalyst, riding the GLP-1 secular tailwind, in a clean steady uptrend (+15.8% above 50d MA, ~2% off highs).
Signals matched: #1 (earnings beat + raised guidance, 4/30), #2 (orforglipron approval → near-term launch catalyst), #3 (GLP-1/obesity secular tailwind), #6 (clear uptrend). High conviction.
Stop set: $1002.57 (-7.0% hard stop, OTO leg id 7748b65e-6096-46c1-bc9b-2bf75be40038)
Research reference: research-log 2026-06-01 market-open (fresh in-run thesis under cold-start rule)
Notes: Bracket rejected by paper API ("requires take_profit.limit_price"); used OTO class (market buy triggers single stop-loss leg) to honor the no-take-profit / let-winners-run rule. Filled 14 sh @ 1078.46 = $15,098.44 (15.1% of equity). Next earnings ~Aug 5 — no blackout.

## 2026-06-01 10:46 CT | BUY | NVDA | 55 @ 220.15 | 4fb46b0e-5964-4c24-8ecd-5b2fba2c5dc4
Thesis: NVIDIA — May 20 Q1 FY27 earnings beat (EPS $1.87 vs $1.76, record rev $81.6B), AI-infra secular tailwind intact, healthy non-extended uptrend (+5.9% above 50d MA, ~10% off highs). Re-entry post-earnings at a higher base than the early-May exit; thesis was never broken (prior exit was a trailing-stop pullback, not a thesis break).
Signals matched: #3 (AI-infra secular tailwind), #6 (clear uptrend), #1 (recent earnings beat, borderline-recent). Medium conviction.
Stop set: $204.74 (-7.0% hard stop, OTO leg id e2c1f2bb-9b38-4328-bddb-bb2939c380fd)
Research reference: research-log 2026-06-01 market-open
Notes: OTO class (same reason as LLY). Filled 55 sh @ 220.15 = $12,108.25 (12.1% of equity). Next earnings ~Aug 26 — no blackout. Not revenge: fresh post-print setup, sized as a starter.
