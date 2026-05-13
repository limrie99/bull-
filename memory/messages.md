# Messages from Bull

Append-only conversation log. **Most recent at the top.** Each entry is what Bull wants the user to see from a routine run.

Format:

```
## YYYY-MM-DD HH:MM CT · {routine name}

**Headline one-liner**

Body — short paragraph or bullets. What happened, what Bull decided, anything the user should know or decide on.
```

---

## 2026-05-13 12:00 CT · midday

**I'm back online — and I owe you a catch-up on what happened while my memory was offline.**

**What I did**
First successful wake-up since April 22nd. The trading system itself kept running on Alpaca's side even while my memory files were stuck — so I went back through the broker records and reconstructed what happened. On April 22nd I bought 25 shares of NVIDIA (NVDA, the AI chipmaker) at $201.38. On April 27th, once it was up about 5%, I switched the safety net from a fixed "stop loss" (a pre-set price at which I automatically sell to cap a loss) to a **trailing stop** (a stop price that follows the share price up but never down — it locks in gains as a stock rises). On May 4th that trailing stop fired and sold all 25 shares at $195.02, for a small loss of $159.

**Why this is worth understanding**
The trailing stop did its job mechanically — NVDA had reached about $217 (a +7.6% high water mark for us) and then pulled back 10% off that peak, which is exactly the rule. The catch: NVDA has since rallied back to about $227, so in hindsight the trail caught a normal wiggle rather than a real reversal. That's the cost of using a rule instead of guessing — sometimes the rule taps you out early. I'd rather pay that cost than freelance.

**The bigger issue**
Since April 21st, the S&P 500 (SPY, the index that tracks the 500 largest US companies — our benchmark) is up about **+5.48%**, and we're at **-0.16%**. So we're behind the market by about 5.6% on the scoreboard — almost entirely because we've been sitting in cash through a rally. Concentration is fine; doing nothing is not.

**What happens next**
Nothing this routine — midday's job is risk management, and we have no positions to manage. The next pre-market scout needs to actually pull the trigger when 2+ buy signals line up, not wait for a perfect setup. I'll check in at market close.

**Numbers**
- Equity: **$99,840.95** (we started at $100,000, so down $159 net — basically flat)
- Cash: **$99,840.95** (100% in cash — nothing at risk, but also nothing earning)
- SPY since inception: **+5.48%** · Us: **-0.16%** · **Alpha: -5.64%** (alpha = our return minus the index; negative means we're trailing)

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
