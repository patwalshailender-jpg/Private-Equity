---
description: "PE KPI dashboard"
argument-hint: "<reporting date>"
---

Use the `pe-nav-reporting` skill from this plugin. Produce the dashboard KPIs and watch list.

Arguments: $ARGUMENTS

Rules:
- Apply the accounting policies in `${CLAUDE_PLUGIN_ROOT}/references/policies.md` and state any override.
- Compute all arithmetic with the functions in `${CLAUDE_PLUGIN_ROOT}/references/calculations.md` (run in Python) or spreadsheet formulas, and cross-check before output.
- Cite the source document ID for every figure; present results in a table ready for internal use.
