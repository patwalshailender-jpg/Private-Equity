---
description: "FATCA / CRS / KYC / regulatory request tracker"
argument-hint: "[fund code]"
---

Use the `pe-compliance-audit` skill from this plugin. Update and report the tracker.

Arguments: $ARGUMENTS

Rules:
- Apply the accounting policies in `${CLAUDE_PLUGIN_ROOT}/references/policies.md` and state any override.
- Compute all arithmetic with the functions in `${CLAUDE_PLUGIN_ROOT}/references/calculations.md` (run in Python) or spreadsheet formulas, and cross-check before output.
- Cite the source document ID for every figure; present results in a table ready for internal use.
