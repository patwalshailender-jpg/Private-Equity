---
name: "pe-liquidity-tax"
description: "Private equity liquidity and planning - cash-flow forecast of calls and distributions (Takahashi-Alexander), commitment pacing, allocation monitoring, liquidity coverage, annual PE budget, FX exposure and withholding tax reclaim tracking. Use for treasury planning, budgets, pacing plans, allocation reviews or WHT reclaims."
---

# Liquidity, pacing, FX and tax

## Cash forecast (`/cash-forecast`)
Takahashi-Alexander model per fund:
- Calls_t = RC_t x Unfunded_{t-1}, with rate of contribution RC by fund age (default yr1 25%, yr2 33.3%, yr3+ 50% of remaining unfunded).
- Distributions_t = RD_t x NAV_{t-1} x (1 + G), RD_t = (age / life)^B, defaults G = 8% growth, B = 2.5, life = 12 years.
- NAV_t = NAV_{t-1} x (1 + G) + Calls_t - Distributions_t.
State parameters, calibrate to strategy and actual history, run in Python. Provide base and stress cases (calls +25% faster, distributions -50%). Show monthly 12-month and annual 3-5 year views and net cash flow.

## Pacing (`/pacing-model`)
New commitments per year needed to reach and hold target PE allocation (NAV and NAV + unfunded), by strategy and vintage, using the forecast model and total portfolio growth assumption.

## Allocation and liquidity coverage
Exposure vs target and ranges; liquidity coverage = liquid assets available / next-12-month expected calls. Alert when outside limits.

## Budget (`/pe-budget`)
Annual budget and forecast of PE NAV, fair value gains, calls, distributions, fees for the entity budget, reconciled to the forecast model.

## FX (`/fx-exposure`)
Exposure by currency (NAV and unfunded), hedging status, sensitivity of NAV to +/-10% FX.

## Withholding tax (`/wht-tracker`)
For each income distribution: WHT deducted vs treaty rate, excess reclaimable, reclaim filed date, time-bar date, status. Track tax packs and residency certificates. Flag reclaims within 90 days of time bar.
