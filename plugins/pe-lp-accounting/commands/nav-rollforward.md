---
description: "Roll GP NAV forward to the reporting date"
argument-hint: "<reporting date> [fund code]"
---

Use the `pe-valuation` skill from this plugin. Run the roll-forward steps for each fund.

Arguments: $ARGUMENTS

Rules:
- Apply the accounting policies in `${CLAUDE_PLUGIN_ROOT}/references/policies.md` and state any override.
- Compute all arithmetic with the functions in `${CLAUDE_PLUGIN_ROOT}/references/calculations.md` (run in Python) or spreadsheet formulas, and cross-check before output.
- Cite the source document ID for every figure; present results in a table ready for internal use.
