# Data templates

Column layouts for the plugin's registers and exports. CSV versions are in the repository's `tools/templates/` folder.


## break_log

| # | Column |
|---|---|
| 1 | `break_id` |
| 2 | `recon_id` |
| 3 | `fund_code` |
| 4 | `period` |
| 5 | `amount` |
| 6 | `category` |
| 7 | `description` |
| 8 | `owner` |
| 9 | `opened_date` |
| 10 | `age_days` |
| 11 | `resolution` |
| 12 | `resolved_date` |
| 13 | `evidence_doc_id` |

## cash_flow_ledger

| # | Column |
|---|---|
| 1 | `entry_id` |
| 2 | `fund_code` |
| 3 | `doc_id` |
| 4 | `notice_no` |
| 5 | `notice_date` |
| 6 | `due_date` |
| 7 | `value_date` |
| 8 | `event_type` |
| 9 | `component` |
| 10 | `source_tag` |
| 11 | `amount_fund_ccy` |
| 12 | `fx_rate` |
| 13 | `amount_reporting_ccy` |
| 14 | `recallable_flag` |
| 15 | `journal_no` |
| 16 | `status` |

## compliance_tracker

| # | Column |
|---|---|
| 1 | `fund_code` |
| 2 | `requirement` |
| 3 | `requested_by` |
| 4 | `requested_date` |
| 5 | `due_date` |
| 6 | `submitted_date` |
| 7 | `expiry_date` |
| 8 | `status` |
| 9 | `evidence_doc_id` |

## document_register

| # | Column |
|---|---|
| 1 | `doc_id` |
| 2 | `fund_code` |
| 3 | `doc_type` |
| 4 | `reference` |
| 5 | `document_date` |
| 6 | `period` |
| 7 | `amount` |
| 8 | `currency` |
| 9 | `file_name` |
| 10 | `path` |
| 11 | `sha256` |
| 12 | `version` |
| 13 | `supersedes` |
| 14 | `status` |
| 15 | `received_date` |
| 16 | `processed_by` |
| 17 | `reviewed_by` |

## fund_master

| # | Column |
|---|---|
| 1 | `fund_code` |
| 2 | `fund_name` |
| 3 | `gp` |
| 4 | `administrator` |
| 5 | `auditor` |
| 6 | `domicile` |
| 7 | `vintage` |
| 8 | `strategy` |
| 9 | `geography` |
| 10 | `currency` |
| 11 | `commitment` |
| 12 | `total_fund_commitments` |
| 13 | `close_date` |
| 14 | `investment_period_end` |
| 15 | `term_end` |
| 16 | `extensions_remaining` |
| 17 | `fee_basis_ip` |
| 18 | `fee_rate_ip` |
| 19 | `fee_basis_post` |
| 20 | `fee_rate_post` |
| 21 | `fee_offset_pct` |
| 22 | `side_letter_fee_discount` |
| 23 | `waterfall_type` |
| 24 | `hurdle` |
| 25 | `catch_up` |
| 26 | `carry` |
| 27 | `clawback` |
| 28 | `notice_days` |
| 29 | `recallable_rules` |
| 30 | `subscription_line` |
| 31 | `mfn` |
| 32 | `ilpa_reporting_right` |
| 33 | `gp_bank_details_hash` |
| 34 | `approval_ref` |
| 35 | `status` |

## gl_mapping

| # | Column |
|---|---|
| 1 | `library_account` |
| 2 | `erp_account_code` |
| 3 | `erp_account_name` |
| 4 | `cost_centre` |
| 5 | `notes` |

Default rows:

| library_account | erp_account_code | erp_account_name | cost_centre | notes |
|---|---|---|---|---|
| Investment in PE fund - cost |  |  |  |  |
| Investment - FV adjustment |  |  |  |  |
| Investment - FX |  |  |  | analysis only |
| Capital call payable |  |  |  |  |
| Distribution receivable |  |  |  |  |
| WHT receivable |  |  |  |  |
| Cash at bank |  |  |  |  |
| Net gain / (loss) on financial assets at FVTPL |  |  |  |  |
| Finance cost |  |  |  |  |
| ECL expense |  |  |  |  |
| Direct investment |  |  |  | in-specie |

## journal_export

| # | Column |
|---|---|
| 1 | `journal_no` |
| 2 | `date` |
| 3 | `fund_code` |
| 4 | `account_code` |
| 5 | `description` |
| 6 | `debit` |
| 7 | `credit` |
| 8 | `currency` |
| 9 | `fx_rate` |
| 10 | `source_doc_id` |
| 11 | `preparer` |
| 12 | `approver` |

## nav_history

| # | Column |
|---|---|
| 1 | `fund_code` |
| 2 | `gp_report_date` |
| 3 | `gp_nav_fund_ccy` |
| 4 | `calls_after` |
| 5 | `dists_after` |
| 6 | `fx_rate` |
| 7 | `adjustments` |
| 8 | `adjusted_nav_reporting_ccy` |
| 9 | `reporting_date` |
| 10 | `doc_id` |
| 11 | `level` |
| 12 | `staleness_flag` |

## wht_register

| # | Column |
|---|---|
| 1 | `fund_code` |
| 2 | `distribution_doc_id` |
| 3 | `income_country` |
| 4 | `gross_income` |
| 5 | `wht_deducted` |
| 6 | `treaty_rate` |
| 7 | `excess_reclaimable` |
| 8 | `reclaim_filed_date` |
| 9 | `time_bar_date` |
| 10 | `status` |
