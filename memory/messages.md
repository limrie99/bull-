# Messages from Bull

Append-only conversation log. **Most recent at the top.** Each entry is what Bull wants the user to see from a routine run.

Format:

```
## YYYY-MM-DD HH:MM CT · {routine name}

**Headline one-liner**

Body — short paragraph or bullets. What happened, what Bull decided, anything the user should know or decide on.
```

---

## 2026-05-13 06:00 CT · pre-market

**Good morning — Bull is back online with a real watchlist. Two strong buy candidates lined up for today.**

**What I did**

I'm awake at 6 AM CT for the pre-market routine. Account is clean ($99,841 cash, no positions). I sent three research sub-agents out in parallel — one for the macro picture (what futures are doing, what bonds and oil are doing), one for today's earnings calendar (which companies are reporting), and one to scout for buy candidates. I didn't place any trades — the market isn't open yet, and the pre-market routine is research-only.

**Why**

Today's tape is **macro-driven**, not earnings-driven — no large companies in our universe report this morning. S&P 500 futures are mildly green (+0.1% to +0.3%), Nasdaq futures are flat-to-slightly-soft, and most of the other macro data (10-year Treasury yield, dollar, oil) didn't come back clearly tonight, so I'm reading it as **a quiet, undecided tape**. That's good enough to act on a high-conviction name at a partial size, not good enough to swing big. The scout found two names that hit our buy rules cleanly:

- **RTX (defense / aerospace contractor)** — they beat earnings last quarter *and* raised their guidance (raised guidance = the company is publicly saying it expects to make more money than analysts thought), got fresh upgrades (analyst upgrades = Wall Street firms raising their rating) from Morgan Stanley and Citi last week, and the stock chart is healthy. Four of our six buy signals are checked — the cleanest setup since I started.
- **AVGO (Broadcom — makes custom AI chips for the big cloud companies)** — sitting on the AI-infrastructure boom but isn't NVDA, so it diversifies that bet. Multiple analyst upgrades in early May and a $15B+ AI revenue run-rate.

**What happens next**

When the market opens at 8:30 CT, the market-open routine will re-check that futures didn't flip negative overnight, then **lead with RTX (~12–15% of the account, around $12K–$15K) and pair it with AVGO (~10–12%, around $10K–$12K)**. Each gets an automatic "hard stop" — a sell order pre-placed 7% below my entry price as a safety net (a "stop loss" — it auto-sells if the price drops too far, so a bad surprise can't wipe me out). I'll skip Lockheed Martin (LMT) for now even though it's a defense name — its chart is broken (price is below its trend line), and our rule is no falling knives. There's a tempting third name, **LLY (Eli Lilly)**, with an FDA decision on a new oral weight-loss pill on **June 15** — I'll consider that one later in the week as a half-size catalyst trade.

**Numbers I care about**

- **Cash:** $99,841 (the paper account drifted ~$159 below the $100K starting line — a small Alpaca paper-trading adjustment, nothing to worry about).
- **Buys used this week:** 0 of 3 (room for 2 buys today if conditions hold).
- **Open positions:** 0 of 5 max.

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
