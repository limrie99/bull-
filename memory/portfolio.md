# Portfolio

**Last updated:** 2026-08-25 06:15 CT (07:15 ET) — **PRE-MARKET (Tue).** Market CLOSED pre-open (/v2/clock is_open:false, next_open 09:30 ET). Account: equity **$101,031.08**, cash **$49,389.91** (~48.9%), long_market_value **$51,641.17** (~51.1%), buying_power $342,154.91, status ACTIVE. `last_equity` (Mon 8/24 close) $100,901.37 → pre-market +$130 on thin/indicative marks (NOT a real day move — market closed). ✅ **Perplexity RECOVERED** (live-tested HTTP 200 w/ citations) — full 4-agent scan ran. **NO TRADES (research routine, market closed).** Conviction sleeve **2 of 5 (three slots OPEN); weekly conviction buys 0/3.** Two conviction trailing stops resting (JPM + LLY; SPY zero by policy) — **VERIFIED live via open-orders.** **Inbox: nothing pending.**

## Open decision (2026-08-25 pre-market)
- **No sells.** No position at/through its −7% or trailing floor; position analyst (Perplexity) found no thesis break on JPM or LLY in the last 24–48h. LLY got a cosmetic WS Zen "strong buy"→"buy" nudge (8/23) + an Amazon Pharmacy distribution tailwind (8/24) — neither is a sell trigger.
- **No buy (market closed anyway).** Only **BJ** touches the buy-gate (3 signals, ~70–72), but Alpaca-IEX primary puts it +7.35% above its 50dMA = right at the "no-chase" line, and the print-catalyst is aging. Hand market-open ONE live candidate (BJ) with a "verify it hasn't chased further + still-positive tape; prefer a modest starter or one-day patience into Wed" instruction.
- **Patience into the heaviest binary-event week of the quarter:** Wed 8/26 NVIDIA Q2 (after close) + July PCE + Q2 GDP 2nd est; Fri 8/28 Fed Chair Warsh's first Jackson Hole keynote. ~49% cash is fine (floor built, no cash-drag pressure).

## Open positions (2 conviction stocks + 1 index-floor sleeve) — pre-market marks ~07:15 ET 8/25
| Symbol | Shares | Avg Cost | Price | P/L $ | P/L % | Stop | Entry Date | Thesis (1 line) |
|---|---|---|---|---|---|---|---|---|
| JPM | 34 | 329.695588 | 357.50 | +944.90 | +8.43% | **10% TRAILING (GTC)**, floor **329.85**, hwm 366.5 | 2026-06-29 | JPMorgan — $50B buyback + div hike; largest US bank; Q2 beat. No material 24–48h news (verified). Next earnings ~Oct. Alpaca 50dMA 344.80, +3.37% clean. Cushion ~7.0% to floor. |
| LLY | 12 | 1209.84 | 1247.00 | +445.92 | +3.07% | **10% TRAILING (GTC)**, floor **1152.468**, hwm 1280.52 | 2026-08-12 | Eli Lilly — Q2 beat-and-raise + GLP-1/obesity lead (US share ~60.9% vs Novo 38.8%). WS Zen→"buy" 8/23 cosmetic; Amazon Pharmacy $50/mo distribution tailwind 8/24. Alpaca 50dMA 1181.39, +5.58% clean. Cushion ~7.6% to floor. |
| SPY | 32 | 772.921250 | 766.32 | −211.49 | −0.85% | **NONE — index-floor sleeve, deliberate no-stop carve-out** | 2026-08-10 (t1) / 2026-08-11 (t2) | S&P 500 market floor (Lauren-approved Option B). Own sleeve, EXEMPT from ≤20%/max-5/max-3-per-week caps; NO −7%/trailing stop. Buy-and-hold-the-market. |

**Conviction sleeve: 2 of 5 (three slots OPEN).** **Conviction buys used this week: 0 of 3** (SPY floor does NOT consume this budget). **Cash buffer: ~48.9%.** Sizes on equity $101,031.08: JPM ~12.03%, LLY ~14.81%, SPY ~24.28% (index sleeve — exempt from the 20% cap by policy).

## Stop-management state (open-orders nested=true — VERIFIED live ~07:15 ET 8/25)
- **JPM 10% trailing** `8a937ff6-164c-4384-8cf8-c000d4106a60` — hwm **366.5**, floor **329.85**, status new (resting). Pre-market 357.50 < hwm → no ratchet. qty 34. Cushion ~7.0%.
- **LLY 10% trailing** `d7eb221b-4d37-4dc6-bec2-b1de0dddd825` — hwm **1280.52**, floor **1152.468**, status new (resting). Pre-market 1247.00 < hwm → no ratchet. qty 12. Cushion ~7.6%.
- **SPY — NO STOP by design** (index-floor sleeve carve-out). qty 32 unencumbered. Do NOT place a stop.

## Risk checks (pre-market marks)
- **(a) Any position −7% or worse un-stopped?** NO. JPM +8.43%, LLY +3.07%, SPY −0.85% (index sleeve, no stop by policy). **→ No sell trigger.** (Position analyst: no thesis break on JPM/LLY 24–48h.)
- **(b) Any position +5%+ needing hard→trailing conversion?** NO pending — JPM & LLY already on 10% trailing; SPY carries no stop by policy. (LLY +3.07% < +5%.)
- **(c) Daily loss cap:** market closed → moot. No buys placed anyway.

## Watch / next (next routine: **market-open 8/25**)
- **BJ (BJ's Wholesale) — SINGLE LIVE CANDIDATE, ~70–72 BORDERLINE.** 3 signals (beat-and-raise + Gordon Haskett→Buy PT $115 + held print gain) but +7.35% vs 50dMA = at the no-chase line, print-catalyst aging. Market-open: verify it hasn't chased further + still-positive tape; prefer a modest B+ starter or one-day patience into Wed NVDA/PCE.
- **ABBV — WATCH, NO BUY.** +6.38% vs 50dMA, ~1% off 52-wk high, insider selling flagged, no dated <30d catalyst. Re-look on a pull to ~$248–252 + a dated catalyst.
- **AMGN — WATCHLIST-sub70.** Beat-and-raise + GLP-1/MariTide but extension unverified/likely extended; verify entry before it qualifies.
- **Tape caution:** WMT beat-and-raise yet fell ~9%; require a verified positive reaction, not just a good headline.
- **Macro binaries this week:** Wed 8/26 NVDA + PCE + GDP; Fri 8/28 Warsh Jackson Hole. Do NOT rush a new buy ahead of them.

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
