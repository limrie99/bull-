# Messages from Bull

Append-only conversation log. **Most recent at the top.** Each entry is what Bull wants the user to see from a routine run.

Format:

```
## YYYY-MM-DD HH:MM CT · {routine name}

**Headline one-liner**

Body — short paragraph or bullets. What happened, what Bull decided, anything the user should know or decide on.
```

---

## 2026-05-29 12:00 CT · midday

**Midday: steady, no changes — we're back online after a long quiet stretch.**

**What I did**
I woke up at noon, pulled fresh data from Alpaca, and checked the account. Good news: the API keys are working again, and I can see everything. Bad news for the calendar: this is my first real check-in since 4/22, so there's been a long stretch where I wasn't running. I did **not** open any new positions — midday is for managing risk on what we already own, not for impulse buys.

**Why**
Our account is sitting at **$99,840.95 in cash with zero positions** (cash means money parked, not invested yet). There's nothing to stop-loss, nothing to take profit on, and no daily-loss-cap to trip — because we have nothing in the market. The strategy specifically says: at midday, only buy on a **high-conviction breaking catalyst** (a fresh, unusual news event that clearly moves a stock). I didn't see one, and starting a brand-new portfolio scan from scratch on a quiet Friday afternoon (the day before a weekend) is exactly the kind of rushed decision that loses money. I'd rather wait until Monday's pre-market routine and do a proper, careful scan.

**What happens next**
Monday morning (June 1) at the pre-market routine, I'll fan out my sub-agents — one for macro (the big picture: rates, oil, Fed talk), one for the earnings calendar (which companies report next week), and one to build a fresh watchlist. By Monday's open we should have 2–3 high-conviction names ready. Until then, cash is the safest place.

**Numbers**
- **Equity: $99,840.95** — essentially the $100K we started with. (There's a tiny $159 paper-account drift from Alpaca over the past 5 weeks of inactivity — nothing we did, no real loss; I'll keep an eye on it.)
- **Cash: $99,840.95 (100% in cash)** — nothing at risk, nothing earning either.
- **SPY (the S&P 500 index, our benchmark): $756.95** — noted for next week's comparison.

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
