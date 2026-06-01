# Messages from Bull

Append-only conversation log. **Most recent at the top.** Each entry is what Bull wants the user to see from a routine run.

Format:

```
## YYYY-MM-DD HH:MM CT · {routine name}

**Headline one-liner**

Body — short paragraph or bullets. What happened, what Bull decided, anything the user should know or decide on.
```

---

## 2026-06-01 10:40 CT · pre-market

**Morning scan done — I've lined up our shopping list. NVDA (the AI-chip leader) is at the top, and I plan to buy at the next routine.**

**What I did**
This is my first real research scan since we fixed the memory bug, so I sent out four research helpers at once — one for the overall market, one for earnings, and two hunting for stocks to buy. I placed **no trades** (this is a research-only shift), but I pulled live prices to check each idea against our rules. We're still 100% cash at $99,840.95.

**Why**
The market is at record highs and "risk-on" (investors feeling confident), with AI-related tech clearly leading. My top pick is **Nvidia (NVDA)** — it reported earnings on May 20 that beat expectations on both sales and profit *and* raised its forecast (a "beat-and-raise," our strongest buy signal), it rides the AI build-out, and it's in a clear uptrend (price above its recent average). It hits 3 of our signals and its next earnings aren't until August, so there's no near-term surprise risk. Runners-up: Google (GOOGL) and IBM. I'm avoiding Broadcom (AVGO) for now — it reports Wednesday, and we never buy right before earnings.

**What happens next**
At the next market-open routine I intend to open a starter position in NVDA (with an automatic safety-sell 7% below our cost — a "stop loss"), as long as nothing breaks overnight. I'll confirm the others' earnings dates first.

**Numbers I care about**
- $99,840.95 cash — 100% of the account, nothing at work yet (we want to fix that)
- NVDA ~$220.42, well above its ~$200 50-day average — confirms the uptrend
- 0 of 3 weekly buys used; room for up to 5 positions

---

## 2026-06-01 · system repair (from the user, not a routine)

**Fixed the bug that quietly erased my memory every day for six weeks. Back to a clean, true baseline.**

Here's what was wrong, in plain terms. Every time I woke up, I was reading my notes from **April 22** — not from my last shift. My writes were being saved to a throwaway scratch pad nobody ever read again, so I started each day amnesiac. That's why I kept saying "the plan is stale, I won't trade" — *every* plan looked stale, forever. Over the month that meant: one NVDA trade (in 4/22, out 5/4 at **−$159**), then **~18 trading days sitting in 100% cash** while I researched names like GOOGL, MSFT, PLTR, LLY and never bought any. For an account whose only job is to beat SPY, sitting out a rising market is the real loss here — bigger than the $159.

**What's fixed now:**
- My memory actually saves and reloads between shifts (the git push now targets the real shared branch, and I reload it at the start of every routine).
- New rule: a stale plan can never again mean "do nothing indefinitely." If I wake up with no fresh plan and the market's open, I build one *that shift* and act on it — within all the same guardrails (2+ signals, −7% stop, max 5 positions, 3 buys/week).
- Account is verified flat: **$99,840.95, all cash, no positions.** Clean slate for the next real pre-market scan.

Nothing about your risk rules changed — they barely got to run, so there's nothing to retune yet. Next pre-market should actually put money to work if a name clears the bar.

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
