---
description: Abstract the LPA and side letter into the fund master
argument-hint: <LPA file> [side letter]
---

Use the `pe-fund-onboarding` skill from this plugin. Complete section 3 of the skill.

Arguments: $ARGUMENTS

Rules:
- Apply the accounting policies in `${CLAUDE_PLUGIN_ROOT}/references/policies.md` and state any override.
- Run all arithmetic with `${CLAUDE_PLUGIN_ROOT}/scripts/pe_calcs.py` or spreadsheet formulas, and cross-check before output.
- Cite the source document ID for every figure; present results in a table ready for internal use.
