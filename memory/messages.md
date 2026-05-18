# Messages from Bull

Append-only conversation log. **Most recent at the top.** Each entry is what Bull wants the user to see from a routine run.

Format:

```
## YYYY-MM-DD HH:MM CT · {routine name}

**Headline one-liner**

Body — short paragraph or bullets. What happened, what Bull decided, anything the user should know or decide on.
```

---

## 2026-05-18 15:09 CT · market-close

**Close: equity $99,840.95 · day 0.00% · SPY −0.09% · alpha +0.09%**

**What I did**
Honestly — nothing today. We have no open positions and I placed no trades. But when I pulled our records from Alpaca (our broker), I found a trade I had no memory of: back on April 22nd, "I" bought 25 shares of NVIDIA at $201.38, and then on May 4th our automatic safety-net (a "trailing stop" — a sell order that follows the price up and triggers if it falls 10% from the high) sold them at $195.02. Net result: a small loss of **−$159.05**, or about **−0.16% of the account**. That's why our cash is $99,840.95 instead of the $100,000 we started with.

**Why this happened**
The trade itself was fine in concept — NVIDIA is a leader in AI chips, the playbook called for a small starter position. The trailing stop did its job: it let the price run up to $216.73 before locking in protection, then sold automatically when NVIDIA pulled back. Our rulebook says we need **2 strong reasons** to buy a stock; this one only had 1, so it was always a small, exploratory position. Lesson learned: even small "starter" buys lose real money when the signal is thin. I'll be stricter next time.

**The mystery part**
My own memory says the 4/22 routines couldn't run (the API keys were missing that morning), but Alpaca shows the order went through. So *something* with credentials ran that day. We should figure out which scheduled run actually has working keys before I lean on it for important decisions.

**What happens next**
Market closed today essentially flat (the S&P 500 — the index of the 500 biggest US companies — slipped −0.09%). Because we were in cash, we earned **+0.09% alpha** (the difference between our return and the market's) — but that's *passive* alpha from sitting out a red day, not from picking winners. Real alpha has to come from being *invested* in the right names. Tomorrow morning I'll do a full pre-market scan and rebuild a watchlist — it's been 4 weeks, the market has moved, and **NVIDIA reports earnings Wednesday after the close**, which will set the tone for the whole AI sector.

**Numbers**
- Equity: **$99,840.95** (down $159.05 from our $100K start, −0.16% all-time)
- Cash: $99,840.95 (100% cash — full firepower for the next setup)
- Day return: 0.00% · SPY day: −0.09% · alpha today: **+0.09%**
- Open positions: 0 · Closed trades all-time: 1 (NVDA, −3.16%)

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
