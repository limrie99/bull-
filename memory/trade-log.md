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

## 2026-06-05 13:52 CT (14:52 ET) | SELL (stop fired) | NVDA | 55 @ 204.7158 | b55fb743-57a8-48b1-8b53-221b358eb2ea
Action: The −7% hard stop on NVDA filled — NOT a manual sell. Resting GTC stop b55fb743 @ 204.74 triggered as the post-NFP tech/semis selloff deepened into the afternoon; filled 55 sh @ 204.715819 (slight slippage below the 204.74 trigger, normal for a stop-market).
Entry was 220.15 (6/1), so realized **−$848.88 (−7.01%)** — a controlled, pre-decided exit exactly at the −7% guardrail. Proceeds $11,259.37 → cash $59,658.21 → $70,917.58.
Signals matched (sell): #1 (−7% hard stop). Thesis was NOT broken — midday Perplexity check rated the drop sector/macro (NFP + rates), no company-specific thesis-breaker (no guidance cut, regulatory, customer loss, exec departure). The stop did its job: capped a macro-driven drawdown at −7% rather than letting it run.
Research reference: research-log 2026-06-05 midday (NVDA news check) + market-close Day summary.
Notes: 2nd NVDA round-trip of the v2 run (prior: −$159 on 5/4 trailing-stop pullback). Both exits were stop-driven, not thesis breaks. Book now 2 of 5 (LLY, DE); weekly buy cap still 3/3 used (resets Mon 6/8), so NO same-week re-entry — revisit NVDA as a fresh candidate Monday if the tape stabilizes. daytrade_count still 0 (entry was 6/1, not a day trade).

## 2026-06-08 08:36 CT | BUY | GE | 45 @ 329.63 | fcbc7204-8982-408d-8c6f-d37dd4187dea
Thesis: GE Aerospace — aerospace/defense industrial; record commercial-aircraft demand + high-margin engine-service (aftermarket) backlog; pure industrial with ZERO AI/semis overlap (lowers book beta after Friday's NVDA stop-out). Lead diversifier in the sector rotation INTO industrials. Deployed on a green, stabilizing tape (SPY +0.6%, Friday's bounce holding) — not catching a knife.
Signals matched: #3 (aerospace aftermarket + defense secular tailwind), #5 (industrials rotation, confirmed), #6 (clear uptrend, "Strong Buy", PT ~$348–350, not at lows). High conviction.
Stop set: $306.56 (-7.0% from fill; provisional OTO day-stop @ 308.47 cancelled post-fill and re-placed as standalone GTC stop ec3f8a10-6e1d-4bf4-8ffb-523dc8d95ae9).
Research reference: research-log 2026-06-08 pre-market (GE = LEAD candidate) + this market-open re-validation.
Notes: OTO market buy filled cleanly 45 sh @ 329.63 = $14,833.35 (~14.8% of equity — full size per high-conviction sizing). Next earnings ~late July — no blackout. 1st of up to 3 weekly buys (cap reset Mon 6/8). Cancelled inherited day-TIF stop leg, re-placed identical −7% stop as GTC so protection persists overnight (verified 6/1–6/4 workflow).

## 2026-06-08 08:38 CT | BUY | ETN | 24 @ 401.5425 | b9bba8a2-a029-4377-a6a0-5854ec749c70
Thesis: Eaton — electrical-equipment "picks-and-shovels" for AI data-center power & broad electrification (electrical-segment orders +55% / rev +50%). Re-adds AI exposure to the book WITHOUT owning a semiconductor (the group being sold). Sized as a smaller starter per the high-beta entry-discipline learning; entered on stabilization (mark ~$402, recovered above Friday's ~$396 flush) rather than chasing a gap-down.
Signals matched: #1 (Q1 2026 beat + raised FY guidance), #3 (AI data-center power + electrification secular), #5 (industrial rotation). Med-high conviction.
Stop set: $373.43 (-7.0% from fill; provisional OTO day-stop @ 373.91 cancelled post-fill and re-placed as standalone GTC stop db3865d5-c24f-40ca-a236-6c0f0c2672f0).
Research reference: research-log 2026-06-08 pre-market (ETN = #2 candidate) + this market-open re-validation.
Notes: OTO market buy filled in many fragments over ~3 min (thin paper liquidity, very wide simulated quote bid 382 / ask 425) — 1→6→19→20→22→23→24, final avg 401.5425 = $9,637.02 (~9.6% of equity, deliberately ≤10% per high-beta starter rule). Next earnings ~late July — no blackout. 2nd of 3 weekly buys. Cancelled inherited day-TIF stop leg, re-placed identical −7% stop as GTC.

## 2026-06-15 08:37 CT | RISK-MGMT (no fill) | GE | converted −7% hard stop → 10% trailing stop | b9dadf2d-b6f5-49e7-8cc9-b3eb8b07aa6c
Action: GE crossed +5% profit at the open (mark ~346.3–346.6 vs entry 329.63 = +5.1%), the +5% conversion threshold, so per strategy I cancelled the −7% GTC hard stop and replaced it with a 10% trailing GTC stop.
- Cancelled hard stop ec3f8a10-6e1d-4bf4-8ffb-523dc8d95ae9 (was @ 306.56) — HTTP 204, confirmed zero open GE orders before re-placing.
- Placed trailing_stop sell, qty 45, trail_percent 10, GTC → id b9dadf2d-b6f5-49e7-8cc9-b3eb8b07aa6c. Initial stop_price 311.976, hwm 346.64 (ratcheted to ~312.09 as GE ticked higher). Confirmed resting (status new).
Signals matched: sell-signal #2 mechanics (10% trailing stop activated at +5% profit). No shares traded.
Stop set: GE 10% trailing GTC (floor ~312.09 at placement; ratchets up as GE rises).
Research reference: research-log 2026-06-15 pre-market (standing conversion task: "if GE ≥ ~346.11, convert") + this market-open execution.
Notes: Floor 312.09 is below entry 329.63 so it doesn't yet lock in a profit, but it's ~$5.5 above the old hard stop and will climb with the price. GE is the book's strongest new entry (+5.13%). No buys/sells this routine — JPM reserve buy deferred to post-FOMC (Wed 6/17 rate decision) per pre-market plan; today's +1.5% tape is a day-one geopolitical (Iran de-escalation) gap, escape-hatch "durable tape + Fed priced" conditions not met. daytrade_count 0.

## 2026-06-18 12:05 CT | RISK-MGMT (no fill) | ETN | converted −7% hard stop → 10% trailing stop | cc843666-7e63-462a-82d4-57cc3e826ead
Action: ETN crossed +5% profit at midday (mark 423.79 vs entry 401.5425 = +5.54%, above the ~421.62 +5% trigger that it sat ~$0.25 short of at the open), so per strategy I cancelled the −7% GTC hard stop and replaced it with a 10% trailing GTC stop.
- Cancelled hard stop db3865d5-c24f-40ca-a236-6c0f0c2672f0 (was @ 373.43) — HTTP 204, confirmed zero open ETN orders before re-placing.
- Placed trailing_stop sell, qty 24, trail_percent 10, GTC → id cc843666-7e63-462a-82d4-57cc3e826ead. stop_price 381.555, hwm 423.95. Confirmed resting (status new), HTTP 200.
Signals matched: sell-signal #2 mechanics (10% trailing stop activated at +5% profit). No shares traded.
Stop set: ETN 10% trailing GTC (floor 381.555 at placement, hwm 423.95; ratchets up as ETN rises).
Research reference: portfolio.md standing task ("the moment ETN tags +5% ~421.62, cancel db3865d5 → place a 10% trailing GTC") + this midday execution.
Notes: New floor 381.555 is ~$8 above the old hard stop 373.43 — locks in more of the run, though still below entry 401.54 so not yet a guaranteed profit. ETN is now the 3rd of 4 names on a trailing stop (GE, LLY, ETN); only DE (+0.19%) remains on a −7% hard stop. No buys/sells this routine. daytrade_count 0.

## 2026-06-25 12:05 CT | RISK-MGMT (no fill) | DE | converted −7% hard stop → 10% trailing stop | dcdd84e5-6b94-4943-aa5b-3d3a299cbfce
Action: DE crossed +5% profit by midday (mark 621.12 vs entry 589.82 = +5.31%, clearing the ~619.31 +5% trigger it sat ~1.66% short of at the open), so per strategy I cancelled the −7% GTC hard stop and replaced it with a 10% trailing GTC stop. This was the #1 flagged near-term action from the open routine.
- Cancelled hard stop a150583a-a58c-42c9-8d12-9d7ece773841 (was @ 548.53) — HTTP 204, confirmed DE qty_available freed to 22 before re-placing.
- Placed trailing_stop sell, qty 22, trail_percent 10, GTC → id dcdd84e5-6b94-4943-aa5b-3d3a299cbfce. stop_price 558.945, hwm 621.05. Confirmed resting (status new).
Signals matched: sell-signal #2 mechanics (10% trailing stop activated at +5% profit). No shares traded.
Stop set: DE 10% trailing GTC (floor 558.945 at placement, hwm 621.05; ratchets up as DE rises).
Research reference: portfolio.md standing task ("convert the moment DE tags ~619.31") + this midday execution.
Notes: New floor 558.945 is ~$10.4 above the old hard stop 548.53 and locks in essentially break-even-plus protection (entry 589.82). DE was the LAST name on a hard stop — **with this conversion all 4 positions (GE, LLY, ETN, DE) are now on 10% trailing stops, zero hard stops in the book.** No buys/sells this routine; nothing on the watchlist clears 2 signals + Conviction ≥70 (PANW 66, JPM 65). daytrade_count 0.

## 2026-06-29 08:38 CT (09:38 ET) | BUY | JPM | 34 @ 329.695588 | 701356fd-d56a-48c1-a2c2-1b57ed8dcce3
Thesis: JPMorgan — post-CCAR capital return: new $50B buyback (eff. Jul 1) + dividend hike $1.50→$1.65/qtr (+10%); largest US bank, near 52-wk high, uptrend intact. First name to clear the gate (2+ signals AND Conviction ≥70) in weeks; fills the cash-drag the weekly review flagged.
Signals matched: (2) catalyst ≤30d ($50B buyback live Jul 1 + div hike), (3) financials-sector tailwind post-CCAR capital-return clearance, (4) capital-return = upgrade-equivalent (counted cautiously, not a formal analyst upgrade), (6) clear uptrend near ATH, not at lows. 4 of 6 signals. Conviction ~74 (Grade B+).
Stop set: $306.62 (-7.0% from fill 329.695588; provisional OTO day-stop @ 306.81 cancelled post-fill [HTTP 204, confirmed zero open JPM orders] and re-placed as standalone GTC stop 3e8fe4ea-d95c-4e6c-82e1-ff66f0d56670, status new).
Research reference: research-log 2026-06-29 pre-market (JPM = LEAD, teed up as STARTER buy) + this market-open re-validation (sub-agent re-confirmed buyback/div STILL LIVE, no weekend walk-back, no negative 72h news).
Notes: OTO market buy filled in fragments (thin paper liquidity) — partials 31 @ 329.70 → final 34 @ 329.695588 = $11,209.65 (~10.8% of equity). Sized as a conservative STARTER (~10-12%, not full Grade-B+ 15%) because Q2 earnings CONFIRMED Tue Jul 14 is a binary print ~11 trading days out. JPM is a financial, NOT high-beta AI/semis → the ≤10% beta-override does not apply; the Jul 14 print is what argues for starter size. 1st of 3 weekly buys (cap reset Mon 6/29). Fills the 5th/last position slot — book now AT the 5-position cap. daytrade_count 0.

## 2026-07-02 13:36 CT (14:36 ET) | SELL (auto — trailing stop fired) | ETN | 24 @ 392.75 | cc843666-7e63-462a-82d4-57cc3e826ead
Action: ETN's 10% trailing stop (order `cc843666`) auto-fired and SOLD all 24 shares at 392.75. This was NOT a discretionary sell — the position had been sitting right on its trailing floor (393.066) at midday (~0.18% cushion); a small further slip in the afternoon tagged the stop and it executed. Filled 2026-07-02T17:36:01Z. Position CLOSED. Confirmed zero open ETN orders and ETN absent from positions afterward.
Realized P/L: (392.75 − 401.5425) × 24 = **−$211.02 (−2.19%)** from entry 401.5425 (bought 2026-06-08).
Signals matched: sell-signal #2 mechanics (10% trailing stop). This is the SYSTEM working as designed on the book's highest-beta name — not a thesis break. AI-power/data-center thesis was intact; beta shook it out on a soft, thin pre-holiday tape.
Stop set: none (position closed). Freed ~$9,426 cash.
Research reference: 7/2 midday research-log flagged ETN "sitting ON its 393.066 trailing floor (~0.18% cushion) — a small further slip auto-fires the stop. By design; no pre-emptive action."
Notes: Book now **4 of 5 positions** (GE, LLY, DE, JPM). Cash → $44,663.52 (~43.1%). Weekly buys still 1 of 3 (a stop-out is not a buy). Realized YTD stop-outs now: NVDA ×2 (−$159, −$849), ETN (−$211). daytrade_count 0. Redeploying the freed cash is the priority for Mon 7/6 pre-market (market CLOSED Fri 7/3).
