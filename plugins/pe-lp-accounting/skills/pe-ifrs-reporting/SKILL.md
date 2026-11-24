---
name: "pe-ifrs-reporting"
description: "Prepare IFRS financial statement content for private equity fund interests held by an investor - IFRS 9 classification, IFRS 10 / IAS 28 assessment, IFRS 13 Level 3 roll-forward and sensitivity, IFRS 7 risk and liquidity notes, IFRS 12 unconsolidated structured entity disclosures, IAS 21, IAS 7, IAS 8, IAS 24, commitments, and IFRS 18 presentation mapping from 2027. Use at quarter or year end, for audit, or for IFRS 18 transition."
---

# IFRS reporting and disclosures

Policies: `${CLAUDE_PLUGIN_ROOT}/references/policies.md`. Cite the policy number and standard in every note working paper. Confirm paragraph references against https://www.ifrs.org before external use.

## Outputs (`/pe-disclosures`)
| Note | Content |
|---|---|
| Classification (IFRS 9) | Memo per fund: FVTPL, SPPI fail, FVOCI election not available (P1) |
| Control / influence (IFRS 10 / IAS 28) | Annual assessment for large stakes; IAS 28.18-19 FVTPL election where used, including the June 2026 amendment extending eligibility to entities whose main business activity is investing, and the one-time switch available on IFRS 18 transition (P12) |
| Fair value (IFRS 13) | Hierarchy table; valuation technique and inputs; Level 3 reconciliation (`/level3-rollforward`): opening, purchases (calls), sales / settlements (distributions), gains in P&L (realised / unrealised), transfers, closing; sensitivity narrative (e.g. +/-10% NAV) |
| Risk (IFRS 7) | Market (price), currency, liquidity (unfunded commitments by expected drawdown year), credit (receivables); concentration |
| Structured entities (IFRS 12) | Per fund or aggregated: nature, purpose, size (fund NAV), carrying amount, unfunded commitment, maximum exposure = carrying + unfunded, support provided (P13) |
| Foreign currency (IAS 21) | Translation policy, FX impact analysis (P9) |
| Cash flows (IAS 7) | Calls and distributions classification (P10) |
| Estimates (IAS 8) | Audited fund FS true-ups (P8); key judgements in valuation |
| Related parties (IAS 24) | GP or co-investment relationships, if any |
| Commitments | Undrawn commitments by fund / strategy |

## IFRS 18 mapping (`/ifrs18-map`)
From 1 January 2027: map PE gains, income and related expenses to the investing category, or operating where investing in assets is a main business activity (P11). Produce current-format and IFRS 18-format statements side by side, restated comparatives, and any management-defined performance measures note.

## Checklist (`/disclosure-checklist`)
Tick-off list by standard and paragraph with reference to the working paper and TB line; unresolved items listed for the Financial Controller.

Deliver note drafts in Word and supporting schedules in Excel cross-referenced to the trial balance.
