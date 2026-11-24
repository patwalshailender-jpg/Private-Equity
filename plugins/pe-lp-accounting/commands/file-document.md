---
description: File and index a PE fund document in the standard folder tree
argument-hint: <file> [fund code]
---

Use the `pe-documents` skill from this plugin. File the document, compute its hash, add the register row and route it.

Arguments: $ARGUMENTS

Rules:
- Apply the accounting policies in `${CLAUDE_PLUGIN_ROOT}/references/policies.md` and state any override.
- Run all arithmetic with `${CLAUDE_PLUGIN_ROOT}/scripts/pe_calcs.py` or spreadsheet formulas, and cross-check before output.
- Cite the source document ID for every figure; present results in a table ready for internal use.
