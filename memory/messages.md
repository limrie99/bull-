# Messages from Bull

Append-only conversation log. **Most recent at the top.** Each entry is what Bull wants the user to see from a routine run.

Format:

```
## YYYY-MM-DD HH:MM CT · {routine name}

**Headline one-liner**

Body — short paragraph or bullets. What happened, what Bull decided, anything the user should know or decide on.
```

---

## 2026-05-20 08:33 CT · market-open

**Open: no trades — we're back online, but I don't have a fresh plan to run today.**

**What I did**
I came back online after a long gap (no routines actually ran for almost a month — the API keys were missing through late April). Checked the market is open and pulled the account from Alpaca: $99,840.95 cash, zero positions, no open orders. So nothing was at risk while I was away. I did **not** place any trades at the open.

**Why**
The market-open routine is supposed to *execute* a plan that the pre-market routine built — and there is no plan for today. The last research entry is from April 22, and the only candidate it surfaced was NVIDIA (NVDA), with an entry idea contingent on Wednesday 4/22 futures being constructive. NVDA reports earnings **after the close today** (5/20), which puts it squarely inside our 3-trading-day earnings blackout — a rule that says we don't open new positions right before a company reports earnings (the "earnings print"), because the stock can move 5–15% on the news and we don't want to take that coin-flip without a thesis that specifically calls for it. Opening on a month-old, unvalidated read would be exactly the kind of unforced error I should avoid.

**What happens next**
The next pre-market routine will run a clean scout — fresh macro, verified earnings calendar, a tightened watchlist — and *that* plan will get executed at the following open. I'll also dig into a small $159 equity drift I noticed on the paper account.

**Numbers I care about**
- Equity: **$99,840.95** (very slightly below the $100,000 seed — I'll explain that $159 gap soon)
- Cash: **$99,840.95** (100% of the account is cash, so nothing was bleeding while I was offline)
- Buys used this week: **0 of 3**

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
