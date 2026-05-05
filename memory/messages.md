# Messages from Bull

Append-only conversation log. **Most recent at the top.** Each entry is what Bull wants the user to see from a routine run.

Format:

```
## YYYY-MM-DD HH:MM CT · {routine name}

**Headline one-liner**

Body — short paragraph or bullets. What happened, what Bull decided, anything the user should know or decide on.
```

---

## 2026-05-05 15:00 CT · market-close

**Close: equity $99,841 · day +0.00% · SPY +0.78% · alpha −0.78%**

**What I did**
Today I sat in cash and didn't trade. I also reconciled the books: while my routines were offline on 4/22 (missing API keys), the live Alpaca account *did* execute the NVDA starter we'd planned — bought 25 shares at $201.38 — and that position rode up to $216.73 before retracing and triggering our trailing stop yesterday (5/4) at $195.02. Net realized loss on NVDA: **−$159 (−3.16%)**.

**Why**
A "trailing stop" is an automatic sell that follows the price up but never down — it locked in a 10% pullback from the high. The mechanic worked exactly as designed: it kept the loss small ($159 on a $5,000 position is 3% of *that position*, less than 0.2% of the whole account). The frustrating bit is timing — I was halted, so I couldn't decide whether to take partial profits manually as the stock ran. Lesson learned: even with stops doing their job, an awake operator can squeeze more out of winners.

**What happens next**
Tomorrow morning's pre-market scout will pull a fresh watchlist (NVDA, AVGO, GOOGL, MSFT, PLTR and a few more) and look for clean 2+ signal setups now that the late-April earnings wave is over. NVDA itself reports earnings on 5/20 — if the thesis is still intact and price has stabilized, a fresh re-entry is on the table (this isn't "averaging down" — that's adding to a losing position, which we don't do; this would be a brand-new trade with its own thesis).

**Numbers I care about**
- Equity: **$99,841** — down $159 from our $100,000 start (essentially flat, −0.16% lifetime)
- Cash: **$99,841** — 100% in cash, ready to deploy on the next clean setup
- SPY today: **+0.78%** — the broad market had a good day, and being in cash cost us about 78 basis points of alpha. That's the price of patience after a stop-out.

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
