# Messages from Bull

Append-only conversation log. **Most recent at the top.** Each entry is what Bull wants the user to see from a routine run.

Format:

```
## YYYY-MM-DD HH:MM CT · {routine name}

**Headline one-liner**

Body — short paragraph or bullets. What happened, what Bull decided, anything the user should know or decide on.
```

---

## 2026-04-22 06:00 CT · pre-market (halted — network)

**Halted — this runtime can't reach Alpaca or Perplexity. Credentials are fine; the problem is the sandbox egress.**

- User supplied keys mid-session; I wrote them to `.env` (mode 600, gitignored ✓) and sourced them. Alpaca + Perplexity DNS/TLS resolve, but Anthropic's egress proxy returns HTTP 403 "Host not in allowlist" for both `paper-api.alpaca.markets` and `api.perplexity.ai`. GitHub is allowed, everything else is blocked.
- Per guardrails, halted before any trade or fabricated research. No Alpaca fetch, no Perplexity, no sub-agents dispatched. Portfolio values carried forward from 2026-04-21 17:00 CT.
- **Action needed:** run this routine in an environment with outbound access to those hosts (local machine with `./.env`, or a cloud runner whose egress policy allows `*.alpaca.markets` and `api.perplexity.ai`). The scheduled Claude Code routines on your laptop should Just Work — this blocked environment is specific to the current session.
- Next wake (midday 4/22) will re-attempt; same block will likely recur here until the egress policy changes.

---

## 2026-04-21 17:00 CT · pre-market (for 4/22)

**First research pass — no high-conviction buy ideas yet; saving cash for a better scan.**

- Fresh paper account confirmed: $100K cash, 0 positions.
- Setup into Wed 4/22: mildly risk-on on Mid-East de-escalation hopes (ES ~+0.35%). TSLA reports AMC 4/22 — biggest tape-setter.
- Scout found no name that cleanly hits ≥2 signals with a verified near-term catalyst. AMZN thesis is real but inside the 3-day earnings window; skipping.
- Next pre-market (6 AM CT 4/22): tighter scan on a seed watchlist (NVDA, AVGO, GOOGL, PLTR, CRWD, PANW) with earnings dates pulled from Alpaca first.

---

(earlier messages below)
