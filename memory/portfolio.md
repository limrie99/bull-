# Portfolio

**Last updated:** 2026-08-04 15:00 CT — **MARKET CLOSE (Tue).** Market CONFIRMED CLOSED via /v2/clock (is_open:false, 16:01 ET, next_open 8/5 09:30 ET). Account: equity **$101,631.36**, cash **$75,893.54** (~74.67%), long_market_value **$25,737.82** (~25.32%), status ACTIVE. `last_equity` (Mon 8/3 close) $101,194.62 → **day +$436.74 / +0.43%** (OFFICIAL EOD). Book **2 of 5 positions (three slots OPEN).** **Weekly buys 0/3.** **NO trades today** (open, midday, close — closed-orders query for 8/4 returned count 0). Both holdings finished green on a strong up day; both intact on resting 10% trailing stops. JPM printed a new intraday high (hwm ratcheted to **363** earlier today, floor **326.70**) then eased to 357.52 into the bell — floor held, no further ratchet. DE eased from its midday 621 to 617.37, so it slipped back under +5% (now +4.67%) — mechanically irrelevant (already on a trailing stop; the +5% rule only converts a *hard* stop, which DE doesn't have). **Inbox: nothing pending** (Lauren has not replied to 7/31 A/B cash decision → Option A / hold-the-bar stays the standing default).

## Scorecard (CLOSE 2026-08-04 — OFFICIAL EOD)
- **Equity $101,631.36.** Total since $100K start: **+1.63%.**
- **Day +$436.74 / +0.43%** vs Mon 8/3 close $101,194.62.
- **SPY day +1.77%** (757.72 Mon close → 771.11 Tue close). **Alpha today −1.34%.**
- **Week-to-date** (new week began Mon 8/3; WTD base = Fri 7/31 close $100,893.14): equity **+$738.22 / +0.73%**; SPY WTD **+3.26%** (746.79 → 771.11); **alpha WTD −2.53%.**
- **Net open unrealized: +$1,552.13** (JPM +946.03, DE +606.10).

## Open positions (2 of 5 — three slots OPEN) — closing marks 8/4

| Symbol | Shares | Avg Cost | Mark (close) | P/L $ | P/L % | Stop | Entry Date | Thesis (1 line) |
|---|---|---|---|---|---|---|---|---|
| JPM | 34 | 329.695588 | 357.52 | +946.03 | +8.44% | **10% TRAILING (GTC)**, floor **326.70**, hwm 363 | 2026-06-29 | JPMorgan — $50B buyback + div hike; largest US bank; Q2 (7/14) beat; DB UPGRADE Hold→Buy PT $375. sev 1 (quiet; next earnings ~Oct). **Cushion ~8.62%.** |
| DE | 22 | 589.82 | 617.37 | +606.10 | +4.67% | **10% TRAILING (GTC)**, floor **579.591**, hwm 643.99 | 2026-06-04 | Deere — Q2 beat, FY26 guide raised, right-to-repair settlement cleared. $1.62 div payable Aug 10. Off-cycle; next report ~Aug 20 (do NOT add ahead). sev 1 (soft ag demand + tariff overhang = SENTIMENT, not break). **Cushion ~6.12%.** |

**Open positions: 2 of 5 (three slots OPEN).** **Buys used this week: 0 of 3.** **Cash buffer: ~74.67%.** Position sizes (on equity $101,631.36): JPM 11.96%, DE 13.36% — both well under the 20% cap.

## Closed THIS WEEK
- **None** (new week began Mon 8/3). Last close: LLY trailing-stop exit 7/31 (+$627.34 / +4.15%), recorded in trade-log.

## Stop-management state (both re-confirmed RESTING via open-orders query, nested=true) — ALL 10% TRAILING GTC
- **JPM 10% trailing** `8a937ff6-164c-4384-8cf8-c000d4106a60` — Alpaca hwm **363**, floor (stop_price) **326.70**, status new (resting). Mark 357.52, cushion ~8.62%. New intraday high earlier ratcheted the floor to 326.70; closed below hwm → no further ratchet. qty 34, qty_available 0.
- **DE 10% trailing** `dcdd84e5-6b94-4943-aa5b-3d3a299cbfce` — Alpaca hwm **643.99**, floor (stop_price) **579.591**, status new (resting). Mark 617.37, cushion ~6.12%. Below hwm 643.99 → no ratchet, floor unchanged. qty 22, qty_available 0.

## Risk checks (close)
- **(a) Any position −7% or worse un-stopped?** NO. JPM +8.44%, DE +4.67%. Both on trailing stops above floors. **→ No −7% name, no Perplexity news check triggered.**
- **(b) Any position +5%+ needing hard→trailing conversion?** JPM +8.44% ≥ +5% but ALREADY on a 10% trailing (never reverted). DE +4.67% is now below +5% and also already trailing. **No −7% hard stop exists in the book to cancel → no conversion action.**
- **(c) Daily loss cap:** N/A — no buys attempted; portfolio +0.43% (up day, not down >3%).

## Watch / next (next routine: **pre-market Wed 8/5**)
- **DE — cushion ~6.12%** at close (was ~6.67% midday; eased 621 → 617.37). Still healthy and comfortably above its 579.591 floor; the tightest name in the book but no thesis break. $1.62 div payable Aug 10; next report ~Aug 20 (do NOT add ahead). Trailing floor handles any real break automatically.
- **JPM — cushion ~8.62%**, healthy and quiet; hit a new high (hwm 363) intraday, eased into the bell. Thesis intact. Next earnings ~Oct.
- **ETN — bench top ~68, FAILS gate, do NOT chase.** Still extended off its $361.88 base (~$445 today, ~+23% in days); wants a pullback to a base near $405–415. Good company, bad entry. No re-check needed unless it cools materially.
- **Macro:** MIXED, risk-on (SPY +1.77% today, +3.26% WTD in two sessions). **Do NOT chase fresh exposure into Fri Aug 7 July NFP** (week's binary event). NO CPI/PCE this week. Aug 12 US-China tariff deadline = DE ag-export risk.
- **No buy candidate clears the gate (~44th effectively-empty scan).** Bench: ETN ~68 (top, extended), RCL ~66, UNH ~64, TXN ~63, NOW 63, GS 63, GEV ~62, LMT ~62, DLR 60, DOV 58, JNJ 58, NOC ~55, OXY 55, STX 53, MS 52. None clears ≥70.
- **Cash-drag / Option A:** Lauren has not replied → Option A (hold the bar, keep cash dry) stands. **−2.53% alpha WTD** is structural (75% cash vs a strongly rallying SPY, +3.26% in two days), not a gate failure. The gate correctly benched every candidate. Deployment-level judgment remains parked on Lauren's A/B reply.

## Recent closes (last 5)

| Symbol | Exit Date | Shares | Entry | Exit | P/L $ | P/L % | Reason |
|---|---|---|---|---|---|---|---|
| LLY | 2026-07-31 | 14 | 1078.46 | 1123.27 | +627.34 | +4.15% | 10% trailing stop fired (give-back from ~1249 hwm; no thesis break; also removed Aug 5 earnings risk) |
| GE | 2026-07-16 | 45 | 329.63 | 344.54 | +670.95 | +4.52% | 10% trailing stop fired (post-Q2-earnings give-back caught the profit; no verified thesis break) |
| ETN | 2026-07-02 | 24 | 401.5425 | 392.75 | −211.02 | −2.19% | 10% trailing stop fired (beta/thin pre-holiday tape, not thesis break) |
| NVDA | 2026-06-05 | 55 | 220.15 | 204.7158 | −848.88 | −7.01% | −7% hard stop fired (macro/NFP semis selloff, not thesis break) |
| NVDA | 2026-05-04 | 25 | 201.38 | ~195.02 | −159.04 | −3.16% | 10% trailing stop fired (round-trip) |

---
*Overwrite this file every routine. Keep it a live snapshot, not a log.*
