# Watchlist

Persistent, scored bench of candidates Bull is tracking but hasn't bought (or has sold and is re-watching). Pre-market re-scores this; market-open buys from the top of it when a name clears the gate. This is how good ideas survive between runs instead of being re-discovered from scratch every morning.

**Scoring = the Conviction Score (0–100) defined in `strategy.md`.** Same number that gates a buy, so the watchlist is literally a ranked queue of "how close is this to a buy."

**Buy trigger reminder:** a name only leaves this list for the portfolio when it has **2+ buy signals AND Conviction ≥ 70** — and only at market-open/midday with caps respected.

## How to maintain it (every pre-market, and after any sell)

1. Re-score every name with fresh Perplexity research (stale = score older than ~3 trading days).
2. Re-sort by Conviction Score, highest first.
3. Set/refresh each row's **Alert** flag:
   - `EARNINGS` — reports within ~14 days (open a position only if the thesis depends on the print; see strategy earnings rule)
   - `NEAR-TRIGGER` — score 65–69, one good catalyst away from clearing the gate
   - `THESIS-RISK` — fundamentals or catalyst deteriorating; consider removing
   - `CATALYST-SOON` — known event (launch, FDA, contract decision) within ~7 days
4. Drop anything that scores < 40 twice in a row, with a one-line reason in the log below.
5. Keep the active table to ~8 names — this is a focused bench, not a screener dump.

## Rankings

_(Last scored: 2026-06-17 06:00 CT pre-market. Conviction = 0.30·Fund + 0.30·Thesis + 0.20·Sent + 0.12·Risk + 0.08·Tech, each dimension 0–100. Buy needs 2+ signals AND Conviction ≥70. PANW clears the gate numerically (70) but is NOT bought today: market closed + buying into the 2 PM FOMC + chasing a +60% YTD run = against discipline. All buys deferred to post-FOMC Thu 6/18.)_

| Rank | Ticker | Company | Conviction | Fund/100 | Thesis/100 | Sent/100 | Risk/100 | Tech/100 | Signals | Alert | One-line thesis |
|------|--------|---------|-----------|---------|-----------|---------|---------|--------|---------|-------|-----------------|
| 1 | PANW | Palo Alto Networks | **70** | 78 | 75 | 65 | 55 | 70 | #1 (beat-and-raise 6/2, VERIFIED), #3 (cybersecurity secular), #6 (uptrend) | NEAR-TRIGGER | Cybersecurity leader; VERIFIED beat-and-raise 6/2 (EPS $0.85 vs $0.79, rev $3.0B vs $2.94B, raised guide). Clears gate numerically but +60% YTD = chase risk + catalyst ~15d old. Post-FOMC watch — buy only if Thu entry looks like a base, not a spike. |
| 2 | JPM | JPMorgan Chase | **64** | 75 | 55 | 60 | 60 | 80 | #6 (uptrend, HARD-verified via bars), #5 (financials rotation, thematic) | NEAR-TRIGGER | Best-in-class bank, fills the missing financials sleeve; clean uptrend + golden cross. No fresh <2wk catalyst (Q1 Apr 14 beat but NII guide cut). Rate-driven → deferred to post-FOMC (Thu 6/18). Earnings ~July 14. |
| 3 | AVGO | Broadcom | **58** | 80 | 55 | 65 | 50 | 65 | #3 (AI-infra secular, verified) | THESIS-RISK (stale catalyst) | Premier AI custom-silicon, but beat-and-raise 3 months stale (Mar 4), high-beta semis (just exited NVDA twice), overlaps ETN. No fresh dated catalyst. |
| 4 | PWR | Quanta Services | **55** | 65 | 60 | 50 | 50 | 55 | #3 (AI-power/onshoring secular) | (watch) | New bench name: AI-power/grid-buildout & onshoring secular fit, but all else UNVERIFIED this cycle. Re-screen for a dated catalyst before scoring higher. |
| 5 | ORCL | Oracle | **50** | 70 | 50 | 40 | 50 | 30 | none re-verified this cycle | THESIS-RISK (knife) | Beat-and-raise (~6/10) and ~9% post-print drop could NOT be re-verified this cycle; market rejected the print, fails #6. Don't catch the knife. |

_Bench (unscored, no verified fresh signal): MSFT, CRM, ADBE — quality/diversifier fits to re-screen when Perplexity/Alpaca surfaces a dated catalyst._

## Log (newest on top)

- **2026-06-17 pre-market** — **PANW (Palo Alto Networks) jumps to #1 at Conviction 70** — the opportunity scout surfaced a VERIFIED beat-and-raise from June 2 (EPS $0.85 vs $0.79, rev $3.0B vs $2.94B, raised Q4+FY guide) plus the cybersecurity secular tailwind and an uptrend = 3 signals, lands exactly on the 70 gate. **Not bought today** though: market closed, it would be buying into the 2 PM FOMC, and a +60% YTD run is a chase, not a confirmed base (per the entry-discipline learning). Carry as lead post-FOMC watch with JPM. **JPM eased to 64** (catalyst staleness — no fresh <2wk beat/upgrade; Q1 NII guide was cut), still the financials-sleeve reserve, rate-deferred to Thu 6/18. **AVGO cut to 58** (stale Mar-4 beat, semis overlap). **PWR (Quanta) added at 55** as a new AI-power/onshoring bench name to re-screen for a dated catalyst. **ORCL held ~50** — couldn't re-verify the June print this cycle. Nothing bought today; all decisions deferred to post-FOMC Thursday.
- **2026-06-16 pre-market** — Seeded from the opportunity-scout screens. **JPM (65, NEAR-TRIGGER)** stays the lead reserve-buy: uptrend hard-verified via Alpaca bars (296→320 over 3 wks, golden cross intact), but only the soft 2-signal pair (#5+#6), no fresh catalyst, and rate-sensitive into Wed's FOMC → deploy decision deferred to Thu 6/18 post-Fed. **AVGO (65)** strong secular story but catalyst stale (Mar 4) + high-beta semis overlap. **ORCL (52)** beat-and-raise on 6/10 but stock fell ~9% the next session — market rejected the print, so it's a knife (fails #6), watchlist-only. Nothing clears 2 signals + Conviction ≥70 today.
