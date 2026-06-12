# Portfolio

**Last updated:** 2026-06-12 12:05 CT (MIDDAY routine, market confirmed open via clock, marks = live Alpaca intraday ~13:05 ET).
**Cash:** $46,447.18 (unchanged — no trades at midday)
**Total equity:** $99,648.29 (live intraday). Prior-day baseline (6/11 close, Alpaca last_equity) $99,632.12.
**Day P/L (intraday):** **+$16.17 / +0.016%.** Essentially flat — GE and LLY green, DE/ETN modestly red. (Authoritative day-vs-SPY is computed at the close.)
**Day vs SPY (intraday, NOT authoritative):** SPY 737.67 (6/11 close) → 741.90 (live ~13:05 ET) = +0.573% → intraday alpha ~−0.56pts (we lag on an up-day because ~47% is in cash that earns nothing rising — same trade-off that cushions down-days). Close routine owns the official figure.
**This week (started Mon 6/8, baseline $99,507.02 = 6/5 close):** Day 5 of 5 (Friday = weekly review + week close later today). WTD intraday +0.142% vs SPY +0.603% (intraday, NOT authoritative — close/weekly-review owns it). Buys used: **2 of 3** (GE + ETN on 6/8); 1 buy in reserve (expires today, resets Mon 6/15). Today's weekly-review routine decides whether to deploy the reserve buy.

## Open positions (4 of 5)

| Symbol | Shares | Avg Cost | Mark (live ~13:05 ET) | P/L $ | P/L % | Stop | +5% trail trigger | Entry Date | Thesis (1 line) |
|---|---|---|---|---|---|---|---|---|---|
| LLY | 14 | 1078.46 | 1144.25 | +921.06 | +6.10% | **10% TRAILING (GTC)**, stop 1064.457, hwm 1182.73 | converted ✅ | 2026-06-01 | Q1 beat + raised FY guidance + oral GLP-1 (orforglipron/Foundayo) approval; GLP-1 tailwind; clean uptrend. Defensive anchor — +6.10%, the book's hero. Trailing floor 1064.457 (~6.97% below mark; mark 1144.25 < hwm 1182.73, floor held — no new high to ratchet). |
| GE | 45 | 329.63 | 335.43 | +261.00 | +1.76% | 306.56 (−7%, **GTC**) | ~346.11 | 2026-06-08 | GE Aerospace — record commercial-aircraft demand + high-margin engine aftermarket + defense; pure industrial, zero AI overlap, lower beta. Green +1.76%, ~8.61% above stop. Thesis intact. No blackout (~late July earnings). |
| DE | 22 | 589.82 | 576.93 | −283.58 | −2.19% | 548.53 (−7%, **GTC**) | ~619.31 | 2026-06-04 | Q2 beat (5/21: EPS $6.55 vs $5.76, rev $13.37B vs $11.48B); ag-equipment/onshoring tailwind; NON-AI diversifier. −2.19% (~4.92% above stop), improved from −3.17% at the open. No Deere-specific catalyst; weakness was sector/macro. Thesis intact; HOLD. |
| ETN | 24 | 401.5425 | 391.45 | −242.22 | −2.51% | 373.43 (−7%, **GTC**) | ~421.62 | 2026-06-08 | Eaton — electrical "picks-and-shovels" for AI data-center power + electrification (orders +55%/rev +50%). Q1 beat + raised guide. 6/10 spinoff of slower-growth vehicle unit (Reverse Morris Trust w/ Dana) sharpens electrical/data-center focus — strengthens thesis. Gave back the open's gains (was −1.00%), now the thinnest cushion ~4.6% above its −7% stop. Thesis intact; HOLD. No blackout (~late July). |

**Open positions: 4 of 5.** **Buys used this week: 2 of 3** (GE + ETN on 6/8; cap resets Mon 6/15) — **1 buy in reserve (expires today).** **Cash buffer: ~46.6%** (~53.4% invested, $53,201.11 market value).

## Today's trades

- **No trades at midday.** Cash unchanged $46,447.18. No orders placed, cancelled, or converted. daytrade_count 0. Held all 4: no −7% breach (worst ETN −2.51%), no new +5% conversions pending (only LLY ≥+5%, already trailing; mark 1144.25 < hwm 1182.73 so no new high to ratchet), day +0.016% (loss cap moot), no high-conviction breaking catalyst to justify a midday deviation. The reserve-buy / JPM decision belongs to today's weekly-review routine, not midday.

## Stop-management state (all 4 confirmed RESTING as GTC, status `new` — verified live at midday via open-orders query)

- **LLY 10% trailing** `6016a7e7-faac-4e93-82e7-851abf30eca8` — stop_price **1064.457**, trail 10%, hwm **1182.73** (mark 1144.25 < hwm, floor held). Floor ~6.97% below mark — no near-term stop risk.
- **ETN −7% hard** `db3865d5-c24f-40ca-a236-6c0f0c2672f0` @ **373.43** (mark 391.45, ~4.6% cushion — thinnest in the book).
- **DE −7% hard** `a150583a-a58c-42c9-8d12-9d7ece773841` @ **548.53** (mark 576.93, ~4.92% cushion).
- **GE −7% hard** `ec3f8a10-6e1d-4bf4-8ffb-523dc8d95ae9` @ **306.56** (mark 335.43, ~8.61% cushion).
- (a) **−7% drawdown check:** worst is ETN −2.51% (not at −7%). HOLD. No sells. No Perplexity news check required (nothing at/below −7%).
- (b) **+5% → trailing stop:** LLY converted ✅ (no new high at midday, floor held). **Standing tasks:** if DE ≥ +5% (~619.31), GE ≥ +5% (~346.11), or ETN ≥ +5% (~421.62), cancel that name's −7% hard stop → 10% trailing GTC. None near (GE closest at +1.76%).
- (c) **Daily loss cap:** day +0.016% (flat/up). Not in play.
- daytrade_count 0.

## Watch

- **Quiet, flat midday** — SPY +0.57% on the day, our book +0.016%, so we lag intraday on an up-day (~47% cash earns nothing rising; that same cash cushions down-days). Nothing tripped a rule; held all 4.
- **ETN** is now the thinnest cushion (−2.51%, ~4.6% above 373.43 stop) — gave back the open's modest gain. No Eaton-specific thesis-breaker; spinoff news remains a positive. Hold; let the −7% stop work if it rolls over (would be macro, not thesis).
- **DE** improved to −2.19% (~4.92% cushion), up from −3.17% at the open. No company-specific catalyst; weakness is sector/macro.
- **LLY** remains the anchor — +6.10%, trailing floor 1064.457.
- **3rd buy slot in reserve, expires today.** Lead watch idea is **JPM** (financials — fills a sector gap, uptrend + rate tailwind, July-14 earnings outside blackout) with 2 signals (one hard #6 uptrend, one thematic #5 rotation). The reserve deploy requires a verified 2-signal setup AND a confirmed-constructive tape — that decision belongs to today's weekly-review routine.
- **Today (Fri 6/12):** weekly review + week close next. Compute full-week alpha vs SPY, run the sub-agent research team for next week's candidates, decide on the reserve buy before it resets Mon 6/15.

## Recent closes (last 5)

| Symbol | Exit Date | Shares | Entry | Exit | P/L $ | P/L % | Reason |
|---|---|---|---|---|---|---|---|
| NVDA | 2026-06-05 | 55 | 220.15 | 204.7158 | −848.88 | −7.01% | −7% hard stop fired (macro/NFP semis selloff, not thesis break) |
| NVDA | 2026-05-04 | 25 | 201.38 | ~195.02 | −159.04 | −3.16% | 10% trailing stop fired (round-trip) |

---
*Overwrite this file every routine. Keep it a live snapshot, not a log.*
