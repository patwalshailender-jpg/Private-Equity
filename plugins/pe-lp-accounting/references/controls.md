# Embedded controls

| ID | Risk | Control | Evidence |
|---|---|---|---|
| C1 | Payment fraud (spoofed notice, changed bank details) | Bank details compared with locked fund master; any change -> HOLD and independent call-back to a known GP contact | Call-back log |
| C2 | Duplicate or missed notices | Notice ref + amount + date + file hash check; quarterly capital account reconciliation (R3) | Register, R3 |
| C3 | Over-call | Hard stop: call <= unfunded + recallable | Validation record |
| C4 | Pro-rata error | Our share = commitment / total fund commitments x total call | Validation record |
| C5 | Fee / carry error | Independent recalculation (scripts/pe_calcs.py) within tolerance | Fee check file |
| C6 | Stale or unsupported NAV | Staleness flag, roll-forward, back-test, valuation memo | Memo |
| C7 | Cut-off | Notice / due / value date logic; accruals J2, J10 | Cut-off report |
| C8 | Segregation of duties | Preparer != reviewer != approver | Sign-off fields |
| C9 | Unauthorised commitment | Fund master activated only with IC / board approval reference | Approval link |
| C10 | Data integrity | Read-only originals, versioning, change log | Log |
| C11 | Policy drift | Policy table locked per year; changes need Financial Controller approval | Policy log |
| C12 | Unresolved breaks | Ageing; > 60 days to audit committee pack | Break log |
| C13 | Post-investment-period misuse | Calls after investment period limited to permitted purposes | Validation record |
| C14 | Sanctions / KYC | GP and co-investor screening before commitment and on change | Compliance tracker |

## Reconciliations

| ID | Reconciliation | Frequency |
|---|---|---|
| R1 | Bank vs booked calls and distributions | Monthly |
| R2 | PE sub-ledger vs GL | Monthly |
| R3 | Our records vs GP capital account statement | Quarterly |
| R4 | Carrying amount vs rolled-forward GP NAV | Quarterly |
| R5 | Commitment register vs LPA / side letter / GP | Quarterly |
| R6 | Q4 estimate vs audited fund FS | Annual |
| R7 | Register vs custodian / administrator | Quarterly |
| R8 | Recalculated vs charged fees | Quarterly |

Break categories: Timing, Error, Unexplained. Each break: amount, owner, ageing, resolution, evidence.
