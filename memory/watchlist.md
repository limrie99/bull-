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

_(Last scored: 2026-06-18 06:00 CT pre-market. Conviction = 0.30·Fund + 0.30·Thesis + 0.20·Sent + 0.12·Risk + 0.08·Tech, each dimension 0–100. Buy needs 2+ signals AND Conviction ≥70. **NOTHING clears the gate today.** The post-FOMC deploy decision resolves to NO buy: PANW slipped to 66 (<70) on fresh insider SELLING + no new upgrade (catalyst decaying), JPM 65 has no fresh <2wk catalyst. Hold the 5th slot into a jumpy triple-witching, pre-Juneteenth tape.)_

| Rank | Ticker | Company | Conviction | Fund/100 | Thesis/100 | Sent/100 | Risk/100 | Tech/100 | Signals | Alert | One-line thesis |
|------|--------|---------|-----------|---------|-----------|---------|---------|--------|---------|-------|-----------------|
| 1 | PANW | Palo Alto Networks | **66** | 78 | 72 | 50 | 55 | 65 | #1 (beat-and-raise 6/2, VERIFIED), #3 (cybersecurity secular), #6 (uptrend) | THESIS-RISK | Cybersecurity leader; VERIFIED beat-and-raise 6/2 (EPS $0.85 vs $0.79, rev $3.0B vs $2.94B, raised guide). **Slipped below 70 on sentiment:** fresh insider SELLING (director Goetz ~20k 6/16, CTO Klarich ~62.9k 5/22) + no new analyst upgrade in 2wk → catalyst decaying (~16d stale). Held a base Wed (+0.80% on a −1.3% tape, tight $276–284). Lead, but no buy at 66 — needs a fresh upgrade or clean dip-and-hold to re-clear 70. |
| 2 | JPM | JPMorgan Chase | **65** | 82 | 70 | 50 | 60 | 70 | #3 (financials rotation), #6 (uptrend, near 52-wk high ~$331–335) | NEAR-TRIGGER | Best-in-class bank, fills the missing financials sleeve; clean uptrend. **No fresh <2wk catalyst** (Q1 Apr 14 beat, NII guide cut). Higher-for-longer rates can help bank NIM. Backup if it gets a pre-earnings analyst catalyst. Earnings ~July 14. |
| 3 | AVGO | Broadcom | **58** | 80 | 72 | 55 | 35 | 45 | #1 (Q2 beat), #3 (AI-infra secular), #4 (analyst) | THESIS-RISK | Premier AI custom-silicon; Q2 beat (rev +48%) but guidance "so-so," fell ~12–13% on 6/4 and still below highs. High-beta semis (exited NVDA twice), overlaps ETN. |
| 4 | PWR | Quanta Services | **52** | 60 | 70 | 45 | 55 | 50 | #3 (AI-power/onshoring secular) | (watch) | AI-power/grid-buildout & onshoring secular fit, but only 1 signal — no dated catalyst or fresh upgrade in 2wk. Fails the gate. |
| 5 | ORCL | Oracle | **48** | 70 | 50 | 40 | 50 | 30 | none re-verified this cycle | THESIS-RISK (knife) | Post-June-print stabilization could NOT be re-verified; market rejected the print, fails #6. Don't catch the knife. |

_Bench (unscored, no verified fresh signal): MSFT, CRM, ADBE — quality/diversifier fits to re-screen when Perplexity/Alpaca surfaces a dated catalyst._

## Log (newest on top)

- **2026-06-18 pre-market** — **The post-FOMC deploy decision resolves to NO buy — nothing clears 2 signals + Conviction ≥70.** **PANW dropped from 70 → 66** and below the gate: still 3 signals (verified 6/2 beat-and-raise, cybersecurity secular, uptrend) and it actually *held a base* Wed (+0.80% on a −1.3% hawkish-Fed tape), but the only fresh insider activity is **SELLING** (director Goetz ~20k 6/16, CTO Klarich ~62.9k 5/22) and there's been **no new analyst upgrade in 2 weeks**, so sentiment fell to 50 and the catalyst is decaying without reinforcement (now ~16d stale). It stays the lead but needs a fresh upgrade or a clean dip-and-hold to re-clear 70. **JPM held ~65** — best-in-class bank, clean uptrend near 52-wk highs, but only 2 borderline signals and no fresh <2wk catalyst (rate backdrop turned higher-for-longer, mildly NIM-supportive); backup if it gets a pre-earnings catalyst. **AVGO 58** (so-so guide, fell ~12% on 6/4, semis overlap with ETN). **PWR eased to 52** (still 1 signal, no dated catalyst). **ORCL 48** (knife — post-print stabilization unverified). No NEW large-cap beat-and-raise verified in the last ~7 days. Cash-drag now entering a 4th week but defensible into a jumpy triple-witching, pre-Juneteenth tape with nothing qualifying. Market-open should only act if the open hands a genuine ≥70 setup.
- **2026-06-17 pre-market** — **PANW (Palo Alto Networks) jumps to #1 at Conviction 70** — the opportunity scout surfaced a VERIFIED beat-and-raise from June 2 (EPS $0.85 vs $0.79, rev $3.0B vs $2.94B, raised Q4+FY guide) plus the cybersecurity secular tailwind and an uptrend = 3 signals, lands exactly on the 70 gate. **Not bought today** though: market closed, it would be buying into the 2 PM FOMC, and a +60% YTD run is a chase, not a confirmed base (per the entry-discipline learning). Carry as lead post-FOMC watch with JPM. **JPM eased to 64** (catalyst staleness — no fresh <2wk beat/upgrade; Q1 NII guide was cut), still the financials-sleeve reserve, rate-deferred to Thu 6/18. **AVGO cut to 58** (stale Mar-4 beat, semis overlap). **PWR (Quanta) added at 55** as a new AI-power/onshoring bench name to re-screen for a dated catalyst. **ORCL held ~50** — couldn't re-verify the June print this cycle. Nothing bought today; all decisions deferred to post-FOMC Thursday.
- **2026-06-16 pre-market** — Seeded from the opportunity-scout screens. **JPM (65, NEAR-TRIGGER)** stays the lead reserve-buy: uptrend hard-verified via Alpaca bars (296→320 over 3 wks, golden cross intact), but only the soft 2-signal pair (#5+#6), no fresh catalyst, and rate-sensitive into Wed's FOMC → deploy decision deferred to Thu 6/18 post-Fed. **AVGO (65)** strong secular story but catalyst stale (Mar 4) + high-beta semis overlap. **ORCL (52)** beat-and-raise on 6/10 but stock fell ~9% the next session — market rejected the print, so it's a knife (fails #6), watchlist-only. Nothing clears 2 signals + Conviction ≥70 today.
