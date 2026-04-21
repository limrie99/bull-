# trading-routine — Bull

A 24/7 AI trading agent (Bull) built on **local** Claude Code routines. Paper trading on Alpaca, research via Perplexity. Bull talks to you through a local **dashboard**. Goal: beat SPY.

## Layout

```
CLAUDE.md              # Agent instructions — how Bull thinks
.env                   # Your API keys (gitignored)
start-dashboard.bat    # Launches the dashboard at http://localhost:8008/dashboard/
memory/
  strategy.md          # Trading rules and guardrails (edit to tune)
  portfolio.md         # Live snapshot of positions (Bull overwrites)
  trade-log.md         # Append-only trade ledger
  research-log.md      # Append-only research / decision log
  weekly-review.md     # Friday retros
  messages.md          # Bull → user message log (newest on top)
  inbox.md             # User → Bull message queue
routines/              # Prompts to paste into each Claude Code routine
  pre-market.md        # 6:00 AM CT  weekdays
  market-open.md       # 8:30 AM CT  weekdays
  midday.md            # 12:00 PM CT weekdays
  market-close.md      # 3:00 PM CT  weekdays
  weekly-review.md     # 4:00 PM CT  Fridays only
scripts/               # API cheat sheets Bull reads at runtime
  alpaca.md
  perplexity.md
  dashboard.md         # How Bull writes messages and state.json
dashboard/
  index.html           # The dashboard UI
  state.json           # Live snapshot Bull overwrites every routine
```

## Setup (one-time)

### 1. Fill in `.env`

Open `C:\Users\lhi\trading-routine\.env` and paste each key between the quotes. Save. Gitignored — stays on your machine.

Need keys?
- **Alpaca** (paper) — [alpaca.markets](https://alpaca.markets/) → Paper Trading → API Keys.
- **Perplexity** — [perplexity.ai](https://www.perplexity.ai/) → Settings → API.

### 2. Start the dashboard

Double-click `start-dashboard.bat` (or run it from a terminal). It starts a local web server on port 8008 and opens `http://localhost:8008/dashboard/` in your browser. Leave the window running while you want the dashboard live. Requires Python 3 on PATH.

### 3. Create five **local** routines in Claude Code desktop

For each file in `routines/`, create a Local routine:

- New Routine → **Local**
- Working directory: `C:\Users\lhi\trading-routine`
- Model: Claude Opus 4.7
- Schedule: copy the schedule from the top of the routine file
- Prompt: copy the code block from the routine file

No GitHub, no cloud environment needed — everything runs locally. Your computer must be on and Claude Code desktop must be running for local routines to fire on schedule.

### 4. Smoke test

Hit "Run now" on each routine once. Watch the stream. Verify:
- `memory/portfolio.md` updates with real Alpaca data
- `memory/messages.md` gets a new top entry
- `dashboard/state.json` updates
- The dashboard in your browser reflects the changes within 15 seconds (it auto-refreshes)

If an env var is missing or a call fails, Bull logs a clear error to `memory/messages.md` so you see it on the dashboard. Fix `.env` and re-run.

## Talking to Bull

- **Bull → you:** `memory/messages.md` (shown on the dashboard).
- **You → Bull:** edit `memory/inbox.md`, add a `## YYYY-MM-DD HH:MM` header under "Pending" with your message. Bull reads the inbox at the start of every routine. When handled, Bull moves the entry to "Handled" with a note.

## Flipping to live money (later, when you're ready)

1. Open a funded live Alpaca account and generate **new** live API keys.
2. Update `.env`:
   - `ALPACA_API_KEY` → live key
   - `ALPACA_SECRET_KEY` → live secret
   - `ALPACA_BASE_URL` → `https://api.alpaca.markets`
3. Edit `memory/strategy.md` → change `mode: paper` to `mode: live`.

Bull's `CLAUDE.md` refuses to trade live unless `strategy.md` says `mode: live`.

## Tuning

- Guardrails and position rules live in `memory/strategy.md` — edit that file, not `CLAUDE.md`.
- Strategy changes are logged in the changelog at the bottom of `strategy.md`.
- Don't delete `trade-log.md` / `research-log.md` / `messages.md` entries — append-only is how Bull learns.

## Benchmark

Only number that matters long-term: **alpha vs SPY**. Everything else is noise.
