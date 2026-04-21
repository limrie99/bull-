# Routine: Pre-Market

**Schedule:** Weekdays, 6:00 AM CT (Mon–Fri)
**Cron equivalent:** `0 6 * * 1-5` (US Central)

## Prompt (paste this into the Claude Code routine)

```
You are Bull waking for the pre-market routine at 6:00 AM CT. Market opens in 3.5 hours.

Follow the full routine loop in CLAUDE.md. For this routine specifically:

1. Source ./.env and read CLAUDE.md, memory/strategy.md, memory/portfolio.md, memory/inbox.md (handle Pending), last 10 entries of memory/trade-log.md, and top 3 entries of memory/research-log.md.

2. **Spin up your wealth-advisor sub-agent team in parallel** (Agent tool). Give each sub-agent one research thread, Perplexity access (see scripts/perplexity.md), and a concise report-back format:
   - Macro analyst — overnight futures (ES, NQ), global indices, Treasury yields, FX/commodities, top macro headlines since yesterday's close.
   - Earnings analyst — companies reporting today (pre-open and post-close), consensus vs whisper, guidance risk.
   - Position analyst — one per current holding: material news, analyst action, sector developments in the last 24h.
   - Opportunity scout — propose 3–5 candidate symbols matching the buy signals in memory/strategy.md with clear near-term catalysts.
   
   Synthesize their digests into one coherent pre-market view.

3. Prepend a new entry to memory/research-log.md with today's date and "pre-market" header. Sections: Market context, Portfolio watch, Buy candidates (with signals matched + conviction), Sell candidates.

4. Do NOT place any trades. Market is closed.

5. Write to the user:
   - Prepend a message to memory/messages.md (newest on top) — a short "pre-market plan" summary: headline (e.g. "Quiet open expected; 2 buy ideas flagged"), 2–4 bullets (top ideas, anything concerning about current holdings).
   - Overwrite dashboard/state.json per scripts/dashboard.md schema. Positions and equity may be stale pre-market — fetch fresh via Alpaca to be accurate. Add your message to latest_messages.

6. If inbox had items, move handled ones to ## Handled in memory/inbox.md with a note.
```

## What "good" looks like

- Research log entry is 200–400 words, structured, actionable.
- Buy candidates name specific catalysts and which signals hit — not generic.
- messages.md entry is ≤ 80 words. User can read it in 10 seconds on the dashboard.
