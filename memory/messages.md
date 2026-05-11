# Messages from Bull

Append-only conversation log. **Most recent at the top.** Each entry is what Bull wants the user to see from a routine run.

Format:

```
## YYYY-MM-DD HH:MM CT · {routine name}

**Headline one-liner**

Body — short paragraph or bullets. What happened, what Bull decided, anything the user should know or decide on.
```

---

## 2026-05-11 08:37 CT · market-open

**Open: no trades — sitting tight, but we have some catching up to do.**

**What I did**
I checked in at the bell. The market is open, our account is healthy ($99,840.95 in cash, no stocks held), and there were no urgent items from you in the inbox. I did **not** place any trades because I don't have a fresh research plan to act on — the last real pre-market scout was nearly three weeks ago (April 21), and acting on stale ideas is exactly how we lose money on bad entries.

**Why**
Our playbook (a "playbook" is the rulebook in `memory/strategy.md`) says I need at least **two confirmed buy signals** — like a real earnings beat, a near-term catalyst, or a fresh analyst upgrade — before I open a position. The old plan was to start a small NVDA position, but NVDA now reports earnings next week, which puts it inside our 3-day pre-earnings blackout (a self-imposed rule that says don't open a fresh position right before a company's earnings — those prints are coin-flips). That plan is dead. I need a fresh scan before I risk capital.

**Honest check-in on our scorecard**
SPY (the S&P 500 index ETF — basically "the market") is up about **+4.78%** since this account opened on April 21. We're flat. That means we're trailing the market by roughly **-4.94%** ("alpha" is the gap between us and SPY — right now ours is negative). That's the cost of being too patient. It's defensible for the first few weeks of a new account, but I owe you a real watchlist soon, not more "waiting."

**What happens next**
- I'll check in at midday (12:00 CT) and at close (3:00 PM CT).
- The next pre-market routine needs to produce either a real trade plan **or** an explicit "stay flat because X" thesis — no more vague watchlists.
- If you want me to push harder on entries, drop a note in `memory/inbox.md`.

**Numbers I care about**
- **Cash: $99,840.95** (essentially the full $100K starting balance — we are 100% on the sidelines)
- **Positions: 0** (max allowed is 5)
- **Buys used this week: 0 of 3** (we reset every Monday — fresh slate today)

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
