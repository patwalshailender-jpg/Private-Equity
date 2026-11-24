---
name: pe-valuation
description: Determine fair value of private equity fund interests under IFRS 13 - capture GP capital account and NAV statements, roll lagged NAV forward to the reporting date, assess GP valuation quality against IPEV Guidelines, classify Level 3, back-test, and write the quarterly valuation memo. Use at each reporting date or when a new NAV statement arrives.
---

# Valuation and NAV roll-forward

Policy: P7 in `${CLAUDE_PLUGIN_ROOT}/references/policies.md`. NAV is a starting point; IFRS has no NAV practical expedient, so the memo must explain why the adjusted NAV represents fair value.

## Roll-forward (`/nav-rollforward`)
Adjusted NAV = (GP NAV at last report date + calls after - distributions after) x closing FX + market / known-event adjustments.
Run `python3 ${CLAUDE_PLUGIN_ROOT}/scripts/pe_calcs.py rollforward --nav <> --calls <> --dists <> --fx <> --adj <>`.

Steps per fund:
1. Record GP report date; flag if older than one quarter (P16, C6).
2. Sum calls and distributions dated after the GP report date up to our reporting date.
3. Apply closing FX at our reporting date (P9).
4. Market adjustment only if policy permits and the lag covers a material move; state the proxy index and calculation.
5. Known events: signed exits, write-downs, impairments announced after the GP date.
6. Result vs carrying amount -> J11 / J12 via `pe-fund-accounting`.

## GP valuation quality review
Check: methodology stated and consistent with IPEV; changes in valuation policy; auditor opinion on last fund FS (unmodified?); large unexplained uplifts; valuation of top 5 holdings; use of NAV facilities or subscription lines; secondary market evidence (bids or trades at discount / premium to NAV).

## Hierarchy
Fund interests: Level 3. Record significant unobservable inputs (reported NAV, adjustments, discount) for IFRS 13.93 disclosure.

## Back-test (`/nav-backtest`)
Compare last quarter's adjusted NAV with the GP NAV later reported for the same date. Report the % difference per fund and portfolio; persistent bias -> revisit adjustment policy.

## Valuation memo (`/valuation-memo`)
Sections: scope and date; policy applied; table per fund (GP NAV, date, roll-forward items, FX, adjustments, adjusted NAV, carrying amount, movement); GP quality findings; stale NAV list; back-test result; Level 3 inputs; conclusion; preparer / reviewer. Save to `07_Memos`.
