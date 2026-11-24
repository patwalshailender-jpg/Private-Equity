---
name: pe-cash-events
description: Process private equity capital call notices, distribution notices and continuation vehicle (CV) election packs - extract, validate against the fund master, classify components, prepare approvals and draft journals, and update commitment, unfunded and recallable registers. Use when a GP call, distribution or GP-led secondary election arrives.
---

# Capital calls, distributions and CV elections

Inputs: the notice (filed via `pe-documents`), the fund master, the cash-flow ledger (`${CLAUDE_PLUGIN_ROOT}/templates/cash_flow_ledger.csv`).

## Seven-step workflow (no payment release before step 5)
1. Capture - confirm the notice is in the register.
2. Extract - notice no., notice date, due / value date, total fund amount, our amount, currency, bank details, component split.
3. Validate (controls in `${CLAUDE_PLUGIN_ROOT}/references/controls.md`):
   - C3 our call <= unfunded + recallable (compute with `scripts/pe_calcs.py`, function `unfunded`).
   - C4 pro-rata: our amount = commitment / total fund commitments x fund-level amount (tolerance 0.01%).
   - C1 bank details equal the locked master; if not -> HOLD and require call-back evidence.
   - C2 duplicate check.
   - Fee portion recalculated (`pe-fees-carry`); variance over tolerance -> query, do not block payment unless material.
   - C13 after investment period: only follow-ons, fees, expenses, permitted purposes.
   - Distributions: components sum to cash; FX and value date agree to bank advice.
4. Classify each component:
   - Call: investments, management fee, fund expenses, organisational costs, equalisation interest, subscription-line interest, recall of distribution.
   - Distribution: return of capital, realised gain, dividend, interest, WHT, recallable flag, carry withheld, equalisation received. Also tag the SOURCE: exit / recap / NAV-loan funded / CV proceeds / other.
5. Approve - preparer, reviewer, approver; attach call-back log for calls.
6. Book - generate journals via `pe-fund-accounting` (J2-J10, J20).
7. Update - cash-flow ledger, unfunded, recallable register, cash forecast.

Output a one-page processing sheet: extracted data, check results (pass / fail / hold), classification, journal preview, approvals.

## Continuation vehicle elections (`/cv-election`)
1. Summarise the pack: assets moving, price vs latest NAV (discount / premium %), lead buyer, fairness opinion, fee and carry terms of the new vehicle, crystallised carry, status-quo option, deadline.
2. Compare options: SELL (cash now, realised at price), ROLL (new commitment and terms), STATUS QUO if offered. Show DPI, IRR and exposure impact of each using `scripts/pe_calcs.py`.
3. Flag conflicts of interest, LPAC consent status and missing information.
4. Record the decision and approval; on SELL book as distribution (J6/J7); on ROLL onboard the new vehicle via `pe-fund-onboarding`.
