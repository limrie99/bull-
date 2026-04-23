# Messages from Bull

Append-only conversation log. **Most recent at the top.** Each entry is what Bull wants the user to see from a routine run.

Format:

```
## YYYY-MM-DD HH:MM CT · {routine name}

**Headline one-liner**

Body — short paragraph or bullets. What happened, what Bull decided, anything the user should know or decide on.
```

---

## 2026-04-23 08:37 CT · market-open

**Open: no new trades — we're back online and you already own 25 shares of NVIDIA.**

**What I did**
I reconnected to the broker (Alpaca) this morning and did a full account check. I placed **no new orders** today. Instead, I did something important: I discovered that the NVIDIA (NVDA) starter trade from our Tuesday night plan **actually filled yesterday morning at $201.38** — 25 shares, ~$5,035 committed. Both of yesterday's routines had halted because the API keys were missing, so neither you nor I had visibility into this until now. I've back-logged the trade and confirmed a safety net is in place.

**Why**
I chose not to open anything new because I don't have a fresh research scan for today — yesterday's pre-market and midday both halted, so I'm flying without a current list of candidates. Strategy says we need at least two verified buy signals before opening a position (a "signal" is a reason the stock should go up — earnings beat, analyst upgrade, sector tailwind, etc.). Opening cold violates that. Better to wait for tonight's pre-market scout than to force a trade.

On NVDA: the position is healthy (+0.10%, basically flat), and I verified the **stop loss** (an automatic sell if the stock drops too far) is in place at $187.28 — that's 7% below our entry, our hard safety net.

**What happens next**
Midday check-in I'll scan NVDA news and watch for any intraday drop past 3%. At the close, I'll log today's P/L against SPY (the whole US stock market) and start tracking our "alpha" — the extra return vs. just buying the index. Tonight's pre-market I'll run the full research scout we missed on Wednesday.

**Numbers**
- Equity: **$100,004** — basically where we started. Day P/L: -$24 (-0.02%), versus SPY -0.18%, so we're a hair ahead of the market right now.
- Cash left: **$94,966** (~95% — we've put only ~5% to work so far on NVDA)
- This week's buys used: **1 of 3** (plenty of room for two more if the research lines up)

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
