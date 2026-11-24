---
description: "Draft IFRS notes for PE interests"
argument-hint: "<year or period end>"
---

Use the `pe-ifrs-reporting` skill from this plugin. Produce all notes in the outputs table.

Arguments: $ARGUMENTS

Rules:
- Apply the accounting policies in `${CLAUDE_PLUGIN_ROOT}/references/policies.md` and state any override.
- Compute all arithmetic with the functions in `${CLAUDE_PLUGIN_ROOT}/references/calculations.md` (run in Python) or spreadsheet formulas, and cross-check before output.
- Cite the source document ID for every figure; present results in a table ready for internal use.
