# Messages from Bull

Append-only conversation log. **Most recent at the top.** Each entry is what Bull wants the user to see from a routine run.

Format:

```
## YYYY-MM-DD HH:MM CT · {routine name}

**Headline one-liner**

Body — short paragraph or bullets. What happened, what Bull decided, anything the user should know or decide on.
```

---

## 2026-04-24 08:35 CT · market-open

**Open: no trades — holding NVDA, up a little, stop safely in place.**

**What I did**
Nothing, on purpose. I checked in at the bell: the market is open, our account is healthy, and our one position (NVDA — the big AI-chip company) is quietly in the green. I did **not** place any new buys because I don't have a fresh pre-market research plan for today — and our strategy says I don't trade without a thesis I can defend.

**Why**
Two things to explain. First: NVDA is up about +0.8% from where we bought it on Tuesday. That's good, but it's not yet up +5% — the level where I flip from a fixed "hard stop" (auto-sell at $187.28 to cap our worst-case loss at -7%) to a "trailing stop" (a safety net that follows the price up as it rises, locking in gains). So the stop stays exactly where it is. Second: I also noticed the trade-log in memory was missing the NVDA buy from 4/22 — it did actually happen on Alpaca, but the routine that placed it didn't write it down. I backfilled that entry so our records match reality. No real money is off — the position is there, the stop is there, both correct.

**What happens next**
Tonight I'll do a proper research scout (fresh earnings calendar, fresh catalysts) so I walk into Monday with a real plan — not stale notes from last week. If NVDA pops above ~$211.45 today, that's my cue to swap the hard stop for the 10% trailing stop.

**Numbers**
- Equity: **$100,042** (up $42 since we started on Monday — basically flat, which is fine for a first week)
- NVDA: 25 shares, +$41 unrealized, stop at $187.28
- Cash: **$94,966** (we've only put ~5% to work so far — plenty of dry powder)
- Buys used this week: 1 of 3 · Open positions: 1 of 5

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
