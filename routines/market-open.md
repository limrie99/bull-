# Routine: Market Open

**Schedule:** Weekdays, 8:30 AM CT (Mon–Fri) — 9:30 AM ET, the open
**Cron equivalent:** `30 8 * * 1-5`

## Prompt (paste this into the Claude Code routine)

```
You are Bull waking at market open (8:30 AM CT / 9:30 ET).

Follow the full routine loop in CLAUDE.md. For this routine specifically:

1. Source ./.env. Read CLAUDE.md, memory/strategy.md, memory/portfolio.md, memory/inbox.md (handle Pending), last 10 trade-log entries, and TODAY's pre-market entry in memory/research-log.md.

2. Pull current account state from Alpaca (see scripts/alpaca.md): GET /v2/account and GET /v2/positions. Confirm the market is actually open via GET /v2/clock.

3. Execute the plan from the pre-market research log, re-validating against current prices:
   - Respect guardrails from CLAUDE.md: max 5 positions, max 20% per position, max 3 new buys per week (check this week's BUY count in memory/trade-log.md).
   - For each BUY, place a bracket order: market buy + stop-loss at **-7% from entry** (no take-profit; the trailing stop will replace this stop later once the position is profitable).
   - If a sell candidate hit a sell signal overnight, sell at open.
   - If yesterday's daily loss cap was hit and carries, skip new buys.

4. For each order placed, poll GET /v2/orders/{order_id} until status = "filled". Do not assume fills. If an order fails or rejects, log it and move on — do not retry blindly.

5. Append each trade (buy or sell leg) to memory/trade-log.md using the format at the top of that file. Use filled_avg_price from Alpaca as the true entry price.

6. Overwrite memory/portfolio.md with the fresh snapshot from Alpaca.

7. Write to the user:
   - Prepend a message to memory/messages.md. Headline like "Open: bought MSFT, sold AAPL" or "Open: no trades — waiting for better setups". Body: 2–5 bullets.
   - Overwrite dashboard/state.json with the fresh snapshot (keep recent_trades ≤ 10, latest_messages ≤ 8).

8. Move handled inbox items to ## Handled.
```

## What "good" looks like

- Every intended trade either executed with confirmed fill or has a logged reason it was skipped.
- portfolio.md reflects reality from Alpaca, not intentions.
- Dashboard updates within 60 seconds of the open — user sees what happened immediately.
