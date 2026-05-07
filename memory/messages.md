# Messages from Bull

Append-only conversation log. **Most recent at the top.** Each entry is what Bull wants the user to see from a routine run.

Format:

```
## YYYY-MM-DD HH:MM CT · {routine name}

**Headline one-liner**

Body — short paragraph or bullets. What happened, what Bull decided, anything the user should know or decide on.
```

---

## 2026-05-07 15:02 CT · market-close

**Close: equity $99,841 · day +0.00% · SPY -0.31% · alpha +0.31% (but I owe you the full picture).**

**What I did**
Today I sat fully in cash — no buys, no sells, no stops to manage — so the account was completely flat. SPY (the S&P 500 index, the benchmark we're trying to beat) drifted down 0.31%, so technically by doing nothing on a red day we "outperformed" by +0.31% (your "alpha" — the extra return vs. just holding the index). I want to be honest: that's not skill, that's just being in cash on a down day.

**The bigger picture you should know**
While the routines were halted for ~12 days on missing API keys, my orders at the broker kept running. Here's what actually happened: I bought 25 shares of NVIDIA on 4/22 at $201.38. It rallied to ~$216, my 10% trailing stop (a safety net that follows the price up and sells if it falls 10% from the highest point) moved up with it, and on 5/4 NVDA pulled back enough to trigger that stop — I was sold out at $195.02. **Net result on the round-trip: -$159, or -3.2% on the position.** Small loss, system worked exactly as designed.

**The ugly part**
SPY then ran +1.5% Mon→Thu this week while I was sitting in cash. So week-to-date, **we're behind SPY by 1.65%**. That's the cost of not having a fresh research pass to put money back to work after the exit. I'll fix that tomorrow.

**What happens next**
Tomorrow's pre-market routine I'll do a fresh scout — NVDA's earnings are 5/20 (likely too close to enter again), but AVGO, GOOGL, MSFT, PLTR, CRWD, PANW are all on the watchlist. I have 0/3 buys used this week and ~$99.8K of dry powder, so a clean setup could still earn its way into the book by Friday close.

**Numbers**
- Equity: **$99,841** (started at $100,000, so we're down $159 / -0.16% since funding — the NVDA round-trip)
- Cash: **$99,841** (100% of the account — nothing at risk, nothing earning)
- Today: 0.00% vs SPY -0.31% → **alpha +0.31%**
- Week-to-date: -0.11% vs SPY +1.53% → **alpha -1.65%** (the gap I need to close)

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
