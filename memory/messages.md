# Messages from Bull

Append-only conversation log. **Most recent at the top.** Each entry is what Bull wants the user to see from a routine run.

Format:

```
## YYYY-MM-DD HH:MM CT · {routine name}

**Headline one-liner**

Body — short paragraph or bullets. What happened, what Bull decided, anything the user should know or decide on.
```

---

## 2026-05-01 08:45 CT · market-open

**Open: no new trades — checking in after a memory gap, and our NVDA position is intact.**

**What I did**
I'm awake again — the API keys are back and the market just opened. First thing I did was reconcile memory against the broker, because no routine successfully wrote anything between 4/22 and today. The good news: the broker did its job. Our NVDA buy from 4/22 (25 shares at $201.38) is alive, and the stop-loss ladder ran exactly to plan. I backfilled all of that into the trade log and portfolio file so the record is clean.

**Why no new buys today**
Market-open routines are supposed to execute a plan from a fresh pre-market scan, and there isn't one for today. Buying blind into the open without research would break our own playbook ("don't force mediocre entries"). I'd rather sit on cash one more day and do a proper scout tonight than chase. We've used 0 of our 3 weekly buys this week, so we have plenty of room.

**About NVDA — a small win, then a giveback**
Here's what happened while memory was dark: NVDA ran up to ~$216.73 (+7.6% from our entry). Once it crossed +5%, the system swapped our −7% hard stop for a **10% trailing stop** — that's an automatic sell that follows the price up. As NVDA hit $216.73, the stop ratcheted up too, and now sits at **$195.06**. NVDA has since pulled back to ~$202, so we've given back most of the unrealized gain — but the trailing stop locks in our floor: we *can't* lose more than $6.92/share from here even if it dumps. The thesis (AI infrastructure buildout, earnings 5/20) is unchanged.

**What happens next**
Midday I'll re-check NVDA for any thesis-break news. Tonight is a proper pre-market scout for next week — I'll come back with a real watchlist (NVDA, MSFT, GOOGL post-earnings, AVGO, etc.).

**Numbers**
- Equity: **$100,009.63** (essentially flat since 4/21 — we put 5% to work, the rest stayed safely in cash)
- Cash: **$94,965.50** (~95% of the account — lots of dry powder)
- NVDA position: $5,042 (5% of portfolio, well under our 20% cap)
- SPY this week: +1.18%; us: ~flat. We're trailing the index by ~1.2% week-to-date — the cost of staying mostly cash. Tonight's scout needs to fix that.

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
