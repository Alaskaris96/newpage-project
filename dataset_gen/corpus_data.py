"""Data engineering and analytics corpus (5 documents)."""

DOCS = [
    {
        "id": "DAT-STD-002",
        "title": "Analytics Event Tracking Specification",
        "doc_type": "Specification",
        "category": "Data and Analytics",
        "department": "Data Engineering",
        "author": "Wei Zhang, Lead Analytics Engineer",
        "owner": "Data Engineering",
        "version": "3.4",
        "effective": "2026-03-01",
        "classification": "Internal",
        "review": "Quarterly",
        "summary": (
            "Defines the Northwind event taxonomy, naming conventions, the "
            "required property set, identity resolution rules, sampling and "
            "sampling correction, the event review process, and the pipeline "
            "that moves events from client to warehouse."
        ),
        "tags": ["event tracking", "taxonomy", "identity resolution", "warehouse", "instrumentation"],
        "sections": [
            {
                "heading": "Event Taxonomy",
                "paragraphs": [
                    "Events are named as object_verb in lower snake case, "
                    "present tense, and are registered in the Event Catalogue "
                    "before any code is written. Unregistered events are dropped "
                    "at the collector rather than silently accepted, which "
                    "prevents the cardinality explosion that unmanaged tracking "
                    "produces. The catalogue currently holds 186 events.",
                    "Events are grouped into four families. Lifecycle events "
                    "describe account and user state changes and are captured "
                    "server-side only. Engagement events describe user "
                    "interaction and are captured client-side. System events "
                    "describe platform behaviour such as errors and latency. "
                    "Business events describe revenue-relevant actions and "
                    "require a review sign-off from Analytics before release."
                ],
                "table": [
                    ["Family", "Capture side", "Example events", "Retention", "Review required"],
                    ["Lifecycle", "Server only", "account_created, seat_added", "7 years", "Analytics"],
                    ["Engagement", "Client", "page_published, report_viewed", "26 months", "Self-service"],
                    ["System", "Server or client", "api_error, render_timeout", "90 days", "Self-service"],
                    ["Business", "Server only", "subscription_upgraded, invoice_paid", "7 years", "Analytics and Finance"],
                ],
            },
            {
                "heading": "Required Properties",
                "paragraphs": [
                    "Every event carries eight required properties. Missing any "
                    "of them causes the event to be routed to the quarantine "
                    "table, where it is visible in the daily data quality report "
                    "but excluded from all dashboards. Quarantine volume above "
                    "0.5 percent of daily events blocks the next release of the "
                    "instrumentation library.",
                    "Custom properties must be typed and registered. Free-form "
                    "string properties are prohibited because they become "
                    "ungovernable; where free text is genuinely needed, the "
                    "value is hashed and the raw value stays in the source "
                    "system."
                ],
                "bullets": [
                    "Required: event_id, event_name, occurred_at, user_id or anonymous_id, account_id, platform, app_version, environment.",
                    "occurred_at is client-generated; server_received_at is added at the collector and both are kept.",
                    "Property names are lower snake case and must be registered before use.",
                    "No property may contain personal data unless it is registered as such and encrypted at rest.",
                ],
            },
            {
                "heading": "Identity Resolution",
                "paragraphs": [
                    "Northwind resolves identity using a two-tier model. "
                    "Anonymous visitors carry a first-party identifier stored in "
                    "a cookie with a 395 day expiry. Authenticated users carry a "
                    "stable user identifier issued by the identity service. On "
                    "login, the anonymous identifier is stitched to the user "
                    "identifier and the mapping is immutable, which preserves "
                    "the pre-login journey.",
                    "Stitching is one-way and never undone, except where a user "
                    "exercises a deletion right, in which case the mapping and "
                    "both identifiers are tombstoned. Cross-device identity is "
                    "not asserted from probabilistic signals such as IP or user "
                    "agent, because the error rate is unacceptable for "
                    "customer-facing numbers."
                ],
                "notes": [
                    "Reporting note: because stitching is client-side, a user who "
                    "clears cookies after authenticating appears as a new "
                    "visitor. This inflates new-visitor counts by roughly 4 "
                    "percent, which is documented in the metric glossary."
                ],
            },
            {
                "heading": "Pipeline and Sampling",
                "paragraphs": [
                    "Events flow from client to the collector, through a stream "
                    "buffer, into the warehouse staging tables, and then through "
                    "a modelled layer of staging, intermediate, and mart tables. "
                    "Consumers read marts only. Direct queries against staging "
                    "are prohibited because staging is not deduplicated.",
                    "End-to-end latency from client event to mart availability is "
                    "targeted at 15 minutes with a 99th percentile of 45 "
                    "minutes. Duplicate handling uses the client-generated "
                    "event_id with a 72 hour deduplication window. Sampling is "
                    "applied only to System events above 10 million per day, at "
                    "a documented rate, and every sampled metric must expose the "
                    "sampling weight so that consumers can extrapolate correctly."
                ],
                "table": [
                    ["Layer", "Contents", "Consumers", "Freshness SLA"],
                    ["Staging", "Raw, deduplicated, not modelled", "Data Engineering only", "10 minutes"],
                    ["Intermediate", "Cleansed, joined, typed", "Data Engineering", "15 minutes"],
                    ["Mart", "Business-ready aggregates", "All teams via BI", "15 minutes"],
                    ["Quarantine", "Schema-invalid events", "Data Quality review", "24 hours"],
                ],
            },
            {
                "heading": "Review Process",
                "paragraphs": [
                    "New or changed events are proposed as a pull request against "
                    "the Event Catalogue repository, reviewed by an Analytics "
                    "Engineer, and merged only after the property schema and the "
                    "owning team are set. Business events additionally require "
                    "Finance sign-off because they feed revenue reporting.",
                    "Events unused in any dashboard or export for 180 days are "
                    "flagged for retirement. Retiring an event requires 30 days' "
                    "notice to consumers and a final archive export, after which "
                    "the collector stops accepting it."
                ],
                "qa": [
                    {
                        "question": "What happens to events not registered in the catalogue?",
                        "answer": "They are dropped at the collector rather than silently accepted.",
                    },
                    {
                        "question": "What is the cookie expiry for the anonymous identifier?",
                        "answer": "395 days.",
                    },
                    {
                        "question": "Which table layer may general consumers query?",
                        "answer": "Marts only; direct queries against staging are prohibited.",
                    },
                ],
            },
        ],
        "qa": [
            {"question": "How many events are in the Northwind Event Catalogue?",
             "answer": "186 events.",
             "evidence": "The catalogue currently holds 186 events"},
            {"question": "What is the anonymous cookie expiry window?",
             "answer": "395 days.",
             "evidence": "a cookie with a 395 day expiry"},
            {"question": "What quarantine volume blocks the next instrumentation library release?",
             "answer": "Above 0.5 percent of daily events.",
             "evidence": "Quarantine volume above 0.5 percent of daily events blocks the next release"},
            {"question": "Which table layer are general consumers allowed to query?",
             "answer": "Marts only; staging is not deduplicated and is restricted to Data Engineering.",
             "evidence": "Consumers read marts only. Direct queries against staging are prohibited"},
            {"question": "After how long unused are events flagged for retirement?",
             "answer": "180 days without use in any dashboard or export.",
             "evidence": "Events unused in any dashboard or export for 180 days are flagged for retirement"},
        ],
    },
    {
        "id": "DAT-STD-008",
        "title": "Data Quality and Observability Standard",
        "doc_type": "Standard",
        "category": "Data and Analytics",
        "department": "Data Engineering",
        "author": "Fatima Al-Rashid, Head of Data Platform",
        "owner": "Data Engineering",
        "version": "2.2",
        "effective": "2026-04-01",
        "classification": "Internal",
        "review": "Annual",
        "summary": (
            "Defines the five dimensions of data quality used at Northwind, the "
            "test tiers and their blocking behaviour, freshness and volume "
            "monitoring, incident handling for data defects, and the data "
            "contract between producers and consumers."
        ),
        "tags": ["data quality", "observability", "freshness", "data contract", "tests", "lineage"],
        "sections": [
            {
                "heading": "Five Quality Dimensions",
                "paragraphs": [
                    "Quality is assessed on five dimensions. Completeness asks "
                    "whether required values are present. Accuracy asks whether "
                    "values reflect reality. Consistency asks whether the same "
                    "fact agrees across systems. Timeliness asks whether data "
                    "arrived within its freshness commitment. Validity asks "
                    "whether values conform to an allowed domain or format.",
                    "Every production dataset declares which dimensions matter "
                    "for it and at what threshold. Declaring all five at 100 "
                    "percent on everything is prohibited because it produces "
                    "alert noise and trains people to ignore alerts."
                ],
                "table": [
                    ["Dimension", "Example check", "Typical threshold", "Severity if breached"],
                    ["Completeness", "Null rate on account_id below 0.1 percent", "0.1 percent", "High"],
                    ["Accuracy", "MRR matches billing system within 0.5 percent", "0.5 percent", "Critical"],
                    ["Consistency", "Row counts agree across source and mart", "Exact", "High"],
                    ["Timeliness", "Mart refreshed within 15 minutes of event", "15 minutes", "Medium"],
                    ["Validity", "Plan value in the allowed enum", "100 percent", "High"],
                ],
            },
            {
                "heading": "Test Tiers",
                "paragraphs": [
                    "Tests run in three tiers. Tier 1 tests are blocking: a "
                    "failure stops the model from being promoted to production "
                    "and pages the on-call data engineer. Tier 1 is reserved for "
                    "uniqueness on primary keys, referential integrity on "
                    "foreign keys, and not-null on declared required columns. "
                    "Tier 2 tests warn and open a ticket without blocking. Tier "
                    "3 tests are trend-based anomaly detection and are advisory.",
                    "Anomaly detection uses a 14-day rolling baseline with a "
                    "seasonality adjustment for weekday effects, and requires a "
                    "minimum of 21 days of history before it will fire, which "
                    "prevents new models from generating false positives during "
                    "ramp-up."
                ],
                "bullets": [
                    "Tier 1 blocks promotion and pages on-call: uniqueness, referential integrity, not-null.",
                    "Tier 2 warns and tickets: distribution shifts, value ranges, duplicate rates.",
                    "Tier 3 advisory: anomaly detection on volume and freshness.",
                    "Anomaly baselines need 21 days of history before firing.",
                ],
            },
            {
                "heading": "Freshness and Volume Monitoring",
                "paragraphs": [
                    "Every production dataset has a declared freshness "
                    "commitment and a declared expected volume band. Freshness "
                    "is measured from the source event timestamp to mart "
                    "availability, not from job start, because measuring from "
                    "job start hides upstream lag. A dataset that misses "
                    "freshness three times in seven days is escalated from a "
                    "warning to an incident.",
                    "Volume is monitored as a percentage band against the "
                    "seasonal baseline. A drop below 60 percent of expected "
                    "volume is treated as a probable upstream break and paged, "
                    "because silent truncation is the most damaging failure mode "
                    "and the one most likely to be missed by schema tests."
                ],
            },
            {
                "heading": "Data Contracts",
                "paragraphs": [
                    "A data contract is a signed agreement between a producing "
                    "team and its consumers, recorded in the catalogue. It "
                    "declares the schema, the semantics of each column, the "
                    "freshness commitment, the quality thresholds, and the "
                    "breaking-change notice period, which is 30 days. A producer "
                    "may not make a breaking change inside the notice period.",
                    "Contracts are versioned. When a contract changes, consumers "
                    "are notified automatically from the lineage graph, which is "
                    "why lineage must be complete before a contract can be "
                    "signed. Datasets without lineage cannot be contracted and "
                    "therefore cannot be used in a customer-facing surface."
                ],
                "notes": [
                    "Trust note: a customer-facing number that is wrong once "
                    "takes roughly a year to re-earn. Tier 1 tests exist mainly "
                    "to protect the four datasets that appear in customer "
                    "reports."
                ],
            },
            {
                "heading": "Incident Handling",
                "paragraphs": [
                    "Data defects are handled under the Incident Response "
                    "Standard with a data-specific severity overlay. A defect "
                    "affecting a customer-facing number or a financial figure is "
                    "SEV-2 or higher regardless of how it was discovered. The "
                    "affected dashboards are badged with a data quality banner "
                    "rather than silently corrected, because silent correction "
                    "destroys trust faster than an acknowledged error.",
                    "Every data incident produces a correction record listing the "
                    "affected datasets, the affected time range, the consumers "
                    "notified, and the downstream figures restated. Correction "
                    "records are reviewed monthly by the Data Governance Council."
                ],
                "qa": [
                    {
                        "question": "Which tests are blocking?",
                        "answer": "Tier 1 tests: uniqueness on primary keys, referential integrity, and not-null on required columns.",
                    },
                    {
                        "question": "What volume drop is treated as a probable upstream break?",
                        "answer": "Below 60 percent of expected volume.",
                    },
                    {
                        "question": "What notice period does a data contract require for breaking changes?",
                        "answer": "30 days.",
                    },
                ],
            },
        ],
        "qa": [
            {"question": "What are the five data quality dimensions used at Northwind?",
             "answer": "Completeness, accuracy, consistency, timeliness, and validity.",
             "evidence": "Completeness asks whether required values are present. Accuracy asks whether values reflect reality. Consistency ... Timeliness ... Validity"},
            {"question": "What volume drop triggers a page for a probable upstream break?",
             "answer": "A drop below 60 percent of expected volume.",
             "evidence": "A drop below 60 percent of expected volume is treated as a probable upstream break and paged"},
            {"question": "What is the breaking-change notice period in a data contract?",
             "answer": "30 days.",
             "evidence": "the breaking-change notice period, which is 30 days"},
            {"question": "How many days of history does anomaly detection require before firing?",
             "answer": "21 days.",
             "evidence": "requires a minimum of 21 days of history before it will fire"},
            {"question": "How is freshness measured?",
             "answer": "From the source event timestamp to mart availability, not from job start.",
             "evidence": "Freshness is measured from the source event timestamp to mart availability, not from job start"},
        ],
    },
    {
        "id": "DAT-HBK-013",
        "title": "Analytics Self-Service Handbook",
        "doc_type": "Handbook",
        "category": "Data and Analytics",
        "department": "Analytics",
        "author": "Oliver Brennan, Analytics Enablement Lead",
        "owner": "Analytics",
        "version": "1.9",
        "effective": "2026-05-01",
        "classification": "Internal",
        "review": "Annual",
        "summary": (
            "Guidance for non-analysts who use Northwind's BI platform. Covers "
            "finding trusted data, the certified versus community content model, "
            "common metric misinterpretations, the request process for new "
            "analysis, and the rules for exporting data outside the platform."
        ),
        "tags": ["self-service", "BI", "certified content", "metrics", "governance", "enablement"],
        "sections": [
            {
                "heading": "Finding Trusted Data",
                "paragraphs": [
                    "Start with the Certified folder, which contains 74 "
                    "dashboards maintained by the Analytics team and covered by "
                    "a data contract. Certified content carries a green badge, "
                    "an owner, a last-reviewed date within 90 days, and a link "
                    "to the metric definition. If a question is not answered by "
                    "certified content, search the Community folder, check the "
                    "owner, and treat unowned content as unverified.",
                    "The single most common cause of wrong numbers is comparing "
                    "a certified dashboard against a community dashboard built "
                    "on a different filter. When two numbers disagree, check the "
                    "filter panel and the date grain before assuming a data "
                    "defect."
                ],
            },
            {
                "heading": "Certified and Community Content",
                "paragraphs": [
                    "Certification requires a named owner, a documented metric "
                    "definition, a passing Tier 1 and Tier 2 test suite on the "
                    "underlying models, and a review within the last 90 days. "
                    "Certification lapses automatically at 90 days without "
                    "review, and the badge is removed rather than left stale.",
                    "Community content is unmanaged but not unpoliced. Content "
                    "that is viewed by more than 20 unique users in 30 days is "
                    "reviewed by Analytics for promotion or correction. Content "
                    "that contradicts a certified metric definition is corrected "
                    "or removed, and the author is notified with the reason."
                ],
                "table": [
                    ["Attribute", "Certified", "Community", "Sandbox"],
                    ["Owner required", "Yes", "Yes", "No"],
                    ["Metric definition linked", "Yes", "Recommended", "No"],
                    ["Test suite passing", "Yes", "No", "No"],
                    ["Review cadence", "90 days", "On report", "None"],
                    ["Safe for exec reporting", "Yes", "No", "No"],
                ],
            },
            {
                "heading": "Common Misinterpretations",
                "paragraphs": [
                    "Four errors account for most of the corrections the "
                    "Analytics team makes. The first is comparing a rolling "
                    "window to a calendar window, which produces a difference of "
                    "up to 12 percent at month boundaries. The second is "
                    "summing a distinct count across dimensions, which "
                    "double-counts users who appear in more than one group.",
                    "The third is reading churn on a monthly cohort as an annual "
                    "rate, which understates annual churn by roughly a factor of "
                    "three. The fourth is comparing a cohort that includes "
                    "trial accounts against one that excludes them. Each of "
                    "these has a worked example in the metric glossary, and the "
                    "glossary is the fastest route to an answer."
                ],
                "bullets": [
                    "Never sum a distinct count across dimensions; recompute the distinct count at the target grain.",
                    "State the window explicitly: rolling 30 days is not calendar month.",
                    "Churn must state its cohort length and its annualisation method.",
                    "Segment comparisons must use the same inclusion rules on both sides.",
                ],
            },
            {
                "heading": "Requesting Analysis",
                "paragraphs": [
                    "Requests are filed in the Analytics Intake form and triaged "
                    "weekly on Tuesday. Small requests, meaning a new dimension "
                    "on an existing model or a one-off pull, have a five "
                    "business day service level. New dashboards are scoped as "
                    "projects and typically take three to six weeks.",
                    "A request must state the decision it supports, the "
                    "audience, and the frequency of use. Requests that cannot "
                    "state the decision are returned rather than built, because "
                    "dashboards nobody acts on are the largest source of "
                    "maintenance cost in the platform."
                ],
            },
            {
                "heading": "Exporting Data",
                "paragraphs": [
                    "Exports are limited to 100,000 rows and are logged with the "
                    "requesting user, the dataset, and the filter applied. "
                    "Exports containing personal data require the Confidential "
                    "handling rules from SEC-STD-012 and must not be emailed; "
                    "use the file gateway with an expiry of no more than 14 "
                    "days.",
                    "Local spreadsheets that become a source of truth are the "
                    "main governance failure mode. Where a spreadsheet is read "
                    "by more than three people or updated more than monthly, it "
                    "should be promoted into the warehouse as a governed source "
                    "with an owner, and the spreadsheet retired."
                ],
                "qa": [
                    {
                        "question": "How many certified dashboards exist?",
                        "answer": "74, maintained by the Analytics team and covered by a data contract.",
                    },
                    {
                        "question": "When does certification lapse?",
                        "answer": "Automatically at 90 days without review.",
                    },
                    {
                        "question": "What is the export row limit?",
                        "answer": "100,000 rows, logged with user, dataset, and filter.",
                    },
                ],
            },
        ],
        "qa": [
            {"question": "How many certified dashboards are in the Northwind BI platform?",
             "answer": "74.",
             "evidence": "which contains 74 dashboards maintained by the Analytics team"},
            {"question": "After how long without review does dashboard certification lapse?",
             "answer": "90 days.",
             "evidence": "Certification lapses automatically at 90 days without review"},
            {"question": "What is the BI export row limit?",
             "answer": "100,000 rows.",
             "evidence": "Exports are limited to 100,000 rows"},
            {"question": "What triggers Analytics review of community content?",
             "answer": "More than 20 unique users in 30 days.",
             "evidence": "Content that is viewed by more than 20 unique users in 30 days is reviewed by Analytics"},
            {"question": "What is the service level for small analytics requests?",
             "answer": "Five business days.",
             "evidence": "have a five business day service level"},
        ],
    },
    {
        "id": "DAT-STD-017",
        "title": "Machine Learning Model Governance Standard",
        "doc_type": "Standard",
        "category": "Data and Analytics",
        "department": "Data Science",
        "author": "Dr. Anke Baumgartner, Head of Data Science",
        "owner": "Data Science",
        "version": "1.6",
        "effective": "2026-06-01",
        "classification": "Confidential",
        "review": "Semi-annual",
        "summary": (
            "Governance for models that influence customer outcomes: model "
            "risk tiers, required documentation, fairness and drift testing, "
            "human review thresholds, approval gates, monitoring obligations, "
            "and the model inventory."
        ),
        "tags": ["machine learning", "model governance", "fairness", "drift", "MLOps", "risk tier"],
        "sections": [
            {
                "heading": "Model Risk Tiers",
                "paragraphs": [
                    "Models are tiered by the consequence of a wrong prediction "
                    "on a person, not by technical complexity. A recommender "
                    "that suggests templates is low risk. A model that decides "
                    "whether a customer's content is published, or that "
                    "influences pricing, is high risk and carries the heaviest "
                    "obligations.",
                    "Any model that uses personal data, produces a score about a "
                    "person, or is not fully explainable to the affected "
                    "individual is at minimum medium risk. Tiering is decided by "
                    "the Model Review Board, which includes Data Science, Legal, "
                    "and a business owner."
                ],
                "table": [
                    ["Tier", "Consequence of error", "Examples", "Human review", "Approval"],
                    ["Low", "Inconvenient suggestion", "Template recommender", "Not required", "Team lead"],
                    ["Medium", "Degraded experience or lost revenue", "Churn propensity, search ranking", "Sampled 5 percent", "Model Review Board"],
                    ["High", "Material effect on a person", "Content moderation, pricing influence", "Required above threshold", "Board and Legal"],
                ],
            },
            {
                "heading": "Required Documentation",
                "paragraphs": [
                    "Every medium and high risk model has a model card covering "
                    "the intended use, the out-of-scope uses, the training data "
                    "provenance and time range, the feature list with a "
                    "justification for each feature, the evaluation results "
                    "including performance by segment, the known limitations, "
                    "and the monitoring plan. The card is reviewed at every "
                    "retraining.",
                    "Training data provenance must name the source systems and "
                    "the extraction window, and must confirm that the data was "
                    "collected under a lawful basis permitting this use. Data "
                    "collected for one purpose may not be repurposed for "
                    "training without a documented assessment."
                ],
                "bullets": [
                    "Model card required for medium and high risk models, reviewed at each retraining.",
                    "Feature justification required for every input feature.",
                    "Evaluation must report performance by segment, not only overall.",
                    "Out-of-scope uses must be stated explicitly.",
                ],
            },
            {
                "heading": "Fairness and Drift Testing",
                "paragraphs": [
                    "Fairness is tested against protected and proxy attributes "
                    "where their use is lawful, using demographic parity "
                    "difference and equal opportunity difference. The current "
                    "acceptance thresholds are a parity difference below 0.1 and "
                    "an equal opportunity difference below 0.1. Exceeding a "
                    "threshold blocks release unless the Model Review Board "
                    "records a documented justification and a remediation plan.",
                    "Drift is monitored on three signals: input feature drift "
                    "using population stability index, prediction distribution "
                    "drift, and outcome drift where labels are available. A "
                    "population stability index above 0.2 on any feature "
                    "triggers investigation; above 0.3 triggers automatic "
                    "retraining review. Labels that arrive late are backfilled "
                    "for 30 days before outcome drift is trusted."
                ],
                "notes": [
                    "Proxy warning: postcode and device tier have previously "
                    "acted as proxies for protected attributes in Northwind "
                    "models. Both are now on the reviewed-feature list."
                ],
            },
            {
                "heading": "Approval and Release Gates",
                "paragraphs": [
                    "Release requires four gates: the model card is complete, "
                    "offline evaluation meets the stated target, fairness tests "
                    "pass or have a recorded exception, and the monitoring plan "
                    "is live before traffic arrives. A model may not be released "
                    "with monitoring to be added later.",
                    "High risk models ship behind a human-in-the-loop threshold. "
                    "Predictions above a confidence threshold are auto-applied; "
                    "predictions in the middle band are routed to a human "
                    "reviewer with a service level of four business hours; "
                    "predictions below the lower threshold are rejected. The "
                    "thresholds are tuned quarterly against reviewer outcomes."
                ],
            },
            {
                "heading": "Inventory and Decommissioning",
                "paragraphs": [
                    "Every model in production is registered in the Model "
                    "Inventory with its owner, tier, purpose, training window, "
                    "last evaluation date, and dependencies. An unregistered "
                    "model may not receive production traffic, and the deployment "
                    "pipeline enforces registration.",
                    "Decommissioning requires a written decision, notification to "
                    "consumers, and a plan for any downstream feature that "
                    "depended on the model's output. Models are not silently "
                    "switched off, because a removed score often breaks a "
                    "business rule that nobody remembered."
                ],
                "qa": [
                    {
                        "question": "What PSI value triggers automatic retraining review?",
                        "answer": "Above 0.3; above 0.2 triggers investigation.",
                    },
                    {
                        "question": "What is the fairness acceptance threshold for parity difference?",
                        "answer": "Below 0.1.",
                    },
                    {
                        "question": "What service level applies to human review of medium-confidence predictions?",
                        "answer": "Four business hours.",
                    },
                ],
            },
        ],
        "qa": [
            {"question": "What population stability index value triggers automatic retraining review?",
             "answer": "Above 0.3, with investigation triggered above 0.2.",
             "evidence": "A population stability index above 0.2 on any feature triggers investigation; above 0.3 triggers automatic retraining review"},
            {"question": "What is the acceptance threshold for demographic parity difference?",
             "answer": "Below 0.1.",
             "evidence": "parity difference below 0.1 and an equal opportunity difference below 0.1"},
            {"question": "What service level applies to human review of middle-band predictions?",
             "answer": "Four business hours.",
             "evidence": "routed to a human reviewer with a service level of four business hours"},
            {"question": "Which two features were found to act as proxies for protected attributes?",
             "answer": "Postcode and device tier.",
             "evidence": "Postcode and device tier have previously acted as proxies for protected attributes"},
            {"question": "How long are late labels backfilled before outcome drift is trusted?",
             "answer": "30 days.",
             "evidence": "Labels that arrive late are backfilled for 30 days before outcome drift is trusted"},
        ],
    },
    {
        "id": "DAT-STD-021",
        "title": "Data Warehouse Modelling Conventions",
        "doc_type": "Standard",
        "category": "Data and Analytics",
        "department": "Data Engineering",
        "author": "Wei Zhang, Lead Analytics Engineer",
        "owner": "Data Engineering",
        "version": "4.0",
        "effective": "2026-02-01",
        "classification": "Internal",
        "review": "Annual",
        "summary": (
            "The modelling conventions for the Northwind warehouse: layering, "
            "naming, the choice of fact and dimension types, slowly changing "
            "dimension handling, incremental materialisation strategy, "
            "partitioning, and the code review rules for models."
        ),
        "tags": ["warehouse", "dbt", "modelling", "dimensions", "facts", "partitioning", "naming"],
        "sections": [
            {
                "heading": "Layering",
                "paragraphs": [
                    "The warehouse uses four layers. Source is a faithful mirror "
                    "of the source system and is never queried directly. Staging "
                    "renames columns to the standard vocabulary, casts types, and "
                    "does nothing else. Intermediate joins and business-rules "
                    "logic live here. Mart is dimensional, wide, and the only "
                    "layer consumers read.",
                    "The rule that keeps the warehouse maintainable is that "
                    "business logic lives in exactly one place. If a metric is "
                    "defined in a mart, no intermediate model may redefine it, "
                    "and if two marts need the same logic it moves down into an "
                    "intermediate model."
                ],
            },
            {
                "heading": "Naming Conventions",
                "paragraphs": [
                    "Models are named layer_entity_grain, all lower snake case. "
                    "Facts end in _fact, dimensions in _dim, and bridges in "
                    "_bridge. Boolean columns are prefixed is_ or has_. Date "
                    "columns end in _date and timestamps end in _at and are "
                    "stored in UTC. Currency columns carry the currency code "
                    "suffix when the table holds more than one currency.",
                    "Ambiguous names are prohibited. Columns called value, "
                    "amount, status, or type must be qualified, for example "
                    "invoice_amount_usd or subscription_status. This rule exists "
                    "because unqualified status columns have caused several "
                    "wrong-number incidents where two different statuses were "
                    "compared."
                ],
                "table": [
                    ["Construct", "Pattern", "Example", "Notes"],
                    ["Staging model", "stg_source_entity", "stg_stripe_invoice", "One model per source table"],
                    ["Intermediate", "int_concept_description", "int_subscription_active_daily", "Business logic lives here"],
                    ["Fact", "fct_entity_grain_fact", "fct_invoice_line_fact", "Grain stated in the name"],
                    ["Dimension", "dim_entity", "dim_account", "Surrogate key named account_key"],
                    ["Bridge", "bridge_entity_relationship", "bridge_account_agency", "Many-to-many"],
                ],
            },
            {
                "heading": "Fact and Dimension Types",
                "paragraphs": [
                    "Three fact types are used. Transaction facts hold one row "
                    "per event at the event's natural grain and are immutable. "
                    "Periodic snapshot facts hold one row per entity per period, "
                    "typically daily, and are used for balances such as active "
                    "seats. Accumulating snapshot facts track a process with "
                    "multiple milestones in one row and are updated as milestones "
                    "complete, which makes them the only mutable fact type.",
                    "Grain must be declared in the model documentation before the "
                    "model is merged, and a model without a declared grain fails "
                    "review. Declaring grain is what makes a duplicate-row defect "
                    "detectable, because the uniqueness test is derived from it."
                ],
            },
            {
                "heading": "Slowly Changing Dimensions",
                "paragraphs": [
                    "Type 2 is the default for attributes where history matters, "
                    "which includes account plan, owner, and industry. Type 1 is "
                    "permitted only where history has no business meaning, such "
                    "as a corrected spelling. A Type 2 dimension carries "
                    "valid_from, valid_to, and is_current, and every Type 2 "
                    "attribute change must be traceable to a source change.",
                    "Late-arriving dimension records are handled by inserting the "
                    "historical row and re-pointing affected facts, which is run "
                    "as a scheduled backfill rather than ad hoc. Facts must never "
                    "point at a current dimension row for a historical event, "
                    "because that silently rewrites history."
                ],
                "bullets": [
                    "Type 2 default for plan, owner, industry, and any attribute used in trend analysis.",
                    "Type 1 only where history has no business meaning.",
                    "Type 2 requires valid_from, valid_to, and is_current.",
                    "Late-arriving dimensions are handled by scheduled backfill, never ad hoc.",
                ],
            },
            {
                "heading": "Incremental Strategy and Partitioning",
                "paragraphs": [
                    "Large tables are incremental, keyed on the natural key and "
                    "the event timestamp, with a nightly full-refresh "
                    "reconciliation of the trailing 7 days to catch late "
                    "arrivals. Full refresh of a table above 500 gigabytes "
                    "requires approval because of cost and runtime.",
                    "Partitioning is by the analytics date, not the ingestion "
                    "date, and clustering is applied to the columns most often "
                    "used in filters, which for most marts is account_id and "
                    "event_date. A model that scans more than 100 gigabytes per "
                    "run is flagged in the weekly cost report and must be "
                    "re-partitioned or clustered."
                ],
                "qa": [
                    {
                        "question": "Which layer may consumers query?",
                        "answer": "Mart only.",
                    },
                    {
                        "question": "Which fact type is mutable?",
                        "answer": "Accumulating snapshot facts, which are updated as milestones complete.",
                    },
                    {
                        "question": "What suffix do timestamp columns use and in what zone are they stored?",
                        "answer": "_at, stored in UTC.",
                    },
                ],
            },
        ],
        "qa": [
            {"question": "Which warehouse layer are consumers allowed to query?",
             "answer": "Mart only; source and staging must not be queried directly.",
             "evidence": "Mart is dimensional, wide, and the only layer consumers read"},
            {"question": "Which fact type is the only mutable one?",
             "answer": "Accumulating snapshot facts.",
             "evidence": "which makes them the only mutable fact type"},
            {"question": "What suffix must timestamp columns use and in what timezone are they stored?",
             "answer": "_at, stored in UTC.",
             "evidence": "timestamps end in _at and are stored in UTC"},
            {"question": "What triggers a model to be flagged in the weekly cost report?",
             "answer": "Scanning more than 100 gigabytes per run.",
             "evidence": "A model that scans more than 100 gigabytes per run is flagged in the weekly cost report"},
            {"question": "How are late-arriving dimension records handled?",
             "answer": "By inserting the historical row and re-pointing affected facts via a scheduled backfill, never ad hoc.",
             "evidence": "handled by inserting the historical row and re-pointing affected facts, which is run as a scheduled backfill"},
        ],
    },
]
