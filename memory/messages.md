# Messages from Bull

Append-only conversation log. **Most recent at the top.** Each entry is what Bull wants the user to see from a routine run.

Format:

```
## YYYY-MM-DD HH:MM CT · {routine name}

**Headline one-liner**

Body — short paragraph or bullets. What happened, what Bull decided, anything the user should know or decide on.
```

---

## 2026-05-01 16:00 CT · weekly-review

**Week ending 2026-05-01: -0.25% | SPY +0.91% | alpha -1.16% | grade D**

**What happened this week**
We owned one position (NVDA, 25 shares bought 4/22 at $201.38) and rode it through a wild round-trip — up to +7.7% on Monday, then back down to -1.5% by Friday. Zero new trades this week. The only "action" was a strategy-correct stop adjustment on Monday (more on that below). The S&P 500 — that's the index of the 500 biggest US companies, the benchmark we compare ourselves against — rose +0.91%. We sat in cash through most of that, so we missed the rally.

**The good**
- Our risk-management rule worked exactly as designed. When NVDA crossed +5% in profit on Monday, I canceled the original "hard stop" (a fixed sell-trigger at -7% from entry) and replaced it with a "trailing stop" — that's a sell-trigger that follows the price up but never down, so profits get protected automatically. NVDA's high was $216.73, which set our trailing floor at $195.06. When NVDA later crashed -4.7% on Thursday, our floor held — the position breathed but didn't get stopped out. That's the v1 lesson playing out in real time.

**The not-so-good (the real lesson)**
- We were ~95% in cash all week. Strategy says we should run 10–20% cash and 80–90% deployed. SPY rallied; we didn't participate. The starter NVDA position alone wasn't enough to keep up.
- Even worse: my own scout and midday routines didn't run Mon–Thu. There are zero new research entries for the week, which means I never sourced a second name to add. A starter position is meant to be the start, not the whole trade.

**No strategy changes this week.** One bad week is noise, not a pattern — bending rules off one underperforming week is exactly the over-reaction the playbook warns against. The real fix is operational: get the routines running again and source new candidates.

**Numbers**
- Equity: $99,924 (down $76 on the week, -0.25%)
- Cash: $94,966 (we still have ~95% of the account ready to deploy)
- SPY beat us by 1.16% — that's our "alpha" for the week, and it's negative. The only number that matters long-term.
- 1 of 5 max positions filled. 0 of 3 weekly buys used.

**What I'm watching next week**
Get a pre-market scout running Monday morning with verified earnings dates and look for a second 5–10% position to add if signals confirm. NVDA's own earnings are 5/20 — 13 trading days out — so I'll need to decide by mid-May whether we hold through the print, trim, or close before. Trailing stop on NVDA stays at $195.06 in the meantime.

---

## 2026-04-22 12:00 CT · midday

**Still halted — API keys still missing (second routine in a row).**

- No `.env` and no `ALPACA_*` / `PERPLEXITY_API_KEY` in the process env. Same halt as this morning's market-open routine (08:30 CT).
- Can't read positions/prices from Alpaca → no risk-management pass. Can't hit Perplexity → no news check.
- No trades, no stop changes, no state changes. Portfolio still $100K cash / 0 positions, so nothing is silently bleeding — but also no one is watching the tape.
- **Action for user:** set the four required vars (in `./.env` locally or in the cloud runner's env) before the next routine. Every routine will keep halting the same way until they're restored.

---

## 2026-04-22 08:30 CT · market-open

**Halted — required API keys missing from environment.**

- No `.env` file present, and `ALPACA_API_KEY`, `ALPACA_SECRET_KEY`, `ALPACA_BASE_URL`, `PERPLEXITY_API_KEY` are all empty in the environment.
- Per CLAUDE.md guardrails, I cannot call Alpaca or Perplexity without these — skipping all trading actions for this routine.
- No orders placed, no positions changed. Paper portfolio still $100K cash, 0 positions.
- **Action needed:** set the four env vars (either in `./.env` locally or in the cloud environment) before the next routine wakes up, otherwise every routine will halt the same way.

---

## 2026-04-21 19:00 CT · pre-market (re-run, for 4/22)

**Tape flipped mildly risk-off — NVDA is the only clean setup; leaning pass or small starter.**

- Futures faded: **ES −0.13%, NQ flat** evening. **10Y +4bps to 4.29%.** Crude up on Iran headlines (levels `n/a`). Wednesday looks macro-driven, not earnings-driven.
- **No confirmed mega-cap earnings for 4/22** in fresh pull — contradicts the earlier TSLA AMC read. Re-verify tomorrow morning before treating TSLA as a tape-setter.
- **Scout top pick: NVDA** (next earnings 5/20, ~21 days out, AI-infra tailwind). Conviction **med**. AVGO / PLTR flagged low-med; **GOOGL and MSFT NOT safe to open** without verified earnings dates (historical late-April print risk).
- **Plan for Wed open:** if futures still risk-off at 6 AM CT scan, **pass entirely**. If constructive, enter a **starter ~5% NVDA tranche ($5K)** with the −7% hard stop, and re-run scout tomorrow night.

---

## 2026-04-21 17:00 CT · pre-market (for 4/22)

**First research pass — no high-conviction buy ideas yet; saving cash for a better scan.**

- Fresh paper account confirmed: $100K cash, 0 positions.
- Setup into Wed 4/22: mildly risk-on on Mid-East de-escalation hopes (ES ~+0.35%). TSLA reports AMC 4/22 — biggest tape-setter.
- Scout found no name that cleanly hits ≥2 signals with a verified near-term catalyst. AMZN thesis is real but inside the 3-day earnings window; skipping.
- Next pre-market (6 AM CT 4/22): tighter scan on a seed watchlist (NVDA, AVGO, GOOGL, PLTR, CRWD, PANW) with earnings dates pulled from Alpaca first.

---

(earlier messages below)
