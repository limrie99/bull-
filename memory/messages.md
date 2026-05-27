# Messages from Bull

Append-only conversation log. **Most recent at the top.** Each entry is what Bull wants the user to see from a routine run.

Format:

```
## YYYY-MM-DD HH:MM CT · {routine name}

**Headline one-liner**

Body — short paragraph or bullets. What happened, what Bull decided, anything the user should know or decide on.
```

---

## 2026-05-27 06:00 CT · pre-market

**Good morning, Lauren — we're back online, and I've found our first real candidate: Eli Lilly.**

After a few weeks where the system couldn't log in (the access keys were missing, so I had to sit on my hands), everything's working again. We're still 100% in cash — about $99,841, essentially the full $100,000 we started with — so we've taken zero risk and lost nothing while we waited. This morning I sent out my research team to scan the market, and here's the plan:

- **No company I care about reports earnings today**, so today is driven by the broader market mood, not by any single result. (Costco reports *tomorrow* — I'm steering clear of it until then, because buying right before a company's earnings report is a coin-flip, and we don't gamble.)
- **The market mood is calm-to-slightly-positive** — stock futures (early bets on where the market opens) are barely up, tensions in the Middle East are easing. The one thing I'm watching is oil, which is a bit high and can stir up inflation worries.
- **My top idea is Eli Lilly (LLY)** — the maker of the blockbuster weight-loss drugs Zepbound and Mounjaro. It hits three of our buy signals at once: a powerful long-term demand trend, several Wall Street analysts raising their price targets this month, and a strong, steady uptrend in the share price. Its next earnings report isn't until August, so there's no near-term landmine.
- **What happens next:** I do NOT trade in this routine — the market is still closed. At the 8:30 AM CT open I'll re-check live prices and, if things still look calm, likely start a position in Lilly with an automatic safety-net sell order (a "stop loss") 7% below our entry. I'll keep most of our cash in reserve.

I'll write again right after the opening bell. 🐂

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
