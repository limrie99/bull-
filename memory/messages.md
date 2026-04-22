# Messages from Bull

Append-only conversation log. **Most recent at the top.** Each entry is what Bull wants the user to see from a routine run.

Format:

```
## YYYY-MM-DD HH:MM CT · {routine name}

**Headline one-liner**

Body — short paragraph or bullets. What happened, what Bull decided, anything the user should know or decide on.
```

---

## 2026-04-22 10:10 CT · pre-market (ran late — cash market already open)

**APIs are back. Tape is mildly risk-on; NVDA is the only clean buy today — research-only run, no trades placed.**

- Secrets restored; Alpaca + Perplexity both 200. Account verified: **$100,000 cash / 0 positions** (unchanged). Routine fired ~3.5 hr late — market was already open, but per routine spec I do NOT trade on the pre-market scan.
- **Macro:** ES ~+0.69% premarket, mild risk-on. **WTI $113.70, Brent $110.25** — crude bid on IRGC attack in Strait of Hormuz; Trump extended US–Iran ceasefire. 10Y / DXY / Asia / Europe came back `n/a` this pull — gap to close next routine.
- **Earnings:** **no large-cap BMO or AMC prints today.** TSLA 4/22 AMC = confirmed NO (yesterday's source was wrong). **MSFT / META / GOOGL confirmed 2026-04-29 AMC** — they're in the 3-trading-day earnings blackout for the rest of this week.
- **Top pick for next market-open: NVDA ~$201, 10% starter ($10K, ~49 shares), next earnings 5/20.** Watchlist backups: AVGO (~$413, 6/3 earnings), PLTR (~$151, 5/4 — tight). GOOGL/MSFT/META/NOW/LLY/AMD all skipped (blackout or unverified earnings date).
- **Next routine** (market-open 4/23 or a midday today) should: verify NVDA 50-DMA, get 10Y + DXY levels, and execute the NVDA starter with a bracket -7% hard stop (~$187.28) if macro stays constructive.

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
