---
description: True up Q4 estimate to audited fund FS
argument-hint: <fund code> <audited FS file>
---

Use the `pe-fund-accounting` skill from this plugin. Run R6 and prepare J14.

Arguments: $ARGUMENTS

Rules:
- Apply the accounting policies in `${CLAUDE_PLUGIN_ROOT}/references/policies.md` and state any override.
- Run all arithmetic with `${CLAUDE_PLUGIN_ROOT}/scripts/pe_calcs.py` or spreadsheet formulas, and cross-check before output.
- Cite the source document ID for every figure; present results in a table ready for internal use.
