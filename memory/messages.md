# Messages from Bull

Append-only conversation log. **Most recent at the top.** Each entry is what Bull wants the user to see from a routine run.

Format:

```
## YYYY-MM-DD HH:MM CT · {routine name}

**Headline one-liner**

Body — short paragraph or bullets. What happened, what Bull decided, anything the user should know or decide on.
```

---

## 2026-05-28 08:32 CT · market-open

**Back online — catching you up on what happened while I was offline, and why I'm not buying anything this morning.**

**What I did**
Nothing new today — no buys, no sells. But I did discover something my records missed: way back on April 22, I actually *did* place that NVDA (Nvidia) starter trade we'd planned — 25 shares at $201.38, about $5,000 of the account. A "trailing stop" (a sell order that follows the stock price up — once a stock is winning, it slides up behind it and only triggers if the stock drops 10% from its peak) fired on May 4 at $195.02, after NVDA had peaked at $216.73 and pulled back. Net result: we lost $159 on that round-trip (-3.2%). I went back and logged both legs of that trade properly so our records match reality.

**Why nothing today**
My system was offline for about five weeks (the API keys were missing — your end, not mine). I've now got fresh keys, but I don't have a fresh "pre-market scout" — the research pass I do before each market open to figure out *what* is worth buying *today*. Our strategy says "fundamentals-driven only — don't trade without verification." A research note from a month ago isn't verification. So I'm sitting in cash this morning and I'll run a proper scout for tomorrow's (Friday's) open.

**The honest scoreboard**
While we were offline, the overall US market (SPY) ran from about $709 to $750 — that's **+5.8%**. We were essentially flat (-0.2%). So we're **about 6% behind the market** since inception. That's not where I want to be, and I want to be straight with you about it.

**What happens next**
- Midday and close routines today: monitoring only, no new trades.
- Friday pre-market: I'll spin up sub-agents to scan macro, earnings, and a fresh watchlist, then propose 1–2 starter buys if the setups are clean.
- I'll raise this in the weekly review: should the system block trading entirely if research is more than 3 days stale? Right now there's no safety net for that.

**Numbers**
- Cash: $99,840.95 (essentially all of it — we're 100% in cash heading into today)
- Equity: $99,840.95 (started at $100,000, so -0.16% lifetime)
- Open positions: 0 of our max 5
- Buys used this week: 0 of 3
- SPY today: ~$750, up about 5.8% since we started — we have ground to make up 🐂

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
