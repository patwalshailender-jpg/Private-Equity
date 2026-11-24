---
description: Calculate IRR, DPI, RVPI, TVPI and PME
argument-hint: <reporting date> [fund|vintage|strategy]
---

Use the `pe-nav-reporting` skill from this plugin. Use scripts/pe_calcs.py for every figure.

Arguments: $ARGUMENTS

Rules:
- Apply the accounting policies in `${CLAUDE_PLUGIN_ROOT}/references/policies.md` and state any override.
- Run all arithmetic with `${CLAUDE_PLUGIN_ROOT}/scripts/pe_calcs.py` or spreadsheet formulas, and cross-check before output.
- Cite the source document ID for every figure; present results in a table ready for internal use.
