---
name: "pe-fees-carry"
description: "Independently recalculate private equity management fees, fee offsets, fund expenses and carried interest against LPA and side-letter terms, quantify variances and draft GP query letters. Use when validating a capital call fee, reviewing quarterly fees, checking GP carry accruals or comparing total cost of ownership across funds."
---

# Fee, carry and expense validation

Use `management_fee()` and `european_waterfall()` in `${CLAUDE_PLUGIN_ROOT}/references/calculations.md` for every calculation.

## Management fee (`/fee-check`)
1. Fee base per fund master for the period: commitment (investment period) or invested capital / NAV (post-period step-down).
2. `management_fee(base, rate, start, end, offsets, discount)` (Actual/365 unless LPA says otherwise).
3. Offsets: transaction, monitoring, director, break-up fees x offset % from LPA.
4. Compare with the fee charged in calls / CAS. Variance > tolerance (P16) -> exception.

## Expenses
Check categories against LPA permitted expenses and caps (organisational costs, broken-deal, legal). Flag items outside scope or over cap.

## Carried interest (`/waterfall-check`)
Replay the waterfall: return of capital -> preferred return -> catch-up -> split. Compare expected carry with the GP's accrued / earned / paid carry in the CAS (ILPA template fields). Report clawback exposure and escrow. The script is a reasonableness check; American (deal-by-deal) waterfalls need per-deal data.

## Subscription line and total cost
Report subscription-line interest and fees; total cost of ownership = fees + expenses + carry as % of commitment and of average NAV; compare across funds.

## MFN and side letters
Check MFN elections and side-letter discounts are applied.

## Query letter (`/fee-query-letter`)
Professional letter to the GP: fund, period, amounts charged, our recalculation, variance, LPA clause reference, request for explanation or credit, response date. Save to `07_Memos`.
