"""Product management corpus (5 documents)."""

DOCS = [
    {
        "id": "PRD-SPEC-004",
        "title": "Product Requirements: Insight Studio Reporting Builder",
        "doc_type": "Specification",
        "category": "Product Management",
        "department": "Product",
        "author": "Rebecca Lindholm, Group Product Manager",
        "owner": "Product, Reporting Squad",
        "version": "2.1",
        "effective": "2026-06-01",
        "classification": "Confidential",
        "review": "Quarterly",
        "summary": (
            "Requirements for Insight Studio, the self-service reporting "
            "builder for Northwind Pages customers. Covers target users, "
            "functional requirements, non-functional targets, the metric "
            "definition model, permissions, rollout plan, and success metrics."
        ),
        "tags": ["insight studio", "reporting", "requirements", "PRD", "metrics", "self-service"],
        "sections": [
            {
                "heading": "Problem and Target Users",
                "paragraphs": [
                    "Customers cannot answer basic content performance questions "
                    "without filing a support ticket. In the last two quarters, "
                    "38 percent of Tier 2 support tickets were report requests, "
                    "consuming a median of 4.2 engineer-hours each. Insight "
                    "Studio replaces that flow with a self-service builder.",
                    "The primary persona is the marketing operations manager at "
                    "a mid-market customer: fluent in spreadsheets, not fluent "
                    "in SQL, managing between 40 and 400 pages. The secondary "
                    "persona is the agency account manager who reports to "
                    "several clients and needs shareable, branded outputs."
                ],
            },
            {
                "heading": "Functional Requirements",
                "paragraphs": [
                    "Requirements are prioritised using must, should, and could. "
                    "Must-have requirements are launch blockers for the general "
                    "availability release; should-have requirements ship in the "
                    "first quarterly follow-up."
                ],
                "table": [
                    ["ID", "Requirement", "Priority", "Acceptance criteria"],
                    ["FR-01", "Drag-and-drop metric and dimension builder", "Must", "User builds a 3-metric report without SQL in under 3 minutes in usability testing"],
                    ["FR-02", "Saved reports with team sharing", "Must", "Report shared to a role group respects the viewer's data permissions"],
                    ["FR-03", "Scheduled email delivery", "Must", "Digest delivered within 15 minutes of the scheduled time at 99 percent reliability"],
                    ["FR-04", "Comparison periods and trend overlays", "Should", "Any metric renders with a prior-period delta"],
                    ["FR-05", "Export to CSV and XLSX", "Must", "Export of 100,000 rows completes in under 60 seconds"],
                    ["FR-06", "White-label PDF for agencies", "Could", "PDF carries the agency logo and hides Northwind branding"],
                    ["FR-07", "Anomaly annotations on charts", "Could", "Annotation appears within 24 hours of a detected anomaly"],
                ],
            },
            {
                "heading": "Metric Definition Model",
                "paragraphs": [
                    "A single source of truth for metric definitions is the core "
                    "of the feature. Metrics are defined once in the semantic "
                    "layer and cannot be redefined by end users, which prevents "
                    "the situation where two reports disagree. Each metric "
                    "carries a canonical name, a plain-language definition, an "
                    "owner, and a formula.",
                    "The launch metric set contains 42 metrics. The four most "
                    "contested definitions, which must be documented in the "
                    "in-product glossary, are engaged session, which requires "
                    "an interaction of any kind; conversion, which is any "
                    "configured goal event; bounce, which is a session with "
                    "exactly one interaction; and returning visitor, which is "
                    "identified by a first-party cookie with a 395 day window."
                ],
                "bullets": [
                    "Metrics defined once in the semantic layer, not per report.",
                    "42 metrics at launch, each with an owner and a formula.",
                    "Definitions are versioned; changing a definition shows a change note in reports.",
                    "End users may filter and combine metrics but may not redefine them.",
                ],
            },
            {
                "heading": "Non-Functional Targets",
                "paragraphs": [
                    "Interactive queries must return within three seconds at the "
                    "95th percentile for a single-site range of 90 days, and "
                    "within eight seconds at the 95th percentile for a 12-month "
                    "range. Queries above 30 seconds are cancelled and the user "
                    "is offered a scheduled export instead. The feature is "
                    "covered by the existing 99.9 percent availability "
                    "commitment and inherits its service credits.",
                    "Multi-tenant isolation is enforced at the query layer: every "
                    "query carries a tenant predicate injected by the platform, "
                    "and a query without one is rejected by the API gateway. "
                    "Cross-tenant leakage is treated as a SEV-1 security "
                    "incident under SEC-STD-005."
                ],
                "qa": [
                    {
                        "question": "What is the interactive query latency target?",
                        "answer": "Three seconds at the 95th percentile for a 90-day single-site range.",
                    },
                    {
                        "question": "How many metrics ship at launch?",
                        "answer": "42 metrics, each with an owner, a plain-language definition, and a formula.",
                    },
                    {
                        "question": "How is multi-tenant isolation enforced?",
                        "answer": "A tenant predicate is injected by the platform into every query, and queries without one are rejected at the API gateway.",
                    },
                ],
            },
            {
                "heading": "Rollout and Success Metrics",
                "paragraphs": [
                    "Rollout is in four stages: internal dogfood for two weeks, "
                    "then 10 design partners, then 10 percent of customers "
                    "behind a feature flag, then general availability. Each "
                    "stage has an exit gate. The gate from design partners "
                    "requires a System Usability Scale score of at least 70 and "
                    "no open severity 1 or 2 defects.",
                    "Success is measured on four outcomes measured 90 days after "
                    "general availability: report-request tickets down 60 "
                    "percent, weekly active report builders above 35 percent of "
                    "eligible accounts, report sharing occurring in at least 25 "
                    "percent of accounts with a saved report, and no regression "
                    "in page publish reliability."
                ],
            },
        ],
        "qa": [
            {"question": "What percentage of Tier 2 support tickets were report requests?",
             "answer": "38 percent in the last two quarters.",
             "evidence": "38 percent of Tier 2 support tickets were report requests"},
            {"question": "How many metrics are in the Insight Studio launch metric set?",
             "answer": "42 metrics.",
             "evidence": "The launch metric set contains 42 metrics"},
            {"question": "What System Usability Scale score is required to exit the design partner stage?",
             "answer": "At least 70, with no open severity 1 or 2 defects.",
             "evidence": "requires a System Usability Scale score of at least 70 and no open severity 1 or 2 defects"},
            {"question": "How is a returning visitor identified in Insight Studio?",
             "answer": "By a first-party cookie with a 395 day window.",
             "evidence": "returning visitor, which is identified by a first-party cookie with a 395 day window"},
            {"question": "What is the target reduction in report-request tickets?",
             "answer": "60 percent, measured 90 days after general availability.",
             "evidence": "report-request tickets down 60 percent"},
        ],
    },
    {
        "id": "PRD-RFC-009",
        "title": "Architecture RFC: Migrating Page Rendering to Edge Functions",
        "doc_type": "RFC",
        "category": "Product Management",
        "department": "Engineering",
        "author": "Piotr Zawadzki, Principal Architect",
        "owner": "Platform Engineering",
        "version": "1.3",
        "effective": "2026-05-10",
        "classification": "Confidential",
        "review": "Quarterly",
        "summary": (
            "Proposes moving Northwind Pages rendering from the origin "
            "monolith to edge functions. Documents the current performance "
            "baseline, three considered options, the recommendation, the "
            "migration plan, risks, and the rollback strategy."
        ),
        "tags": ["edge functions", "rendering", "architecture", "RFC", "latency", "migration"],
        "sections": [
            {
                "heading": "Current State",
                "paragraphs": [
                    "Pages are rendered by the origin monolith in us-east-1 and "
                    "served from the CDN cache. Cache hits are fast, at a median "
                    "of 42 milliseconds to first byte globally. Cache misses are "
                    "the problem: the median miss takes 890 milliseconds and the "
                    "99th percentile reaches 3.4 seconds, which breaches the "
                    "Core Web Vitals budget for the largest customer sites.",
                    "Miss rate is 11 percent overall but 34 percent on sites "
                    "with personalised blocks, because personalisation "
                    "intentionally bypasses the cache. Personalised sites are "
                    "also the sites with the highest revenue per account, which "
                    "is why this is a priority rather than a background task."
                ],
                "table": [
                    ["Metric", "Current", "Target", "Notes"],
                    ["Cache hit TTFB, median", "42 ms", "42 ms", "Already compliant"],
                    ["Cache miss TTFB, median", "890 ms", "180 ms", "Primary driver of the change"],
                    ["Cache miss TTFB, p99", "3.4 s", "600 ms", "Breaches CWV budget"],
                    ["Miss rate", "11 percent", "9 percent", "Personalised sites at 34 percent"],
                    ["Origin CPU, peak", "78 percent", "55 percent", "Headroom risk at peak"],
                ],
            },
            {
                "heading": "Options Considered",
                "paragraphs": [
                    "Option A keeps the monolith and adds read replicas plus a "
                    "longer cache TTL. It is the cheapest and lowest risk but "
                    "does not help personalised pages, which is where the pain "
                    "is. Option B rewrites rendering as edge functions running "
                    "close to the user, with the monolith retained for authoring "
                    "and publishing. Option C moves rendering into the CDN's "
                    "own compute layer, which is fastest but locks Northwind to "
                    "a single vendor's runtime and its cold-start behaviour."
                ],
                "table": [
                    ["Option", "Miss TTFB estimate", "Effort", "Vendor lock-in", "Recommendation"],
                    ["A: replicas plus TTL", "780 ms", "3 weeks", "None", "Rejected, does not address personalisation"],
                    ["B: edge functions", "160 ms", "14 weeks", "Low, portable runtime", "Recommended"],
                    ["C: CDN-native compute", "95 ms", "20 weeks", "High", "Rejected on lock-in and cold starts"],
                ],
            },
            {
                "heading": "Recommendation and Migration Plan",
                "paragraphs": [
                    "Proceed with Option B. Rendering logic is extracted into a "
                    "portable runtime with a compatibility shim so that the same "
                    "code runs on the origin during migration and at the edge "
                    "afterwards, which allows a per-site traffic shift rather "
                    "than a flag day. Authoring, publishing, and the database "
                    "remain on the monolith and are unchanged.",
                    "Migration runs in five steps over 14 weeks: extract the "
                    "rendering module behind an interface, deploy a shadow "
                    "comparison that renders both paths and diffs the HTML, "
                    "shift 1 percent of traffic, ramp by 10 percent per week "
                    "with a 48 hour soak at each step, then retire the origin "
                    "render path for published pages. The shadow comparison "
                    "stage is mandatory and may not be skipped to save time."
                ],
                "bullets": [
                    "Shadow diffing must show fewer than 0.01 percent mismatched renders before any traffic shift.",
                    "Ramp steps are 1, 10, 20, 50, 100 percent with a 48 hour soak at each.",
                    "Origin render path is retained for 30 days after full ramp.",
                    "Personalised blocks are migrated last because they carry the most state.",
                ],
            },
            {
                "heading": "Risks and Rollback",
                "paragraphs": [
                    "The principal risk is rendering divergence, where the edge "
                    "produces different HTML from the origin because of a "
                    "runtime difference such as locale handling or date "
                    "formatting. The mitigation is the shadow diff plus a "
                    "golden-file suite of 1,200 representative pages run in CI "
                    "on every change to the rendering module.",
                    "Rollback is a configuration change at the router that "
                    "returns traffic to the origin render path, with a target of "
                    "under five minutes and no data migration required. Rollback "
                    "is tested at every ramp step, not only once at the end. The "
                    "second risk is cold starts on the edge runtime, measured "
                    "during the 1 percent stage; if p99 cold-start overhead "
                    "exceeds 120 milliseconds the design is revisited before "
                    "further ramp."
                ],
                "qa": [
                    {
                        "question": "What is the current median cache-miss time to first byte?",
                        "answer": "890 milliseconds.",
                    },
                    {
                        "question": "Which option is recommended?",
                        "answer": "Option B, edge functions with a portable runtime and a compatibility shim.",
                    },
                    {
                        "question": "How fast must rollback complete?",
                        "answer": "Under five minutes, as a router configuration change.",
                    },
                ],
            },
        ],
        "qa": [
            {"question": "What is the current median cache miss TTFB?",
             "answer": "890 milliseconds, with a p99 of 3.4 seconds.",
             "evidence": "the median miss takes 890 milliseconds and the 99th percentile reaches 3.4 seconds"},
            {"question": "What is the miss rate on sites with personalised blocks?",
             "answer": "34 percent, against 11 percent overall.",
             "evidence": "Miss rate is 11 percent overall but 34 percent on sites with personalised blocks"},
            {"question": "What mismatch rate is allowed before shifting traffic in the shadow stage?",
             "answer": "Fewer than 0.01 percent mismatched renders.",
             "evidence": "Shadow diffing must show fewer than 0.01 percent mismatched renders before any traffic shift"},
            {"question": "How many golden-file pages are in the rendering CI suite?",
             "answer": "1,200 representative pages.",
             "evidence": "a golden-file suite of 1,200 representative pages run in CI"},
            {"question": "What cold-start p99 overhead triggers a design revisit?",
             "answer": "More than 120 milliseconds.",
             "evidence": "if p99 cold-start overhead exceeds 120 milliseconds the design is revisited"},
        ],
    },
    {
        "id": "PRD-REL-014",
        "title": "Release Notes: Northwind Pages 2026.2 Spring Release",
        "doc_type": "Release Notes",
        "category": "Product Management",
        "department": "Product",
        "author": "Rebecca Lindholm, Group Product Manager",
        "owner": "Product",
        "version": "2026.2",
        "effective": "2026-04-22",
        "classification": "Public",
        "review": "Per release",
        "summary": (
            "Customer-facing release notes for the 2026.2 Spring release of "
            "Northwind Pages, covering new features, improvements, fixed "
            "defects, deprecations, breaking changes, and the upgrade "
            "considerations for API consumers."
        ),
        "tags": ["release notes", "2026.2", "changelog", "deprecation", "breaking change", "API"],
        "sections": [
            {
                "heading": "Release Summary",
                "paragraphs": [
                    "The 2026.2 Spring release shipped on 22 April 2026 to all "
                    "customers on the Standard, Professional, and Enterprise "
                    "plans. The release contains 14 new features, 38 "
                    "improvements, and 127 defect fixes. Two deprecations take "
                    "effect immediately and one breaking change takes effect on "
                    "1 August 2026, which gives API consumers roughly 14 weeks "
                    "to migrate.",
                    "Rollout completed in 41 minutes with no rollback. The "
                    "release is available in all regions. Enterprise customers "
                    "on a pinned version receive it in their next maintenance "
                    "window."
                ],
            },
            {
                "heading": "New Features",
                "paragraphs": [
                    "Insight Studio entered limited availability for "
                    "Professional and Enterprise accounts, delivering the "
                    "self-service report builder described in PRD-SPEC-004. "
                    "Form Builder gained conditional logic, allowing fields to "
                    "show or hide based on earlier answers, with a maximum "
                    "depth of eight nested conditions. The media library gained "
                    "automatic alt-text suggestions, which customers must "
                    "review before publishing because the suggestions are not "
                    "guaranteed accurate."
                ],
                "bullets": [
                    "Insight Studio report builder in limited availability for Professional and Enterprise.",
                    "Conditional logic in Form Builder, up to eight nested conditions.",
                    "Automatic alt-text suggestions in the media library.",
                    "Bulk content scheduling with a queue view and conflict warnings.",
                    "Two additional locales, Polish and Swedish, bringing the total to 31.",
                    "Webhook delivery now includes a signed header for verification.",
                ],
            },
            {
                "heading": "Improvements",
                "paragraphs": [
                    "Publish time for sites with more than 5,000 pages improved "
                    "by 43 percent through incremental dependency resolution, "
                    "reducing a typical large publish from 11 minutes to 6.3 "
                    "minutes. The editor now autosaves every 15 seconds rather "
                    "than every 60, and the recovery dialog lists the three most "
                    "recent autosaves rather than only the latest. Image "
                    "processing moved to a queue, which removes the previous "
                    "30-second timeout on uploads above 20 megabytes.",
                    "Search relevance was retuned using customer feedback, "
                    "improving the click-through rate on the first result from "
                    "54 percent to 68 percent in the internal evaluation set."
                ],
            },
            {
                "heading": "Deprecations and Breaking Changes",
                "paragraphs": [
                    "The legacy v1 REST endpoints for content retrieval are "
                    "deprecated with effect from this release and will be "
                    "removed on 1 August 2026. The v2 equivalents are "
                    "documented and return the same data with a different "
                    "envelope. Any account still calling v1 receives an "
                    "in-product banner and a weekly email listing the number of "
                    "calls made.",
                    "One breaking change is scheduled: the published_at field "
                    "changes from a naive local timestamp to a proper ISO 8601 "
                    "value with a UTC offset on 1 August 2026. Consumers that "
                    "parse the field with a strict parser should test against "
                    "the sandbox environment, which has already returned the new "
                    "format since 1 April."
                ],
                "table": [
                    ["Change", "Type", "Effective", "Action required"],
                    ["v1 content REST endpoints", "Deprecation", "Immediate, removal 2026-08-01", "Migrate to v2 endpoints"],
                    ["published_at becomes ISO 8601 with offset", "Breaking", "2026-08-01", "Test parsers against sandbox"],
                    ["Webhook payload adds signature header", "Additive", "Immediate", "Verify signatures recommended"],
                    ["Default image quality raised to 82", "Behaviour change", "Immediate", "None, cache purge optional"],
                ],
            },
            {
                "heading": "Notable Fixes",
                "paragraphs": [
                    "Fixed an issue where scheduled publishes silently failed "
                    "for sites in the Australia region during daylight saving "
                    "transitions, which affected 41 accounts. Fixed a defect "
                    "where form submissions with more than 50 fields truncated "
                    "the payload. Fixed a caching bug where a redirect rule "
                    "change did not invalidate the CDN entry for up to 24 hours. "
                    "Fixed right-to-left layout regressions in the editor "
                    "toolbar for Arabic and Hebrew locales.",
                    "The full defect list is available in the public changelog. "
                    "Customers who want a defect investigated further should "
                    "reference the defect identifier when contacting support."
                ],
                "qa": [
                    {
                        "question": "When are the v1 REST endpoints removed?",
                        "answer": "On 1 August 2026.",
                    },
                    {
                        "question": "What breaking change affects published_at?",
                        "answer": "It changes from a naive local timestamp to ISO 8601 with a UTC offset on 1 August 2026.",
                    },
                    {
                        "question": "How much faster is publish for large sites?",
                        "answer": "43 percent faster, from 11 minutes to 6.3 minutes.",
                    },
                ],
            },
        ],
        "qa": [
            {"question": "When did the 2026.2 Spring release ship?",
             "answer": "22 April 2026.",
             "evidence": "The 2026.2 Spring release shipped on 22 April 2026"},
            {"question": "When are the legacy v1 REST endpoints removed?",
             "answer": "1 August 2026.",
             "evidence": "removed on 1 August 2026"},
            {"question": "How much did publish time improve for sites over 5,000 pages?",
             "answer": "43 percent, from 11 minutes to 6.3 minutes.",
             "evidence": "improved by 43 percent ... reducing a typical large publish from 11 minutes to 6.3 minutes"},
            {"question": "How many locales does Northwind Pages support after 2026.2?",
             "answer": "31 locales, after adding Polish and Swedish.",
             "evidence": "Two additional locales, Polish and Swedish, bringing the total to 31"},
            {"question": "What is the maximum nesting depth for conditional logic in Form Builder?",
             "answer": "Eight nested conditions.",
             "evidence": "with a maximum depth of eight nested conditions"},
        ],
    },
    {
        "id": "PRD-RES-019",
        "title": "User Research Report: Content Authoring Friction Study",
        "doc_type": "Research Report",
        "category": "Product Management",
        "department": "User Research",
        "author": "Naomi Feldman, Senior UX Researcher",
        "owner": "User Research",
        "version": "1.0",
        "effective": "2026-03-18",
        "classification": "Confidential",
        "review": "As needed",
        "summary": (
            "Findings from a mixed-method study of content authoring at 24 "
            "customer accounts. Reports time-to-publish benchmarks, the five "
            "highest-friction moments, quantified survey results, and "
            "prioritised recommendations with expected impact."
        ),
        "tags": ["user research", "authoring", "friction", "usability", "time to publish", "findings"],
        "sections": [
            {
                "heading": "Method",
                "paragraphs": [
                    "The study ran for six weeks across 24 accounts selected to "
                    "span company size, industry, and tenure. It combined 31 "
                    "moderated sessions of 45 minutes, contextual observation of "
                    "11 authors working normally, and an unmoderated survey with "
                    "212 respondents. Sessions were recorded with consent and "
                    "coded independently by two researchers, with disagreements "
                    "resolved by discussion rather than majority vote.",
                    "Participants are described by persona rather than by "
                    "account. The three personas studied were the solo marketer "
                    "who owns everything, the distributed team with separate "
                    "authors and approvers, and the agency with many client "
                    "workspaces."
                ],
            },
            {
                "heading": "Time to Publish Benchmark",
                "paragraphs": [
                    "Median time from a blank page to a published page was 27 "
                    "minutes for the solo marketer and 74 minutes for the "
                    "distributed team, where the extra time is almost entirely "
                    "waiting for approval rather than doing work. The internal "
                    "target is 15 minutes for the solo persona, so the gap is "
                    "12 minutes, and the largest single contributors were "
                    "metadata entry and image handling."
                ],
                "table": [
                    ["Task", "Solo marketer median", "Distributed team median", "Target", "Gap"],
                    ["Create page and add body copy", "9 min", "11 min", "8 min", "3 min"],
                    ["Add and position images", "7 min", "8 min", "4 min", "4 min"],
                    ["Complete metadata and SEO fields", "6 min", "7 min", "2 min", "5 min"],
                    ["Preview on mobile", "3 min", "3 min", "1 min", "2 min"],
                    ["Submit and wait for approval", "0 min", "45 min", "0 min", "45 min"],
                ],
            },
            {
                "heading": "Top Five Friction Moments",
                "paragraphs": [
                    "Friction was scored on frequency of occurrence multiplied "
                    "by observed emotional intensity on a three-point scale. The "
                    "five highest-scoring moments are listed below. Metadata "
                    "entry scored highest because it is mandatory, repetitive, "
                    "and poorly explained: authors do not know which fields "
                    "affect search ranking and therefore fill all of them "
                    "badly, or none of them."
                ],
                "table": [
                    ["Rank", "Friction moment", "Frequency", "Intensity", "Score"],
                    ["1", "Metadata and SEO field completion", "28 of 31 sessions", "High", "84"],
                    ["2", "Image cropping losing the intended framing", "22 of 31 sessions", "High", "66"],
                    ["3", "Waiting for approval with no visibility of who holds it", "19 of 31 sessions", "High", "57"],
                    ["4", "Undo not working across autosave boundaries", "14 of 31 sessions", "High", "42"],
                    ["5", "Finding the right reusable component", "17 of 31 sessions", "Medium", "34"],
                ],
            },
            {
                "heading": "Survey Results",
                "paragraphs": [
                    "Of 212 survey respondents, 61 percent said approval waiting "
                    "is their biggest single source of delay, and 47 percent had "
                    "abandoned an edit because the process took too long. "
                    "Task completion confidence was high for body editing, at "
                    "4.4 out of 5, and low for metadata, at 2.6 out of 5, and "
                    "for component reuse, at 2.9 out of 5.",
                    "Qualitative comments clustered on trust and visibility. "
                    "Authors repeatedly asked who has their page, and approvers "
                    "repeatedly said they did not know a review was waiting. "
                    "This is a notification and state-visibility problem rather "
                    "than an editor problem, which is a useful finding because "
                    "the cheap fix is in a different part of the product than "
                    "the team expected."
                ],
                "bullets": [
                    "61 percent named approval waiting as their biggest delay.",
                    "47 percent had abandoned an edit because the process took too long.",
                    "Metadata confidence scored 2.6 out of 5, the lowest measured.",
                    "Solo marketers published 3.1 pages per week; distributed teams published 8.4.",
                ],
            },
            {
                "heading": "Recommendations",
                "paragraphs": [
                    "Four recommendations are prioritised by expected impact "
                    "against effort. The approval visibility work is the highest "
                    "return because it addresses the 45-minute approval wait and "
                    "requires notification and state work rather than editor "
                    "rework. Metadata guidance is second because it is small and "
                    "touches every author.",
                    "Two further ideas were considered and deferred: an AI "
                    "drafting assistant, deferred because the underlying content "
                    "quality question is unresolved, and a full editor rewrite, "
                    "deferred because no evidence supports it."
                ],
                "table": [
                    ["Recommendation", "Addresses", "Expected impact", "Effort", "Priority"],
                    ["Approval queue with owner and age visible to authors", "Friction 3, 61 percent survey", "Cut approval wait by half", "M", "P1"],
                    ["Inline metadata guidance with required-field hints", "Friction 1", "Metadata confidence to 4.0", "S", "P1"],
                    ["Smart crop preserving focal point", "Friction 2", "Cut image handling to 4 min", "L", "P2"],
                    ["Component gallery with search and usage counts", "Friction 5", "Component reuse up 20 percent", "M", "P2"],
                ],
                "qa": [
                    {
                        "question": "What was the median time to publish for a distributed team?",
                        "answer": "74 minutes, of which 45 minutes was waiting for approval.",
                    },
                    {
                    "question": "Which friction moment scored highest?",
                        "answer": "Metadata and SEO field completion, with a score of 84.",
                    },
                    {
                        "question": "What percentage abandoned an edit because it took too long?",
                        "answer": "47 percent.",
                    },
                ],
            },
        ],
        "qa": [
            {"question": "What was the median time to publish for the solo marketer persona?",
             "answer": "27 minutes.",
             "evidence": "Median time from a blank page to a published page was 27 minutes for the solo marketer"},
            {"question": "How many survey respondents named approval waiting as their biggest delay?",
             "answer": "61 percent.",
             "evidence": "61 percent said approval waiting is their biggest single source of delay"},
            {"question": "Which friction moment scored highest and what was its score?",
             "answer": "Metadata and SEO field completion, scoring 84.",
             "evidence": "Metadata and SEO field completion | 28 of 31 sessions | High | 84"},
            {"question": "How many accounts and sessions were in the study?",
             "answer": "24 accounts and 31 moderated sessions, plus a 212 respondent survey.",
             "evidence": "31 moderated sessions of 45 minutes ... an unmoderated survey with 212 respondents"},
            {"question": "What was the lowest confidence score measured in the survey?",
             "answer": "2.6 out of 5, for metadata.",
             "evidence": "low for metadata, at 2.6 out of 5"},
        ],
    },
    {
        "id": "PRD-GTM-023",
        "title": "Go-To-Market Plan: Insight Studio Launch",
        "doc_type": "Plan",
        "category": "Product Management",
        "department": "Product Marketing",
        "author": "Sandra Kowalczyk, Director of Product Marketing",
        "owner": "Product Marketing",
        "version": "1.2",
        "effective": "2026-07-01",
        "classification": "Confidential",
        "review": "Quarterly",
        "summary": (
            "Go-to-market plan for Insight Studio covering positioning, "
            "segmentation, pricing and packaging, the launch timeline and "
            "channels, enablement requirements, competitive response, and the "
            "metrics that define a successful launch."
        ),
        "tags": ["go to market", "GTM", "positioning", "pricing", "launch", "enablement"],
        "sections": [
            {
                "heading": "Positioning",
                "paragraphs": [
                    "Insight Studio is positioned as the reporting layer that "
                    "makes a marketing team self-sufficient. The primary "
                    "statement is: for marketing operations managers who wait "
                    "days for a report, Insight Studio is the self-service "
                    "reporting builder that delivers answers in minutes, because "
                    "metrics are defined once by the vendor and cannot be "
                    "misinterpreted by end users.",
                    "The differentiator we lead with is the governed metric "
                    "layer. Competitors offer flexibility; we offer trust. The "
                    "proof point is the 42-metric governed definition set and "
                    "the elimination of the support-ticket workaround, which "
                    "customers can verify against their own ticket history."
                ],
            },
            {
                "heading": "Segmentation and Personas",
                "paragraphs": [
                    "Three segments are targeted in order of expected revenue "
                    "contribution. The beachhead is mid-market marketing teams "
                    "of 5 to 50 employees with between 40 and 400 pages, which "
                    "represents 41 percent of the existing base and has the "
                    "highest reported pain. The second is agencies managing "
                    "multiple client workspaces, where white-label PDF is the "
                    "hook. The third is enterprise marketing operations, which "
                    "has the largest contract value but the longest cycle and is "
                    "therefore sequenced last."
                ],
                "table": [
                    ["Segment", "Share of base", "Primary need", "Hook feature", "Sequence"],
                    ["Mid-market marketing", "41 percent", "Self-service answers", "Drag-and-drop builder", "Wave 1"],
                    ["Agencies", "18 percent", "Client-ready reporting", "White-label PDF", "Wave 2"],
                    ["Enterprise marketing ops", "22 percent", "Governance and audit", "Metric versioning", "Wave 3"],
                    ["SMB", "19 percent", "Simple dashboard", "Templates", "Not targeted at launch"],
                ],
            },
            {
                "heading": "Pricing and Packaging",
                "paragraphs": [
                    "Insight Studio is included in Professional and Enterprise "
                    "at no additional price, which is a deliberate decision to "
                    "remove friction from adoption and to close the gap that "
                    "competitors exploit by charging for reporting as an add-on. "
                    "For Standard customers, Insight Studio is available as an "
                    "add-on at 150 USD per month per workspace, which is priced "
                    "below the cost of the equivalent agency reporting service.",
                    "Rate limits are set at 500 saved reports and 50 scheduled "
                    "deliveries per workspace, which covers 97 percent of "
                    "projected usage. White-label PDF is Enterprise-only at "
                    "launch, which is the primary upgrade lever for the agency "
                    "segment."
                ],
                "bullets": [
                    "Included at no cost in Professional and Enterprise.",
                    "Standard add-on priced at 150 USD per month per workspace.",
                    "500 saved reports and 50 scheduled deliveries per workspace.",
                    "White-label PDF is Enterprise-only at launch.",
                ],
            },
            {
                "heading": "Launch Timeline and Channels",
                "paragraphs": [
                    "Launch runs over eight weeks. Weeks 1 to 4 are internal: "
                    "sales and support enablement, content production, and "
                    "demo environment build. Week 5 is the design-partner "
                    "reference release. Week 6 is the public announcement with "
                    "the blog post, documentation, and a product tour. Weeks 7 "
                    "and 8 are demand capture through webinars and lifecycle "
                    "email.",
                    "Channels in priority order are existing-customer lifecycle "
                    "email, which has the highest conversion, in-product "
                    "promotion, the customer community, the public blog, and "
                    "partner agencies. Paid acquisition is deliberately excluded "
                    "at launch because the feature is included in existing plans "
                    "and does not justify new-logo spend in the first quarter."
                ],
                "table": [
                    ["Week", "Activity", "Owner", "Success gate"],
                    ["1-2", "Sales and support enablement", "Product Marketing", "90 percent certification"],
                    ["3-4", "Content and demo build", "Product Marketing", "All assets approved"],
                    ["5", "Design partner references", "Product", "3 quotable references"],
                    ["6", "Public announcement", "Communications", "10,000 launch-week activations"],
                    ["7-8", "Webinars and lifecycle", "Demand Generation", "25 percent activation of eligible accounts"],
                ],
            },
            {
                "heading": "Enablement and Success Metrics",
                "paragraphs": [
                    "Sales enablement requires a two-page battlecard, a five "
                    "minute demo script, and objection handling for the three "
                    "most likely challenges, which are metric flexibility, "
                    "comparison to dedicated business intelligence tools, and "
                    "concern about vendor-defined metrics. Support enablement "
                    "requires a troubleshooting guide and an updated ticket "
                    "routing rule so that report requests reach the Insight "
                    "Studio queue.",
                    "Launch success is judged at 90 days on five metrics: "
                    "activation of 35 percent of eligible accounts, 25 percent "
                    "of activated accounts sharing a report, a 60 percent "
                    "reduction in report-request tickets, Insight Studio "
                    "mentioned in at least 15 percent of won-deal notes, and "
                    "fewer than 8 support tickets per 1,000 active builders."
                ],
                "qa": [
                    {
                        "question": "Is Insight Studio charged extra on Professional and Enterprise?",
                        "answer": "No, it is included at no additional price.",
                    },
                    {
                        "question": "What does the Standard add-on cost?",
                        "answer": "150 USD per month per workspace.",
                    },
                    {
                        "question": "Which capability is Enterprise-only at launch?",
                        "answer": "White-label PDF export.",
                    },
                ],
            },
        ],
        "qa": [
            {"question": "What does the Insight Studio Standard add-on cost?",
             "answer": "150 USD per month per workspace.",
             "evidence": "available as an add-on at 150 USD per month per workspace"},
            {"question": "Which segment is the launch beachhead?",
             "answer": "Mid-market marketing teams of 5 to 50 employees with 40 to 400 pages, 41 percent of the base.",
             "evidence": "The beachhead is mid-market marketing teams of 5 to 50 employees with between 40 and 400 pages, which represents 41 percent of the existing base"},
            {"question": "What is the activation target at 90 days?",
             "answer": "35 percent of eligible accounts.",
             "evidence": "activation of 35 percent of eligible accounts"},
            {"question": "Which feature is Enterprise-only at launch?",
             "answer": "White-label PDF export.",
             "evidence": "White-label PDF is Enterprise-only at launch"},
            {"question": "What is the saved report limit per workspace?",
             "answer": "500 saved reports and 50 scheduled deliveries.",
             "evidence": "500 saved reports and 50 scheduled deliveries per workspace"},
        ],
    },
]
