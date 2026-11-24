---
description: "Price a secondary sale or purchase vs NAV"
argument-hint: "<fund code> <bid>"
---

Use the `pe-secondaries` skill from this plugin. Run the pricing analysis.

Arguments: $ARGUMENTS

Rules:
- Apply the accounting policies in `${CLAUDE_PLUGIN_ROOT}/references/policies.md` and state any override.
- Compute all arithmetic with the functions in `${CLAUDE_PLUGIN_ROOT}/references/calculations.md` (run in Python) or spreadsheet formulas, and cross-check before output.
- Cite the source document ID for every figure; present results in a table ready for internal use.
