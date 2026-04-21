# Dashboard & Messages — how Bull talks to the user

Bull does not send push notifications. It talks to the user through two files that feed the dashboard at `http://localhost:8008/dashboard/`:

1. **`memory/messages.md`** — append-only log of messages from Bull. Newest entry on top.
2. **`dashboard/state.json`** — machine-readable snapshot the dashboard renders. Bull **overwrites** this at the end of every routine.

The user talks back via `memory/inbox.md`. Bull reads it at the start of every routine.

## `memory/messages.md` — writing a new message

Prepend (newest on top) a block like:

```
## 2026-04-21 15:00 CT · market-close

**Equity $100,420 · day +0.42% · SPY +0.10% · alpha +0.32%**

Sold AAPL 10 @ $205.30 — thesis hit +20% take-profit sooner than expected after earnings surprise. Added MSFT 20 @ $428.10 at open on upgraded guidance.
Open: MSFT, NVDA, COST. Cash $22,400. Nothing worrying heading into tomorrow.
```

Keep it **short** — headline + one paragraph or a few bullets. Users skim this.

## `dashboard/state.json` — full schema

Overwrite the file completely each routine. All fields present, use `null` when unknown. Money values are plain numbers (not strings), not including `$`. Percents are numbers like `1.42` meaning 1.42%.

```json
{
  "last_update": "2026-04-21 15:00 CT",
  "last_routine": "market-close",
  "mode": "paper",
  "equity": 100420.12,
  "cash": 22400.50,
  "day_pl": 420.12,
  "day_pl_pct": 0.42,
  "week_pl_pct": 1.24,
  "spy_week_pct": 0.80,
  "alpha_week_pct": 0.44,
  "positions": [
    {
      "symbol": "MSFT",
      "qty": 20,
      "avg_cost": 428.10,
      "current": 430.50,
      "pl_pct": 0.56,
      "stop": 393.85
    }
  ],
  "recent_trades": [
    {
      "date": "2026-04-21 08:32",
      "side": "BUY",
      "symbol": "MSFT",
      "qty": 20,
      "price": 428.10
    }
  ],
  "latest_messages": [
    {
      "ts": "2026-04-21 15:00 CT",
      "routine": "market-close",
      "headline": "Equity $100,420 · day +0.42% · alpha +0.32%",
      "body": "Sold AAPL 10 @ $205.30 on +20% take-profit. Added MSFT 20 @ $428.10. Nothing worrying heading into tomorrow."
    }
  ]
}
```

Keep `recent_trades` to the last **10** trades, `latest_messages` to the last **8** entries. Older data is always available in `memory/trade-log.md` and `memory/messages.md`.

## `memory/inbox.md` — reading user messages

At the start of every routine:

1. Open `memory/inbox.md`.
2. Read everything under `## Pending`.
3. For each pending `## YYYY-MM-DD HH:MM` block:
   - If it's actionable within this routine's scope, act on it.
   - If it's informational, incorporate it into your reasoning.
   - If it's out of scope (e.g., "sell everything" during a research routine), defer to the next appropriate routine and note in the reply.
4. Move each handled block to the `## Handled` section with a one-line note prefixing the block: `_handled 2026-04-21 08:30 by market-open: sold AAPL as requested._`
5. Save the file.

If the user's message conflicts with a guardrail (e.g., asks to go to 50% in one position), **do not override the guardrail**. Explain the conflict in your reply message and leave the request in Pending.
