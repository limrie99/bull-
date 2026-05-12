# Messages from Bull

Append-only conversation log. **Most recent at the top.** Each entry is what Bull wants the user to see from a routine run.

Format:

```
## YYYY-MM-DD HH:MM CT · {routine name}

**Headline one-liner**

Body — short paragraph or bullets. What happened, what Bull decided, anything the user should know or decide on.
```

---

## 2026-05-12 12:05 CT · midday

**We're back online — and I have some honest news from the time I was dark.**

**What I did**
First successful wake-up since the API keys went missing on 4/22. While I was offline, the one trade I had open (25 shares of NVIDIA, ticker NVDA) ran up nicely, then pulled back and got sold automatically by our "trailing stop" — a safety net that follows the price up and triggers a sale if the stock drops a set percentage from its peak. The position closed at a small loss of $159 (−3.16%), so the account today sits at **$99,840.95 — basically flat to start.** I just backfilled the trade record so our log matches reality, and I did not place any new trades at midday.

**Why**
Two reasons. First, midday isn't when I look for new buys unless there's a breaking catalyst (a sudden piece of news big enough to move a stock right now), and there isn't one today. Second, my last research scan is three weeks stale — the market has moved, and re-entering NVDA at this exact moment is risky because they report earnings next week (we avoid buying within 3 trading days of an earnings report). Better to wait for tonight's pre-market routine, do a fresh scan, and pick the next setup with conviction.

**What happens next**
Tonight's pre-market routine will rebuild a 6–8 name watchlist with verified earnings dates and current catalysts. I'm also adding a fix: when I place a stop order, it has to be "GTC" (good-til-cancelled), not just for the day — a small mistake on the NVDA trade left it briefly un-protected overnight before I caught it.

**Numbers I care about**
- **Equity: $99,840.95** — we started at $100,000, so we are −$159 (−0.16%) since I went live on 4/22.
- **SPY (the S&P 500 index, our benchmark): +3.07% over the same window.** That means I'm **−3.23% behind the market right now**, almost entirely from sitting in cash during a rally. Honest read: cash drag is hurting us. Fixing it starts with tonight's scout.
- **0 of 3 weekly buys used.** $99,840.95 cash dry powder ready for the next high-conviction idea.

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
