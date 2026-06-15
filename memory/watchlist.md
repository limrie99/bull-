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

_(Last scored: — · seed empty; pre-market will populate)_

| Rank | Ticker | Company | Conviction | Fund/30 | Thesis/30 | Sent/20 | Risk/12 | Tech/8 | Signals | Alert | One-line thesis |
|------|--------|---------|-----------|---------|-----------|---------|---------|--------|---------|-------|-----------------|
| — | — | — | — | — | — | — | — | — | — | — | _no candidates yet_ |

## Log (newest on top)

- _empty — first pre-market run after 2026-06-15 will seed this from the opportunity scout's screens._
