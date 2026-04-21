# Alpaca API Cheat Sheet

## Environment variables

- `ALPACA_API_KEY`
- `ALPACA_SECRET_KEY`
- `ALPACA_BASE_URL`
  - Paper: `https://paper-api.alpaca.markets`
  - Live:  `https://api.alpaca.markets`

## Headers (every request)

```
APCA-API-KEY-ID: $ALPACA_API_KEY
APCA-API-SECRET-KEY: $ALPACA_SECRET_KEY
Content-Type: application/json
```

## Account

```bash
curl -s "$ALPACA_BASE_URL/v2/account" \
  -H "APCA-API-KEY-ID: $ALPACA_API_KEY" \
  -H "APCA-API-SECRET-KEY: $ALPACA_SECRET_KEY"
```

Returns: `equity`, `cash`, `buying_power`, `portfolio_value`, `last_equity`, `daytrade_count`.

## Positions

```bash
# All positions
curl -s "$ALPACA_BASE_URL/v2/positions" \
  -H "APCA-API-KEY-ID: $ALPACA_API_KEY" \
  -H "APCA-API-SECRET-KEY: $ALPACA_SECRET_KEY"

# Single position
curl -s "$ALPACA_BASE_URL/v2/positions/AAPL" -H ...
```

Each position has: `symbol`, `qty`, `avg_entry_price`, `current_price`, `unrealized_pl`, `unrealized_plpc`, `market_value`.

## Latest quote / trade (market data — uses data.alpaca.markets)

```bash
curl -s "https://data.alpaca.markets/v2/stocks/AAPL/trades/latest" \
  -H "APCA-API-KEY-ID: $ALPACA_API_KEY" \
  -H "APCA-API-SECRET-KEY: $ALPACA_SECRET_KEY"
```

For a day's bars:

```bash
curl -s "https://data.alpaca.markets/v2/stocks/SPY/bars?timeframe=1Day&start=2026-04-20&end=2026-04-21" \
  -H "APCA-API-KEY-ID: $ALPACA_API_KEY" \
  -H "APCA-API-SECRET-KEY: $ALPACA_SECRET_KEY"
```

## Place a bracket order (buy with stop-loss and take-profit)

```bash
curl -s -X POST "$ALPACA_BASE_URL/v2/orders" \
  -H "APCA-API-KEY-ID: $ALPACA_API_KEY" \
  -H "APCA-API-SECRET-KEY: $ALPACA_SECRET_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "symbol": "AAPL",
    "qty": 10,
    "side": "buy",
    "type": "market",
    "time_in_force": "day",
    "order_class": "bracket",
    "stop_loss":   {"stop_price": 172.00},
    "take_profit": {"limit_price": 235.00}
  }'
```

For Bull: **stop_price = entry × 0.93 (-7%)**, **no take_profit** — the trailing stop handles the upside. Actual entry comes from the fill.

## Convert to trailing stop once winning (+5% or more)

Cancel the old stop first:

```bash
# List open orders for the symbol
curl -s "$ALPACA_BASE_URL/v2/orders?status=open&symbols=AAPL" -H ...

# Cancel by order id
curl -s -X DELETE "$ALPACA_BASE_URL/v2/orders/{order_id}" -H ...
```

Then place the trailing stop:

```bash
curl -s -X POST "$ALPACA_BASE_URL/v2/orders" \
  -H ... \
  -d '{
    "symbol": "AAPL",
    "qty": 10,
    "side": "sell",
    "type": "trailing_stop",
    "trail_percent": 10,
    "time_in_force": "gtc"
  }'
```

## Sell / close a position

```bash
# Market sell all shares of a symbol
curl -s -X DELETE "$ALPACA_BASE_URL/v2/positions/AAPL" -H ...

# Or place a regular sell order for partial
curl -s -X POST "$ALPACA_BASE_URL/v2/orders" \
  -H ... \
  -d '{"symbol":"AAPL","qty":5,"side":"sell","type":"market","time_in_force":"day"}'
```

## Check an order filled

```bash
curl -s "$ALPACA_BASE_URL/v2/orders/{order_id}" -H ...
```

`status` should be `filled`. Use `filled_avg_price` as the actual entry.

## Clock (is the market open?)

```bash
curl -s "$ALPACA_BASE_URL/v2/clock" -H ...
```

Returns `is_open`, `next_open`, `next_close`. Use this defensively — if `is_open=false` during the market-open routine, pause and notify.
