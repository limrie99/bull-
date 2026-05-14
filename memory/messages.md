# Messages from Bull

Append-only conversation log. **Most recent at the top.** Each entry is what Bull wants the user to see from a routine run.

Format:

```
## YYYY-MM-DD HH:MM CT · {routine name}

**Headline one-liner**

Body — short paragraph or bullets. What happened, what Bull decided, anything the user should know or decide on.
```

---

## 2026-05-14 12:00 CT · midday

**Midday: steady, no changes — and an honest catch-up on where we are.**

**What I did**
First successful check-in since the API keys went missing on April 22. Everything's wired back up — I can see the account, prices, and news again. I pulled our state: $99,841 cash, no positions, no open orders. Nothing to manage and nothing's bleeding. I also ran a quick midday market scan looking for any breaking catalyst (a sudden piece of news big enough to justify buying right now), and didn't find one specific to any name.

**Why I didn't buy**
Midday rules: I only open new positions in the middle of the day if there's a high-conviction, *breaking* catalyst — a fresh earnings beat with raised guidance, a major analyst upgrade, a big contract win. Today's tape is "risk-on at record highs" with no single-name catalyst named. The wrong move here would be to FOMO into the S&P just because we missed the rally while the keys were down. The right move is to let tomorrow morning's pre-market routine build a proper watchlist with verified earnings dates and catalysts, then act from that plan.

**The honest part**
We've been sitting in cash for three weeks while SPY rallied ~6%. That means our "alpha" (extra return vs. just buying the index) is currently about **-6.4%**. That's a hole I have to dig us out of — but I'd rather dig out with two or three good entries than with one panicked chase. We have all our chips and no losses.

**What happens next**
- Tomorrow's 6 AM CT pre-market routine will rebuild the watchlist from scratch (most of April's names will have reported earnings by now — context is stale).
- Friday's weekly review will formally re-baseline alpha and lay out the path back.

**Numbers**
- Equity: $99,841 (essentially flat since April 21 — paper account drift)
- Cash: $99,841 (100% cash; 0 open positions)
- SPY since 4/21: +6.21% · SPY today: +0.72% intraday
- Alpha since inception: **-6.37%** (the gap we're closing)
- Buys used this week: 0 of 3 · Positions: 0 of 5

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
