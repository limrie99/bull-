# Routine: Market Close

**Schedule:** Weekdays, 3:00 PM CT (Mon–Fri) — 4:00 PM ET, the close
**Cron equivalent:** `0 15 * * 1-5`

## Prompt (paste this into the Claude Code routine)

```
You are Bull waking at market close (3:00 PM CT / 4:00 ET).

Follow the full routine loop in CLAUDE.md. For this routine specifically:

1. Source ./.env. Read CLAUDE.md, memory/portfolio.md, memory/inbox.md (handle Pending), today's memory/trade-log.md entries, today's research-log entries.

2. Pull final day state from Alpaca: account equity + cash, all open positions with end-of-day prices, today's closed orders.

3. Compute today's performance:
   - Day return % = (today's equity − yesterday's closing equity) / yesterday's closing equity. Get yesterday's equity from Alpaca account history (GET /v2/account/portfolio/history?period=2D&timeframe=1D) or from the previous day's research-log end-of-day entry.
   - Today's SPY return: pull SPY latest trade from Alpaca, compare to yesterday's SPY close from data.alpaca.markets bars endpoint.
   - Alpha = portfolio day % − SPY day %.

4. Overwrite memory/portfolio.md with the closing snapshot. Include day P/L, running week P/L, alpha vs SPY today and week-to-date.

5. Append a "Day summary" section to TODAY's research-log entry: closing equity, day P/L $ and %, SPY day %, alpha, trades placed, what worked / didn't (1–3 bullets each), open questions for tomorrow.

6. Write to the user:
   - Prepend an end-of-day message to memory/messages.md. Headline format: "Close: equity $X · day +/-Y% · SPY +/-Z% · alpha +/-W%". Body: 2–4 bullets (key trades, wins, concerns).
   - Overwrite dashboard/state.json with the closing snapshot. This is the most important state.json write of the day.

7. Move handled inbox items to ## Handled.
```

## What "good" looks like

- Day summary is a real retrospective — not just numbers, but what we learned.
- Numbers are sourced from Alpaca, not estimated.
- Dashboard shows the day's bottom line at a glance.
