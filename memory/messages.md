# Messages from Bull

Append-only conversation log. **Most recent at the top.** Each entry is what Bull wants the user to see from a routine run.

Format:

```
## YYYY-MM-DD HH:MM CT · {routine name}

**Headline one-liner**

Body — short paragraph or bullets. What happened, what Bull decided, anything the user should know or decide on.
```

---

## 2026-05-15 16:00 CT · weekly-review

**Week ending 2026-05-15: portfolio 0.00% | SPY +0.35% | alpha −0.35% | grade F**

**What I did**
The weekly review is a Friday-afternoon honest look at how we did versus the S&P 500 (SPY — that's the ticker for an exchange-traded fund that tracks the 500 biggest US companies, our benchmark). The verdict is uncomfortable: we placed zero trades this week, and the trade log shows we've placed zero trades since the account opened on April 21. The market drifted up about a third of a percent; we sat in cash and earned nothing.

**Why this happened**
Back on April 22 the routine halted because the API keys were missing from the environment. After that, the record goes dark — no research notes, no trades, no messages — for about three weeks. The plumbing is now working (I just confirmed Alpaca and the market data feeds end-to-end), but we lost three weeks of "at-bats." This was an *operational* failure, not a strategy failure, so I am **not** changing the strategy in response. One bad week is noise; tweaking the playbook now would be exactly the kind of overreaction we want to avoid.

**What happens next**
Monday pre-market I'll run a full fresh scout — a new earnings calendar (NVDA's May 20 print now falls inside our 3-day "earnings blackout" rule, so it's off the table for a fresh entry), a new macro read, and a real seed watchlist. The first successful trade next week will also be a litmus test that the routine-to-log-to-dashboard pipeline is actually writing things down.

**Numbers I care about**
- Equity: $99,840.95 (down $159 from the $100,000 we started with on 4/21 — about a sixth of a percent, immaterial in dollars but symbolically bad)
- Cash: $99,840.95 (100% cash — no risk on the book, but also no upside)
- This week vs SPY: we lagged by 0.35% — small, but it's the *only* number that matters long-term

**Grade: F.** Doing nothing while the benchmark went up is the worst outcome for a fund whose mandate is "beat SPY." Plan for next week is in the weekly review file (`memory/weekly-review.md`) if you want the full breakdown.

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
