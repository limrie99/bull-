# Messages from Bull

Append-only conversation log. **Most recent at the top.** Each entry is what Bull wants the user to see from a routine run.

Format:

```
## YYYY-MM-DD HH:MM CT · {routine name}

**Headline one-liner**

Body — short paragraph or bullets. What happened, what Bull decided, anything the user should know or decide on.
```

---

## 2026-06-01 06:00 CT · pre-market

**Good morning — quiet open expected. I'm sitting on cash and waiting for a cleaner setup.**

**What I did**
I ran our overnight macro, earnings, and opportunity scans (three sub-advisors in parallel). No trades — pre-market routines never trade; we just prepare. Account is still fully in cash at **$99,840.95** (essentially the full $100K), zero positions.

**Why**
Three things shaped my plan. **One:** today is an earnings-free day for the big names — Monday after Memorial Day weekend, calendar is empty. **Two:** Wednesday evening is huge — Broadcom (AVGO) reports, and "readthrough" (what one company's results tell us about its peers) means the whole AI-chip group will be jumpy through then. I don't want to buy an AI name on Monday and watch it chop sideways for two days waiting on AVGO. **Three:** April PCE inflation came in hot at 3.8% (the Fed's preferred inflation gauge — higher = Fed stays tighter for longer), which makes pricey high-multiple stocks vulnerable today even as the broader tape leans up on Iran-ceasefire hopes.

Our playbook needs **at least two confirmed buy signals** before I enter (earnings beat + raised guidance, analyst upgrade, insider buying, secular tailwind, sector rotation, clear uptrend). Honest read: nothing cleared two signals this morning. Patience beats forcing a mediocre first trade.

**What happens next**
At 8:30 AM CT (market open) I'll re-scan with fresh quotes and look for any overnight news on **NVDA ($212), GOOGL ($381), MSFT ($448), LLY ($1,105)** — those four are blackout-safe (no earnings inside 3 trading days) and each has a real secular tailwind, just no second signal yet. **AVGO, PANW, CRWD are off-limits this week** because they report in the next 3 days — strategy rule. I'll also watch the **ISM Manufacturing** print today (a survey of factory bosses — strong = bond yields up = high-multiple tech down).

**Numbers I care about**
- Cash: **$99,840.95** (~100% — full dry powder, nothing at risk)
- Positions open: 0 of 5 max · Buys used this week: 0 of 3 max
- Benchmark check: SPY closed Friday at **$755.95** — that's what we're trying to beat

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
