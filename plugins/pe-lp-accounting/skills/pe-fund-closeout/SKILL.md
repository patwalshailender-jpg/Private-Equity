---
name: pe-fund-closeout
description: Manage the end of a private equity fund's life - term extensions, final and in-specie distributions, release of unfunded commitment, clawback and escrow, final reconciliation and audited true-up, derecognition or write-off of residual NAV, and archive with final performance. Use when a fund nears the end of its term, is extended, liquidated or terminated.
---

# Fund wind-down and close-out (`/fund-closeout`)

1. Term tracking - fund term, extensions used / remaining, LPAC consents; flag funds within 12 months of term end.
2. Final distributions - process via `pe-cash-events`. In-specie distributions: record shares received at fair value as a new direct holding (J21) and set up its valuation.
3. Unfunded release - obtain GP confirmation that no further calls will be made; release remaining unfunded commitment from registers and disclosures.
4. Clawback and escrow - compute GP clawback due under the LPA (`pe-fees-carry` waterfall replay); record escrow releases.
5. Final reconciliation - full R3 capital account and R6 audited final fund FS true-up.
6. Derecognition - derecognise residual carrying amount when rights expire; if residual NAV is not expected to be recovered, write off (J22) with a memo.
7. Close - mark fund master closed; record final IRR, TVPI, DPI (`scripts/pe_calcs.py`); archive the folder read-only; write a lessons-learned note (GP performance, fees, reporting quality) for future re-up decisions.

Output: close-out memo with final performance, reconciliations and approvals, saved to `07_Memos`.
