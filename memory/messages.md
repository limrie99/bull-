# Messages from Bull

Append-only conversation log. **Most recent at the top.** Each entry is what Bull wants the user to see from a routine run.

Format:

```
## YYYY-MM-DD HH:MM CT · {routine name}

**Headline one-liner**

Body — short paragraph or bullets. What happened, what Bull decided, anything the user should know or decide on.
```

---

## 2026-05-06 12:00 CT · midday

**Midday: steady, no changes — but I owe you a reconciliation.**

**What I did**
Sat on 100% cash and made no trades. Spent the routine reconciling our records with Alpaca, because while the cloud routines were halted earlier (the API-key blackout), an NVDA round-trip actually happened on the broker side and our local notebook missed it. I've now logged it properly: we bought 25 shares of NVDA on April 22 at $201.38, and on May 4 a "trailing stop" (a sell order that follows the price up and only fires if the stock drops 10% from its peak) sold all 25 at $195.02. Net loss on that trade: **-$159 (-3.16%)**.

**Why**
The trailing stop did exactly what our playbook says it should — it activated once NVDA was up 5%+, rode it up to a peak of $216.73 (+7.6%), then locked in our exit when it pulled back 10% from that high. Annoyingly, NVDA bounced today (+4% to $204.77), so in hindsight we got out near the low. But "in hindsight" is not a strategy. The rule worked, we follow the rule, we move on. No revenge buy.

**What happens next**
I'm passing on a midday entry. The rules say no new buys at midday unless there's a genuinely breaking catalyst, and there isn't one. **Tomorrow's pre-market is where I'll do real work** — fan out the sub-agents (macro / earnings / opportunity scout) on a fresh watchlist (NVDA, AVGO, GOOGL, PLTR, CRWD, PANW, BE) and look for a 2-signal name to redeploy ~10–15% of the account.

**Numbers I care about**
- **Equity: $99,840.95** — basically flat from start, but down -0.16% all-in vs. our $100K beginning.
- **SPY** (the S&P 500 ETF I benchmark us against) is up **+1.0% today and +2.75% on the week**. We're in cash, so we're missing this rally — **alpha vs. SPY this week: -2.84%**. Not great. The fix is finding a real buy, not panicking.
- 0 of 3 weekly buys used, 0 of 5 position slots used. Plenty of room to act when a real setup shows up.

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
