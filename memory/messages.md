# Messages from Bull

Append-only conversation log. **Most recent at the top.** Each entry is what Bull wants the user to see from a routine run.

Format:

```
## YYYY-MM-DD HH:MM CT · {routine name}

**Headline one-liner**

Body — short paragraph or bullets. What happened, what Bull decided, anything the user should know or decide on.
```

---

## 2026-04-30 08:40 CT · market-open

**Open: no new trades — caught up on memory and confirmed our NVDA position is in good shape.**

**What I did**
First successful routine since the API keys went missing on 4/22, so my first job was to reconcile what my notes said vs. what's actually in the brokerage account. They had drifted apart. Alpaca shows we own **25 shares of NVIDIA at an average cost of $201.38** (bought 4/22) — that part of my memory was blank because the routines that should have written it down had halted on missing keys. I've now backfilled that into the trade log and the portfolio file. No new buys today — I don't have fresh pre-market research for 4/30, and our playbook is "no entries without a thesis."

**Why**
NVIDIA is up about **+3.2% from our entry**, and the position already has the right safety net on it: a **10% trailing stop** (an automatic sell that follows the stock up but never down — so if NVDA is at $216 and drops 10%, we're out). That swap from the original −7% safety net to the trailing stop happened on 4/27 once we crossed +5% profit, exactly the way our strategy says to do it. No bad news on NVIDIA in the last 48 hours, so the original reason for owning it (Blackwell chip ramp, AI data-center buildout) is still intact.

**What happens next**
I'll watch NVDA into its earnings on **2026-05-20** (about three weeks away). Tomorrow morning's pre-market routine should surface a fresh list of buy candidates — we have a lot of cash sitting idle and only one position, so I'd like to add 1–2 more good names if I can verify the signals.

**Numbers**
- **Equity: $100,161** — basically dead-flat to where we started ($100,000), and dead-flat to SPY over the same window (SPY +0.09% since 4/22). No alpha yet — too early to read into.
- **Cash: $94,966** — about 95% of the account, plenty of dry powder.
- **NVDA: 25 sh, +$160 unrealized**, trailing stop triggers at **$195.06** (a $260 max loss from here, locks in $1.43/sh of gains).
- **0 of 3 weekly buys used.**

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
