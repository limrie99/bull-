# Astra — independent challenger ✨

Astra is strategy #3 in Lauren's paper-trading league. It uses the OpenAI Responses API with ChatGPT Astra (`gpt-6-astra`), Alpaca paper trading, built-in web search, persistent JSON/JSONL memory, a multi-voice investment committee, and a deterministic risk engine.

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
- A buy needs at least one buyer voice to have named that exact ticker, and at least one skeptic voice to have answered.
- A skeptic voice at stance BLOCK with conviction ≥ 85 vetoes the buy, whatever the chair decided.
- Execution is disabled unless `ASTRA_EXECUTION_ENABLED=true`; even then, the paper URL check remains mandatory.

## Committee voices

`astra/voices.json` is the roster. Each voice is one ChatGPT Astra call with its own mandate, its own web search, and a strict JSON answer: stance, conviction, tickers, and a short plain-English argument. Astra chairs them — it reads every voice, then issues the single decision the risk engine sees.

| Bench | Job | Voices |
| --- | --- | --- |
| Researchers | Establish what is verifiably true | Filings Researcher · Catalyst Researcher · Macro and Rotation Researcher |
| Buyers | Judge whether a business is worth owning today | Quality Compounder · Margin of Safety · Trend and Catalyst |
| Skeptics | Argue why this loses money | The Bear Case · Risk and Liquidity · Pre-Mortem |

The three buyer voices are deliberately incompatible: a name that a compounder buyer, a deep-value buyer and a trend buyer all want is rare and worth noticing, and any one of them is enough to clear the support rule.

Researchers answer first; buyers and skeptics then argue over the same evidence, and the chair reads all of it. Each routine only wakes the benches it needs (`routines` per voice), so the buy bench never sits during `risk-shutdown`. Voices run in parallel, and one that errors or times out is recorded as silent rather than cancelling the run — but a silent *skeptic* bench blocks buying, because nobody checked the downside.

Tuning knobs, all in `voices.json`: `enabled`, `max_parallel`, `min_buyer_support`, `skeptic_veto_conviction`, and each voice's `mandate`, `routines`, `reasoning_effort`, `web_search`, `model`, `timeout_seconds`. Set `ASTRA_VOICES_ENABLED=false` to fall back to a single-voice run, or `ASTRA_VOICE_MODEL` to run the benches on a cheaper model than the chair.

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

Manual dry run (no network, fixed committee, fixed decision):

```bash
python astra/runner.py --fixture astra/tests/fixture.json --routine entry-check
```

Manual live paper-account run:

```bash
python astra/runner.py --routine entry-check
```

Unit tests (scheduling, paper guardrails, committee gate):

```bash
python -m unittest discover -s astra/tests -p 'test_*.py'
```

The dashboard is `astra/dashboard/index.html`. It reads `astra/dashboard/state.json` and refreshes automatically, and shows each bench's stance and argument under the decision log.
