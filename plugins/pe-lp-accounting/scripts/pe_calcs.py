#!/usr/bin/env python3
"""
pe_calcs.py - Deterministic calculations for the PE LP Accounting plugin.

All arithmetic used by the plugin's skills runs through this module so that
results are reproducible and auditable. Standard library only.

Functions
---------
xirr(cashflows)                      Net IRR on dated cash flows (LP sign convention)
multiples(paid_in, distributions, nav)  DPI, RVPI, TVPI
ks_pme(contribs, dists, nav, index)  Kaplan-Schoar Public Market Equivalent
unfunded(commitment, called, recallable)  Unfunded commitment
nav_rollforward(...)                 Adjusted NAV at reporting date
management_fee(...)                  Pro-rata management fee
european_waterfall(...)              Whole-of-fund carry check (simplified)

CLI
---
python3 pe_calcs.py performance cashflows.csv --nav 1250000 --nav-date 2026-09-30
python3 pe_calcs.py rollforward --nav 1000000 --calls 50000 --dists 20000 --fx 1.0 --adj 0
python3 pe_calcs.py selftest

Cash-flow CSV columns: date (YYYY-MM-DD), amount
Sign convention (LP view): capital calls negative, distributions positive.
"""
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


# --------------------------------------------------------------------------- #
# CLI
# --------------------------------------------------------------------------- #
def _read_cashflows(path: str) -> list[tuple[date, float]]:
    with open(path, newline="", encoding="utf-8") as fh:
        return [(_d(r["date"]), float(r["amount"])) for r in csv.DictReader(fh)]


def _cmd_performance(a) -> dict:
    flows = _read_cashflows(a.cashflows)
    paid_in = -sum(x for _, x in flows if x < 0)
    dists = sum(x for _, x in flows if x > 0)
    out = multiples(paid_in, dists, a.nav)
    out.update({"paid_in": paid_in, "distributions": dists, "nav": a.nav})
    out["net_irr"] = xirr(flows + [(_d(a.nav_date), a.nav)]) if a.nav or dists else None
    return out


def selftest() -> None:
    # 1) XIRR: -100 at t0, +110 after 365 days -> 10.000%
    r = xirr([("2025-01-01", -100), ("2026-01-01", 110)])
    assert abs(r - 0.10) < 1e-8, r
    # 2) Multiples
    m = multiples(1000, 400, 900)
    assert abs(m["TVPI"] - 1.3) < 1e-12 and abs(m["DPI"] - 0.4) < 1e-12
    # 3) Unfunded
    assert unfunded(10_000_000, 6_500_000, 250_000) == 3_750_000
    # 4) NAV roll-forward
    nr = nav_rollforward(1_000_000, 50_000, 20_000, 1.0, 0)
    assert nr["adjusted_nav_reporting_ccy"] == 1_030_000
    # 5) KS-PME = 1 when fund exactly tracks index
    idx = {"2024-01-01": 100, "2025-01-01": 110, "2026-01-01": 121}
    p = ks_pme([("2024-01-01", 100)], [("2025-01-01", 55)], 60.5, idx, "2026-01-01")
    assert abs(p - 1.0) < 1e-12, p
    # 6) Fee: 10m x 2% x 365/365 = 200k; 10% discount -> 180k; 30k offsets -> 150k
    f = management_fee(10_000_000, 0.02, "2025-01-01", "2026-01-01", 30_000, 0.10)
    assert abs(f["net_fee"] - 150_000) < 1e-6, f
    # 7) Waterfall: 100 in, 200 out, 8% for 1 yr, 20% carry, full catch-up
    w = european_waterfall(100, 200, 1, 0.08, 0.20, 1.0)
    assert abs(w["gp_carry_total"] - 20.0) < 1e-9, w           # 20% of 100 profit
    assert abs(w["lp_total"] + w["gp_carry_total"] - 200) < 1e-9
    # 8) Partial (80%) catch-up: GP still ends at 20% of total profit when ample
    w2 = european_waterfall(100, 200, 1, 0.08, 0.20, 0.80)
    assert abs(w2["gp_carry_total"] - 20.0) < 1e-9, w2
    # 9) Below hurdle: no carry
    w3 = european_waterfall(100, 105, 1, 0.08, 0.20, 1.0)
    assert w3["gp_carry_total"] == 0.0, w3
    print("selftest: all 9 checks passed")


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)

    pp = sub.add_parser("performance", help="IRR, DPI, RVPI, TVPI from a cash-flow CSV")
    pp.add_argument("cashflows"); pp.add_argument("--nav", type=float, default=0.0)
    pp.add_argument("--nav-date", required=True)

    pr = sub.add_parser("rollforward", help="Adjusted NAV")
    pr.add_argument("--nav", type=float, required=True)
    pr.add_argument("--calls", type=float, default=0.0)
    pr.add_argument("--dists", type=float, default=0.0)
    pr.add_argument("--fx", type=float, default=1.0)
    pr.add_argument("--adj", type=float, default=0.0)

    pf = sub.add_parser("fee", help="Management fee recalculation")
    pf.add_argument("--base", type=float, required=True)
    pf.add_argument("--rate", type=float, required=True)
    pf.add_argument("--start", required=True); pf.add_argument("--end", required=True)
    pf.add_argument("--offsets", type=float, default=0.0)
    pf.add_argument("--discount", type=float, default=0.0)

    pw = sub.add_parser("waterfall", help="European waterfall carry check")
    pw.add_argument("--contributed", type=float, required=True)
    pw.add_argument("--distributable", type=float, required=True)
    pw.add_argument("--years", type=float, required=True)
    pw.add_argument("--hurdle", type=float, default=0.08)
    pw.add_argument("--carry", type=float, default=0.20)
    pw.add_argument("--catch-up", type=float, default=1.0)

    sub.add_parser("selftest", help="Run built-in checks")

    a = p.parse_args(argv)
    if a.cmd == "selftest":
        selftest(); return 0
    if a.cmd == "performance":
        out = _cmd_performance(a)
    elif a.cmd == "rollforward":
        out = nav_rollforward(a.nav, a.calls, a.dists, a.fx, a.adj)
    elif a.cmd == "fee":
        out = management_fee(a.base, a.rate, a.start, a.end, a.offsets, a.discount)
    else:
        out = european_waterfall(a.contributed, a.distributable, a.years, a.hurdle, a.carry, a.catch_up)
    print(json.dumps(out, indent=2, default=str))
    return 0


if __name__ == "__main__":
    sys.exit(main())
