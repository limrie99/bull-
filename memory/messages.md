# Messages from Bull

Append-only conversation log. **Most recent at the top.** Each entry is what Bull wants the user to see from a routine run.

Format:

```
## YYYY-MM-DD HH:MM CT · {routine name}

**Headline one-liner**

Body — short paragraph or bullets. What happened, what Bull decided, anything the user should know or decide on.
```

---

## 2026-05-08 15:10 CT · market-close

**Close: equity $99,840.95 · day 0.00% · SPY +0.82% · alpha −0.82%**

**What I did**
Nothing on the trading side today — no buys, no sells, no stops to manage because we own zero stocks. The big news is we're back online: I'm Bull, your AI wealth advisor, and my API keys (the credentials I need to talk to our broker, Alpaca, and to my research engine, Perplexity) had been missing since 4/22, which forced me to stay halted for safety. They're restored now, so this is my first real check-in in a couple of weeks.

**Why**
I won't pretend this was a great week for us. The S&P 500 (SPY — the index that tracks the 500 biggest US companies and is the benchmark we're trying to beat) gained about **+2.37% this week**, while we just sat in cash. Cash earns ~0%, so we trail the market by about **−2.46% week-to-date** — what we call **negative alpha** (alpha = our return minus the index's return; positive alpha is the whole point of this account). No positions means no losses, but it also means no gains in an up-market.

**What happens next**
On Monday's pre-market routine I'll do a fresh scan. Earnings season has mostly passed since 4/22, so a lot of names that were too risky to enter then (because their results were imminent) are now safe to consider. I'll send up to 3 candidates with my reasoning before pulling the trigger. I won't chase a market that's already up 2%+ this week — I'd rather wait for a pullback than buy the top.

**Numbers I care about**
- Equity: **$99,840.95** (essentially unchanged from start — we drifted about $160 lower over two weeks of inactivity; immaterial, but I noticed it)
- Cash: **$99,840.95** (100% — we have full firepower available)
- SPY this week: **+2.37%**, our portfolio: **−0.09%**, alpha this week: **−2.46%**

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
