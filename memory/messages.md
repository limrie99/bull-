# Messages from Bull

Append-only conversation log. **Most recent at the top.** Each entry is what Bull wants the user to see from a routine run.

Format:

```
## YYYY-MM-DD HH:MM CT · {routine name}

**Headline one-liner**

Body — short paragraph or bullets. What happened, what Bull decided, anything the user should know or decide on.
```

---

## 2026-04-29 12:00 CT · midday

**Midday: steady, no changes — NVDA cooling off but our safety net is well in place.**

**What I did**
Nothing on the trading side. I checked our one open position (NVDA), the account, and the live tape. No buys, no sells, no stop changes — the right move when nothing in our playbook is shouting at us.

**Why**
NVDA is up +4.11% from where we bought it, and earlier this week it ran higher and triggered our switch to a "trailing stop" — that's an automatic sell that follows the stock up but stays 10% below its highest price. So our worst-case exit is now $195.06, which is *above* what we paid, meaning even if NVDA rolled over hard, we'd lock in a small profit. Today it slipped about -1.65% on no specific news, which is normal noise. Our rules only force a news check on positions down -7% or worse, and we're nowhere near that. Everything else is calm: we're down just $88 on the day (-0.09%), well within our 3% daily loss limit, so trading isn't restricted.

**What happens next**
I'll run a fresh pre-market scout tomorrow morning to look for new ideas — we've got room for up to 4 more positions and used 0 of our 3 weekly buys so far. NVDA's earnings are 5/20, still ~14 trading days out, so no blackout pressure yet. Next check-in: market close (3:00 CT).

**Numbers**
- Equity: **$100,206** (+0.03% on the week, while SPY is **-0.60%** → we're +0.63% ahead of the market this week)
- NVDA: 25 shares, +$207 unrealized, stop at $195.06 (a $14+ cushion)
- Cash: **$94,966** — about 95% still in cash, plenty of dry powder for the next setup

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
