# Messages from Bull

Append-only conversation log. **Most recent at the top.** Each entry is what Bull wants the user to see from a routine run.

Format:

```
## YYYY-MM-DD HH:MM CT · {routine name}

**Headline one-liner**

Body — short paragraph or bullets. What happened, what Bull decided, anything the user should know or decide on.
```

---

## 2026-04-24 12:10 CT · midday

**Midday check: steady, no changes — our NVDA position is quietly working.**

**What I did**
Nothing — and that's the right call today. I pulled fresh data from our broker (Alpaca), confirmed our one position (Nvidia) and its safety net, and ran the three risk checks I do every midday. All three came back clean, so no trades.

**Why**
Here's the teaching moment. Our rules say I only act at midday if something's wrong or urgent: (1) a position is down −7% or worse (time to cut losses), (2) a position is up +5% or more (time to upgrade its safety net from a fixed −7% stop to a "trailing stop" — a sell order that follows the price up and locks in gains if it reverses 10%), or (3) the whole account is down more than 3% today (pause new buying). None of those triggered. Nvidia is up +4.14% — really close to the +5% trailing-stop line, but not there yet. The broader market (the S&P 500, tracked by SPY) is up +0.34% on the day, so the tape is calm. Forcing a trade in quiet conditions is how portfolios bleed.

**What happens next**
I'll check again at market close (3 PM CT). If Nvidia crosses $211.45 (our +5% line) before then, the close routine will swap the fixed stop for the 10% trailing stop automatically.

**Numbers I care about**
- Equity: **$100,208.50** — up $252 today (+0.25%), and up $208 on the week since the account went live.
- Nvidia: 25 shares, bought at $201.38 on Wednesday, now $209.72 — unrealized gain of **+$208 (+4.14%)**. Hard stop still at $187.28 (it sells automatically if NVDA drops there, capping our loss at −7% from entry).
- Cash: **$94,965** left (~95% of the account). We are deliberately still mostly in cash — with only one small position, we're lagging SPY's +1.38% week so far by about 1.17 percentage points ("alpha" is just the gap between us and the index). That gap will close as we add the next 2–3 high-conviction names. Patience is part of the strategy, not a mistake.

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
