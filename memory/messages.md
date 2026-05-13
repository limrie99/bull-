# Messages from Bull

Append-only conversation log. **Most recent at the top.** Each entry is what Bull wants the user to see from a routine run.

Format:

```
## YYYY-MM-DD HH:MM CT · {routine name}

**Headline one-liner**

Body — short paragraph or bullets. What happened, what Bull decided, anything the user should know or decide on.
```

---

## 2026-05-13 08:36 CT · market-open

**Open: no trades — and I need to flag something I just discovered about an old NVDA trade.**

**What I did**
I woke up at the open, pulled our account from Alpaca, and the first thing I noticed is that our cash is $99,840.95 — not the $100,000 we started with. That sent me digging through Alpaca's order history, and I found a NVDA round-trip from late April that never made it into our trade log (the routines that should have logged it had halted on missing API keys, but somehow the trade still happened). I've now backfilled the trade log honestly so we have a real record.

**What that NVDA trade was**
We bought 25 shares of NVIDIA at $201.38 on April 22. It ran up to a high of $216.73 (about +7.6%), which is when our **trailing stop** (a sell order that follows the price up but locks in if it falls a set amount) flipped on. NVDA then drifted down, and the trailing stop sold us out at $195.02 on May 4 — a small loss of $159 (−3.2%). The stop did its job: without it, the loss would have been bigger.

**Why no trades today**
There is no fresh pre-market plan for today. Our last research entry is 22 days old, and three weeks of news (earnings, Fed talk, macro) is just unknown to me right now. I will not size into the open on a stale thesis — that's exactly the "casino" behavior the strategy forbids. Better to wait one day with cash than enter blind.

**What happens next**
Tonight's pre-market routine needs to rebuild a real watchlist from scratch. I'll also note that NVDA earnings are 5/20 (5 trading days out), so if we want to revisit it, we have to do it today — by tomorrow we're inside the 3-day earnings blackout window per our rules.

**Numbers**
- Equity: **$99,840.95** (−$159.05, −0.16% from our $100K start — all from the NVDA trade above)
- Cash: $99,840.95 (100% in cash, 0 open positions)
- This week's buys used: 0 of 3 allowed

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
