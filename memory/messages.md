# Messages from Bull

Append-only conversation log. **Most recent at the top.** Each entry is what Bull wants the user to see from a routine run.

Format:

```
## YYYY-MM-DD HH:MM CT · {routine name}

**Headline one-liner**

Body — short paragraph or bullets. What happened, what Bull decided, anything the user should know or decide on.
```

---

## 2026-04-22 06:00 CT · pre-market — HALTED

**Halted: this environment's network sandbox is blocking Alpaca, Perplexity, and Telegram. No research, no trades.**

- Every call to `paper-api.alpaca.markets`, `api.perplexity.ai`, and `api.telegram.org` returns HTTP 403 `host_not_allowed` — blocked below the normal sandbox bypass. Only `api.github.com` is reachable, so commits/pushes still work.
- Creds you sent were written to local `.env` (gitignored, not committed). When routines run in the cloud, those vars need to be injected as real env vars — `.env` won't be there in a fresh clone.
- Yesterday's plan has **not** been re-validated this morning. If futures turned constructive overnight, the NVDA starter (~5% / ~$5K) from the 4/21 19:00 CT entry is still a candidate — but do not treat it as approved until we can re-check Alpaca + Perplexity live.
- **Action needed from you:** allow these hosts in the session/sandbox allowlist (`paper-api.alpaca.markets`, `data.alpaca.markets`, `api.perplexity.ai`, `api.telegram.org`) and re-run this routine. Market opens 08:30 CT — we have ~2.5h.

---

## 2026-04-21 19:00 CT · pre-market (re-run, for 4/22)

**Tape flipped mildly risk-off — NVDA is the only clean setup; leaning pass or small starter.**

- Futures faded: **ES −0.13%, NQ flat** evening. **10Y +4bps to 4.29%.** Crude up on Iran headlines (levels `n/a`). Wednesday looks macro-driven, not earnings-driven.
- **No confirmed mega-cap earnings for 4/22** in fresh pull — contradicts the earlier TSLA AMC read. Re-verify tomorrow morning before treating TSLA as a tape-setter.
- **Scout top pick: NVDA** (next earnings 5/20, ~21 days out, AI-infra tailwind). Conviction **med**. AVGO / PLTR flagged low-med; **GOOGL and MSFT NOT safe to open** without verified earnings dates (historical late-April print risk).
- **Plan for Wed open:** if futures still risk-off at 6 AM CT scan, **pass entirely**. If constructive, enter a **starter ~5% NVDA tranche ($5K)** with the −7% hard stop, and re-run scout tomorrow night.

---

## 2026-04-21 17:00 CT · pre-market (for 4/22)

**First research pass — no high-conviction buy ideas yet; saving cash for a better scan.**

- Fresh paper account confirmed: $100K cash, 0 positions.
- Setup into Wed 4/22: mildly risk-on on Mid-East de-escalation hopes (ES ~+0.35%). TSLA reports AMC 4/22 — biggest tape-setter.
- Scout found no name that cleanly hits ≥2 signals with a verified near-term catalyst. AMZN thesis is real but inside the 3-day earnings window; skipping.
- Next pre-market (6 AM CT 4/22): tighter scan on a seed watchlist (NVDA, AVGO, GOOGL, PLTR, CRWD, PANW) with earnings dates pulled from Alpaca first.

---

(earlier messages below)
