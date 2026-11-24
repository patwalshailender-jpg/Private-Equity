---
name: "pe-compliance-audit"
description: "Private equity audit support and investor-side compliance - build the audit PBC pack, draft responses to auditor queries with document references, track FATCA / CRS / KYC / AIFMD investor requests and sanctions screening, and monitor side-letter rights. Use at audit time, when an auditor or GP compliance request arrives, or for periodic side-letter checks."
---

# Audit support and compliance

## Audit pack (`/pe-audit-pack`)
Assemble in `PE/_Portfolio/Audit_PBC/`:
1. Fund listing: commitment, called, distributions, unfunded, carrying amount, fair value (ties to TB).
2. Capital account confirmation request list (GP / administrator contacts).
3. Notice-to-journal tie-out for all period calls and distributions.
4. Reconciliations R1-R8 signed.
5. Valuation memos, roll-forward and back-test.
6. Level 3 roll-forward and sensitivity.
7. Audited fund FS and true-up workings.
8. Fee recalculations and GP responses.
9. Policy table and any changes.
10. Break log with resolutions.

## Auditor queries (`/audit-query-response`)
For each query: restate the query, answer with figures, cite register document IDs and working paper references, attach evidence, flag open items with owner and date.

## Compliance tracker (`/compliance-tracker`)
Rows per fund: FATCA / CRS self-certification (date, expiry), KYC / AML refresh requests, tax residency certificate, AIFMD / regulatory investor questionnaires, sanctions screening of GP and co-investors (control C14). Status and due date; overdue items flagged.

## Side-letter monitoring (`/side-letter-check`)
Quarterly: fee discount applied, ILPA-format reporting received, MFN elections made by deadline, co-invest offers received, excuse rights respected, LPAC rights. Exceptions -> query to GP.
