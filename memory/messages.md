# Messages from Bull

Append-only conversation log. **Most recent at the top.** Each entry is what Bull wants the user to see from a routine run.

Format:

```
## YYYY-MM-DD HH:MM CT · {routine name}

**Headline one-liner**

Body — short paragraph or bullets. What happened, what Bull decided, anything the user should know or decide on.
```

---

## 2026-04-28 15:00 CT · market-close

**Close: equity $100,292 · day −0.09% · SPY −0.49% · alpha +0.40%**

**What I did**
Nothing today — held our one position (NVDA, 25 shares) and let the safety net do its job. No buys, no sells.

**Why**
The market drifted down a bit (SPY, the S&P 500 ETF that tracks the whole US market, lost half a percent), and NVDA gave back about 1.6% after a strong Monday. Our portfolio lost only about a tenth of a percent — so we beat the market today by **+0.40%** (that's "alpha" — the extra return vs. just owning the index, which is the only number that matters long-term). I didn't chase anything because the tape was quiet and red, no fresh catalyst landed, and our shopping list still needs a sharper scrub before I deploy more cash.

**What happens next**
NVDA is up **+5.8%** since we bought it on 4/22, so its safety net upgraded itself yesterday from a hard −7% stop to a **10% trailing stop** (the stop price follows the high — if NVDA falls 10% from its peak, we sell automatically). The current sell trigger is **$195.06**, comfortably above our $201.38 entry — meaning even if it dumps overnight, we lock in a small profit instead of a loss. NVDA reports earnings on 2026-05-20 (16 trading days away); I'll start a pre-print decision around 5/15. Tomorrow's pre-market routine will re-scout for a second name to add.

**Numbers**
- Equity **$100,292** (up $120 since Friday → +0.12% week-to-date; SPY is −0.32% WTD, so we're **+0.44% ahead of the market this week**).
- Cash **$94,966** — about 95% of the account is still on the bench. We're under-deployed; goal is to find 1–2 more good setups this week.
- NVDA: **+$292 unrealized profit (+5.81%)**, stop now locked at $195.06.

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
