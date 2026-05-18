# Messages from Bull

Append-only conversation log. **Most recent at the top.** Each entry is what Bull wants the user to see from a routine run.

Format:

```
## YYYY-MM-DD HH:MM CT · {routine name}

**Headline one-liner**

Body — short paragraph or bullets. What happened, what Bull decided, anything the user should know or decide on.
```

---

## 2026-05-18 08:35 CT · market-open

**Open: no trades today — picking up where we left off after a four-week gap.**

**What I did**
I came back online this morning and checked our account. While I was offline, the small NVDA starter trade I'd planned did execute on 4/22 (25 shares at $201.38), and then on 5/4 our **trailing stop** (an auto-sell that follows the price up and triggers when it pulls back too far) fired at $195.02. Net result: a small −$159 loss, about −0.16% of the account. I've logged both trades retroactively. No new trades at today's open.

**Why**
Two reasons for not buying today. **First**, my last fresh research pass is from 4/21 — over four weeks old. Prices, news, and earnings dates have all moved, so that watchlist is stale. **Second**, NVDA — the only name I had an active thesis on — reports earnings this Wednesday (5/20), which puts it inside our 3-day no-buy window around earnings (we avoid opening positions right before earnings because a bad print can gap a stock 10%+ overnight, blowing through any stop). So today's discipline is: don't force a trade just because we're back online. Cash-heavy is fine for one session.

**What happens next**
The next pre-market routine will rebuild the watchlist from scratch — fresh earnings dates, fresh macro read, and a decision on whether to play the NVDA 5/20 print. I'll check in at midday with status, then do a proper close summary this afternoon.

**Numbers**
- Equity: **$99,840.95** (down $159 from our $100K start — that's the NVDA loss, our first round-trip in v2)
- **0 open positions, $99,840.95 cash** (100% in cash, full firepower for the next clean setup)
- SPY: ~$738.65 today — the market is up roughly **+3.9% since 4/22**; we sat out most of that move in cash. Catching back up is the focus this week. 🐂

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
