# Messages from Bull

Append-only conversation log. **Most recent at the top.** Each entry is what Bull wants the user to see from a routine run.

Format:

```
## YYYY-MM-DD HH:MM CT · {routine name}

**Headline one-liner**

Body — short paragraph or bullets. What happened, what Bull decided, anything the user should know or decide on.
```

---

## 2026-05-29 16:00 CT · weekly review

**Week ending 2026-05-29: 0.00% | SPY +1.43% | alpha −1.43% | grade D**

**What happened this week**
Nothing — and that's the problem. I didn't place a single trade, didn't sell anything, didn't move a stop. The account sat in cash all week ($99,840.95) while SPY (an index fund that tracks the whole US stock market, our scorecard) climbed 1.43%. So I underperformed the market by 1.43% — that gap is called **negative alpha** (alpha = our return minus the market's return; positive alpha means we beat the market, negative means we lagged it).

**Top win:** Honestly, none this week. The closest thing to a "win" is that nothing in the account lost money — but that's because nothing was in the account to lose money in the first place. That's not a win, that's just luck of standing still.

**Top loss:** **Opportunity cost.** Sitting 100% in cash while the market rallies is itself an expensive bet — we're effectively betting that stocks will fall, and they didn't. Tech and chips led the tape this week and we participated in zero of it. This is now our fifth straight week with no new trades (the last activity was the NVDA stop-out back on 5/04, which closed for a small −$159 loss).

**Lesson:** Holding cash isn't safe — it's a bet. When the market goes up and we're not in it, we lose. We need to get back to actively scouting candidates next week. The rulebook is fine; the issue is that the research routines haven't been firing.

**Strategy change:** None. One quiet week isn't enough data to change the rules — I only adjust when I see the same mistake repeat over 3+ weeks. The fix here is execution, not rewriting the playbook.

**What happens next:** I'll resume the normal cadence starting Monday's pre-market scan (Mon 6/01). Goal for next week: at least one validated buy candidate written up, and a real trade by Wed 6/03 if any name cleanly hits 2+ of our buy signals. If not, I'll still report in every routine so you know I'm awake.

**Numbers I care about**
- Equity: $99,840.95 (basically unchanged for over 3 weeks now)
- Cash: $99,840.95 — 100% cash, which is the wrong allocation when the market is grinding higher
- Year-to-date vs SPY: we are behind SPY by a widening margin since 5/04; precise number next routine

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
