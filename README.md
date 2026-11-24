# PE Plugins marketplace

A Claude plugin marketplace containing **pe-lp-accounting**: end-to-end investor-side private equity accounting, reporting and IFRS compliance.

> **Disclaimer:** This plugin provides professional support for qualified finance teams. It is not accounting, audit, tax, legal or investment advice. All outputs, including figures, journal entries and IFRS disclosures, must be reviewed and approved by a qualified accountant before use. IFRS references should be confirmed against the current standards at https://www.ifrs.org.


![version](https://img.shields.io/badge/version-1.0.4-blue) ![checks](https://img.shields.io/badge/validation-33%2F33%20passed-brightgreen) ![IFRS](https://img.shields.io/badge/IFRS-reviewed%20Nov%202026-informational)

## Validation checks

**Last validated:** 24 November 2026 · **Version:** 1.0.4 · **Result:** 33 of 33 automated checks passed · [Full report](plugins/pe-lp-accounting/VALIDATION.md)

| Test suite | Checks | Result |
|---|---|---|
| Independent benchmarks (`tools/tests/validate_benchmarks.py`) | 19 | ✅ 19 passed |
| Built-in self-test (`tools/scripts/pe_calcs.py selftest`) | 9 | ✅ 9 passed |
| Unit tests (`tools/tests/test_pe_calcs.py`) | 5 | ✅ 5 passed |
| **Total** | **33** | **✅ 33 passed** |

| Area | What was tested | Result |
|---|---|---|
| IRR | Microsoft Excel XIRR documentation example (37.3363%), closed-form 2-year case, loss-making fund (-20%) | ✅ Exact match |
| DPI / RVPI / TVPI | Sample fund; fund with no distributions | ✅ Exact match |
| PME (Kaplan-Schoar) | Fund 1.5x vs index 1.2x = 1.25 | ✅ Exact match |
| NAV roll-forward | Cash flows after GP report date, FX 0.385, manual adjustment | ✅ Exact match |
| Management fee | Actual/365 day count, side-letter discount, offsets floored at zero | ✅ Exact match |
| Carried interest | Full catch-up, partial catch-up, compounded 5-year hurdle, no catch-up | ✅ Exact match |
| Controls | Pro-rata call share; rejection of invalid cash flows | ✅ Working |
| Sample fund (end to end) | DPI 0.50x, RVPI 0.74x, TVPI 1.24x, net IRR 6.54% | ✅ Exact match |

| IFRS reference review | Finding |
|---|---|
| IFRS 9 4.1.4 / IAS 32.16A (FVOCI not available for fund units) | ✅ Confirmed: IFRS Interpretations Committee agenda decision, Sept 2017 |
| IFRS 12.24-31 (maximum exposure to loss) | ✅ Confirmed |
| IAS 28.18-19 (fair value option) | 🔄 Updated in v1.0.1 for the IASB amendments of 26 June 2026 and the IFRS 18 transition election |

**Limitations:** the European waterfall is a single-contribution-date reasonableness check; accounting policy defaults require approval by your technical accounting function; extraction from real LPAs and GP notices should be validated on live documents. Outputs are professional support only, not accounting, audit, tax or investment advice.

**Re-run the checks:**

```bash
python3 tools/tests/validate_benchmarks.py
python3 tools/scripts/pe_calcs.py selftest
python3 -m unittest discover -s tools/tests -v
```

## Repository layout

```
.claude-plugin/marketplace.json        Marketplace catalogue
plugins/pe-lp-accounting/
  .claude-plugin/plugin.json           Plugin manifest
  skills/<12 skills>/SKILL.md
  commands/<43 commands>.md
  references/                          Policies, journals, taxonomy, controls
  scripts/pe_calcs.py                  Calculations
  templates/                           CSV schemas
  tests/                               Unit tests
```

## Publish on GitHub

```bash
git init
git add .
git commit -m "PE LP accounting plugin v1.0.0"
git branch -M main
git remote add origin https://github.com/<your-org>/<repo-name>.git
git push -u origin main
```

A private repository works for your organisation as long as users have access to it.

## Install in Claude Code

```
/plugin marketplace add <your-org>/<repo-name>
/plugin install pe-lp-accounting@pe-plugins
```

## Install in the Claude app (organisation)

An organisation owner can add the GitHub repository as a plugin marketplace in the organisation's plugin settings and enable `pe-lp-accounting` for members. Alternatively, upload the plugin folder as a zip where your plan supports custom plugin uploads.

## Update

Bump `version` in both `marketplace.json` and `plugin.json`, push, then run `/plugin marketplace update pe-plugins`.

## Test

```bash
python3 -m unittest discover -s tools/tests -v
```

## Licence

MIT. See [LICENSE](LICENSE). Copyright (c) 2026 patwalshailender-jpg.

## Privacy

The plugin stores and transmits no data. See [PRIVACY.md](PRIVACY.md).
