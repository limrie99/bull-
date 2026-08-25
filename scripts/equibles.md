# Equibles API Cheat Sheet (filing-grade research data)

Equibles serves data straight from primary filings (SEC Forms 4/5, 13F, FINRA short
interest, XBRL financials, congressional disclosures). Use it to replace web-search
guesses with filing-cited numbers for the **Fundamental** and **Sentiment** conviction
dimensions and for **buy signal #7 (smart-money accumulation)** in memory/strategy.md.

## Environment variable

- `EQUIBLES_API_KEY` — **optional**. If empty, skip this sheet entirely (Perplexity +
  the free SEC EDGAR fallback below still work). Never halt on a missing Equibles key.

## Auth + base URL

```
Base: https://api.equibles.com/v1
Header: Authorization: Bearer $EQUIBLES_API_KEY
```

All list endpoints page with `limit`/`offset` and return a `hasMore` flag.

## Insider activity (signal #7 input, Sentiment dimension)

```bash
# Recent Form 4/5 transactions for a ticker (who bought/sold, role, price, value)
curl -s "https://api.equibles.com/v1/stocks/AAPL/insider-transactions?limit=25" \
  -H "Authorization: Bearer $EQUIBLES_API_KEY" | jq .

# Composite insider-sentiment score 0-100 for one ticker
# (blends net distinct buyers, net shares bought % of outstanding, net buy value;
#  isClusterBuy=true means multiple distinct insiders bought — the strong form)
curl -s "https://api.equibles.com/v1/insider-sentiment-scores?ticker=AAPL" \
  -H "Authorization: Bearer $EQUIBLES_API_KEY" | jq .
```

Key fields: `transactionDate`, `insiderName`, `role`, `transactionType`,
`isOpenMarketTrade`, `shares`, `pricePerShare`, `value`, `sharesOwnedAfter`;
scores: `score`, `distinctBuyers`, `netSharesBoughtPercentOfShares`, `isClusterBuy`.
Only open-market buys count as a bullish read — option exercises and 10b5-1 sales are noise.

## Institutional holdings / 13F (signal #7 input, Sentiment dimension)

```bash
# Aggregate institutional ownership by quarter (institution count, total shares, QoQ change)
curl -s "https://api.equibles.com/v1/stocks/AAPL/institutional-ownership?periods=4" \
  -H "Authorization: Bearer $EQUIBLES_API_KEY" | jq .

# Biggest institutional buyers and sellers vs the prior quarter
curl -s "https://api.equibles.com/v1/stocks/AAPL/institutional-activity?limit=10" \
  -H "Authorization: Bearer $EQUIBLES_API_KEY" | jq .

# Largest current 13F holders
curl -s "https://api.equibles.com/v1/stocks/AAPL/institutional-holders?limit=10" \
  -H "Authorization: Bearer $EQUIBLES_API_KEY" | jq .
```

Remember: 13F data is quarterly and lags up to 45 days — treat it as confirmation of
accumulation, never as a timing signal.

## Short data (signal #7 input, Risk dimension)

```bash
# Bi-monthly FINRA short interest: position, change vs prior settlement, days to cover
curl -s "https://api.equibles.com/v1/stocks/AAPL/short-interest?limit=6" \
  -H "Authorization: Bearer $EQUIBLES_API_KEY" | jq .

# Daily FINRA short-volume percentage (finer-grained trend between settlements)
curl -s "https://api.equibles.com/v1/stocks/AAPL/short-volume?limit=10" \
  -H "Authorization: Bearer $EQUIBLES_API_KEY" | jq .
```

For signal #7 we want short interest **flat or falling** while insiders/institutions
accumulate. Rising days-to-cover on a candidate is a risk-dimension flag, not a buy reason
— we are not a squeeze strategy.

## Fundamentals (Fundamental dimension — real numbers, not estimates)

```bash
# TTM P/E, EV/Revenue, EV/EBIT with peer-cohort median/quartiles (valuation vs sector)
curl -s "https://api.equibles.com/v1/stocks/AAPL/valuation-multiples" \
  -H "Authorization: Bearer $EQUIBLES_API_KEY" | jq .

# Management guidance ranges extracted from 8-Ks and earnings calls (raised guidance = signal #1 evidence)
curl -s "https://api.equibles.com/v1/stocks/AAPL/guidance" \
  -H "Authorization: Bearer $EQUIBLES_API_KEY" | jq .

# Company KPIs (ARR, backlog, units, FCF) mined from earnings releases and MD&A
curl -s "https://api.equibles.com/v1/stocks/AAPL/kpis" \
  -H "Authorization: Bearer $EQUIBLES_API_KEY" | jq .
```

## Congressional trades (color only — never a signal by itself)

```bash
curl -s "https://api.equibles.com/v1/congress/trades?ticker=AAPL&limit=10" \
  -H "Authorization: Bearer $EQUIBLES_API_KEY" | jq .
```

Disclosure ranges are wide (`amountFrom`/`amountTo`) and filings lag up to 45 days.

## Market-wide smart-money screens (opportunity scout)

```bash
# Universe ranked by insider-sentiment score, cluster buys only, large caps
curl -s "https://api.equibles.com/v1/insider-sentiment-scores?clusterBuysOnly=true&minMarketCap=10000000000&limit=15" \
  -H "Authorization: Bearer $EQUIBLES_API_KEY" | jq .

# Market-wide 13F leaderboard: what institutions bought most last quarter
curl -s "https://api.equibles.com/v1/13f/market-activity?bucket=top-buys&limit=15" \
  -H "Authorization: Bearer $EQUIBLES_API_KEY" | jq .
```

Screen output still has to pass the Universe filter and the full Conviction Score —
a hot smart-money name with no catalyst is watchlist-only at best.

## Budget tip (hard limit — plan around it)

The free tier is **100 requests per DAY, shared across all 5 routines** (and the MCP
server, if ever used). Same discipline as the Perplexity budget: batch, don't browse.
- Pre-market owns most of the budget: ~3-4 calls per scout candidate + held name
  (insider-transactions, institutional-ownership, short-interest, valuation-multiples).
  5 candidates + 4 holdings ≈ 35 calls. Fine.
- Market-open / midday / close: only re-check a name if a decision hinges on it.
- A `429` or quota error is NOT a halt: log it, fall back to EDGAR (below) or
  Perplexity, keep the routine moving.

## Free fallback: SEC EDGAR (keyless, unlimited daily budget)

When the Equibles budget is spent or the key is unset, raw filings are free. EDGAR
requires a descriptive `User-Agent` and allows ~10 req/s:

```bash
UA="Bull-research-agent (github.com/limrie99/bull-)"

# 1) Ticker -> 10-digit CIK (zero-padded)
curl -s -H "User-Agent: $UA" "https://www.sec.gov/files/company_tickers.json" \
  | jq -r 'to_entries[] | select(.value.ticker=="AAPL") | .value.cik_str' \
  | xargs printf "%010d\n"

# 2) All recent filings for the company (Form 4 = insider buys/sells, 8-K, 10-Q...)
curl -s -H "User-Agent: $UA" "https://data.sec.gov/submissions/CIK0000320193.json" \
  | jq '.filings.recent | {form: .form[:15], filingDate: .filingDate[:15]}'

# 3) XBRL company facts (revenue, EPS, margins, debt — every reported number)
curl -s -H "User-Agent: $UA" "https://data.sec.gov/api/xbrl/companyfacts/CIK0000320193.json" \
  | jq '.facts."us-gaap".Revenues.units.USD[-4:]'
```

EDGAR costs zero dollars but more of your context — prefer Equibles when budget allows,
EDGAR when it doesn't.
