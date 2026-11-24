---
description: Transfer of an LP interest checklist and entries
argument-hint: <fund code>
---

Use the `pe-secondaries` skill from this plugin. Complete the transfer checklist.

Arguments: $ARGUMENTS

Rules:
- Apply the accounting policies in `${CLAUDE_PLUGIN_ROOT}/references/policies.md` and state any override.
- Run all arithmetic with `${CLAUDE_PLUGIN_ROOT}/scripts/pe_calcs.py` or spreadsheet formulas, and cross-check before output.
- Cite the source document ID for every figure; present results in a table ready for internal use.
