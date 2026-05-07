# Messages from Bull

Append-only conversation log. **Most recent at the top.** Each entry is what Bull wants the user to see from a routine run.

Format:

```
## YYYY-MM-DD HH:MM CT · {routine name}

**Headline one-liner**

Body — short paragraph or bullets. What happened, what Bull decided, anything the user should know or decide on.
```

---

## 2026-05-07 12:00 CT · midday

**Midday: steady, no changes — but I owe you a catch-up on what happened the last two weeks.**

**What I did**
Pulled fresh state from Alpaca and reconciled our memory files, which were out of date because the routines were halting on missing API keys for a stretch in late April. While we were "asleep," the paper account quietly worked through a trade I'd already staged: it bought 25 shares of NVIDIA (NVDA) on 4/22 at $201.38, and on 5/04 the trailing stop sold those shares at an average of $195.02. Net result: a small realized loss of **−$159.00** (about −3.2%). I've back-filled the trade log so it's all on the record now.

**Why**
A "trailing stop" is a sell order that automatically follows the price up — once a position is +5% in profit, I cancel the original −7% safety net and replace it with one that trails 10% below the high. NVDA ran up briefly, the trailing stop activated, then it pulled back and we got sold out. That's the system working as designed: small loss, no drama. There's nothing to manage right now (we hold zero positions), no breaking news catalyst that demands a midday entry, and the daily loss cap isn't triggered.

**What happens next**
I'm holding cash (about $99,841) until the next pre-market routine, when I'll do a fresh scout. SPY has drifted up ~3% in the two weeks we sat out, so we're behind the index — the next entry needs to be a real ≥2-signal setup, not a stretch.

**Numbers I care about**
- Equity: **$99,840.95** (down $159 from our $100,000 start, −0.16% since inception)
- Cash: **$99,841 (100% of the account)** — fully dry powder
- SPY since 4/22: **roughly +3%**, so our alpha (return vs. SPY) is **about −3% over those two weeks** — fair to call out, not a panic

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
