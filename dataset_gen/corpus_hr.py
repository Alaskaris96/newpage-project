"""Human Resources corpus (5 documents).

Every document is set inside Northwind Consolidated Holdings (NCH) so that
cross-document retrieval questions have consistent answers.
"""

COMPANY = "Northwind Consolidated Holdings"

DOCS = [
    {
        "id": "HR-POL-001",
        "title": "Remote and Hybrid Work Policy",
        "doc_type": "Policy",
        "category": "Human Resources",
        "department": "People Operations",
        "author": "Dana Whitfield, Director of People Operations",
        "owner": "People Operations",
        "version": "4.1",
        "effective": "2026-02-01",
        "classification": "Internal",
        "review": "Annual",
        "summary": (
            "This policy defines the three work modes available to Northwind "
            "Consolidated Holdings employees, the approval path for each mode, "
            "the anchor-day requirements for hybrid staff, the equipment and "
            "reimbursement allowances attached to each mode, and the "
            "performance and safety obligations that apply when work is "
            "performed outside a Northwind facility."
        ),
        "tags": ["remote work", "hybrid", "anchor days", "home office stipend", "WFO"],
        "sections": [
            {
                "heading": "Purpose and Scope",
                "paragraphs": [
                    "Northwind Consolidated Holdings operates a hybrid-first "
                    "working model. The model exists to give employees "
                    "predictable control over where they work while preserving "
                    "the in-person collaboration that product, hardware, and "
                    "customer-facing teams depend on. This policy applies to "
                    "all regular full-time and part-time employees of "
                    "Northwind Consolidated Holdings in every region. It does "
                    "not apply to contractors, vendors, or staff of acquired "
                    "entities still operating under a legacy handbook, although "
                    "managers may extend these terms voluntarily.",
                    "The policy covers three work modes: Work From Office "
                    "(WFO), Hybrid, and Fully Remote. An employee's work mode "
                    "is recorded in Workday under Position Data and is treated "
                    "as a term of employment for tax and immigration purposes. "
                    "Changing a work mode is therefore a formal change, not an "
                    "informal arrangement between a manager and an employee."
                ],
            },
            {
                "heading": "Work Modes",
                "paragraphs": [
                    "Work From Office employees work on site five days per "
                    "week. Hybrid employees work on site a minimum of two "
                    "days per week, measured as a rolling four-week average "
                    "rather than a weekly quota, which allows a heavy travel "
                    "week to be balanced against a lighter one. Fully Remote "
                    "employees work off site permanently and are expected to "
                    "attend at least one on-site gathering per quarter, plus "
                    "any all-hands event designated as mandatory by the "
                    "Executive Staff."
                ],
                "table": [
                    ["Work mode", "On-site minimum", "Approval required", "Home office stipend"],
                    ["Work From Office", "5 days per week", "Hiring manager", "$0"],
                    ["Hybrid", "2 days per week (4-week rolling average)", "Hiring manager and department head", "$600 one-off, refreshed every 24 months"],
                    ["Fully Remote", "1 on-site day per quarter", "Department head and VP of People Operations", "$1,200 one-off, refreshed every 24 months"],
                ],
            },
            {
                "heading": "Anchor Days",
                "paragraphs": [
                    "Hybrid teams publish anchor days, which are the days the "
                    "whole team is expected to be on site. Anchor days are set "
                    "at team level by the team's manager and must be published "
                    "in the team calendar at least two weeks in advance. The "
                    "default anchor days for Northwind Columbus are Tuesday and "
                    "Thursday; the default for the Austin office is Wednesday. "
                    "Anchor days may be waived for documented caregiving "
                    "obligations, medical accommodations, or approved leave, "
                    "and a waiver must never reduce an employee's "
                    "performance rating.",
                    "Managers are responsible for monitoring the rolling "
                    "average through the Badge Activity report in the People "
                    "Operations dashboard. Persistent under-attendance, defined "
                    "as two consecutive four-week windows below the minimum "
                    "without an approved waiver, is handled as a performance "
                    "conversation under the Performance Management Standard, "
                    "not as a disciplinary matter."
                ],
                "bullets": [
                    "Anchor days are team-level, not company-level, and must be published two weeks ahead.",
                    "Attendance is measured as a rolling four-week average using badge data.",
                    "Approved waivers do not count toward the on-site minimum but never count against the employee.",
                    "Client-facing travel days count as on-site days only when the client site is a Northwind facility.",
                ],
            },
            {
                "heading": "Cross-Border and Tax Restrictions",
                "paragraphs": [
                    "Fully Remote employees must reside in a country where "
                    "Northwind holds an employer of record entity or a "
                    "registered legal entity. As of the effective date, those "
                    "countries are the United States, Canada, the United "
                    "Kingdom, Ireland, Germany, the Netherlands, Australia, and "
                    "Singapore. Employees in other countries may be onboarded "
                    "only through the approved employer-of-record partner, "
                    "Deel, and only after Global Mobility issues a written "
                    "clearance.",
                    "Remote employees may work from a different country for up "
                    "to 30 calendar days per rolling twelve months without "
                    "clearance, provided the role is not security-cleared and "
                    "does not touch production customer data. Beyond 30 days, "
                    "the manager must file a Work Location Change request and "
                    "Global Mobility has a service-level target of ten "
                    "business days to respond. Working from a restricted "
                    "jurisdiction without clearance is a Category 2 "
                    "compliance violation."
                ],
                "notes": [
                    "Tax note: a work-location change can create a permanent "
                    "establishment risk. Payroll must be notified before the "
                    "change takes effect, not after."
                ],
            },
            {
                "heading": "Equipment, Connectivity, and Safety",
                "paragraphs": [
                    "Northwind issues one primary laptop and, where the role "
                    "requires it, one monitor and docking station to Hybrid and "
                    "Fully Remote employees. The home office stipend covers "
                    "everything else: chair, desk, desk lamp, webcam, headset, "
                    "and broadband upgrade. Claims are filed in Concur under "
                    "expense type HOME-OFFICE and require a receipt; claims "
                    "above the stipend cap are rejected automatically rather "
                    "than routed for exception approval.",
                    "Employees working remotely must use a company-managed "
                    "device with full-disk encryption and the Northwind VPN "
                    "profile, must not work with customer data in public "
                    "spaces, and must report loss or theft of any device "
                    "within four hours to the Security Operations Center. "
                    "Managers hold a documented ergonomic self-assessment for "
                    "each remote direct report once per year."
                ],
                "qa": [
                    {
                        "question": "How many on-site days per week does a hybrid employee need?",
                        "answer": "A minimum of two days per week, measured as a rolling four-week average rather than a strict weekly quota.",
                    },
                    {
                        "question": "What is the fully remote home office stipend?",
                        "answer": "$1,200 as a one-off payment, refreshed every 24 months.",
                    },
                    {
                        "question": "Who must approve a fully remote work mode?",
                        "answer": "The department head and the VP of People Operations.",
                    },
                ],
            },
            {
                "heading": "Related Documents",
                "paragraphs": [
                    "This policy should be read with the Performance Management "
                    "Standard (HR-STD-004), the Information Security Acceptable "
                    "Use Policy (SEC-POL-002), and the Global Mobility "
                    "Handbook (HR-HBK-011). Where this policy and another "
                    "document conflict on a matter of security, the security "
                    "document governs; on all other matters this policy governs."
                ],
            },
        ],
        "qa": [
            {"question": "How many on-site days per week are required of a hybrid Northwind employee?",
             "answer": "Two days per week minimum, measured as a rolling four-week average.",
             "evidence": "Hybrid employees work on site a minimum of two days per week, measured as a rolling four-week average"},
            {"question": "What one-off home office stipend does a fully remote employee receive?",
             "answer": "$1,200, refreshed every 24 months.",
             "evidence": "$1,200 one-off, refreshed every 24 months"},
            {"question": "Which roles must approve a change to Fully Remote work mode?",
             "answer": "The department head and the VP of People Operations.",
             "evidence": "Department head and VP of People Operations"},
            {"question": "How many days per year may a remote employee work from another country without clearance?",
             "answer": "Up to 30 calendar days per rolling twelve months.",
             "evidence": "up to 30 calendar days per rolling twelve months without clearance"},
            {"question": "What are the default anchor days for the Columbus office?",
             "answer": "Tuesday and Thursday.",
             "evidence": "The default anchor days for Northwind Columbus are Tuesday and Thursday"},
        ],
    },
    {
        "id": "HR-STD-004",
        "title": "Performance Management Standard",
        "doc_type": "Standard",
        "category": "Human Resources",
        "department": "People Operations",
        "author": "Marcus Oyelaran, Head of Talent Development",
        "owner": "People Operations",
        "version": "6.0",
        "effective": "2026-01-01",
        "classification": "Internal",
        "review": "Annual",
        "summary": (
            "Defines the Northwind performance cycle, the five-point rating "
            "scale and its calibration distribution guidance, the "
            "goal-setting rules, the rules for written feedback and "
            "performance improvement plans, and the link between ratings and "
            "merit increases and bonuses."
        ),
        "tags": ["performance", "ratings", "calibration", "PIP", "merit increase", "goal setting"],
        "sections": [
            {
                "heading": "The Northwind Performance Cycle",
                "paragraphs": [
                    "Northwind runs one formal cycle per year with a lightweight "
                    "mid-year checkpoint. Goals are set in January and locked by "
                    "31 January. The mid-year checkpoint runs in the first two "
                    "weeks of July and is a conversation, not a rating. The "
                    "annual review opens on 1 October, self-assessments close on "
                    "15 October, manager assessments close on 31 October, "
                    "calibration sessions run through November, and final ratings "
                    "are released to employees on the first business day of "
                    "December.",
                    "Every employee participates, including the Executive Staff, "
                    "who are reviewed by the CEO. Probationary employees in their "
                    "first 90 days receive a separate probation review and are "
                    "excluded from the annual cycle; their first annual rating "
                    "covers the remainder of the year pro rata."
                ],
            },
            {
                "heading": "Rating Scale",
                "paragraphs": [
                    "Ratings are assigned on a five-point scale. The scale is "
                    "deliberately anchored to observable outcomes so that two "
                    "managers reviewing the same evidence reach the same rating. "
                    "A rating is a judgement about the year, not about the "
                    "person, and a rating below Expectations does not by itself "
                    "trigger any employment action."
                ],
                "table": [
                    ["Rating", "Label", "Definition", "Merit guidance", "Bonus guidance"],
                    ["5", "Outstanding", "Results far beyond the role's scope, with company-level impact", "8-12%", "130-180% of target"],
                    ["4", "Exceeds Expectations", "Consistently above scope, measurable team or function impact", "5-7%", "110-130% of target"],
                    ["3", "Expectations Met", "Reliably delivers the role's commitments at the expected quality", "2-4%", "100% of target"],
                    ["2", "Partially Meets", "Gaps in one or more commitments that require active manager support", "0-1%", "50-80% of target"],
                    ["1", "Does Not Meet", "Sustained failure to deliver core commitments", "0%", "0%"],
                ],
            },
            {
                "heading": "Calibration",
                "paragraphs": [
                    "Calibration exists to remove drift between managers, not to "
                    "enforce a curve. Northwind does not mandate a forced "
                    "distribution. As guidance, a well-calibrated department "
                    "lands roughly 5 percent at Outstanding, 20 percent at "
                    "Exceeds, 60 percent at Expectations Met, 12 percent at "
                    "Partially Meets, and 3 percent at Does Not Meet. Any "
                    "department deviating by more than ten percentage points "
                    "from the guidance at either extreme must document the "
                    "reason in the calibration record.",
                    "Calibration sessions are chaired by the department head "
                    "with an HR Business Partner present. Managers bring written "
                    "evidence for every rating of 4 or 5 and every rating of 2 "
                    "or 1. Ratings may be challenged by peers in the session; "
                    "the chair's decision is final and is recorded with the "
                    "supporting evidence."
                ],
                "notes": [
                    "Bias note: the HR Business Partner must stop the session if "
                    "evidence for a rating is absent, if language about an "
                    "employee references protected characteristics, or if "
                    "feedback volume differs materially between employees of "
                    "similar tenure and scope."
                ],
            },
            {
                "heading": "Goal Setting Rules",
                "paragraphs": [
                    "Each employee carries three to five goals. At least one "
                    "goal must be a learning goal, and no more than one goal may "
                    "be a maintenance goal that describes the ordinary duties of "
                    "the role. Every goal carries an owner, a measurable success "
                    "criterion, and a target date. Goals that depend on another "
                    "team must name the dependency and the counterpart owner.",
                    "Goals may be revised mid-year when the business direction "
                    "changes, but the revision must be recorded in Workday with "
                    "a reason. Silently rewriting a goal in October so that it "
                    "matches what was delivered is prohibited and is treated as "
                    "a manager conduct issue."
                ],
                "bullets": [
                    "Three to five goals per employee, locked by 31 January.",
                    "At least one learning goal; at most one maintenance goal.",
                    "Cross-team goals must name the dependency and counterpart owner.",
                    "Mid-year goal edits require a recorded reason in Workday.",
                ],
            },
            {
                "heading": "Performance Improvement Plans",
                "paragraphs": [
                    "A Performance Improvement Plan is offered when an employee "
                    "is rated Partially Meets or Does Not Meet and the manager "
                    "judges the gap to be closable. A PIP runs 60 days by "
                    "default and 90 days for roles with long feedback loops, "
                    "such as enterprise sales or research. It states the "
                    "specific gaps, the expected outcomes, the support "
                    "Northwind will provide, and the check-in cadence, which is "
                    "weekly.",
                    "A PIP is not a disciplinary warning and must not be "
                    "described as one. Two PIPs in twelve months for the same "
                    "gap is permitted only with written approval from the VP of "
                    "People Operations. Where a PIP concludes without the "
                    "expected improvement, the manager, HR Business Partner, and "
                    "department head jointly decide the next step, which may "
                    "include role change, redeployment, or separation."
                ],
                "qa": [
                    {
                        "question": "When are final annual ratings released?",
                        "answer": "On the first business day of December, after calibration completes in November.",
                    },
                    {
                        "question": "What is the default length of a performance improvement plan?",
                        "answer": "60 days, extended to 90 days for roles with long feedback loops such as enterprise sales or research.",
                    },
                    {
                        "question": "What merit range applies to an Exceeds Expectations rating?",
                        "answer": "5 to 7 percent.",
                    },
                ],
            },
        ],
        "qa": [
            {"question": "When do annual goals have to be locked?",
             "answer": "By 31 January.",
             "evidence": "Goals are set in January and locked by 31 January"},
            {"question": "What merit increase range is guided for a rating of Outstanding?",
             "answer": "8 to 12 percent.",
             "evidence": "Outstanding ... 8-12%"},
            {"question": "How long does a default performance improvement plan run?",
             "answer": "60 days, or 90 days for roles with long feedback loops.",
             "evidence": "A PIP runs 60 days by default and 90 days for roles with long feedback loops"},
            {"question": "Does Northwind use a forced distribution for ratings?",
             "answer": "No. Calibration guidance suggests approximate percentages, but no forced curve is mandated.",
             "evidence": "Calibration exists to remove drift between managers, not to enforce a curve. Northwind does not mandate a forced distribution."},
            {"question": "How many goals does each employee carry?",
             "answer": "Three to five goals, with at least one learning goal and at most one maintenance goal.",
             "evidence": "Each employee carries three to five goals"},
        ],
    },
    {
        "id": "HR-STD-007",
        "title": "Leave of Absence and Time Off Standard",
        "doc_type": "Standard",
        "category": "Human Resources",
        "department": "People Operations",
        "author": "Priya Raghunathan, Leave and Benefits Program Manager",
        "owner": "People Operations",
        "version": "3.4",
        "effective": "2026-03-01",
        "classification": "Internal",
        "review": "Annual",
        "summary": (
            "Sets out the Northwind time-off model, which replaces separate "
            "sick, personal, and vacation banks with a single flexible bank "
            "plus statutory and protected leaves. Covers accrual rates, "
            "carry-over limits, payout rules, parental leave, bereavement, "
            "jury and voting leave, and the approval workflow in Workday."
        ),
        "tags": ["PTO", "leave", "parental leave", "sick leave", "accrual", "carry-over"],
        "sections": [
            {
                "heading": "The Flexible Bank",
                "paragraphs": [
                    "Northwind operates a single flexible time-off bank called "
                    "FlexTime. FlexTime covers vacation, personal days, and "
                    "short-term illness. There is no separate sick bank and no "
                    "requirement to give a reason for a FlexTime day. Northwind "
                    "does not require a doctor's note for absences of three "
                    "consecutive business days or fewer.",
                    "Accrual is per pay period and begins on the first day of "
                    "employment. The accrual rate rises with completed years of "
                    "service on the anniversary date, not on the hire month."
                ],
                "table": [
                    ["Completed service", "Accrual per pay period", "Annual total (26 periods)", "Carry-over cap"],
                    ["0-2 years", "5.0 hours", "130 hours (16.25 days)", "40 hours"],
                    ["3-6 years", "6.0 hours", "156 hours (19.5 days)", "60 hours"],
                    ["7-11 years", "7.0 hours", "182 hours (22.75 days)", "80 hours"],
                    ["12+ years", "8.0 hours", "208 hours (26 days)", "100 hours"],
                ],
            },
            {
                "heading": "Carry-Over, Payout, and Forfeiture",
                "paragraphs": [
                    "Unused FlexTime carries over to the next year up to the "
                    "cap for the employee's service band. Hours above the cap "
                    "are forfeited on 31 March of the following year, and "
                    "Payroll sends a forfeiture warning on 1 January and again "
                    "on 1 March. Forfeited hours are not restored except where "
                    "the employee was on approved leave for at least 60 "
                    "consecutive days during the accrual year.",
                    "FlexTime is paid out on separation only in the United "
                    "States and only where state law requires it, which today "
                    "means Colorado, California, Illinois, and Massachusetts. "
                    "In all other jurisdictions FlexTime is use-it-or-lose-it "
                    "and no payout is made, in line with the local employment "
                    "contract."
                ],
            },
            {
                "heading": "Parental Leave",
                "paragraphs": [
                    "All employees with at least 12 months of service receive "
                    "20 weeks of fully paid parental leave following the birth, "
                    "adoption, or surrogacy placement of a child. The leave is "
                    "gender-neutral and may be taken in up to three blocks, "
                    "with at least one block of eight consecutive weeks taken "
                    "within the first 18 months. Employees on parental leave "
                    "continue to accrue FlexTime at their normal rate and "
                    "continue to receive employer benefit contributions.",
                    "In addition, employees receive 10 fully paid days of "
                    "partner leave, which may be taken at any point in the "
                    "first year and does not require 12 months of service. "
                    "Parental leave runs concurrently with any statutory "
                    "parental pay; Northwind tops the statutory payment up to "
                    "full base salary."
                ],
                "bullets": [
                    "20 fully paid weeks, gender-neutral, available after 12 months of service.",
                    "Up to three blocks, with one block of at least eight consecutive weeks inside 18 months.",
                    "FlexTime continues to accrue during parental leave.",
                    "10 fully paid partner days, no service requirement.",
                ],
            },
            {
                "heading": "Protected and Statutory Leave",
                "paragraphs": [
                    "Protected leaves sit outside the FlexTime bank and are "
                    "never counted against it. These include medical leave under "
                    "the Family and Medical Leave Act, military leave, jury "
                    "duty, voting leave, bereavement leave, and leave related to "
                    "domestic violence or sexual violence. Bereavement provides "
                    "5 paid days for the death of an immediate family member and "
                    "2 paid days for any other person the employee considers "
                    "family, with additional unpaid days available on request.",
                    "Jury duty is paid for up to 15 days per year at base "
                    "salary, less any fee paid by the court. Voting leave is two "
                    "consecutive hours at the start or end of a shift. Requests "
                    "for protected leave are routed to the Leave of Absence team "
                    "at leave@northwind.example, not to the line manager, and "
                    "the manager is told only the return date."
                ],
                "notes": [
                    "Confidentiality: line managers are not entitled to the "
                    "medical reason behind a protected leave. Sharing a "
                    "diagnosis with a manager without the employee's written "
                    "consent is a privacy violation under HR-STD-009."
                ],
            },
            {
                "heading": "Requesting and Approving Time Off",
                "paragraphs": [
                    "All FlexTime is requested in Workday. Requests of five "
                    "consecutive days or fewer are approved by the line manager "
                    "with a service-level target of three business days. "
                    "Requests above five consecutive days, or any request that "
                    "overlaps a published team blackout window, additionally "
                    "require the department head. Team blackout windows are "
                    "published once per quarter and may not exceed ten business "
                    "days per quarter.",
                    "Managers may deny a request only for capacity reasons that "
                    "are documented in the Workday comment field. Denial because "
                    "an employee has taken a lot of leave recently, or because "
                    "the leave is protected, is prohibited and should be "
                    "escalated to the HR Business Partner."
                ],
                "qa": [
                    {
                        "question": "Does Northwind require a doctor's note for sick days?",
                        "answer": "No. No note is required for absences of three consecutive business days or fewer.",
                    },
                    {
                        "question": "How many paid parental leave weeks are offered?",
                        "answer": "20 fully paid weeks, available after 12 months of service.",
                    },
                    {
                        "question": "When are unused FlexTime hours forfeited?",
                        "answer": "On 31 March of the following year, after warnings on 1 January and 1 March.",
                    },
                ],
            },
        ],
        "qa": [
            {"question": "How many FlexTime hours does an employee with 4 years of service accrue per year?",
             "answer": "156 hours, or 19.5 days, across 26 pay periods.",
             "evidence": "3-6 years | 6.0 hours | 156 hours (19.5 days)"},
            {"question": "How many weeks of fully paid parental leave does Northwind offer?",
             "answer": "20 fully paid weeks, gender-neutral, after 12 months of service.",
             "evidence": "20 weeks of fully paid parental leave"},
            {"question": "How many paid bereavement days for an immediate family member?",
             "answer": "5 paid days for an immediate family member, 2 paid days for anyone else the employee considers family.",
             "evidence": "5 paid days for the death of an immediate family member and 2 paid days for any other person"},
            {"question": "In which US states is unused FlexTime paid out on separation?",
             "answer": "Colorado, California, Illinois, and Massachusetts.",
             "evidence": "which today means Colorado, California, Illinois, and Massachusetts"},
            {"question": "What is the maximum size of a quarterly team blackout window?",
             "answer": "Ten business days per quarter.",
             "evidence": "may not exceed ten business days per quarter"},
        ],
    },
    {
        "id": "HR-STD-009",
        "title": "Workplace Conduct and Anti-Harassment Standard",
        "doc_type": "Standard",
        "category": "Human Resources",
        "department": "People Operations",
        "author": "Dana Whitfield, Director of People Operations",
        "owner": "People Operations and Legal",
        "version": "5.2",
        "effective": "2026-01-15",
        "classification": "Internal",
        "review": "Annual",
        "summary": (
            "Defines expected conduct at Northwind, the prohibited categories of "
            "behaviour including harassment, discrimination, bullying, and "
            "retaliation, the four reporting channels, the investigation "
            "timeline and evidentiary standard, and the anti-retaliation "
            "guarantees that protect reporters and witnesses."
        ),
        "tags": ["conduct", "harassment", "discrimination", "retaliation", "investigation", "reporting"],
        "sections": [
            {
                "heading": "Expected Conduct",
                "paragraphs": [
                    "Northwind expects every person working for the company to "
                    "act with honesty, to treat colleagues and customers with "
                    "respect, and to raise concerns when something looks wrong. "
                    "The standard applies to employees, contractors, interns, "
                    "and vendors while on Northwind premises or representing "
                    "Northwind, and to conduct on Northwind systems and "
                    "communication tools regardless of where it occurs.",
                    "Conduct at off-site events, team dinners, conferences, and "
                    "in work-related messaging groups is in scope. Alcohol at a "
                    "company event does not lower the standard, and neither does "
                    "the fact that behaviour was framed as a joke."
                ],
            },
            {
                "heading": "Prohibited Conduct",
                "paragraphs": [
                    "Harassment is unwelcome conduct related to a protected "
                    "characteristic that is severe or pervasive enough to create "
                    "an intimidating, hostile, or offensive environment. "
                    "Discrimination is an adverse employment decision taken "
                    "wholly or partly because of a protected characteristic. "
                    "Bullying is repeated unreasonable conduct that endangers "
                    "an employee's dignity or wellbeing, whether or not a "
                    "protected characteristic is involved."
                ],
                "bullets": [
                    "Harassment, including sexual harassment, sexual coercion, and quid pro quo demands.",
                    "Discrimination in hiring, pay, promotion, leave, or termination based on a protected characteristic.",
                    "Bullying, humiliation, and the deliberate exclusion of a colleague from work they need to do.",
                    "Retaliation against anyone who reports a concern in good faith or participates in an investigation.",
                    "Falsely reporting a violation, which is itself misconduct.",
                ],
                "notes": [
                    "Good faith is the test for a report, not accuracy. An "
                    "unsubstantiated report made honestly is protected; a report "
                    "known to be false is not."
                ],
            },
            {
                "heading": "How to Report",
                "paragraphs": [
                    "There are four reporting channels and an employee may use "
                    "any of them in any order. Reporting to your line manager is "
                    "the default. If the manager is involved, or if you would "
                    "rather not use that route, report to your HR Business "
                    "Partner, to the Ethics Line at ethics.northwind.example "
                    "which is operated by an independent third party and accepts "
                    "anonymous reports, or to Legal at conduct@northwind.example.",
                    "Reports may be made verbally or in writing, and the "
                    "receiver must log the report in the Conduct Case system "
                    "within one business day. An employee who makes a verbal "
                    "report is entitled to ask for a written summary of what was "
                    "recorded and to correct it."
                ],
                "table": [
                    ["Channel", "Anonymous?", "Logged within", "Best for"],
                    ["Line manager", "No", "1 business day", "Day-to-day issues, early resolution"],
                    ["HR Business Partner", "No", "1 business day", "Issues involving the manager"],
                    ["Ethics Line (third party)", "Yes", "Same day", "Serious allegations, senior staff, anonymity"],
                    ["Legal", "No", "1 business day", "Legal exposure, regulator involvement"],
                ],
            },
            {
                "heading": "Investigation Process and Timelines",
                "paragraphs": [
                    "Every report is triaged within two business days by the "
                    "Conduct Review Panel, which decides whether the matter is "
                    "handled informally, formally, or referred to Legal. "
                    "Informal matters, such as a single low-severity "
                    "misunderstanding, are resolved by facilitated conversation "
                    "within 15 business days. Formal investigations have a "
                    "target of 30 business days from intake to written outcome, "
                    "with a documented extension permitted for complex cases "
                    "involving more than five witnesses.",
                    "The evidentiary standard is the balance of probabilities, "
                    "not the criminal standard of beyond reasonable doubt. The "
                    "investigator interviews the reporter, the respondent, and "
                    "relevant witnesses, reviews documents and messages where "
                    "lawfully available, and writes an outcome letter to both "
                    "parties stating the findings and the reasons. The outcome "
                    "letter does not disclose the specific disciplinary action "
                    "taken against the respondent.",
                    "Both parties may request a review of the outcome within 10 "
                    "business days. Review is conducted by a panel member who "
                    "was not involved in the original investigation and is "
                    "limited to whether the process was fair and the findings "
                    "were open on the evidence."
                ],
                "qa": [
                    {
                        "question": "How quickly must a report be logged?",
                        "answer": "Within one business day of being received, and the same day for the Ethics Line.",
                    },
                    {
                        "question": "What standard of proof is used in investigations?",
                        "answer": "The balance of probabilities, not the criminal standard of beyond reasonable doubt.",
                    },
                    {
                        "question": "Can a report be made anonymously?",
                        "answer": "Yes, through the independently operated Ethics Line.",
                    },
                ],
            },
            {
                "heading": "Anti-Retaliation Guarantees",
                "paragraphs": [
                    "Retaliation is prohibited and is treated as a separate, "
                    "independent violation, which means a respondent may be "
                    "sanctioned for retaliation even where the original "
                    "allegation was not substantiated. Protected activity "
                    "includes making a report, refusing to participate in "
                    "conduct believed to be unlawful, giving a witness "
                    "statement, and requesting an accommodation.",
                    "Where a reporter alleges retaliation, the Conduct Review "
                    "Panel assesses that allegation on an expedited basis within "
                    "10 business days and may impose interim measures such as "
                    "changing a reporting line or placing an employee on paid "
                    "administrative leave while the matter is open. Interim "
                    "measures are not a finding against anyone."
                ],
            },
        ],
        "qa": [
            {"question": "How many reporting channels exist for conduct concerns at Northwind?",
             "answer": "Four: line manager, HR Business Partner, the third-party Ethics Line, and Legal.",
             "evidence": "There are four reporting channels"},
            {"question": "What is the target duration of a formal conduct investigation?",
             "answer": "30 business days from intake to written outcome.",
             "evidence": "Formal investigations have a target of 30 business days from intake to written outcome"},
            {"question": "Which channel accepts anonymous reports?",
             "answer": "The Ethics Line, operated by an independent third party.",
             "evidence": "the Ethics Line at ethics.northwind.example which is operated by an independent third party and accepts anonymous reports"},
            {"question": "What standard of proof applies in a conduct investigation?",
             "answer": "The balance of probabilities.",
             "evidence": "The evidentiary standard is the balance of probabilities"},
            {"question": "How fast must an alleged retaliation claim be assessed?",
             "answer": "On an expedited basis within 10 business days.",
             "evidence": "assesses that allegation on an expedited basis within 10 business days"},
        ],
    },
    {
        "id": "HR-HBK-011",
        "title": "Global Mobility Handbook",
        "doc_type": "Handbook",
        "category": "Human Resources",
        "department": "Global Mobility",
        "author": "Ingrid Halvorsen, Global Mobility Lead",
        "owner": "Global Mobility",
        "version": "2.3",
        "effective": "2026-04-01",
        "classification": "Internal",
        "review": "Semi-annual",
        "summary": (
            "Guidance for managers and employees on international transfers, "
            "short-term assignments, business travel thresholds, immigration "
            "timelines, relocation support levels, and the tax equalisation "
            "model used when an employee becomes tax resident in a new country."
        ),
        "tags": ["relocation", "immigration", "assignment", "tax equalisation", "visa", "mobility"],
        "sections": [
            {
                "heading": "When Mobility Rules Apply",
                "paragraphs": [
                    "Global Mobility governs any change that moves an employee "
                    "across a border for work, or that changes the country in "
                    "which an employee is tax resident. Three situations trigger "
                    "this handbook: a permanent international transfer, a "
                    "short-term assignment of 30 to 180 days, and a remote work "
                    "location change that crosses a border. Ordinary business "
                    "travel below 30 days per rolling twelve months in any one "
                    "country is handled by the Travel team under TRV-STD-002.",
                    "Managers must open a mobility case before making a verbal "
                    "offer or promising a start date. An offer made without "
                    "mobility clearance is not binding on Northwind and has "
                    "previously caused start dates to slip by a full quarter."
                ],
            },
            {
                "heading": "Assignment Types",
                "paragraphs": [
                    "A permanent transfer changes the employee's employing "
                    "entity, payroll country, and benefits plan. A short-term "
                    "assignment keeps the employee on their home entity and "
                    "home payroll for up to 180 days, after which a transfer is "
                    "mandatory. A remote location change keeps the entity "
                    "unchanged where Northwind holds an employer-of-record "
                    "partner in the destination country, and otherwise requires "
                    "onboarding through Deel."
                ],
                "table": [
                    ["Type", "Duration", "Payroll entity", "Relocation support", "Tax treatment"],
                    ["Permanent transfer", "Indefinite", "Host country entity", "Tier 2", "Tax equalisation"],
                    ["Short-term assignment", "30-180 days", "Home country entity", "Tier 3 (housing and flights only)", "Home country, monitored for treaty breach"],
                    ["Remote location change", "Indefinite", "Home entity or Deel EOR", "Tier 4 (self-managed)", "Host country, no equalisation"],
                ],
            },
            {
                "heading": "Relocation Support Tiers",
                "paragraphs": [
                    "Tier 2 applies to permanent transfers and covers "
                    "round-trip travel for the employee and accompanying "
                    "dependants, 60 days of temporary accommodation, "
                    "household goods shipment up to 500 cubic feet, a "
                    "one-off settling-in payment of 1.5 months of gross base "
                    "salary, and visa and immigration fees. Spousal employment "
                    "support is provided through the partner network but "
                    "Northwind does not guarantee a job for a dependant.",
                    "Tier 3 covers housing and flights for the assignee only. "
                    "Tier 4 provides no relocation money; the employee is "
                    "responsible for their own move and must confirm a "
                    "residential address that satisfies local registration "
                    "rules before payroll can be switched."
                ],
                "bullets": [
                    "Tier 2: travel, 60 days temporary housing, 500 cubic feet of goods, 1.5 months salary settling-in payment, visa fees.",
                    "Tier 3: housing and flights for the assignee only, no goods shipment.",
                    "Tier 4: self-managed, no relocation payment.",
                    "Immigration fees are always paid directly by Northwind, never reimbursed.",
                ],
            },
            {
                "heading": "Immigration Timelines",
                "paragraphs": [
                    "Timelines below are the 2026 planning assumptions for "
                    "common corridors and are not guarantees. Work permit "
                    "processing is outside Northwind's control, and managers "
                    "must add a 20 percent buffer to any start date that "
                    "depends on a permit.",
                    "The fastest corridor is the UK Skilled Worker route at "
                    "roughly 6 weeks including certificate of sponsorship. "
                    "Ireland Critical Skills is roughly 8 weeks. The US H-1B "
                    "route is dominated by the annual registration window in "
                    "March and the 1 April filing date, which means an H-1B "
                    "start date cannot realistically be earlier than 1 October. "
                    "Germany's EU Blue Card is roughly 10 weeks once the "
                    "recognition of qualifications is settled."
                ],
                "table": [
                    ["Corridor", "Route", "Planning estimate", "Notes"],
                    ["US to UK", "Skilled Worker", "6 weeks", "CoS first, then biometrics"],
                    ["India to US", "H-1B", "6-9 months", "Consular processing plus registration window"],
                    ["EU to Germany", "EU Blue Card", "10 weeks", "Qualification recognition can add 8 weeks"],
                    ["Any to Singapore", "Employment Pass", "5 weeks", "COMPASS scoring applies"],
                ],
            },
            {
                "heading": "Tax Equalisation",
                "paragraphs": [
                    "Employees on a permanent transfer are tax equalised. Tax "
                    "equalisation means the employee pays the hypothetical "
                    "amount of tax they would have paid had they stayed in "
                    "their home country, and Northwind bears the actual tax "
                    "liability in the host country. The hypothetical tax is "
                    "calculated by the assigned provider, currently Mercer, and "
                    "is withheld through payroll each period.",
                    "A settlement runs after the employee files in both "
                    "countries, normally 12 to 18 months after the move. If the "
                    "actual host-country tax is lower than the hypothetical "
                    "amount, Northwind refunds the difference. If it is higher, "
                    "Northwind absorbs the excess. Employees must give the "
                    "provider power of attorney and must not file their own "
                    "returns while equalised, because a self-filed return "
                    "invalidates the equalisation calculation."
                ],
                "qa": [
                    {
                        "question": "What is the maximum length of a short-term assignment?",
                        "answer": "180 days, after which a permanent transfer becomes mandatory.",
                    },
                    {
                    "question": "Who pays immigration fees?",
                        "answer": "Northwind pays them directly; they are never reimbursed to the employee.",
                    },
                    {
                        "question": "What does tax equalisation mean for a transferred employee?",
                        "answer": "The employee pays the hypothetical home-country tax while Northwind bears the actual host-country liability.",
                    },
                ],
            },
        ],
        "qa": [
            {"question": "What is the maximum duration of a short-term assignment before a transfer is mandatory?",
             "answer": "180 days.",
             "evidence": "up to 180 days, after which a transfer is mandatory"},
            {"question": "How much settling-in payment does a Tier 2 relocation include?",
             "answer": "A one-off payment of 1.5 months of gross base salary.",
             "evidence": "a one-off settling-in payment of 1.5 months of gross base salary"},
            {"question": "Which provider calculates Northwind's hypothetical tax?",
             "answer": "Mercer.",
             "evidence": "calculated by the assigned provider, currently Mercer"},
            {"question": "What is the planning estimate for a UK Skilled Worker visa?",
             "answer": "Roughly 6 weeks, including certificate of sponsorship.",
             "evidence": "the UK Skilled Worker route at roughly 6 weeks including certificate of sponsorship"},
            {"question": "Above what travel threshold does the Mobility handbook apply instead of the Travel standard?",
             "answer": "30 days per rolling twelve months in any one country.",
             "evidence": "Ordinary business travel below 30 days per rolling twelve months in any one country is handled by the Travel team under TRV-STD-002"},
        ],
    },
]
