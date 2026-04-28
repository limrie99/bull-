# Messages from Bull

Append-only conversation log. **Most recent at the top.** Each entry is what Bull wants the user to see from a routine run.

Format:

```
## YYYY-MM-DD HH:MM CT · {routine name}

**Headline one-liner**

Body — short paragraph or bullets. What happened, what Bull decided, anything the user should know or decide on.
```

---

## 2026-04-28 12:00 CT · midday

**Midday: steady, no changes — Nvidia is taking a breather and that's fine.**

**What I did**
Nothing — and I want to explain why that's the right call. I checked our one open position (Nvidia, 25 shares), looked for any breaking news, and decided we're in good shape to sit tight and let the safety net do its work.

**Why**
Nvidia is down about 2.8% today after closing at an all-time high of $216.61 yesterday. The selloff is sector-wide — every chipmaker dipped on a CNBC story questioning whether OpenAI can really afford the massive AI computing power they've ordered. OpenAI pushed back hard, calling it "ridiculous." Our reason for owning Nvidia (they sell the picks and shovels for the AI buildout) is unchanged — this looks like a healthy pullback after a 29% one-month rally, not a thesis break.

Importantly, Nvidia is *still* up 4.6% from where we bought it. Earlier this week it was up 7.6%, and that high triggered our **trailing stop** — an automatic sell order that follows the price up but only ratchets one way. Right now it sits at $195.06; if Nvidia drops to that, we sell automatically. So even on a red day, our downside is capped.

**What happens next**
I'll check in at the close (3:00 CT) and again pre-market tomorrow. If chips keep selling off, the trailing stop handles it. Earnings are May 20 — still 22 days out.

**Numbers**
- Equity: $100,229 (down $152 today, -0.15%) — SPY is down -0.73%, so we *beat* the market by +0.58% today
- NVDA: +$230 from entry, trailing stop at $195.06
- Cash: $94,965 — about 95% dry powder, ready when the right setup appears

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
