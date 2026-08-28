# Portfolio

**Last updated:** 2026-08-28 16:00 CT (weekly-review; snapshot unchanged from the 15:00 CT market-close, market still closed) — **MARKET CLOSED** (/v2/clock is_open:false, 16:02 ET, next_open Mon 2026-08-31 09:30 ET). Closing snapshot from Alpaca: equity **$100,251.79**, cash **$49,389.91 (~49.27%)**, long_market_value **$50,861.88 (~50.73%)**, buying_power $339,972.90, status ACTIVE. Yesterday (Thu 8/27) close $100,221.79 → **day +$30.00 / +0.03%**. **NO TRADES today** (0 closed orders). Both conviction trailing stops VERIFIED resting (2 open orders, JPM + LLY); SPY unencumbered by design. Conviction sleeve **2 of 5 (three slots OPEN); weekly conviction buys 0/3.**

> **⚠️ STANDING ACTION NOT EXECUTED TODAY — CARRIED TO MON 8/31 OPEN.** Lauren's 8/27 instruction to deploy idle cash into the SPY floor (leave ~$10k buffer) was **not executed during Friday's session** — the open and midday routines held on cash. Market is now closed, so the market-close routine cannot fill it. The deploy is **re-armed for the Mon 8/31 market-open routine** (inbox item kept Pending). This cash drag is the main reason we trail SPY week-to-date.

## Day performance (2026-08-28 close)
- **Portfolio day:** +$30.00 / **+0.03%** (equity $100,251.79 vs Thu close $100,221.79).
- **SPY day:** **−0.25%** (close 769.28 vs Thu close 771.18, Alpaca daily bars).
- **Alpha today:** **+0.28 pp** — we edged SPY today (our conviction names held while the index dipped).
- **Week-to-date (WTD, vs prior-Fri 8/21 close $100,911.47):** portfolio **−0.65%** · SPY **+0.48%** (769.28 vs 765.64) · **WTD alpha −1.13 pp (we LAG the market this week).**

## Open positions (2 conviction stocks + 1 index-floor sleeve) — closing marks 2026-08-28
| Symbol | Shares | Avg Cost | Close Price | P/L $ | P/L % | Stop | Entry Date | Thesis (1 line) |
|---|---|---|---|---|---|---|---|---|
| JPM | 34 | 329.695588 | 357.50 | +945.35 | +8.43% | **10% TRAILING (GTC)**, floor **329.85**, hwm 366.5 | 2026-06-29 | JPMorgan — $50B buyback + div hike; largest US bank; Q2 beat. Thesis INTACT. Cushion ~7.7% to floor. Next earnings ~Oct. |
| LLY | 12 | 1209.84 | 1174.00 | −430.08 | −2.96% | **10% TRAILING (GTC)**, floor **1152.468**, hwm 1280.52 | 2026-08-12 | Eli Lilly — Q2 beat-and-raise + GLP-1/obesity lead. Thesis INTACT (no fresh negative catalyst; slide = profit-taking). Cushion **~1.83% (tightest in book)** — a drift to ~$1,152 auto-exits. Next earnings ~late Oct. |
| SPY | 32 | 772.921250 | 769.33 | −114.92 | −0.47% | **NONE — index-floor sleeve, deliberate no-stop carve-out** | 2026-08-10 (t1) / 2026-08-11 (t2) | S&P 500 market floor (Lauren-approved Option B). Own sleeve, EXEMPT from ≤20%/max-5/max-3-per-week caps; NO −7%/trailing stop. Buy-and-hold-the-market. |

**Conviction sleeve: 2 of 5 (three slots OPEN).** **Conviction buys used this week: 0 of 3** (SPY floor does NOT consume this budget). **Cash buffer: ~49.27%** (target per Lauren: ~$10k / ~10% once the floor deploy runs Monday). Sizes on equity $100,251.79: JPM ~12.12%, LLY ~14.05%, SPY ~24.56% (index sleeve — exempt from the 20% cap by policy).

## Stop-management state (open-orders nested=true — VERIFIED live at close 2026-08-28)
- **JPM 10% trailing** `8a937ff6-164c-4384-8cf8-c000d4106a60` — hwm **366.5**, floor **329.85**, status new (resting). qty 34. No ratchet (357.50 < hwm). Cushion ~7.7%.
- **LLY 10% trailing** `d7eb221b-4d37-4dc6-bec2-b1de0dddd825` — hwm **1280.52**, floor **1152.468**, status new (resting). qty 12. No ratchet (1174.00 < hwm). Cushion **~1.83% (tightest)**.
- **SPY — NO STOP by design** (index-floor sleeve carve-out). qty 32 unencumbered. Confirmed only 2 open orders total (JPM + LLY stops).

## Risk checks (closing marks)
- **(a) Any position −7% or worse un-stopped?** NO. JPM +8.43%, LLY −2.96% (on trailing stop), SPY −0.47%. **→ No sell trigger.**
- **(b) Any position +5%+ needing hard→trailing conversion?** NO — both conviction names already on 10% trailing; SPY carries no stop by policy. Zero hard stops in book.
- **(c) Daily loss cap:** day +0.03%. Clear.

## Watch / next (next routine: **pre-market Mon 2026-08-31**)
- **MON 8/31 OPEN — EXECUTE THE CASH DEPLOY (#1 NON-NEGOTIABLE, per weekly review 8/28).** Per Lauren's 8/27 standing instruction: enlarge the SPY market-floor sleeve so whole-book cash lands near **$10,000** (leave the ~10% buffer, never below it). Size from live Monday-open prices. This was due Friday and got missed on the open AND midday despite a benign-tape green light — Monday's routine MUST run it first (unless Lauren countermands in inbox first). The weekly review graded the week a C largely for this miss; the tape-timing excuse is spent and research is back online. No rule changed — strategy already mandates it; the gap is execution.
- **Weekly review DONE (8/28 16:00 CT):** week −0.65% vs SPY +0.48% = **−1.13 alpha (miss)**; cumulative alpha −1.30 (run-worst). Grade **C**. Miss decomposition: ~65% LLY (−6.5%, newsless/thesis-intact), ~20% idle-cash drag, JPM +0.14 offset, SPY floor tracked (neutral). No strategy change warranted. Perplexity **recovered** 8/24 — research online again.
- **LLY:** cushion **~1.83% (tightest of the run)** — a drift to ~$1,152 trips the trailing stop and auto-exits. Thesis intact; mechanical protection working as designed, no manual action needed. Watch for any late Novo/reimbursement/FDA headline.
- **JPM:** anchor, +8.43%, ~7.7% cushion; thesis intact.
- **BJ — former #1 candidate, still DON'T buy (below 50dMA).** Re-arm only on a confirmed base / 50dMA reclaim (~$92) with a positive tape. ROST same broken chart.

## Recent closes (last 5)
| Symbol | Exit Date | Shares | Entry | Exit | P/L $ | P/L % | Reason |
|---|---|---|---|---|---|---|---|
| DE | 2026-08-19 | 22 | 589.82 | 579.4659 | −227.79 | −1.76% | 10% trailing stop fired at close; exited one minute before the Thu 8/20 Q3 print — no thesis break. Post-print +9%, but entry now a gap-chase; NOT re-bought. |
| LLY | 2026-07-31 | 14 | 1078.46 | 1123.27 | +627.34 | +4.15% | 10% trailing stop fired (give-back; no thesis break). **RE-ENTERED 8/12** on the verified beat-and-raise. |
| GE | 2026-07-16 | 45 | 329.63 | 344.54 | +670.95 | +4.52% | 10% trailing stop fired (post-Q2 give-back; no verified thesis break) |
| ETN | 2026-07-02 | 24 | 401.5425 | 392.75 | −211.02 | −2.19% | 10% trailing stop fired (beta/thin pre-holiday tape, not thesis break) |
| NVDA | 2026-06-05 | 55 | 220.15 | 204.7158 | −848.88 | −7.01% | −7% hard stop fired (macro/NFP semis selloff, not thesis break) |

---
*Overwrite this file every routine. Keep it a live snapshot, not a log.*
