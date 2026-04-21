# Telegram Push Notifications (optional)

The dashboard at `http://localhost:8008/dashboard/` is Bull's primary voice. Telegram is a **push layer on top** for events Bull doesn't want the user to miss when they're away from the dashboard.

## Env vars

- `TELEGRAM_BOT_TOKEN` — from @BotFather
- `TELEGRAM_CHAT_ID` — your personal chat id

Both are **optional**. If either is empty, Bull writes to `memory/messages.md` and the dashboard as usual and **skips Telegram silently** (no error).

## When to push to Telegram

Push on: trade placed, stop triggered, daily close summary, weekly review, urgent (>3% intraday drop, API failure, need user decision).

Do NOT push on: routine pre-market scan with no trades, quiet midday check, research-only work.

## Send a message

Before each push, check both vars are non-empty. If empty, skip.

```bash
if [ -n "$TELEGRAM_BOT_TOKEN" ] && [ -n "$TELEGRAM_CHAT_ID" ]; then
  curl -s -X POST "https://api.telegram.org/bot${TELEGRAM_BOT_TOKEN}/sendMessage" \
    -H "Content-Type: application/json" \
    -d "{\"chat_id\":\"${TELEGRAM_CHAT_ID}\",\"text\":\"${TEXT}\",\"parse_mode\":\"Markdown\"}"
fi
```

Message style: mirror the headline + first 2 bullets from the message Bull just wrote to `memory/messages.md`. Keep it to what fits on a phone lock screen. No need to repeat everything that's on the dashboard.

If the API returns `"ok": false`, log the `description` to `memory/research-log.md` and move on. Do not retry in a loop.

## Getting the chat_id (one-time)

1. Create a bot via @BotFather in Telegram → you get `TELEGRAM_BOT_TOKEN`.
2. Send any message to your new bot.
3. Visit `https://api.telegram.org/bot<TOKEN>/getUpdates` in a browser.
4. Look for `"chat":{"id":<number>}` — that number is `TELEGRAM_CHAT_ID`.
