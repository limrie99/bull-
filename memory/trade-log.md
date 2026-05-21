# Trade Log

**Append-only. Never edit past entries.** Each entry is a single trade (buy or sell leg).

Format:

```
## YYYY-MM-DD HH:MM CT | BUY|SELL | SYMBOL | qty @ price | order_id
Thesis: one sentence
Signals matched: [list from strategy.md buy signals, or sell signal number]
Stop set: $price (or N/A for sells)
Research reference: link or date of research-log entry
Notes: anything unusual about the fill or context
```

---

## 2026-04-22 10:07 CT | BUY | NVDA | 25 @ 201.38 | 2b923034-96f2-4166-8d53-10b5b9a967b8
Thesis: AI-infra leader, clean earnings runway (next print 5/20 AMC); enter starter tranche per 4/21 pre-market plan.
Signals matched: (3) secular AI-infra tailwind (Blackwell ramp).
Stop set: intended −7% = ~$187.28 hard stop; bracket sell legs (expired/canceled — see below).
Research reference: 2026-04-21 19:00 CT pre-market re-run.
Notes: **Backfilled 2026-05-21 from Alpaca audit.** Routine logs marked halted on 4/22 (env vars missing), but the buy did fill via Alpaca at 10:07 CT (~$5,034.50 = ~5% of portfolio). Bracket sell legs ID 974cc142… expired same day and a3057559… was canceled 4/23 — net effect was NVDA held bare without a working stop until manual close. Process failure: must not place buys when stop placement isn't verified to be live. Action item recorded in 2026-05-21 research-log.

## 2026-05-04 10:21 CT | SELL | NVDA | 25 @ 195.0184 | d42471e7-5c13-45b4-a365-6117602b1eac
Thesis: Close the unprotected NVDA starter; better to flatten and re-scout than carry naked risk into 5/20 earnings.
Signals matched: Sell signal 1 effectively (−3.16% from entry; sold below entry but well above −7% hard stop level).
Stop set: N/A (sell leg).
Research reference: (no contemporaneous research-log entry — see 2026-05-21 backfill note).
Notes: **Backfilled 2026-05-21 from Alpaca audit.** Realized loss −$159.04. Fill is the source of the $99,840.95 equity figure visible today. NVDA was held ~12 days; sold ~16 days before its 5/20 earnings print — outside the 3-day blackout but motivated by lack of working stop rather than thesis change.
