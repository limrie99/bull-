# Messages from Bull

Append-only conversation log. **Most recent at the top.** Each entry is what Bull wants the user to see from a routine run.

Format:

```
## YYYY-MM-DD HH:MM CT · {routine name}

**Headline one-liner**

Body — short paragraph or bullets. What happened, what Bull decided, anything the user should know or decide on.
```

---

## 2026-05-04 08:52 CT · market-open

**Open: no trades — found a missed NVDA position from 4/22 and got our books back in sync.**

When I logged in this morning I noticed our memory files said we had $100K in cash and zero positions, but our actual broker account (Alpaca) said we own **25 shares of Nvidia (NVDA)** bought at $201.38 on April 22nd. So someone — or rather, some earlier routine I can't see — actually placed our planned NVDA starter trade after I'd halted that day on missing API keys. The trade is real; the bookkeeping just never made it into our notes. I've now backfilled the trade log and portfolio so everything matches reality.

**The state of our NVDA position right now**

- We own **25 shares at $201.38 average cost**, currently $199.46 — so we're down about **$48 (-1%)**, basically flat.
- The good news: NVDA briefly ran to **$216.73 (+7.6%)** sometime in the last two weeks, which triggered our strategy rule to swap the hard -7% stop for a **10% trailing stop** (a "trailing stop" rises with the stock and only triggers an auto-sell if the stock falls 10% from its highest point — it locks in gains). That trailing stop is **active right now at $195.06**. If NVDA dips below that, we exit automatically, no questions asked.
- **NVDA reports earnings on 2026-05-20** (16 days out). We're well outside our 3-day "no new buys before earnings" window, so we're holding through the print as planned.

**Why I'm not buying anything today**

My last real research scan was April 21st — that's nine trading days old, which is ancient in market terms. Our rule is not to trade off stale context. So today I'm only watching the NVDA position; I'll run a proper market scan in tonight's pre-market routine for tomorrow's open.

**Numbers**
- Equity: $99,953 (essentially unchanged from Friday's close)
- Cash: $94,966 — about 95% of the account is in cash, ready to deploy
- Buys used this week: **0 of 3** allowed
- One open order: the NVDA trailing stop at $195.06

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
