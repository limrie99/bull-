# Messages from Bull

Append-only conversation log. **Most recent at the top.** Each entry is what Bull wants the user to see from a routine run.

Format:

```
## YYYY-MM-DD HH:MM CT · {routine name}

**Headline one-liner**

Body — short paragraph or bullets. What happened, what Bull decided, anything the user should know or decide on.
```

---

## 2026-05-06 06:00 CT · pre-market

**Good morning, Lauren — APIs are back, tape looks constructive, and I've found a high-conviction trade for the open.**

**What I did**
This is research-only — markets are closed until 8:30 AM CT. I sent three sub-advisors to scout overnight: one to read the macro tape, one to comb the earnings calendar, and one to hunt for buy candidates. I'm not placing any trades right now.

**Why**
The setup heading into the open is mildly **risk-on** (a "risk-on" tape means investors are willing to buy stocks rather than hide in bonds). S&P 500 futures are up about 0.22%, the 10-year Treasury yield dropped 7 basis points (good for stocks because lower rates make future earnings worth more today), and oil is softer on the US-Iran ceasefire holding. The catch: **AMD reported a weak quarter last night** and is down ~5% after-hours, so semiconductors will likely open under pressure even as the rest of the tape rallies. That tells me to lean **away from chip stocks today and into Industrials and Defense**, which is exactly where the money has been rotating ("rotation" = investors moving from one sector to another).

**Plan for the 8:30 AM open**
My top idea is **RTX (Raytheon Technologies)** — a defense contractor with four real signals stacking up: a fresh Wall Street upgrade (RBC raised it to "Outperform" with a $140 target), the **CFO bought $8 million of his own stock last week** (insiders only buy for one reason — they think it's going up), a defense-spending tailwind, and money is flowing into the industrial sector. I'm targeting a **standard 12% position (~$12,000, ~96 shares around $125)** with a **-7% hard stop** (an automatic sell-order placed at the same time as the buy — our safety net). A possible second trade is **FIX (Comfort Systems USA)** — they crushed earnings 4/29 and ride the data-center build-out — but only if RTX fills cleanly first.

**Numbers**
- Equity: $99,840.95 (we're $159 below the $100K start with no trades on record — small Alpaca paper-account quirk, watching it)
- Cash: $99,840.95 (100% in cash, 0 positions)
- Buys used this week: 0 of 3
- SPY benchmark: $723.94 at yesterday's close

I'll check in again at the market-open routine in ~2.5 hours. 🐂

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
