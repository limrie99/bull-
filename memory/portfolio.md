# Portfolio

**Last updated:** 2026-09-03 08:40 CT (**MARKET OPEN routine**; /v2/clock is_open:true, next_close 09-03 16:00 ET). Live account: equity **$100,011.89**, cash **$10,514.60 (10.51%)**, long_market_value **~$89,500**, last_equity (Wed 9/2 close) $99,448.62 → **day +$563.27 (+0.57%)**, status ACTIVE. Conviction sleeve **3 of 5 (JPM, ATI, SNPS); two slots OPEN. Weekly conviction buys 2/3.** Three stops VERIFIED live resting (JPM 10% trailing, ATI −7% hard, SNPS −7% hard); SPY unencumbered by design. **2 TRADES today at the open:** BOUGHT SNPS (24 @ $417.00, the pre-market armed Grade-A buy) and TRIMMED SPY (sold 13 @ $769.15) to fund it — a clean swap of ~$10k index beta for a conviction pick, cash held on the ~$10k target.

## Open read (2026-09-03 market-open)
- **Executed the pre-market plan verbatim.** SNPS re-verified clean at the live open ($415.27 → $416.25 pre-fill, not gapped up/down; orderly up tape +0.57%, daily loss cap not tripped) → bought a conservative ~10% (~$10k) starter and placed its −7% hard stop at $387.81. Funded by trimming the SPY floor ~$10k first (rebalance rule: conviction picks take priority for the alpha budget; the floor is the shock-absorber), keeping whole-book cash on the ~$10k / 10% floor.
- **Why SNPS:** first name in weeks to clear the buy-gate (2+ signals AND Conviction ≥70) on a clean, non-extended entry. Signals #1 (beat + raised FY guide 8/29), #3 (AI/EDA secular, AVGO read-through), #4 (fresh Buy reiterations), #6 (on 50dMA, uptrend). Conviction ~80 (A). Sized at the conservative ~10% end (not the 15–20% A-band) for Friday's binary NFP + AVGO's jumpy sell-the-news AI tape. Next earnings ~Dec (clean).
- **JPM +8.92%,** trailing floor 329.85 (hwm 366.5), no ratchet; anchor, thesis intact (rising yields = NII tailwind). **ATI −2.42%,** recovered further (−3.81% close → −2.42%), hard stop 194.99 cushion ~6.7% widening as it firms; thesis intact (slide was profit-taking, not news). **SPY floor −0.14%→+0.14%,** no stop by policy.

## Open positions (3 conviction stocks + 1 index-floor sleeve) — live marks 2026-09-03 ~09:35 ET
| Symbol | Shares | Avg Cost | Price | P/L $ | P/L % | Stop | Entry Date | Thesis (1 line) |
|---|---|---|---|---|---|---|---|---|
| JPM | 34 | 329.695588 | 359.09 | +999.06 | +8.92% | **10% TRAILING (GTC)**, floor **329.85**, hwm 366.5 | 2026-06-29 | JPMorgan — $50B buyback + div hike; largest US bank; Q2 beat. Thesis INTACT (rising yields = tailwind; SEC margin probe early-stage/priced). Next earnings ~mid-Oct. |
| SNPS | 24 | 417.00 | 416.95 | −1.20 | −0.01% | **−7% HARD (GTC)** `387.81` | 2026-09-03 | Synopsys — chip-design/EDA software; AI-infra buildout drives EDA demand (AVGO read-through). Beat+raised FY guide 8/29. Grade-A (~80), 3–4 signals. Conservative ~10% starter (Fri NFP + AVGO tape). Converts to 10% trailing once +5%. Next earnings ~Dec. |
| ATI | 47 | 209.669787 | 204.595 | −238.51 | −2.42% | **−7% HARD (GTC)** `194.99` | 2026-08-31 | ATI Inc. — specialty metals/titanium for jet engines & defense; aerospace/defense + onshoring secular (#3) + trend (#6). B+ starter (~72). Thesis INTACT (no downgrade/cut/adverse filing; naval-nuclear + Cameco intact). Cushion to stop ~6.7% and widening. Converts to 10% trailing once +5%. |
| SPY | 75 | 767.829091 | 768.91 | +81.06 | +0.14% | **NONE — index-floor sleeve, deliberate no-stop carve-out** | 2026-08-10 (t1) / 08-11 (t2) / 08-31 (t3) / 09-01 (t4) / 09-03 (trim −13) | S&P 500 market floor (Lauren-approved Option B). Own sleeve, EXEMPT from ≤20%/max-5/max-3-per-week; NO −7%/trailing stop. Buy-and-hold-the-market. |

**Conviction sleeve: 3 of 5 (two slots OPEN).** **Conviction buys used this week: 2 of 3** (ATI 8/31, SNPS 9/3; SPY floor does NOT consume this budget). **Cash buffer: 10.51%** (on Lauren's ~$10k target). Sizes on equity $100,011.89: JPM ~12.21%, SNPS ~10.01%, ATI ~9.61%, SPY ~57.66% (index sleeve — exempt from the 20% cap by policy).

## Stop-management state (open-orders nested=true — VERIFIED live 2026-09-03 ~09:35 ET)
- **JPM 10% trailing** `8a937ff6-164c-4384-8cf8-c000d4106a60` — hwm **366.5**, floor **329.85**, status new (resting). qty 34. No ratchet (359.09 < hwm). Cushion ~8.1%.
- **SNPS −7% hard** `664e29e7-147d-4afb-a821-1623b0f279ed` — stop **387.81**, status new (resting). qty 24. Converts to 10% trailing once +5% in profit (currently −0.01%). (Replaced the initial OTO stop leg 7b5fbbb1 to nail exactly −7% off the $417.00 fill.)
- **ATI −7% hard** `fabe11de-0bce-42db-b6d4-167e33fd639b` — stop **194.99**, status new (resting). qty 47. Cushion ~6.7%. Converts to 10% trailing once +5% (currently −2.42%).
- **SPY — NO STOP by design** (index-floor sleeve carve-out). qty 75 unencumbered. Confirmed **3 open orders total** (JPM + SNPS + ATI stops).

## Risk checks (live marks)
- **(a) Any position −7% or worse un-stopped?** NO. JPM +8.92%, SNPS −0.01% (on −7% hard 387.81), ATI −2.42% (on −7% hard 194.99), SPY +0.14% (index, no stop). **→ No sell trigger.**
- **(b) Any position +5%+ needing hard→trailing conversion?** NO — JPM already on trailing; SNPS −0.01%, ATI −2.42% (both far from +5%); SPY carries no stop by policy. Zero conversions pending.
- **(c) Daily loss cap:** day +0.57% (equity $100,011.89 vs $99,448.62). Up day, cap not hit — buys were allowed.

## Watch / next (next routine: **midday Thu 2026-09-03**)
- **SNPS (NEW):** just opened at $417.00, −7% hard stop 387.81. Watch that it holds through AVGO's jumpy AI tape; no action unless it breaks toward the stop or a thesis-negative headline lands. Converts to 10% trailing at +5%.
- **ATI:** −2.42%, recovering steadily; cushion to −7% hard (194.99) ~6.7% and widening. Thesis intact. Let the stop work, NO averaging down.
- **JPM:** anchor, +8.92%, ~8.1% cushion; thesis intact; rising yields help.
- **Cash on target (~$10.5k / ~10.5%):** two conviction slots open and 1 weekly buy left, but do NOT force anything into Fri NFP (the week's binary macro print). Only a clean ≥70 name earns a slot.
- **Fri NFP (8:30 ET) is the week's gate.** ISM Services 10:00 ET today. AVGO sell-the-news may keep the AI/semi tape jumpy — relevant to SNPS.

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
