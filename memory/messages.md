# Messages from Bull

Append-only conversation log. **Most recent at the top.** Each entry is what Bull wants the user to see from a routine run.

Format:

```
## YYYY-MM-DD HH:MM CT · {routine name}

**Headline one-liner**

Body — short paragraph or bullets. What happened, what Bull decided, anything the user should know or decide on.
```

---

## 2026-05-25 12:00 CT · midday

**Quiet day — markets are closed for Memorial Day. Catching up on what's happened since we last talked.**

**What I did**
The US stock market is closed today for Memorial Day (a federal holiday — no trading happens, so I can't buy or sell anything until tomorrow morning). I used the quiet to do a clean audit of the account against the broker's records, because our local notes had a gap.

**Why**
Here's what I found and want to be upfront about: between April 22 and May 4, an earlier routine bought 25 shares of NVIDIA (the AI chip company, ticker NVDA) at $201.38 and was later stopped out at $195.02 — a small loss of $159 (about −3.2% on that one position, or −0.16% on the whole account). The exit was the **trailing stop** doing its job: a trailing stop is an auto-sell that follows the price up and only fires if the stock drops a set percentage (10% in our playbook) off its peak. NVDA ran up to $216 and then pulled back hard enough to trigger it. The trade itself was fine; what wasn't fine is that I never wrote it down in our log at the time. I've now backfilled the trade log so the paper trail matches the broker.

**What happens next**
Tomorrow morning (Tuesday) the market reopens and I'll do a full pre-market scan — NVDA, MSFT, GOOGL, and PLTR have all reported earnings since I last looked, so the picture has changed and there should be real setups to consider. Sitting in 100% cash any longer isn't free: while we've been on the sidelines, the broader market (the S&P 500, tracked by an ETF called SPY) has rallied about **+5.9%**, and we're up only −0.16%. That gap — about **−6% of "alpha"** (alpha = our return minus the market's return) — is the real cost of inaction. I'll be looking to put capital back to work tomorrow, carefully.

**Numbers I care about**
- Equity: $99,840.95 (down $159 from our $100K starting line — the NVDA round-trip)
- Cash: $99,840.95 (100% cash, 0 positions open)
- **Alpha vs SPY since we started: −6.06%** — we're behind the index and I want to start closing that gap

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
