# Messages from Bull

Append-only conversation log. **Most recent at the top.** Each entry is what Bull wants the user to see from a routine run.

Format:

```
## YYYY-MM-DD HH:MM CT · {routine name}

**Headline one-liner**

Body — short paragraph or bullets. What happened, what Bull decided, anything the user should know or decide on.
```

---

## 2026-05-11 06:00 CT · pre-market

**Good morning, Lauren — we're back online and I've done a fresh pre-market scan. Plan for today: one careful starter buy, not a shopping spree.**

**What I did**
Pulled overnight futures, this week's earnings calendar, and ran the candidate scout with a four-name shortlist. Then I checked our account at our broker (Alpaca) — we're sitting at **$99,841 cash, no positions** after a long pause where I was offline. I'm not placing any trades right now (market doesn't open until 8:30 AM CT) — this is the research/plan step.

**Why**
After three weeks dark, I'd rather ease back in with one clean, well-supported buy than spray cash across four ideas. The macro backdrop today is OK — not euphoric, not hostile. Oil has cooled off, trade tone is improving, and chips made new record highs Friday. **No mega-cap earnings (when companies report their quarterly numbers) report today**, so the market will trade on mood and positioning more than on any single name.

**The plan for the market-open routine (~8:30 AM CT)**
- **Top pick: Broadcom (AVGO) ~$10K starter** (about 10% of the account). Reason: it's a key beneficiary of the AI buildout (custom chips + networking for the giant cloud companies), in a clear uptrend, and its next earnings aren't until June 3 — well outside our 3-day "don't buy right before earnings" rule.
- **Nvidia (NVDA): deferred.** I love the thesis, but their earnings land May 20 — only 7 trading days away. Buying now means betting on a binary event, which our playbook discourages. I'll revisit on May 21.
- **Quanta Services (PWR): deferred.** Best fundamentals story I saw (huge earnings beat + raised forecast on AI-power demand), but the stock is up 32% in 30 days — chasing a runner is how you get hurt. I want a pullback toward $710 first.
- **Safety valve:** if futures sour by the open or oil spikes on a Middle East headline, I'll pass entirely and re-scan midday.

**Numbers I care about**
- Cash: **$99,841** (essentially the full $100K paper account; ~$159 drift is paper-broker housekeeping)
- Weekly buys used: **0 of 3**
- SPY (the S&P 500 index, our benchmark) closed Friday at **$737.54** — that's the line I need to beat over time

I'll check back at 8:30 AM CT with the actual trade decision. 🐂

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
