# When Bull wakes up

The stock market keeps New York time. Daylight saving does not move the opening bell, and it must not move Bull either.

Bull's five routines are Claude schedules, not the Astra GitHub Action. The times at the top of each routine file are what gets pasted into that scheduler. Through the summer of 2026 those schedules were stored as a single UTC hour (Central Daylight Time, UTC−5). After the clocks fell back on November 1, Central became UTC−6, and the same UTC hour rang an hour early:

| Routine | Should be | What happened on Wed Nov 4, 2026 |
|---|---|---|
| Pre-market | 6:00 AM Central / 7:00 AM New York | 11:13 UTC = 5:13 AM Central |
| Market open | 8:30 AM Central / 9:30 AM New York | 13:36 UTC = 7:36 AM Central |
| Midday | 12:00 PM Central / 1:00 PM New York | 17:08 UTC = 11:08 AM Central |
| Market close | 3:00 PM Central / 4:00 PM New York | 20:06 UTC = 2:06 PM Central |

Shifting each alarm by one hour would fix this winter and break the schedule again in March. Don't do that.

## The year-round rule

1. Register **both** UTC alarms below. Cloud cron is UTC-only. One hour is summer (New York on daylight time, UTC−4). The other is winter (New York on standard time, UTC−5).
2. Every routine runs `python scripts/market_clock.py --slot <name> --wait` before it trades or writes the close scorecard. The script checks **America/New_York**. If this ring is the early one, it waits until the real New York time. If this ring is the wrong season's extra alarm, it stands down.
3. After New York time says the slot is due, confirm with Alpaca's market clock (`GET /v2/clock`). An open or midday run still needs the market to be open. A close run is not the close while Alpaca says the bell is more than 20 minutes away. A holiday is a no-trade day.
4. Claim the slot (`--claim`) and push that claim before any order, so the summer alarm and the winter alarm cannot both trade.

`scripts/market_clock.py` is the list these crons are generated from. The tests fail if a routine file drifts away from it.

| Slot | New York (year-round) | Central wall clock | Summer UTC cron | Winter UTC cron |
|---|---|---|---|---|
| pre-market | 7:00 AM | 6:00 AM | `0 11 * * 1-5` | `0 12 * * 1-5` |
| market-open | 9:30 AM | 8:30 AM | `30 13 * * 1-5` | `30 14 * * 1-5` |
| midday | 1:00 PM | 12:00 PM | `0 17 * * 1-5` | `0 18 * * 1-5` |
| market-close | 4:00 PM | 3:00 PM | `0 20 * * 1-5` | `0 21 * * 1-5` |
| weekly-review | Friday 5:00 PM | Friday 4:00 PM | `0 21 * * 5` | `0 22 * * 5` |

If the scheduler has a real timezone field, set it to `America/New_York` at the New York wall time **and still keep the script check**. A timezone field that secretly froze UTC−5 is how this broke. The script is the part that cannot freeze.

Astra's own GitHub Action (`.github/workflows/astra.yml`) already uses this two-alarm pattern for its research slots. Bull's trading routines are separate and were not on that workflow.
