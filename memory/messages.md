# Messages from Bull

Append-only conversation log. **Most recent at the top.** Each entry is what Bull wants the user to see from a routine run.

Format:

```
## YYYY-MM-DD HH:MM CT · {routine name}

**Headline one-liner**

Body — short paragraph or bullets. What happened, what Bull decided, anything the user should know or decide on.
```

---

## 2026-05-28 06:15 CT · pre-market

**Quiet open expected — I'm eyeing one name (Nvidia) for our first trade.**

**What I did**
Woke up at 6 AM, ran the secrets check (all good — we're back online after that long April outage), and pulled fresh data with a team of three sub-agents in parallel: one watching overnight markets, one checking today's earnings calendar, and one scouting buy ideas. No trades placed — market doesn't open until 8:30 CT, and the pre-market routine is research only.

**Why it's quiet**
Futures are mildly soft (S&P 500 futures down about 0.2%, Nasdaq down about 0.4%) but nothing scary. The 10-year Treasury yield (a key interest-rate gauge — when it falls, stocks tend to like it) is easing to ~4.45%. Oil is down on Middle East de-escalation hopes. No mega-cap earnings reports are confirmed for today, so the day will likely be driven by macro headlines and weekly jobless-claims data, not company-specific news.

**The one real candidate: Nvidia (NVDA)**
NVDA reported earnings last Wednesday (5/20) and *crushed it* — $1.87 earnings per share vs. $1.76 expected, $81.62B revenue vs. $78.42B expected. That's a "positive earnings surprise" — signal #1 in our playbook. Pair that with the ongoing AI buildout (signal #3, a "secular tailwind" — a multi-year trend that lifts a whole sector), and NVDA clears our 2-signal minimum. Next earnings aren't until late August, so we have ~3 months of runway — well outside our 3-day-before-earnings blackout rule.

**What happens next**
At the 8:30 market-open routine I'll re-verify NVDA's price, double-check that overnight tone hasn't flipped risk-off, and likely open a **starter position around 10–15% of the account** (~$10–15K). I keep it small because it's our first trade — better to size up later if the thesis holds than overcommit on day one.

**Numbers**
- Equity: $99,841 (basically untouched since 4/21 — the API outage meant we sat in cash the whole time, which was the right call)
- Cash: $99,841 (100% in cash — about to put some to work)
- Open positions: 0 of 5 max
- New buys used this week: 0 of 3

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
