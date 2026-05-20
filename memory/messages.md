# Messages from Bull

Append-only conversation log. **Most recent at the top.** Each entry is what Bull wants the user to see from a routine run.

Format:

```
## YYYY-MM-DD HH:MM CT · {routine name}

**Headline one-liner**

Body — short paragraph or bullets. What happened, what Bull decided, anything the user should know or decide on.
```

---

## 2026-05-20 06:03 CT · pre-market

**Back online — and tonight NVIDIA reports, which is the biggest event of the month for our portfolio.**

**What I did**
Just research — markets don't open for another 3.5 hours. I checked our account ($99,841 cash, no positions yet — still fresh) and sent my sub-agent team out to scan overnight headlines, today's earnings calendar, and buy candidates. Then I built a plan for the 8:30 CT open.

**Why today is unusual**
**NVIDIA reports earnings after the close** (a "print" — when a company tells the market how much money it made last quarter). NVIDIA is the world's biggest AI chip maker; when it reports, it moves the whole AI sector tomorrow morning. Two of my three best buy candidates today — **Palantir (PLTR)** and **Vertiv (VRT)** — move with NVIDIA. If I buy them at the open and NVIDIA disappoints tonight, they could drop 5–10% Thursday morning before I've even gotten comfortable with the position.

**My plan for the open**
- **Open a starter in Eli Lilly (LLY)** — about 10% of the account, roughly $10,000. LLY makes Zepbound (the leading weight-loss drug) and has nothing to do with NVIDIA. It lets me start putting cash to work without taking on the wrong risk.
- **Hold off on PLTR and VRT until tomorrow morning**, after NVIDIA's report digests. If NVIDIA prints clean, I add Palantir (my top pick) and Vertiv. If it misses, both get cheaper and I rescan.
- **Pass on everything** if futures drop more than 0.5% by 8:30 CT or a hawkish Fed headline lands.

**What happens next**
8:30 CT open routine will execute (or pass on) the LLY starter. Then we wait for the Federal Reserve meeting minutes at 1pm CT (could move bond yields) and NVIDIA at 3pm CT. Big day.

**Numbers**
- Cash: $99,841 (a tiny $159 phantom delta from $100K start — looks like Alpaca paper-account housekeeping, not a real trade; I'll confirm next routine)
- Open positions: 0 of 5 max
- Buys used this week: 0 of 3

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
