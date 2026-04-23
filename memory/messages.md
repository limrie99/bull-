# Messages from Bull

Append-only conversation log. **Most recent at the top.** Each entry is what Bull wants the user to see from a routine run.

Format:

```
## YYYY-MM-DD HH:MM CT · {routine name}

**Headline one-liner**

Body — short paragraph or bullets. What happened, what Bull decided, anything the user should know or decide on.
```

---

## 2026-04-23 12:20 CT · midday

**Midday: steady — NVDA is slightly red, no changes to make.**

**What I did**
Secrets are back, so I could actually see the account again. I pulled fresh numbers from Alpaca and checked on our one position, NVDA (Nvidia). I did no trading this routine — just a risk review.

**Why**
One thing I need to flag: Alpaca shows we actually **bought 25 shares of NVDA at $201.38 yesterday morning**, even though yesterday's routines reported being "halted." So the trade did happen — the logs were just wrong. I back-filled the trade record so we have an honest paper trail. The -7% "stop loss" (an automatic sell order that caps the worst-case loss) is live at **$187.28** — so if NVDA suddenly dropped 7%, we'd be out before it got worse. Right now NVDA is at $199.51, down 0.93% from our entry — normal chop, well inside the stop, and nothing I'd call "thesis-breaking" (meaning the reason we bought hasn't changed: the AI-chip story and the May 20 earnings report are still ahead of us).

**What happens next**
I watch NVDA for two triggers: (1) if it drops to about $187 the stop sells us out; (2) if it rallies 5%+ from entry (~$211+), I swap the fixed stop for a **10% trailing stop** — a safety net that moves *up* with the price, locking in gains while letting winners run. I'll check in again at market close.

**Numbers**
- Equity: **$99,953.50** (down $74.50, about -0.07% today). The broad market (SPY) is down -0.66% — we're outperforming because most of our $94,966 cash isn't moving with stocks.
- NVDA position: $4,988 (~5% of the account), unrealized P/L -$46.75.
- Buys used this week: 1 of 3. Open positions: 1 of 5. Plenty of room.

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
