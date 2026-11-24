"""Run: python3 -m unittest discover -s plugins/pe-lp-accounting/tests"""
import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
import pe_calcs as pc  # noqa: E402


class TestPeCalcs(unittest.TestCase):
    def test_selftest(self):
        pc.selftest()

    def test_xirr_zero_npv(self):
        flows = [("2022-03-31", -4_000_000), ("2023-06-30", -3_000_000),
                 ("2024-12-31", 1_500_000), ("2025-09-30", 2_000_000),
                 ("2026-09-30", 5_200_000)]
        r = pc.xirr(flows)
        self.assertAlmostEqual(pc._npv(r, sorted((pc._d(d), a) for d, a in flows)), 0.0, places=4)

    def test_xirr_needs_both_signs(self):
        with self.assertRaises(ValueError):
            pc.xirr([("2025-01-01", -100), ("2026-01-01", -10)])

    def test_rollforward_fx(self):
        out = pc.nav_rollforward(100.0, 10.0, 5.0, 2.0, 1.0)
        self.assertEqual(out["adjusted_nav_fund_ccy"], 105.0)
        self.assertEqual(out["adjusted_nav_reporting_ccy"], 211.0)

    def test_waterfall_conserves_cash(self):
        for dist in (50, 100, 105, 110, 150, 400):
            w = pc.european_waterfall(100, dist, 2, 0.08, 0.20, 1.0)
            self.assertAlmostEqual(w["lp_total"] + w["gp_carry_total"], dist, places=9)


if __name__ == "__main__":
    unittest.main()
