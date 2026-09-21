# Astra — research helper for Bull and Maverick ✨

Astra is the team's **research and strategy helper**, not a fourth portfolio. It uses the OpenAI Responses API with `gpt-6-astra`, built-in web search, a read-only view of the Alpaca **paper** account, persistent JSON/JSONL memory, and a deterministic risk engine. Its output is a stream of scored, falsifiable **proposals** that Bull — and the two Maverick agents — can accept, reject, or ignore.

> **Pivot, 2026-09-21 (per Lauren).** Astra was originally built as league strategy #3: a separate book on its own account, deliberately blind to Bull's decisions, scored head-to-head against Bull and Maverick. That framing is retired. Astra now *helps* the other agents instead of racing them. The competitive language throughout this folder has been replaced, and helper mode is enforced in code, not just in docs.

## How Astra fits the team

| Agent | Role | Places orders? |
|-------|------|----------------|
| **Bull** (Claude) | Fundamentals-driven swing trader, the accountable owner of the account | Yes — Bull's Trader voice only |
| **Maverick** / **Maverick-aggressive** (Grok) | Challenger books in their own repos | Yes, in their own accounts |
| **Astra** (GPT-6) | Research/strategist helper: scores ideas, writes proposals, argues the other side | **No** |

Astra's proposals land in `memory/astra-proposals.md` (newest on top) with a machine-readable mirror in `astra/memory/proposals.jsonl`. Bull reads that file at the start of pre-market, market-open, and midday. A proposal is one more research input — it must still clear **Bull's own buy-gate (2+ buy signals AND Conviction ≥ 70)**, Bull's sizing and cash-floor rules, and Bull's hard stop. Nothing Astra writes is self-executing.

## Credentials — Astra shares Bull's paper keys

**Lauren authorized Astra to use Bull's existing Alpaca paper credentials (2026-09-21)**, so there is nothing new to create. The workflow passes every accepted name through and `runner.py` picks the first complete pair:

| Precedence | Secret pair | Result |
|---|---|---|
| 1 | `ASTRA_ALPACA_API_KEY` + `ASTRA_ALPACA_SECRET_KEY` | Dedicated Astra paper account (optional, none exist today) |
| 2 | `ALPACA_API_KEY` + `ALPACA_SECRET_KEY` | **Bull's existing paper keys — the expected path** |
| 3 | `APCA_API_KEY_ID` + `APCA_API_SECRET_KEY` | Same thing under Alpaca's own naming |

`OPENAI_API_KEY` is also required and is already a repository secret. Keys live **only** in GitHub Actions secrets (or a local gitignored `.env`) — never in a prompt, a chat message, a log line, or a commit. Astra's logs record decisions and fills, never credentials.

The workflow hard-codes `ASTRA_ALPACA_BASE_URL=https://paper-api.alpaca.markets` and deliberately does **not** pass Bull's `ALPACA_BASE_URL`, which could point at the live endpoint. Paper only, no exceptions: the runner refuses to start against any other base URL.

**The known risk of sharing, stated plainly:** Astra and Bull are looking at the same paper account. Two agents that can both trade one account can place conflicting or duplicate orders, blow past position caps, and make the trade log impossible to attribute. That is exactly why sharing keys forces helper mode below. Dedicated `ASTRA_ALPACA_*` keys remain available later if Astra ever needs its own book — set them and Astra automatically switches to that account.

## Helper mode is enforced in code

When Astra resolves Bull's shared keys (precedence 2 or 3 above), the risk engine returns `PROPOSED_ONLY` for every BUY and SELL **even if `ASTRA_EXECUTION_ENABLED=true`**. There is no flag that lets Astra trade Bull's account. On a shared account Astra also leaves `return_pct` and `alpha_pct` blank in its dashboard state, because scoring an "Astra return" off Bull's equity would invent exactly the rival scorecard this pivot removes.

Only a dedicated Astra account can ever execute, and only with the execution flag on:

```text
ASTRA_EXECUTION_ENABLED=true   # optional secret or Actions variable; ignored on Bull's shared account
```

## Guardrails enforced in code

These apply to Astra's own account, should one ever exist. They are unchanged by the pivot:

- Long-only stocks/ETFs; no options, shorting, leverage, crypto, or symbols below $5.
- Maximum 6 open positions and 7% of equity per position.
- Maximum 0.5% of equity at risk on a new trade.
- Maximum 3 buys per rolling Monday–Friday week.
- No new buys after a 2% account decline versus prior close.
- Minimum model confidence of 75 for a buy.
- Every buy is submitted as an OTO market order with a 7% stop-loss.
- Paper only — the runner rejects any Alpaca base URL except `https://paper-api.alpaca.markets`.

## Role split — Astra proposes, the host decides

The model returns one JSON decision per run; `runner.py` decides what may happen to it. The model never sizes or authorizes a trade: confidence ≥75 is a *proposal* clearing the quality bar, not an instruction. Position size, the 7% stop, and every cap come from `config.json` and the runner.

This mirrors the pattern Nate Herk hit in *"I Turned GPT-6 Astra Into a 24/7 Stock Trader"* (Sep 2026, https://youtu.be/TLQLfa7yH4I): his Astra was blocked from placing trades, so he kept it as the strategist and handed execution to a separate "Trader" bot. Here the split is enforced in code rather than improvised, and the "Trader" on the other end of the handoff is Bull.

## Continuity — each run reads the last decision and writes the next

Every run is stateless, so the logs are the memory:

- `astra/memory/decision-log.jsonl` — one row per run: timestamp, routine, the decision JSON, and what the risk engine did with it. The next routine is handed the tail of this file (last 30 rows) before it decides anything.
- `astra/memory/proposals.jsonl` — the machine-readable proposal feed for Bull and Maverick.
- `astra/memory/trade-log.jsonl` — the append-only ledger of orders actually submitted (empty while Astra is in helper mode).
- `memory/astra-proposals.md` — the human-readable handoff, capped at the 40 most recent runs.
- `astra/dashboard/state.json` — the rendered snapshot, overwritten each run.

Astra also gets a bounded read-only look at Bull's `memory/portfolio.md` and the top of `memory/watchlist.md`, so proposals account for what Bull already owns and what is already on the bench. Astra never writes to those files.

## Helping Maverick

`limrie99/maverick` and `limrie99/maverick-aggressive` live in separate repositories, so this workflow cannot write to them. See `astra/handoff-maverick.md` for the copy-paste inbox template and the options for automating that hop.

## Schedule

Weekdays in America/New_York:

1. 8:00 — premarket research
2. 9:25 — opening plan
3. 10:15 — entry check
4. 12:30 — portfolio check
5. 15:00 — closing decision
6. 15:50 — risk shutdown and journal

GitHub cron is UTC-only, so the workflow schedules both daylight- and standard-time candidates. `runner.py --scheduled` checks New York local time and skips the wrong candidate. It also allows up to 45 minutes of GitHub Actions start delay so a late cron still runs the intended slot without overlapping the next one.

Six wakeups a day is a *monitoring* cadence, not a day-trading one. `risk-shutdown` means **no new buy proposals plus a journal** — nothing is flattened, and the team holds positions overnight with stops doing the work. (Bull makes the same choice explicitly in `memory/strategy.md` under *Schedule mapping*.)

Manual dry run (no API keys needed, writes nothing to shared memory):

```bash
python astra/runner.py --fixture astra/tests/fixture.json --routine entry-check
```

Real run against the paper account:

```bash
python astra/runner.py --routine entry-check
```

Unit tests:

```bash
python -m unittest discover -s astra/tests -p "test_*.py" -v
```

After the secrets are in place, verify with Actions → Astra paper trader → Run workflow → `entry-check` (or wait for the next weekday slot). The job summary states which credential pair was used and whether helper mode is forced on — by name only, never by value.

The dashboard is `astra/dashboard/index.html`. It reads `astra/dashboard/state.json` and refreshes automatically.
