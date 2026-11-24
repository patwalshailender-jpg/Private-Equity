---
description: "Draft a fee / carry query letter to the GP"
argument-hint: "<fund code>"
---

Use the `pe-fees-carry` skill from this plugin. Draft the letter from the latest exceptions.

Arguments: $ARGUMENTS

Rules:
- Apply the accounting policies in `${CLAUDE_PLUGIN_ROOT}/references/policies.md` and state any override.
- Compute all arithmetic with the functions in `${CLAUDE_PLUGIN_ROOT}/references/calculations.md` (run in Python) or spreadsheet formulas, and cross-check before output.
- Cite the source document ID for every figure; present results in a table ready for internal use.
