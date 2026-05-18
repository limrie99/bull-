# Messages from Bull

Append-only conversation log. **Most recent at the top.** Each entry is what Bull wants the user to see from a routine run.

Format:

```
## YYYY-MM-DD HH:MM CT · {routine name}

**Headline one-liner**

Body — short paragraph or bullets. What happened, what Bull decided, anything the user should know or decide on.
```

---

## 2026-05-18 12:00 CT · midday

**Midday: we're back online, no changes — sitting in cash and waiting for the right setup.**

**What I did**
Almost a month ago (April 22), the routines started halting because the API keys vanished — without them I can't talk to our broker (Alpaca) or research engine (Perplexity), so I sat on my hands rather than guess. The keys are now restored, the market is open, and I just did a full sweep: 0 positions, $99,840.95 in cash, no open orders, no pending messages from you. There was nothing to fix, so I didn't trade.

**Why**
At midday I only act on emergencies — a position bleeding out, a stop that needs tightening because we're winning, or a breaking catalyst (a news event big enough to move the stock right now) that's too good to ignore. We had none of those because we have no positions yet. After a 26-day blackout, the worst thing I could do is force a trade just to "make up for lost time." Patience is part of the playbook — we re-enter the market through a careful pre-market scout (my morning research routine), not a panic-buy at lunch.

**What happens next**
Tomorrow morning at 6:00 CT I'll run a full pre-market: macro check, earnings calendar, and a hunt for 2–3 fresh buy ideas using our signals (earnings beats, near-term catalysts, secular tailwinds). I'll write up the top picks and either place a starter trade at the open or explain why I'm still passing. Market-close routine today is just a quiet "no changes" check.

**Numbers**
- Equity: **$99,840.95** (started with $100,000, so we're $159 below the seed — likely a small fee that predates today; I've flagged it for the weekly review and will track it down)
- Cash: **$99,840.95** (100% in cash — maximum dry powder)
- Buys used this week: **0 of 3** — full ammo for tomorrow

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
