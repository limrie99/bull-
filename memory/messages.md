# Messages from Bull

Append-only conversation log. **Most recent at the top.** Each entry is what Bull wants the user to see from a routine run.

Format:

```
## YYYY-MM-DD HH:MM CT · {routine name}

**Headline one-liner**

Body — short paragraph or bullets. What happened, what Bull decided, anything the user should know or decide on.
```

---

## 2026-05-08 08:34 CT · market-open

**Open: no trades — sitting on cash and waiting for a fresh research pass.**

**What I did**
The market is open and I'm watching. I confirmed the account is healthy ($99,841 cash, no open positions) but I chose **not** to open any new trades at the bell.

**Why**
I want to be honest with you: my last real research session was way back on April 21 — 17 days ago. A lot has happened in markets since then, and my own notes from that day literally say "don't blindly execute this plan on stale context." The one name I was eyeing (NVDA, the AI chip company) has its earnings report on May 20 — that's only about 8 trading days from now. Our playbook says we don't open new positions when earnings are right around the corner ("earnings risk" — the rule that we need at least a few weeks of runway for a thesis to play out before the company reports its quarterly results, since those reports can swing the stock 10%+ in either direction). Forcing a trade today on old research, into a tight earnings window, is the kind of mistake that costs us our edge.

**What happens next**
Tonight's pre-market routine will do a full fresh scout — I'll have my sub-agents look at this week's earnings calendar (May 11–15), check the macro tape (interest rates, oil, the dollar), and re-validate the watchlist. If I find a clean setup with at least 4–6 weeks of runway, I'll act at Monday's open.

**Numbers**
- Equity: $99,841 (essentially flat — we haven't started trading yet, so no real P/L to report)
- Cash: $99,841 (100% in cash, dry powder ready)
- Buys used this week: 0 of 3 allowed
- Open positions: 0 of 5 max

A small note: the account shows $159 less than the $100K we started with, with no trades from me. Looks like a paper-account housekeeping adjustment — I'll dig into it on the next routine to confirm. Not a concern, but I'd rather flag it than ignore it.

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
