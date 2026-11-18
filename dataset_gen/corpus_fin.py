"""Finance and accounting corpus (5 documents)."""

DOCS = [
    {
        "id": "FIN-POL-001",
        "title": "Expense Reimbursement and Corporate Card Policy",
        "doc_type": "Policy",
        "category": "Finance",
        "department": "Finance Operations",
        "author": "Helena Brandt, Controller",
        "owner": "Finance Operations",
        "version": "9.2",
        "effective": "2026-01-01",
        "classification": "Internal",
        "review": "Annual",
        "summary": (
            "Sets the rules for submitting business expenses at Northwind, the "
            "approval thresholds, per-diem and travel limits by region, "
            "corporate card tiers and their limits, prohibited expenses, and "
            "the timelines for submission, audit, and reimbursement."
        ),
        "tags": ["expenses", "concur", "per diem", "corporate card", "reimbursement", "T&E"],
        "sections": [
            {
                "heading": "Submitting Expenses",
                "paragraphs": [
                    "All business expenses are submitted in Concur within 30 "
                    "calendar days of the expense being incurred, or within 30 "
                    "days of returning from a trip longer than a week. Expenses "
                    "older than 60 days are rejected automatically and cannot "
                    "be resubmitted without a Controller exception. A receipt "
                    "is required for every expense above 25 USD, or the local "
                    "equivalent; expenses below that threshold may be claimed "
                    "without a receipt up to a total of 75 USD per month.",
                    "Approval is by line manager up to 2,500 USD per expense "
                    "report. Reports above 2,500 USD additionally require the "
                    "department head, and reports above 10,000 USD require the "
                    "Controller. Approvers have a five business day service "
                    "level; reports unapproved after 15 days are escalated "
                    "automatically to the next level rather than left open.",
                    "Reimbursement is paid on the twice-monthly payroll run, "
                    "which means an approved expense is paid on the next run "
                    "after approval, typically 10 to 15 days after submission."
                ],
            },
            {
                "heading": "Travel Limits",
                "paragraphs": [
                    "Northwind uses a per-diem model for meals and incidentals "
                    "so that employees do not need to track every coffee. "
                    "Accommodation is reimbursed at actual cost up to the city "
                    "cap. Flights are booked through the corporate travel "
                    "agency only; independently booked flights are reimbursed "
                    "at 80 percent of the agency quote unless the trip was "
                    "urgent and pre-approved by the department head."
                ],
                "table": [
                    ["Region", "Meal per diem", "Accommodation cap per night", "Class of travel"],
                    ["US Tier 1 (NYC, SF)", "95 USD", "325 USD", "Economy, premium economy over 6 hours"],
                    ["US Tier 2", "70 USD", "225 USD", "Economy"],
                    ["London", "85 GBP", "275 GBP", "Economy, premium economy over 6 hours"],
                    ["EU Western", "75 EUR", "215 EUR", "Economy"],
                    ["Singapore, Tokyo", "90 SGD / 18,000 JPY", "290 USD", "Economy, premium economy over 6 hours"],
                ],
            },
            {
                "heading": "Corporate Card Tiers",
                "paragraphs": [
                    "Three card tiers exist. The general staff card carries a "
                    "5,000 USD monthly limit and blocks the prohibited "
                    "merchant categories at authorisation. The manager card "
                    "carries 15,000 USD and may be used for team events. The "
                    "travel card carries 25,000 USD and is issued only to "
                    "employees who travel more than 20 days per year. Cards are "
                    "personal and may not be shared, including with an "
                    "assistant.",
                    "Card data is reconciled monthly against Concur. A card "
                    "transaction with no matching expense line after 45 days is "
                    "reported to the cardholder's department head, and two "
                    "consecutive months of unreconciled spend results in the "
                    "card being suspended."
                ],
                "bullets": [
                    "Prohibited: alcohol above 100 USD per event, first class travel, personal purchases of any kind, fines and penalties.",
                    "Prohibited: cash advances except for countries where card acceptance is documented as unreliable.",
                    "Team building is capped at 120 USD per person per event and 300 USD per person per year.",
                    "Client entertainment requires the client's organisation named on the expense line.",
                ],
            },
            {
                "heading": "Audit and Consequences",
                "paragraphs": [
                    "Finance Operations audits 8 percent of expense reports on "
                    "a risk-weighted sample, plus 100 percent of reports above "
                    "5,000 USD, reports from employees with prior findings, and "
                    "reports containing merchant categories flagged as high "
                    "risk. Audit findings are reported to the department head "
                    "quarterly. Duplicate claims, split claims designed to "
                    "avoid an approval threshold, and personal purchases "
                    "claimed as business are treated as conduct matters under "
                    "HR-STD-009 rather than as clerical errors.",
                    "Employees may correct a submitted report at any time "
                    "before payment without consequence. Self-reporting an "
                    "error after payment is handled as a repayment, not a "
                    "disciplinary matter, provided it is reported within 10 "
                    "business days of noticing."
                ],
                "qa": [
                    {
                        "question": "Within how many days must an expense be submitted?",
                        "answer": "Within 30 calendar days of the expense, or 30 days of returning from a trip longer than a week.",
                    },
                    {
                        "question": "What is the receipt threshold?",
                        "answer": "A receipt is required for every expense above 25 USD.",
                    },
                    {
                        "question": "Who must approve an expense report above 10,000 USD?",
                        "answer": "The Controller, in addition to the line manager and department head.",
                    },
                ],
            },
        ],
        "qa": [
            {"question": "After how many days are unsubmitted expenses automatically rejected?",
             "answer": "60 days.",
             "evidence": "Expenses older than 60 days are rejected automatically"},
            {"question": "What is the US Tier 1 accommodation cap per night?",
             "answer": "325 USD.",
             "evidence": "US Tier 1 (NYC, SF) | 95 USD | 325 USD"},
            {"question": "What monthly limit does the manager corporate card carry?",
             "answer": "15,000 USD.",
             "evidence": "The manager card carries 15,000 USD"},
            {"question": "What percentage of expense reports does Finance Operations audit?",
             "answer": "8 percent on a risk-weighted sample, plus 100 percent of reports above 5,000 USD.",
             "evidence": "audits 8 percent of expense reports on a risk-weighted sample, plus 100 percent of reports above 5,000 USD"},
            {"question": "What is the team building cap per person per year?",
             "answer": "300 USD per person per year, and 120 USD per person per event.",
             "evidence": "Team building is capped at 120 USD per person per event and 300 USD per person per year"},
        ],
    },
    {
        "id": "FIN-STD-006",
        "title": "Procurement and Purchase Approval Standard",
        "doc_type": "Standard",
        "category": "Finance",
        "department": "Procurement",
        "author": "Daniel Okonkwo, Head of Procurement",
        "owner": "Procurement",
        "version": "5.4",
        "effective": "2026-02-01",
        "classification": "Internal",
        "review": "Annual",
        "summary": (
            "Defines the purchase requisition workflow, approval thresholds by "
            "value, competitive bidding rules, preferred supplier obligations, "
            "the purchase order requirement, and the treatment of "
            "maverick spend and emergency purchases."
        ),
        "tags": ["procurement", "purchase order", "RFQ", "supplier", "sourcing", "requisition"],
        "sections": [
            {
                "heading": "Requisition to Purchase Order",
                "paragraphs": [
                    "Nothing may be ordered from a supplier without a purchase "
                    "order, except expenses covered by the corporate card "
                    "policy. A requisition is raised in the Procurement Portal "
                    "and routes automatically for approval. The approved "
                    "requisition becomes a purchase order, which is the only "
                    "document that creates a legal commitment for Northwind. "
                    "An email telling a supplier to proceed is not a purchase "
                    "order and does not obligate Northwind to pay.",
                    "Invoices are matched three ways against the purchase "
                    "order and the goods or service receipt. A mismatch above "
                    "5 percent blocks payment until resolved. Suppliers are "
                    "paid on net 30 from a valid, matched invoice, and Northwind "
                    "takes a 1.5 percent discount for payment within 10 days "
                    "where the supplier offers it."
                ],
            },
            {
                "heading": "Approval Thresholds",
                "paragraphs": [
                    "Approvals scale with annual contract value, not with the "
                    "first invoice, because multi-year commitments are the "
                    "common route around a threshold. Where a contract has an "
                    "auto-renewal, the full committed value including renewals "
                    "is used for the threshold."
                ],
                "table": [
                    ["Annual contract value", "Approvals required", "Procurement involvement", "Legal review"],
                    ["Under 5,000 USD", "Line manager", "Catalogue only", "Not required"],
                    ["5,000 - 50,000 USD", "Line manager and department head", "Buyer assigned", "Standard terms only"],
                    ["50,000 - 250,000 USD", "Department head and Finance Business Partner", "Full sourcing support", "Required"],
                    ["250,000 - 1,000,000 USD", "VP and CFO delegate", "Competitive bid mandatory", "Required"],
                    ["Over 1,000,000 USD", "CFO and Executive Staff sponsor", "Competitive bid with board notification", "Required"],
                ],
            },
            {
                "heading": "Competitive Bidding",
                "paragraphs": [
                    "Contracts above 250,000 USD require a minimum of three "
                    "comparable bids evaluated against a scoring matrix agreed "
                    "before the request for quotation is issued. Price carries "
                    "a weighting of 40 percent, capability 30 percent, security "
                    "and compliance 20 percent, and supplier sustainability 10 "
                    "percent. The scoring matrix may not be changed after bids "
                    "are received.",
                    "A sole-source justification is permitted where only one "
                    "supplier can meet a documented requirement, where "
                    "switching cost exceeds the expected benefit of a bid, or "
                    "where the purchase extends an existing agreement. Sole "
                    "source above 250,000 USD requires the department head and "
                    "the CFO to sign the justification, and is reported "
                    "quarterly to the Audit Committee."
                ],
                "bullets": [
                    "Three bids minimum above 250,000 USD, scored on a pre-agreed matrix.",
                    "Weightings: price 40, capability 30, security 20, sustainability 10.",
                    "Preferred suppliers must be invited to every relevant bid.",
                    "Sole source above 250,000 USD is reported to the Audit Committee.",
                ],
            },
            {
                "heading": "Maverick Spend and Emergency Purchases",
                "paragraphs": [
                    "Maverick spend, meaning purchases made outside the "
                    "requisition process, is measured monthly by department and "
                    "reported to the CFO. Departments above 5 percent maverick "
                    "spend are required to produce a remediation plan. "
                    "Maverick spend is not automatically disallowed, but the "
                    "retrospective purchase order must be approved by the level "
                    "that should have approved the original purchase.",
                    "Emergency purchases that cannot wait for the normal "
                    "approval path may be authorised verbally by the department "
                    "head, who must raise the requisition within two business "
                    "days. Emergency authorisation may not be used to work "
                    "around a planned deadline; repeat use for the same "
                    "department triggers a review of its forecasting."
                ],
                "qa": [
                    {
                        "question": "What document creates a legal commitment for Northwind?",
                        "answer": "The purchase order generated from an approved requisition.",
                    },
                    {
                        "question": "At what value does a competitive bid become mandatory?",
                        "answer": "Above 250,000 USD annual contract value, with three comparable bids.",
                    },
                    {
                        "question": "What is the standard payment term?",
                        "answer": "Net 30 from a valid, matched invoice.",
                    },
                ],
            },
        ],
        "qa": [
            {"question": "Above what contract value are three competitive bids required?",
             "answer": "250,000 USD annual contract value.",
             "evidence": "Contracts above 250,000 USD require a minimum of three comparable bids"},
            {"question": "What price weighting is used in the bid scoring matrix?",
             "answer": "40 percent price, 30 capability, 20 security and compliance, 10 sustainability.",
             "evidence": "Price carries a weighting of 40 percent, capability 30 percent, security and compliance 20 percent"},
            {"question": "What invoice-to-PO mismatch percentage blocks payment?",
             "answer": "A mismatch above 5 percent.",
             "evidence": "A mismatch above 5 percent blocks payment until resolved"},
            {"question": "What maverick spend rate triggers a remediation plan?",
             "answer": "Departments above 5 percent maverick spend.",
             "evidence": "Departments above 5 percent maverick spend are required to produce a remediation plan"},
            {"question": "What are Northwind's standard supplier payment terms?",
             "answer": "Net 30 from a valid, matched invoice, with a 1.5 percent discount for payment within 10 days where offered.",
             "evidence": "Suppliers are paid on net 30 from a valid, matched invoice"},
        ],
    },
    {
        "id": "FIN-STD-011",
        "title": "Revenue Recognition Guidance for SaaS Contracts",
        "doc_type": "Guidance",
        "category": "Finance",
        "department": "Technical Accounting",
        "author": "Helena Brandt, Controller",
        "owner": "Technical Accounting",
        "version": "3.0",
        "effective": "2026-01-01",
        "classification": "Confidential",
        "review": "Annual",
        "summary": (
            "Applies the five-step revenue model to Northwind's subscription "
            "business. Explains performance obligation identification, "
            "allocation of standalone selling price, treatment of implementation "
            "services, contract assets and deferred revenue, and the "
            "capitalisation of contract acquisition costs."
        ),
        "tags": ["revenue recognition", "ASC 606", "IFRS 15", "deferred revenue", "SSP", "contract assets"],
        "sections": [
            {
                "heading": "The Five-Step Model at Northwind",
                "paragraphs": [
                    "Northwind applies the five-step model in ASC 606 and IFRS "
                    "15. Step one requires a contract with commercial substance "
                    "and approved enforceable rights, which in practice means a "
                    "signed order form or an accepted click-through agreement "
                    "with payment terms. Step two identifies performance "
                    "obligations. Step three determines the transaction price. "
                    "Step four allocates the price to obligations on standalone "
                    "selling price. Step five recognises revenue as each "
                    "obligation is satisfied.",
                    "The subscription itself is a single performance obligation "
                    "satisfied over time and recognised ratably from the service "
                    "start date, which is not necessarily the contract signature "
                    "date. Where a contract permits the customer to receive "
                    "updates and new features, the subscription and the updates "
                    "are combined into one obligation rather than separated."
                ],
            },
            {
                "heading": "Distinct and Non-Distinct Services",
                "paragraphs": [
                    "Implementation and configuration services are normally not "
                    "distinct when they significantly customise the platform or "
                    "are required for the customer to use it. Non-distinct "
                    "services are combined with the subscription and recognised "
                    "over the subscription period. Where implementation is "
                    "genuinely optional, does not customise the software, and is "
                    "sold separately by other vendors, it is distinct and is "
                    "recognised as the service is delivered.",
                    "Professional services delivered by Northwind's own team are "
                    "assessed on the same test each quarter, and the conclusion "
                    "is documented in the accounting memo library. A change in "
                    "conclusion is a material accounting judgement and requires "
                    "the Controller's approval and disclosure to the Audit "
                    "Committee."
                ],
                "table": [
                    ["Element", "Distinct?", "Recognition pattern", "Rationale"],
                    ["Core subscription", "No, combined with updates", "Ratable over subscription term", "Customer benefits continuously"],
                    ["Mandatory implementation", "No", "Over subscription term", "Required for the customer to use the platform"],
                    ["Optional training", "Yes", "As delivered", "Sold separately, no customisation"],
                    ["Premium support tier", "Yes", "Ratable over support term", "Standalone benefit, priced separately"],
                    ["Usage-based credits", "Yes", "As consumed", "Right to invoice as the benefit is received"],
                ],
            },
            {
                "heading": "Standalone Selling Price",
                "paragraphs": [
                    "Allocation uses observable standalone selling price where "
                    "available. Where a component is never sold separately, "
                    "Northwind estimates using the expected cost plus a margin "
                    "approach or the residual approach, and the method is "
                    "applied consistently within a component class. The SSP "
                    "table is refreshed twice a year, in January and July, by "
                    "Technical Accounting and is approved by the Controller.",
                    "Material rights, such as a discount on renewal that is "
                    "more than the normal discount range given to new "
                    "customers, must be identified and deferred into the "
                    "renewal period. The normal discount range for the core "
                    "product is 5 to 15 percent, so a renewal discount above 15 "
                    "percent is tested for a material right."
                ],
                "notes": [
                    "Common error: allocating a bundle at contract list price "
                    "rather than SSP. Where a discount of 30 percent is given on "
                    "a bundle, the discount must be allocated to all obligations "
                    "proportionately, not absorbed entirely by the services line."
                ],
            },
            {
                "heading": "Contract Costs",
                "paragraphs": [
                    "Incremental costs of obtaining a contract, principally "
                    "sales commissions that would not have been incurred without "
                    "the contract, are capitalised and amortised over the period "
                    "the benefit is transferred. For Northwind that period is "
                    "the expected customer relationship life of five years, "
                    "which is longer than the three-year contract term because "
                    "historical renewal rates support it. Commissions on "
                    "renewals at normal rates are amortised over the renewal "
                    "period.",
                    "Costs that would be incurred regardless of winning the "
                    "contract, such as bid team salaries and general marketing, "
                    "are expensed as incurred. A practical expedient allows "
                    "expensing of costs with an amortisation period of one year "
                    "or less, which Northwind applies to short-term incentive "
                    "payments."
                ],
                "qa": [
                    {
                        "question": "How is the core subscription recognised?",
                        "answer": "Ratably over the subscription term from the service start date.",
                    },
                    {
                        "question": "When is mandatory implementation revenue recognised?",
                        "answer": "Over the subscription term, because it is not distinct from the subscription.",
                    },
                    {
                        "question": "Over what period are incremental commissions amortised?",
                        "answer": "Five years, the expected customer relationship life.",
                    },
                ],
            },
        ],
        "qa": [
            {"question": "Over what period are sales commissions capitalised and amortised?",
             "answer": "Five years, the expected customer relationship life.",
             "evidence": "For Northwind that period is the expected customer relationship life of five years"},
            {"question": "What is the normal discount range for the core Northwind product?",
             "answer": "5 to 15 percent; a renewal discount above 15 percent is tested for a material right.",
             "evidence": "The normal discount range for the core product is 5 to 15 percent"},
            {"question": "When is optional training revenue recognised?",
             "answer": "As delivered, because it is a distinct performance obligation.",
             "evidence": "Optional training | Yes | As delivered"},
            {"question": "How often is the standalone selling price table refreshed?",
             "answer": "Twice a year, in January and July.",
             "evidence": "The SSP table is refreshed twice a year, in January and July"},
            {"question": "What discount on a bundle must be allocated proportionately across obligations?",
             "answer": "Any bundle discount, such as a 30 percent discount, must be allocated to all obligations proportionately rather than absorbed by one line.",
             "evidence": "the discount must be allocated to all obligations proportionately, not absorbed entirely by the services line"},
        ],
    },
    {
        "id": "FIN-STD-016",
        "title": "Month-End Close and Reporting Calendar",
        "doc_type": "Calendar",
        "category": "Finance",
        "department": "Finance Operations",
        "author": "Marcus Lindqvist, Director of Financial Reporting",
        "owner": "Finance Operations",
        "version": "2.8",
        "effective": "2026-01-01",
        "classification": "Confidential",
        "review": "Annual",
        "summary": (
            "The Northwind financial close calendar, listing the working-day "
            "tasks from close day 1 through reporting day 8, the owners of "
            "each task, the journal approval and materiality thresholds, and "
            "the rules for late entries and restatements."
        ),
        "tags": ["month end", "close", "journal entries", "reporting", "materiality", "calendar"],
        "sections": [
            {
                "heading": "Close Calendar",
                "paragraphs": [
                    "The Northwind close runs on working days after month end, "
                    "abbreviated WD. The target is a complete close pack by "
                    "WD5 and board reporting by WD8. The close is a hard "
                    "deadline: the reporting pack is distributed to the "
                    "Executive Staff at 16:00 Eastern on WD5 whether or not "
                    "every sub-ledger is reconciled, and unreconciled items are "
                    "listed as open items with an owner and a due date.",
                    "Sub-ledger owners must submit their reconciliation "
                    "evidence into the close management tool, not attach it to "
                    "an email, because the auditor samples from the tool. A "
                    "reconciliation without evidence in the tool is treated as "
                    "not performed."
                ],
                "table": [
                    ["Day", "Task", "Owner", "Hard deadline"],
                    ["WD1", "Sub-ledgers closed, AP and AR cut off", "Finance Operations", "12:00"],
                    ["WD2", "Intercompany eliminations, FX revaluation", "Group Accountant", "17:00"],
                    ["WD3", "Accruals, prepayments, deferred revenue roll-forward", "Financial Accounting", "17:00"],
                    ["WD4", "Balance sheet reconciliations complete, variance analysis drafted", "Controllers", "17:00"],
                    ["WD5", "Close pack issued to Executive Staff", "Financial Reporting", "16:00"],
                    ["WD6", "Management commentary and KPI pack", "FP&A", "17:00"],
                    ["WD8", "Board pack distributed", "CFO office", "12:00"],
                ],
            },
            {
                "heading": "Journal Entry Controls",
                "paragraphs": [
                    "Every manual journal above 50,000 USD requires a second "
                    "person's approval before posting, and journals above 500,000 "
                    "USD require a Controller. Journals posted by the same person "
                    "who approves them are blocked by system control. All manual "
                    "journals must carry a narrative explaining the business "
                    "reason, not only the account names, and must attach "
                    "supporting evidence.",
                    "Top-side journals, meaning adjustments made above the "
                    "sub-ledgers directly to the consolidation, are prohibited "
                    "except for consolidation eliminations and are reviewed by "
                    "the Controller every close. Late journals after WD5 require "
                    "the Controller's approval and are logged in the late entry "
                    "register, which the external auditor reviews."
                ],
                "bullets": [
                    "Manual journals above 50,000 USD need second-person approval.",
                    "Manual journals above 500,000 USD need a Controller.",
                    "Self-approval of journals is blocked by system control.",
                    "Late entries after WD5 are logged in a register the auditor reviews.",
                ],
            },
            {
                "heading": "Materiality",
                "paragraphs": [
                    "Planning materiality for the statutory accounts is set at "
                    "1 percent of revenue, which for the current year is "
                    "approximately 2.4 million USD. Performance materiality is "
                    "set at 75 percent of planning materiality. For management "
                    "reporting, the reporting threshold is much lower: any "
                    "variance above 250,000 USD or 10 percent against budget, "
                    "whichever is lower, requires written commentary from the "
                    "responsible controller.",
                    "An error discovered after a close is assessed against both "
                    "the current period and the cumulative effect on prior "
                    "periods. An error that would change a reported metric used "
                    "in a bonus calculation is escalated to the CFO regardless "
                    "of size, because it creates a conflict of interest in the "
                    "correction decision."
                ],
            },
            {
                "heading": "Restatement and Prior Period Errors",
                "paragraphs": [
                    "A prior period error is corrected retrospectively where it "
                    "is material, which means restating the comparative figures "
                    "rather than adjusting the current period. The decision that "
                    "an error is material is made by the Controller with the "
                    "CFO and is documented, including the quantitative and "
                    "qualitative reasoning. Qualitative factors can make a small "
                    "error material, notably where the error affects a "
                    "regulatory ratio, a debt covenant, or a segment result.",
                    "Where restated figures were previously communicated to "
                    "investors or lenders, Investor Relations and Legal must be "
                    "engaged before the restatement is finalised, and the "
                    "timing of any external communication is agreed with them."
                ],
                "qa": [
                    {
                        "question": "When is the close pack issued to the Executive Staff?",
                        "answer": "At 16:00 Eastern on working day 5 after month end.",
                    },
                    {
                        "question": "What is the approval threshold for manual journals?",
                        "answer": "Second-person approval above 50,000 USD and a Controller above 500,000 USD.",
                    },
                    {
                        "question": "What is planning materiality for the statutory accounts?",
                        "answer": "1 percent of revenue, approximately 2.4 million USD for the current year.",
                    },
                ],
            },
        ],
        "qa": [
            {"question": "By which working day must the close pack reach the Executive Staff?",
             "answer": "WD5, at 16:00 Eastern.",
             "evidence": "WD5 | Close pack issued to Executive Staff | Financial Reporting | 16:00"},
            {"question": "What is the manual journal value requiring a Controller's approval?",
             "answer": "500,000 USD.",
             "evidence": "journals above 500,000 USD require a Controller"},
            {"question": "What is planning materiality set at?",
             "answer": "1 percent of revenue, approximately 2.4 million USD.",
             "evidence": "Planning materiality for the statutory accounts is set at 1 percent of revenue, which for the current year is approximately 2.4 million USD"},
            {"question": "What variance triggers written commentary in management reporting?",
             "answer": "Any variance above 250,000 USD or 10 percent against budget, whichever is lower.",
             "evidence": "any variance above 250,000 USD or 10 percent against budget, whichever is lower"},
            {"question": "What percentage of planning materiality is performance materiality?",
             "answer": "75 percent.",
             "evidence": "Performance materiality is set at 75 percent of planning materiality"},
        ],
    },
    {
        "id": "FIN-HBK-022",
        "title": "Treasury and Cash Management Handbook",
        "doc_type": "Handbook",
        "category": "Finance",
        "department": "Treasury",
        "author": "Yusuf Demir, Treasurer",
        "owner": "Treasury",
        "version": "4.5",
        "effective": "2026-03-01",
        "classification": "Confidential",
        "review": "Semi-annual",
        "summary": (
            "Describes how Northwind manages bank accounts, cash pooling, "
            "foreign exchange exposure and hedging, counterparty limits, "
            "payment release controls and dual authorisation, and fraud "
            "controls including payment detail change verification."
        ),
        "tags": ["treasury", "cash pooling", "FX hedging", "counterparty limit", "payment controls", "fraud"],
        "sections": [
            {
                "heading": "Banking Structure",
                "paragraphs": [
                    "Northwind maintains 41 bank accounts across 14 currencies "
                    "with four relationship banks. New accounts require Treasury "
                    "approval and are opened only at a relationship bank; "
                    "opening an account without Treasury approval is a control "
                    "breach reported to the CFO. Dormant accounts, meaning no "
                    "movement for 180 days, are closed automatically after "
                    "notice to the account owner.",
                    "Cash is pooled through a notional pool in USD, EUR, and "
                    "GBP. The pool nets balances daily so that only the net "
                    "position is funded, which saves roughly 1.1 million USD of "
                    "interest per year against un-pooled balances. Minimum "
                    "operating cash for each operating entity is set at 15 days "
                    "of forecast operating outflow."
                ],
            },
            {
                "heading": "Foreign Exchange Exposure",
                "paragraphs": [
                    "Northwind's transaction exposure is dominated by EUR and "
                    "GBP costs against USD revenue. Treasury hedges forecast "
                    "highly probable exposures on a layered policy: 80 percent "
                    "of the next three months, 60 percent of months four to "
                    "six, and 40 percent of months seven to twelve. Hedge "
                    "instruments are plain vanilla forwards only; options and "
                    "speculative positions are prohibited.",
                    "Exposures are re-forecast monthly and the hedge book is "
                    "rebalanced on the first business day of each month. A "
                    "hedge that becomes ineffective is de-designated and the "
                    "gain or loss moves to the income statement, which Treasury "
                    "reports to the Audit Committee quarterly."
                ],
                "table": [
                    ["Currency", "Annual gross exposure", "Hedged at policy", "Instrument"],
                    ["EUR", "68 million USD", "80 / 60 / 40 percent layered", "Forward"],
                    ["GBP", "31 million USD", "80 / 60 / 40 percent layered", "Forward"],
                    ["CAD", "9 million USD", "Unhedged, below threshold", "None"],
                    ["SGD", "7 million USD", "50 percent, next 6 months", "Forward"],
                ],
            },
            {
                "heading": "Counterparty Limits",
                "paragraphs": [
                    "Counterparty credit limits are set by the Treasury Risk "
                    "Committee and reviewed quarterly, using the external rating "
                    "and the credit default swap spread. The limit for a "
                    "single-A rated bank is 50 million USD of daily exposure and "
                    "200 million USD of aggregate notional. Breaching a limit "
                    "requires immediate reporting to the Treasurer and unwinding "
                    "within two business days.",
                    "Investment of surplus cash is restricted to government "
                    "bills, overnight money market funds with a floating net "
                    "asset value only where the fund is government-only, and "
                    "term deposits within counterparty limits. Maximum "
                    "maturity is 90 days and no single instrument may exceed 20 "
                    "percent of total surplus cash."
                ],
                "bullets": [
                    "Single-A bank limit: 50 million USD daily exposure, 200 million USD aggregate notional.",
                    "Maximum investment maturity 90 days.",
                    "No single instrument above 20 percent of surplus cash.",
                    "Speculative FX and derivatives for profit are prohibited.",
                ],
            },
            {
                "heading": "Payment Controls and Fraud Prevention",
                "paragraphs": [
                    "All outbound payments require dual authorisation: a "
                    "preparer and an approver, who must be different people and "
                    "different devices. Payments above 100,000 USD require a "
                    "third authorisation from a Treasury authoriser. Payment "
                    "run files are released only from the Treasury workstation, "
                    "and the callback verification number used to confirm "
                    "changes is held offline.",
                    "The highest-risk fraud vector is a change to a supplier's "
                    "bank details. Any request to change beneficiary details is "
                    "verified by callback to a phone number already held on "
                    "file, never a number supplied in the request, and by email "
                    "confirmation to two known contacts. Changes take effect "
                    "only after a 24 hour cooling-off period during which the "
                    "first payment to new details is held.",
                    "Employees must report suspected payment fraud to Treasury "
                    "and Security within one hour of discovery. Northwind has "
                    "lost money to business email compromise in the past, and "
                    "the callback rule exists because of those losses."
                ],
                "qa": [
                    {
                        "question": "What authorisation does a payment above 100,000 USD need?",
                        "answer": "Dual authorisation plus a third authorisation from a Treasury authoriser.",
                    },
                    {
                        "question": "How is a supplier bank detail change verified?",
                        "answer": "By callback to a number already on file plus email confirmation to two known contacts, with a 24 hour cooling-off period.",
                    },
                    {
                        "question": "What is the hedging policy for months seven to twelve?",
                        "answer": "40 percent of the forecast exposure, using plain vanilla forwards.",
                    },
                ],
            },
        ],
        "qa": [
            {"question": "How many bank accounts does Northwind maintain?",
             "answer": "41 accounts across 14 currencies with four relationship banks.",
             "evidence": "Northwind maintains 41 bank accounts across 14 currencies with four relationship banks"},
            {"question": "What percentage of next-three-month FX exposure is hedged?",
             "answer": "80 percent, using plain vanilla forwards.",
             "evidence": "80 percent of the next three months, 60 percent of months four to six, and 40 percent of months seven to twelve"},
            {"question": "What is the maximum maturity for investing surplus cash?",
             "answer": "90 days.",
             "evidence": "Maximum maturity is 90 days"},
            {"question": "How long is the cooling-off period for new supplier payment details?",
             "answer": "24 hours, during which the first payment to new details is held.",
             "evidence": "a 24 hour cooling-off period during which the first payment to new details is held"},
            {"question": "What daily exposure limit applies to a single-A rated bank?",
             "answer": "50 million USD of daily exposure and 200 million USD aggregate notional.",
             "evidence": "The limit for a single-A rated bank is 50 million USD of daily exposure and 200 million USD of aggregate notional"},
        ],
    },
]
