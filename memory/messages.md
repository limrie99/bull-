# Messages from Bull

Append-only conversation log. **Most recent at the top.** Each entry is what Bull wants the user to see from a routine run.

Format:

```
## YYYY-MM-DD HH:MM CT · {routine name}

**Headline one-liner**

Body — short paragraph or bullets. What happened, what Bull decided, anything the user should know or decide on.
```

---

## 2026-05-25 08:35 CT · market-open

**Quiet day — market is closed for Memorial Day, so I'm standing down on trading.**

Today is Memorial Day (the US federal holiday honoring fallen service members), and the New York Stock Exchange and Nasdaq are both closed. I confirmed this directly with Alpaca's market clock — it shows the next open as tomorrow, Tuesday 5/26 at 9:30 AM ET / 8:30 AM CT. No trades can be placed today, so this routine is a no-op on the trading side.

A small honest disclosure on the account: equity reads **$99,840.95** vs. our $100K paper starting balance — about $159 lower than expected. Our trade log is empty, so there's nothing I did to cause that; it looks like a small paper-account adjustment from Alpaca. With zero positions, nothing is actively at risk, but I'll dig into it on the next live session.

The bigger thing you should know: I've been offline a while. The last real research entry I have is from **late April**, and a lot has happened in the market since then. My old plan (a small NVDA starter ahead of their 5/20 earnings) is **stale and not safe to execute** — that earnings print has already come and gone. So tomorrow's pre-market routine (Tuesday 5/26 at 6 AM CT) will be a **full fresh scout** — macro tone, earnings calendar for the holiday-shortened week, and a clean watchlist — before I touch the buy button.

**Numbers I care about today:**
- **$99,840.95 cash** (we started with $100K, so we're effectively still all-cash and dry powder ready).
- **0 of 5 position slots used, 0 of 3 weekly buys used.** Plenty of room to act when I see a real setup.
- **Next routine: Tuesday 5/26 pre-market (6 AM CT)**, then market-open at 8:30 AM CT.

Enjoy the long weekend. 🐂

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
