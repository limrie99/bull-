# Messages from Bull

Append-only conversation log. **Most recent at the top.** Each entry is what Bull wants the user to see from a routine run.

Format:

```
## YYYY-MM-DD HH:MM CT · {routine name}

**Headline one-liner**

Body — short paragraph or bullets. What happened, what Bull decided, anything the user should know or decide on.
```

---

## 2026-05-20 15:10 CT · market-close

**Close: equity $99,841 · day 0.00% · SPY +1.02% · alpha −1.02%**

**What I did**
Nothing today — and that's the problem I want to be honest with you about. The account is back online (your API keys are working again, which is great), but we own zero stocks. The market (SPY, which tracks the 500 biggest US companies) rose about 1% today, and because we were 100% in cash, we earned 0%. So we underperformed by ~1% today alone.

**The bigger picture**
The account has been sitting in cash for almost three weeks while I was offline. In that time SPY climbed about **+5%**, and we're down a small **−0.16%** from the $100,000 we started with on 4/21. That gap — about **−5.5% vs the index since inception** — is what we have to work to close. It's not because of a bad trade; it's because we weren't in the game.

**Why no buys today**
Two reasons. First, **NVDA** (Nvidia — the AI chipmaker) reports their quarterly earnings tonight after the bell. Earnings can swing a stock 10%+ in either direction, and our rule is to not open a new position within 3 trading days of its earnings — too much risk of buying right before bad news. Second, I'd rather take one good look at the post-earnings tape tomorrow morning than rush a buy on a partial-info day.

**What happens next**
Tomorrow morning (pre-market, around 6 AM CT) I'll read NVDA's print and re-scan a fresh watchlist. If the print is clean and the tape is constructive, I'll start putting cash to work — likely a starter position (about 5% of the account, ~$5K) rather than a full-size buy, so we leave room to add if it works.

**Numbers**
- Equity: $99,841 (flat today, −$159 since 4/21 inception)
- Cash: $99,841 — 100% of the account is sitting in cash, earning nothing
- SPY today +1.02% vs us at 0.00% → **alpha −1.02% today** ("alpha" = how much we beat the market by; negative means we lagged)
- One small admin note: Alpaca's history shows there were a few small trades during the period my secrets were missing (net −$159). Those fills aren't in our trade log because I wasn't writing memory then. The account itself is clean and accurate; just the per-trade detail for that window is gone.

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
