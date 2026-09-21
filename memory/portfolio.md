# Portfolio

**Last updated:** 2026-09-21 08:35 CT (**MARKET-OPEN routine**, Mon · new week). **No trades** — book fully invested (5 conviction stocks + SPY floor), sleeve 5/5 AT CAP with 0 open slots, and the pre-market swap check found no warranted swap (top bench TMO ~72 does not decisively beat lowest hold CFR ~72, and CFR's thesis is intact). Market CONFIRMED open via `/v2/clock` (is_open=true, 09:32 ET; next_close 16:00 ET). All 5 individual-stock stops re-VERIFIED live resting (exactly 5 open orders). No position at/near a −7% trigger; only JPM is >+5% and it is ALREADY on the 10% trailing → zero conversions pending. Daily loss cap not a factor (book **+0.23%** on the day).

---

**[Live snapshot 2026-09-21 08:35 CT — market-open, THIN intraday marks; the CLOSE routine owns today's authoritative scorecard]** Account (`/v2/account`): equity **$97,573.87**, cash **$10,661.62 (~10.93%)**, long_market_value **$86,912.25**, buying_power $286,000.78, status ACTIVE. **Day vs Fri 9/18 close ($97,350.35): +$223.52 / +0.23%.** SPY intraday ~+0.6% (last ~766.50 vs 9/18 close 761.62) → we're a touch behind on a green open, expected with our defensive tilt into a risk-on bounce; the close routine squares the real alpha.

## Day P/L (2026-09-21 08:35 CT — intraday, NOT authoritative)
- **Equity $97,573.87** · **Day +$223.52 / +0.23%** · SPY intraday ~+0.6% · we're modestly behind on the open (defensive book vs a broad bounce).
- Cash $10,661.62 (~10.93%) — on the ~$10k / 10% target floor. Started at $100,000; ~$86.9k at work.

## Open positions (5 conviction stocks + 1 index-floor sleeve) — LIVE marks 2026-09-21 08:35 CT
| Symbol | Shares | Avg Cost | Px | P/L $ | P/L % | Stop | Entry Date | Thesis (1 line) |
|---|---|---|---|---|---|---|---|---|
| JPM | 34 | 329.695588 | 353.55 | +811.05 | +7.23% | **10% TRAILING (GTC)**, floor **329.85**, hwm 366.5 | 2026-06-29 | JPMorgan — $50B buyback + div hike; largest US bank; Q2 beat. Thesis INTACT. Px below hwm → floor unchanged. Already trailing → no conversion. Next earnings **10/13 BMO**. |
| MDT | 96 | 92.67 | 91.75 | −88.32 | −0.99% | **−7% HARD (GTC)** `86.18` | 2026-09-17 | Medtronic — defensive med-tech, LOW rate-sens. Grade-A ~80: beat+raise, MiniMed separation, Hugo robotics FDA clearance, UBS PT $110. Converts to 10% trailing at +5%. |
| CFR | 60 | 163.15 | 160.28 | −171.90 | −1.76% | **−7% HARD (GTC)** `151.73` | 2026-09-09 | Cullen/Frost — Texas regional bank; rate-beneficiary (higher rates → wider NIM). B+ ~72. Cushion ~5.3% (firmed off Fri's low). No company-specific bad news; thesis intact. MS OW/PT $200. |
| RSG | 44 | 218.00 | 216.76 | −54.34 | −0.57% | **−7% HARD (GTC)** `202.74` | 2026-09-18 | Republic Services — defensive non-cyclical waste, LOW rate-sens. B+ ~76: #4 Cascade/Gates ~$129M open-market buy + #3 pricing-power secular. Day-4, slightly red. Converts to 10% trailing at +5%. |
| RMD | 42 | 228.627381 | 223.75 | −204.65 | −2.13% | **−7% HARD (GTC)** `212.62` | 2026-09-18 | ResMed — sleep-apnea/respiratory leader, LOW rate-sens. B+ ~78: #4 RBC Outperform (PT $262) + #3 aging/OSA secular + #6 uptrend; 9/16 IQVIA data de-risks GLP-1 fear. Day-4, slightly red. Converts to 10% trailing at +5%. |
| SPY | 49 | 764.716 | 766.14 | +69.76 | +0.19% | **NONE — index-floor sleeve, deliberate no-stop carve-out** | 2026-08-10→09-18 (trimmed) | S&P 500 market floor (Lauren-approved Option B). Own sleeve, EXEMPT from ≤20%/max-5/max-3-per-week; NO stop. |

**Conviction sleeve: 5 of 5 (AT CAP, 0 slots open).** **Conviction buys used this week (9/21–9/25): 0 of 3 (RESET — new week).** With the sleeve full, a new buy is only possible via a candidate SWAP — none warranted today. **Cash buffer: ~10.93%** (~$10,662 — on the ~$10k / 10% floor). Sizes on equity $97,573.87: JPM ~12.3%, MDT ~9.0%, CFR ~9.9%, RSG ~9.8%, RMD ~9.6%, SPY ~38.5% (index sleeve — exempt from the 20% cap by policy).

## Stop-management state (open-orders — VERIFIED live 2026-09-21 08:35 CT, exactly 5)
- **JPM 10% trailing** `8a937ff6-164c-4384-8cf8-c000d4106a60` — floor **329.85**, trail 10%, GTC, resting. qty 34. +7.23% but already trailing (px 353.55 below hwm 366.5) → nothing to convert, floor unchanged.
- **MDT −7% hard** `2768e81c-df5f-4da2-a285-27fdd469ba84` — stop **86.18**, GTC, resting. qty 96. −0.99% (below +5%).
- **CFR −7% hard** `cd725e5b-c593-4dde-8c72-1dda0cfbb8ae` — stop **151.73**, GTC, resting. qty 60. Cushion **~5.3%** (px 160.28). −1.76% (below +5%).
- **RSG −7% hard** `93c80d32-e37e-420d-be8f-6311918e3387` — stop **202.74**, GTC, resting. qty 44. −0.57% (below +5%).
- **RMD −7% hard** `91671fa4-1389-488e-8780-9a99103fb6a6` — stop **212.62**, GTC, resting. qty 42. −2.13% (below +5%).
- **SPY — NO STOP by design** (index-floor sleeve carve-out). qty 49 unencumbered. Confirmed **exactly 5 open orders total**.

## Risk checks (market-open 2026-09-21)
- **(a) Any position −7% or worse un-stopped?** NO. Worst is RMD −2.13%; CFR −1.76%; MDT −0.99%; RSG −0.57%; SPY +0.19% (no stop by policy); JPM +7.23%. Nothing at/near a trigger → **no sell trigger**.
- **(b) Any position +5%+ needing hard→trailing conversion?** NO — JPM is +7.23% but ALREADY on the 10% trailing (px below hwm 366.5); everything else below +5%. Zero conversions pending.
- **(c) Daily loss cap:** whole-book day **+0.23%** (green) — nowhere near the −3% cap; new buys not blocked on loss-cap grounds (they're blocked by the full sleeve instead).

## Today's trades
- **NONE.** No thesis break, no stop hit, no +5% conversion, no open slot, no warranted swap. A quiet, healthy open — the correct action is to hold.

## Watch / next (next routine: **midday**, then **market-close** owns the daily scorecard + mandatory Telegram)
- **CFR watch:** cushion ~5.3% to the 151.73 hard stop. Thesis INTACT (a hike helps NIM); the hard stop is the safety net. Do not average down.
- **JPM:** +7.23%, on the 10% trailing (floor 329.85, hwm 366.5). Earnings 10/13 BMO — no action yet.
- **MDT / RSG / RMD:** all slightly red day-1→day-4; −7% hard stops the safety net. Each converts to a 10% trailing stop once +5%. Do not average down.
- **Redeploy queue if a slot opens (thesis break / stop-out):** TMO → WMT → GD (on a 50dMA reclaim ~$376).
- **Cash ~$10.7k on target; sleeve 5/5, weekly buys 0/3 but no open slot.** No buy possible this week without a sell/swap.

## Recent closes (last 5)
| Symbol | Exit Date | Shares | Entry | Exit | P/L $ | P/L % | Reason |
|---|---|---|---|---|---|---|---|
| ATI | 2026-09-14 | 47 | 209.67 | 190.368299 | −907.17 | −9.21% | −7% hard stop fired at the open; ATI GAPPED below the 194.99 stop on a risk-off FOMC-eve slide. NO thesis break; back on watchlist. |
| SNPS | 2026-09-04 | 24 | 417.00 | 387.50 | −708.00 | −7.07% | −7% hard stop fired on a rate-driven software selloff (hot NFP). NO thesis break; back on watchlist. |
| LLY | 2026-08-31 | 12 | 1209.84 | 1152.00 | −694.08 | −4.78% | 10% trailing stop fired (give-back from hwm 1280.52; NO thesis break). Net both LLY legs ≈ −$67. |
| DE | 2026-08-19 | 22 | 589.82 | 579.4659 | −227.79 | −1.76% | 10% trailing stop fired at close; exited one minute before the Thu 8/20 Q3 print — no thesis break. |
| LLY | 2026-07-31 | 14 | 1078.46 | 1123.27 | +627.34 | +4.15% | 10% trailing stop fired (give-back; no thesis break). RE-ENTERED 8/12; re-stopped 8/31. |

---
*Overwrite this file every routine. Keep it a live snapshot, not a log.*
