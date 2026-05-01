# Messages from Bull

Append-only conversation log. **Most recent at the top.** Each entry is what Bull wants the user to see from a routine run.

Format:

```
## YYYY-MM-DD HH:MM CT · {routine name}

**Headline one-liner**

Body — short paragraph or bullets. What happened, what Bull decided, anything the user should know or decide on.
```

---

## 2026-05-01 12:00 CT · midday

**Midday check — quiet, holding NVDA, no changes.**

**What I did**
Pulled fresh prices from our broker (Alpaca) and reviewed our one open position — Nvidia (ticker NVDA, the AI-chip leader we bought on April 22). It's down a tiny amount today, well within our risk rules, and the safety net is already in place. No buys, no sells, no stop adjustments needed.

**Why**
At midday I only act if one of three things is true: (a) a position is down 7% or more from where we bought it (NVDA is just −1%, so we're nowhere near that), (b) a position has crossed +5% profit and needs its safety net upgraded to a "trailing stop" — an auto-sell that follows the price up but never down (already done last week when NVDA peaked at $216.73), or (c) the whole portfolio is down more than 3% on the day (we're flat). None triggered, so the disciplined move is to hold and let the thesis play out. New buys at midday need a high-conviction breaking catalyst (something major just happened) — nothing on the tape today qualifies.

**What happens next**
I'll check again at the close. If NVDA falls to about $195, the trailing stop will auto-sell us out — that's our worst-case downside locked in. The big upcoming watch: NVDA's earnings report on **2026-05-20** (when companies reveal their quarterly results — usually a big stock-moving event).

**Numbers I care about**
- NVDA: 25 shares, −1% from our $201.38 entry — paper loss of $51, no big deal.
- Trailing stop set at $195.06 — the price below which we automatically sell to cap losses.
- Cash: $94,966 left (we've put about 5% to work, so we're sitting on ~95% cash — deliberate, since no clean second buy has set up).
- Today vs the market: SPY (the S&P 500 index, our benchmark) is up about +0.5%; we're roughly flat. Since our NVDA buy on 4/22 we're down about 1.6% relative to SPY — early days, but a thing I'm watching.

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
