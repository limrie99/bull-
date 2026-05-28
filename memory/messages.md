# Messages from Bull

Append-only conversation log. **Most recent at the top.** Each entry is what Bull wants the user to see from a routine run.

Format:

```
## YYYY-MM-DD HH:MM CT · {routine name}

**Headline one-liner**

Body — short paragraph or bullets. What happened, what Bull decided, anything the user should know or decide on.
```

---

## 2026-05-28 15:00 CT · market-close

**Close: equity $99,841 · day +0.00% · SPY +0.54% · alpha −0.54%**

**What I did**
Nothing today — no buys, no sells. We sat in 100% cash. The broader US market (the S&P 500, which we track through an index fund called SPY) drifted up 0.54%. Because we held no stocks, our account value didn't move, which means we *lagged the market* (our "alpha" — the difference between us and SPY — was −0.54% today).

**Why**
Honest update: my routines went quiet for several weeks after our first trade (NVDA, which we exited 5/04 on a trailing stop — a sell rule that locks in profit if the stock drops a set percentage from its peak). I'm now back online with this market-close run. I didn't see a setup today that cleared our 2-signal threshold (our rule: a stock needs at least 2 of our 6 buy signals to qualify), and a quiet midweek session isn't the moment to force a position just to feel busy.

**What happens next**
Friday's pre-market routine will rebuild a fresh watchlist with verified earnings dates and a near-term catalyst. I want our next buy to be a conviction trade — earnings beat, guidance raise, or a clean sector tailwind — not a "we need to do something" trade.

**Numbers I care about**
- Equity: **$99,841** (started at $100K, so we're −0.16% lifetime — basically flat, accounting for the NVDA trade that closed at a small loss)
- Cash: **$99,841** (0 of 5 position slots used; max we can put in any single stock is $20K)
- Week vs SPY: portfolio flat, SPY +1.21%, **alpha −1.21% WTD** — catching up to do, but I'd rather pick the right entry than chase

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
