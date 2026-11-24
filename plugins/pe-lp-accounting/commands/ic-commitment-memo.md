---
description: "Draft the IC / board memo for a new fund commitment"
argument-hint: "<fund name>"
---

Use the `pe-fund-onboarding` skill from this plugin. Complete section 2 of the skill.

Arguments: $ARGUMENTS

Rules:
- Apply the accounting policies in `${CLAUDE_PLUGIN_ROOT}/references/policies.md` and state any override.
- Compute all arithmetic with the functions in `${CLAUDE_PLUGIN_ROOT}/references/calculations.md` (run in Python) or spreadsheet formulas, and cross-check before output.
- Cite the source document ID for every figure; present results in a table ready for internal use.
