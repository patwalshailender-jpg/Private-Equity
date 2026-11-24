---
name: pe-nav-reporting
description: Produce private equity NAV and performance reporting - commitment, called, unfunded, calls and distributions in period, reported and adjusted NAV, total value, IRR, DPI, RVPI, TVPI, KS-PME, J-curve, concentration and portfolio look-through, watch list, management dashboard. Use for quarterly NAV packs, commitment reports, performance questions or management / board PE reporting.
---

# NAV and performance reporting

All figures come from the cash-flow ledger and NAV history; all calculations run through `${CLAUDE_PLUGIN_ROOT}/scripts/pe_calcs.py` (xirr, multiples, ks_pme, unfunded). Field definitions follow the ILPA Reporting Template.

## Fund schedule (`/nav-pack`)
One row per fund, subtotals by strategy, vintage, currency, GP:
Commitment | Called (split investments / fees / expenses) | % called | Unfunded (= Commitment - Called + Recallable) | Calls in period / YTD | Cumulative distributions (split ROC / gain / income) | Distributions in period / YTD | Reported NAV (with date) | Adjusted NAV | Total value | Net gain | GP accrued carry | Exposure (Adjusted NAV + Unfunded) | Net cash flow in period.

## Performance (`/pe-performance`)
Net IRR (XIRR, adjusted NAV as terminal flow), DPI, RVPI, TVPI, KS-PME vs the chosen public index, gross MOIC as reported by GP; where the GP provides ILPA Performance Template data, also show IRR excluding subscription-line effect. Report by fund, vintage, strategy and total. Show the distribution-source mix (exit / recap / NAV loan / CV) so DPI quality is visible.

## Commitment report (`/commitment-report`)
Commitments, unfunded by fund, expected drawdowns (from `pe-liquidity-tax`), investment period end dates.

## Look-through (`/look-through`)
From GP portfolio schedules: top portfolio companies by our share of NAV, sector, country, currency, overlap of the same company across funds.

## Dashboard and management pack (`/pe-dashboard`, `/pe-mgmt-pack`)
KPIs: total commitment, NAV, unfunded, exposure vs target, quarter net cash flow, TVPI, DPI, IRR, stale NAV count, open breaks, watch list (key-person events, extensions, TVPI < 1.0x after year 4, CV elections pending). Produce Excel for the pack and slides or a doc for management, following house templates.

Every number must tie to the fund schedule; show reporting date and currency on every page.
