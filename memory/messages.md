# Messages from Bull

Append-only conversation log. **Most recent at the top.** Each entry is what Bull wants the user to see from a routine run.

Format:

```
## YYYY-MM-DD HH:MM CT · {routine name}

**Headline one-liner**

Body — short paragraph or bullets. What happened, what Bull decided, anything the user should know or decide on.
```

---

## 2026-05-19 06:00 CT · pre-market

**We're back online — and I've got a 3-stock starter plan ready for the open.**

**What I did**
The API keys are back, so the long halt is over. I scanned the tape with my research team (a macro analyst, an earnings analyst, and an opportunity scout, all running in parallel) and built a plan for today's market open. No trades placed yet — the market is still closed. Opens in about 2.5 hours.

**Why**
While we were dark, SPY (the S&P 500 ETF — our benchmark) climbed about +4.9%, so we have ground to make up. Good news: earnings season has been the strongest since 2021 (companies beating profit estimates by a wide margin), which gives us a constructive backdrop. The slight headwind today is the 10-year Treasury yield at 4.63% (a 15-month high — when bond yields rise, growth stocks feel pressure), and tech has been soft for two sessions. So I want to deploy carefully and diversified, not all-in on tech.

**The plan at the open**: three "starter" positions, about 12% of the account each, with automatic -7% stop-losses (a safety-net order that sells if the stock drops 7%):
1. **PLTR (Palantir)** — AI/defense software, just beat earnings AND raised their full-year forecast on 5/4.
2. **LLY (Eli Lilly)** — GLP-1 obesity drugs, also beat-and-raised, strong uptrend.
3. **GE (GE Aerospace)** — aerospace/defense industrial, beat-and-raised — gives us non-tech sector diversification.

I'm **avoiding NVDA and PANW** even though they're tempting — both report earnings in the next 2 days, and our rules say no buying within 3 trading days of a print (too risky — the report can swing the stock 10%+ in either direction).

**What happens next**
At 8:30 CT (market open) I'll check futures one more time. If they hold or rally, I execute all three. If they gap down hard (>0.75%) or yields spike past 4.70%, I cut back to just PLTR and reassess at midday. NVDA reports tomorrow night — that'll set the AI tape for the week, and I'll react to it Thursday morning.

**Numbers I care about**
- Equity: $99,841 (a tiny $159 below our $100K start — paper-account drift, nothing real)
- Plan: ~$36K to be deployed today (3 × ~$12K), leaving ~$64K cash (~64%) for opportunistic adds later this week
- Buy capacity used: **0 of 3 this week** before the open (will be 3 of 3 after if all execute)
- SPY benchmark: $738.65 — we're starting +4.9% behind it; the only number that matters long-term is whether we close that gap and pass it

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
