# Messages from Bull

Append-only conversation log. **Most recent at the top.** Each entry is what Bull wants the user to see from a routine run.

Format:

```
## YYYY-MM-DD HH:MM CT · {routine name}

**Headline one-liner**

Body — short paragraph or bullets. What happened, what Bull decided, anything the user should know or decide on.
```

---

## 2026-04-24 06:00 CT · pre-market

**Quiet Friday — holding NVDA, not buying anything today.**

**What I did**
I pulled overnight macro, scanned the earnings calendar, checked NVDA for news, and had my opportunity scout review a 17-name watchlist. I reconciled one loose end too: an NVDA buy from Wednesday (25 shares @ $201.38) never made it into the trade log because the earlier routines that day halted on missing API keys — I've backfilled that entry now so our records match Alpaca.

**Why**
Three reasons to sit tight. First, **Fridays rarely have big earnings**; the mega-cap tech cluster — Google, Microsoft, Meta — reports next Tuesday/Wednesday (around April 29), so the tape-moving news is a few days away. Second, **oil is near $100** on Middle East tensions, which tends to drag on expensive tech stocks because it pushes up interest rates (a "macro headwind"). Third, my scout couldn't verify two fresh buy signals on any watchlist name — and our playbook requires at least two. Forcing a mediocre buy into a quiet, headwind-y Friday is exactly the mistake we're trying to avoid.

**NVDA quick check:** Thesis still intact — Google Cloud announced on Wednesday that it's expanding its AI supercomputer on NVIDIA's next-gen chips, which is bullish for NVDA demand. No bad news, no analyst downgrades. I'm holding.

**What happens next**
I'll check in again at midday. The NVDA stop stays at $187.28 — if it ever drops there, I sell automatically to cap the loss at -7%. Once NVDA is up +5% from our entry (at $211.45), I'll swap that fixed stop for a "trailing stop" — a stop that automatically ratchets up as the price climbs, so we lock in gains.

**Numbers I care about**
- Equity $99,981.50 (basically flat since Wednesday — we started with $100,000)
- Cash $94,965.50 — about 95% of the account is still cash, waiting for a better setup
- 0 of 3 weekly buys used; 1 of 5 position slots filled

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
