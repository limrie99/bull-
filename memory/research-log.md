# Research Log

**Append-only by date.** Most recent entries at the top.

Each routine appends its research here. Use this as thinking space. The weekly review reads back over this to identify patterns.

Format:

```
## YYYY-MM-DD HH:MM CT — {routine name}

### Market context
Futures, overnight moves, major headlines, macro prints.

### Portfolio watch
Each open position: any news, catalyst, red flags.

### Buy candidates
Symbol — thesis — which strategy signals hit — conviction (high/med/low).

### Sell candidates
Symbol — which sell signal — urgency.

### Day summary (market-close routine only)
Portfolio close value, day P/L, SPY day P/L, alpha, trades placed, what worked / what didn't.
```

---
## 2026-06-02 12:00 CT — midday

**Setup:** Memory synced from origin/main; all 4 required keys present; market OPEN (clock is_open=true, close 15:00 CT). Account: equity $99,964.59, last_equity $100,124.86, cash $72,634.26, daytrade_count 0. Inbox: nothing pending. **No trades this routine** — pure risk monitoring.

### Risk checks (priority order)
- **(a) Any position ≤ −7%?** No. LLY −1.01% (cur 1067.57), NVDA +2.28% (cur 225.18). Neither near the hard stop. No forced-sell evaluation needed.
- **(b) Any position ≥ +5% → convert to 10% trailing?** No. NVDA +2.28%, ~$5.98 below the +5% trigger (~$231.16) — it pulled back from this morning's pre-market +3.23%, so the trailing-stop conversion does NOT fire yet. LLY −1.01% nowhere close. Carry the same watch into market-close: if NVDA tags +5%, cancel hard stop b55fb743 and place a 10% trailing stop GTC.
- **(c) Daily loss cap (−3% intraday)?** Equity $99,964.59 vs yesterday close $100,124.86 = **−0.16% intraday** — well inside the −3% cap. No new-buy restriction from this rule.
- Both −7% hard stops confirmed live and GTC (LLY 6c4d0225 @ 1002.57, NVDA b55fb743 @ 204.74).

### Portfolio watch
- **NVDA +2.28% (was +3.23% pre-mkt).** Gave back ~$2/sh intraday — normal noise, no headline driving it; AI-infra thesis unchanged from the 06:00 fan-out (Computex AI-PC push, Vera Rubin in production). No action.
- **LLY −1.01% (was −0.14% pre-mkt).** Modest intraday slide of ~$10/sh; GLP-1 thesis intact, no fresh negative catalyst. A slow compounder doing slow-compounder things. No action.

### New buys
None. Midday rule bars new buys absent a high-conviction breaking catalyst — none present. GOOGL remains the pre-market plan for the 3rd/final weekly buy (1 of 3 remaining), to be executed at a future routine if it opens/holds constructively; midday is not the venue to originate it without a catalyst.

### Benchmark (intraday)
- Portfolio −0.16% intraday vs **SPY +0.19%** (yest close 758.44 → 759.885). Trailing the market by ~0.35% on the day as NVDA cooled and LLY dipped.
- **Week-to-date (baseline Mon 6/1 $99,840.95):** portfolio +0.12% | SPY +0.47% (5/29 close 756.34 → 759.885) | **alpha −0.35% WTD.** Slipped behind this session; positions still only 2 days old — thesis needs time to express. Tracking, not alarming.

### Net
Steady, no changes. Stops live, no triggers hit, loss cap not breached, no catalyst to chase. Watch NVDA → +5% into the close.

---
## 2026-06-02 06:00 CT — pre-market

**Setup:** Memory synced from origin/main; keys all present; Alpaca reachable. Market CLOSED (next open 8:30 CT). Account: equity $100,211.56, cash $72,634.26, last_equity $100,124.86, daytrade_count 0. Positions: LLY 14 @ 1078.46 (mark 1077, −0.14%), NVDA 55 @ 220.15 (pre-mkt mark 227.26, **+3.23%**). Both −7% GTC hard stops confirmed live/working (LLY 6c4d0225 @ 1002.57, NVDA b55fb743 @ 204.74). Inbox: nothing pending. **No trades this routine — market closed.** 5-agent fan-out (macro, earnings, LLY, NVDA, scout).

### Market context
- **Futures (unconfirmed precision, Perplexity treats this date as near-future):** ES ~+0.3%, NQ ~+0.2%. Asia firmer (Nikkei +0.3–0.8%, HSI +0.5–1.0%); Europe slightly up (DAX/FTSE +0.1–0.6%).
- **Rates:** 10Y ~4.2–4.3%, biasing UP as markets pare Fed-cut bets — mild headwind, not a stop.
- **FX/commodities:** DXY ~104–105 firm; WTI ~$77–79 up modestly; gold softer on higher real yields.
- **SPY (Alpaca):** 758.65, +7.5% over ~50dMA (705.6), basically AT its ~120d high (760.26) — market at record highs.
- **Data this week (dates INFERRED, unconfirmed):** ISM Mfg (Mon), JOLTS (Tue), ISM Svcs + ADP (Wed), claims (Thu), **NFP Fri 6/5 = key event**. CPI/PCE later in month. → size any entry mindful of Friday's jobs print.
- **Risk read:** mildly risk-on / constructive. **Macro does NOT gate new buys today.**

### Portfolio watch
- **LLY — INTACT.** No 48h thesis-breaker. Recent confirms: retatrutide TRIUMPH-1 strong topline (ASCO ~5/29), Foundayo (oral orforglipron) gets CVS Caremark coverage from 6/1 — all 3 major PBMs now cover LLY's obesity portfolio. FDA proposing to drop tirzepatide/semaglutide from 503B list = tailwind (curbs compounded copycats). Watch: Medicare GLP-1 $50/mo bridge (from 7/1) boosts volume but compresses realized price (hits Novo too). No reason to sell/trim — day-2 hold.
- **NVDA — INTACT, strengthening.** Computex/GTC Taipei keynote (~6/1): NVDA entering Windows AI-PC market (RTX Spark + N1X with MediaTek; OEMs MSFT/Dell/HP/Lenovo) = TAM expansion; Vera Rubin in production, Blackwell Ultra ramping; hyperscaler capex intact. Export-control loophole closure noted as minimal demand impact (supply-constrained). **At +3.23%, ~$3.90 below the +5% (~$231.16) trailing-stop trigger** — a fresh positive narrative could push it through today. **Market-open task: if NVDA ≥ +5%, cancel −7% hard stop b55fb743 and place a 10% trailing stop (GTC).** No sell reason.

### Buy candidates (1 of 3 weekly buys remaining; 2 of 5 slots used; $72.6K cash)
Perplexity refused dated 6/2 earnings/upgrade data → signals #1/#4 UNVERIFIED, must confirm at open. Trend (#6) verified via Alpaca below.
- **GOOGL — LEAD CANDIDATE.** 367.94, +5.4% over ~50dMA (349), ~10% off ~120d-hi (408.57) = constructive uptrend, NOT parabolic, NOT a fresh low. Thesis: AI cloud + ad monetization + TPU buildout (secular #3) + clean uptrend (#6) = **2 signals, med conviction.** Adds AI exposure via a different vector than NVDA. No looming earnings coin-flip. Verify at open: holds constructive open; any recent upgrade would add #4.
- **MSFT — backup.** 456.42, +13% over 50dMA, −2% off 120d-hi (466.27). Strong uptrend near highs; secular #3 (Azure/Copilot) + #6. No near-term catalyst. Med conviction.
- **AVGO — PASS for now (earnings-risk rule).** 467.15, +20% over 50dMA, AT 120d-hi (466) = extended, and fiscal Q2 earnings ~6/3 = **within 3 trading days → strategy bars opening unless thesis depends on the print.** Revisit post-beat only.
- **PANW — conditional.** 300.5, near 120d-hi (302.87); cybersecurity secular #3; fiscal Q3 earnings "this month" — must confirm date isn't within 3 trading days before any entry.
- **DELL — WAIT/PASS.** 477.13, at/above 120d-hi (468.64) after the +30% earnings gap = extended. Don't chase; only revisit if it digests sideways / pulls back to gap-low on light volume.

### Sell candidates
None. Both holdings INTACT; neither near −7%; NVDA approaching (not at) +5% trailing trigger.

### Net / handoff to market-open
1. **Watch NVDA → +5% (~$231.16): convert to 10% trailing stop** if hit.
2. **GOOGL is the plan for the 3rd weekly buy** if it opens constructively (and ideally a per-ticker confirm of trend/any upgrade). Med conviction → ~12–15% size (~$12–15K), −7% hard stop via OTO order_class, GTC. AVGO excluded by earnings-risk rule; DELL still extended.
3. Mind **NFP Friday 6/5** — don't over-size into it.

---
## 2026-06-01 15:00 CT — market-close

### Day summary
- **Closing equity:** $100,128.53 (cash $72,634.26, ~72.5% buffer). Crossed back above $100K for the first time since the long flat stretch.
- **Day P/L:** +$287.58, **+0.29%** vs yesterday's close ($99,840.95, from account `last_equity`).
- **SPY day:** +0.28% (5/29 close 756.34 → 6/1 close 758.44; latest trade 758.42). **Alpha: +0.01%** — effectively matched the market on day 1.
- **Week-to-date (week started Mon 6/1):** portfolio +0.29%, SPY +0.28%, alpha +0.01%.
- **Trades placed today:** none at close. The two morning buys (LLY 14 @ 1078.46, NVDA 55 @ 220.15) and the midday GTC stop re-issue are already logged. Close routine = pure monitoring + reporting.

**What worked**
- NVDA (+1.94%, +$235) carried the day — the post-earnings re-entry above the 5/4 exit is behaving; AI-infra bid intact.
- Both GTC hard stops confirmed live/working at close, so the overnight-unprotected bug from this morning's OTO legs is fully closed out. Protection persists.

**What didn't / watch**
- LLY only +0.35% (+$52) — fine, it's a slow steady compounder, not a mover; no concern.
- Alpha is dead-even, not positive. Expected on day 1 with freshly opened positions, but the mandate is to *beat* SPY — the thesis needs a few sessions to express. Not a problem yet; flagging so it's tracked.

**Open questions for 6/2 pre-market**
- Deploy the 3rd (and final) weekly buy? Re-evaluate **DELL** post-gap (was +30% on the midday print — has it consolidated to a sane entry, or still extended?). Fresh watchlist seed: NVDA-adjacent (AVGO, GOOGL, MSFT, PLTR, NOW, CRWD, PANW) + DELL.
- Watch this week's inflation/jobs prints (dates still unconfirmed) — they could move the whole tape and gate new buys.
- Neither position near a +5% trailing-stop conversion yet; check again 6/2 — NVDA closest at +1.94%.

---
## 2026-06-01 10:46 CT — market-open (FRESH IN-RUN THESIS, traded)

**Context:** Woke to the cold-start scenario the new strategy rule was written for. The only "pre-market" entries in the log were the 4/22 HALTED no-ops (missing secrets) and the 4/21 NVDA scout — both stale by ~6 weeks. Book was 100% cash since the 5/4 NVDA trailing-stop exit (~18 trading days). Keys valid, market open (clock is_open=true, woke mid-session ~11:46 ET). Per the anti-paralysis rule: originated a fresh thesis this run with the sub-agent team and acted under normal guardrails. Account: $99,840.95 cash, 0 positions, 0 buys this week, daytrade_count 0, flat day (last_equity==equity → no daily-loss-cap block).

**Sub-agent fan-out (3 parallel):** macro + two opportunity scouts.
- **Macro:** neutral / mildly cautious. S&P near record highs (~7,230 area; SPY ~757, at/near 120d high, +7.5% over 50d MA). WTI up ~3% (growth optimism + Iran risk) = mild inflation overhang. 10Y elevated/biasing up (no exact tick). VIX contained but unconfirmed. Inflation/jobs prints this week (dates unconfirmed). Verdict: OK to open a high-conviction long, size conservatively, don't front-run the data.
- **Scouts:** Perplexity's index treats late-May/June 2026 as forward-dated and REFUSED to name dated earnings beats / fresh upgrades — so signals #1 and #4 are hard to verify from that source right now. Scouts surfaced a theme watchlist only: NVDA, AMD, MU, ETN, LLY, defense primes, etc. Lesson logged: for this date window, use Alpaca for hard facts (price/trend) + narrow per-ticker Perplexity for earnings dates; don't ask for "5 names from the future."

**My verification pass (Alpaca trend + per-ticker Perplexity):**
| Sym | Px | vs 50dMA | off 120d-hi | Read |
|---|---|---|---|---|
| NVDA | 220 | +5.9% | −10.4% | clean healthy uptrend, not extended |
| AMD | 513 | +57% | −0.4% | PARABOLIC — chase risk, pass |
| MU | 1032 | +74% | 0% | PARABOLIC at highs — pass |
| ETN | 399 | +1.8% | −7.5% | mild/consolidating; no fresh catalyst → pass (don't force) |
| LLY | 1078 | +15.8% | −1.9% | strong steady uptrend |

Per-ticker Perplexity confirmed:
- **LLY** — Q1 2026 (rel 4/30): non-GAAP EPS $8.55 vs ~$6.97, rev $19.8B +56% YoY, **raised FY26 guidance** ($82–85B rev, $35.50–37.00 EPS). **FDA approval of Foundayo/orforglipron** (oral GLP-1, obesity). Next earnings ~Aug 5 (est) → no blackout. Signals #1+#2+#3+#6. **High conviction.**
- **NVDA** — Q1 FY27 (rel 5/20): EPS $1.87 vs $1.76, record rev $81.6B, "Beat." Guidance-raise not explicitly confirmed. Next earnings ~Aug 26 → no blackout. Signals #3+#6 (+#1 borderline-recent). **Medium conviction.** Re-entry above the 5/4 exit; thesis never broke (prior exit was a trailing-stop pullback).
- **ETN** — Q1 (5/5) beat (adj EPS $2.81 vs $2.73), next ~Aug 4. Only #3 + a weak #6. No fresh catalyst. **Passed.**

**Decision / sizing (conservative re-entry on a cautious-macro day, 1 buy kept in reserve):**
- LLY 14 sh @ 1078.46 = $15,098.44 (15.1%), stop $1002.57. High conviction → ~target 15%.
- NVDA 55 sh @ 220.15 = $12,108.25 (12.1%), stop $204.74. Medium → ~12%.
- Total deployed ~$27.2K (27%); cash buffer ~73%. 2 of 5 positions, 2 of 3 weekly buys used.

**Execution note (infra):** paper API rejects `bracket` without `take_profit.limit_price`. Strategy = no take-profit (trailing stop handles upside). Used **OTO** order_class (market buy triggers single stop-loss leg) — exact behavior we want. Update scripts/alpaca.md cheat-sheet to reflect OTO-for-no-TP. Both filled at/near pre-fill price; both −7% stop legs live (status new/working).

**Why not deploy harder:** anti-paralysis rule says find qualifying setups (done) but explicitly ≠ force trades. Macro is neutral-to-cautious with unconfirmed inflation/jobs prints this week; this is the first re-entry after a long flat stretch. Two genuine high-quality names now + a 3rd buy in reserve for midday/close or a pullback is the disciplined middle path. Cash-drag broken honestly, not recklessly.


## 2026-06-01 12:00 CT — midday

### State on wake
- **First live routine after the 6/1 memory-persistence repair.** Keys all present, memory synced from `origin/main`, Alpaca reachable.
- **Account verified flat:** $99,840.95 equity, $99,840.95 cash, **0 positions** (Alpaca `/v2/account` + `/v2/positions` both confirm). Market open (`is_open: true`, next_close 6/1 16:00 ET).
- Inbox: nothing pending.
- **No fresh pre-market thesis exists for today** — last real research-log entry predates the repair (4/21–4/22). The 4/22 entries are HALT notes (missing keys), not tradeable plans.

### Portfolio watch
No open positions → no -7% stops to action, no +5% winners to convert to trailing stops, nothing to sell. Risk-management pass is a no-op by construction.

### Daily loss cap
N/A — flat book, and the tape is **up** today anyway. Perplexity: SPY **~+0.6% intraday** vs Friday's close (risk-on; oil lower, yields softer, AI/tech leading). No drawdown, no buy-block triggered.

### Cash-drag flag (per cold-start rule)
**Book has been 100% cash since the 5/4 NVDA exit — ~18 trading days.** This is exactly the condition the 6/1 rule says to escalate. Root cause (memory never persisting) is now fixed, so this should not recur. Per the rule, **finding a qualifying 2-signal setup is the priority — but that work belongs to a scan routine, not midday.**

### Midday buy decision
Midday rule: **no new buys unless a high-conviction *breaking* catalyst** AND buys-this-week < 3 AND positions < 5 (caps are fine: 0/3 buys, 0/5 positions).

Single breaking catalyst surfaced: **DELL +30%+** post-earnings on a beat + raised guidance (AI-server demand). Clears signal #1 (earnings beat + raised guidance) and arguably #3 (AI-infra tailwind) = 2 signals.

**Decision: DO NOT chase DELL at midday.** A +30% post-earnings gap is an extended entry — buying here puts the −7% hard stop squarely inside normal post-gap volatility (a routine gap-fill whipsaws us out at a loss). Strategy's "we don't catch knives" logic cuts both ways: don't chase blow-off gaps either. This is FOMO, not a disciplined swing entry. **Queued for tomorrow's pre-market** to evaluate a proper entry once the gap settles / consolidates.

### Sell candidates
None — no positions.

### Net / handoff to 6/2 pre-market
- No trades, no stop changes this midday (nothing to manage on a flat book).
- **Priority for 6/2 pre-market:** run the full sub-agent scan and actually deploy capital if a name clears 2 signals — 18 days of cash drag against a rising SPY is the real cost here. Re-evaluate DELL post-gap; build a fresh watchlist (seed: NVDA, AVGO, GOOGL, MSFT, PLTR, LLY, NOW, CRWD, PANW, plus DELL).

---

## 2026-04-22 12:00 CT — midday (HALTED)

### Halt reason
Same as this morning's market-open: `ALPACA_API_KEY`, `ALPACA_SECRET_KEY`, `ALPACA_BASE_URL`, `PERPLEXITY_API_KEY` all empty and no `./.env`. Per CLAUDE.md guardrail, halted before any API call.

### No actions taken
- No Alpaca calls (positions, prices, orders, stop-management).
- No Perplexity news-check on any drawdown (there's no live positions data to know if there's a drawdown anyway).
- No new buys (moot — can't confirm price, daily-loss cap, or position count without Alpaca).
- Portfolio unchanged: assumed still $100K cash / 0 positions from 2026-04-21 19:00 CT.

### Pattern note
Second halt in a row (market-open 08:30 also halted for the same reason). If this keeps up through market-close, the whole 4/22 session is a no-op — fine, since we have no open risk, but the user needs to restore secrets before any routine can actually trade.

### Next steps
Once secrets are set: run a fresh pre-market-style scout before executing the old NVDA starter plan. Don't trade off last night's context — tape will have moved.

---

## 2026-04-22 08:30 CT — market-open (HALTED)

### Halt reason
Required env vars missing: `ALPACA_API_KEY`, `ALPACA_SECRET_KEY`, `ALPACA_BASE_URL`, `PERPLEXITY_API_KEY`. No `./.env` file and no env vars set in the cloud environment. Per CLAUDE.md guardrail ("If a required var is empty, halt, write a clear error to `memory/messages.md`, and stop"), aborted before any API call.

### No actions taken
- No Alpaca calls (clock, account, positions, orders).
- No Perplexity calls.
- Portfolio snapshot unchanged (no live data to refresh it with). Paper account assumed still $100K cash / 0 positions from last known state.
- Planned NVDA starter ($5K) from last night's scout re-run is deferred — will need a fresh pre-market re-validation once secrets are back, since "if futures risk-off, pass" was part of the plan and we have no way to check futures from this routine.

### Next steps
Once secrets are set, the next routine (midday-check or next pre-market) should re-scout — don't blindly execute last night's NVDA plan on stale context.

---

## 2026-04-21 19:00 CT — pre-market (for 2026-04-22 open) — re-run

**Timing note:** Second pass for the Wed 4/22 open, after the 17:00 CT pass flagged too many `n/a`s to act on. APIs verified live (Alpaca 200, Perplexity 200). Three sub-agents fanned out in parallel — macro, earnings, opportunity scout. Account unchanged: $100K cash, 0 positions.

### Market context
Tape shifted **mildly risk-off** vs the earlier bullish futures read.
- **ES (Jun'26):** ~7,165.75, **−0.13%** evening session (was ~+0.35% at 17:00 CT — faded).
- **NQ (Jun'26):** ~flat to +0.05% evening.
- **US 10Y Treasury:** 4.294%, **+4.4 bps** on the day (range 4.236 – 4.319). Bonds sold off.
- **Crude:** direction up on "Iran concerns" headlines; WTI/Brent exact levels `n/a`.
- **DXY, Nikkei, Hang Seng, European closes:** `n/a` — Perplexity sparse on these; not actionable.
- **Headline flow:** Iran/Middle East risk premium flipped the intraday tone — early equity gains erased, crude spiked, rates up. No Fed speaker, CPI/PPI, or tariff print surfaced in this window.
- **Net:** mildly risk-off. Iran/oil is the live wire. Secondary watch: does 10Y hold above 4.30% at Wed open.

### Portfolio watch
No open positions. $100K cash, $200K buying power (cash-only / no leverage per strategy).

### Earnings calendar (2026-04-22)
Contradicts the 17:00 CT pass — worth flagging.
- **Fresh Perplexity (sonar-pro) returned no confirmed $10B+ US earnings for 4/22, BMO or AMC.** Names that *may* report BMO per an Interactive Investor preview dated 4/17 (unconfirmed for 4/22 specifically): **MMM, GE, UNH, EL, XOM, MRNA**. Consensus EPS/rev not supplied.
- **TSLA AMC 4/22** was asserted in the 17:00 CT pass but was NOT confirmed in tonight's fresh pull. Source contradiction — do not treat TSLA as a confirmed tape-setter until verified tomorrow morning.
- **4/21 AMC mega-cap prints (MSFT / GOOGL / META / AMZN / NVDA):** none reported per tonight's pull.
- **Guidance-risk call:** low-conviction — with no confirmed mega-cap print, Wednesday is more likely to be macro-driven (Iran / rates) than earnings-driven.

### Buy candidates

Scout verified next-earnings dates on 3 of 10 seed names; the rest came back `n/a` on critical fields — strategy says do not propose without verification. Documenting honestly.

- **NVDA — AI-infra leader, clean earnings runway.** Signals: (3) secular AI-infra tailwind (Blackwell ramp, cap-ex cycle). Next earnings **2026-05-20 AMC (confirmed)** — ~21 trading days out, outside the 3-day blackout. **Conviction: med.** Only 1 hard signal verified tonight; the earnings date is inbound catalyst but not near-term. Prefer a pullback entry; do not chase.
- **AVGO — AI ASIC/networking play, widest earnings window.** Signals: (3) custom-silicon + VMware AI tailwind. Next earnings **2026-06-03 (confirmed)** — 6+ weeks out. **Conviction: low–med.** Single verified signal; would upgrade with a verified upgrade or insider-buy tomorrow.
- **PLTR — AI/defense software, earnings in 9 trading days.** Signals: (3) AI + gov tailwind. Next earnings **2026-05-04 AMC (confirmed)** — 9 trading days out (clear of 3-day blackout but close). **Conviction: low.** High multiple risk into the print; any entry now must be size-to-trim-before-5/1 OR hold-through willingness.
- **GOOGL, MSFT, CRWD, PANW, BE, LLY, NOW** — earnings dates and fresh catalysts unverified in tonight's 3 Perplexity calls. **MSFT and GOOGL historically print late April** — treat as likely inside/adjacent 3-day blackout until a date is confirmed. **Do not open GOOGL or MSFT at Wed open without an explicit earnings-date check.**

**Net:** no clean ≥2-signal-verified buy tonight. **NVDA is the only name with verified runway + a real tailwind.** Strategy explicitly prefers patience; recommend at most a **starter tranche (1/3 of target size, ~5% of portfolio ≈ $5K)** in NVDA at Wed open IF macro tone is constructive, and re-run the scout after tomorrow night's close with a better-pulled watchlist. If pre-open futures are still risk-off (ES < flat, 10Y > 4.30, WTI gapped up), **pass entirely.**

### Sell candidates
None — no positions.

### Notes / research gaps to close next routine
1. Verify TSLA 4/22 AMC print — source contradiction between 17:00 and 19:00 CT passes.
2. Pull MSFT and GOOGL next-earnings dates explicitly (likely inside late-April blackout window).
3. Get WTI/Brent cash levels and DXY at open — macro still has too many `n/a`s to size rate-sensitive names.
4. Perplexity sonar-pro with low search context was thin tonight. Consider raising context size for the scout call (`search_context_size: "medium"`) if budget allows — but batch tickers to keep the call count down.

---

## 2026-04-21 17:00 CT — pre-market (for 2026-04-22 open)

**Timing note:** Routine fired ad-hoc, not at scheduled 6:00 AM CT slot. Alpaca clock confirms market closed; next_open = 2026-04-22 09:30 ET. Treating this as pre-market prep for Wednesday's session. Account is fresh ($100K cash, no positions) — this is Bull's first research pass.

### Market context
Mildly **risk-on** into Wed 4/22 open, low conviction.
- **ES ~+0.35%, NQ ~+0.05 to +0.40%** late Tuesday (E-mini S&P/Nasdaq). Earlier-session weakness (-0.4%) faded on Mid-East peace-deal progress headlines.
- **Dominant narrative:** US–Iran / Middle East de-escalation hopes lifting futures. Oil moves are the swing factor — a re-spike would flip sentiment to mixed.
- **Data gaps:** Perplexity returned n/a for 10Y yield, DXY, WTI/Brent levels, and Asia/Europe indices. Not confident on rate direction — avoid sizing up rate-sensitive names until a fresh cash-session print.
- No Fed commentary, CPI/PPI, tariff, or mega-cap earnings surprise surfaced since Tuesday's close.

### Portfolio watch
No open positions. Nothing to watch. $100K cash, $200K buying power (2× margin, but strategy is cash-only / no leverage).

### Earnings calendar (2026-04-22)
- **BMO:** BSX (Boston Scientific) — consensus EPS ~$0.555. Watch Farapulse / PFA adoption, Watchman utilization, hospital capex commentary. Med-tech tone-setter.
- **AMC:** TSLA — consensus EPS ~$2.61, revenue ~$10.81B (directional — source numbers were noisy). Key watches: auto gross margin ex-credits, delivery trajectory, Optimus / FSD / robotaxi commentary, AI infra capex. Biggest single tape-setter for Thursday sentiment.
- **Calendar unconfirmed:** IBM, T, NOW, CMG, LRCX, GD are commonly on this slate historically — sub-agent could not verify. Cross-reference needed before treating as tradeable.
- **Post-close 4/21 reports:** data thin; no confirmed mega-cap AMC prints to front-run tomorrow.

### Buy candidates

Research pass was sparse — two Perplexity calls yielded only one fully specified candidate, and that one is blocked by strategy rules. Documenting the state honestly rather than forcing low-conviction picks.

- **AMZN (~$205, ~$2.2T mcap)** — Signals hit: (3) secular AI/AWS tailwind; partial (1) Q4 beat with AWS +24% YoY. Next earnings ~2026-04-30. **EXCLUDED** — inside the 3-trading-day earnings window per strategy rule. Revisit post-print on May 1.
- **BE (Bloom Energy)** — Signals (6) strong uptrend, (3) fuel-cells-for-AI-data-center narrative. Earnings date unverified. **LOW/MED conviction**, catalyst is generic. Needs a verified earnings date and a specific near-term catalyst (contract announcement, capacity expansion) before entering.
- **CAR (Avis)** — Up ~+382% in 30 days per scout. **SKIP.** Momentum-alone, no catalyst, smells short-squeeze / meme-adjacent. Strategy explicitly forbids.
- **NVDA, AVGO, PLTR, GOOGL, CRWD, PANW** — scout returned n/a on critical fields (catalysts, earnings dates, current price confirms). Insufficient to propose. Next pre-market routine should pull NVDA/AVGO earnings dates directly from Alpaca and query Perplexity more narrowly.

**Net:** no high-conviction buy for 4/22 open from this scan. Better to wait and do a better-focused scan tomorrow than to force a mediocre entry on Bull's first trade.

### Sell candidates
None — no positions.

### Notes / research gaps to close next routine
1. Get actual 10Y yield, DXY, WTI, Brent levels at open — macro digest had too many n/a's.
2. Pull next-earnings dates directly from Alpaca calendar API before asking Perplexity for thesis — avoids wasting calls.
3. Build a small seed watchlist (NVDA, AVGO, GOOGL, MSFT, PLTR, CRWD, PANW, BE, LLY, NOW) so the opportunity scout has a concrete set to research rather than fishing open-universe.

---

## 2026-06-01 12:00 CT — midday

**APIs live** (Alpaca account/positions/orders 200, market data 200). First midday running off correctly-persisted live memory. Market open (next_close 16:00 ET).

### Live account snapshot
- Equity **$99,889.97**, cash **$72,634.26**, last_equity (5/29 close) $99,840.95 → **day P/L +$49.02 (+0.05%)**.
- Positions (2 of 5):
  - **LLY** 14 @ 1078.46, current 1074.89 → −$49.98 (**−0.33%**). lastday 1105, change_today −2.7%.
  - **NVDA** 55 @ 220.15, current 221.95 → +$99.00 (**+0.82%**). lastday 211.14, change_today +5.1%.
- daytrade_count 2 (not PDT; no day trades initiated by us — these are the broker's count from the round-trips, watch it).

### Risk management (priority order)
- **(a) −7% drawdown check:** neither position near −7% (worst is LLY −0.33%). No Perplexity news-check needed, no sells.
- **(b) +5% profit → trailing stop:** NVDA +0.82%, LLY −0.33%; neither at +5%. No conversion to trailing stop yet. (Watch NVDA — closest.)
- **(c) Daily loss cap:** portfolio +0.05% intraday, nowhere near −3%. Cap NOT triggered. (Moot anyway — no buys planned.)

### Stop-protection gap found + fixed (the real action of this run)
Open-orders pull showed both OTO stop legs were `time_in_force: day`, `expires_at 2026-06-01T20:00:00Z` — i.e. they would **expire at today's market close**, leaving LLY and NVDA with **no stop overnight**. That silently voids the −7% hard-stop guardrail. Root cause: an OTO stop leg inherits the parent market buy's TIF (day). Fix:
1. Cancelled LLY day-stop 7748b65e (204), NVDA day-stop e2c1f2bb (204). Confirmed open orders empty, qty_available restored (14 / 55).
2. Placed GTC stops at identical −7% prices: LLY 6c4d0225 @ 1002.57, NVDA b55fb743 @ 204.74. Confirmed both `tif=gtc`, expires 2026-08-28 (quarterly GTC horizon).
**Forward fix for entries:** market-open/pre-market buy logic should place the protective stop as a standalone GTC order (or convert same-day), not rely on the OTO day leg. Flagging for the next entry routine; not a strategy-rule change, so not escalating to a weekly-review item unless it recurs.

### New buys
None. Midday rule: no new buys unless a high-conviction breaking catalyst AND buys-this-week < 3 AND positions < 5. No qualifying breaking catalyst surfaced; also buys-this-week = 2 of 3 (LLY+NVDA filled today). Held.

### Benchmark (informational, full compare at close)
- SPY: 5/29 close 756.34 → now 757.71 (**+0.18%** today). Portfolio +0.05% → trailing by ~0.13% intraday — noise on day one of exposure.

### Next watch
- NVDA toward +5% ($231.16) → convert −7% hard stop to 10% trailing stop.
- LLY: nothing fundamental; −2.7% on the day is sector/tape noise, thesis (raised guidance + orforglipron + GLP-1 tailwind) intact. No news-check warranted at −0.33%.
- Close routine: full SPY alpha compare; confirm GTC stops still resting.
