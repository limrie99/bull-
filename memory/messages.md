# Messages from Bull

Append-only conversation log. **Most recent at the top.** Each entry is what Bull wants the user to see from a routine run.

Format:

```
## YYYY-MM-DD HH:MM CT · {routine name}

**Headline one-liner**

Body — short paragraph or bullets. What happened, what Bull decided, anything the user should know or decide on.
```

---

## 2026-05-21 06:00 CT · pre-market

**Good morning Lauren — we're back online, and Nvidia just handed the AI story a clean win.**

**What I did**
Nothing in the account yet — the market doesn't open for another two and a half hours and pre-market is for research, not trading. I pulled live data from our broker (Alpaca) to confirm we're at $99,841 in cash with zero positions, then sent my research team (sub-agents) to sweep the macro tape, the earnings calendar, and to find buy candidates.

**Why**
Yesterday after the close, **Nvidia (NVDA) reported earnings** — earnings is when a public company tells investors how much money it made last quarter. Nvidia crushed it: revenue $81.6B vs $78.4B expected (a "beat"), they raised next quarter's forecast (called "guidance") to $91B, and their data-center business — the part that sells AI chips — grew 92% year-over-year. Despite that, the stock dipped about 1.3% after-hours because traders had already priced in a great print (we call that "priced for perfection"). The setup matters because Nvidia's print sets the tone for the whole AI complex.

Beyond NVDA, my scout found four other large companies that recently reported strong beats AND raised guidance — **AMAT (Applied Materials), WMT (Walmart), INTU (Intuit), TJX**. All five are clean of the 3-day earnings blackout (our rule that says don't open a new position right before a company reports). That's a target-rich morning.

**What happens next**
At the 8:30 AM CT market-open routine I'll act on this plan:
- **AMAT** ~15% of the account — purest "picks-and-shovels" AI play that just beat-and-raised, less crowded than NVDA.
- **WMT** ~10–12% — defensive anchor; their raised guide tells you the consumer business is healthy.
- **NVDA** ~10% — but ONLY if it opens down a couple percent and stabilizes. If it gaps up and rips, I sit out — chasing crowded longs is how money gets burned.
- Each buy gets a "bracket order" — a safety net that automatically sells if the price drops 7% from where I bought. Standard risk control.

**Numbers I care about**
- Cash: **$99,841** (about $159 below our $100K start — no trades happened, just a paper-account drift Alpaca shows; nothing real lost).
- Positions: **0 of 5 allowed**.
- Buys-this-week budget: **0 of 3 used**.
- SPY (the overall US market) last close: **$740.86** — that's our benchmark. The only number that matters long-term is whether we beat it.

I'll be back at 8:30 CT with the actual trade decisions. 🐂

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
