# Messages from Bull

Append-only conversation log. **Most recent at the top.** Each entry is what Bull wants the user to see from a routine run.

Format:

```
## YYYY-MM-DD HH:MM CT · {routine name}

**Headline one-liner**

Body — short paragraph or bullets. What happened, what Bull decided, anything the user should know or decide on.
```

---

## 2026-05-22 12:00 CT · midday

**I'm back online — and we have some catching up to do. We're sitting in cash while the market has rallied.**

**What I did**
Reconnected to your Alpaca account and reconstructed what's actually been happening. The honest story: on 4/22 I bought 25 shares of NVIDIA (NVDA), and on 5/4 my trailing stop (an automatic sell that follows the price up — "trailing" means it locks in gains as the stock climbs, and sells if the stock falls 10% from its peak) triggered after the price dipped. Net result: a small loss of about $159, or -0.16% of the account. Then for the last 18 days I was effectively offline — my memory files were never updated, so I had no positions and never restarted the engine. Nothing happened this midday because there's nothing to manage (no positions = no stops to move, no risk-cap to worry about).

**Why this matters**
SPY (the S&P 500, our benchmark — the index of the 500 biggest US companies that we're trying to beat) is **up about 6.2% since we started**. We're down 0.16%. That gap (-6.4 points) is called negative "alpha" (alpha = how much we beat or miss the market by). The trailing-stop did its job — it cut a losing trade — but I didn't get back in the water after, and the market kept climbing without us. That's the lesson here: cash is only safe in the short term; long-term, sitting out a rising market is its own kind of risk.

**What happens next**
I'm not buying anything at midday — we're heading into a 3-day weekend (Memorial Day is Monday) and there's no breaking news that would justify rushing a trade in. Instead, I'll do a full fresh scouting pass at Tuesday morning's pre-market routine, looking at how NVDA's earnings (released 5/20) and the rest of our watchlist (MSFT, GOOGL, AVGO, PLTR, CRWD) actually printed. Goal: 1-2 starter positions at Tuesday's open if the signals line up. We won't chase the rally — we'll build positions deliberately.

**Numbers**
- Equity: **$99,840.95** (down $159 from our $100,000 start — basically flat)
- Cash: **$99,840.95** (100% of the account is cash — too much)
- Today: **flat** (no positions to move with the tape)
- SPY this week: +1.16%. Us: 0.00%. Alpha this week: **-1.16 points**
- Alpha since start: **-6.37 points** (the catch-up gap)
- Positions: **0 of 5 slots used** | New buys this week: **0 of 3 allowed**

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
