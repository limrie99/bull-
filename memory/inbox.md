# Inbox — talk to Bull

Write messages to Bull here. Bull reads this file at the start of **every routine**, acts on anything actionable, and replies in `memory/messages.md` (which shows up in the dashboard).

Add a new `## YYYY-MM-DD HH:MM` header with your request under **Pending**. When Bull handles a message, it moves the entry to **Handled** with a note about what it did.

---

## Pending

(nothing — add a `## date-time` header above with your message to Bull)

---

## Handled

### 2026-06-10 · "I want a daily update in easy English explaining how we're doing"
Handled by updating `CLAUDE.md` — added a standing rule under Communication style: the **market-close routine now sends a mandatory plain-English "How we're doing" daily update every trading day** (to the dashboard message log AND Telegram), even on quiet no-trade days, leading with a beginner scorecard (up/down in $ and %, vs. the S&P 500, and whether we're ahead). This was already happening most days; the rule makes it guaranteed and never skipped.
