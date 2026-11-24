---
name: "pe-secondaries"
description: "Handle secondary transactions and changes to LP interests - pricing a secondary sale or purchase versus NAV, derecognition and purchase accounting, transfers of LP interests with GP consent, and LP default handling. Use when buying or selling fund interests, transferring commitments, or when a capital call default occurs."
---

# Secondaries, transfers and defaults

## Pricing (`/secondary-pricing`)
For each interest: reference NAV and date, roll-forward to pricing date (`pe-valuation`), bid as % of NAV, implied discount / premium, unfunded commitment transferred, deferred payment terms (present value), effect on portfolio DPI, IRR and exposure. Compare with market discount ranges the user provides.

## Accounting (`/secondary-accounting`)
- Sale: derecognise carrying amount; gain / loss = consideration (PV of deferred) - carrying amount (J16). Remove unfunded commitment from registers from the effective date.
- Purchase: initial recognition at transaction price (J17); remeasure to fair value at the next reporting date; any day-one difference follows IFRS 9 / IFRS 13 guidance - document in a memo.

## LP transfer (`/lp-transfer`)
Checklist: GP consent, transfer agreement, effective date, purchase price, allocation of calls / distributions between signing and closing, transfer of unfunded commitment, updated fund master and registers, notices to administrator, tax forms.

## Defaults
If a call cannot be met by the due date: cure period, penalty interest (J18), LPA remedies (forced sale, forfeiture, reduced commitment). Draft notice to the GP and escalate to the Financial Controller immediately.
