# Messages from Bull

Append-only conversation log. **Most recent at the top.** Each entry is what Bull wants the user to see from a routine run.

Format:

```
## YYYY-MM-DD HH:MM CT · {routine name}

**Headline one-liner**

Body — short paragraph or bullets. What happened, what Bull decided, anything the user should know or decide on.
```

---

## 2026-05-26 06:00 CT · pre-market

**Back online after the long weekend — no trade planned for today's open. Here's why I'm sitting on my hands (for now).**

**What I did**
I'm awake again — your API keys are restored, so I could finally talk to Alpaca and Perplexity. I sent three research helpers out in parallel: one to read the overnight macro tape, one to map today's earnings calendar, and one to hunt for buy candidates. I then double-checked the top names myself against live price data.

**Why no trade**
The two best ideas were **NVDA** (the AI chip leader — they reported great earnings last Wed) and **PLTR** (AI/government software — they raised their forecasts on May 4). On paper both look strong. But:
- NVDA had a "sell-the-news fade" — it ran up 42% in a month before earnings, then dropped 8.6% off the high even though the numbers were great. If I bought now at $215 with our −7% safety net (the "hard stop" — an auto-sell if it falls too far), the stop would land right at $200, which is also its 50-day average price. Translation: there'd be almost zero room for normal wiggle. Not a margin of safety I'm willing to pay for.
- PLTR is trading **below** its 50-day average — that fails our "uptrend" rule (we don't try to catch falling knives). Wait.

The tape itself is **mildly risk-on** (Asia +2%, Europe firm, futures slightly green), but today's only big US data point is **Consumer Confidence** (a survey of how households feel about the economy — already at historic lows, so a miss could spook the market). And the real fireworks are tomorrow night when **Salesforce (CRM)** reports — that print sets the tone for the whole enterprise-software complex.

**What happens next**
Market-open routine in 2.5 hours: most likely no trade, just a tape read. I'll watch how NVDA behaves today — if it bases or reclaims $225, the setup improves. Real opportunity window opens Thursday morning if CRM prints clean.

**Numbers**
- $99,841 cash (essentially the full $100K starting stake; ~$160 of admin dust)
- 0 positions; 0 of 3 weekly buys used
- SPY closed Fri at $745.64, up +1.6% on the week — the market is trending, we are not. That's our patience cost; we'll only deploy when we have a real edge.

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
