# Messages from Bull

Append-only conversation log. **Most recent at the top.** Each entry is what Bull wants the user to see from a routine run.

Format:

```
## YYYY-MM-DD HH:MM CT · {routine name}

**Headline one-liner**

Body — short paragraph or bullets. What happened, what Bull decided, anything the user should know or decide on.
```

---

## 2026-05-25 06:00 CT · pre-market (for Tue 5/26 open)

**Back online — and I've got a plan to put money to work on Tuesday.**

**What I did**
Today is Memorial Day, so the US stock market is closed. I used the morning to read overnight data and run a four-analyst research sweep (one each on macro, earnings, sector rotation, and stock picks). No trades — I can't trade a closed market — but I'm staging the Tuesday open routine.

**Where we stand**
The bad news: while I was offline for a month (the API keys got unset back on 4/22), the S&P 500 — the basket of America's 500 biggest companies that we measure ourselves against — rallied **+5.9%**. We're still at roughly $99,841 in cash, basically flat. That puts us about **6% behind the market** for the period. I'm not going to panic-buy to catch up — that's how accounts blow up. I AM going to stop sitting in 100% cash and start putting capital to work on real setups.

**Why NVDA is the trade for Tuesday**
NVIDIA (chipmaker that powers most AI servers) reported earnings (its quarterly financial scorecard) on Wednesday 5/20 after the close. They **beat expectations** (revenue $81.6B vs. ~$78.5B expected) and **raised guidance** (their own forecast for next quarter) to $91B — much higher than Wall Street was modeling. That's the cleanest "beat and raise" signal in our playbook.

The funny thing: the stock actually **dropped about 3.6%** in the two days after the print, from $223 to $215. That's a Wall Street thing called "sell the news" — the stock had already run +57% in a year, so even great results disappointed traders who wanted *perfect* results. For us, that's a gift — a cheaper entry on a name whose fundamentals just got confirmed for the next 3 months (their next earnings isn't until late August, so we have clean runway).

**The plan for Tuesday 5/26**
- Open a **starter position** in NVDA — roughly **$10–12K, about 10–12% of the account, ~50 shares around $215**.
- Place a "bracket order" (a buy with an automatic sell built in) so if NVDA drops 7% to $200, I sell automatically — that's our hard stop, the safety net.
- Hold off on a second position until I can verify earnings dates on AMD, CRWD, PANW, and LLY at Tuesday's 6 AM check — a couple of those may have earnings this week, which we don't trade through.
- **Big watch:** Thursday morning 5/28 the government releases the PCE inflation number, which is the Federal Reserve's favorite gauge of inflation. A hot reading could shake the market. I'll keep most of the cash dry until after that print.

**Numbers I care about**
- **Equity: $99,840.95** (-0.16% from $100K seed)
- **Cash: $99,840.95** (100% — that needs to change Tuesday)
- **SPY since 4/21: +5.90% — we're 6.06% behind the index**, my fault for the dead-cash stretch. Earning that back is the next 30 days' job.

I'll write again Tuesday morning before the open. — Bull 🐂

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
