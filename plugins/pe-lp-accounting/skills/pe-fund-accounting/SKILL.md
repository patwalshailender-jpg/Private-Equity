---
name: "pe-fund-accounting"
description: "Investor-side private equity fund accounting - generate IFRS journal entries for calls, distributions, fair value remeasurement, FX, true-ups, secondaries and wind-down; run reconciliations R1-R8 (bank, GL, GP capital account, NAV, commitment, audited FS, custodian, fees) and manage the break log. Use for month-end / quarter-end PE accounting and reconciliation."
---

# Fund accounting and reconciliation

References: `${CLAUDE_PLUGIN_ROOT}/references/journal-library.md` (J1-J22), `policies.md` (P1-P16), `controls.md` (R1-R8).

## Sub-ledger per fund
Maintain: paid-in cost, cumulative distributions by type, fair value adjustment, carrying amount, unfunded commitment, recallable balance, GP-reported accrued carry, FX analysis.

## Journals (`/pe-journals`)
1. Collect processed cash events and quarter-end valuations for the period.
2. Select the journal pattern from the library; apply the policy defaults (state any override).
3. Map accounts using `${CLAUDE_PLUGIN_ROOT}/references/templates.md` (section gl_mapping).
4. Each line: journal no., date, fund code, account, debit, credit, currency, FX rate, source document ID, narrative.
5. Check debits = credits per journal (compute, do not eyeball).
6. Export in `${CLAUDE_PLUGIN_ROOT}/references/templates.md` (section journal_export) format for ERP upload.

## Reconciliations (`/pe-recon`)
Run R1-R8. For each: our balance, comparison balance, difference, explained items, unexplained difference, conclusion, preparer / reviewer.
- R3 capital account: commitment, contributions, distributions, unfunded - line by line against the GP CAS.
- R4 NAV: carrying amount vs rolled-forward GP NAV.
- R6 audited true-up (`/audited-trueup`): Q4 estimate vs audited fund FS NAV -> J14 as change in estimate (P8).
Unexplained differences above threshold block NAV sign-off.

## Break log (`/break-log`)
Columns per `${CLAUDE_PLUGIN_ROOT}/references/templates.md` (section break_log). Categorise Timing / Error / Unexplained; age every break; > 60 days -> audit committee pack (C12).

All arithmetic runs in Python or spreadsheet formulas and is cross-checked before output.
