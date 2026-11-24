# Journal entry library (LP interest at FVTPL)

Map account names to the entity's chart of accounts with `references/templates.md` (section gl_mapping).
Every journal line carries: journal no., date, fund code, source document ID, preparer, approver.

| # | Event | Debit | Credit | Notes |
|---|---|---|---|---|
| J1 | Commitment signed | - | - | Off balance sheet; commitment register and disclosure |
| J2 | Call due at period end, unpaid (P2) | Investment in PE fund - cost | Capital call payable | Reverse with J20 on payment |
| J3 | Capital call paid | Investment in PE fund - cost | Cash at bank | Includes fee and expense portion (P3) |
| J4 | Equalisation interest paid | Investment - cost | Cash at bank | P4 |
| J5 | Equalisation interest received | Cash at bank | Investment - cost | P4; income only if GP designates |
| J6 | Distribution - return of capital | Cash at bank | Investment - cost | |
| J7 | Distribution - realised gain | Cash at bank | Investment - carrying amount | Gain recognised through remeasurement (P6) |
| J8 | Distribution - dividend / interest | Cash at bank; WHT receivable or expense | Investment - carrying amount | Gross-up for WHT; income disclosed in notes |
| J9 | Recallable distribution recalled | Investment - cost | Cash at bank | Updates unfunded register |
| J10 | Distribution notice received, cash after period end | Distribution receivable | Investment - carrying amount | Cut-off |
| J11 | Quarter-end fair value gain | Investment - FV adjustment | Net gain on financial assets at FVTPL | Adjusted NAV minus carrying amount |
| J12 | Quarter-end fair value loss | Net loss on financial assets at FVTPL | Investment - FV adjustment | |
| J13 | FX analysis (memo split) | Investment - FX | FVTPL gain - FX component | Analysis only where FX tracked separately (P9) |
| J14 | Audited fund FS true-up | Investment - FV adjustment | FVTPL gain (or reverse) | P8 |
| J15 | Fee rebate received in cash | Cash at bank | Investment - carrying amount | Side letter |
| J16 | Secondary sale of LP interest | Cash / receivable | Investment - carrying amount; FVTPL gain (or Dr loss) | Derecognition; transfer unfunded commitment |
| J17 | Secondary purchase | Investment - cost | Cash; deferred consideration payable | Remeasure to fair value at next reporting date |
| J18 | Default penalty / late interest | Finance cost | Cash at bank | Exceptional |
| J19 | Expected credit loss on receivable | ECL expense | Loss allowance | Usually immaterial |
| J20 | Payment of accrued call | Capital call payable | Cash at bank | |
| J21 | In-specie distribution received | Direct investment (at fair value) | Investment - carrying amount | New holding set up at fair value |
| J22 | Residual NAV write-off at fund termination | FVTPL loss | Investment - carrying amount | Memo required |

Controls: sequential numbering; source link on every line; preparer differs from approver; period lock respected; corrections only by reversal plus new entry.
