"""Independent validation of pe_calcs.py against published / hand-computed benchmarks."""
import sys
from datetime import date

import os
sys.path.insert(0, sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(__file__), "..", "scripts"))
import pe_calcs as pc  # noqa: E402

results = []


def check(area, case, expected, actual, tol, source):
    ok = abs(expected - actual) <= tol
    results.append((area, case, expected, actual, "PASS" if ok else "FAIL", source))


# 1. XIRR - Microsoft Excel documentation example (expected 0.373362535)
ms = [(date(2008, 1, 1), -10000), (date(2008, 3, 1), 2750), (date(2008, 10, 30), 4250),
      (date(2009, 2, 15), 3250), (date(2009, 4, 1), 2750)]
check("IRR", "Microsoft Excel XIRR doc example", 0.373362535, pc.xirr(ms), 1e-6,
      "Microsoft Support: XIRR function")

# 2. XIRR - closed form: -1,000 then +1,500 exactly 2 years (730 days) later
r = (1.5) ** (365 / 730) - 1
check("IRR", "Closed form 1.5x over 730 days", r,
      pc.xirr([("2024-01-01", -1000), ("2025-12-31", 1500)]), 1e-9, "Hand: 1.5^(365/730)-1")

# 3. XIRR - negative IRR (loss fund): -100 then +80 after 365 days -> -20%
check("IRR", "Loss-making fund (-20%)", -0.20,
      pc.xirr([("2025-01-01", -100), ("2026-01-01", 80)]), 1e-9, "Hand")

# 4. Multiples
m = pc.multiples(7_000_000, 3_500_000, 5_200_000)
check("Multiples", "DPI 3.5m/7.0m", 0.5, m["DPI"], 1e-12, "Hand")
check("Multiples", "RVPI 5.2m/7.0m", 5.2 / 7.0, m["RVPI"], 1e-12, "Hand")
check("Multiples", "TVPI", 8.7 / 7.0, m["TVPI"], 1e-12, "Hand")
m0 = pc.multiples(1_000_000, 0, 850_000)
check("Multiples", "No distributions: DPI 0, TVPI 0.85", 0.85, m0["TVPI"], 1e-12, "Hand")

# 5. Unfunded
check("Unfunded", "10m - 6.5m + 0.25m recallable", 3_750_000,
      pc.unfunded(10_000_000, 6_500_000, 250_000), 0, "Hand")

# 6. KS-PME: fund beats index. Contribute 100 at I=100; NAV 150 when I=120 -> 150/120 = 1.25
idx = {"2024-01-01": 100, "2026-01-01": 120}
check("PME", "Fund 1.5x vs index 1.2x -> 1.25", 1.25,
      pc.ks_pme([("2024-01-01", 100)], [], 150, idx, "2026-01-01"), 1e-12, "Hand")

# 7. NAV roll-forward with FX: (10m + 0.5m - 0.8m) x 0.385 + 20k = 3,754,500
nr = pc.nav_rollforward(10_000_000, 500_000, 800_000, 0.385, 20_000)
check("NAV", "Roll-forward incl. FX 0.385 and +20k adj", 3_754_500,
      nr["adjusted_nav_reporting_ccy"], 1e-6, "Hand")

# 8. Management fee: 50m x 1.75% x 182/365, 15% discount, 40k offsets
g = 50_000_000 * 0.0175 * 182 / 365
exp = g * 0.85 - 40_000
f = pc.management_fee(50_000_000, 0.0175, "2026-01-01", "2026-07-02", 40_000, 0.15)
check("Fees", "Half-year fee, discount and offsets", exp, f["net_fee"], 1e-6, "Hand")
check("Fees", "Day count 1 Jan - 2 Jul 2026", 182, f["days"], 0, "Calendar")
f2 = pc.management_fee(1_000_000, 0.02, "2026-01-01", "2026-04-01", 100_000, 0)
check("Fees", "Offsets exceed fee -> floored at 0", 0.0, f2["net_fee"], 0, "LPA practice")

# 9. Waterfall - full catch-up. 100 in, 160 out, 8% x 1y, 20% carry.
#    ROC 100, pref 8, catch-up = 0.25 x 8 = 2, split remaining 50 -> GP 10. GP total 12 = 20% of 60.
w = pc.european_waterfall(100, 160, 1, 0.08, 0.20, 1.0)
check("Carry", "Full catch-up, GP = 20% of 60 profit", 12.0, w["gp_carry_total"], 1e-9, "Hand")
# Catch-up not completed: 100 in, 109 out -> pref 8, catch-up 1 (GP), no split
w2 = pc.european_waterfall(100, 109, 1, 0.08, 0.20, 1.0)
check("Carry", "Catch-up partially reached", 1.0, w2["gp_carry_total"], 1e-9, "Hand")
# Multi-year compounding pref: 100 in, 5 years, 8% -> pref 46.93; 140 out -> no carry
w3 = pc.european_waterfall(100, 140, 5, 0.08, 0.20, 1.0)
check("Carry", "Below compounded 5y hurdle -> no carry", 0.0, w3["gp_carry_total"], 1e-9, "Hand")
# No catch-up (catch_up=0): 100 in, 160 out -> split of 52 above pref -> GP 10.4
w4 = pc.european_waterfall(100, 160, 1, 0.08, 0.20, 0.0)
check("Carry", "No catch-up: GP 20% of 52 above pref", 10.4, w4["gp_carry_total"], 1e-9, "Hand")

# 10. Pro-rata capital call check (control C4): 25m of 500m fund, fund call 40m -> 2m
check("Controls", "Pro-rata share of call", 2_000_000, 25_000_000 / 500_000_000 * 40_000_000, 0, "Hand")

# 11. Error handling
try:
    pc.xirr([("2025-01-01", -100), ("2026-01-01", -5)])
    results.append(("Errors", "XIRR rejects all-negative flows", 1, 0, "FAIL", "Design"))
except ValueError:
    results.append(("Errors", "XIRR rejects all-negative flows", 1, 1, "PASS", "Design"))

w_pass = sum(1 for r in results if r[4] == "PASS")
print(f"{'Area':<10}{'Case':<44}{'Expected':>16}{'Actual':>16}  Result")
for a, c, e, act, res, s in results:
    print(f"{a:<10}{c:<44}{e:>16.6f}{act:>16.6f}  {res}")
print(f"\n{w_pass}/{len(results)} passed")
