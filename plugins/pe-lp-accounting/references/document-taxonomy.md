# Document storage taxonomy

## Folder tree (per fund)

```
PE/<GP name>/<Fund name>/
  01_Legal/            LPA, side letter, subscription docs, MFN elections, amendments
  02_Capital_Calls/    Notices, payment confirmations, call-back evidence
  03_Distributions/    Notices, bank credit advice, tax breakdowns
  04_Capital_Account/  Quarterly capital account statements (CAS)
  05_NAV_Reports/      Quarterly investor reports, portfolio company schedules
  06_Fund_FS/          Audited fund financial statements, audit opinion
  07_Memos/            IC, valuation, accounting, fee query, close-out memos
  08_Tax/              Tax packs, WHT certificates, residency certificates
  09_Correspondence/   GP emails, AGM / LPAC materials, consents, CV election packs
  10_Reconciliations/  Signed reconciliations
PE/_Portfolio/
  Journals/  NAV_Pack/  IFRS_Disclosures/  Board_Pack/  Audit_PBC/  Compliance/
```

## Naming

`<FundCode>_<DocType>_<YYYYMMDD>_<Ref>_v<n>.<ext>` e.g. `ABCIV_CALL_20261115_CC12_v1.pdf`

| DocType | Meaning |
|---|---|
| LEGAL | LPA, side letter, subscription, amendment |
| CALL | Capital call notice |
| DIST | Distribution notice |
| CAS | Capital account statement |
| NAV | Quarterly investor / NAV report |
| FS | Audited fund financial statements |
| MEMO | Any memo |
| TAX | Tax document |
| CORR | Correspondence |
| RECON | Reconciliation |
| CVEL | Continuation vehicle election pack |

## Rules

- Originals read-only; working copies separate.
- New version = `_v2`; never delete superseded versions; register marks supersession.
- SHA-256 hash recorded on upload (duplicate and tamper check).
- Register status: Received -> Processed -> Reviewed -> Filed.
- Retention default: fund life + 10 years; legal documents and memos permanent. Confirm against local law.
- Access: preparer, reviewer, approver, auditor (read-only); legal and banking restricted.
