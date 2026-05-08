# Messages from Bull

Append-only conversation log. **Most recent at the top.** Each entry is what Bull wants the user to see from a routine run.

Format:

```
## YYYY-MM-DD HH:MM CT · {routine name}

**Headline one-liner**

Body — short paragraph or bullets. What happened, what Bull decided, anything the user should know or decide on.
```

---

## 2026-05-08 16:00 CT · weekly-review

**Week ending 2026-05-08: −0.09% | SPY +2.37% | alpha −2.45% | grade C−**

**What happened this week**
We did one trade, and it was a small loss. On 4/22 we bought 25 shares of NVIDIA (NVDA) at $201.38 — a starter position worth about 5% of the account. NVDA ran up to $216.73 on 4/27 (+7.6%), which triggered our "trailing stop" rule (an automatic sell that follows the stock up but locks in if it drops 10% from its peak). NVDA then reversed, and on 5/4 the trailing stop fired and sold us out at $195.02, a **−$159 loss (−3.16%)** on the trade. The rule did exactly what it's supposed to do — capped the loss well inside our −7% safety net.

**Why we still lost ground to the market**
The S&P 500 (SPY, the broad-market index we measure ourselves against) rallied **+2.37%** this week. We finished **−0.09%**, so our "alpha" — extra return vs. just owning the index — was **−2.45%**. The bigger culprit wasn't the NVDA loss; it was that we sat in cash for the four days after the stop-out (5/5–5/8) while the rally happened. NVDA itself recovered to $215.21 by Friday — if we'd held, we'd be up ~+6.9%. Classic whipsaw.

**The lesson I'm taking forward**
- **Don't enter on a single signal.** The strategy says "need at least 2" buy signals. NVDA had one (the AI tailwind). Sizing the position small didn't fix that — it just made the whipsaw cheap. Either find the second signal or pass.
- **Cash is not a default.** After a stop-out I should re-scout immediately, not idle for four days.
- **The trailing-stop rule is staying at 10%.** One whipsaw isn't a pattern; v1's data already proved tighter stops scalp us out of winners. We need three weeks of the same problem to consider changing it.

**One housekeeping fix**
Memory hygiene broke down — between 4/22 noon and today, no routine wrote anything to our notes, even though a real trade executed at the broker. I reconstructed the records from Alpaca today and added a memory-hygiene rule to `strategy.md` so every routine reconciles against the broker and writes a message, no matter how quiet.

**Numbers**
- Equity: **$99,840.95** (started the week at $99,926.75)
- Cash: $99,840.95 — 100% of the account is in cash heading into next week
- Year-to-date: account is essentially flat since 4/21 funding ($100,000 → $99,841 = −0.16%)
- Grade: **C−** — rules followed, loss capped, but single-signal entry + 4 idle days while SPY ran. Survivable, unimpressive.

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
