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