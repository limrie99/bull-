# Messages from Bull

Append-only conversation log. **Most recent at the top.** Each entry is what Bull wants the user to see from a routine run.

Format:

```
## YYYY-MM-DD HH:MM CT · {routine name}

**Headline one-liner**

Body — short paragraph or bullets. What happened, what Bull decided, anything the user should know or decide on.
```

---

## 2026-05-12 08:40 CT · market-open

**Back online — but no trades at this open. Holding $99,841 in cash on purpose.**

**What I did**
The API keys are working again (we were halted for the last few weeks because they were missing). I confirmed with Alpaca that the market is open, pulled our account state — $99,840.95 cash, zero positions — and then I *chose not to trade*.

**Why**
Here's the honest version: the last real research pass I did was three weeks ago (April 21st), back when I was thinking about a small starter position in NVIDIA (NVDA). That plan is stale — markets move a lot in three weeks, and our strategy explicitly says **don't execute old context blindly**. Trading at the open on a 3-week-old thesis would be acting on vibes, not research. A wealth advisor wouldn't do that with your money. NVDA's earnings (the company's quarterly results report, which often moves the stock sharply) are now about 6 trading days away — close enough that I want a fresh scout before I size anything in, not a guess.

**What happens next**
The next pre-market routine will run a proper fresh scout: macro check (futures, bond yields, oil), updated earnings calendar, and verified buy signals across our watchlist (NVDA, MSFT, GOOGL, AVGO, etc.). If anything cleanly hits 2+ buy signals from our playbook, I'll act then.

**Numbers**
- Equity: **$99,840.95** (vs. $100,000 paper seed — small ~$159 drift from Alpaca's internal paper-account bookkeeping over the dormant weeks, no trades involved)
- Cash: **$99,840.95** (100% cash — full powder dry)
- SPY (the S&P 500 ETF, our benchmark) trading around $735.78 — I'm anchoring our alpha tracking from here

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
