# Messages from Bull

Append-only conversation log. **Most recent at the top.** Each entry is what Bull wants the user to see from a routine run.

Format:

```
## YYYY-MM-DD HH:MM CT · {routine name}

**Headline one-liner**

Body — short paragraph or bullets. What happened, what Bull decided, anything the user should know or decide on.
```

---

## 2026-04-27 06:05 CT · pre-market

**Quiet plan today — holding NVDA, no new buys, big tech earnings mid-week is the real event.**

**What I did**
I checked the account, our one position (NVDA — the AI-chip giant), the overnight news, and the earnings calendar. I also scouted for new buy ideas. Result: I'm not placing any trades today, and I want to walk you through why so it's clear that "doing nothing" was the right move, not a miss.

**Why**
Three reasons. First, the **macro tape is mildly risk-off** — the S&P 500 fell 1.67% Friday on Middle-East war worries and an oil-price spike, and futures only ticked up a tiny 0.09% overnight. That's digestion, not a bounce. Second, **Wednesday after the close is the dominant catalyst this week** — Google, Meta, and Microsoft all report earnings (the quarterly scorecard a public company gives investors) on the *same evening*. A clean set of beats lifts the whole market Thursday; one bad guide drags it down. Buying tech today and getting blindsided 48 hours later would be undisciplined. Third, my opportunity scout couldn't verify two strong "buy signals" on any new name this morning — and our rule says we need at least two confirmed reasons, not gut feel.

**What happens next**
I'm watching NVDA closely. It closed Friday up 4.3% on heavy volume after Intel's blowout earnings lit up the chip sector and NVDA announced a long-term nuclear-power partnership for AI data centers. If NVDA keeps climbing and crosses **+5% gain** from our entry (at about $211.45), I swap our fixed safety net (the −7% "hard stop" — auto-sell if it falls 7% from where we bought) for a **trailing stop** — a smarter safety net that locks in gains as the stock keeps rising. We're at +4.45% right now, just 55¢ away from that switch. Midday routine will check.

**Numbers**
- Equity: $100,224 (up $52 from Friday, +0.05%) — tiny tick higher
- NVDA: 25 shares, +$224 unrealized gain (+4.45%); safety-net price $187.28
- Cash left: $94,966 — about 95% of the account is still cash, by design while we look for the right second name

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
