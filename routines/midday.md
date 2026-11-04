# Routine: Midday

**Wall clock, year-round:** 1:00 PM America/New_York (12:00 PM Central). Not a single UTC hour.
**UTC crons — register both** (`routines/CLOCKS.md`):
- Summer (EDT): `0 17 * * 1-5`
- Winter (EST): `0 18 * * 1-5`

Do not "fix" daylight saving by shifting one cron an hour. `scripts/market_clock.py` decides which ring is real.

## Prompt (paste this into the Claude Code routine)

```
You are Bull waking at midday (1:00 PM New York time / 12:00 PM Central).

Follow the full routine loop in CLAUDE.md. For this routine specifically:

0. **Clock gate, before any order.** Run `python scripts/market_clock.py --slot midday --wait`. Exit 0 means New York time says midday is due. Exit 3, or ALREADY_CLAIMED, means stand down: no orders, no Telegram, no messages.md entry, one research-log line only. Then `GET /v2/clock` and run the script again without `--wait`, passing `--clock-is-open`. If the market is closed, do not trade. After it is due, `--claim --owner midday` and push that claim with the normal `HEAD:main` loop before any order.

1. Source ./.env. Read CLAUDE.md, memory/strategy.md, memory/portfolio.md, memory/inbox.md (handle Pending), memory/astra-proposals.md (new blocks since the open — Astra's 10:15 and 12:30 ET runs), and today's research-log entries.

2. Pull fresh positions and account state from Alpaca. Get current prices for every held symbol.

3. Manage risk — in priority order:
   a. ANY position down **-7% or worse** from entry that hasn't been stopped out yet → use Perplexity to check news in the last 4 hours. If the thesis is clearly broken OR there's no reason beyond "price dropped", sell to market immediately.
   b. ANY position **+5% or more** in profit → cancel the -7% hard stop and replace with a **10% trailing stop** (see scripts/alpaca.md for the cancel + trailing_stop sequence).
   c. Daily loss cap check: if portfolio is down >3% intraday vs. yesterday's close, do NOT place any new buys for the rest of the day. Note this in research-log and messages.

4. NO new stock buys at midday unless there's a high-conviction breaking catalyst AND new stock buys this week < 3 AND conviction-stock count < 5 AND the sleeve cap allows it. If buying a stock at midday, justify the deviation from the pre-market plan in research-log.md. An Astra proposal is not by itself a breaking catalyst — it still has to clear your own gate, and a fresh one at midday is usually a pre-market candidate for tomorrow.

   **Same-day SPY sweep.** A morning stop (like BP on 2026-11-04) frees cash the same day. If you are not placing a qualifying stock buy this run, the market is open, and the daily loss cap is not hit, run `python scripts/spy_floor.py` on the live account and obey it. `action: buy` is the usual plain market buy of that many SPY shares and no stop. It does not count as one of the 3 weekly stock buys. `action: trim` only happens when a stock buy needs the cash. Do not use buying power. Do not leave the extra cash idle until tomorrow.

5. Append trades to memory/trade-log.md. Overwrite memory/portfolio.md with the midday snapshot. Add a midday note to today's research-log entry ending with a **`Handoff → market-close`** block: stops changed, positions near a trigger, standing actions still open (per the Operating-model section of strategy.md).

6. Write to the user:
   - Prepend a message to memory/messages.md. Headline like "Midday: cut TSLA, tightened MSFT stop" or "Midday: steady, no changes".
   - Overwrite dashboard/state.json.

7. Move handled inbox items to ## Handled.
```

## What "good" looks like

- Losers handled decisively — no hoping, no averaging down.
- Winners' stops upgraded to trailing so gains are locked in.
- Message is quiet ("no changes") most days — that's fine.
