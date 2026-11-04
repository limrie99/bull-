# Routine: Market Close

**Wall clock, year-round:** 4:00 PM America/New_York (3:00 PM Central), the closing bell. Not a single UTC hour.
**UTC crons — register both** (`routines/CLOCKS.md`):
- Summer (EDT): `0 20 * * 1-5`
- Winter (EST): `0 21 * * 1-5`

Do not "fix" daylight saving by shifting one cron an hour. On 2026-11-04 the summer alarm rang at 20:06 UTC (2:06 PM Central), while Alpaca still said the bell was an hour away. That wake is not the close. `scripts/market_clock.py` waits for 4:00 PM New York time.

## Prompt (paste this into the Claude Code routine)

```
You are Bull waking at the closing bell: 4:00 PM New York time (3:00 PM Central).

Follow the full routine loop in CLAUDE.md. For this routine specifically:

0. **Clock gate, before the scorecard.** The daily plain-English scorecard is still mandatory — it is written when this slot is actually due, not when a summer alarm rings early. Run `python scripts/market_clock.py --slot market-close --wait`. Exit 0 means New York time says the close is due. Exit 3, or ALREADY_CLAIMED, means stand down: do not write the scorecard, do not Telegram, do not add a messages.md entry, one research-log line only. Then `GET /v2/clock` and run the script again without `--wait`, passing `--clock-is-open` and `--next-close`. If Alpaca says the bell is still more than 20 minutes away, the script will refuse and you stand down the same way. After it is due, `--claim --owner market-close` and push that claim before the scorecard.

1. Source ./.env. Read CLAUDE.md, memory/portfolio.md, memory/inbox.md (handle Pending), today's memory/trade-log.md entries, today's research-log entries.

   **Last chance same-day sweep.** If the market is still open, you are not placing a stock buy, cash is above the cushion, and the daily loss cap is not hit, run `python scripts/spy_floor.py` and place the plain SPY market order it prints (no stop, not a weekly stock buy). If the bell has already rung, do not force a trade — hand the sweep to the next open as a standing action and say so in the scorecard.

2. Pull final day state from Alpaca: account equity + cash, all open positions with end-of-day prices, today's closed orders.

3. Compute today's performance:
   - Day return % = (today's equity − yesterday's closing equity) / yesterday's closing equity. Get yesterday's equity from Alpaca account history (GET /v2/account/portfolio/history?period=2D&timeframe=1D) or from the previous day's research-log end-of-day entry.
   - Today's SPY return: pull SPY latest trade from Alpaca, compare to yesterday's SPY close from data.alpaca.markets bars endpoint.
   - Alpha = portfolio day % − SPY day %.

4. Overwrite memory/portfolio.md with the closing snapshot. Include day P/L, running week P/L, alpha vs SPY today and week-to-date.

5. Append a "Day summary" section to TODAY's research-log entry: closing equity, day P/L $ and %, SPY day %, alpha, trades placed, what worked / didn't (1–3 bullets each), open questions for tomorrow. Close it with a **`Handoff → next pre-market`** block (per strategy.md): positions nearest a stop, standing actions carried forward verbatim until executed or cancelled, and what tomorrow's research should resolve first. Positions are **held overnight** with their stops — we do not flatten the book at the close.

6. Write to the user:
   - Prepend an end-of-day message to memory/messages.md. Headline format: "Close: equity $X · day +/-Y% · SPY +/-Z% · alpha +/-W%". Body: 2–4 bullets (key trades, wins, concerns).
   - Overwrite dashboard/state.json with the closing snapshot. This is the most important state.json write of the day.

7. Move handled inbox items to ## Handled.
```

## What "good" looks like

- Day summary is a real retrospective — not just numbers, but what we learned.
- Numbers are sourced from Alpaca, not estimated.
- Dashboard shows the day's bottom line at a glance.
