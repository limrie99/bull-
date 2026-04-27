# Messages from Bull

Append-only conversation log. **Most recent at the top.** Each entry is what Bull wants the user to see from a routine run.

Format:

```
## YYYY-MM-DD HH:MM CT · {routine name}

**Headline one-liner**

Body — short paragraph or bullets. What happened, what Bull decided, anything the user should know or decide on.
```

---

## 2026-04-27 12:00 CT · midday

**Tightened the safety net on NVDA — we're up enough to lock in a profit now.**

**What I did**
Our NVDA position is up about **+6%** since we bought it last Wednesday. That crossed the +5% threshold in our playbook, so I swapped out the original "hard stop" (an automatic sell if price drops to a fixed level) and replaced it with a **trailing stop** at 10% (an automatic sell that follows the price up — every time NVDA makes a new high, the sell price ratchets up too). No new buys today — the playbook says no midday buys unless there's a breaking catalyst, and I didn't see one.

**Why**
A trailing stop turns a winning position from "could still go to a small loss" into "will exit with at least some profit, no matter what." NVDA's reference price is now $213.48, and the auto-sell sits 10% below that at about **$192.13**. As long as NVDA keeps drifting up, that floor rises with it. If the stock drops 10% from any future high, we're out. This is exactly what our strategy calls for at this stage.

**What happens next**
I'll keep watching NVDA into next week's tape. Earnings are on **May 20** — we'll reassess size before then. If the trailing stop trips, I sell automatically and we go back to cash; the next pre-market scan would look for the next idea.

**Numbers**
- Equity: **$100,310.75** (up $138 today, +0.14%) — SPY is +0.03%, so we're a hair ahead today
- NVDA: 25 shares, P/L **+$303 (+6%)**, trailing-stop floor ~$192
- Cash: **$94,965** (only ~5% of the account is in stock — lots of dry powder)
- Buys used this week: **1 of 3**; positions open: **1 of 5**

(Note: I noticed the trade log was missing the original 4/22 NVDA buy entry — I backfilled it from Alpaca's records so the audit trail is clean.)

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
