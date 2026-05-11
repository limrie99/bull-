# Messages from Bull

Append-only conversation log. **Most recent at the top.** Each entry is what Bull wants the user to see from a routine run.

Format:

```
## YYYY-MM-DD HH:MM CT · {routine name}

**Headline one-liner**

Body — short paragraph or bullets. What happened, what Bull decided, anything the user should know or decide on.
```

---

## 2026-05-11 12:10 CT · midday

**Back online — we're alive, still all in cash, and that's the right call today.**

**What I did**
First thing: I checked our paper account at Alpaca (the broker). We're sitting at **$99,840.95 in cash, zero positions, zero open orders.** I also pulled today's market price for SPY (the S&P 500 index — what we measure ourselves against) for context: $739.31. No buys, no sells, no stop changes. There's literally nothing to manage because we don't own anything yet.

**Why**
Two reasons to stand pat. First, my last real research scout was back on April 21, and the trading playbook has a rule I take seriously: don't act on stale context. Three weeks of news, earnings prints, and macro moves have come and gone without me watching — chasing a buy at lunchtime on dead research is exactly how amateurs lose money. Second, the routine's own rules forbid midday buys unless there's a genuine breaking catalyst (a fresh, urgent reason — a guidance raise, a big upgrade, a contract win). I don't have one. Patience here costs us nothing.

**What happens next**
Tomorrow's pre-market routine is where I do real work: I'll spin up a team of sub-agents in parallel to re-scan macro (rates, oil, the dollar), the earnings calendar, and our watchlist. That's when we'll line up our first real trade — carefully, with the −7% safety net built in (a "stop-loss" — an automatic sell if the price drops 7% from where we bought).

**Numbers**
- Equity: **$99,840.95** (essentially the starting $100K — the $159 gap is from before today, not a loss I took)
- Cash: **$99,840.95** — 100% dry powder, ready when a real setup shows up
- Positions: **0 of 5 allowed** · New buys this week: **0 of 3 allowed**
- Day P/L: **$0.00** — no positions = no daily move

Quiet is fine. Quiet plus patient is how we beat the index over time. 🐂

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
