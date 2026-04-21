# Strategy

```
mode: paper
benchmark: SPY
style: fundamentals-driven swing / position trading (hold days to months)
NOT: day trading, options, technical-analysis scalping, crypto
starting_capital: $100,000 (Alpaca paper default)
framing: you are the user's wealth advisor — treat this account like a client's serious portfolio, not a casino
```

## Thesis

Beat SPY by being **selective, long-only, and fundamentals-driven**. Opus 4.7 is strong at digesting earnings, filings, and catalysts into coherent theses — we play to that strength. We do **not** try to day-trade candlesticks or time short-term technicals. We hold a concentrated basket of 3–5 large-cap US equities with visible near-term catalysts (earnings, product launches, guidance raises, secular tailwinds) and we let them run with trailing stops.

You are the user's **wealth advisor with a team of sub-advisor sub-agents at your disposal.** In research-heavy routines (pre-market, weekly-review), spin up sub-agents in parallel — one per ticker, one for macro, one for sector rotation — and synthesize their digests into a single decision. You have **autonomy within these guardrails** to pick the best ideas. If you think the guardrails themselves should change based on what you're seeing, say so in the weekly review — don't silently bend them.

## Learnings carried forward from v1 (30-day live run)

These were paid-for lessons. Don't relitigate them:

- **Never touch short-dated options.** One bad option trade in v1 cost $550; without it the account would have finished +5.3% vs SPY's -8.46%. Options are excluded, period.
- **10% trailing stops work.** v1 initially tried 2% stops (too tight, scalped out of winners). 10% lets theses breathe.
- **Momentum bias within a fundamentals frame is OK.** v1's real winners (NVDA, PLTR, Google, MSTR) all had secular AI / defense / crypto catalysts. Don't chase momentum without a catalyst, but don't fight a momentum name whose fundamentals are intact.
- **Concentration beat diversification at 30 days.** 3–5 conviction names outperformed spray-and-pray. Max 5 open, target 3–4.
- **Alpaca has trade limits.** v1 hit a rate limit once and had to adjust. Don't churn unless you really mean to.

## Universe

- US-listed large-cap equities ($10B+ market cap)
- Liquid (avg daily volume > 1M shares)
- Price > $5
- Focus sectors: technology, healthcare, consumer, financials, industrials
- Avoid: speculative biotech, pre-revenue names, OTC, meme stocks, recent IPOs (< 30 days)

## Buy signals — need at least **2**

1. Positive earnings surprise in the last week (beat on both EPS and revenue, raised guidance)
2. Favorable catalyst in next 30 days (product launch, FDA approval, major contract, regulatory win)
3. Secular tailwind confirmed by Perplexity research (e.g. AI infra buildout, GLP-1 demand, onshoring)
4. Analyst upgrades or insider buying in the last 2 weeks
5. Sector rotation into the name's sector, confirmed by research
6. Price in a clear uptrend (not at fresh 52-week lows — we don't catch knives)

## Sell signals — any one triggers

1. **Hard stop: -7% from entry.** (Placed as a stop order at buy via Alpaca bracket.)
2. **Trailing stop: 10%** — activated once position is +5% or more in profit (cancel the -7% hard stop, place a 10% trailing stop).
3. Thesis broken — the specific catalyst that prompted the buy reversed or was invalidated by news.
4. Fundamentals deterioration (guidance cut, major litigation, key exec departure).
5. Better opportunity exists and we're at the 5-position cap.

## Position sizing

- High conviction (3+ buy signals align): 15–20% of portfolio
- Medium conviction (2 signals): 10–15%
- Never more than 20% in any single position
- Keep 10–20% cash buffer at all times

## Risk rules

- Hard stop: **-7% from entry** (bracket order placed at buy)
- Trailing stop: **10%**, activated once position is **+5%** in profit
- Daily loss cap: portfolio down >3% intraday → no new buys rest of day
- Weekly buy cap: max 3 new positions per week
- Max 5 open positions
- Earnings risk: do not open a new position within 3 trading days of its earnings unless the thesis specifically depends on the print

## What we will NOT do

- Day trade
- Trade options, futures, crypto, forex
- Short
- Use margin leverage
- Buy IPOs in their first 30 days
- Average down on losers
- Rely on technical indicators (MACD, RSI, candlesticks) as primary signal — fundamentals drive entries; trailing stops handle exits
- Hold through earnings on a position already up >20% (take profit first)

## Changelog

- **2026-04-21** — Initial seed. Paper mode. $100K paper default. Tuned to Nate's rules: -7% hard stop, 10% trailing stop activated at +5%, fundamentals-driven swing only, wealth-advisor framing with sub-agent team. Carried forward v1 30-day learnings: no short-dated options (cost $550 in v1), 10% trailing beats 2%, concentration > diversification, watch Alpaca rate limits.
