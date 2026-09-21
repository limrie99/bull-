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

## Role split — Astra proposes, the host executes

Astra is a **strategist**, not a trader. The model returns one JSON decision per run; `runner.py` decides whether that decision is allowed, computes the quantity, and places the order. With `ASTRA_EXECUTION_ENABLED` unset or false, every decision is recorded as `PROPOSED_ONLY` and no order is sent — the strategist keeps working and the log keeps compounding, which is the point.

This mirrors the pattern Nate Herk hit in *"I Turned GPT-6 Astra Into a 24/7 Stock Trader"* (Sep 2026, https://youtu.be/TLQLfa7yH4I): his Astra was blocked from placing trades, so he kept it as the strategist and handed execution to a separate "Trader" bot. Here the split is enforced in code rather than improvised — the deterministic risk engine is the executor.

Two rules that follow from it:

- **The model never sizes or authorizes a trade.** Confidence ≥75 is a *proposal* clearing the quality bar, not an instruction. Position size, the 7% stop, and every cap come from `config.json` and the runner.
- **No cross-strategy handoff.** Astra must stay blind to Bull's and Maverick's current-day decisions (see *Experimental design*), so its proposals are never routed into another strategy's order flow. Bull runs its own internal Research → Risk → Trader split, documented in `memory/strategy.md`; the league comparison only means something if the three books decide independently.

## Continuity — each run reads the last decision and writes the next

Every run is stateless, so the logs are the memory:

- `astra/memory/decision-log.jsonl` — one row per run: timestamp, routine, the decision JSON, and what the risk engine did with it. The next routine is handed the tail of this file (last 30 rows) before it decides anything.
- `astra/memory/trade-log.jsonl` — the append-only ledger of orders actually submitted.
- `astra/dashboard/state.json` — the rendered snapshot, overwritten each run.

Each routine should therefore read the recent decision rows *and* the live account state before acting: the log says what Astra planned, Alpaca says what is true, and truth wins. The 15:50 `risk-shutdown` journal is the day's handoff into tomorrow's `premarket-research`.

## Required GitHub Actions secrets

Keys live **only** in GitHub Actions secrets (or a local gitignored `.env` for manual runs) — never in a prompt, a chat message, a log line, or a commit. Astra's logs record decisions and fills, never credentials. Use a third Alpaca paper account; do not reuse Bull's or Maverick's keys.

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

Six wakeups a day is a *monitoring* cadence, not a day-trading one. `risk-shutdown` means **no new buys plus a journal** — it does not flatten the book, and Astra is expected to hold positions overnight with its 7% stop doing the work. (Bull makes the same choice explicitly in `memory/strategy.md` under *Schedule mapping*.)

Manual dry run:

```bash
python astra/runner.py --fixture astra/tests/fixture.json --routine entry-check
```

Manual live paper-account run:

```bash
python astra/runner.py --routine entry-check
```

The dashboard is `astra/dashboard/index.html`. It reads `astra/dashboard/state.json` and refreshes automatically.
