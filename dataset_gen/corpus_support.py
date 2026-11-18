"""Customer support and success corpus (5 documents)."""

DOCS = [
    {
        "id": "SUP-SOP-003",
        "title": "Support Triage and Escalation Procedure",
        "doc_type": "Procedure",
        "category": "Customer Support",
        "department": "Customer Success",
        "author": "Marta Kowalska, Support Operations Manager",
        "owner": "Support Operations",
        "version": "6.0",
        "effective": "2026-01-15",
        "classification": "Internal",
        "review": "Quarterly",
        "summary": (
            "How Northwind support agents triage incoming tickets, assign "
            "business hours and severity, route to the correct queue, escalate "
            "to engineering, and handle executive and churn-risk escalations. "
            "Includes the severity definitions and the response commitments by "
            "plan."
        ),
        "tags": ["support", "triage", "escalation", "severity", "SLA", "routing"],
        "sections": [
            {
                "heading": "Triage Steps",
                "paragraphs": [
                    "Triage happens within 30 minutes of ticket creation during "
                    "staffed hours and is performed by the triage queue, not by "
                    "the assigned agent. The triage agent confirms the customer, "
                    "the plan, the affected site or workspace, reproduces the "
                    "issue where possible, and sets severity and queue. A ticket "
                    "may be re-triaged once by a senior agent; repeated "
                    "re-triage is a routing defect and is reported weekly.",
                    "Tickets that cannot be reproduced are not closed. They are "
                    "moved to a needs-information state with a specific ask and "
                    "an automatic reminder at 3 days and 10 days, then closed at "
                    "14 days of silence with a documented reason."
                ],
                "steps": [
                    "Confirm the customer identity, plan, and support entitlement from the account record.",
                    "Identify the affected workspace, site, or integration and record the environment.",
                    "Attempt reproduction in the sandbox using the customer's steps.",
                    "Assign severity using the definitions below and select the destination queue.",
                    "Send the first substantive reply, which must state what happens next and when.",
                    "Link the ticket to any existing incident or known issue rather than duplicating it.",
                ],
            },
            {
                "heading": "Severity Definitions",
                "paragraphs": [
                    "Severity reflects business impact on the customer, not the "
                    "number of tickets. A single enterprise customer whose "
                    "publish pipeline is broken is Sev 1 even if only one "
                    "account is affected. Severity may be raised by the customer "
                    "and is then reviewed by a senior agent within one hour."
                ],
                "table": [
                    ["Severity", "Definition", "Examples", "First response", "Update cadence"],
                    ["Sev 1", "Production down or data loss for the customer", "Publish fails site-wide, API returning 5xx, data loss", "30 minutes", "Every hour"],
                    ["Sev 2", "Major function unusable, no workaround", "Forms not submitting, SSO broken, editor unusable", "2 hours", "Every 4 hours"],
                    ["Sev 3", "Function impaired with a workaround", "Slow publish, broken layout on one template", "8 business hours", "Daily"],
                    ["Sev 4", "Question, cosmetic, or feature request", "How do I schedule a post", "1 business day", "On progress"],
                ],
            },
            {
                "heading": "Response Commitments by Plan",
                "paragraphs": [
                    "Commitments are contractual and are reported monthly to the "
                    "customer in the account health report. Standard and "
                    "Professional are staffed 8x5 in the customer's local "
                    "business hours. Enterprise is 24x5 for Sev 1 and Sev 2 and "
                    "8x5 otherwise. Business hours are defined per contract, "
                    "which matters because a customer in Sydney on a US contract "
                    "has a different clock from one in Berlin.",
                    "Breaching a first-response commitment is tracked as a "
                    "service credit exposure. Where a Sev 1 commitment is missed "
                    "twice in a rolling quarter, the account is flagged for "
                    "review by the Customer Success Manager and the support "
                    "director."
                ],
                "table": [
                    ["Plan", "Coverage", "Sev 1 response", "Sev 2 response", "Channels"],
                    ["Standard", "8x5 local", "8 business hours", "1 business day", "Email, community"],
                    ["Professional", "8x5 local", "4 business hours", "8 business hours", "Email, chat"],
                    ["Enterprise", "24x5 for Sev 1-2", "30 minutes", "2 hours", "Email, chat, phone, shared channel"],
                ],
            },
            {
                "heading": "Escalation to Engineering",
                "paragraphs": [
                    "Escalation requires a reproduction, the environment, the "
                    "expected and actual behaviour, and the customer impact "
                    "statement. Tickets escalated without a reproduction are "
                    "returned once with a specific ask rather than worked "
                    "speculatively, which is the single biggest driver of "
                    "engineering rework in support.",
                    "Sev 1 escalations page the on-call engineer directly and "
                    "open an incident under SEC-STD-005 if more than one "
                    "customer is affected. Sev 2 escalations route to the "
                    "owning team's queue with a 24 hour response expectation. "
                    "Agent-to-engineer direct messages are discouraged because "
                    "they bypass the queue and lose the audit trail."
                ],
                "bullets": [
                    "Always attach a reproduction, environment, expected and actual behaviour, and impact.",
                    "Sev 1 pages on-call and opens an incident if multi-customer.",
                    "Returned escalations get one specific ask, not a rejection.",
                    "Churn-risk accounts escalate to the CSM in parallel, never instead.",
                ],
            },
            {
                "heading": "Special Escalation Paths",
                "paragraphs": [
                    "Executive escalations, meaning a request from a customer "
                    "executive or an internal executive, are handled by the "
                    "support director and acknowledged within 30 minutes "
                    "regardless of severity. The acknowledgement is not a "
                    "diagnosis and must not be presented as one.",
                    "Churn-risk escalations are triggered by the account health "
                    "score falling below 60, by three Sev 1 tickets in 30 days, "
                    "or by an explicit cancellation intent. All three notify the "
                    "Customer Success Manager automatically and require a "
                    "save-plan document within two business days."
                ],
                "qa": [
                    {
                        "question": "How quickly must a Sev 1 ticket receive a first response on Enterprise?",
                        "answer": "Within 30 minutes.",
                    },
                    {
                        "question": "What must an escalation to engineering include?",
                        "answer": "A reproduction, the environment, expected and actual behaviour, and a customer impact statement.",
                    },
                    {
                        "question": "When is a churn-risk escalation triggered?",
                        "answer": "Health score below 60, three Sev 1 tickets in 30 days, or explicit cancellation intent.",
                    },
                ],
            },
        ],
        "qa": [
            {"question": "What is the Sev 1 first response commitment for Enterprise customers?",
             "answer": "30 minutes.",
             "evidence": "Enterprise | 24x5 for Sev 1-2 | 30 minutes"},
            {"question": "How often must a Sev 1 ticket be updated?",
             "answer": "Every hour.",
             "evidence": "Sev 1 ... 30 minutes | Every hour"},
            {"question": "What triggers a churn-risk escalation?",
             "answer": "Account health score below 60, three Sev 1 tickets in 30 days, or explicit cancellation intent.",
             "evidence": "account health score falling below 60, by three Sev 1 tickets in 30 days, or by an explicit cancellation intent"},
            {"question": "How long before a needs-information ticket is closed?",
             "answer": "14 days of silence, with reminders at 3 and 10 days.",
             "evidence": "an automatic reminder at 3 days and 10 days, then closed at 14 days of silence"},
            {"question": "Within how long must an executive escalation be acknowledged?",
             "answer": "30 minutes, regardless of severity.",
             "evidence": "acknowledged within 30 minutes regardless of severity"},
        ],
    },
    {
        "id": "SUP-KB-007",
        "title": "Troubleshooting Guide: Publishing and CDN Cache Issues",
        "doc_type": "Knowledge Base",
        "category": "Customer Support",
        "department": "Technical Support",
        "author": "Diego Ferreira, Senior Support Engineer",
        "owner": "Technical Support",
        "version": "5.3",
        "effective": "2026-06-01",
        "classification": "Internal",
        "review": "Quarterly",
        "summary": (
            "Diagnostic guide for the most common support category: pages not "
            "updating after publish. Covers the publish pipeline stages, cache "
            "invalidation, the diagnostic decision tree, the log sources to "
            "check in order, and the fixes for the eight most common root causes."
        ),
        "tags": ["publishing", "cache", "CDN", "troubleshooting", "stale content", "invalidation"],
        "sections": [
            {
                "heading": "Publish Pipeline Stages",
                "paragraphs": [
                    "A publish runs in five stages, and knowing which stage "
                    "failed is most of the diagnosis. Build compiles content "
                    "into artefacts. Validate checks schema and links. Deploy "
                    "atomically swaps the artefact version. Invalidate purges "
                    "the CDN entries for affected paths. Verify confirms the new "
                    "version is serving from at least two edge regions.",
                    "A publish is reported successful when Deploy completes, "
                    "which is why a customer can see a green publish and still "
                    "see old content: Invalidate or Verify may have failed "
                    "afterwards. Always check the publish record's stage "
                    "breakdown rather than the overall status badge."
                ],
                "table": [
                    ["Stage", "Typical duration", "Failure symptom", "Log source"],
                    ["Build", "20-90 s", "Build error in editor, no version created", "build-worker"],
                    ["Validate", "3-8 s", "Publish blocked with validation report", "validator"],
                    ["Deploy", "2-5 s", "Version created but not active", "deploy-controller"],
                    ["Invalidate", "5-30 s", "New version active, edge serving stale", "cdn-invalidator"],
                    ["Verify", "5-15 s", "Regional inconsistency", "edge-probe"],
                ],
            },
            {
                "heading": "Diagnostic Decision Tree",
                "paragraphs": [
                    "Start by asking whether the change appears in the preview "
                    "URL. If it does not, the problem is upstream of the CDN and "
                    "is a build or content problem. If it does, the problem is "
                    "the CDN, the browser, or a downstream cache.",
                    "Next, fetch the response headers for the affected URL. The "
                    "x-nw-version header identifies which artefact version the "
                    "edge served, and the x-nw-cache header states HIT, MISS, or "
                    "BYPASS. A HIT carrying an old version means invalidation "
                    "failed. A MISS carrying an old version means the deploy did "
                    "not activate. This two-header check resolves roughly 70 "
                    "percent of these tickets without engineering involvement."
                ],
                "steps": [
                    "Open the preview URL and confirm whether the change is present.",
                    "Fetch the live URL with cache disabled in the browser to rule out local caching.",
                    "Read x-nw-version and x-nw-cache from the response headers.",
                    "Compare the served version against the publish record's active version.",
                    "If the version is correct but content is old, check for a downstream proxy or customer WAF.",
                    "If the version is old and cache is HIT, request a targeted purge for the affected paths.",
                ],
            },
            {
                "heading": "Common Root Causes",
                "paragraphs": [
                    "The eight causes below account for 84 percent of "
                    "publish-related tickets. The listed fix is the correct "
                    "customer-facing action; do not offer a purge as a fix for a "
                    "cause where purging does not help, because it teaches "
                    "customers to rely on a workaround."
                ],
                "table": [
                    ["Cause", "Share", "Signal", "Fix"],
                    ["Browser or service worker cache", "26 percent", "Preview correct, live stale, no HIT on edge", "Hard refresh, unregister service worker"],
                    ["Purge failed on wildcard path rule", "18 percent", "HIT with old version on some paths only", "Targeted purge, then file defect NW-4412"],
                    ["Scheduled publish not yet due", "13 percent", "Publish record shows scheduled", "Confirm timezone on the schedule"],
                    ["Content scheduled in a different locale", "11 percent", "One locale updated, others not", "Publish each locale explicitly"],
                    ["Customer WAF caching HTML", "9 percent", "Edge correct, customer sees old", "Ask customer to purge their WAF"],
                    ["Build cached a stale dependency", "7 percent", "Component unchanged after update", "Force rebuild with no cache"],
                    ["Redirect rule masking new page", "5 percent", "New URL 301s to old", "Correct redirect rule order"],
                    ["Entitlement gate serving fallback", "3 percent", "Plan-gated block hidden", "Check plan and feature flags"],
                ],
            },
            {
                "heading": "Escalation Criteria",
                "paragraphs": [
                    "Escalate to the Platform team when the served version is "
                    "old and the cache header is MISS, which indicates a deploy "
                    "activation problem, or when edge probes report regional "
                    "inconsistency. Escalate to the Content team when the build "
                    "succeeds but the artefact is missing content.",
                    "Do not escalate when the fix is a purge, a service worker "
                    "unregistration, or a customer-side WAF purge. Those are "
                    "support-resolvable and escalating them consumes engineering "
                    "capacity that is reserved for genuine defects."
                ],
                "notes": [
                    "Customer communication: never tell a customer the platform "
                    "is down because one URL is stale. Confirm the platform "
                    "status page and the edge probe results before using the "
                    "word outage."
                ],
            },
            {
                "heading": "Useful Commands and Endpoints",
                "paragraphs": [
                    "Support agents have read access to three internal endpoints "
                    "that answer most questions without engineering. The publish "
                    "record endpoint returns the stage breakdown and timings. The "
                    "edge probe endpoint returns the served version from each "
                    "region. The purge history endpoint shows every purge "
                    "requested in the last 72 hours and its result.",
                    "Always attach the publish record identifier and the affected "
                    "URL to the ticket before escalating. An escalation without a "
                    "publish identifier cannot be actioned and will be returned."
                ],
                "qa": [
                    {
                        "question": "Which two response headers identify a stale content problem?",
                        "answer": "x-nw-version and x-nw-cache.",
                    },
                    {
                        "question": "What is the most common root cause of stale content tickets?",
                        "answer": "Browser or service worker cache, at 26 percent.",
                    },
                    {
                        "question": "When does a green publish still show old content?",
                        "answer": "When Invalidate or Verify failed after Deploy, because success is reported at Deploy completion.",
                    },
                ],
            },
        ],
        "qa": [
            {"question": "Which two response headers diagnose stale published content?",
             "answer": "x-nw-version and x-nw-cache.",
             "evidence": "The x-nw-version header identifies which artefact version the edge served, and the x-nw-cache header states HIT, MISS, or BYPASS"},
            {"question": "What share of publish tickets do the eight common causes cover?",
             "answer": "84 percent.",
             "evidence": "The eight causes below account for 84 percent of publish-related tickets"},
            {"question": "Why can a publish report success while content stays stale?",
             "answer": "Because success is reported when Deploy completes, so Invalidate or Verify may still have failed.",
             "evidence": "A publish is reported successful when Deploy completes"},
            {"question": "What is the most frequent root cause of stale content?",
             "answer": "Browser or service worker cache, at 26 percent.",
             "evidence": "Browser or service worker cache | 26 percent"},
            {"question": "What defect number applies to wildcard path purge failures?",
             "answer": "NW-4412.",
             "evidence": "Targeted purge, then file defect NW-4412"},
        ],
    },
    {
        "id": "SUP-STD-012",
        "title": "Customer Success Onboarding Standard",
        "doc_type": "Standard",
        "category": "Customer Support",
        "department": "Customer Success",
        "author": "Aisha Bello, Director of Customer Success",
        "owner": "Customer Success",
        "version": "3.2",
        "effective": "2026-02-01",
        "classification": "Internal",
        "review": "Annual",
        "summary": (
            "Defines the Northwind onboarding programme: segment-based "
            "onboarding tracks, the 90-day milestone plan, time-to-value "
            "definitions and targets, health scoring, the handover from sales, "
            "and the criteria for graduating an account to business as usual."
        ),
        "tags": ["onboarding", "customer success", "time to value", "health score", "adoption", "handover"],
        "sections": [
            {
                "heading": "Onboarding Tracks",
                "paragraphs": [
                    "Onboarding intensity is set by contract value and "
                    "complexity, not by the customer's request. High-touch "
                    "onboarding is assigned to accounts above 50,000 USD annual "
                    "value or with a migration of more than 500 pages. "
                    "Technology-assisted onboarding covers everything else and "
                    "relies on in-product guidance and cohort webinars.",
                    "An account may be promoted to high-touch once during "
                    "onboarding if it stalls, but may not be demoted, because a "
                    "demoted account almost always churns."
                ],
                "table": [
                    ["Track", "Trigger", "CSM ratio", "Duration", "Sessions included"],
                    ["High-touch", "Above 50,000 USD or 500+ page migration", "1:35", "90 days", "8"],
                    ["Mid-touch", "15,000-50,000 USD", "1:80", "60 days", "3"],
                    ["Tech-touch", "Below 15,000 USD", "1:250", "Self-paced", "0"],
                    ["Migration", "Any value, competitive replatform", "1:20", "120 days", "12"],
                ],
            },
            {
                "heading": "90-Day Milestone Plan",
                "paragraphs": [
                    "Onboarding is measured against five milestones. Kickoff "
                    "within 5 business days of the contract start. Success plan "
                    "agreed within 10 business days, naming the outcomes the "
                    "customer is buying and the owner on their side. First "
                    "production publish within 30 days. Third team member active "
                    "within 45 days. Value review at day 75 with a written "
                    "outcome assessment.",
                    "The milestone that predicts retention best is the third "
                    "active team member. Accounts that reach three active "
                    "authors by day 45 renew at 94 percent; accounts that reach "
                    "only one renew at 61 percent. That gap is why the milestone "
                    "exists even when the customer says they do not need it."
                ],
                "table": [
                    ["Milestone", "Target", "Renewal rate if met", "Owner"],
                    ["Kickoff held", "5 business days", "89 percent", "CSM"],
                    ["Success plan agreed", "10 business days", "91 percent", "CSM and sponsor"],
                    ["First production publish", "30 days", "93 percent", "Customer with CSM support"],
                    ["Third active team member", "45 days", "94 percent", "Customer sponsor"],
                    ["Value review completed", "Day 75", "96 percent", "CSM"],
                ],
            },
            {
                "heading": "Time to Value",
                "paragraphs": [
                    "Time to value is measured from contract start to the first "
                    "moment the customer achieves the outcome named in their "
                    "success plan, not to first login. The current median is 34 "
                    "days for high-touch and 51 days for tech-touch. The target "
                    "is 25 days for high-touch, and the gap is concentrated in "
                    "migration accounts where content transfer is the bottleneck.",
                    "Where a customer cannot reach value within 90 days, the CSM "
                    "must raise a stall escalation with a named blocker and a "
                    "recovery plan. Stalled accounts are reviewed weekly by the "
                    "Customer Success Manager's director, and a stall older than "
                    "30 days is reported to the Executive Staff."
                ],
                "bullets": [
                    "Time to value is measured to the success-plan outcome, not to login.",
                    "Median TTV is 34 days high-touch and 51 days tech-touch.",
                    "A stall older than 30 days is reported to the Executive Staff.",
                    "Migration accounts are the main TTV bottleneck.",
                ],
            },
            {
                "heading": "Health Scoring",
                "paragraphs": [
                    "Health is a composite score from 0 to 100 built from five "
                    "signals: adoption breadth, which is active users against "
                    "seats; depth of use, which is features adopted against "
                    "available; support load, weighted by severity; sponsor "
                    "engagement, measured by meetings in the last 90 days; and "
                    "contract proximity, which is days to renewal. Weights are "
                    "adoption 30, depth 25, support 20, sponsor 15, proximity 10.",
                    "A score below 60 triggers a save plan. A score below 40 "
                    "triggers an executive sponsor assignment. Health is a "
                    "prompt for conversation, not a verdict, and must never be "
                    "quoted to a customer as a number."
                ],
            },
            {
                "heading": "Sales Handover and Graduation",
                "paragraphs": [
                    "The sales-to-success handover happens within 3 business days "
                    "of signature and uses the Handover Record, which captures "
                    "the promised outcomes, the stakeholders and their "
                    "positions, the commercial context, and any commitments made "
                    "that are not in the contract. Verbal commitments not "
                    "recorded are the most common source of early friction.",
                    "An account graduates from onboarding to business as usual "
                    "when it has completed the value review, reached at least "
                    "two active authors, and has no open Sev 1 or Sev 2 ticket. "
                    "Graduation is not automatic on day 90; an account that has "
                    "not met the criteria stays in onboarding with a documented "
                    "reason."
                ],
                "qa": [
                    {
                        "question": "What triggers high-touch onboarding?",
                        "answer": "A contract above 50,000 USD annual value or a migration of more than 500 pages.",
                    },
                    {
                        "question": "Which milestone best predicts renewal?",
                        "answer": "A third active team member by day 45, which correlates with 94 percent renewal.",
                    },
                    {
                        "question": "What health score triggers a save plan?",
                        "answer": "Below 60.",
                    },
                ],
            },
        ],
        "qa": [
            {"question": "What contract value triggers high-touch onboarding?",
             "answer": "Above 50,000 USD annual value, or a migration of more than 500 pages.",
             "evidence": "High-touch onboarding is assigned to accounts above 50,000 USD annual value or with a migration of more than 500 pages"},
            {"question": "What renewal rate is associated with three active authors by day 45?",
             "answer": "94 percent.",
             "evidence": "Accounts that reach three active authors by day 45 renew at 94 percent"},
            {"question": "What is the current median time to value for high-touch accounts?",
             "answer": "34 days.",
             "evidence": "The current median is 34 days for high-touch and 51 days for tech-touch"},
            {"question": "What weight does adoption breadth carry in the health score?",
             "answer": "30 of 100.",
             "evidence": "Weights are adoption 30, depth 25, support 20, sponsor 15, proximity 10"},
            {"question": "Within how many business days must the sales-to-success handover occur?",
             "answer": "3 business days of signature.",
             "evidence": "The sales-to-success handover happens within 3 business days of signature"},
        ],
    },
    {
        "id": "SUP-STD-018",
        "title": "Service Level Agreement Framework",
        "doc_type": "Framework",
        "category": "Customer Support",
        "department": "Customer Success",
        "author": "Marta Kowalska, Support Operations Manager",
        "owner": "Customer Success and Legal",
        "version": "4.4",
        "effective": "2026-01-01",
        "classification": "Public",
        "review": "Annual",
        "summary": (
            "The Northwind availability and support SLA framework: the "
            "availability commitment and how it is measured, the service credit "
            "schedule and claim process, exclusions, the support response "
            "commitments, and the reporting customers receive."
        ),
        "tags": ["SLA", "availability", "service credits", "uptime", "commitment", "exclusions"],
        "sections": [
            {
                "heading": "Availability Commitment",
                "paragraphs": [
                    "Northwind commits to 99.9 percent monthly availability for "
                    "the content delivery and editing services, measured per "
                    "calendar month. Availability is measured at the edge as the "
                    "proportion of successful requests, using synthetic probes "
                    "every 60 seconds from 12 regions plus real user traffic. A "
                    "request is unsuccessful when it returns a server error "
                    "between 500 and 509 attributable to Northwind.",
                    "99.9 percent permits 43 minutes and 49 seconds of "
                    "unavailability in a 30-day month. Authoring services carry "
                    "the same commitment but are measured separately, so an "
                    "authoring outage does not create a delivery credit and vice "
                    "versa."
                ],
                "table": [
                    ["Monthly availability", "Permitted downtime, 30-day month", "Service credit"],
                    ["99.9 percent or better", "43 min 49 s or less", "None"],
                    ["99.0 to 99.9 percent", "Up to 7 h 12 m", "10 percent of monthly fee"],
                    ["95.0 to 99.0 percent", "Up to 36 h", "25 percent of monthly fee"],
                    ["Below 95.0 percent", "More than 36 h", "50 percent of monthly fee"],
                ],
            },
            {
                "heading": "Exclusions",
                "paragraphs": [
                    "Downtime is excluded where it is caused by customer "
                    "configuration, by a third party outside Northwind's control "
                    "such as the DNS provider or the customer's own WAF, by "
                    "force majeure, or by notifiable maintenance announced at "
                    "least 72 hours in advance. Notifiable maintenance is capped "
                    "at 4 hours per month and must be scheduled outside the "
                    "customer's declared peak window.",
                    "Beta and limited-availability features are excluded from the "
                    "commitment, which is stated in the service description "
                    "rather than buried in the contract. Features in preview are "
                    "labelled in the product so that customers can see the "
                    "distinction without reading legal text."
                ],
                "bullets": [
                    "Excluded: customer configuration, third-party DNS or WAF, force majeure.",
                    "Excluded: notifiable maintenance announced 72 hours ahead, capped at 4 hours per month.",
                    "Excluded: beta and preview features.",
                    "Included: any Northwind-attributable 500-509 response at the edge.",
                ],
            },
            {
                "heading": "Claiming a Service Credit",
                "paragraphs": [
                    "Credits are claimed by the customer within 30 days of the "
                    "end of the affected month, by email to the named support "
                    "address with the affected service and period. Northwind "
                    "responds within 10 business days. Credits are applied to the "
                    "next invoice and are not paid in cash.",
                    "Total credits in any month are capped at 50 percent of that "
                    "month's fee, which is the highest tier of the schedule. "
                    "Customers may not claim both a service credit and terminate "
                    "for the same incident window. Repeated breaches, defined as "
                    "three months below commitment in a rolling six, give the "
                    "customer a termination right without penalty."
                ],
            },
            {
                "heading": "Support Response Commitments",
                "paragraphs": [
                    "Support commitments are separate from availability and are "
                    "defined by severity and plan, as set out in "
                    "SUP-SOP-003. The Enterprise commitment of 30 minutes to "
                    "first response on Sev 1 is contractual; the remaining "
                    "figures are targets that are reported but do not create "
                    "credits.",
                    "Northwind publishes monthly availability on the public "
                    "status page and provides Enterprise customers a per-account "
                    "report showing their measured availability, ticket history, "
                    "and credit exposure. The report is issued on the fifth "
                    "business day of each month."
                ],
                "qa": [
                    {
                        "question": "What downtime does 99.9 percent monthly availability permit?",
                        "answer": "43 minutes and 49 seconds in a 30-day month.",
                    },
                    {
                        "question": "Within how long must a customer claim a service credit?",
                        "answer": "Within 30 days of the end of the affected month.",
                    },
                    {
                        "question": "What is the maximum total credit in a month?",
                        "answer": "50 percent of that month's fee.",
                    },
                ],
            },
            {
                "heading": "Measurement Disputes",
                "paragraphs": [
                    "Where a customer disputes a measurement, Support opens a "
                    "review comparing the customer's evidence against Northwind "
                    "probe data and real user traffic for the same window. "
                    "Disputes are resolved within 10 business days and the "
                    "decision is made by the Support Operations Manager, not by "
                    "the account team.",
                    "The most common dispute is scope: the customer measures a "
                    "page that includes third-party scripts, while Northwind "
                    "measures its own responses. Where a third-party script "
                    "delays rendering, the page is slow but the service is "
                    "available, and the SLA does not apply."
                ],
            },
        ],
        "qa": [
            {"question": "What availability does Northwind commit to monthly?",
             "answer": "99.9 percent for content delivery and editing, measured separately.",
             "evidence": "Northwind commits to 99.9 percent monthly availability for the content delivery and editing services"},
            {"question": "How much downtime does 99.9 percent permit in a 30-day month?",
             "answer": "43 minutes and 49 seconds.",
             "evidence": "99.9 percent permits 43 minutes and 49 seconds of unavailability in a 30-day month"},
            {"question": "What is the service credit for availability between 99.0 and 99.9 percent?",
             "answer": "10 percent of the monthly fee.",
             "evidence": "99.0 to 99.9 percent | Up to 7 h 12 m | 10 percent of monthly fee"},
            {"question": "How far in advance must notifiable maintenance be announced?",
             "answer": "At least 72 hours, capped at 4 hours per month.",
             "evidence": "notifiable maintenance announced at least 72 hours in advance"},
            {"question": "What repeated-breach condition gives a customer a termination right?",
             "answer": "Three months below commitment in a rolling six.",
             "evidence": "three months below commitment in a rolling six, give the customer a termination right without penalty"},
        ],
    },
    {
        "id": "SUP-STD-024",
        "title": "Voice of Customer and Feedback Loop Standard",
        "doc_type": "Standard",
        "category": "Customer Support",
        "department": "Customer Success",
        "author": "Aisha Bello, Director of Customer Success",
        "owner": "Customer Success",
        "version": "2.1",
        "effective": "2026-04-01",
        "classification": "Internal",
        "review": "Annual",
        "summary": (
            "How Northwind collects, classifies, and acts on customer feedback. "
            "Covers the feedback channels and their response commitments, the "
            "classification taxonomy, the monthly feedback review with product, "
            "NPS and CSAT measurement rules, and the closing-the-loop "
            "obligations to customers."
        ),
        "tags": ["voice of customer", "NPS", "CSAT", "feedback", "product feedback", "closing the loop"],
        "sections": [
            {
                "heading": "Channels and Commitments",
                "paragraphs": [
                    "Feedback arrives through six channels: support tickets, the "
                    "in-product feedback widget, the customer community, the "
                    "quarterly NPS survey, account business reviews, and "
                    "churn interviews. Every piece of feedback is captured in the "
                    "Feedback Hub within one business day of receipt, including "
                    "feedback heard verbally in a meeting.",
                    "The in-product widget is the highest-volume channel at "
                    "roughly 400 submissions per month and has the weakest "
                    "context, which is why the triage step adds the account "
                    "record, the plan, and the recent ticket history before "
                    "routing."
                ],
                "table": [
                    ["Channel", "Monthly volume", "Response commitment", "Owner"],
                    ["Support tickets", "2,100", "Per plan SLA", "Support"],
                    ["In-product widget", "400", "5 business days acknowledgement", "Customer Success"],
                    ["Community", "320", "3 business days", "Community manager"],
                    ["NPS survey", "Quarterly", "Individual follow-up within 5 days", "Customer Success"],
                    ["Business reviews", "60", "Actions logged same week", "CSM"],
                    ["Churn interviews", "14", "Summary to Product within 10 days", "Customer Success"],
                ],
            },
            {
                "heading": "Classification Taxonomy",
                "paragraphs": [
                    "Feedback is classified on three axes. Type is bug, "
                    "enhancement, documentation gap, or expectation mismatch. "
                    "Area is the product surface, using the same 24 areas as the "
                    "support taxonomy so that data joins cleanly. Value is the "
                    "commercial weight, scored from the number of distinct "
                    "accounts requesting it, the revenue those accounts "
                    "represent, and whether it blocks a renewal.",
                    "Expectation mismatch is the most useful and most ignored "
                    "category. It means the product works as designed but the "
                    "customer expected otherwise, which is usually a "
                    "documentation, naming, or default-settings problem rather "
                    "than a feature request. Roughly 22 percent of enhancement "
                    "requests are reclassified this way at triage."
                ],
                "bullets": [
                    "Type: bug, enhancement, documentation gap, expectation mismatch.",
                    "Area: the 24 product surfaces shared with the support taxonomy.",
                    "Value: distinct accounts, revenue weight, renewal blockage.",
                    "Duplicate feedback is merged to one record with multiple account links.",
                ],
            },
            {
                "heading": "Measurement Rules",
                "paragraphs": [
                    "NPS is surveyed quarterly to all admin users with a "
                    "minimum of 30 days of account history, using an invitation "
                    "email and an in-product prompt, deduplicated to one "
                    "response per account per quarter. The current score is 41 "
                    "with a 34 percent response rate. Promoters are 9 or 10, "
                    "passives 7 or 8, detractors 0 to 6.",
                    "CSAT is surveyed transactionally at ticket close and is "
                    "reported as a five-point mean, currently 4.3. CSAT is not "
                    "used to assess individual agents on low volume; a minimum of "
                    "20 responses in the period is required before an agent's "
                    "score is reported at all, because small samples produce "
                    "noise that damages trust in the metric."
                ],
                "notes": [
                    "Bias note: surveying only at ticket close over-represents "
                    "resolved cases. The quarterly survey exists to reach the "
                    "silent majority, and the two must be read together."
                ],
            },
            {
                "heading": "Monthly Review with Product",
                "paragraphs": [
                    "The Voice of Customer review runs on the second Thursday of "
                    "each month with Product, Support, and Customer Success. The "
                    "agenda is fixed: the top ten items by value, any item "
                    "blocking a renewal, items previously promised and now "
                    "shipped, and items declined with reasons. Renewal-blocking "
                    "items are never deferred to the next meeting.",
                    "Product must respond to every item reviewed with one of four "
                    "dispositions: planned, investigating, declined, or duplicate "
                    "of an existing item. Silence is not a disposition and is "
                    "escalated to the Head of Product."
                ],
            },
            {
                "heading": "Closing the Loop",
                "paragraphs": [
                    "Every customer who submitted feedback on an item that ships "
                    "is notified within 10 business days of general availability, "
                    "by name, with a link to the feature and an invitation to "
                    "try it. Notification is automatic from the Feedback Hub and "
                    "is not left to the account team, because manual follow-up "
                    "is the step that reliably fails.",
                    "Declined feedback must also be communicated, with the "
                    "reason. Customers accept a no far more readily than silence; "
                    "the most common complaint in the quarterly survey is not "
                    "that a request was refused but that nobody replied."
                ],
                "qa": [
                    {
                        "question": "What is the current NPS and response rate?",
                        "answer": "NPS 41 with a 34 percent response rate.",
                    },
                    {
                        "question": "When must customers be told their feedback shipped?",
                        "answer": "Within 10 business days of general availability, automatically.",
                    },
                    {
                        "question": "What minimum responses are needed before reporting an agent's CSAT?",
                        "answer": "20 responses in the period.",
                    },
                ],
            },
        ],
        "qa": [
            {"question": "What is Northwind's current NPS score and response rate?",
             "answer": "NPS 41 with a 34 percent response rate.",
             "evidence": "The current score is 41 with a 34 percent response rate"},
            {"question": "How quickly must customers be notified when their feedback ships?",
             "answer": "Within 10 business days of general availability.",
             "evidence": "notified within 10 business days of general availability"},
            {"question": "What is the current CSAT mean?",
             "answer": "4.3 on a five-point scale.",
             "evidence": "reported as a five-point mean, currently 4.3"},
            {"question": "What minimum CSAT responses are required before reporting an individual agent?",
             "answer": "20 responses in the period.",
             "evidence": "a minimum of 20 responses in the period is required before an agent's score is reported"},
            {"question": "When does the monthly Voice of Customer review occur?",
             "answer": "The second Thursday of each month.",
             "evidence": "The Voice of Customer review runs on the second Thursday of each month"},
        ],
    },
]
