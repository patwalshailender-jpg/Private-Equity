---
description: Back-test prior adjusted NAV against later GP NAV
argument-hint: <reporting date>
---

Use the `pe-valuation` skill from this plugin. Report % differences by fund and in total.

Arguments: $ARGUMENTS

Rules:
- Apply the accounting policies in `${CLAUDE_PLUGIN_ROOT}/references/policies.md` and state any override.
- Run all arithmetic with `${CLAUDE_PLUGIN_ROOT}/scripts/pe_calcs.py` or spreadsheet formulas, and cross-check before output.
- Cite the source document ID for every figure; present results in a table ready for internal use.
