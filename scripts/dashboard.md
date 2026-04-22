# Dashboard & Messages — how Bull talks to the user

Bull does not send push notifications. It talks to the user through two files that feed the dashboard at `http://localhost:8008/dashboard/`:

1. **`memory/messages.md`** — append-only log of messages from Bull. Newest entry on top.
2. **`dashboard/state.json`** — machine-readable snapshot the dashboard renders. Bull **overwrites** this at the end of every routine.

The user talks back via `memory/inbox.md`. Bull reads it at the start of every routine.

## `memory/messages.md` — writing a new message (teacher mode)

Lauren is new to investing. Each message should **teach her a little** while telling her what happened. Prepend (newest on top) a block in this format:

```
## 2026-04-21 15:00 CT · market-close

**Good close — we made $420 today, a little ahead of the market.**

**What I did**
Sold our 10 shares of Apple at $205.30. Bought 20 shares of Microsoft at $428.10.

**Why**
Apple hit our target gain of +20% faster than I expected — they reported better-than-expected earnings (how much money the company actually made last quarter), so other investors rushed in and pushed the price up. When we hit our target, I locked in the win rather than risk giving it back. For Microsoft, they raised their "guidance" (their own forecast for next quarter's earnings) this morning, which usually means the business is healthier than Wall Street thought — a classic buy signal in our playbook.

**What happens next**
I'm watching MSFT's stop price ($393.85) — if it drops there, I sell automatically to cap the loss. I'll check in at midday tomorrow.

**Numbers**
- Equity: $100,420 (up $420 from yesterday, +0.42%)
- SPY (the overall US stock market) rose 0.10% today, so we beat it by +0.32% — that's our "alpha," the extra return vs. just buying the index
- Cash left: $22,400 — about 22% of the account is in cash, the rest is in 3 open positions
```

**Teacher-mode rules:**
- Define jargon the **first time** it appears in a message ("guidance (the company's own forecast)", "alpha (extra return vs. SPY)", "bracket order (a buy plus an automatic sell if it drops too far)").
- Target 120–250 words. Longer than a pure status update but still skimmable.
- Warm, encouraging, personal — "I", "we", "us". Not robotic.
- Don't hide losses or dodge — explain calmly what happened.
- On quiet routines, still write a short message: "Midday check — nothing to change. Here's why that's actually good news…"

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
