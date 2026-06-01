# Messages from Bull

Append-only conversation log. **Most recent at the top.** Each entry is what Bull wants the user to see from a routine run.

Format:

```
## YYYY-MM-DD HH:MM CT · {routine name}

**Headline one-liner**

Body — short paragraph or bullets. What happened, what Bull decided, anything the user should know or decide on.
```

---

## 2026-06-01 12:00 CT · midday

**Midday: steady, no changes — and for the first time in weeks that's a real decision, not a glitch.**

**What I did**
This is my first proper shift since we fixed the memory bug this morning. I checked our account live with the broker (Alpaca): we're holding **$99,840.95, all in cash, no stocks**. With nothing owned, there are no losses to cut and no winners to protect — so the risk-management part of midday is genuinely a no-op today.

**Why**
I also scanned the news for any "breaking catalyst" big enough to justify buying right now, midday, off-plan. The one standout was **Dell (DELL)**, up more than 30% today after strong earnings (the profit it reported) and raised guidance (the company lifting its own forecast). Tempting — but I'm passing for now. Buying a stock that's already jumped 30% in a single day means paying an extended price, and our automatic −7% safety-sell (a "stop loss") would likely get tripped by the normal post-jump wobble and kick us out at a loss. Chasing a spike isn't our game. I've put DELL on the list to study properly tomorrow once the dust settles.

**What happens next**
The bigger issue: we've sat in 100% cash for ~18 trading days while the market rose — that was the old bug, now fixed. Tomorrow's pre-market scan is the priority, and the goal is to actually put money to work if a stock clears our bar (two solid buy signals). I'll report back then.

**Numbers I care about**
- **$99,840.95 cash** — the full account (we started at $100,000), nothing at risk right now.
- **The market (SPY) is up ~0.6% today** — a green day we're not yet sharing in, which is exactly what tomorrow fixes.
- **0 of 5 position slots used, 0 of 3 weekly buys used** — plenty of room to deploy.

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
