# Routine: Market Open

**Wall clock, year-round:** 9:30 AM America/New_York (8:30 AM Central), the opening bell. Not a single UTC hour.
**UTC crons — register both** (`routines/CLOCKS.md`):
- Summer (EDT): `30 13 * * 1-5`
- Winter (EST): `30 14 * * 1-5`

Do not "fix" daylight saving by shifting one cron an hour. On 2026-11-04 the summer alarm rang at 13:36 UTC (7:36 AM Central). `scripts/market_clock.py` waits for 9:30 New York time instead of trading early.

## Prompt (paste this into the Claude Code routine)

```
You are Bull waking at the opening bell: 9:30 AM New York time (8:30 AM Central).

Follow the full routine loop in CLAUDE.md. For this routine specifically:

0. **Clock gate, before any order.** Run `python scripts/market_clock.py --slot market-open --wait`. Exit 0 means New York time says the open is due. Exit 3, or ALREADY_CLAIMED, means stand down: no orders, no Telegram, no messages.md entry, one research-log line only. Then `GET /v2/clock` and run the script again without `--wait`, passing `--clock-is-open` and `--next-open`. Exit 2 is a holiday: tell Lauren the market is closed, place nothing. After it is due, `--claim --owner market-open` and push that claim with the normal `HEAD:main` loop before any order.

1. Source ./.env. Read CLAUDE.md, memory/strategy.md (the Conviction Score buy-gate, the same-day SPY sweep, the sleeve cap), memory/portfolio.md, memory/watchlist.md, memory/inbox.md (handle Pending), memory/astra-proposals.md (Astra's proposals from the 8:00 and 9:25 ET runs), last 10 trade-log entries, and TODAY's pre-market entry in memory/research-log.md.

2. Pull current account state from Alpaca (see scripts/alpaca.md): GET /v2/account and GET /v2/positions. Confirm the market is actually open via GET /v2/clock.

3. Execute the plan from the pre-market research log / top of the watchlist, re-validating against current prices:
   - **Astra proposals are research, never orders.** A name Astra proposed is buyable only if you scored it yourself and it clears the same gate as anything else. Astra shares our paper keys but is hard-blocked from trading this account, so there is never an Astra order to reconcile — if you see an order you did not place, something is wrong; log it and do not trade around it.
   - **Buy-gate (strategy.md):** only buy a name with **2+ buy signals AND Conviction Score ≥ 70**. If overnight news moved a candidate, recompute its score before acting — a name that has slipped below 70 stays on the watchlist, not in the book. Size per the score band (A: 15–20%, B+: 10–15%).
   - Respect guardrails from CLAUDE.md: max 5 conviction stocks, max 20% per stock, max 3 new stock buys per week (check this week's stock BUY count in memory/trade-log.md). SPY is not one of the five, is not capped at 20%, and a SPY top-up does not count as one of the three. The sleeve cap in strategy.md also applies: do not buy another defensive or low-beta name while 2 or more are already held. Do not sell a current holding to satisfy that cap.
   - For each stock BUY, place a plain market buy, then — after that buy fills — a separate GTC stop at **-7% from entry** (no take-profit; the trailing stop will replace this stop later once the position is profitable). If that buy would drop cash under the cushion, `scripts/spy_floor.py` will say `trim`: sell that many SPY shares first with the same plain market order (no stop on the SPY that remains).
   - **Same-day SPY sweep, after the stock decision.** If you are not placing a qualifying stock buy this run and the daily loss cap is not hit, run `python scripts/spy_floor.py` with live equity, cash, SPY price, SPY shares, and stock market value (`--stock-buy-dollars 0`). Obey the JSON. `action: buy` is a plain market buy of that many SPY shares (`type: market`, `time_in_force: day` — the order in `scripts/alpaca.md`), then no stop. Do not use buying power. Do not invent the share count. Re-pull cash and the SPY price immediately before sending it, and re-run the script if they moved. `action: none` means do not touch SPY.
   - If a sell candidate hit a sell signal overnight, sell at open.
   - If yesterday's daily loss cap was hit and carries, skip new buys.

4. Poll each market buy with GET /v2/orders/{order_id} until status = "filled". For a stock, confirm the separate GTC stop is resting (open, time_in_force gtc). For SPY, confirm there is no stop. Do not assume fills. If an order fails or rejects, log it and move on — do not retry blindly.

5. Append each trade (buy or sell leg) to memory/trade-log.md using the format at the top of that file. Use filled_avg_price from Alpaca as the true entry price.

6. Overwrite memory/portfolio.md with the fresh snapshot from Alpaca. Prepend a short market-open entry to memory/research-log.md — what you executed or declined and why (label the voices when Research and Trader disagreed, per strategy.md) — ending with a **`Handoff → midday`** block: levels to watch, stops to upgrade, standing actions still open.

7. Write to the user:
   - Prepend a message to memory/messages.md. Headline like "Open: bought MSFT, sold AAPL" or "Open: no trades — waiting for better setups". Body: 2–5 bullets.
   - Overwrite dashboard/state.json with the fresh snapshot (keep recent_trades ≤ 10, latest_messages ≤ 8).

8. Move handled inbox items to ## Handled.
```

## What "good" looks like

- Every intended trade either executed with confirmed fill or has a logged reason it was skipped.
- portfolio.md reflects reality from Alpaca, not intentions.
- Dashboard updates within 60 seconds of the open — user sees what happened immediately.
