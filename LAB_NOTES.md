# Lab Notes — Claude Trading Agent Audit

## 2026-10-29 — Setup
- Public repo; raw data stays in private/ (gitignored), copied from the
  private trading-research repo
- src/sanitize.py: allow-list of 13 columns; drops size_usd, reason_text,
  cited, market, id, source, trigger
- Timestamps converted via UTC back to America/New_York (first version
  shifted times +4h; fixed)
- 115 decision records, Oct 7–23 (prompt v1–v5); v6 not yet extracted
- Actions: 59 PASS, 29 HOLD, 17 WAIT, 6 TOOK, 3 EXIT, 1 ADD → taken-trade
  results will be anecdotal

## 2026-10-30 — Sanitizer fixes
- Removed stray space in time format ("12: 46" → "12:46")
- Rounded stated_rr to 2 decimals to remove floating-point artifacts
  (e.g. 0.7000000000000001 → 0.7)
- Removed a stray "" in the KEEP list (harmless by accident: Python joins
  adjacent strings, but it would break if a comma were added)

## 2026-11-04 — Data refresh
- Pulled trading-research: 213 decisions, Oct 7–30
  (v1 29, v2 44, v3 9, v4 5, v5 64, v6 62)
- Fixed time zone name capitalization ("America/New_York"); matters now
  that DST ended Nov 1 (offsets change -04:00 → -05:00)
- Prompt v7 went live Nov 2 (entry timing + stop management rules);
  runs moved to 9:45 / 11:45 / 13:45 ET after DST. v7 decisions not
  yet in the extracted data.
- Checked output: times correct, private/ not tracked by git