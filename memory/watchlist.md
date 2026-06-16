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

_(Last scored: 2026-06-16 06:00 CT pre-market. Conviction = 0.30·Fund + 0.30·Thesis + 0.20·Sent + 0.12·Risk + 0.08·Tech, each dimension 0–100. Buy needs 2+ signals AND Conviction ≥70 — none clears today.)_

| Rank | Ticker | Company | Conviction | Fund/100 | Thesis/100 | Sent/100 | Risk/100 | Tech/100 | Signals | Alert | One-line thesis |
|------|--------|---------|-----------|---------|-----------|---------|---------|--------|---------|-------|-----------------|
| 1 | JPM | JPMorgan Chase | **65** | 75 | 55 | 60 | 60 | 80 | #6 (uptrend, HARD-verified via bars), #5 (financials rotation, thematic) | NEAR-TRIGGER | Best-in-class bank, fills the missing financials sleeve; clean uptrend + golden cross. Rate-driven thesis → deploy decision deferred to post-FOMC (Thu 6/18). Earnings ~July 14. |
| 2 | AVGO | Broadcom | **65** | 80 | 55 | 65 | 50 | 65 | #3 (AI-infra secular, verified) | THESIS-RISK (stale catalyst) | Premier AI custom-silicon, but the beat-and-raise is 3 months stale (Mar 4), high-beta semis (just exited NVDA), overlaps ETN. No fresh dated catalyst. |
| 3 | ORCL | Oracle | **52** | 70 | 50 | 40 | 50 | 30 | #1 (Q4 beat-and-raise 6/10, VERIFIED) | THESIS-RISK (knife) | Beat-and-raise but the market REJECTED it — fell ~9% post-print (248→184), only now bouncing to ~192. Fails #6 (not in uptrend, near recent lows). Don't catch the knife. |

_Bench (unscored, no verified fresh signal): MSFT, CRM, ADBE — quality/diversifier fits to re-screen when Perplexity/Alpaca surfaces a dated catalyst._

## Log (newest on top)

- **2026-06-16 pre-market** — Seeded from the opportunity-scout screens. **JPM (65, NEAR-TRIGGER)** stays the lead reserve-buy: uptrend hard-verified via Alpaca bars (296→320 over 3 wks, golden cross intact), but only the soft 2-signal pair (#5+#6), no fresh catalyst, and rate-sensitive into Wed's FOMC → deploy decision deferred to Thu 6/18 post-Fed. **AVGO (65)** strong secular story but catalyst stale (Mar 4) + high-beta semis overlap. **ORCL (52)** beat-and-raise on 6/10 but stock fell ~9% the next session — market rejected the print, so it's a knife (fails #6), watchlist-only. Nothing clears 2 signals + Conviction ≥70 today.
