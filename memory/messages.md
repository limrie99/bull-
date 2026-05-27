# Messages from Bull

Append-only conversation log. **Most recent at the top.** Each entry is what Bull wants the user to see from a routine run.

Format:

```
## YYYY-MM-DD HH:MM CT · {routine name}

**Headline one-liner**

Body — short paragraph or bullets. What happened, what Bull decided, anything the user should know or decide on.
```

---

## 2026-05-27 12:00 CT · midday

**Midday: steady, no changes — and good news, the keys are working again.**

**What I did**
First, the relief: the API keys that were missing back in April are restored, so I can see and trade the account again. I checked the live account at Alpaca (the broker that holds our money) and pulled fresh prices. We hold no stocks right now — we're 100% in cash — so there were no positions to manage, no losses to cut, and no winners to protect. I made no trades.

**Why**
Midday is my risk-checkup, not my shopping trip. My job here is to (1) cut anything down 7% on a broken story, (2) protect any winner up 5%+ with a trailing stop (an auto-sell that follows the price up and only sells if it falls back 10%), and (3) freeze new buys if we're having a bad day. With no holdings, none of that applied. I did one quick news scan for a big breaking catalyst that might justify a rare midday buy — there wasn't one (the market's just drifting up on AI-chip optimism, no single must-own headline). So I stayed patient rather than forcing a trade off month-old notes.

**What happens next**
Here's the honest part: we've been sitting entirely in cash since late April, when the routines stalled on those missing keys. That's safe, but it means we've been on the sidelines while the market (SPY, the index of the 500 biggest US companies) has been grinding higher — that costs us a little. Now that I can trade again, the next pre-market routine will do a full fresh research sweep and start putting money to work where the case is strong.

**Numbers**
- Equity: $99,840.95 — basically flat today, and just ~$159 under our $100,000 starting point
- All in cash (0 stocks), so 0% return this week vs. the market's ~+0.55% — being uninvested is a small drag we'll fix
- Buys used this week: 0 of 3 — plenty of room when a real opportunity shows up

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
