# Validation report: pe-lp-accounting v1.0.1

**Date:** 24 November 2026
**Code version tested:** commit `e1fd30e` (v1.0.1)
**Result:** all 33 automated checks passed (19 benchmark tests, 9 built-in self-tests, 5 unit tests); one IFRS reference updated.

## 1. Summary

| Test suite | File | Checks | Result |
|---|---|---|---|
| Independent benchmarks | `tools/tests/validate_benchmarks.py` | 19 | 19 passed |
| Built-in self-test | `references/calculations.md selftest` | 9 | 9 passed |
| Unit tests | `tools/tests/test_pe_calcs.py` | 5 | 5 passed |
| **Total** | | **33** | **33 passed** |

## 2. Benchmark results

| Area | Case | Expected | Actual | Result | Benchmark source |
|---|---|---|---|---|---|
| IRR | Microsoft Excel XIRR documentation example | 37.3363% | 37.3363% | PASS | Microsoft Support: XIRR function |
| IRR | 1.5x over 730 days (closed form) | 22.4745% | 22.4745% | PASS | 1.5^(365/730) - 1 |
| IRR | Loss-making fund | -20.0000% | -20.0000% | PASS | Hand calculation |
| Multiples | DPI 3.5m / 7.0m | 0.5000x | 0.5000x | PASS | Hand calculation |
| Multiples | RVPI 5.2m / 7.0m | 0.7429x | 0.7429x | PASS | Hand calculation |
| Multiples | TVPI | 1.2429x | 1.2429x | PASS | Hand calculation |
| Multiples | No distributions: TVPI | 0.8500x | 0.8500x | PASS | Hand calculation |
| Unfunded | 10m - 6.5m + 0.25m recallable | 3,750,000 | 3,750,000 | PASS | Hand calculation |
| PME | Fund 1.5x vs index 1.2x | 1.2500 | 1.2500 | PASS | Kaplan-Schoar formula |
| NAV | Roll-forward with FX 0.385 and +20,000 adjustment | 3,754,500 | 3,754,500 | PASS | Hand calculation |
| Fees | 50m x 1.75% x 182/365, 15% discount, 40,000 offsets | 330,856.16 | 330,856.16 | PASS | Hand calculation |
| Fees | Day count 1 Jan - 2 Jul 2026 | 182 | 182 | PASS | Calendar |
| Fees | Offsets exceed fee, floored at zero | 0 | 0 | PASS | LPA practice |
| Carry | Full catch-up: GP = 20% of 60 profit | 12.00 | 12.00 | PASS | Hand calculation |
| Carry | Catch-up partially reached | 1.00 | 1.00 | PASS | Hand calculation |
| Carry | Below 5-year compounded 8% hurdle | 0.00 | 0.00 | PASS | Hand calculation |
| Carry | No catch-up: 20% of 52 above preferred return | 10.40 | 10.40 | PASS | Hand calculation |
| Controls | Pro-rata share: 25m of 500m fund, 40m call | 2,000,000 | 2,000,000 | PASS | Hand calculation |
| Errors | XIRR rejects all-negative cash flows | Error raised | Error raised | PASS | Design |

## 3. Sample fund (end-to-end test)

Source: `tools/tests/sample_cashflows.csv`, adjusted NAV 5,200,000 at 30 September 2026.

| Measure | Result |
|---|---|
| Paid-in | 7,000,000 |
| Distributions | 3,500,000 |
| DPI | 0.50x |
| RVPI | 0.74x |
| TVPI | 1.24x |
| Net IRR | 6.54% |

## 4. IFRS reference review

| Policy | Reference | Finding | Action |
|---|---|---|---|
| P1 | IFRS 9 4.1.4; BC5.21 | Confirmed: puttable instruments classified as equity under IAS 32.16A-16D are not eligible for the FVOCI presentation election (IFRS Interpretations Committee agenda decision, September 2017) | Agenda decision added as reference |
| P13 | IFRS 12.24-31 | Confirmed: disclosure of the amount that best represents maximum exposure to loss from unconsolidated structured entities | No change |
| P12 | IAS 28.18-19 | Updated: IASB amendments issued 26 June 2026 extend the fair value option to entities with a specified main business activity of investing in assets (IFRS 18.49(a)), with a one-time election on IFRS 18 transition | Policy and IFRS skill updated in v1.0.1 |

## 5. Limitations

- The European waterfall is a reasonableness check with a single contribution date; dated multi-flow and American (deal-by-deal) waterfalls need fund-level modelling.
- Accounting policy defaults reflect common industry practice and should be approved by the user's technical accounting function.
- Document extraction from real LPAs and GP notices is not covered by automated tests; validate on live documents before relying on outputs.
- Outputs are professional support only, not accounting, audit, tax or investment advice.

## 6. How to re-run

```bash
python3 tools/tests/validate_benchmarks.py
python3 plugins/pe-lp-accounting/references/calculations.md selftest
python3 -m unittest discover -s tools/tests -v
```
