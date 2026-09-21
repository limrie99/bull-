# Inbox — talk to Bull

Write messages to Bull here. Bull reads this file at the start of **every routine**, acts on anything actionable, and replies in `memory/messages.md` (which shows up in the dashboard).

Add a new `## YYYY-MM-DD HH:MM` header with your request under **Pending**. When Bull handles a message, it moves the entry to **Handled** with a note about what it did.

---

## Pending

_(nothing pending)_

---

## Handled

### 2026-09-21 · Astra fold-in (both blocks) — "voices/continuity from Herk, no day-trading" + "Astra HELPS, does not compete"
_handled 2026-09-21 15:00 CT by market-close._ Confirmed on `main`: `memory/strategy.md` carries both the "Operating model — voices, continuity, and research fan-out" section (line ~128) and the "Astra as the outside research voice" section (line ~148) plus the dated 2026-09-21 changelog entry; `scripts/dashboard.md` has the "Who's talking" label guidance; the `astra/` folder (README, config, runner, tests, handoff-maverick) is present; and **`memory/astra-proposals.md` exists** (initialized, "No proposals yet" — nothing to fold into today's scoring). Wrote Lauren a plain-English note in `messages.md` (in the *Why* section of the close message): the three internal Bull hats (**research** proposes, **risk** checks sizing/stops, **trader** is the only one that places orders), plus **Astra** as a fourth *outside* helper that can suggest but **can never trade** this account, and that we deliberately **skipped the video's day-trade / flatten-by-afternoon cadence** and changed **no guardrail** (still paper). Both original blocks preserved below.

---

### 2026-09-21 · "Fold Nate Herk's Astra setup into our strategy — without turning Bull into a day trader"
Lauren asked me to absorb the useful ideas from Nate Herk's *"I Turned GPT-6 Astra Into a 24/7 Stock Trader"* (https://youtu.be/TLQLfa7yH4I, Sep 2026) and his follow-up where Astra, blocked from placing trades, became the **strategist** while a separate "Trader" bot executed: the strategist/executor role split, the read-handoff → act → write-handoff continuity loop, research fan-out, and secrets-in-env — while explicitly **not** adopting his day-trade "flatten everything by mid-afternoon" cadence and **not** weakening any guardrail.

**Status:** a docs-only change is open on `main` for this — `memory/strategy.md` (new "Operating model — voices, continuity, and research fan-out" section + dated 2026-09-21 changelog entry), `astra/README.md`, and `scripts/dashboard.md` (who's-talking label guidance). No trade, no guardrail change, no live trading.

### 2026-09-21 (later, supersedes the Astra part of the note above) · "Astra must HELP Bull and both Mavericks — not compete"
Lauren retired the league framing: Astra is no longer an independent third book scored head-to-head against me and Maverick. **Astra is now the team's outside Research/Strategist helper.** It scores ideas and writes proposals to **`memory/astra-proposals.md`**; I read that file at pre-market, market-open, and midday and treat each block as evidence for my own scoring — never a pre-approved trade.

She also authorized Astra to use **my existing Alpaca paper Actions secrets plus `OPENAI_API_KEY`**, so there are no separate Astra keys to create. Because we are now on one shared paper account, Astra's runner **hard-blocks execution** whenever those shared keys are in use — every Astra decision returns `PROPOSED_ONLY`, even with its execution flag on. It cannot place an order on this book, so there is no conflicting-order risk from Astra itself. Dedicated `ASTRA_ALPACA_*` keys stay optional for later and would take precedence automatically.

**Status:** shipped in the same PR as the note above — `astra/` (helper framing, shared-secret resolution, proposal writer, tests), `.github/workflows/astra.yml` (Bull's secret names, paper URL still hard-coded), `memory/strategy.md` (new "Astra as the outside research voice" section + dated changelog entry superseding the old "blind to Bull" clause), the three routines that now read the proposals file, `CLAUDE.md`, `scripts/dashboard.md`, the root README, and `astra/handoff-maverick.md` for the Maverick hop. **No guardrail changed. Paper only.**

### 2026-08-27 ~20:20 CT · "start spending some cash" / "keep a safe 10k" / "your job is to invest"
_handled 2026-08-31 08:40 CT by market-open: EXECUTED the cash deploy._ Weekend veto window closed with no countermand → the deploy stood. At the live open (market confirmed open, mild-but-orderly risk-off tape, intraday −0.34% well under the loss cap) I placed two buys: (1) enlarged the SPY market-floor sleeve by 38 shares @ $766.34 ($29,120.92, no stop — index sleeve), and (2) opened a modest ATI starter, 47 shares @ $209.67 ($9,854.48) with a −7% hard stop at $194.99 — ATI re-confirmed live (~72 B+, 2 verified signals #3 secular + #6 clean uptrend, no adverse news, no binary event in 3 days, ~$28-29B large-cap; sized at the LOW end of the B+ band for the insider-selling yellow flag). Together these moved whole-book cash from ~$49,390 (~49.32%) to **~$10,414.51 (~10.42%)** — on Lauren's ~$10k target, above the 10% floor. Conviction ≥70 gate NOT lowered (ATI cleared it on merit); BJ/ROST NOT force-bought (still below trend). Conviction sleeve now 3/5; weekly buys 1/3. The Friday miss is closed.

### 2026-08-07 · "Edit strat to go forward" → APPROVED Option B (S&P 500 market floor)
_handled 2026-08-07 by weekly-review follow-up._ Read Lauren's reply as her answer to the escalated A/B cash decision: go forward with **Option B**, my recommended path. Edited `strategy.md`: added a "Cash-deployment / market-floor policy" section + a dated changelog RULE-CHANGE entry. Policy: park idle cash in a broad S&P 500 ETF (SPY/VOO) to move total cash from ~75% toward 50–55%, initial tranche ≈20% of equity; the floor is its own sleeve exempt from the single-position / max-5 / max-3-per-week caps and carries **no stop** (index-sleeve-only carve-out); the **≥70 Conviction gate and all individual-stock stops are unchanged**. Market was closed at edit time, so **execution is deferred to the Mon 2026-08-10 market-open routine** — that run must build the floor at live prices and log it. Weekend veto window open for Lauren. **STANDING ACTION FOR MON 8/10 OPEN: build the S&P 500 market floor per the new policy unless Lauren countermands here first.**

### 2026-06-10 · "I want a daily update in easy English explaining how we're doing"
Handled by updating `CLAUDE.md` — added a standing rule under Communication style: the **market-close routine now sends a mandatory plain-English "How we're doing" daily update every trading day** (to the dashboard message log AND Telegram), even on quiet no-trade days, leading with a beginner scorecard (up/down in $ and %, vs. the S&P 500, and whether we're ahead). This was already happening most days; the rule makes it guaranteed and never skipped.
