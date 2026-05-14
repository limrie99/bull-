# Messages from Bull

Append-only conversation log. **Most recent at the top.** Each entry is what Bull wants the user to see from a routine run.

Format:

```
## YYYY-MM-DD HH:MM CT · {routine name}

**Headline one-liner**

Body — short paragraph or bullets. What happened, what Bull decided, anything the user should know or decide on.
```

---

## 2026-05-14 08:34 CT · market-open

**Open: no trades — we're back online but I don't have a fresh plan to act on.**

**What I did**
The market opened a few minutes ago and my API keys are working again — first time since 4/22. I pulled our account from Alpaca to confirm where we stand: **$99,840.95 in cash, zero positions open.** No buys, no sells.

**Why**
This is the right call, even though it might feel slow. Three weeks of routines halted because the keys were missing, so I have **no pre-market research from today** — and my rule is to never open a position without a verified plan (at least 2 of our 6 buy signals confirmed, an earnings/catalyst check, and a macro read). Acting on stale 4/22 notes (a half-baked NVDA starter idea) on today's tape would be guessing, not investing. The S&P 500 ("SPY," the index that tracks the 500 biggest US companies and our benchmark) is up about +1% this week to $744 — constructive, but I want fresh eyes before deploying cash.

**What happens next**
My next scheduled wake-up is the midday check around 12:00 CT — I'll re-scan then. The most useful run will be **tonight's pre-market routine**, where I'll spin up my sub-agents (one per ticker, one for macro, one for sector rotation) and rebuild the watchlist from scratch. Expect a real buy plan in tomorrow's open if anything clears the bar.

**Numbers I care about**
- $99,840.95 cash — basically untouched (about $159 of paper drift vs. the $100K seed; no trades on record to explain it, so I've flagged it but I'm not chasing it).
- 0 of 3 buys used this week. 0 of 5 position slots filled. Full powder, full optionality.
- SPY $744.66, +0.32% so far today, +0.97% this week — the market we're trying to beat.

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
