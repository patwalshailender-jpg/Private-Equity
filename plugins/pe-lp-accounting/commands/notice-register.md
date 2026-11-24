---
description: Show or update the PE document / notice register
argument-hint: [fund code] [period]
---

Use the `pe-documents` skill from this plugin. List register rows with status; highlight items not yet Processed or Reviewed.

Arguments: $ARGUMENTS

Rules:
- Apply the accounting policies in `${CLAUDE_PLUGIN_ROOT}/references/policies.md` and state any override.
- Run all arithmetic with `${CLAUDE_PLUGIN_ROOT}/scripts/pe_calcs.py` or spreadsheet formulas, and cross-check before output.
- Cite the source document ID for every figure; present results in a table ready for internal use.
