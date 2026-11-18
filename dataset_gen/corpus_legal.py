"""Legal and compliance corpus (5 documents)."""

DOCS = [
    {
        "id": "LEG-POL-003",
        "title": "Privacy and Personal Data Protection Policy",
        "doc_type": "Policy",
        "category": "Legal and Compliance",
        "department": "Legal",
        "author": "Claire Beaumont, General Counsel",
        "owner": "Legal and Data Protection Office",
        "version": "6.1",
        "effective": "2026-01-01",
        "classification": "Internal",
        "review": "Annual",
        "summary": (
            "Establishes Northwind's privacy principles, lawful bases for "
            "processing, data subject rights and the response deadlines, "
            "international transfer mechanisms, records of processing, and the "
            "obligations of product teams when they introduce new personal data "
            "processing."
        ),
        "tags": ["privacy", "GDPR", "CCPA", "lawful basis", "DSAR", "transfers", "DPIA"],
        "sections": [
            {
                "heading": "Privacy Principles",
                "paragraphs": [
                    "Northwind processes personal data lawfully, fairly, and "
                    "transparently, only for specified and legitimate purposes, "
                    "minimally, accurately, for no longer than necessary, and "
                    "with appropriate security. Every processing activity must "
                    "have a documented lawful basis recorded in the Record of "
                    "Processing Activities before it begins. Retro-fitting a "
                    "basis after collection is not permitted.",
                    "The Data Protection Officer is independent of the business "
                    "and reports to the General Counsel. Any product or "
                    "business initiative that processes personal data in a new "
                    "way must consult the DPO at the design stage, not at "
                    "launch."
                ],
            },
            {
                "heading": "Lawful Bases in Practice",
                "paragraphs": [
                    "Most Northwind processing rests on contract necessity, "
                    "which covers delivering the service the customer bought, "
                    "or legitimate interests, which covers product analytics, "
                    "security monitoring, and fraud prevention. Legitimate "
                    "interests require a completed balancing test on file. "
                    "Consent is used only for marketing email and non-essential "
                    "cookies, and must be granular, freely given, and as easy "
                    "to withdraw as to give."
                ],
                "table": [
                    ["Processing activity", "Lawful basis", "Retention", "Balancing test on file"],
                    ["Service delivery to customer users", "Contract necessity", "Contract term plus 90 days", "Not required"],
                    ["Product analytics, aggregated", "Legitimate interests", "26 months", "DPA-BT-014"],
                    ["Security log retention", "Legitimate interests", "13 months", "DPA-BT-002"],
                    ["Marketing email", "Consent", "Until withdrawal plus 12 months", "Not required"],
                    ["Fraud and abuse prevention", "Legitimate interests", "7 years", "DPA-BT-021"],
                ],
            },
            {
                "heading": "Data Subject Rights",
                "paragraphs": [
                    "Access, rectification, erasure, restriction, portability, "
                    "and objection rights are honoured. Requests are verified "
                    "against the account record before any data is disclosed, "
                    "and identity verification may not request more data than "
                    "is needed. The response deadline is 30 calendar days from "
                    "receipt, extendable by a further 60 days where the request "
                    "is complex or numerous, provided the individual is told "
                    "within the first month.",
                    "Erasure is not absolute. Northwind refuses erasure where "
                    "an overriding obligation applies, most commonly financial "
                    "records retained for seven years, security logs retained "
                    "for 13 months, and data subject to a legal hold. A refusal "
                    "must state the reason and the right to complain to a "
                    "supervisory authority.",
                    "Requests are received at privacy@northwind.example and are "
                    "tracked in the Privacy Portal. The current median response "
                    "time is 14 days and the target is under 20 days."
                ],
                "bullets": [
                    "30 calendar days to respond, extendable by 60 days for complex requests.",
                    "Verification must not collect more data than necessary.",
                    "Erasure refused for financial records, security logs, and legal holds.",
                    "Refusals must state the reason and the right to complain.",
                ],
            },
            {
                "heading": "International Transfers",
                "paragraphs": [
                    "Personal data originating in the EEA, UK, or Switzerland "
                    "may be transferred only under a valid mechanism: an "
                    "adequacy decision, the EU Standard Contractual Clauses "
                    "module appropriate to the relationship, or the UK "
                    "International Data Transfer Agreement. Every transfer is "
                    "supported by a transfer risk assessment, and the "
                    "assessments are refreshed annually.",
                    "Northwind hosts EEA customer data in the eu-west-1 region "
                    "and does not replicate it outside the EEA except to the "
                    "Ireland support environment. Support engineers outside the "
                    "EEA access EEA data only through the privileged access "
                    "portal under a documented necessity test, and access is "
                    "logged and reviewed monthly."
                ],
                "notes": [
                    "Sub-processor note: the sub-processor list is published on "
                    "the Trust Portal. Adding a new sub-processor requires 30 "
                    "days' notice to customers who contracted for that right."
                ],
            },
            {
                "heading": "Product Obligations",
                "paragraphs": [
                    "Any feature that collects new personal data requires a "
                    "Data Protection Impact Assessment where the processing is "
                    "likely to result in a high risk, which includes profiling "
                    "with significant effects, large-scale processing of "
                    "special category data, systematic monitoring, and any use "
                    "of innovative technology including machine learning that "
                    "affects individuals. The DPIA must be complete before "
                    "development begins, and the DPO holds a veto on launch.",
                    "Privacy by design means default settings are the most "
                    "protective available, collection is limited to what the "
                    "feature needs, and retention is enforced by a job rather "
                    "than by policy alone. Features that cannot state a "
                    "retention period at design stage are not approved."
                ],
                "qa": [
                    {
                        "question": "How long do we have to respond to a data subject access request?",
                        "answer": "30 calendar days, extendable by 60 more days for complex or numerous requests.",
                    },
                    {
                        "question": "When is a DPIA required?",
                        "answer": "Where processing is likely to result in high risk, including significant profiling, large-scale special category data, systematic monitoring, or innovative technology affecting individuals.",
                    },
                    {
                        "question": "Which lawful basis covers product analytics?",
                        "answer": "Legitimate interests, with balancing test DPA-BT-014 on file.",
                    },
                ],
            },
        ],
        "qa": [
            {"question": "What is the deadline to respond to a data subject access request?",
             "answer": "30 calendar days from receipt, extendable by a further 60 days for complex or numerous requests.",
             "evidence": "The response deadline is 30 calendar days from receipt, extendable by a further 60 days"},
            {"question": "How long are product analytics records retained?",
             "answer": "26 months.",
             "evidence": "Product analytics, aggregated | Legitimate interests | 26 months"},
            {"question": "Where is EEA customer data hosted?",
             "answer": "In the eu-west-1 region, replicated only to the Ireland support environment.",
             "evidence": "hosts EEA customer data in the eu-west-1 region and does not replicate it outside the EEA except to the Ireland support environment"},
            {"question": "What is the current median DSAR response time?",
             "answer": "14 days, against a target of under 20 days.",
             "evidence": "The current median response time is 14 days and the target is under 20 days"},
            {"question": "Which lawful basis covers marketing email?",
             "answer": "Consent, which must be granular, freely given, and as easy to withdraw as to give.",
             "evidence": "Marketing email | Consent | Until withdrawal plus 12 months"},
        ],
    },
    {
        "id": "LEG-STD-007",
        "title": "Commercial Contracting and Signature Authority Standard",
        "doc_type": "Standard",
        "category": "Legal and Compliance",
        "department": "Legal",
        "author": "Claire Beaumont, General Counsel",
        "owner": "Legal",
        "version": "4.3",
        "effective": "2026-02-15",
        "classification": "Internal",
        "review": "Annual",
        "summary": (
            "Sets out who may sign for Northwind and up to what value, the "
            "mandatory clauses in customer and supplier agreements, the "
            "negotiation playbook and approved deviation ranges, the legal "
            "review triggers, and the contract lifecycle obligations for "
            "renewals and terminations."
        ),
        "tags": ["contracts", "signature authority", "indemnity", "liability cap", "renewal", "playbook"],
        "sections": [
            {
                "heading": "Signature Authority",
                "paragraphs": [
                    "Only named signatories may bind Northwind, and authority is "
                    "limited by value and by clause type. A sales director may "
                    "sign a standard-form order form up to 250,000 USD total "
                    "contract value. Above that, the VP of Sales and the General "
                    "Counsel must both sign. Any agreement containing a "
                    "liability cap above the approved range, an uncapped "
                    "indemnity, a change of control termination right, or an "
                    "audit right broader than the standard requires the General "
                    "Counsel regardless of value.",
                    "Signing without authority is a disciplinary matter. Where a "
                    "counterparty has been told that a person can sign and they "
                    "cannot, Legal must be notified immediately so the position "
                    "can be corrected before reliance builds."
                ],
                "table": [
                    ["Role", "Standard form limit", "Negotiated form limit", "May approve non-standard IP terms"],
                    ["Sales Director", "250,000 USD", "Not permitted", "No"],
                    ["VP Sales", "1,000,000 USD", "500,000 USD", "No"],
                    ["General Counsel", "Unlimited", "Unlimited", "Yes"],
                    ["CFO", "Unlimited for finance matters", "Unlimited", "No"],
                    ["CEO", "Unlimited", "Unlimited", "Yes"],
                ],
            },
            {
                "heading": "Mandatory Clauses",
                "paragraphs": [
                    "Customer agreements must contain the data processing "
                    "agreement where personal data is processed, a service "
                    "credit schedule tied to the published availability "
                    "commitment, a limitation of liability capped at 12 months "
                    "of fees, a customer obligation not to circumvent licence "
                    "metrics, and a governing law of either Delaware or England "
                    "and Wales. Supplier agreements must contain the security "
                    "schedule, breach notification within 24 hours, audit "
                    "rights, and data return and destruction on termination.",
                    "The following are prohibited and cannot be agreed by any "
                    "signatory without board approval: unlimited or uncapped "
                    "liability, indemnity for the counterparty's own "
                    "negligence, assignment of Northwind foreground IP, "
                    "most-favoured-customer pricing, and any clause giving a "
                    "counterparty the right to audit Northwind's source code."
                ],
                "bullets": [
                    "Liability cap: 12 months of fees paid, with carve-outs for IP infringement and confidentiality breach.",
                    "Availability commitment: 99.9 percent monthly, measured excluding notifiable maintenance.",
                    "Service credits capped at 20 percent of the monthly fee.",
                    "Governing law: Delaware or England and Wales only.",
                ],
            },
            {
                "heading": "Negotiation Playbook",
                "paragraphs": [
                    "The Commercial Playbook states the opening position, the "
                    "approved fallback, and the escalation trigger for 62 "
                    "commonly negotiated clauses. Sales teams may agree anything "
                    "within the approved fallback without Legal review, which is "
                    "what makes the median enterprise deal close in 11 business "
                    "days. Anything outside the fallback routes to Legal with a "
                    "two business day service level for standard escalations.",
                    "The three clauses most often escalated are liability caps, "
                    "data residency, and termination for convenience. The "
                    "approved position on termination for convenience is 90 days "
                    "notice with payment of fees already committed; a "
                    "termination right with no payment is escalated to the "
                    "General Counsel."
                ],
            },
            {
                "heading": "Contract Lifecycle",
                "paragraphs": [
                    "Every contract lives in the Contract Lifecycle Management "
                    "system, which is the system of record. Contracts held only "
                    "in email are not enforceable in practice because no one "
                    "knows the renewal date. Auto-renewal clauses require a "
                    "reminder to the account owner 90 days before the notice "
                    "deadline, and the account owner must record a decision.",
                    "Contracts with an auto-renewal that were not reviewed "
                    "before the notice deadline are reported monthly to the CFO "
                    "as unplanned commitments. Termination notices must be sent "
                    "by the method stated in the contract, which is usually "
                    "registered post to a named address, and Legal must confirm "
                    "the method before it is used."
                ],
                "qa": [
                    {
                        "question": "What is the standard liability cap?",
                        "answer": "12 months of fees paid, with carve-outs for IP infringement and confidentiality breach.",
                    },
                    {
                        "question": "Up to what value may a Sales Director sign a standard form?",
                        "answer": "250,000 USD total contract value.",
                    },
                    {
                        "question": "How far ahead must an auto-renewal be flagged?",
                        "answer": "90 days before the notice deadline, with a recorded decision by the account owner.",
                    },
                ],
            },
        ],
        "qa": [
            {"question": "What is Northwind's standard limitation of liability cap?",
             "answer": "12 months of fees paid.",
             "evidence": "a limitation of liability capped at 12 months of fees"},
            {"question": "What is the maximum service credit exposure per month?",
             "answer": "20 percent of the monthly fee.",
             "evidence": "Service credits capped at 20 percent of the monthly fee"},
            {"question": "Which governing law jurisdictions are permitted?",
             "answer": "Delaware or England and Wales.",
             "evidence": "a governing law of either Delaware or England and Wales"},
            {"question": "How many clauses does the Commercial Playbook cover?",
             "answer": "62 commonly negotiated clauses.",
             "evidence": "the approved fallback, and the escalation trigger for 62 commonly negotiated clauses"},
            {"question": "Within how many hours must a supplier notify Northwind of a breach?",
             "answer": "24 hours.",
             "evidence": "breach notification within 24 hours"},
        ],
    },
    {
        "id": "LEG-STD-012",
        "title": "Intellectual Property and Open Source Policy",
        "doc_type": "Policy",
        "category": "Legal and Compliance",
        "department": "Legal",
        "author": "Priya Anand, Senior Counsel, Technology",
        "owner": "Legal and Engineering",
        "version": "5.0",
        "effective": "2026-04-01",
        "classification": "Internal",
        "review": "Annual",
        "summary": (
            "Governs ownership of work created at Northwind, the open source "
            "licence categories permitted in Northwind code, the approval "
            "process for new dependencies, obligations when distributing "
            "licensed code, and the rules for contributing to and releasing "
            "open source projects."
        ),
        "tags": ["intellectual property", "open source", "licence", "copyleft", "GPL", "contributions"],
        "sections": [
            {
                "heading": "Ownership of Work Product",
                "paragraphs": [
                    "Everything created by an employee in the course of "
                    "employment, and everything created by a contractor under a "
                    "Northwind agreement, is owned by Northwind as work made for "
                    "hire, supported by an assignment. Employees must disclose "
                    "inventions through the Invention Disclosure form, which "
                    "also covers work done on personal time if it relates to "
                    "Northwind's business or was made using Northwind resources.",
                    "Pre-existing IP brought into a project must be declared "
                    "before it is used, using the Pre-Existing IP register, so "
                    "that ownership boundaries stay clear. Contributions to "
                    "personal open source projects are permitted where they are "
                    "outside working hours, use no Northwind resources, do not "
                    "compete with Northwind, and do not incorporate Northwind "
                    "confidential information."
                ],
            },
            {
                "heading": "Open Source Licence Categories",
                "paragraphs": [
                    "Dependencies are classified green, amber, or red. Green "
                    "licences may be used freely in all distributions. Amber "
                    "licences require review of the specific use case because "
                    "obligations may be triggered by how the code is linked or "
                    "distributed. Red licences are prohibited in distributed "
                    "product code and require Legal approval even for internal "
                    "use.",
                    "The classification is enforced automatically by the "
                    "dependency scanner in CI, which blocks a build that "
                    "introduces a red licence. Amber approvals are recorded "
                    "against the specific repository and version, and do not "
                    "extend to other repositories."
                ],
                "table": [
                    ["Category", "Example licences", "Permitted use", "Approval"],
                    ["Green", "MIT, BSD-2, BSD-3, Apache-2.0, ISC", "All uses including distributed product code", "None"],
                    ["Amber", "LGPL-2.1, MPL-2.0, EPL-2.0, CDDL-1.0", "Dynamic linking, internal use, review required", "Legal review"],
                    ["Red", "GPL-2.0, GPL-3.0, AGPL-3.0, SSPL, CC-BY-NC", "Prohibited in product; internal-only with approval", "General Counsel"],
                    ["Unknown", "No licence file, or custom terms", "Prohibited", "Not permitted without a licence"],
                ],
            },
            {
                "heading": "Obligations When Distributing",
                "paragraphs": [
                    "Distributing software that contains open source triggers "
                    "attribution and, for some licences, source availability "
                    "obligations. Every release that leaves Northwind's control, "
                    "including on-premises appliances and desktop installers, "
                    "must ship a notice file listing all open source components, "
                    "their licences, and copyright notices, plus a written offer "
                    "or a URL for source where the licence requires it.",
                    "Server-hosted software that the customer never receives is "
                    "generally not distribution, which is why AGPL is treated "
                    "differently from GPL: AGPL's network clause can trigger "
                    "source obligations even for hosted use. Any AGPL dependency "
                    "in a hosted service requires General Counsel approval."
                ],
                "bullets": [
                    "Every distributed release ships a NOTICE file and licence texts.",
                    "The SBOM is generated automatically and reviewed before release.",
                    "AGPL in a hosted service requires General Counsel approval.",
                    "Unknown or missing licences are prohibited outright.",
                ],
            },
            {
                "heading": "Contributing and Releasing Open Source",
                "paragraphs": [
                    "Employees may contribute fixes upstream to projects "
                    "Northwind depends on, and are encouraged to, provided the "
                    "contribution contains no confidential information and is "
                    "made under the Corporate Contributor Licence Agreement "
                    "where the project requires one. Contributions must be "
                    "reviewed by the team's technical lead before submission.",
                    "Releasing a new Northwind open source project requires "
                    "approval from the Open Source Review Board, which checks "
                    "trademark clearance, the licence choice, dependency "
                    "hygiene, security review, and a named maintainer with a "
                    "documented support expectation. Unmaintained public "
                    "projects damage Northwind's reputation and are archived "
                    "rather than left abandoned."
                ],
                "qa": [
                    {
                        "question": "Which licence category is Apache-2.0?",
                        "answer": "Green, permitted in all uses including distributed product code with no approval.",
                    },
                    {
                        "question": "Why is AGPL treated differently from GPL?",
                        "answer": "Because AGPL's network clause can trigger source obligations even for hosted use where no distribution occurs.",
                    },
                    {
                        "question": "Who must approve releasing a new open source project?",
                        "answer": "The Open Source Review Board.",
                    },
                ],
            },
        ],
        "qa": [
            {"question": "Which licence category covers MIT and Apache-2.0?",
             "answer": "Green, permitted in all uses with no approval required.",
             "evidence": "Green | MIT, BSD-2, BSD-3, Apache-2.0, ISC | All uses including distributed product code | None"},
            {"question": "Who must approve an AGPL dependency in a hosted service?",
             "answer": "The General Counsel.",
             "evidence": "Any AGPL dependency in a hosted service requires General Counsel approval"},
            {"question": "What must every distributed release ship regarding open source?",
             "answer": "A notice file listing all open source components, licences and copyright notices, plus a source offer where required.",
             "evidence": "must ship a notice file listing all open source components, their licences, and copyright notices"},
            {"question": "Who approves releasing a new Northwind open source project?",
             "answer": "The Open Source Review Board.",
             "evidence": "Releasing a new Northwind open source project requires approval from the Open Source Review Board"},
            {"question": "What licence categories are prohibited in distributed product code?",
             "answer": "Red licences, including GPL-2.0, GPL-3.0, AGPL-3.0, SSPL, and CC-BY-NC, plus any unknown or missing licence.",
             "evidence": "Red | GPL-2.0, GPL-3.0, AGPL-3.0, SSPL, CC-BY-NC | Prohibited in product"},
        ],
    },
    {
        "id": "LEG-STD-018",
        "title": "Records Retention and Legal Hold Standard",
        "doc_type": "Standard",
        "category": "Legal and Compliance",
        "department": "Legal Operations",
        "author": "Thomas Whitaker, Head of Legal Operations",
        "owner": "Legal",
        "version": "3.6",
        "effective": "2026-05-01",
        "classification": "Confidential",
        "review": "Annual",
        "summary": (
            "Sets the Northwind retention schedule by record category, the "
            "process for issuing, maintaining, and releasing a legal hold, the "
            "obligations of custodians, the suspension of routine destruction, "
            "and the consequences of spoliation."
        ),
        "tags": ["records retention", "legal hold", "litigation", "spoliation", "custodian", "destruction"],
        "sections": [
            {
                "heading": "Retention Schedule",
                "paragraphs": [
                    "Records are retained for the period set in the Retention "
                    "Schedule and destroyed at the end of that period "
                    "automatically. Retention is a legal obligation, not a "
                    "convenience, and keeping records longer than the schedule "
                    "is itself a violation because it increases discovery "
                    "burden and exposure. Destruction must be evidenced.",
                    "The clock usually starts at the end of the relevant "
                    "transaction rather than at creation, for example at "
                    "contract end rather than contract signature."
                ],
                "table": [
                    ["Record category", "Retention", "Trigger", "Owner"],
                    ["Financial ledgers and supporting records", "7 years", "End of fiscal year", "Finance"],
                    ["Customer contracts", "7 years", "Contract end", "Legal"],
                    ["Employee personnel files", "6 years after separation", "Separation date", "People Operations"],
                    ["Payroll records", "7 years", "End of fiscal year", "Payroll"],
                    ["Security and access logs", "13 months", "Log creation", "Security Operations"],
                    ["Incident evidence", "7 years", "Incident closure", "Security Operations"],
                    ["Support tickets with personal data", "24 months, then anonymised", "Ticket close", "Customer Success"],
                    ["Board minutes and resolutions", "Permanent", "Date of meeting", "Corporate Secretary"],
                ],
            },
            {
                "heading": "Issuing a Legal Hold",
                "paragraphs": [
                    "A legal hold is issued by Legal when litigation is "
                    "reasonably anticipated, when a regulator makes a request, "
                    "or when an internal investigation opens. The hold notice "
                    "names the matter, describes the subject scope in plain "
                    "language, lists the custodians, and states the systems in "
                    "scope. Holds are issued within two business days of the "
                    "triggering event.",
                    "On issue, routine destruction is suspended for the "
                    "identified custodians and systems, including backup "
                    "rotation where technically feasible, and the suspension is "
                    "recorded in the Hold Management system. Suspending "
                    "destruction globally is avoided because it is disproportionate; "
                    "the hold should be as narrow as the matter allows."
                ],
                "bullets": [
                    "Hold issued within 2 business days of the triggering event.",
                    "Notice names the matter, scope, custodians, and systems.",
                    "Custodians must acknowledge within 5 business days.",
                    "Custodians must self-report additional sources they control.",
                    "Holds are re-issued and re-acknowledged every 90 days.",
                ],
            },
            {
                "heading": "Custodian Obligations",
                "paragraphs": [
                    "A custodian is anyone who controls potentially relevant "
                    "material. Custodians must preserve, not curate: they may "
                    "not delete, edit, or tidy material, and must not delete "
                    "messages, calendar entries, or files even where obviously "
                    "irrelevant. Where a custodian is unsure whether something "
                    "is in scope, they preserve it and ask Legal.",
                    "Custodians must confirm preservation in writing within "
                    "five business days and must disclose every system holding "
                    "relevant material, including personal devices used for "
                    "work, messaging apps, and personal email if used for "
                    "business. Failure to preserve can expose Northwind to "
                    "sanctions for spoliation, including adverse inference "
                    "instructions and default judgment."
                ],
                "notes": [
                    "Spoliation is the most avoidable litigation risk. Every "
                    "sanction Northwind has faced in the past decade arose from "
                    "a custodian deleting material after a hold was issued."
                ],
            },
            {
                "heading": "Releasing a Hold",
                "paragraphs": [
                    "A hold is released in writing by the issuing lawyer when "
                    "the matter concludes, and the release notice tells "
                    "custodians that routine destruction resumes under the "
                    "schedule. Custodians must not resume destruction on the "
                    "assumption that a matter has ended; only the written "
                    "release authorises it.",
                    "Released holds are archived with the notice, the "
                    "acknowledgements, and the evidence of resumed destruction. "
                    "Legal Operations audits five closed matters per year to "
                    "confirm that preservation was maintained for the full "
                    "period and that no deletion occurred during the hold."
                ],
                "qa": [
                    {
                        "question": "How quickly must a legal hold be issued?",
                        "answer": "Within two business days of the triggering event.",
                    },
                    {
                        "question": "How often must holds be re-acknowledged?",
                        "answer": "Every 90 days.",
                    },
                    {
                        "question": "When may a custodian resume deleting material?",
                        "answer": "Only after a written release from the issuing lawyer.",
                    },
                ],
            },
        ],
        "qa": [
            {"question": "How long are financial records retained?",
             "answer": "7 years from the end of the fiscal year.",
             "evidence": "Financial ledgers and supporting records | 7 years | End of fiscal year"},
            {"question": "How long are security and access logs retained?",
             "answer": "13 months.",
             "evidence": "Security and access logs | 13 months | Log creation"},
            {"question": "Within how many business days must a custodian acknowledge a legal hold?",
             "answer": "5 business days.",
             "evidence": "Custodians must acknowledge within 5 business days"},
            {"question": "How often are active legal holds re-issued for re-acknowledgement?",
             "answer": "Every 90 days.",
             "evidence": "Holds are re-issued and re-acknowledged every 90 days"},
            {"question": "How long are board minutes retained?",
             "answer": "Permanently.",
             "evidence": "Board minutes and resolutions | Permanent"},
        ],
    },
    {
        "id": "LEG-STD-024",
        "title": "Anti-Bribery, Gifts and Hospitality Standard",
        "doc_type": "Standard",
        "category": "Legal and Compliance",
        "department": "Compliance",
        "author": "Amadou Diallo, Chief Compliance Officer",
        "owner": "Compliance",
        "version": "4.1",
        "effective": "2026-01-01",
        "classification": "Internal",
        "review": "Annual",
        "summary": (
            "Implements Northwind's anti-bribery obligations. Defines prohibited "
            "payments and facilitation payments, the gift and hospitality "
            "thresholds and register, rules on government officials and "
            "political contributions, due diligence on intermediaries, and the "
            "approval and reporting workflow."
        ),
        "tags": ["anti-bribery", "FCPA", "gifts", "hospitality", "facilitation payment", "due diligence"],
        "sections": [
            {
                "heading": "Core Prohibitions",
                "paragraphs": [
                    "Northwind prohibits bribery in any form, including "
                    "offering, promising, giving, requesting, or accepting an "
                    "advantage to obtain or retain business or a business "
                    "advantage. The prohibition covers both public officials and "
                    "private sector counterparties, and applies to conduct by "
                    "third parties acting for Northwind, which is where most of "
                    "the real risk sits.",
                    "Facilitation payments, meaning small payments to secure a "
                    "routine government action such as clearing goods through "
                    "customs, are prohibited without exception. Employees under "
                    "duress, including where personal safety is threatened, "
                    "should protect their safety first and report the payment to "
                    "Compliance within 24 hours; the report is the protection."
                ],
            },
            {
                "heading": "Gifts and Hospitality Thresholds",
                "paragraphs": [
                    "Gifts and hospitality must be reasonable, infrequent, "
                    "transparent, and never given at a point where a decision is "
                    "pending. Anything intended to influence a decision is "
                    "prohibited regardless of value. All gifts and hospitality "
                    "involving a public official, or any value above the "
                    "register threshold, must be recorded in the Gifts and "
                    "Hospitality Register before the event where practicable."
                ],
                "table": [
                    ["Situation", "Threshold", "Approval", "Register entry"],
                    ["Gift to a private sector contact", "Up to 100 USD per year per recipient", "Line manager", "Required above 50 USD"],
                    ["Hospitality to a private sector contact", "Up to 200 USD per event", "Line manager", "Required above 100 USD"],
                    ["Any gift to a public official", "Any value", "Compliance, in advance", "Always required"],
                    ["Any hospitality to a public official", "Any value", "Compliance, in advance", "Always required"],
                    ["Travel or accommodation for a counterparty", "Any value", "Compliance, in advance", "Always required"],
                ],
            },
            {
                "heading": "Government Officials and Political Contributions",
                "paragraphs": [
                    "A public official is interpreted broadly and includes "
                    "employees of state-owned enterprises, public hospitals, "
                    "state universities, regulators, political parties, and "
                    "candidates, as well as their family members and close "
                    "associates. Employees must check the counterparty against "
                    "the government ownership register before offering anything "
                    "of value, because a customer that appears private may be "
                    "state-controlled.",
                    "Northwind makes no political contributions of any kind, "
                    "including charitable donations that a political figure "
                    "controls, and no sponsorship of political events. Charitable "
                    "donations must be routed through the Northwind Foundation "
                    "and may never be requested by, or directed to, a customer "
                    "or official as a condition of a deal."
                ],
                "bullets": [
                    "No facilitation payments, with a 24-hour duress reporting route.",
                    "No political contributions of any kind.",
                    "Charitable donations only through the Northwind Foundation.",
                    "No sponsorship of personal development or travel for officials.",
                    "Third-party intermediaries require documented due diligence before engagement.",
                ],
            },
            {
                "heading": "Third-Party Due Diligence",
                "paragraphs": [
                    "Intermediaries such as resellers, agents, consultants, and "
                    "customs brokers present the largest bribery exposure. "
                    "Before engagement, the sponsor must complete risk screening "
                    "covering beneficial ownership, government connections, "
                    "sanctions and adverse media, and the reason the third party "
                    "is needed. High-risk intermediaries additionally require a "
                    "site visit or interview and Compliance sign-off.",
                    "Contracts with intermediaries must include anti-bribery "
                    "representations, audit rights, a right to terminate for "
                    "breach, and a prohibition on sub-agents without consent. "
                    "Commission rates materially above the market range are a "
                    "red flag and must be justified in writing by the sponsor."
                ],
                "notes": [
                    "Red flags to escalate: a request for payment to an "
                    "unrelated third party or offshore account, refusal to "
                    "sign anti-bribery terms, an unexplained personal "
                    "relationship with the customer's decision maker, and an "
                    "invoice with no description of services."
                ],
            },
            {
                "heading": "Training, Reporting and Consequences",
                "paragraphs": [
                    "All employees complete anti-bribery training on joining and "
                    "annually. Sales, procurement, and any role that engages "
                    "intermediaries in a high-risk jurisdiction complete "
                    "advanced training every year. Completion is reported to the "
                    "Audit Committee and non-completion blocks system access "
                    "renewal.",
                    "Concerns are reported to Compliance at "
                    "compliance@northwind.example or to the Ethics Line, which "
                    "accepts anonymous reports. Retaliation is prohibited. "
                    "Breaches may result in dismissal, contract termination, "
                    "recovery of incentive payments, and referral to authorities."
                ],
                "qa": [
                    {
                        "question": "Are facilitation payments ever permitted?",
                        "answer": "No. They are prohibited without exception, with a 24-hour reporting route where an employee acted under duress.",
                    },
                    {
                        "question": "What approval is needed to give a gift to a public official?",
                        "answer": "Advance approval from Compliance, regardless of value, plus a register entry.",
                    },
                    {
                        "question": "What commission treatment is a red flag for an intermediary?",
                        "answer": "A rate materially above the market range, which must be justified in writing by the sponsor.",
                    },
                ],
            },
        ],
        "qa": [
            {"question": "What is the gift threshold for a private sector contact per year?",
             "answer": "Up to 100 USD per year per recipient, with register entry required above 50 USD.",
             "evidence": "Gift to a private sector contact | Up to 100 USD per year per recipient | Line manager | Required above 50 USD"},
            {"question": "How quickly must a payment made under duress be reported?",
             "answer": "Within 24 hours to Compliance.",
             "evidence": "report the payment to Compliance within 24 hours"},
            {"question": "Does Northwind allow political contributions?",
             "answer": "No. Northwind makes no political contributions of any kind.",
             "evidence": "Northwind makes no political contributions of any kind"},
            {"question": "What is the hospitality threshold per event for a private sector contact?",
             "answer": "Up to 200 USD per event, with register entry required above 100 USD.",
             "evidence": "Hospitality to a private sector contact | Up to 200 USD per event"},
            {"question": "Which roles must complete advanced anti-bribery training annually?",
             "answer": "Sales, procurement, and any role that engages intermediaries in a high-risk jurisdiction.",
             "evidence": "Sales, procurement, and any role that engages intermediaries in a high-risk jurisdiction complete advanced training every year"},
        ],
    },
]
