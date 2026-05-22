# Messages from Bull

Append-only conversation log. **Most recent at the top.** Each entry is what Bull wants the user to see from a routine run.

Format:

```
## YYYY-MM-DD HH:MM CT · {routine name}

**Headline one-liner**

Body — short paragraph or bullets. What happened, what Bull decided, anything the user should know or decide on.
```

---

## 2026-05-22 15:05 CT · market-close (Fri)

**Close: equity $99,841 · day +0.00% · SPY +0.40% · alpha −0.40%**

**What I did**
Nothing today — and that's worth talking about. We held no positions all week, so the account sat at exactly $99,841 from Monday through the Friday close. The market (SPY) was up about +0.40% today and +0.89% on the week, so we underperformed by roughly 0.9% this week purely from being parked in cash.

**Why**
When I pulled live data back up today, I found something I want to be straight with you about: a trade we placed back in April **was never written into our trade log**. Specifically, we bought 25 shares of NVIDIA on April 22 at $201.38, and a "trailing stop" (an automatic sell that follows the price up but locks in a sale if it drops 10% from its peak) closed that position on May 4 at $195.02 for a small loss of **−$159 (−3.16%)**. That single trade is exactly why our equity is $99,841 and not $100,000. The reason the log was blank: those earlier routines reported themselves halted (missing API keys), but the trade actually executed in the background. I've now logged it properly so our books match reality.

Since that NVDA stop on 5/4, the account has been **100% cash for 18 trading days**. That's too long to be dormant — cash isn't free when SPY is climbing. I'll treat Tuesday's pre-market as a clean rescan.

**What happens next**
Market is closed Monday (Memorial Day). I'll wake up Tuesday 5/26 pre-market with a fresh scout — top of the list is checking NVIDIA's May 20 earnings reaction, plus the AI / cybersecurity / large-cap names on our watchlist. Goal: find at least one ≥2-signal entry to put a small amount of cash back to work.

**Numbers I care about**
- Equity **$99,841** (down $159 from our $100K start — that's the NVDA trade, fully accounted for)
- Cash **$99,841** (100% — all of it sitting idle)
- **Alpha vs SPY this week: −0.89%** (we trailed the market by about 0.9% by holding cash)
- **0 of 3 weekly buys used.** Next week's cap resets Monday.

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
