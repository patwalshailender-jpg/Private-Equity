---
description: Replay the carry waterfall vs GP accrual
argument-hint: <fund code> <date>
---

Use the `pe-fees-carry` skill from this plugin. Run the waterfall check.

Arguments: $ARGUMENTS

Rules:
- Apply the accounting policies in `${CLAUDE_PLUGIN_ROOT}/references/policies.md` and state any override.
- Run all arithmetic with `${CLAUDE_PLUGIN_ROOT}/scripts/pe_calcs.py` or spreadsheet formulas, and cross-check before output.
- Cite the source document ID for every figure; present results in a table ready for internal use.
