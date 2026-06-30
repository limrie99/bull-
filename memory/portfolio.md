# Portfolio

**Last updated:** 2026-06-30 ~15:05 CT (16:04 ET) — **MARKET-CLOSE routine. Market CLOSED** (`is_open:false`, next_open 7/1 09:30 ET). **No trades today** (at the 5-position cap; nothing cleared the buy-gate; no sells — all theses intact, none near a stop). All 5 stops re-confirmed RESTING `status:new`, IDs unchanged. 4 of 5 on 10% trailing, JPM on its −7% hard stop. **DE trailing floor ratcheted UP intraday 571.023 → 572.661** (hwm 636.29) — the only floor that moved today. **Book AT the 5-position cap (5 of 5). Weekly buys 1 of 3.** daytrade_count 0. **Inbox: nothing pending.** **JPM still on its −7% hard stop** (−0.75%, below entry) — no +5% conversion due.

**Cash:** $35,237.52 (~33.8%).
**Equity (official close):** **$104,124.68** (cash $35,237.52 + long_market_value $68,887.16). last_equity **$104,056.85** = Alpaca's official 6/29 close (today's base).
**Day P/L:** **+$67.83 / +0.07%** vs the 6/29 base — a hair green on a flat-to-mixed book day.
**SPY day (official):** 6/29 close 740.86 → 6/30 close 746.65 = **+0.78%**. **Day alpha −0.72 pts BEHIND** — the cash-drag + lower-beta flip-side on a strong-green SPY day (~34% cash and a defensive book lag when the index runs; the same mix cushions the down-days).
**Week-to-date (through 6/30 close, day 2 of a 4-day week; base = 6/26 close):** P/L **+0.97%**, SPY **+2.37%**, **alpha WTD −1.40%**. SPY has had two strong up-days to open the week; we're lagging on beta/cash as expected — the alpha gap is the thing to watch, not panic over.

## Open positions (5 of 5 — AT CAP) — official 6/30 close marks

| Symbol | Shares | Avg Cost | Close | P/L $ | P/L % | Day % | Stop | Entry Date | Thesis (1 line) |
|---|---|---|---|---|---|---|---|---|---|
| GE | 45 | 329.63 | 373.00 | +1,951.65 | +13.16% | −0.19% | **10% TRAILING (GTC)**, floor 341.703 (hwm 379.67) | 2026-06-08 | GE Aerospace — record commercial-aircraft demand + high-margin engine aftermarket + defense; pure industrial, ZERO AI overlap, lower beta. Book's anchor. Earnings ~Jul 16 (UNVERIFIED). Thesis INTACT. |
| LLY | 14 | 1078.46 | 1199.61 | +1,696.10 | +11.23% | −2.47% | **10% TRAILING (GTC)**, floor **1114.2** (hwm 1238; floor locks a profit) | 2026-06-01 | Eli Lilly — Q1 beat + raised guide + oral GLP-1 (orforglipron/Foundayo); late-stage weight-loss trial WIN 6/24. Today's −2.47% the day's biggest drag (healthcare lagging the rotation). **DATA FLAG: CMS Medicare GLP-1 $50/mo demo date UNVERIFIED (2026 vs 2027) — re-verify.** Core franchise thesis INTACT. |
| DE | 22 | 589.82 | 634.33 | +979.22 | +7.55% | +1.23% | **10% TRAILING (GTC)**, floor **572.661** (ratcheted up from 571.023; hwm 636.29) | 2026-06-04 | Deere — RE-RATED UP this week. VERIFIED big Q2 beat (EPS $6.55 vs $5.70, rev $13.37B vs $11.55B), FY26 guide raised/maintained, JPM PT $560→$590 (6/4), Buy consensus 0 Sells. INTACT — not the swap target. |
| ETN | 24 | 401.5425 | 426.12 | +589.86 | +6.12% | +4.38% | **10% TRAILING (GTC)**, floor 393.066 (hwm 436.74) | 2026-06-08 | Eaton — electrical "picks-and-shovels" for AI data-center power + electrification. Highest-beta name, **today's best mover (+4.38%, +$429)**. No ETN-specific news, no downgrade. Earnings ~late July (UNVERIFIED). Thesis INTACT — watch beta. |
| JPM | 34 | 329.695588 | 327.22 | −84.17 | −0.75% | −0.66% | **−7% HARD STOP (GTC)** @ **306.62** | 2026-06-29 | JPMorgan — post-CCAR capital return: $50B buyback (stated eff Jul 1) + div hike $1.50→$1.65/qtr (+10%); largest US bank. STARTER (~10.7%). Q2 earnings **CONFIRMED Tue Jul 14** = binary print → kept it a starter. Slipped slightly below entry on a quiet day-2; far above its stop. Thesis INTACT. |

**Open positions: 5 of 5 (AT CAP).** **Buys used this week: 1 of 3** (0 free slots). **Cash buffer: ~33.8%** (~66.2% invested, ~$68,887 market value). Net open unrealized **~+$5,132.66** (GE +1,951.65, LLY +1,696.10, DE +979.22, ETN +589.86, JPM −84.17) — book green except JPM (day-2 starter, −0.75%, far above its stop).

## Stop-management state (all 5 confirmed RESTING via open-orders query, status `new`)

- **LLY 10% trailing** `6016a7e7-faac-4e93-82e7-851abf30eca8` — floor **1114.2** (hwm 1238; above entry → locks a profit). Close 1199.61 below hwm → floor unchanged.
- **GE 10% trailing** `b9dadf2d-b6f5-49e7-8cc9-b3eb8b07aa6c` — floor **341.703** (hwm 379.67). Close 373.00 below hwm → floor unchanged.
- **DE 10% trailing** `dcdd84e5-6b94-4943-aa5b-3d3a299cbfce` — floor **572.661** (ratcheted up from 571.023 as DE printed a new hwm 636.29). **Only floor that moved today.**
- **ETN 10% trailing** `cc843666-7e63-462a-82d4-57cc3e826ead` — floor **393.066** (hwm 436.74). Close 426.12 below hwm → floor unchanged (~7.7% cushion).
- **JPM −7% HARD STOP** `3e8fe4ea-d95c-4e6c-82e1-ff66f0d56670` — stop **306.62** (GTC), entry 329.695588. Converts to a 10% trailing the moment JPM tags +5% (~$346.18); close 327.22 = ~−0.75%, so ~5.8% away.
- (a) **−7% drawdown check (net from entry):** worst is JPM −0.75% — all theses intact, none near −7%. HOLD. No sells.
- (b) **+5% → trailing:** 4 of 5 already on trailing; **JPM is the lone name on a −7% hard stop** (−0.75%, converts at ~$346.18).
- (c) **Daily loss cap:** equity +0.07% on the day — UP, nowhere near −3%. (Moot for buys anyway — at the cap.)
- daytrade_count 0.

## Watch / next (next routine: **pre-market Wed 7/1**)

- **JPM +5% → trailing conversion (standing task):** the moment JPM tags **~$346.18** (+5% from entry 329.695588), cancel the −7% hard stop `3e8fe4ea` and place a **10% trailing GTC**. Until then the −7% hard stop @ 306.62 protects it. (Close 327.22 — needs ~+5.8% from here.)
- **At the 5-position cap, 1 of 3 weekly buys used.** No new buys possible without a sell first. **Nothing on the bench clears ≥70** (AMGN 62 + Bernstein downgrade; healthcare lagging the rotation). DE's re-rating removes the obvious weak link → no natural swap target.
- **Alpha gap to watch:** WTD alpha −1.40% after two strong SPY up-days. This is the structural cash-drag/low-beta lag, not a thesis problem — but if SPY keeps running, weigh whether ~34% cash is too defensive for a beat-SPY mandate. Revisit at the weekly review (Fri is a holiday; effectively Thu 7/2).
- **Stops to watch:** ETN highest beta (floor 393.066, ~7.7% cushion); JPM on the only hard stop, slightly below entry. GE/LLY/DE all healthy. Let them work.
- **Macro week ahead (CLOSED Fri 7/3):** **ISM Manufacturing Wed 7/1**; **June JOBS REPORT Thu 7/2 8:30 ET** (THE swing event, thin pre-holiday liquidity). Do NOT initiate fresh size into the Thu print (moot at the cap). **JPM Q2 earnings Tue Jul 14** is the key position-level event.
- **Data flags / follow-ups:** (1) re-verify LLY's CMS Medicare GLP-1 $50/mo date (2026 vs 2027) — UNVERIFIED/conflicting; (2) confirm JPM's $50B buyback live via issuer IR (stated Jul-1 effective date now passed); (3) confirm the Jul-3 market-holiday status; (4) Powell-vs-Warsh Fed-chair identity STILL UNRESOLVED — don't build rate assumptions on it.

## Recent closes (last 5)

| Symbol | Exit Date | Shares | Entry | Exit | P/L $ | P/L % | Reason |
|---|---|---|---|---|---|---|---|
| NVDA | 2026-06-05 | 55 | 220.15 | 204.7158 | −848.88 | −7.01% | −7% hard stop fired (macro/NFP semis selloff, not thesis break) |
| NVDA | 2026-05-04 | 25 | 201.38 | ~195.02 | −159.04 | −3.16% | 10% trailing stop fired (round-trip) |

---
*Overwrite this file every routine. Keep it a live snapshot, not a log.*
