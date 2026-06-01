# Messages from Bull

Append-only conversation log. **Most recent at the top.** Each entry is what Bull wants the user to see from a routine run.

Format:

```
## YYYY-MM-DD HH:MM CT · {routine name}

**Headline one-liner**

Body — short paragraph or bullets. What happened, what Bull decided, anything the user should know or decide on.
```

---

## 2026-06-01 08:31 CT · market-open

**Open: no trades — research is six weeks stale and I won't trade blind.**

The market just opened (Monday 6/1) and I checked the account — we're sitting at **$99,840.95 in cash, no open positions**. That's almost exactly where you left me. Good news: the API keys are working again, so I can see and trade.

Here's the honest situation. The last real research I did was 2026-04-22 — six weeks ago. Two routines after that **halted** because the API keys were missing, and then nothing ran until now. The old plan (a small NVDA starter into the 4/22 open) is dead context: prices have moved, NVDA's May 20 earnings have already happened, and the macro picture I was watching (Iran headlines, 10-year yields, futures tone) is from another tape entirely.

One of my own strategy rules says: *don't blindly execute a stale plan*. So I deliberately did **not** force a trade just to look busy. The right move at the open is to wait for a fresh pre-market scout — that's where I do the heavy lifting on earnings, catalysts, and macro before risking any of your money.

**What happens next:** the next pre-market routine should re-scout with a fresh watchlist (a "watchlist" is just my shortlist of names I want to research that day). Once I have a verified setup — meaning at least two of my buy signals hit on the same name — I'll place a trade with a built-in **stop loss** (an auto-sell that caps losses at -7%). Until then, cash is safer than a guess.

**Numbers I care about:**
- $99,840.95 cash on hand (we started at $100,000 — about $159 of unexplained drift; I'll reconcile via the Alpaca activities feed next routine)
- 0 of 3 weekly buys used
- 0 of 5 position slots filled

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
