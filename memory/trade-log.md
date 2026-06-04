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

## 2026-06-01 12:00 CT | RISK-MGMT (no fill) | LLY + NVDA | re-issued hard stops as GTC
Action: Cancelled the two day-TIF stop legs created by this morning's OTO entries (which would have expired at today's 16:00 ET close, leaving both positions unprotected overnight) and re-placed identical −7% hard stops as GTC.
- LLY: cancelled 7748b65e → new GTC stop 6c4d0225-ae01-42a9-95a6-af790a87d286 @ 1002.57
- NVDA: cancelled e2c1f2bb → new GTC stop b55fb743-57a8-48b1-8b53-221b358eb2ea @ 204.74
Signals matched: N/A (risk-rule maintenance — honoring the −7% hard-stop guardrail's intent that protection persist, not vanish at close).
Stop set: LLY 1002.57 GTC, NVDA 204.74 GTC (both unchanged price, only TIF changed day→gtc).
Research reference: research-log 2026-06-01 midday
Notes: No shares traded. Root cause: OTO stop legs inherit the parent buy's time_in_force (day). For protective stops we want GTC. Going forward, entries should place GTC stops or this conversion must happen same-day. Neither position was at −7% (LLY −0.33%) or +5% (NVDA +0.82%), so no other stop action.

## 2026-06-04 08:35 CT | BUY | DE | 22 @ 589.82 | d8eaf151-071b-40f3-b666-2edeb3f190a9
Thesis: Deere — Q2 beat (5/21: EPS $6.55 vs $5.76, rev $13.37B vs $11.48B est) + accelerating clean uptrend + ag-equipment/onshoring secular tailwind = a high-conviction NON-AI industrial diversifier for an AI-heavy book (NVDA). 3rd/final weekly buy, deployed on a settle (DE flat ~589.7 at the open vs 588.61 prior close, not chasing the 3-day spike).
Signals matched: #1 (earnings beat & raised production), #3 (ag/onshoring secular tailwind), #6 (clear, strong uptrend). High conviction; sized conservatively (~13%) for the steep recent run + NFP-Friday event risk.
Stop set: $548.53 (-7.0% from fill; placed as standalone GTC stop a150583a-a58c-42c9-8d12-9d7ece773841 after cancelling the day-TIF OTO leg 1c404b6b)
Research reference: research-log 2026-06-04 pre-market (DE = lead candidate) + this market-open re-validation
Notes: OTO market buy + day stop; filled in fragments (thin paper liquidity, wide quote) — partials 20→21→22, final avg 589.82 = $12,976.04 (~13.0% of equity). Cancelled the inherited day-TIF stop leg and re-placed an identical −7% stop as GTC so protection persists overnight (same fix as the 6/1 OTO entries). 3 of 5 slots, 3 of 3 weekly buys used.

## 2026-06-04 12:02 CT | RISK-MGMT (no fill) | LLY | converted −7% hard stop → 10% trailing stop | 6016a7e7-faac-4e93-82e7-851abf30eca8
Action: LLY hit +5.13% (mark 1133.825 vs entry 1078.46), crossing the +5% profit threshold, so per strategy I cancelled the −7% GTC hard stop and replaced it with a 10% trailing GTC stop.
- Cancelled hard stop 6c4d0225-ae01-42a9-95a6-af790a87d286 (was @ 1002.57) — HTTP 204, confirmed no open LLY orders.
- Placed trailing_stop sell, qty 14, trail_percent 10, GTC → id 6016a7e7-faac-4e93-82e7-851abf30eca8. Initial stop_price 1019.70, hwm 1133. Confirmed resting (status new).
Signals matched: sell-signal #2 mechanics (10% trailing stop activated at +5% profit). No shares traded.
Stop set: LLY 10% trailing GTC (floor 1019.70 at placement; ratchets up as LLY rises).
Research reference: research-log 2026-06-04 midday.
Notes: Trailing floor 1019.70 is below entry 1078.46, so it doesn't yet lock in a profit — but it's ~$17 higher than the old hard stop (1002.57) and will climb with the price. NVDA (−0.69%) and DE (+0.03%) unchanged — neither at +5% or −7%, no action.
