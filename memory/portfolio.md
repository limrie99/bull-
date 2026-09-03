# Portfolio

**Last updated:** 2026-09-03 15:05 CT (**MARKET-CLOSE routine**; /v2/clock is_open:false, next_open 09-04 09:30 ET). Live account: equity **$100,415.97**, cash **$10,514.60 (10.47%)**, long_market_value **$89,901.37**, last_equity (Wed 9/2 close) $99,448.62 → **day +$967.35 (+0.97%)**, status ACTIVE. Conviction sleeve **3 of 5 (JPM, ATI, SNPS); two slots OPEN. Weekly conviction buys 2/3.** **Three stops VERIFIED live resting** (JPM 10% trailing, ATI −7% hard, SNPS −7% hard). **⚠️ Fixed at close:** the SNPS stop set at this morning's buy was submitted as a `day` order (via the OTO-then-replace) and **expired at 16:01 ET / close** — I re-placed it as a proper **GTC** hard stop (`8b33dd45`, 387.81) minutes after close, so SNPS is protected again before the next open. No trades at close.

## Close read (2026-09-03)
- **Up day, a hair behind the tape.** Book **+0.97%** vs **SPY +1.04%** → **alpha −0.07pp today.** Week-to-date **+0.15% vs SPY +0.50% → WTD alpha −0.35pp** (behind this week). Same shape all week: ~58% of the book is SPY (matches the index), JPM's large *cumulative* gain isn't throwing off *daily* alpha, and ATI's red (now much smaller) is the residual drag.
- **The one real event today was a plumbing catch, not a market move:** the SNPS hard stop expired at the close because the morning routine wrote it with `time_in_force: day` instead of `gtc` (the two OTHER stops — JPM, ATI — are GTC and survived). Caught it at the first routine after expiry, re-armed a GTC stop before any next-session trading could occur. Lesson for future routines: **always place standalone stops as GTC and re-verify tif, not just presence, at close.**
- **ATI recovered strongly** — closed −2.45% (204.54), up ~+1.41% on the day from 201.69; cushion to the −7% hard (194.99) widened to ~4.67%. Best relative mover in the sleeve today.

## Open positions (3 conviction stocks + 1 index-floor sleeve) — closing marks 2026-09-03
| Symbol | Shares | Avg Cost | Close | P/L $ | P/L % | Stop | Entry Date | Thesis (1 line) |
|---|---|---|---|---|---|---|---|---|
| JPM | 34 | 329.695588 | 362.95 | +1130.65 | +10.09% | **10% TRAILING (GTC)**, floor **329.85**, hwm 366.5 | 2026-06-29 | JPMorgan — $50B buyback + div hike; largest US bank; Q2 beat. Thesis INTACT (rising yields = tailwind). Next earnings ~mid-Oct. Cushion ~9.12%. |
| SNPS | 24 | 417.00 | 416.31 | −16.56 | −0.17% | **−7% HARD (GTC)** `387.81` — **RE-PLACED at close** (`8b33dd45`) | 2026-09-03 | Synopsys — chip-design/EDA software; AI-infra buildout drives EDA demand (AVGO read-through). Beat+raised FY guide 8/29. Grade-A (~80). Converts to 10% trailing once +5%. Next earnings ~Dec. Cushion ~6.85%. |
| ATI | 47 | 209.669787 | 204.54 | −241.10 | −2.45% | **−7% HARD (GTC)** `194.99` | 2026-08-31 | ATI Inc. — specialty metals/titanium for jet engines & defense; aerospace/defense + onshoring secular. B+ starter (~72). Thesis INTACT. Recovered +1.41% today; cushion ~4.67%. Converts to 10% trailing once +5%. |
| SPY | 75 | 767.829091 | 772.71 | +366.07 | +0.64% | **NONE — index-floor sleeve, deliberate no-stop carve-out** | 2026-08-10 (t1) / 08-11 (t2) / 08-31 (t3) / 09-01 (t4) / 09-03 (trim −13) | S&P 500 market floor (Lauren-approved Option B). Own sleeve, EXEMPT from ≤20%/max-5/max-3-per-week; NO −7%/trailing stop. Buy-and-hold-the-market. |

**Conviction sleeve: 3 of 5 (two slots OPEN).** **Conviction buys used this week: 2 of 3** (ATI 8/31, SNPS 9/3; SPY floor does NOT consume this budget). **Cash buffer: 10.47%** (on Lauren's ~$10k target). Sizes on equity $100,415.97: JPM ~12.29%, SNPS ~9.95%, ATI ~9.57%, SPY ~57.71% (index sleeve — exempt from the 20% cap by policy).

## Performance
- **Today:** equity $100,415.97 vs $99,448.62 (Wed 9/2 close) = **+$967.35 (+0.97%)**. SPY 765.13 → 773.115 (authoritative daily bars) = **+1.04%**. **Alpha today = −0.07pp.**
- **Week-to-date** (base Fri 8/28 close $100,263.51 → $100,415.97) = **+0.15%**; SPY 769.28 → 773.115 = **+0.50%**. **WTD alpha = −0.35pp.**

## Stop-management state (open-orders — VERIFIED live 2026-09-03 ~16:02 ET, post-close)
- **JPM 10% trailing** `8a937ff6-164c-4384-8cf8-c000d4106a60` — hwm **366.5**, floor **329.85**, GTC, status new (resting). qty 34. No ratchet (362.95 < hwm). Cushion ~9.12%.
- **ATI −7% hard** `fabe11de-0bce-42db-b6d4-167e33fd639b` — stop **194.99**, GTC, status new (resting). qty 47. Cushion ~4.67%. Converts to 10% trailing once +5% (currently −2.45%).
- **SNPS −7% hard** `8b33dd45-04f5-450f-b0e1-096796af172c` — stop **387.81**, GTC, status accepted (resting). qty 24. **NEW — replaces the expired `day`-tif stop `664e29e7`.** Converts to 10% trailing once +5% (currently −0.17%). Cushion ~6.85%.
- **SPY — NO STOP by design** (index-floor sleeve carve-out). qty 75 unencumbered. Confirmed **3 open orders total** (JPM + ATI + SNPS stops).

## Risk checks (closing marks)
- **(a) Any position −7% or worse un-stopped?** NO. JPM +10.09%, SNPS −0.17% (on −7% hard 387.81, GTC), ATI −2.45% (on −7% hard 194.99), SPY +0.64% (index, no stop). **→ No sell trigger; no news-check required.**
- **(b) Any position +5%+ needing hard→trailing conversion?** NO — JPM already on trailing; SNPS −0.17%, ATI −2.45% (both far from +5%); SPY carries no stop by policy. Zero conversions pending.
- **(c) Daily loss cap:** day +0.97% (up day). Cap (−3% intraday) NOT hit.

## Watch / next (next routine: **pre-market Fri 2026-09-04**)
- **SNPS stop tif:** re-verify the new GTC stop `8b33dd45` is still resting at the next open (it should survive overnight — GTC — unlike the expired day-order). Guard against a repeat: standalone stops go in as GTC.
- **Fri NFP (8:30 ET) is the week's gate.** August payrolls — the binary macro print. Keep entry discipline; do NOT initiate fresh beta into it. Two conviction slots and 1 weekly buy remain, but only a clean ≥70 name earns a slot.
- **ATI:** recovered to −2.45% (cushion ~4.67%); thesis intact, let the stop work, NO averaging down.
- **JPM:** anchor, +10.09%, ~9.12% cushion; thesis intact (rising yields help).
- **SPY sleeve** captured most of today's up tape as designed (~58% of book, no stop).

## Recent closes (last 5)
| Symbol | Exit Date | Shares | Entry | Exit | P/L $ | P/L % | Reason |
|---|---|---|---|---|---|---|---|
| LLY | 2026-08-31 | 12 | 1209.84 | 1152.00 | −694.08 | −4.78% | 10% trailing stop fired (give-back from hwm 1280.52; NO thesis break). Re-entry of the 7/31 winner; net both LLY legs ≈ −$67. |
| DE | 2026-08-19 | 22 | 589.82 | 579.4659 | −227.79 | −1.76% | 10% trailing stop fired at close; exited one minute before the Thu 8/20 Q3 print — no thesis break. |
| LLY | 2026-07-31 | 14 | 1078.46 | 1123.27 | +627.34 | +4.15% | 10% trailing stop fired (give-back; no thesis break). RE-ENTERED 8/12; re-stopped 8/31. |
| GE | 2026-07-16 | 45 | 329.63 | 344.54 | +670.95 | +4.52% | 10% trailing stop fired (post-Q2 give-back; no verified thesis break) |
| ETN | 2026-07-02 | 24 | 401.5425 | 392.75 | −211.02 | −2.19% | 10% trailing stop fired (beta/thin pre-holiday tape, not thesis break) |

---
*Overwrite this file every routine. Keep it a live snapshot, not a log.*
