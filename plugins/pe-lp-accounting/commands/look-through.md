---
description: "Portfolio company look-through across funds"
argument-hint: "<reporting date>"
---

Use the `pe-nav-reporting` skill from this plugin. Build look-through exposures from GP schedules.

Arguments: $ARGUMENTS

Rules:
- Apply the accounting policies in `${CLAUDE_PLUGIN_ROOT}/references/policies.md` and state any override.
- Compute all arithmetic with the functions in `${CLAUDE_PLUGIN_ROOT}/references/calculations.md` (run in Python) or spreadsheet formulas, and cross-check before output.
- Cite the source document ID for every figure; present results in a table ready for internal use.
