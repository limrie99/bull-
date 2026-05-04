# Messages from Bull

Append-only conversation log. **Most recent at the top.** Each entry is what Bull wants the user to see from a routine run.

Format:

```
## YYYY-MM-DD HH:MM CT · {routine name}

**Headline one-liner**

Body — short paragraph or bullets. What happened, what Bull decided, anything the user should know or decide on.
```

---

## 2026-05-04 15:00 CT · market-close

**Close: equity $99,841 · day −0.09% · SPY −0.33% · alpha +0.24%**

**What I did**
Our trailing stop on NVDA fired at 10:21 AM CT and automatically sold all 25 shares at $195.02. We're back to 100% cash heading into Tuesday — $99,841 in the account, no open positions.

**Why**
Quick refresher on the move: a "trailing stop" is an order that follows a stock up but never down. Once NVDA was up more than 5% (our playbook rule), I converted it from a fixed −7% safety net into a 10% trailing stop — meaning, "if the stock ever drops 10% from its highest point, sell automatically." NVDA peaked at $216.73 (up 7.6% from our $201.38 entry), then sold off, and at $195.06 — exactly 10% below that peak — the order tripped. Net on the round-trip: a small realized loss of $159 (−3.2% on the position, −0.16% on the whole account). Frustrating, because the trade was green and we gave it back. But the system did exactly what it should: cap downside, no babysitting required.

**What happens next**
We're flat, which is fine — fully reset for tomorrow. NVDA still has earnings May 20 (16 trading days away); not buying back into it without a fresh setup. PLTR (an AI/defense software name) reports tonight after the close — that's a useful read-through on the AI-software group I'll factor into tomorrow's pre-market scan. SPY also fell 0.33% today — I'll watch whether that's one quiet Monday or the start of a broader pullback.

**Numbers**
- Equity: $99,841 (down $86 from Friday's close, −0.09%)
- SPY (the broader US market) fell 0.33% today, so we beat the index by +0.24% — that gap is our "alpha" (the extra return vs. just owning SPY)
- Cash: $99,841 (100% of the account) — full dry powder for tomorrow
- 0 of 5 position slots used · 0 of 3 weekly buys used

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
