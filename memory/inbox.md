# Inbox — talk to Bull

Write messages to Bull here. Bull reads this file at the start of **every routine**, acts on anything actionable, and replies in `memory/messages.md` (which shows up in the dashboard).

Add a new `## YYYY-MM-DD HH:MM` header with your request under **Pending**. When Bull handles a message, it moves the entry to **Handled** with a note about what it did.

---

## Pending

(nothing — add a `## date-time` header above with your message to Bull)

---

## Handled

### 2026-08-07 · "Edit strat to go forward" → APPROVED Option B (S&P 500 market floor)
_handled 2026-08-07 by weekly-review follow-up._ Read Lauren's reply as her answer to the escalated A/B cash decision: go forward with **Option B**, my recommended path. Edited `strategy.md`: added a "Cash-deployment / market-floor policy" section + a dated changelog RULE-CHANGE entry. Policy: park idle cash in a broad S&P 500 ETF (SPY/VOO) to move total cash from ~75% toward 50–55%, initial tranche ≈20% of equity; the floor is its own sleeve exempt from the single-position / max-5 / max-3-per-week caps and carries **no stop** (index-sleeve-only carve-out); the **≥70 Conviction gate and all individual-stock stops are unchanged**. Market was closed at edit time, so **execution is deferred to the Mon 2026-08-10 market-open routine** — that run must build the floor at live prices and log it. Weekend veto window open for Lauren. **STANDING ACTION FOR MON 8/10 OPEN: build the S&P 500 market floor per the new policy unless Lauren countermands here first.**

### 2026-06-10 · "I want a daily update in easy English explaining how we're doing"
Handled by updating `CLAUDE.md` — added a standing rule under Communication style: the **market-close routine now sends a mandatory plain-English "How we're doing" daily update every trading day** (to the dashboard message log AND Telegram), even on quiet no-trade days, leading with a beginner scorecard (up/down in $ and %, vs. the S&P 500, and whether we're ahead). This was already happening most days; the rule makes it guaranteed and never skipped.
