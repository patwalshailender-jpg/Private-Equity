# PE LP Accounting plugin

End-to-end private equity for the investor (Limited Partner), from fund due diligence to fund close-out, following IFRS and industry standards (ILPA templates, IPEV Valuation Guidelines).

> **Disclaimer:** This plugin provides professional support for qualified finance teams. It is not accounting, audit, tax, legal or investment advice. All outputs, including figures, journal entries and IFRS disclosures, must be reviewed and approved by a qualified accountant before use. IFRS references should be confirmed against the current standards at https://www.ifrs.org.


## Contents

| Folder | What it holds |
|---|---|
| `skills/` | 12 skills, one per module (loaded automatically when relevant) |
| `commands/` | 43 slash commands |
| `references/` | Accounting policy defaults (P1-P16), journal library (J1-J22), document taxonomy, controls (C1-C14) and reconciliations (R1-R8) |
| `scripts/pe_calcs.py` | Deterministic calculations: XIRR, DPI / RVPI / TVPI, KS-PME, unfunded, NAV roll-forward, management fee, European waterfall |
| `templates/` | CSV schemas: fund master, cash-flow ledger, NAV history, document register, break log, GL mapping, journal export, compliance tracker, WHT register |
| `tests/` | Unit tests and independent benchmark tests |
| `VALIDATION.md` | Latest validation report: 33 of 33 checks passed |

## Skills and commands

| Skill | Commands |
|---|---|
| pe-documents | `/file-document`, `/notice-register`, `/doc-search` |
| pe-fund-onboarding | `/fund-dd`, `/ic-commitment-memo`, `/onboard-fund`, `/policy-setup` |
| pe-cash-events | `/process-call`, `/process-distribution`, `/cv-election` |
| pe-fund-accounting | `/pe-journals`, `/pe-recon`, `/break-log`, `/audited-trueup` |
| pe-valuation | `/nav-rollforward`, `/valuation-memo`, `/nav-backtest` |
| pe-nav-reporting | `/nav-pack`, `/pe-performance`, `/commitment-report`, `/look-through`, `/pe-dashboard`, `/pe-mgmt-pack` |
| pe-ifrs-reporting | `/pe-disclosures`, `/level3-rollforward`, `/ifrs18-map`, `/disclosure-checklist` |
| pe-fees-carry | `/fee-check`, `/waterfall-check`, `/fee-query-letter` |
| pe-liquidity-tax | `/cash-forecast`, `/pacing-model`, `/pe-budget`, `/fx-exposure`, `/wht-tracker` |
| pe-secondaries | `/secondary-pricing`, `/secondary-accounting`, `/lp-transfer` |
| pe-compliance-audit | `/pe-audit-pack`, `/audit-query-response`, `/compliance-tracker`, `/side-letter-check` |
| pe-fund-closeout | `/fund-closeout` |

## Recommended connectors

Connect in Claude settings (not bundled): document storage (SharePoint / OneDrive or Google Drive) for the document vault, email (Outlook or Gmail) for notice intake, and your ERP if a connector exists. Without connectors the plugin works on uploaded files and produces outputs for manual filing and upload.

## Before first use

1. Fill `templates/gl_mapping.csv` with your chart of accounts.
2. Review `references/policies.md` and record any overrides with `/policy-setup`.
3. Onboard each fund with `/onboard-fund`.
4. Run `python3 scripts/pe_calcs.py selftest`.

IFRS paragraph references should be confirmed against https://www.ifrs.org by your technical accounting team before external use.

## Licence

MIT. See [LICENSE](LICENSE). Copyright (c) 2026 patwalshailender-jpg.
