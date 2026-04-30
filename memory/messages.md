# Messages from Bull

Append-only conversation log. **Most recent at the top.** Each entry is what Bull wants the user to see from a routine run.

Format:

```
## YYYY-MM-DD HH:MM CT · {routine name}

**Headline one-liner**

Body — short paragraph or bullets. What happened, what Bull decided, anything the user should know or decide on.
```

---

## 2026-04-30 15:00 CT · market-close

**Close: equity $99,961 · day −0.24% · SPY +0.96% · alpha −1.19%**

**What I did**
First real check-in since my keys were restored — welcome back. I didn't place any trades today; I just took the closing snapshot, confirmed our one open position (25 shares of NVDA), and checked that our automatic safety net is still in the right place.

**Why**
Today was a frustrating one to watch. The overall market (the S&P 500, which I track using the SPY ETF) had a strong day, up about +0.96%. We slipped −0.24% — not a big dollar move, just $236 on the whole account, but we lagged the market by about 1.2 percentage points (that gap is called "alpha" — the extra return we earn versus just buying the index). The reason is simple: ~95% of the account is still in cash, and our one stock, NVDA, fell −4.5% on a day the rest of the market rose. When you're concentrated in one name and mostly in cash, you eat the bad days alone and miss the good ones.

The good news: I sized the NVDA entry as a small "starter" position (~$5K, about 5% of the account) precisely because we only had one strong signal at the time — so a −4.5% NVDA day cost us less than a quarter of a percent. That's the discipline working.

**What happens next**
NVDA's automatic sell price ("trailing stop" — a sell order that follows the stock up but never down, locking in gains as it rises) is at $195.06. The stock closed at $199.80, so we're only ~2.4% above being stopped out. Tomorrow morning I'll dig into *why* NVDA dropped today (any bad news vs. just profit-taking?) and look at AMZN's earnings report tonight as a possible second position to add — running with only one stock is leaving us too exposed to one company's bad days.

**Numbers**
- Equity: **$99,960.50** (down $39.50 since we started — a rounding error in market terms)
- Cash: **$94,965.50** (~95% of account still in cash, which is a lot — that's the gap I want to close, carefully, this week)
- NVDA: 25 shares, down 0.78% from where I bought, with a trailing stop at $195.06 ready to sell automatically if it falls further
- Alpha week-to-date: **−0.83%** (we're behind SPY by about $830-equivalent on a $100K account this week — Friday's close is when I formally measure)

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
