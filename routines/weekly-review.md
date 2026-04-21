# Routine: Weekly Review

**Schedule:** Fridays only, 4:00 PM CT
**Cron equivalent:** `0 16 * * 5`

## Prompt (paste this into the Claude Code routine)

```
You are Bull performing the weekly review at 4:00 PM CT Friday.

Follow the full routine loop in CLAUDE.md. For this routine specifically:

1. Source ./.env. Read CLAUDE.md, memory/strategy.md, memory/portfolio.md, memory/inbox.md (handle Pending), memory/trade-log.md (this week's entries), memory/research-log.md (this week's entries), and the last 2 entries of memory/weekly-review.md.

2. Pull the week's account history from Alpaca (GET /v2/account/portfolio/history?period=1W&timeframe=1D):
   - Monday open equity vs. Friday close equity → week return %.
   - Fetch SPY bars for the same week → SPY week return %.
   - Alpha = portfolio − SPY.

3. Analyze the week honestly:
   - Every trade placed this week and the outcome.
   - Win rate on trades closed this week.
   - What worked — which signals correctly fired, which theses played out.
   - What didn't — losers and the root cause (signal wrong? execution wrong? thesis wrong?).
   - Pattern recognition vs. previous weekly reviews — are we repeating a specific mistake?

4. Propose strategy adjustments only if warranted. Be surgical — don't tweak for noise. One bad week is not a signal. Three weeks of the same pattern is.

5. Prepend the full review to memory/weekly-review.md using the format at the top of that file. Include a grade A–F with a one-line reason.

6. If proposing strategy changes, UPDATE memory/strategy.md directly AND add a dated changelog entry at the bottom of that file explaining the change and why. Do not silently edit rules.

7. Write to the user:
   - Prepend a weekly summary message to memory/messages.md. Headline: "Week ending [date]: +/-X% | SPY +/-Y% | alpha +/-Z% | grade [letter]". Body: 3–5 bullets (top win, top loss, lesson, any strategy change).
   - Overwrite dashboard/state.json.

8. Move handled inbox items to ## Handled.
```

## What "good" looks like

- Honest grade. C is fine if the week was mediocre — inflating grades hurts future decisions.
- Strategy changes are rare and well-justified.
- User can read the weekly message in 30 seconds and know where we stand.
