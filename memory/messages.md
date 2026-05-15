# Messages from Bull

Append-only conversation log. **Most recent at the top.** Each entry is what Bull wants the user to see from a routine run.

Format:

```
## YYYY-MM-DD HH:MM CT · {routine name}

**Headline one-liner**

Body — short paragraph or bullets. What happened, what Bull decided, anything the user should know or decide on.
```

---

## 2026-05-15 06:05 CT · pre-market

**Good morning — back online after a quiet stretch. Today I'm watching AVGO and GOOGL for the open.**

**What I did**
Re-checked the account (we're at $99,840.95 in cash, no positions) and spun up my research team — three sub-analysts running in parallel: one on overnight macro, one on today's earnings calendar, one scouting new buy ideas. I also pulled fresh prices on our watchlist from Alpaca and verified the next earnings date for each name (this matters — we never want to buy a stock that's about to report, because a single number can swing the price 10%+ overnight, and that's not a swing trade, that's a coin flip).

**Why**
Yesterday the AI-infrastructure trade got a big lift after Cisco gave bullish AI guidance (when a company tells Wall Street it expects strong sales next quarter). **AVGO (Broadcom) jumped +5.4%** and broke out of a multi-week base — that's our cleanest setup: a real secular tailwind (AI chips & networking) + a fresh tape-confirming day, with **no earnings risk for ~18 trading days**. **GOOGL** actually *fell* slightly on a tech-up day, which I read as a chance to add a quality name without chasing — and it's already reported earnings, so we have a long runway. **NVDA and PANW are off the list today** because both report earnings next week, and our rule is no new buys within 3 trading days of a print.

**What happens next**
At the 9:30 ET open, the trading routine will re-check overnight futures and then look to **buy AVGO (~12-15% of the account)** as the anchor, and **GOOGL (~10-12%)** as a second leg. Each gets an automatic "stop loss" (a safety net that sells the position if it drops 7% from where we bought it). If both fill cleanly and the tape stays calm, I may add a small **starter in ANET (Arista)** — but I'll cap us at 3 new buys this week regardless. Reminder: today is pre-market research only, no trades have been placed yet.

**Numbers I care about**
- **Equity: $99,840.95** (essentially flat since April — we missed SPY's +1.4% week because we were on the sidelines waiting for clarity)
- **SPY closed at $748.17 yesterday, up +1.4% this week** — we'll measure ourselves against that going forward
- **Cash deployable: ~$60K target after today's planned buys** (keeping a healthy reserve for post-earnings setups next week)
- **Weekly buy budget: 3 of 3 still available**

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
