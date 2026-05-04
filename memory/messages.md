# Messages from Bull

Append-only conversation log. **Most recent at the top.** Each entry is what Bull wants the user to see from a routine run.

Format:

```
## YYYY-MM-DD HH:MM CT · {routine name}

**Headline one-liner**

Body — short paragraph or bullets. What happened, what Bull decided, anything the user should know or decide on.
```

---

## 2026-05-04 12:00 CT · midday

**Back online — and our NVDA trade auto-sold this morning at a small loss.**

**What I did**
The system has been quiet since April 22 because the API keys went missing — that's fixed now, and I just did a full reconciliation. The big news: our NVIDIA position (which I bought on 4/22 as a starter) auto-sold this morning at 10:21 CT for a small loss of about $159. We bought 25 shares at $201.38, sold 25 shares at $195.02. No new buys at midday — strategy says I only break the "no midday buys" rule for breaking-news catalysts, and there isn't one.

**Why**
Two things to explain. First, a "trailing stop" is a safety net that follows the price up — once we were +5% in profit, I cancelled the original safety net and put a new one at "10% below the highest price the stock hits." NVIDIA peaked at $216.73 on 4/27, so the stop set itself at $195.057 (10% below). When the stock drifted down today, that line tripped automatically. Second, *why* did NVIDIA drift down? Three real reasons: investors are trimming ahead of NVIDIA's earnings (their quarterly report card) on May 20, China export rules are still capping revenue, and Google/Amazon hinted they'll start selling their own AI chips to outside customers — meaning NVIDIA's biggest buyers might also become rivals. None of those break the long-term AI thesis, but together they were enough to push the price 10% off the top, which is exactly when our safety net is designed to fire.

**What happens next**
We're 100% cash again ($99,841). I'll wait for tomorrow's pre-market (6 AM CT) to do a fresh scan. NVIDIA goes back on the watchlist *after* its 5/20 earnings — we don't open positions inside the 3-day window before a company reports, because earnings nights can swing 10% either way and that's gambling, not investing. I want the report's information first.

**Numbers I care about**
- Equity: **$99,840.96** — down $159 since inception (-0.16%)
- SPY (the broad market index) is up +1.00% over the same window, so we're behind by about **1.16%** — not a hole we can't climb out of, but the scoreboard is honest
- Cash: **$99,840.96** (100% cash, 0 of 3 weekly buys used, 0 of 5 position slots filled)
- Today's auto-sell was the system working as designed: small loss capped, capital preserved, ready for the next idea

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
