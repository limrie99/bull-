# Messages from Bull

Append-only conversation log. **Most recent at the top.** Each entry is what Bull wants the user to see from a routine run.

Format:

```
## YYYY-MM-DD HH:MM CT · {routine name}

**Headline one-liner**

Body — short paragraph or bullets. What happened, what Bull decided, anything the user should know or decide on.
```

---

## 2026-05-18 06:10 CT · pre-market

**We're back online — but I'm holding fire at the open. Here's the read.**

**What I did**
First thing, I confirmed everything works: Alpaca and Perplexity both responded, our paper account is sitting at **$99,840.95 cash, zero positions** — exactly where we left it. Then I spun up three research sub-agents in parallel (one for macro, one for earnings, one to hunt buy ideas) and cross-checked their work against fresh price data from Alpaca.

**Why I'm not buying at the open**
Friday's tape told a clear story: **semiconductors got smoked** (NVDA −4.5%, AMD −5.7%, MU −6.6%) while **cybersecurity names ran higher against the red tape** (CRWD +2.5%, PANW +1.9%, MSFT +2.8%). That's called **sector rotation** — money leaving one corner of the market and crowding into another — and rotation into cyber on a down day is a real signal. Normally I'd open a cyber starter (a small first tranche, ~5% of the account) at the open this morning. The blocker: I couldn't verify when CRWD and PANW next report earnings, and our playbook says **never open inside a 3-trading-day earnings window** (too much gap-down risk if they miss). CRWD/PANW both historically report mid-to-late May, so they could easily be in that window this week.

Also, Middle-East oil spiked overnight (WTI +1.15% on a UAE strike headline) — risk-off in the air, not a clean "lean in" morning.

**What happens next**
At market-open (8:30 CT), my first job is one tight Perplexity call to nail down the next-earnings dates for CRWD, PANW, MSFT, and a few others. If CRWD or PANW prints **more than 3 trading days out**, I'll open a 5–7% starter ($5K–$7K) in the cleaner one with our standard −7% hard stop (the automatic safety-net sell). If both are inside the blackout, I'll consider a smaller 5% MSFT starter as a defensive AI/cloud foothold. If oil spikes another 2% or futures roll red, I pass entirely.

**Numbers I care about**
- **Cash: $99,840.95** (paper account, zero positions — fully dry powder).
- **3 buys remaining this week** (the gap reset our weekly counter).
- **NVDA is on the bench** — it reports earnings Wed 5/20 after the close, and we don't open new positions inside the 3-day blackout. Revisit Thursday.

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
