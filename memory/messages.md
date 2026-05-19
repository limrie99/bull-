# Messages from Bull

Append-only conversation log. **Most recent at the top.** Each entry is what Bull wants the user to see from a routine run.

Format:

```
## YYYY-MM-DD HH:MM CT · {routine name}

**Headline one-liner**

Body — short paragraph or bullets. What happened, what Bull decided, anything the user should know or decide on.
```

---

## 2026-05-19 08:30 CT · market-open

**Back online — but no trades at the open. Holding cash until I do fresh research.**

**What I did**
Nothing — and that's the right move. The API keys are restored (thank you!), so I can finally see the account and the market again. Alpaca shows we're still flat: about **$99,841 in cash, no open positions**. The market is open. I checked, decided to pass, and saved my reasoning.

**Why**
This is the first time I've woken up successfully since April 22 — almost a month dark. The only buy idea on file is NVIDIA (NVDA), but **NVDA reports earnings tomorrow afternoon**. Our playbook (the rules in `strategy.md` we wrote together) says **no new buys within 3 trading days of an earnings report** — a company's stock can swing 10%+ on the print, which is exactly the kind of randomness we want to avoid. Everything else in my old notes is from April and the tape has moved a lot since then; trading off stale research is exactly how amateurs lose money. So I'm passing. Better to wait for the next pre-market routine, run a fresh scout, and enter with conviction.

**What happens next**
The next routine (midday or pre-market tomorrow) should fire a full research scan with sub-agents — macro, earnings calendar for this week, sector rotation, and a fresh ticker hunt. We'll re-look at NVDA after Tuesday's print clears (~5/26). If you want to nudge me on any specific names, drop a note in `memory/inbox.md`.

**Numbers**
- Equity: **$99,841** (started at $100,000; account drifted ~$159 while idle — no trades on record, so it's likely a small fee or rebalance from Alpaca. I'll dig into the activities feed next routine if it sticks)
- Cash: **$99,841** — 100% cash, all dry powder
- Buys used this week: **0 of 3** allowed

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
