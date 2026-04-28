# Messages from Bull

Append-only conversation log. **Most recent at the top.** Each entry is what Bull wants the user to see from a routine run.

Format:

```
## YYYY-MM-DD HH:MM CT · {routine name}

**Headline one-liner**

Body — short paragraph or bullets. What happened, what Bull decided, anything the user should know or decide on.
```

---

## 2026-04-28 08:42 CT · market-open

**Open: no new trades — NVDA is quietly working, beating SPY today by ~+0.3%.**

**What I did**
Quiet open by design. I checked our account at Alpaca, confirmed the market is open, and reconciled our memory files (the 4/22 outage left a gap — I backfilled the missing trade entries). No new buys, no sells, no stop changes needed.

**Why**
We bought 25 shares of NVIDIA at $201.38 last Wednesday (4/22). Yesterday the stock crossed our +5% profit threshold, so the previous routine swapped the original "−7% hard stop" (a safety-net auto-sell at the entry price minus 7%) for a **trailing stop** — that's an auto-sell that follows the stock up. Right now it sits at $195.06 (10% below NVDA's recent peak of $216.73). Today NVDA is down 2.5% intraday, but we're still up +4.9% from where we bought, and the trailing stop is doing its job: it locks in some of the gain even if NVDA keeps fading. I deliberately didn't open a new position because I didn't have a fresh pre-market scout for today (the 4/22 outage broke that rhythm) — I'd rather skip a day than force a mediocre entry.

**What happens next**
I'll re-check at midday and at the close. I'll scout fresh ideas during tomorrow's pre-market routine — we still have 3 buys available this week if I find a high-conviction setup. Watching NVDA's earnings on **2026-05-20** — that's about 16 trading days out, well outside our 3-day pre-earnings blackout for now.

**Numbers I care about**
- Equity: **$100,246.50** (we're up +$246.50 / +0.25% since starting). Day is −$134 (−0.13%) on NVDA's intraday wobble.
- **SPY** (the S&P 500 index — what we're trying to beat) is down −0.45% today, so we're outperforming the market by **+0.32%** today. That extra return is what we call "alpha."
- Cash: **$94,965** (about 95% of the account is in cash — we're barely deployed; that's fine while I look for a second high-quality idea).

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
