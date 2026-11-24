---
name: "pe-fund-onboarding"
description: "Onboard a private equity fund commitment - fund due diligence checklist, IC commitment memo, LPA and side-letter abstraction into a fund master, and accounting policy setup. Use when the investor is considering or has signed a new LP commitment, or when policies need to be set or changed."
---

# Fund onboarding

## 1. Pre-commitment due diligence (`/fund-dd`)
Produce a checklist with findings and evidence for: GP track record (net IRR, TVPI and especially DPI by prior fund), team stability and key persons, strategy and pipeline, terms vs market (fee, hurdle, carry, catch-up, GP commitment), ILPA principles alignment, valuation policy (IPEV), administrator and auditor quality, ESG policy, sanctions / KYC screening of GP (control C14), fund-level leverage (subscription line, NAV facility).

## 2. IC commitment memo (`/ic-commitment-memo`)
Sections: recommendation; fund summary; terms table; track record; fit with allocation and pacing (call `pe-liquidity-tax` pacing output); key risks and mitigants; fees and total cost estimate; approval requested. Record the approval reference once granted - the fund master cannot be activated without it (control C9).

## 3. LPA abstraction (`/onboard-fund`)
Read LPA, side letter and subscription documents. Fill every column of `${CLAUDE_PLUGIN_ROOT}/references/templates.md` (section fund_master):
- Identity: fund code, name, GP, administrator, auditor, domicile, vintage, strategy, geography, currency.
- Commitment: amount, total fund size, our close, equalisation terms.
- Term: investment period end, term, extensions, key-person clause.
- Economics: fee basis and rate by period, offsets %, expense caps, side-letter discount.
- Waterfall: European / American, hurdle, catch-up, carry, clawback, escrow.
- Cash rules: notice days, recallable rules and limit, recycling, default penalties, subscription line terms.
- Side-letter rights: MFN, ILPA reporting, co-invest, LPAC, excuse.
- Banking: GP payment instructions (lock them; changes later trigger control C1).
Quote the clause reference for every abstracted term. Flag ambiguous clauses for legal / Financial Controller confirmation. Save the abstraction memo to `07_Memos`.

## 4. Policy setup (`/policy-setup`)
Start from `${CLAUDE_PLUGIN_ROOT}/references/policies.md` (P1-P16). Record any override with reason, approver and effective date (control C11). Lock the policy table per financial year.
