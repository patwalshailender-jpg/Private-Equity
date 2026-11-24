---
name: "pe-documents"
description: "File, name, index and retrieve private equity fund documents (capital calls, distributions, capital account statements, NAV reports, audited fund FS, memos, legal and tax documents) in a standard folder tree with a document register. Use when a GP document arrives, when filing or searching PE documents, or when building an evidence trail."
---

# PE document storage

Read `${CLAUDE_PLUGIN_ROOT}/references/document-taxonomy.md` first. It defines the folder tree, naming rule, document types and retention.

## Filing a document
1. Identify fund, GP and document type (CALL, DIST, CAS, NAV, FS, MEMO, LEGAL, TAX, CORR, RECON, CVEL).
2. Extract the key fields for the register (columns in `${CLAUDE_PLUGIN_ROOT}/references/templates.md` (section document_register)): notice / reference no., document date, period, amount, currency, due or value date.
3. Compute the SHA-256 hash of the file. If the hash or (fund, ref, amount, date) already exists in the register, stop and report a possible duplicate (control C2).
4. Name the file `<FundCode>_<DocType>_<YYYYMMDD>_<Ref>_v<n>`. A revised document gets the next version; never overwrite.
5. Save to the correct folder on the connected storage (SharePoint / Google Drive / local). If no storage connector is available, produce the target path and the register row for the user to file.
6. Append the register row with status `Received`.
7. Route: CALL / DIST -> `pe-cash-events`; CAS / NAV -> `pe-valuation`; FS -> `pe-fund-accounting` (audited true-up); LEGAL -> `pe-fund-onboarding`; CVEL -> `pe-cash-events`.

## Searching
Search the register first (fund, type, period, ref), then open the file. Always return the file path with the answer.

## Rules
- Originals are read-only. Work on copies.
- Every journal, reconciliation and report line must cite a register document ID.
- Never delete; mark superseded versions in the register.
