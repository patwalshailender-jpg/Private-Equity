---
description: Map PE income and expenses to IFRS 18 categories
argument-hint: <period end>
---

Use the `pe-ifrs-reporting` skill from this plugin. Produce current vs IFRS 18 presentation.

Arguments: $ARGUMENTS

Rules:
- Apply the accounting policies in `${CLAUDE_PLUGIN_ROOT}/references/policies.md` and state any override.
- Run all arithmetic with `${CLAUDE_PLUGIN_ROOT}/scripts/pe_calcs.py` or spreadsheet formulas, and cross-check before output.
- Cite the source document ID for every figure; present results in a table ready for internal use.
