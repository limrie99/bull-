# Handing Astra's proposals to the Maverick agents

Astra helps three teammates: **Bull** (this repo), **`limrie99/maverick`**, and **`limrie99/maverick-aggressive`**. Bull is easy — Astra writes `memory/astra-proposals.md` in this repository and Bull's routines read it. The Mavericks live in separate repositories, so the handoff needs one deliberate hop.

Nothing here lets Astra place an order anywhere. A proposal that reaches a Maverick inbox is research, and that agent's own guardrails still decide everything.

## What to copy

The source of truth is `memory/astra-proposals.md` (human-readable, newest on top) with the same content in `astra/memory/proposals.jsonl` (one JSON object per run — use this if you are automating).

Only forward proposals worth a teammate's attention: `BUY`, `SELL`, or a `WATCH` with a dated catalyst. Routine `HOLD` rows are continuity notes for Astra, not news for anyone else.

## Inbox template

Paste into the Maverick repo's inbox file under its **Pending** section, filling in from the proposal block:

```markdown
### YYYY-MM-DD HH:MM · Astra proposal — <ACTION> <TICKER> (confidence <NN>)

Astra (the team's GPT-6 research helper in `limrie99/bull-`) scored this idea and wrote it to
`memory/astra-proposals.md`. It is **research only** — Astra does not trade and has no keys to
this account. Apply this book's own gate, sizing, and stop rules before acting on it, and log
the decision either way.

- **Thesis:** <one or two plain-English sentences>
- **Strongest counter-argument:** <the other side>
- **What would prove it wrong:** <invalidation condition>
- **Entry condition:** <price/level/event that has to happen first>
- **Intended holding period:** <days / weeks / months>
- **Sources:** <links or "none recorded">
- **Astra's status on it:** PROPOSED_ONLY (helper mode — Astra shares Bull's paper account and cannot place orders)

**If you take it:** note in your trade log that the idea originated with Astra, so we can tell
later whether Astra's proposals actually helped.
**If you pass:** one line on why is enough — that feedback is how Astra gets better.
```

## Who does the copying

In order of preference:

1. **A Grok Bot routine in the Maverick repo** pulls the raw proposals file each morning and appends new blocks to its own inbox. No credentials needed — the file is public in this repository:
   ```
   https://raw.githubusercontent.com/limrie99/bull-/main/astra/memory/proposals.jsonl
   ```
   De-duplicate on the `timestamp` field, which is unique per run.
2. **A follow-up PR on each Maverick repo** adding that fetch step to its pre-market routine. Out of scope here — this repository cannot write to those repos, and a cross-repo push would need a new token, which is a bigger permission grant than this change is asking for.
3. **Lauren copies a block by hand** when one looks worth it. Always available, no setup.

## What Astra does not do

- It does not write to the Maverick repositories.
- It does not hold or request Maverick's Alpaca keys.
- It does not track "who won." If a Maverick book takes an Astra idea and does well, that is the system working as intended.
