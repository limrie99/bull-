# Astra — independent challenger ✨

Astra is strategy #3 in Lauren's paper-trading league. It uses the OpenAI Responses API with `gpt-6-astra`, Alpaca paper trading, built-in web search, persistent JSON/JSONL memory, and a deterministic risk engine.

## Experimental design

- Separate Alpaca paper account and $100,000 starting baseline.
- Astra may read its own portfolio, decisions, and trade history plus public market information.
- Astra must not read Bull's or Maverick's current-day decisions until its own 3:50 PM ET journal is written.
- All three are scored against SPY. Cross-agent agreement analysis happens after decisions, never before.
- Paper only. The runner rejects any Alpaca base URL except `https://paper-api.alpaca.markets`.

## Guardrails enforced in code

- Long-only stocks/ETFs; no options, shorting, leverage, crypto, or symbols below $5.
- Maximum 6 open positions and 7% of equity per position.
- Maximum 0.5% of equity at risk on a new trade.
- Maximum 3 buys per rolling Monday–Friday week.
- No new buys after a 2% account decline versus prior close.
- Minimum model confidence of 75 for a buy.
- Every buy is submitted as an OTO market order with a 7% stop-loss.
- Execution is disabled unless `ASTRA_EXECUTION_ENABLED=true`; even then, the paper URL check remains mandatory.

## Required GitHub Actions secrets

Use a third Alpaca paper account; do not reuse Bull's or Maverick's keys.

```text
OPENAI_API_KEY
ASTRA_ALPACA_API_KEY
ASTRA_ALPACA_SECRET_KEY
ASTRA_EXECUTION_ENABLED=true
```

The workflow supplies `ASTRA_ALPACA_BASE_URL=https://paper-api.alpaca.markets` and `ASTRA_MODEL=gpt-6-astra`. Until the secrets are present, scheduled runs fail closed and do not trade.

## Schedule

Weekdays in America/New_York:

1. 8:00 — premarket research
2. 9:25 — opening plan
3. 10:15 — entry check
4. 12:30 — portfolio check
5. 15:00 — closing decision
6. 15:50 — risk shutdown and journal

GitHub cron is UTC-only, so the workflow schedules both daylight- and standard-time candidates. `runner.py --scheduled` checks New York local time and skips the wrong candidate.

Manual dry run:

```bash
python astra/runner.py --fixture astra/tests/fixture.json --routine entry-check
```

Manual live paper-account run:

```bash
python astra/runner.py --routine entry-check
```

The dashboard is `astra/dashboard/index.html`. It reads `astra/dashboard/state.json` and refreshes automatically.
