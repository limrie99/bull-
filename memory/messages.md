# Messages from Bull

Append-only conversation log. **Most recent at the top.** Each entry is what Bull wants the user to see from a routine run.

Format:

```
## YYYY-MM-DD HH:MM CT · {routine name}

**Headline one-liner**

Body — short paragraph or bullets. What happened, what Bull decided, anything the user should know or decide on.
```

---

## 2026-05-15 15:10 CT · market-close

**Close: equity $99,841 · day 0.00% · SPY −1.20% · alpha +1.20%**

I'm back online — the API keys you set are now working, and this is the first routine that's actually been able to talk to Alpaca since April 22nd. So a few things to share, and one honest note:

**What I did**
Nothing — I had no positions to manage and the market closed before I could responsibly open new ones. Market-close is the wrong routine to start fresh risk; that's Monday morning's job.

**Why**
Today, the S&P 500 (the index of 500 big US companies — when people say "the market" they usually mean SPY, which tracks it) fell about 1.2%. Because we were sitting in cash, we didn't lose a cent. That technically means we beat the market by +1.2% today — what we call "alpha" (the extra return vs. just buying the index). But I want to be honest: that's **not real skill on my part**. Cash always wins on a down day. Our edge has to come from being *invested* in the right stocks on up days, not from hiding in cash. So I'm not patting myself on the back.

**What happens next**
Monday morning's pre-market routine is the important one. I'll send a team of research sub-agents out in parallel to refresh our watchlist (the April list is too stale to act on), check what's reporting earnings next week, and pick our first real position. NVDA reports next Wednesday 5/20 — we're already inside our pre-earnings "blackout" window for NVDA, so that name is off the table until after the print.

**Numbers I care about**
- Equity: **$99,840.95** (we started at $100,000 — the $159 difference appears to be small accrued fees that crept in during the outage; no trades happened, I checked). Treating this as our new baseline.
- Cash: $99,840.95 — **100% in cash**, 0 of 5 position slots used.
- This week vs. SPY: we're flat (0.00%), SPY is up about +0.21% — so we're slightly behind, which makes sense since we weren't invested.

The honest summary: 17 trading days in cash is a long time to miss. Monday we get back to work. 🐂

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
