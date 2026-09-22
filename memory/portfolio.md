# Portfolio

**Last updated:** 2026-09-22 08:32 CT (**MARKET-OPEN routine**, Tue). Market **CONFIRMED open** via `/v2/clock` (is_open=true, 09:32 ET; next_close 16:00 ET). **No trades** — pre-market plan executed as written: sleeve **5/5 AT CAP, 0 open slots**, no thesis break, no stop hit, no +5% conversion pending, no warranted swap. All 5 individual-stock stops re-VERIFIED live resting GTC (exactly 5 open orders). All 5 theses INTACT; CFR still the tightest cushion. Marks below are **live opening marks** pulled from `/v2/positions` at 09:32 ET.

---

**[Live open snapshot 2026-09-22 08:32 CT]** Account (`/v2/account`): equity **$97,831.23**, cash **$10,661.62 (~10.90%)**, long_market_value **$87,169.61**, last_equity (Mon 9/21 close) $97,669.42, status ACTIVE. Intraday drift vs Mon close ≈ **+$161.81 / +0.17%** (green, quiet open). New week 9/21→9/25: WTD vs Fri 9/18 close ($97,350.35) ≈ **+$480.88 / +0.494%**. SPY opening mark 774.73 (own sleeve). Authoritative alpha-vs-SPY scorecard belongs to the market-close routine.

## Open positions (5 conviction stocks + 1 index-floor sleeve) — live marks 2026-09-22 08:32 CT
| Symbol | Shares | Avg Cost | Px | P/L $ | P/L % | Stop | Entry Date | Thesis (1 line) |
|---|---|---|---|---|---|---|---|---|
| JPM | 34 | 329.695588 | 350.61 | +711.06 | +6.34% | **10% TRAILING (GTC)**, floor **329.85**, hwm 366.5 | 2026-06-29 | JPMorgan — $50B buyback + div hike; largest US bank; Q2 beat. Thesis INTACT. Consensus PT ~$360. Already trailing → no conversion. Next earnings **10/13 BMO**. |
| MDT | 96 | 92.67 | 92.265 | −38.88 | −0.44% | **−7% HARD (GTC)** `86.18` | 2026-09-17 | Medtronic — defensive med-tech, LOW rate-sens. Grade-A ~80: beat+raise, MiniMed separation, Hugo robotics FDA clearance, avg PT ~$104. Converts to 10% trailing at +5%. |
| CFR | 60 | 163.15 | 159.19 | −237.60 | −2.43% | **−7% HARD (GTC)** `151.73` | 2026-09-09 | Cullen/Frost — Texas regional bank; rate-beneficiary/NIM. B+ ~72. Cushion **~4.7%** (tightest). No company-specific/Texas-bank bad news; thesis intact. |
| RSG | 44 | 218.00 | 214.28 | −163.68 | −1.71% | **−7% HARD (GTC)** `202.74` | 2026-09-18 | Republic Services — defensive non-cyclical waste, LOW rate-sens. B+ ~76: #4 Cascade/Gates buy + #3 pricing power. BofA reiterated Buy $241 (9/21). Converts at +5%. |
| RMD | 42 | 228.627381 | 224.98 | −153.21 | −1.59% | **−7% HARD (GTC)** `212.62` | 2026-09-18 | ResMed — sleep-apnea/respiratory leader, LOW rate-sens. B+ ~78: #4 RBC Outperform (PT $262) + #3 aging/OSA secular. Reaffirmed LT targets 9/21. Converts at +5%. |
| SPY | 49 | 764.716327 | 774.7276 | +490.84 | +1.31% | **NONE — index-floor sleeve, deliberate no-stop carve-out** | 2026-08-10→09-18 (trimmed) | S&P 500 market floor (Lauren-approved Option B). Own sleeve, EXEMPT from ≤20%/max-5/max-3-per-week; NO stop. |

**Conviction sleeve: 5 of 5 (AT CAP, 0 slots open).** **Conviction buys used this week (9/21–9/25): 0 of 3.** With the sleeve full, a new buy is only possible via a candidate SWAP — none warranted (no breaking catalyst; top bench TMO ~72 got weaker last run and does not beat lowest hold CFR ~72, thesis intact). **Cash buffer: ~10.90%** (~$10,662 — on the ~$10k / 10% floor). Sizes on equity $97,831.23: JPM ~12.2%, MDT ~9.1%, CFR ~9.8%, RSG ~9.6%, RMD ~9.7%, SPY ~38.8% (index sleeve — exempt from the 20% cap by policy).

## Stop-management state (open-orders — VERIFIED live 2026-09-22 08:32 CT, exactly 5)
- **JPM 10% trailing** `8a937ff6-164c-4384-8cf8-c000d4106a60` — floor **329.85**, trail 10%, GTC, resting. qty 34. +6.34% but already trailing (px below hwm 366.5) → nothing to convert.
- **MDT −7% hard** `2768e81c-df5f-4da2-a285-27fdd469ba84` — stop **86.18**, GTC, resting. qty 96. −0.44% (below +5%).
- **CFR −7% hard** `cd725e5b-c593-4dde-8c72-1dda0cfbb8ae` — stop **151.73**, GTC, resting. qty 60. Cushion **~4.7%** (px 159.19, tightest in book). −2.43% (below +5%).
- **RSG −7% hard** `93c80d32-e37e-420d-be8f-6311918e3387` — stop **202.74**, GTC, resting. qty 44. −1.71% (below +5%).
- **RMD −7% hard** `91671fa4-1389-488e-8780-9a99103fb6a6` — stop **212.62**, GTC, resting. qty 42. −1.59% (below +5%).
- **SPY — NO STOP by design** (index-floor sleeve carve-out). qty 49 unencumbered. Confirmed **exactly 5 open orders total**.

## Risk checks (live open 2026-09-22 08:32 CT)
- **(a) Any position −7% or worse un-stopped?** NO. Worst is CFR −2.43%; RSG −1.71%; RMD −1.59%; MDT −0.44%; SPY +1.31% (no stop by policy); JPM +6.34%. Nothing at/near a trigger → **no sell trigger**.
- **(b) Any position +5%+ needing hard→trailing conversion?** NO — JPM is +6.34% but ALREADY on the 10% trailing; everything else below +5%. Zero conversions pending.
- **(c) Daily loss cap:** intraday +0.17% (green) — cap governs a >3% intraday drop; not close, and no new buys planned regardless (sleeve full).

## Today's trades
- **NONE.** Market-open routine, market confirmed open. No thesis break, no stop hit, no +5% conversion, no open slot, no warranted swap, no binary catalyst. Correct action: hold and manage.

## Watch / next (next routine: **midday Tue 9/22 12:00 CT**)
- **No standing buy order armed** — hold-and-manage unless something breaks intraday. Re-verify /v2/clock + re-pull account/positions/open-orders at midday before acting.
- **CFR watch:** cushion ~4.7% to the 151.73 hard stop (tightest in book). Thesis INTACT; if a rate-driven regional-bank reaction tags the stop, that is the plan working — do NOT pre-empt, do NOT average down.
- **JPM:** +6.34%, on the 10% trailing (floor 329.85, hwm 366.5). Earnings 10/13 BMO — no action yet.
- **MDT / RSG / RMD:** all slightly red; −7% hard stops the safety net. Each converts to a 10% trailing stop once +5%. Do not average down.
- **Redeploy queue if a slot opens (thesis break / stop-out):** TMO (only on a non-extended pullback) → ADM (needs a live ≥70 re-score) → GD/WMT on a 50dMA reclaim. Idle remainder → SPY floor per policy.
- **Astra:** `memory/astra-proposals.md` present, **still no proposals** — nothing to fold into scoring.
- **Cash ~$10.7k on target; sleeve 5/5, weekly buys 0/3 but no open slot.** No buy possible this week without a sell/swap. Market-close owns the alpha-vs-SPY scorecard + mandatory daily Telegram.

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
