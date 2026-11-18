"""Software engineering practices corpus (5 documents)."""

DOCS = [
    {
        "id": "ENG-STD-001",
        "title": "Engineering Code Review Standard",
        "doc_type": "Standard",
        "category": "Software Engineering",
        "department": "Engineering",
        "author": "Piotr Zawadzki, Principal Architect",
        "owner": "Engineering",
        "version": "5.1",
        "effective": "2026-01-01",
        "classification": "Internal",
        "review": "Annual",
        "summary": (
            "The Northwind code review standard: review scope and reviewer "
            "counts, turnaround targets, size limits, comment conventions and "
            "blocking levels, the rules for approvals and self-approval, and the "
            "quality metrics reported monthly."
        ),
        "tags": ["code review", "pull request", "reviewers", "turnaround", "quality"],
        "sections": [
            {
                "heading": "Review Requirements",
                "paragraphs": [
                    "No change reaches a production-bound branch without review. "
                    "One approving reviewer is the default; two are required for "
                    "security-relevant changes, database migrations, changes "
                    "above 400 lines, and any change to shared libraries used by "
                    "more than two teams. Self-approval is blocked by branch "
                    "protection and cannot be overridden.",
                    "Reviewers are chosen by the author, with at least one "
                    "reviewer who did not write the change and, for shared code, "
                    "one reviewer from the owning team. CODEOWNERS files are "
                    "enforced by the platform, so an owning team cannot be "
                    "skipped even if the author knows a member personally."
                ],
                "table": [
                    ["Change type", "Approvers", "Reviewer must be outside author's squad", "Merge method"],
                    ["Bug fix under 50 lines", "1", "No", "Squash"],
                    ["Feature", "1", "No", "Squash"],
                    ["Security-relevant", "2", "Yes", "Merge commit"],
                    ["Database migration", "2", "Yes", "Merge commit"],
                    ["Shared library", "2", "Yes, owning team", "Merge commit"],
                ],
            },
            {
                "heading": "Size and Turnaround",
                "paragraphs": [
                    "Pull requests should be under 400 changed lines and under "
                    "10 files. Larger changes must be stacked into a series or "
                    "carry a written justification in the description. Median "
                    "review turnaround is targeted at 4 business hours and "
                    "reviewers are expected to triage, not complete, within that "
                    "window by either approving, requesting changes, or "
                    "commenting that they need more time.",
                    "A pull request open longer than 5 business days is flagged "
                    "in the weekly report as stale. Stale pull requests are the "
                    "largest single source of merge conflict cost and are raised "
                    "in squad retrospectives when a squad's stale rate exceeds "
                    "15 percent."
                ],
                "bullets": [
                    "Target under 400 changed lines and 10 files per pull request.",
                    "Median review turnaround target of 4 business hours.",
                    "Triage within the window even if the full review takes longer.",
                    "Stale above 5 business days; squad escalation above a 15 percent stale rate.",
                ],
            },
            {
                "heading": "Comment Conventions",
                "paragraphs": [
                    "Comments are labelled by prefix so that authors know what is "
                    "required. blocking means the change must be made before "
                    "merge and is reserved for correctness, security, data loss, "
                    "and breach of a documented standard. suggestion is an "
                    "improvement the author may accept or decline. nit is "
                    "optional and must never be used for anything a linter could "
                    "enforce. question asks for explanation without implying a "
                    "defect.",
                    "Style arguments that cannot be automated are resolved by "
                    "adding a rule to the linter rather than by debating in a "
                    "thread. Threads longer than five comments must move to a "
                    "call and return with a written decision, because long "
                    "public threads discourage junior authors from opening "
                    "changes at all."
                ],
                "notes": [
                    "Tone note: comment on the code, never the author. Reviews "
                    "that use 'you' rather than 'this line' are called out by the "
                    "reviewer's manager in the monthly quality review."
                ],
            },
            {
                "heading": "What Reviewers Check",
                "paragraphs": [
                    "Reviewers check correctness, security, tests, observability, "
                    "and rollback. Observability means the change emits enough "
                    "logging and metrics to diagnose a failure in production "
                    "without a redeploy. Rollback means the description states "
                    "how to undo the change and, for migrations, that the "
                    "migration is backward compatible for at least one release.",
                    "Test coverage is not a gate; behaviour is. A change with no "
                    "new tests is acceptable where it changes no behaviour, and a "
                    "change with 90 percent coverage that does not test the "
                    "changed behaviour is not. Reviewers ask what would break if "
                    "this shipped wrong, and require a test that would catch it."
                ],
            },
            {
                "heading": "Quality Metrics",
                "paragraphs": [
                    "Four metrics are reported monthly by squad: median review "
                    "turnaround, stale rate, rubber-stamp rate, and revert rate. "
                    "A rubber-stamp review is an approval on a change above 100 "
                    "lines completed in under two minutes, and the current "
                    "company rate is 6 percent. A revert rate above 5 percent "
                    "triggers a review of the squad's testing approach.",
                    "These metrics measure the system, not individuals, and are "
                    "never used in performance assessment. Publishing individual "
                    "review speeds reliably produces fast, shallow reviews, which "
                    "is the opposite of the intent."
                ],
                "qa": [
                    {
                        "question": "How many approvers does a database migration need?",
                        "answer": "Two, including a reviewer outside the author's squad.",
                    },
                    {
                        "question": "What is the target median review turnaround?",
                        "answer": "4 business hours.",
                    },
                    {
                        "question": "What defines a rubber-stamp review?",
                        "answer": "An approval on a change above 100 lines completed in under two minutes.",
                    },
                ],
            },
        ],
        "qa": [
            {"question": "How many approvers are required for a security-relevant change?",
             "answer": "Two, with a reviewer outside the author's squad.",
             "evidence": "Security-relevant | 2 | Yes | Merge commit"},
            {"question": "What is the target median code review turnaround?",
             "answer": "4 business hours.",
             "evidence": "Median review turnaround is targeted at 4 business hours"},
            {"question": "After how many business days is a pull request considered stale?",
             "answer": "5 business days.",
             "evidence": "A pull request open longer than 5 business days is flagged in the weekly report as stale"},
            {"question": "What is the current company rubber-stamp review rate?",
             "answer": "6 percent.",
             "evidence": "the current company rate is 6 percent"},
            {"question": "What revert rate triggers a review of a squad's testing approach?",
             "answer": "Above 5 percent.",
             "evidence": "A revert rate above 5 percent triggers a review of the squad's testing approach"},
        ],
    },
    {
        "id": "ENG-STD-006",
        "title": "API Design Guidelines",
        "doc_type": "Guidelines",
        "category": "Software Engineering",
        "department": "Engineering",
        "author": "Ingrid Sørensen, API Design Lead",
        "owner": "Platform Engineering",
        "version": "3.5",
        "effective": "2026-03-01",
        "classification": "Public",
        "review": "Annual",
        "summary": (
            "Conventions for Northwind public and internal HTTP APIs: resource "
            "naming, versioning policy, pagination, filtering, error envelope, "
            "idempotency, rate limiting headers, and the deprecation process "
            "for public endpoints."
        ),
        "tags": ["API", "REST", "versioning", "pagination", "idempotency", "errors", "deprecation"],
        "sections": [
            {
                "heading": "Resource Naming",
                "paragraphs": [
                    "Paths use plural nouns, lower case, and hyphens for "
                    "multi-word resources. No verbs in paths, no camelCase, and "
                    "no more than two levels of nesting; deeper nesting signals "
                    "that the sub-resource should be top-level with a foreign "
                    "key filter. Actions that are genuinely not CRUD are modelled "
                    "as sub-resources with a verb, for example "
                    "/pages/{id}/actions/publish.",
                    "Version is carried in the path as v1, v2 and is mandatory "
                    "for all public endpoints. Internal services use content "
                    "type versioning instead, because path versioning leads to "
                    "forked implementations."
                ],
                "table": [
                    ["Concern", "Convention", "Example"],
                    ["Collection", "Plural noun", "GET /v1/pages"],
                    ["Single resource", "Identifier in path", "GET /v1/pages/{page_id}"],
                    ["Sub-resource", "One level only", "GET /v1/pages/{page_id}/versions"],
                    ["Non-CRUD action", "actions sub-resource", "POST /v1/pages/{page_id}/actions/publish"],
                    ["Filtering", "Query parameters", "GET /v1/pages?status=published&locale=en-GB"],
                ],
            },
            {
                "heading": "Versioning and Compatibility",
                "paragraphs": [
                    "A new major version is required for any breaking change: "
                    "removing a field, changing a field's type, changing the "
                    "meaning of a field, tightening validation, or changing a "
                    "status code. Adding an optional field, adding an endpoint, "
                    "or adding an optional query parameter is non-breaking and "
                    "does not need a new version.",
                    "Old major versions are supported for 18 months after the "
                    "new version's general availability. During that window both "
                    "versions must return equivalent data, which is verified by a "
                    "contract test that runs nightly against both."
                ],
                "bullets": [
                    "Breaking: remove a field, change a type, change semantics, tighten validation, change a status code.",
                    "Non-breaking: add optional field, add endpoint, add optional parameter, expand an enum.",
                    "Major versions supported 18 months after the successor's GA.",
                    "Never change the meaning of a field in place; add a new field instead.",
                ],
            },
            {
                "heading": "Pagination and Filtering",
                "paragraphs": [
                    "All collections are paginated with cursor pagination using "
                    "an opaque cursor and a limit parameter defaulting to 50 with "
                    "a maximum of 200. Offset pagination is prohibited on public "
                    "endpoints because it produces skipped and duplicated rows "
                    "when the underlying set changes during traversal.",
                    "The response includes a next_cursor that is null at the end "
                    "of the set. Sorting must be explicitly supported by a sort "
                    "parameter with a stable tiebreaker, normally the identifier, "
                    "so that cursors remain deterministic."
                ],
            },
            {
                "heading": "Errors and Idempotency",
                "paragraphs": [
                    "Errors use a single envelope with a machine-readable code, a "
                    "human-readable message, a request identifier for support, and "
                    "an optional details array for field-level validation. Codes "
                    "are stable strings such as validation_failed or "
                    "entitlement_required and are documented per endpoint. Never "
                    "put a stack trace or an internal identifier in a public "
                    "message.",
                    "All non-idempotent POST endpoints must accept an "
                    "Idempotency-Key header, store the response for 24 hours, and "
                    "replay it on retry. Without it, a client retry after a "
                    "timeout can create duplicate publishes, which has happened "
                    "twice.",
                    "Rate limits are communicated with X-RateLimit-Limit, "
                    "X-RateLimit-Remaining, and X-RateLimit-Reset, and exceeded "
                    "limits return 429 with a Retry-After header."
                ],
                "qa": [
                    {
                        "question": "Which pagination scheme is required for public collections?",
                        "answer": "Cursor pagination, with a default limit of 50 and a maximum of 200.",
                    },
                    {
                        "question": "How long are old major API versions supported?",
                        "answer": "18 months after the successor's general availability.",
                    },
                    {
                        "question": "How long is an idempotency response replayed?",
                        "answer": "24 hours.",
                    },
                ],
            },
            {
                "heading": "Deprecation Process",
                "paragraphs": [
                    "Deprecating a public endpoint requires a deprecation notice "
                    "in the changelog, a Deprecation response header with the "
                    "sunset date, a Sunset header, an entry in the API "
                    "documentation banner, and a minimum of 180 days before "
                    "removal. Where usage exceeds 1 percent of traffic, the "
                    "deprecation must also be emailed to affected account owners "
                    "with their own call volume attached.",
                    "An endpoint may not be removed while it carries more than "
                    "0.1 percent of traffic without an Executive Staff decision, "
                    "because late removal of a still-used endpoint is the fastest "
                    "way to lose an enterprise customer's trust."
                ],
            },
        ],
        "qa": [
            {"question": "What pagination scheme must Northwind public collections use?",
             "answer": "Cursor pagination with an opaque cursor, default limit 50, maximum 200.",
             "evidence": "All collections are paginated with cursor pagination using an opaque cursor and a limit parameter defaulting to 50 with a maximum of 200"},
            {"question": "How long are old major API versions supported after the successor ships?",
             "answer": "18 months.",
             "evidence": "Old major versions are supported for 18 months after the new version's general availability"},
            {"question": "How long are idempotency responses stored for replay?",
             "answer": "24 hours.",
             "evidence": "store the response for 24 hours, and replay it on retry"},
            {"question": "What is the minimum notice before removing a deprecated public endpoint?",
             "answer": "180 days, with Deprecation and Sunset headers.",
             "evidence": "a minimum of 180 days before removal"},
            {"question": "What traffic level blocks removing an endpoint without an Executive Staff decision?",
             "answer": "More than 0.1 percent of traffic.",
             "evidence": "An endpoint may not be removed while it carries more than 0.1 percent of traffic without an Executive Staff decision"},
        ],
    },
    {
        "id": "ENG-STD-011",
        "title": "Testing Strategy and Quality Gates",
        "doc_type": "Standard",
        "category": "Software Engineering",
        "department": "Engineering",
        "author": "Lucia Romano, Engineering Quality Lead",
        "owner": "Engineering",
        "version": "4.2",
        "effective": "2026-02-15",
        "classification": "Internal",
        "review": "Annual",
        "summary": (
            "The Northwind testing pyramid, the required test types per change, "
            "CI gates and their thresholds, flaky test policy, the test data "
            "policy, and the definition of done used across squads."
        ),
        "tags": ["testing", "CI", "flaky tests", "coverage", "quality gates", "test data"],
        "sections": [
            {
                "heading": "The Testing Pyramid",
                "paragraphs": [
                    "Northwind targets roughly 70 percent unit tests, 20 percent "
                    "integration tests, and 10 percent end-to-end tests by count. "
                    "The ratio is a cost statement rather than a rule: unit tests "
                    "are cheap and fast, end-to-end tests are slow and brittle, so "
                    "the same assertion should live at the lowest layer that can "
                    "make it credibly.",
                    "End-to-end tests are reserved for the five critical user "
                    "journeys: sign in, create page, publish page, submit form, "
                    "and upgrade plan. Those journeys run on every merge to the "
                    "main branch and on a 15 minute schedule against production."
                ],
                "table": [
                    ["Layer", "Share", "Runtime budget", "Runs on", "Owner"],
                    ["Unit", "70 percent", "Under 5 ms each", "Every commit", "Author"],
                    ["Integration", "20 percent", "Under 2 s each", "Every pull request", "Author"],
                    ["Contract", "5 percent", "Under 30 s per pair", "Every pull request", "API owner"],
                    ["End-to-end", "10 percent", "Under 3 min each", "Merge to main, plus 15 min schedule", "Quality squad"],
                ],
            },
            {
                "heading": "CI Gates",
                "paragraphs": [
                    "Six gates block a merge: build, unit tests, integration "
                    "tests, static analysis with zero new high severity findings, "
                    "dependency scan, and coverage. The coverage gate is a delta "
                    "gate requiring 80 percent of changed lines to be covered, "
                    "not an absolute repository threshold, because absolute "
                    "thresholds encourage tests that assert nothing.",
                    "Gates may not be disabled by a pull request author. A gate "
                    "may be skipped only by a maintainer with a recorded reason, "
                    "and skips are reported weekly. More than three skips in a "
                    "month for one repository triggers a review of the gate "
                    "itself, because a frequently skipped gate is usually a "
                    "broken gate."
                ],
                "bullets": [
                    "Six blocking gates: build, unit, integration, static analysis, dependency scan, coverage.",
                    "Coverage gate is 80 percent of changed lines, not repository-wide.",
                    "Zero new high severity static analysis findings.",
                    "Gate skips require a maintainer and a recorded reason.",
                ],
            },
            {
                "heading": "Flaky Test Policy",
                "paragraphs": [
                    "A test that fails without a code change is flaky and is "
                    "quarantined automatically after two failures in the last 20 "
                    "runs. Quarantined tests still run and still report, but do "
                    "not block. Quarantine is time-boxed to 14 days, after which "
                    "the test must be fixed or deleted; the owner is the team that "
                    "wrote it.",
                    "The company quarantine budget is 3 percent of the suite. "
                    "Above that, the Quality squad halts new end-to-end test "
                    "authoring until the rate returns below budget, because a "
                    "suite nobody trusts is worse than no suite."
                ],
                "notes": [
                    "Root cause note: the three most common flakiness causes at "
                    "Northwind are time dependence, shared test fixtures mutated "
                    "in parallel, and assertions on eventual-consistency reads. "
                    "Fix the cause rather than adding a retry."
                ],
            },
            {
                "heading": "Test Data Policy",
                "paragraphs": [
                    "Production data may not be copied into test environments. "
                    "Test data is generated by the fixture factory, which "
                    "produces realistic values without personal data. Where "
                    "production-like scale is needed, a synthetic generator "
                    "produces the volume and a masked extract may be used only "
                    "with the DPO's written approval and only in the isolated "
                    "analysis account.",
                    "Tests must not depend on data created by other tests, and "
                    "each test creates and cleans up its own fixtures. Tests that "
                    "require a specific pre-existing record are a design smell "
                    "pointing at missing dependency injection."
                ],
            },
            {
                "heading": "Definition of Done",
                "paragraphs": [
                    "A change is done when the behaviour is implemented, tests "
                    "cover the changed behaviour and would fail without the "
                    "change, documentation and the changelog are updated, "
                    "observability is added, the rollback path is stated, and the "
                    "change has been verified in a non-production environment.",
                    "Verification means someone observed the change working, not "
                    "that tests are green. Squads that skip this step report more "
                    "reverts, and the correlation is strong enough that the "
                    "requirement survived three attempts to remove it as "
                    "bureaucracy."
                ],
                "qa": [
                    {
                        "question": "What coverage threshold blocks a merge?",
                        "answer": "80 percent of changed lines, as a delta gate.",
                    },
                    {
                        "question": "When is a test quarantined as flaky?",
                        "answer": "After two failures in the last 20 runs.",
                    },
                    {
                        "question": "How long may a test stay quarantined?",
                        "answer": "14 days, after which it must be fixed or deleted.",
                    },
                ],
            },
        ],
        "qa": [
            {"question": "What is the target unit to integration to e2e test ratio?",
             "answer": "Roughly 70 percent unit, 20 percent integration, 10 percent end-to-end.",
             "evidence": "Northwind targets roughly 70 percent unit tests, 20 percent integration tests, and 10 percent end-to-end tests by count"},
            {"question": "What coverage threshold blocks a merge?",
             "answer": "80 percent of changed lines, applied as a delta gate.",
             "evidence": "requiring 80 percent of changed lines to be covered"},
            {"question": "After how many failures is a test quarantined as flaky?",
             "answer": "Two failures in the last 20 runs.",
             "evidence": "quarantined automatically after two failures in the last 20 runs"},
            {"question": "What is the company-wide quarantine budget for the test suite?",
             "answer": "3 percent of the suite.",
             "evidence": "The company quarantine budget is 3 percent of the suite"},
            {"question": "Which user journeys are covered by end-to-end tests?",
             "answer": "Sign in, create page, publish page, submit form, and upgrade plan.",
             "evidence": "sign in, create page, publish page, submit form, and upgrade plan"},
        ],
    },
    {
        "id": "ENG-STD-017",
        "title": "Observability and On-Call Standard",
        "doc_type": "Standard",
        "category": "Software Engineering",
        "department": "Engineering",
        "author": "Sofia Marchetti, Staff Platform Engineer",
        "owner": "Platform Engineering",
        "version": "3.0",
        "effective": "2026-05-01",
        "classification": "Internal",
        "review": "Annual",
        "summary": (
            "Defines the three telemetry pillars and their retention, the "
            "service level indicator model, alert quality rules and the "
            "actionability requirement, on-call rotation and workload limits, "
            "and the post-incident review format."
        ),
        "tags": ["observability", "on-call", "SLO", "alerting", "tracing", "telemetry"],
        "sections": [
            {
                "heading": "Telemetry Pillars",
                "paragraphs": [
                    "Every production service emits logs, metrics, and traces. "
                    "Logs are structured JSON with a request identifier that "
                    "matches the trace identifier, which is what makes the three "
                    "pillars usable together. Unstructured log lines are rejected "
                    "at the collector.",
                    "Retention differs by pillar and by tier. Metrics are kept 13 "
                    "months at full resolution for Tier 1 services. Traces are "
                    "sampled at 10 percent normally and 100 percent for errors "
                    "and for any request above the SLO latency threshold, because "
                    "sampling away the slow requests defeats the purpose."
                ],
                "table": [
                    ["Pillar", "Sampling", "Tier 1 retention", "Tier 2 retention", "Query budget"],
                    ["Logs", "All, errors always", "30 days hot, 90 days cold", "14 days hot", "5 minutes"],
                    ["Metrics", "Full resolution", "13 months", "13 months", "30 seconds"],
                    ["Traces", "10 percent, 100 percent on error or slow", "15 days", "7 days", "2 minutes"],
                ],
            },
            {
                "heading": "Service Level Indicators",
                "paragraphs": [
                    "Every Tier 1 and Tier 2 service declares at least three "
                    "service level indicators: availability, latency, and "
                    "correctness. Availability is the proportion of successful "
                    "requests. Latency is the 99th percentile of request "
                    "duration. Correctness is the proportion of responses that "
                    "are semantically valid, which catches the case where the "
                    "service returns 200 with wrong data.",
                    "Objectives are set with an error budget. A 99.9 percent "
                    "objective permits 43 minutes and 49 seconds of breach per "
                    "30-day month. When the error budget is exhausted, feature "
                    "work for that service pauses and the squad works on "
                    "reliability until the budget resets, unless the Executive "
                    "Staff explicitly overrides the pause."
                ],
                "bullets": [
                    "Three SLIs minimum for Tier 1 and Tier 2: availability, latency, correctness.",
                    "Correctness catches 200 responses with wrong data.",
                    "Error budget exhausted pauses feature work for that service.",
                    "SLOs are reviewed quarterly with the service owner.",
                ],
            },
            {
                "heading": "Alert Quality",
                "paragraphs": [
                    "Every page must be actionable, meaning a human can do "
                    "something about it within the alert's stated scope, and must "
                    "link to a runbook. Alerts that consistently resolve without "
                    "action are deleted rather than tuned, because tuning an "
                    "unactionable alert usually produces a slightly quieter "
                    "unactionable alert.",
                    "Pages are budgeted at four per engineer per week. A squad "
                    "exceeding that budget for two consecutive weeks must reduce "
                    "page volume before adding new alerts. Alert-to-page ratio "
                    "above 10 to 1 is a sign that alerts are being used as "
                    "dashboards."
                ],
                "notes": [
                    "Wake-up test: if you would not want to be woken at 04:00 for "
                    "this alert, it should be a ticket, not a page."
                ],
            },
            {
                "heading": "On-Call Model",
                "paragraphs": [
                    "On-call rotates weekly with a minimum team size of six, "
                    "which gives at least six weeks between rotations. Primary "
                    "on-call carries the page; secondary is a fallback after 15 "
                    "minutes of no acknowledgement. Business-hours-only on-call is "
                    "permitted for internal services with no customer exposure.",
                    "On-call engineers are entitled to reduced delivery "
                    "expectations during their week and are taken off release "
                    "duty. Compensatory time-off is granted after any week "
                    "containing three or more overnight pages. On-call burnout is "
                    "tracked and a squad with a rising rotation-avoidance pattern "
                    "is treated as having a reliability problem, not a staffing "
                    "problem."
                ],
                "qa": [
                    {
                        "question": "What trace sampling rate applies to errors?",
                        "answer": "100 percent, against 10 percent for normal traffic.",
                    },
                    {
                        "question": "What is the page budget per engineer per week?",
                        "answer": "Four pages.",
                    },
                    {
                        "question": "What happens when a service exhausts its error budget?",
                        "answer": "Feature work for that service pauses until the budget resets, unless overridden by the Executive Staff.",
                    },
                ],
            },
            {
                "heading": "Post-Incident Review",
                "paragraphs": [
                    "Reviews are blameless and are held within five business days "
                    "of recovery for SEV-1 and SEV-2. The document covers the "
                    "timeline from the scribe, the detection path, the impact "
                    "quantified in customer terms, the contributing factors "
                    "rather than a single root cause, and the action items with "
                    "owners and dates.",
                    "Action items are tracked to completion and their closure "
                    "rate is reported quarterly. An incident whose action items "
                    "are not closed within 30 days is reopened at the Engineering "
                    "Leadership review, because unclosed items are how the next "
                    "incident is scheduled."
                ],
            },
        ],
        "qa": [
            {"question": "What trace sampling rate applies to errors?",
             "answer": "100 percent, versus 10 percent for normal traffic.",
             "evidence": "sampled at 10 percent normally and 100 percent for errors"},
            {"question": "What is the weekly page budget per on-call engineer?",
             "answer": "Four pages per engineer per week.",
             "evidence": "Pages are budgeted at four per engineer per week"},
            {"question": "How long may metrics be retained at full resolution for Tier 1 services?",
             "answer": "13 months.",
             "evidence": "Metrics are kept 13 months at full resolution for Tier 1 services"},
            {"question": "What is the minimum team size required to run an on-call rotation?",
             "answer": "Six engineers.",
             "evidence": "On-call rotates weekly with a minimum team size of six"},
            {"question": "Within how many business days must a post-incident review be held for SEV-1 or SEV-2?",
             "answer": "Five business days of recovery.",
             "evidence": "held within five business days of recovery for SEV-1 and SEV-2"},
        ],
    },
    {
        "id": "ENG-STD-023",
        "title": "Deployment and Release Engineering Standard",
        "doc_type": "Standard",
        "category": "Software Engineering",
        "department": "Engineering",
        "author": "Tomas Bergqvist, Director of Engineering",
        "owner": "Platform Engineering",
        "version": "2.9",
        "effective": "2026-06-10",
        "classification": "Internal",
        "review": "Annual",
        "summary": (
            "How Northwind ships software: the trunk-based branching model, "
            "feature flags and their expiry, progressive delivery and canary "
            "thresholds, deployment windows and freeze policy, the automated "
            "rollback triggers, and the release ownership model."
        ),
        "tags": ["deployment", "release", "canary", "feature flags", "trunk based", "rollback"],
        "sections": [
            {
                "heading": "Branching and Trunk",
                "paragraphs": [
                    "Northwind uses trunk-based development. Branches are short, "
                    "typically under two days, and are merged by pull request. "
                    "Long-lived release branches are prohibited except for "
                    "supported major versions of the on-premises appliance, which "
                    "receive security patches for 24 months.",
                    "Main is always deployable, which means a change that breaks "
                    "main is reverted rather than fixed forward unless the fix is "
                    "genuinely faster than the revert. The revert decision is made "
                    "by the release owner within 15 minutes of detection."
                ],
            },
            {
                "heading": "Feature Flags",
                "paragraphs": [
                    "Incomplete work is merged behind a flag rather than left on "
                    "a branch. Every flag carries an owner, a creation date, and "
                    "an expiry date no more than 90 days out. Expired flags are "
                    "reported weekly to their owners and are force-cleaned by the "
                    "platform after 30 days past expiry, which removes the code "
                    "path and the flag.",
                    "Flag debt is measured as the count of live flags per 10,000 "
                    "lines of code, and the company budget is 12. Above budget, "
                    "the owning team cannot introduce new flags until it is back "
                    "under, because unbounded flag state makes testing and "
                    "debugging combinatorially hard."
                ],
                "table": [
                    ["Flag type", "Max lifetime", "Targeting", "Cleanup owner"],
                    ["Release flag, hides incomplete work", "90 days", "All or nothing", "Author"],
                    ["Experiment flag", "90 days", "Percentage split", "Growth squad"],
                    ["Kill switch", "None, permanent", "All or nothing", "Service owner"],
                    ["Entitlement flag", "None, permanent", "Plan based", "Product"],
                ],
            },
            {
                "heading": "Progressive Delivery",
                "paragraphs": [
                    "Production deployments use a canary at 1 percent for 10 "
                    "minutes, then 10 percent for 20 minutes, then 100 percent. "
                    "Progression is automatic when the canary analysis passes, "
                    "which compares error rate, latency p99, and saturation "
                    "against the baseline in the same window with a 5 percent "
                    "tolerance.",
                    "Any canary metric breaching tolerance halts the rollout and "
                    "pages the deployer. A rollback is automatic when the error "
                    "rate exceeds baseline by more than 1 percentage point for "
                    "three consecutive minutes, and completes within 90 seconds "
                    "because traffic shifting is a control-plane operation rather "
                    "than a redeploy."
                ],
                "steps": [
                    "Build and sign the artefact; unsigned artefacts are rejected by admission control.",
                    "Deploy to canary at 1 percent and hold for 10 minutes.",
                    "Run canary analysis against baseline on error rate, p99 latency, and saturation.",
                    "Progress to 10 percent for 20 minutes and re-run the analysis.",
                    "Progress to 100 percent and monitor for 30 minutes before closing the release.",
                    "Record the release outcome and any automatic rollback in the release log.",
                ],
            },
            {
                "heading": "Deployment Windows and Freezes",
                "paragraphs": [
                    "Deploys to production run Monday to Thursday between 09:00 "
                    "and 16:00 Eastern. Friday deploys are prohibited except for "
                    "fixes to a live incident, which require the release owner's "
                    "approval. The rationale is simple: nobody should start a "
                    "risky change with no one available to help.",
                    "Freezes follow the ITSM calendar in IT-STD-003, running 20 "
                    "December to 2 January and through the last five business "
                    "days of each quarter. Emergency deploys during a freeze "
                    "require the Emergency Advisory Board and are reported to the "
                    "Engineering Leadership review."
                ],
                "bullets": [
                    "Production deploys Monday to Thursday, 09:00-16:00 Eastern.",
                    "Friday deploys prohibited except for live incident fixes.",
                    "Freeze windows inherited from IT-STD-003.",
                    "Emergency deploys require the Emergency Advisory Board.",
                ],
            },
            {
                "heading": "Release Ownership",
                "paragraphs": [
                    "Every release has a named release owner who is present and "
                    "available until the release is closed. The owner is "
                    "responsible for the go or no-go decision, for calling a "
                    "rollback, and for the release log entry. Release ownership "
                    "rotates within the squad rather than sitting with the most "
                    "senior person, so the skill is distributed.",
                    "Release frequency is a reported metric, with a company "
                    "median of 14 production deployments per squad per week and a "
                    "change failure rate target below 15 percent. Deploy "
                    "frequency is not a target in itself; it is a leading "
                    "indicator of whether the pipeline is trusted."
                ],
                "qa": [
                    {
                        "question": "What are the canary stages?",
                        "answer": "1 percent for 10 minutes, 10 percent for 20 minutes, then 100 percent.",
                    },
                    {
                        "question": "When does an automatic rollback trigger?",
                        "answer": "When the error rate exceeds baseline by more than 1 percentage point for three consecutive minutes.",
                    },
                    {
                        "question": "What is the maximum lifetime of a release feature flag?",
                        "answer": "90 days, with force-cleanup 30 days past expiry.",
                    },
                ],
            },
        ],
        "qa": [
            {"question": "What are the canary rollout stages and hold times?",
             "answer": "1 percent for 10 minutes, 10 percent for 20 minutes, then 100 percent.",
             "evidence": "a canary at 1 percent for 10 minutes, then 10 percent for 20 minutes, then 100 percent"},
            {"question": "When does an automatic rollback trigger during a canary?",
             "answer": "When the error rate exceeds baseline by more than 1 percentage point for three consecutive minutes.",
             "evidence": "error rate exceeds baseline by more than 1 percentage point for three consecutive minutes"},
            {"question": "What is the maximum lifetime of a release feature flag?",
             "answer": "90 days.",
             "evidence": "Release flag, hides incomplete work | 90 days"},
            {"question": "When are production deployments permitted?",
             "answer": "Monday to Thursday, 09:00 to 16:00 Eastern.",
             "evidence": "Deploys to production run Monday to Thursday between 09:00 and 16:00 Eastern"},
            {"question": "What is the target change failure rate?",
             "answer": "Below 15 percent.",
             "evidence": "a change failure rate target below 15 percent"},
        ],
    },
]
