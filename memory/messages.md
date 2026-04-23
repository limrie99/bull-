# Messages from Bull

Append-only conversation log. **Most recent at the top.** Each entry is what Bull wants the user to see from a routine run.

Format:

```
## YYYY-MM-DD HH:MM CT · {routine name}

**Headline one-liner**

Body — short paragraph or bullets. What happened, what Bull decided, anything the user should know or decide on.
```

---

## 2026-04-23 15:00 CT · market-close

**Close: equity $99,949 · day -0.08% · SPY -0.39% · alpha +0.31%**

**What I did**
No new trades today. Our one position (25 shares of NVIDIA, ticker NVDA) sat in the account all day, and the "hard stop" (an automatic sell order that kicks in if the price drops 7% from where we bought — our safety net) stayed parked at $187.28, well below today's price. I watched, I reviewed, I didn't churn.

**Why**
The broad market had a red day — SPY (the ETF that tracks the whole S&P 500 index, basically "the market") fell -0.39%. NVDA fell a bit more (-1.56%), but because we're only **5% invested** — most of the account is still cash — the portfolio only dropped -0.08%. That's the **alpha (extra return vs. just owning the market)** our position sizing bought us today: +0.31 percentage points of outperformance, purely from being small while things were ugly.

**What happens next**
Tomorrow I'll look for a *second* conviction name to add — something with a confirmed near-term catalyst (an upcoming earnings beat, a product launch, etc.) and clean fundamentals. $95K in cash is a lot of dry powder to have on a day the market went on sale, so I want to be ready to deploy a chunk of it if a clean setup shows up.

**Numbers I care about**
- Equity: **$99,949** — down just **$79** from yesterday's $100,028 close, basically flat.
- NVDA: -$51 unrealized (-1% from where we bought), stop parked at $187.28 (far below today's $199.35 price — no danger).
- Cash: **$94,966** — about 95% of the account is still in cash, i.e., under-deployed. Goal next week: get to 2–3 positions.

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
