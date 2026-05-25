# Messages from Bull

Append-only conversation log. **Most recent at the top.** Each entry is what Bull wants the user to see from a routine run.

Format:

```
## YYYY-MM-DD HH:MM CT · {routine name}

**Headline one-liner**

Body — short paragraph or bullets. What happened, what Bull decided, anything the user should know or decide on.
```

---

## 2026-05-25 15:10 CT · market-close

**Close: equity $99,840.95 · day 0.00% · SPY 0.00% · alpha 0.00% — Memorial Day, market closed**

**What I did**
Nothing tradable — today is Memorial Day, a US federal holiday, so the NYSE and Nasdaq were both closed all day. No prices changed, no orders could fill. What I *did* do is open up Alpaca's order history and reconcile a gap I found between what my memory said and what actually happened in the account. Two real trades had run in late April and early May that were never written into my trade log, so I've back-filled them — see "Numbers" below.

**Why**
Your account is being honestly transparent matters more than looking tidy. Here's what really happened over the last 4 weeks: on 4/22 I bought 25 shares of **NVIDIA (ticker NVDA)** at $201.38 — a "starter tranche," meaning a small first slice (about 5% of the account) rather than a full position. The plan was the AI-infrastructure thesis with a safety net underneath: a **stop-loss order** (an automatic sell if the price falls a set amount). NVDA actually ran up to about $216 — at which point my rules say convert the safety net into a **trailing stop** (a stop that slides up with the price, so it locks in gains as the stock climbs but cuts the position if it gives back 10%). It did exactly that on **5/4** at $195.02 — a small realized loss of **−$159** (−3.16%). The strategy worked as designed: small loss rather than a big one.

**The harder truth**: from 5/4 through today (3+ weeks) the account has been **100% in cash** and my routines went silent — no new ideas committed. While I was idle, SPY (the S&P 500 ETF, our benchmark) climbed **+0.89% this past week** and **+5.93% since we started on 4/21**. The account is essentially flat (−0.16% since 4/21). So today's *headline* alpha is zero (nothing moved), but the **week's alpha is −0.89% and inception alpha is −6.09%** — the cost of holding cash through an up-market.

**What happens next**
Markets reopen Tuesday 5/26. Tomorrow's pre-market routine needs to do a real fresh scout from scratch (the watchlist from 4/21 is stale — NVDA already reported earnings on 5/20). I'd like to know from you whether the routines have been off, or whether they've been running and just not committing — either way, the dashboard had been showing stale state until today's repair. With ~$99.8K in cash and a clean slate, I'll come into tomorrow ready to deploy a small 2–3 position basket on the next clean signal, but I won't force anything.

**Numbers I care about**
- Equity: $99,840.95 — basically where we started ($100K), but the market has risen ~6% in the meantime, so we've underperformed by **−6.09% since 4/21**.
- Cash: $99,840.95 (100% cash). 0 open positions.
- Realized P/L on the only completed trade so far: **−$159 on NVDA** (entry $201.38, exit $195.02, peak $216.73 before it pulled back).
- Buys used this week: 0 of 3 available. New-position headroom: 5 of 5 slots open.

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
