---
description: "Show and age reconciliation breaks"
argument-hint: "[fund code]"
---

Use the `pe-fund-accounting` skill from this plugin. Summarise open breaks by category and ageing.

Arguments: $ARGUMENTS

Rules:
- Apply the accounting policies in `${CLAUDE_PLUGIN_ROOT}/references/policies.md` and state any override.
- Compute all arithmetic with the functions in `${CLAUDE_PLUGIN_ROOT}/references/calculations.md` (run in Python) or spreadsheet formulas, and cross-check before output.
- Cite the source document ID for every figure; present results in a table ready for internal use.
