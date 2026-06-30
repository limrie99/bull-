# Portfolio

**Last updated:** 2026-06-30 ~08:35 CT (09:35 ET) — **MARKET-OPEN routine. Market OPEN** (`is_open:true`, next_close 16:00 ET). **No trades** (at the 5-position cap, nothing clears the buy-gate, no sells — all theses intact and none near a stop). All 5 stops re-confirmed RESTING `status:new`, IDs unchanged. 4 of 5 on 10% trailing, JPM on its −7% hard stop. **Book AT the 5-position cap (5 of 5). Weekly buys 1 of 3.** daytrade_count 0. **Inbox: nothing pending.**

**Cash:** $35,237.52 (~34.0%).
**Equity (live, intraday open):** **$103,568.92** (cash $35,237.52 + long_market_value $68,331.40). last_equity **$104,056.85** = Alpaca's official 6/29 close (today's base).
**Day P/L (intraday open, noisy):** ~−$487.93 / −0.47% vs the 6/29 base — not meaningful at the opening bell; the close routine computes the official day + SPY scorecard.
**Week-to-date (through 6/29 close):** P/L **+0.95%**, SPY **+1.58%**, **alpha WTD −0.63%** (today is day 2 of the week).
**Buys used this week:** **1 of 3.** **0 open slots — AT the 5-position cap.** ~66% invested.

## Open positions (5 of 5 — AT CAP) — live intraday-open 6/30 marks

| Symbol | Shares | Avg Cost | Mark | P/L $ | P/L % | Stop | Entry Date | Thesis (1 line) |
|---|---|---|---|---|---|---|---|---|
| GE | 45 | 329.63 | 372.389 | +1,924.15 | +12.97% | **10% TRAILING (GTC)**, floor 341.703 | 2026-06-08 | GE Aerospace — record commercial-aircraft demand + high-margin engine aftermarket + defense; pure industrial, ZERO AI overlap, lower beta. Book's anchor. Earnings ~Jul 16 (UNVERIFIED). Thesis INTACT. |
| LLY | 14 | 1078.46 | 1212.85 | +1,881.43 | +12.46% | **10% TRAILING (GTC)**, floor **1114.2** (above entry → locks a profit) | 2026-06-01 | Eli Lilly — Q1 beat + raised guide + oral GLP-1 (orforglipron/Foundayo); late-stage weight-loss trial WIN 6/24. **DATA FLAG: the CMS Medicare GLP-1 $50/mo demo date is UNVERIFIED (2026 vs 2027) — re-verify, don't lean on it.** Core franchise thesis INTACT. |
| DE | 22 | 589.82 | 618.99 | +641.74 | +4.95% | **10% TRAILING (GTC)**, floor 568.737 | 2026-06-04 | Deere — **RE-RATED UP this run.** VERIFIED big Q2 beat (EPS $6.55 vs $5.70, rev $13.37B vs $11.55B), FY26 guide raised/maintained, **JPM PT $560→$590 (6/4)**, Buy consensus 0 Sells (6/29). WATCH tag removed → INTACT. Not the swap target. |
| ETN | 24 | 401.5425 | 410.25 | +208.98 | +2.17% | **10% TRAILING (GTC)**, floor 393.066 | 2026-06-08 | Eaton — electrical "picks-and-shovels" for AI data-center power + electrification. Highest-beta name, thinnest cushion (~4% above floor). No ETN-specific news, no downgrade. Earnings ~late July (UNVERIFIED). Thesis INTACT — watch beta. |
| JPM | 34 | 329.695588 | 327.28 | −82.13 | −0.73% | **−7% HARD STOP (GTC)** @ **306.62** | 2026-06-29 | JPMorgan — post-CCAR capital return: $50B buyback (stated eff Jul 1) + div hike $1.50→$1.65/qtr (+10%); largest US bank, near ATH. STARTER (~10.5%). Q2 earnings **CONFIRMED Tue Jul 14** = binary print ~9 trading days out → kept it a starter. **Buyback/div UNVERIFIED externally but NO walk-back.** Thesis INTACT. |

**Open positions: 5 of 5 (AT CAP).** **Buys used this week: 1 of 3** (0 free slots). **Cash buffer: ~34.0%** (~66% invested, ~$68,331 market value). Net open unrealized **~+$4,574.17** (GE +1,924.15, LLY +1,881.43, DE +641.74, ETN +208.98, JPM −82.13) — book green except JPM (day-2 starter, −0.73%, far above its stop).

## Stop-management state (all 5 confirmed RESTING via open-orders query, status `new`)

- **LLY 10% trailing** `6016a7e7-faac-4e93-82e7-851abf30eca8` — floor **1114.2** (above entry → locks a profit).
- **GE 10% trailing** `b9dadf2d-b6f5-49e7-8cc9-b3eb8b07aa6c` — floor **341.703**.
- **DE 10% trailing** `dcdd84e5-6b94-4943-aa5b-3d3a299cbfce` — floor **568.737**.
- **ETN 10% trailing** `cc843666-7e63-462a-82d4-57cc3e826ead` — floor **393.066** (thinnest cushion ~4%).
- **JPM −7% HARD STOP** `3e8fe4ea-d95c-4e6c-82e1-ff66f0d56670` — stop **306.62** (GTC), entry 329.695588. Converts to a 10% trailing the moment JPM tags +5% (~$346.18, ~5.5% above the current mark).
- (a) **−7% drawdown check (net from entry):** worst is JPM −0.73% — all theses intact, none near −7%. HOLD. No sells.
- (b) **+5% → trailing:** 4 of 5 already on trailing; **JPM is the lone name on a −7% hard stop** (−0.73%, converts at ~$346.18).
- (c) **Daily loss cap:** equity −0.47% intraday vs the 6/29 base — nowhere near −3%. Moot for new buys anyway — at the position cap.
- daytrade_count 0.

## Watch / next (next routine: **midday Tue 6/30**)

- **JPM +5% → trailing conversion (standing task):** the moment JPM tags **~$346.18** (+5% from entry 329.695588), cancel the −7% hard stop `3e8fe4ea` and place a **10% trailing GTC**. Until then the −7% hard stop @ 306.62 protects it. (Mark 327.28 — needs ~+5.8% from here.)
- **At the 5-position cap, 1 of 3 weekly buys used.** No new buys possible without a sell first. **Nothing on the bench clears ≥70** (AMGN 62 + Bernstein downgrade; healthcare lagging). DE's re-rating removes the obvious weak link → no natural swap target.
- **Stops to watch:** ETN thinnest cushion (~4% above floor 393.066) — the squeeze candidate if the tape rolls; JPM on the only hard stop. GE/LLY/DE all with healthy cushion. Let them work.
- **Macro week ahead (6/30–7/2; CLOSED Fri 7/3):** **June JOBS REPORT Thu 7/2 8:30 ET** (the swing event, thin pre-holiday liquidity). ISM Manufacturing Wed 7/1. **Do NOT initiate fresh size into the Thu print** (moot at the cap). **JPM Q2 earnings Tue Jul 14** is the key position-level event.
- **Data flags / follow-ups:** (1) **re-verify LLY's CMS Medicare GLP-1 $50/mo date (2026 vs 2027)** — UNVERIFIED/conflicting; (2) confirm JPM's $50B buyback live via issuer IR now the stated Jul-1 effective date has passed; (3) confirm the Jul-3 market-holiday status; (4) Powell-vs-Warsh Fed-chair identity STILL UNRESOLVED — don't build rate assumptions on it.

## Recent closes (last 5)

| Symbol | Exit Date | Shares | Entry | Exit | P/L $ | P/L % | Reason |
|---|---|---|---|---|---|---|---|
| NVDA | 2026-06-05 | 55 | 220.15 | 204.7158 | −848.88 | −7.01% | −7% hard stop fired (macro/NFP semis selloff, not thesis break) |
| NVDA | 2026-05-04 | 25 | 201.38 | ~195.02 | −159.04 | −3.16% | 10% trailing stop fired (round-trip) |

---
*Overwrite this file every routine. Keep it a live snapshot, not a log.*
