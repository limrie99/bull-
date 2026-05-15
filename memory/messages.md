# Messages from Bull

Append-only conversation log. **Most recent at the top.** Each entry is what Bull wants the user to see from a routine run.

Format:

```
## YYYY-MM-DD HH:MM CT · {routine name}

**Headline one-liner**

Body — short paragraph or bullets. What happened, what Bull decided, anything the user should know or decide on.
```

---

## 2026-05-15 08:40 CT · market-open

**I'm back online — and I owe you a catch-up. Your NVDA trade ran and exited while I was offline.**

**What I did**
Today: nothing new — no buys, no sells, just reconciling the books. While I was offline for the last three weeks (my API keys were missing in the cloud, so most routines just halted), one routine on 4/22 squeezed through and actually placed our planned starter trade in NVDA (Nvidia — the AI chip company). The auto-sell rules I set up at the time then ran themselves without me watching, exactly as designed.

**Why**
Here's the story in order: On 4/22 I bought 25 shares of NVDA at $201.38 (about $5,034, or 5% of the account) as a small "starter" position with a -7% safety net (a *stop loss*, an order that automatically sells if the price falls too far). The stock then climbed to a high of $216.73 — a +7.6% gain. Because we crossed the +5% mark, my rule swapped the safety net for a **trailing stop** (a sell that follows the price up but never down — it locks in profit). The trailing stop is set 10% below the highest price ever reached. On 5/4, NVDA pulled back enough to hit it, and we were sold at $195.02. Result: a small loss of **-$159.04 (-3.16%)** rather than the unrealized gain we briefly had.

**What happens next**
No trades today — I don't have fresh research to act on. My last real market scout was three weeks ago, and the world has moved. The next pre-market routine will run a real scan; I'll be patient until then. NVDA's next earnings are on 5/20, so even our prior idea is off-limits for now (we don't open new positions within 3 trading days of an earnings print — too much surprise risk).

**Numbers I care about**
- Equity: **$99,840.95** (-$159.05 since funding on 4/21 — basically flat, just that one realized loss)
- Cash: **$99,840.95** — 100% cash, fully ready to deploy when a good setup appears
- Since I started, **SPY** (the S&P 500 ETF — a proxy for "the market") is up about **+5%**, and we're at **-0.16%**, so our **alpha** (return vs. the market) is **-5.18%** since inception. That's not great. The mechanical stop did its job, but the cost of being out of the market entirely during a +5% rally is real — getting capital back to work (carefully) is the next priority.
- Buys used this week: **0 of 3** — plenty of room when a real signal shows up

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
