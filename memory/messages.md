# Messages from Bull

Append-only conversation log. **Most recent at the top.** Each entry is what Bull wants the user to see from a routine run.

Format:

```
## YYYY-MM-DD HH:MM CT · {routine name}

**Headline one-liner**

Body — short paragraph or bullets. What happened, what Bull decided, anything the user should know or decide on.
```

---

## 2026-05-21 15:05 CT · market-close

**Close: equity $99,840.95 · day +0.00% · SPY +0.21% · alpha −0.21%**

Good news first — the keys are back, I can see Alpaca again, and we're sitting on $99,840.95 in cash with no open positions. Today the broader market (the S&P 500, tracked by an ETF called SPY) ticked up about a fifth of a percent. We made $0, so we underperformed by that same amount — being all in cash on an up day is the cost of having no positions on, which is exactly where we ended up.

The bigger story is something I owe you honestly: when I pulled the trade history just now, I found that **a NVDA trade actually went through on 4/22 that my notes claimed never happened.** Bought 25 shares at $201.38, the automatic safety-net sell order (the "stop loss") expired within seconds for a reason I haven't figured out yet, and the position sat unprotected for 12 days until it was sold on 5/4 at $195.02 — a small **−$159.04 loss**. That's why we're at $99,840.95 instead of the $100,000 we started with. I've back-filled this into the trade log so the record matches reality going forward.

**What I'm doing about it**
- Tomorrow morning's pre-market scout will *first* test that a bracket order's stop leg actually stays alive on the paper account before we buy anything. We don't put real money to work until that safety net is verified.
- Then I'll refresh the watchlist (NVDA, MSFT, GOOGL, AMZN, META all reported earnings during the blackout — fresh data needed).

**What happens next**
Quiet close tonight. Pre-market tomorrow at 6 AM CT we re-scout with a clean slate. Cash is dry powder; we'll deploy it deliberately, not in a rush to "catch up."

**Numbers**
- Equity $99,840.95 · cash $99,840.95 (100% — completely in cash)
- Down −$159.05 from the $100K start, all from that one unmonitored NVDA round-trip
- SPY this week +0.49% · us 0.00% · so we're behind the index by about half a percent week-to-date

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
