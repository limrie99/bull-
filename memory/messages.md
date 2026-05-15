# Messages from Bull

Append-only conversation log. **Most recent at the top.** Each entry is what Bull wants the user to see from a routine run.

Format:

```
## YYYY-MM-DD HH:MM CT · {routine name}

**Headline one-liner**

Body — short paragraph or bullets. What happened, what Bull decided, anything the user should know or decide on.
```

---

## 2026-05-15 12:05 CT · midday

**Midday: quiet by design — but I reconciled a missing chapter from a few weeks back.**

**What I did**
First thing this routine: when I asked our broker (Alpaca) for the account, the cash came back as $99,840.95 — not the $100,000 my notes said we had. So I pulled the broker's activity feed and found three trades from April and May that my memory never logged. I'll explain them below. No new trades today — midday rules say no buys unless there's a breaking catalyst, and I don't see one.

**Why**
Between April 22 and May 4, an earlier session of mine actually did execute the NVIDIA (NVDA) starter trade we'd been planning, ran it through our normal risk rules, and exited cleanly when our safety net tripped. Here's the story in order:

1. **April 22:** Bought 25 shares of NVDA at $201.38 (~$5,034, about 5% of the account). At the same time I set a "hard stop" — a standing order to auto-sell if the price dropped 7% (to $187.12).
2. **April 27:** NVDA had run up more than 5% in profit, so per our playbook I swapped the hard stop for a "trailing stop" — a smarter version that follows the price up. Set it to lock in a sell if the price ever fell 10% from its highest point.
3. **May 4:** NVDA peaked at $216.73 (up ~7.6% from our entry), then pulled back. The trailing stop kicked in around $195 and sold all 25 shares.

Result: realized loss of **−$159.04 (−3.16%)** on that position, which is ~−0.16% of our total account. Why I'm calling this a *clean* execution even though it lost money: the trailing stop did exactly what it's designed to do — let a winner breathe, then cap how much profit we give back. It's the same mechanic that locked in big wins in v1 of this account.

The frustrating footnote: NVDA is back at $227.92 today, so if we'd held we'd be up ~13%. That happens with trailing stops sometimes — we trade the occasional missed rebound for protection against the bad days. I'm not going to relitigate it.

**What happens next**
Today the market is down about 0.93% intraday and we're 100% cash — so we're outperforming SPY (the S&P 500 index that tracks the overall US market) by roughly +0.93% on the day, just by sitting still. That's not a strategy long-term (cash drags in up markets), but it's a small silver lining today. My research notes are 23 days stale, so I won't fire off buys on old theses. The next **pre-market routine** will do a fresh scout — I'll especially look at NVDA again (their earnings are May 20, which is 3 trading days from today; I either buy now or wait until after the print, per our rules) plus the rest of our watchlist.

**Numbers**
- Equity: **$99,840.95** (down $159.05 from our $100,000 start — that's the realized NVDA loss, fully accounted for)
- Cash: $99,840.95 (100% — nothing in the market right now)
- Day P/L: $0 (we're flat because we hold nothing); SPY: −0.93%; **intraday alpha (extra return vs SPY): +0.93%**
- New buys used this week: 0 of 3; open positions: 0 of 5

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
