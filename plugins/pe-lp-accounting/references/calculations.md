# Calculation reference

All arithmetic in this plugin must be computed, never estimated. Run the functions below in Python (code execution or analysis tool), or reproduce them with spreadsheet formulas, and cross-check before reporting.

| Function | Use | Spreadsheet equivalent |
|---|---|---|
| `xirr(cashflows)` | Net IRR on dated flows (calls negative, distributions and terminal NAV positive) | `=XIRR(values, dates)` |
| `multiples(paid_in, distributions, nav)` | DPI, RVPI, TVPI | `=dist/paid_in`, `=nav/paid_in` |
| `ks_pme(contribs, dists, nav, index_levels, valuation_date)` | Kaplan-Schoar PME | FV each flow at index ratio |
| `unfunded(commitment, called, recallable)` | Unfunded commitment | `=commitment-called+recallable` |
| `nav_rollforward(reported_nav, calls_after, dists_after, fx_rate, adjustments)` | Adjusted NAV at reporting date | `=(nav+calls-dists)*fx+adj` |
| `management_fee(base, annual_rate, start, end, offsets, discount_rate)` | Pro-rata fee, Actual/365 | `=base*rate*days/365*(1-disc)-offsets` |
| `european_waterfall(contributed, total_distributable, years, hurdle, carry, catch_up)` | Carry reasonableness check | Tiered waterfall |

Validated: 33 of 33 checks passed, including Microsoft's published Excel XIRR example (37.3363%). Full test suite and the command-line version are in the repository's `tools/` folder.

## Benchmark to confirm before use

`xirr([("2008-01-01", -10000), ("2008-03-01", 2750), ("2008-10-30", 4250), ("2009-02-15", 3250), ("2009-04-01", 2750)])` must return `0.373362535`.

## Code

```python
from __future__ import annotations

import argparse
import csv
import json
import sys
from datetime import date
from typing import Iterable, Sequence

DAYS_IN_YEAR = 365.0


# --------------------------------------------------------------------------- #
# Helpers
# --------------------------------------------------------------------------- #
def _d(x) -> date:
    return x if isinstance(x, date) else date.fromisoformat(str(x))


def _npv(rate: float, flows: Sequence[tuple[date, float]]) -> float:
    t0 = flows[0][0]
    return sum(a / (1.0 + rate) ** ((d - t0).days / DAYS_IN_YEAR) for d, a in flows)


def _dnpv(rate: float, flows: Sequence[tuple[date, float]]) -> float:
    t0 = flows[0][0]
    total = 0.0
    for d, a in flows:
        t = (d - t0).days / DAYS_IN_YEAR
        total += -t * a / (1.0 + rate) ** (t + 1.0)
    return total


# --------------------------------------------------------------------------- #
# Performance
# --------------------------------------------------------------------------- #
def xirr(cashflows: Iterable[tuple], tol: float = 1e-10, max_iter: int = 200) -> float:
    """Annualised IRR (Actual/365) for irregular dated cash flows.

    cashflows: iterable of (date, amount). Needs at least one negative and one
    positive amount. Uses Newton-Raphson with a bisection fallback.
    """
    flows = sorted(((_d(d), float(a)) for d, a in cashflows), key=lambda x: x[0])
    if not flows or not any(a < 0 for _, a in flows) or not any(a > 0 for _, a in flows):
        raise ValueError("xirr needs at least one negative and one positive cash flow")

    rate = 0.10
    for _ in range(max_iter):
        f = _npv(rate, flows)
        df = _dnpv(rate, flows)
        if df == 0:
            break
        new = rate - f / df
        if new <= -0.999999:
            break
        if abs(new - rate) < tol:
            return new
        rate = new

    # Bisection fallback
    lo, hi = -0.9999, 10.0
    f_lo, f_hi = _npv(lo, flows), _npv(hi, flows)
    if f_lo * f_hi > 0:
        raise ValueError("xirr did not converge: no sign change in range")
    for _ in range(1000):
        mid = (lo + hi) / 2.0
        f_mid = _npv(mid, flows)
        if abs(f_mid) < tol or (hi - lo) / 2.0 < tol:
            return mid
        if f_lo * f_mid < 0:
            hi, f_hi = mid, f_mid
        else:
            lo, f_lo = mid, f_mid
    return (lo + hi) / 2.0


def multiples(paid_in: float, distributions: float, nav: float) -> dict:
    """DPI, RVPI, TVPI. paid_in and distributions as positive totals."""
    if paid_in <= 0:
        raise ValueError("paid_in must be positive")
    dpi = distributions / paid_in
    rvpi = nav / paid_in
    return {"DPI": dpi, "RVPI": rvpi, "TVPI": dpi + rvpi}


def ks_pme(contributions: Sequence[tuple], distributions: Sequence[tuple],
           nav: float, index_levels: dict, valuation_date) -> float:
    """Kaplan-Schoar PME.

    contributions / distributions: (date, positive amount)
    index_levels: {date: index level} must include every cash-flow date and the
    valuation date. Each flow is compounded to the valuation date at the index
    return: FV = amount * I(valuation) / I(flow date).
    """
    vd = _d(valuation_date)
    lv = {_d(k): float(v) for k, v in index_levels.items()}
    i_end = lv[vd]
    fv_c = sum(a * i_end / lv[_d(d)] for d, a in contributions)
    fv_d = sum(a * i_end / lv[_d(d)] for d, a in distributions)
    if fv_c == 0:
        raise ValueError("no contributions")
    return (fv_d + nav) / fv_c


def unfunded(commitment: float, called: float, recallable: float = 0.0) -> float:
    """Unfunded commitment = Commitment - Called + Recallable distributions."""
    return commitment - called + recallable


# --------------------------------------------------------------------------- #
# Valuation
# --------------------------------------------------------------------------- #
def nav_rollforward(reported_nav: float, calls_after: float, dists_after: float,
                    fx_rate: float = 1.0, adjustments: float = 0.0) -> dict:
    """Adjusted NAV = (Reported NAV + calls - distributions) x FX + adjustments.

    Amounts before fx are in fund currency; adjustments in reporting currency.
    """
    fund_ccy = reported_nav + calls_after - dists_after
    reporting = fund_ccy * fx_rate + adjustments
    return {"adjusted_nav_fund_ccy": fund_ccy, "adjusted_nav_reporting_ccy": reporting}


# --------------------------------------------------------------------------- #
# Fees and carry
# --------------------------------------------------------------------------- #
def management_fee(base: float, annual_rate: float, start, end,
                   offsets: float = 0.0, discount_rate: float = 0.0) -> dict:
    """Pro-rata fee on Actual/365: base x rate x days/365, less side-letter
    discount and fee offsets (floored at zero)."""
    days = (_d(end) - _d(start)).days
    gross = base * annual_rate * days / DAYS_IN_YEAR
    after_discount = gross * (1.0 - discount_rate)
    net = max(after_discount - offsets, 0.0)
    return {"days": days, "gross_fee": gross, "after_discount": after_discount, "net_fee": net}


def european_waterfall(contributed: float, total_distributable: float, years: float,
                       hurdle: float = 0.08, carry: float = 0.20,
                       catch_up: float = 1.0) -> dict:
    """Simplified whole-of-fund (European) waterfall for a carry reasonableness
    check. Preferred return compounded annually on contributed capital over
    `years`. catch_up = GP share during catch-up (1.0 = full catch-up).
    Not a substitute for the LPA's exact mechanics (timing of each flow).
    """
    remaining = total_distributable
    roc = min(remaining, contributed); remaining -= roc
    pref_due = contributed * ((1.0 + hurdle) ** years - 1.0)
    pref = min(remaining, pref_due); remaining -= pref

    # Catch-up tier: amount x flows; GP takes catch_up * x, LP the rest, until
    # GP has received carry% of all profit distributed so far:
    #   catch_up * x = carry * (pref + x)  ->  x = carry * pref / (catch_up - carry)
    gp_catch = lp_catch = 0.0
    if remaining > 0 and catch_up > carry:
        x_needed = carry * pref / (catch_up - carry)
        x = min(remaining, x_needed)
        gp_catch = catch_up * x
        lp_catch = x - gp_catch
        remaining -= x

    split_gp = remaining * carry
    split_lp = remaining - split_gp
    lp_total = roc + pref + lp_catch + split_lp
    gp_total = gp_catch + split_gp
    return {
        "return_of_capital": roc, "preferred_return": pref,
        "gp_catch_up": gp_catch, "lp_catch_up": lp_catch,
        "lp_split": split_lp, "gp_split": split_gp,
        "lp_total": lp_total, "gp_carry_total": gp_total,
    }
```
