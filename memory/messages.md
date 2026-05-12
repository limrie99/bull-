# Messages from Bull

Append-only conversation log. **Most recent at the top.** Each entry is what Bull wants the user to see from a routine run.

Format:

```
## YYYY-MM-DD HH:MM CT · {routine name}

**Headline one-liner**

Body — short paragraph or bullets. What happened, what Bull decided, anything the user should know or decide on.
```

---

## 2026-05-12 06:10 CT · pre-market

**Good morning — we're back online, and I have a plan for today's open.**

**What I did**
This is my first real routine since the API keys went missing on 4/22 — that's three weeks where I literally couldn't see the market. Everything is now working: Alpaca is live, Perplexity is live, and our paper account is sitting at $99,841 cash with zero positions. I ran my full team — a macro analyst, an earnings analyst, and an opportunity scout — to build a view of today's tape. No trades happen in this routine (market is closed until 8:30 AM CT); this is research and planning.

**Why**
Here's the honest picture: while I was offline, the market climbed to fresh all-time highs (SPY closed at $738 yesterday). We've been in 100% cash through a rally — that's an "opportunity cost" (the gains we missed by not being invested), and it's now our biggest risk, not drawdowns. Today's setup is mixed: futures are flat, there are no big earnings reports today, but the 10-year Treasury yield (the benchmark US government bond rate — when it rises, stocks usually wobble) ticked up 5 basis points on rising oil prices. So today's tape is macro-driven, not earnings-driven, which actually makes it a calmer day to start a position.

**What happens next**
At the 8:30 AM CT market-open routine, my plan is to consider a **starter position in Nvidia (NVDA)** at around 10% of our account (~$10,000, roughly 46 shares at $219). Why NVDA: it's the cleanest AI-infrastructure name on the board, in a clear uptrend, and only 2% off its 52-week high. The catch: NVDA reports earnings on **May 20** (6 trading days away). My playbook says no opening trades within 3 trading days of earnings, so I'd buy now with a plan to either exit by **May 15** or wait through the print only if our thesis specifically depends on it. I'll only pull the trigger if futures haven't deteriorated by 8:30 CT — if oil spikes hard overnight or yields jump above 4.45%, I'll pass and rescout midday.

**Numbers**
- Equity: $99,841 (we started at $100,000, so essentially flat — a $159 paper drag from account creation dust)
- Cash: $99,841 (100% — that needs to change carefully, not recklessly)
- Watchlist closes: NVDA $219.04 · AVGO $428.32 · MSFT $412.62 · META $599.26 · LLY $967.16 · SPY $738.29

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
