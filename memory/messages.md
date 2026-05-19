# Messages from Bull

Append-only conversation log. **Most recent at the top.** Each entry is what Bull wants the user to see from a routine run.

Format:

```
## YYYY-MM-DD HH:MM CT · {routine name}

**Headline one-liner**

Body — short paragraph or bullets. What happened, what Bull decided, anything the user should know or decide on.
```

---

## 2026-05-19 15:10 CT · market-close

**Close: equity $99,841 · day 0.00% · SPY −0.62% · alpha +0.62%**

**What I did**
Nothing today — we sat fully in cash. But I owe you a real update because I just discovered we have a memory gap from 4/22 through today, and meaningful things happened that I never wrote down. The short version: we bought NVDA on 4/22 and got automatically stopped out on 5/04 for a small loss. We've been in cash since.

**Why (the NVDA round-trip you didn't hear about)**
On 4/22 at the open I bought 25 shares of NVDA at $201.38 — about 5% of the account, a "starter" position (small first bite of a stock to test the thesis before committing more). I set a safety net: a "10% trailing stop" (an auto-sell that follows the price up and only sells if the stock drops 10% from its peak). NVDA ran up to about $216.73 — a gain of ~7.6% — and then the tape faded. On 5/04 the trailing stop did its job and sold us out at $195.02. Net result: a **$159 loss on a $5,000 position (about −3.2%)**, and the account moved from $100,000 to $99,841. That's the entire P/L for the last 27 days.

**Why today's "alpha" is misleading good news**
Today the S&P 500 (the index we're measured against) was down −0.62%. We were flat at 0.00%, so on paper we "beat the market by +0.62%." But that's defensive alpha — we beat SPY by not playing, not by picking winners. We only earn real alpha by redeploying that cash into good ideas.

**What happens next**
NVDA reports earnings tomorrow after the close (5/20 AMC) — that's the big tape event of the week. I'll do a fresh pre-market scout at 6 AM CT tomorrow with a refreshed watchlist (the 4/21 list is a month old; most names have already reported earnings since). The goal: find 1–2 high-quality entries this week and stop sitting in 100% cash.

**Numbers**
- Equity: **$99,841** (down $159 from 4/21 start — that's the NVDA round-trip)
- Cash: $99,841 (100% in cash; zero open positions)
- This week so far: Bull 0.00%, SPY −0.72% → **alpha +0.72% week-to-date**
- Buys used this week: 0 of 3 allowed

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
