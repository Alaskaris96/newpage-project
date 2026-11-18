"""Marketing, growth, and sales corpus (5 documents)."""

DOCS = [
    {
        "id": "MKT-PLN-002",
        "title": "Content Strategy and Editorial Plan",
        "doc_type": "Plan",
        "category": "Marketing",
        "department": "Marketing",
        "author": "Sandra Kowalczyk, Director of Product Marketing",
        "owner": "Marketing",
        "version": "2026.1",
        "effective": "2026-01-06",
        "classification": "Internal",
        "review": "Quarterly",
        "summary": (
            "The Northwind content strategy for the year: audience segments, "
            "content pillars and their allocation, publishing cadence, the "
            "editorial workflow and roles, performance targets, and the "
            "distribution channels."
        ),
        "tags": ["content", "editorial", "SEO", "blog", "distribution", "strategy"],
        "sections": [
            {
                "heading": "Audience and Pillars",
                "paragraphs": [
                    "Content serves three audiences in priority order: the "
                    "marketing operations manager who evaluates and adopts, the "
                    "agency owner who resells Northwind to many clients, and the "
                    "developer who integrates. Evaluation-stage content is "
                    "prioritised because it is the content that can be attributed "
                    "to pipeline.",
                    "Four pillars structure the plan. Governance and workflow "
                    "receives 35 percent of output and is the highest-performing "
                    "pillar on organic search. Performance and Core Web Vitals "
                    "receives 25 percent and earns the most backlinks. "
                    "Comparisons and alternatives receives 20 percent and has the "
                    "highest conversion rate. Migration guides receive 20 percent "
                    "and have the longest production time."
                ],
                "table": [
                    ["Pillar", "Share", "Primary audience", "Primary channel", "Conversion rate"],
                    ["Governance and workflow", "35 percent", "Marketing ops", "Organic search", "3.1 percent"],
                    ["Performance and CWV", "25 percent", "Marketing ops, developer", "Organic, social", "1.8 percent"],
                    ["Comparisons and alternatives", "20 percent", "Evaluator", "Organic, paid", "6.4 percent"],
                    ["Migration guides", "20 percent", "Agency, evaluator", "Email, sales", "4.9 percent"],
                ],
            },
            {
                "heading": "Cadence and Production",
                "paragraphs": [
                    "The plan commits to 8 long-form articles per month at 1,800 "
                    "words or more, 4 technical deep dives per month, 2 customer "
                    "stories per month, and 1 newsletter per week. Long-form "
                    "production takes 14 business days from brief to publish at "
                    "the current team size, which is the constraint that caps "
                    "volume.",
                    "Every article begins with a brief containing the target "
                    "query, the search intent, the existing top-ten results and "
                    "why the new piece will beat them, the internal links "
                    "required, and the call to action. Articles published without "
                    "an approved brief are not counted toward the monthly target, "
                    "which is the enforcement mechanism that keeps briefs honest."
                ],
                "bullets": [
                    "8 long-form articles and 4 technical deep dives per month.",
                    "2 customer stories per month, requiring a named customer sponsor.",
                    "1 newsletter per week, Thursday, currently 24,300 subscribers.",
                    "Brief required before writing; no brief means no credit toward target.",
                ],
            },
            {
                "heading": "Editorial Workflow and Roles",
                "paragraphs": [
                    "Roles are separated so that the writer is never the final "
                    "approver. The content lead owns the brief and the calendar. "
                    "The writer produces the draft. The subject-matter expert "
                    "verifies technical accuracy and must sign off before "
                    "publication, which is the step that prevents published "
                    "errors. The editor owns voice and clarity. The SEO reviewer "
                    "owns internal linking and metadata.",
                    "Technical content requires a second reviewer from "
                    "Engineering because two published articles in the last year "
                    "contained instructions that no longer worked after a "
                    "release. Both were caught by customers before they were "
                    "caught internally, which is the reason the rule exists."
                ],
                "steps": [
                    "Content lead writes and approves the brief with the target query and intent.",
                    "Writer produces a draft against the brief.",
                    "Subject-matter expert verifies technical accuracy and signs off.",
                    "Editor revises for voice, clarity, and reading level.",
                    "SEO reviewer sets metadata and internal links.",
                    "Publish, then submit to the index and schedule the social and newsletter slots.",
                    "Review performance at 60 days and refresh if below target.",
                ],
            },
            {
                "heading": "Performance Targets",
                "paragraphs": [
                    "Targets are set on organic sessions, assisted pipeline, and "
                    "content efficiency. Organic sessions target 340,000 per "
                    "month by year end, up from 218,000 at the start of the year. "
                    "Assisted pipeline target is 4.2 million USD attributed to "
                    "content. Efficiency is measured as cost per organic "
                    "session, targeting below 0.85 USD.",
                    "Content is reviewed at 60 days and again at 180 days. "
                    "Articles below the 25th percentile of their pillar at 180 "
                    "days are refreshed, consolidated, or retired. Retiring "
                    "content is as important as publishing it and is the step "
                    "teams skip."
                ],
                "table": [
                    ["Metric", "Start of year", "Year-end target", "Current", "Status"],
                    ["Organic sessions per month", "218,000", "340,000", "261,000", "On track"],
                    ["Assisted pipeline", "2.6 m USD", "4.2 m USD", "3.1 m USD", "On track"],
                    ["Cost per organic session", "1.10 USD", "0.85 USD", "0.98 USD", "At risk"],
                    ["Articles ranking top 3", "84", "160", "103", "On track"],
                    ["Newsletter subscribers", "19,800", "30,000", "24,300", "On track"],
                ],
            },
            {
                "heading": "Distribution",
                "paragraphs": [
                    "Publishing without distribution is drafting. Every article "
                    "is distributed through the newsletter, the customer "
                    "community, two social channels, and the partner agency "
                    "network. Comparison and migration content is additionally "
                    "routed to the sales enablement library and referenced in "
                    "outbound sequences.",
                    "Paid amplification is reserved for content with proven "
                    "organic performance, defined as above-median engagement in "
                    "the first 14 days, because amplifying unproven content is "
                    "the most common way a content budget is wasted."
                ],
                "qa": [
                    {
                        "question": "Which pillar has the highest conversion rate?",
                        "answer": "Comparisons and alternatives, at 6.4 percent.",
                    },
                    {
                        "question": "Who must sign off on technical accuracy before publication?",
                        "answer": "The subject-matter expert, with a second Engineering reviewer for technical content.",
                    },
                    {
                        "question": "When is an article reviewed after publication?",
                        "answer": "At 60 days and again at 180 days.",
                    },
                ],
            },
        ],
        "qa": [
            {"question": "Which content pillar has the highest conversion rate?",
             "answer": "Comparisons and alternatives, at 6.4 percent.",
             "evidence": "Comparisons and alternatives | 20 percent | Evaluator | Organic, paid | 6.4 percent"},
            {"question": "What is the year-end organic sessions target?",
             "answer": "340,000 per month, up from 218,000.",
             "evidence": "Organic sessions target 340,000 per month by year end, up from 218,000"},
            {"question": "How many long-form articles are committed per month?",
             "answer": "8 long-form articles at 1,800 words or more.",
             "evidence": "The plan commits to 8 long-form articles per month at 1,800 words or more"},
            {"question": "What is the current newsletter subscriber count?",
             "answer": "24,300 subscribers.",
             "evidence": "1 newsletter per week, Thursday, currently 24,300 subscribers"},
            {"question": "Which metric is currently flagged as at risk?",
             "answer": "Cost per organic session, at 0.98 USD against a 0.85 USD target.",
             "evidence": "Cost per organic session | 1.10 USD | 0.85 USD | 0.98 USD | At risk"},
        ],
    },
    {
        "id": "MKT-PLN-008",
        "title": "Demand Generation and Paid Acquisition Playbook",
        "doc_type": "Playbook",
        "category": "Marketing",
        "department": "Demand Generation",
        "author": "Felix Andersson, Head of Demand Generation",
        "owner": "Demand Generation",
        "version": "3.3",
        "effective": "2026-02-01",
        "classification": "Confidential",
        "review": "Quarterly",
        "summary": (
            "The Northwind paid acquisition model: channel mix and budget, "
            "target cost per acquisition by channel and segment, the funnel "
            "conversion benchmarks, the campaign testing protocol, and the "
            "attribution model used for reporting."
        ),
        "tags": ["demand generation", "paid", "CPA", "funnel", "attribution", "testing"],
        "sections": [
            {
                "heading": "Budget and Channel Mix",
                "paragraphs": [
                    "The annual demand generation budget is 3.4 million USD, "
                    "allocated across five channels. Search carries the largest "
                    "share because it captures existing intent. Social is used "
                    "for upper-funnel demand creation and is judged on assisted "
                    "conversions rather than last click, which changes how it "
                    "performs in reporting.",
                    "Budget is reviewed monthly and reallocated quarterly. A "
                    "channel that misses its target cost per acquisition for two "
                    "consecutive months has 20 percent of its budget moved to the "
                    "best-performing channel until it recovers."
                ],
                "table": [
                    ["Channel", "Budget share", "Target CPA", "Current CPA", "Monthly leads"],
                    ["Paid search", "42 percent", "420 USD", "448 USD", "310"],
                    ["Paid social", "22 percent", "610 USD", "575 USD", "120"],
                    ["Programmatic display", "8 percent", "900 USD", "1,140 USD", "22"],
                    ["Sponsored content and partnerships", "18 percent", "380 USD", "352 USD", "95"],
                    ["Retargeting", "10 percent", "180 USD", "166 USD", "140"],
                ],
            },
            {
                "heading": "Funnel Benchmarks",
                "paragraphs": [
                    "The funnel is measured in five stages with published "
                    "benchmarks so that a decline can be localised rather than "
                    "debated. Visitor to trial signup targets 2.4 percent; trial "
                    "to activated targets 45 percent; activated to paid targets "
                    "28 percent. The current weak stage is trial to activated at "
                    "38 percent, which is why the activation project is the "
                    "priority rather than more traffic.",
                    "Buying more traffic into a leaky funnel is the most "
                    "expensive mistake available, and the monthly review exists "
                    "mainly to prevent it."
                ],
                "table": [
                    ["Stage", "Benchmark", "Current", "Gap", "Owner"],
                    ["Visitor to trial signup", "2.4 percent", "2.3 percent", "-0.1", "Demand Gen"],
                    ["Trial to activated", "45 percent", "38 percent", "-7.0", "Product"],
                    ["Activated to paid", "28 percent", "29 percent", "+1.0", "Sales"],
                    ["Paid to retained at 12 months", "88 percent", "90 percent", "+2.0", "Customer Success"],
                ],
            },
            {
                "heading": "Testing Protocol",
                "paragraphs": [
                    "Every campaign change is a test with a hypothesis, a primary "
                    "metric, a minimum sample, and a stop rule. Tests run to the "
                    "pre-computed sample size and are not stopped early for a "
                    "promising result, because early stopping is the most common "
                    "way to ship a false positive.",
                    "A minimum of 100 conversions per arm is required before a "
                    "conclusion, and the significance threshold is 95 percent. "
                    "Landing page tests are owned by Demand Generation; offer "
                    "tests require Product Marketing approval because an offer "
                    "change is a pricing decision in disguise."
                ],
                "bullets": [
                    "Hypothesis, primary metric, sample size, and stop rule defined before launch.",
                    "Minimum 100 conversions per arm and 95 percent significance.",
                    "No early stopping for a promising result.",
                    "Offer changes require Product Marketing approval.",
                ],
            },
            {
                "heading": "Attribution",
                "paragraphs": [
                    "Reporting uses a position-based model, with 40 percent "
                    "credited to first touch, 40 percent to last touch, and 20 "
                    "percent distributed across the middle. Last-touch is shown "
                    "alongside it for comparison, and the two disagree in ways "
                    "that matter: last-touch over-credits retargeting and "
                    "under-credits content by roughly a factor of three.",
                    "Attribution is a decision aid, not a truth. Where a channel "
                    "decision depends on attribution alone, a holdout test is run "
                    "instead, because the model cannot measure demand that would "
                    "not have existed without the campaign."
                ],
                "notes": [
                    "Cookie note: consent mode reduces modelled conversions by "
                    "roughly 12 percent. Comparisons between periods must use the "
                    "same modelling version or the trend is an artefact."
                ],
            },
            {
                "heading": "Campaign Calendar",
                "paragraphs": [
                    "Four major campaigns run each year, aligned to the product "
                    "release cycle and to the two buying seasons. The spring "
                    "campaign launches with the 2026.2 release, the summer "
                    "campaign targets agencies, the autumn campaign is the "
                    "largest and aligns to the Insight Studio general "
                    "availability, and the winter campaign is retention-focused "
                    "rather than acquisition-focused.",
                    "Each campaign requires a brief with the audience, the "
                    "message, the offer, the landing page, the budget, the "
                    "success metric, and the holdout plan. Campaigns launch with "
                    "a 10 percent holdout where volume allows, which is the only "
                    "reliable way to know whether the spend was incremental."
                ],
                "qa": [
                    {
                        "question": "What is the annual demand generation budget?",
                        "answer": "3.4 million USD across five channels.",
                    },
                    {
                        "question": "Which funnel stage is currently under benchmark?",
                        "answer": "Trial to activated, at 38 percent against a 45 percent benchmark.",
                    },
                    {
                        "question": "What attribution model is used for reporting?",
                        "answer": "Position-based, 40 percent first touch, 40 percent last touch, 20 percent distributed.",
                    },
                ],
            },
        ],
        "qa": [
            {"question": "What is the annual demand generation budget?",
             "answer": "3.4 million USD.",
             "evidence": "The annual demand generation budget is 3.4 million USD"},
            {"question": "Which funnel stage is currently below benchmark?",
             "answer": "Trial to activated, at 38 percent against a 45 percent benchmark.",
             "evidence": "Trial to activated | 45 percent | 38 percent | -7.0 | Product"},
            {"question": "What is the target CPA for paid search?",
             "answer": "420 USD.",
             "evidence": "Paid search | 42 percent | 420 USD | 448 USD"},
            {"question": "What attribution model does Northwind use for reporting?",
             "answer": "Position-based: 40 percent first touch, 40 percent last touch, 20 percent distributed across the middle.",
             "evidence": "Reporting uses a position-based model, with 40 percent credited to first touch, 40 percent to last touch, and 20 percent distributed across the middle"},
            {"question": "What is the minimum conversions per arm before a test conclusion?",
             "answer": "100 conversions per arm at 95 percent significance.",
             "evidence": "A minimum of 100 conversions per arm is required before a conclusion, and the significance threshold is 95 percent"},
        ],
    },
    {
        "id": "MKT-STD-014",
        "title": "Brand Guidelines and Messaging Standard",
        "doc_type": "Guidelines",
        "category": "Marketing",
        "department": "Brand",
        "author": "Yasmin Haddad, Brand Lead",
        "owner": "Brand",
        "version": "5.0",
        "effective": "2026-03-15",
        "classification": "Public",
        "review": "Annual",
        "summary": (
            "The Northwind brand system: the messaging hierarchy and approved "
            "value statements, tone of voice rules, visual identity including "
            "colour and typography, logo usage rules, and the approval process "
            "for third-party and partner usage."
        ),
        "tags": ["brand", "messaging", "tone of voice", "logo", "typography", "identity"],
        "sections": [
            {
                "heading": "Messaging Hierarchy",
                "paragraphs": [
                    "Messaging is fixed at three levels and may not be improvised "
                    "in customer-facing material. The category statement is: the "
                    "content platform for marketing teams who need to move fast "
                    "without breaking things. The company value statement is: "
                    "governance that feels like nothing at all, because it works "
                    "in the background.",
                    "Each product has one approved one-liner and three approved "
                    "proof points. The Insight Studio one-liner is: self-service "
                    "reporting your team can trust, because the metrics are "
                    "defined once by us. Proof points must be verifiable and "
                    "dated; undated statistics are removed at review."
                ],
                "table": [
                    ["Product", "Approved one-liner", "Proof point count", "Owner"],
                    ["Northwind Pages", "The content platform marketing teams trust", "3", "Product Marketing"],
                    ["Insight Studio", "Self-service reporting your team can trust", "3", "Product Marketing"],
                    ["Form Builder", "Forms that route, validate, and integrate themselves", "2", "Product Marketing"],
                    ["Governance Suite", "Approvals and audit without the bottleneck", "3", "Product Marketing"],
                ],
            },
            {
                "heading": "Tone of Voice",
                "paragraphs": [
                    "Northwind sounds competent, direct, and warm. Competent "
                    "means specific numbers rather than adjectives. Direct means "
                    "the point comes first and the qualifier follows. Warm means "
                    "the reader is never made to feel uninformed.",
                    "Four words are banned from customer-facing copy because they "
                    "signal vagueness: innovative, seamless, cutting-edge, and "
                    "robust. The word AI may be used only where a specific model "
                    "or capability is named, and never as a general adjective. "
                    "Passive voice is permitted where the actor is genuinely "
                    "unknown, and prohibited where it obscures responsibility, "
                    "particularly in incident communications."
                ],
                "bullets": [
                    "Banned: innovative, seamless, cutting-edge, robust.",
                    "Numbers over adjectives: say 43 percent faster, not much faster.",
                    "Point first, qualifier second.",
                    "Never blame the customer in error messages.",
                    "Error messages state what happened, why, and what to do next.",
                ],
            },
            {
                "heading": "Visual Identity",
                "paragraphs": [
                    "The primary palette is Northwind Navy #1F3A5F, Harbor Teal "
                    "#2E8B8B, and Paper #F7F8FA, with Signal Amber #E8A33D "
                    "reserved for warnings only. Body text is set in Inter at "
                    "16 pixels with a line height of 1.6; headings use Freight "
                    "Sans. Minimum contrast is 4.5 to 1 for body text and 3 to 1 "
                    "for large text, and all published material is checked with "
                    "the accessibility checker before release.",
                    "Photography is documentary rather than staged. Screenshots "
                    "must show real data patterns, never lorem ipsum, and must be "
                    "captured at the current release. Stock imagery of people "
                    "pointing at charts is prohibited outright."
                ],
                "table": [
                    ["Token", "Value", "Usage", "Contrast on Paper"],
                    ["Northwind Navy", "#1F3A5F", "Headings, primary buttons", "11.2 to 1"],
                    ["Harbor Teal", "#2E8B8B", "Links, accents", "3.9 to 1"],
                    ["Signal Amber", "#E8A33D", "Warnings only", "2.1 to 1, large text only"],
                    ["Paper", "#F7F8FA", "Backgrounds", "n/a"],
                ],
            },
            {
                "heading": "Logo Usage",
                "paragraphs": [
                    "The clear space around the logo equals the height of the N "
                    "in the wordmark. Minimum size is 24 pixels tall on screen and "
                    "10 millimetres in print. The logo may not be recoloured "
                    "outside the approved variants, rotated, stretched, or placed "
                    "on a background with insufficient contrast.",
                    "Partner and co-branded usage requires a brand review request "
                    "with the artwork attached, and is approved within three "
                    "business days. Press and analyst usage follows the press "
                    "kit and does not require review, provided the logo is used "
                    "unmodified."
                ],
                "qa": [
                    {
                        "question": "Which four words are banned from customer-facing copy?",
                        "answer": "Innovative, seamless, cutting-edge, and robust.",
                    },
                    {
                        "question": "What is the minimum body text contrast ratio?",
                        "answer": "4.5 to 1, with 3 to 1 permitted for large text.",
                    },
                    {
                        "question": "How is logo clear space measured?",
                        "answer": "By the height of the N in the wordmark.",
                    },
                ],
            },
        ],
        "qa": [
            {"question": "Which four words are banned from Northwind customer-facing copy?",
             "answer": "Innovative, seamless, cutting-edge, and robust.",
             "evidence": "Four words are banned from customer-facing copy because they signal vagueness: innovative, seamless, cutting-edge, and robust"},
            {"question": "What is the hex value of Northwind Navy?",
             "answer": "#1F3A5F.",
             "evidence": "Northwind Navy #1F3A5F"},
            {"question": "What minimum contrast ratio is required for body text?",
             "answer": "4.5 to 1.",
             "evidence": "Minimum contrast is 4.5 to 1 for body text and 3 to 1 for large text"},
            {"question": "How is logo clear space defined?",
             "answer": "Equal to the height of the N in the wordmark.",
             "evidence": "The clear space around the logo equals the height of the N in the wordmark"},
            {"question": "What body font and size does the brand system specify?",
             "answer": "Inter at 16 pixels with a line height of 1.6.",
             "evidence": "Body text is set in Inter at 16 pixels with a line height of 1.6"},
        ],
    },
    {
        "id": "MKT-STD-019",
        "title": "Marketing Analytics and Attribution Standard",
        "doc_type": "Standard",
        "category": "Marketing",
        "department": "Marketing Operations",
        "author": "Felix Andersson, Head of Demand Generation",
        "owner": "Marketing Operations",
        "version": "2.4",
        "effective": "2026-04-01",
        "classification": "Confidential",
        "review": "Annual",
        "summary": (
            "How marketing measurement is run at Northwind: the tracking stack, "
            "consent and cookie handling, UTM discipline, the marketing data "
            "model, pipeline attribution rules, and the reporting cadence and "
            "data quality checks."
        ),
        "tags": ["marketing analytics", "attribution", "UTM", "consent", "pipeline", "measurement"],
        "sections": [
            {
                "heading": "Tracking Stack",
                "paragraphs": [
                    "Marketing data flows from the tag manager through the "
                    "consent management platform into the customer data platform, "
                    "then into the warehouse and the CRM. Server-side tagging is "
                    "used for all advertising pixels, which improves resilience "
                    "to ad blockers and keeps the browser payload small.",
                    "Only the Marketing Operations team may create or edit tags. "
                    "Tags created by other teams are removed at the weekly audit, "
                    "because unmanaged tags are the main cause of duplicate "
                    "conversion reporting and of consent violations."
                ],
            },
            {
                "heading": "Consent and Cookies",
                "paragraphs": [
                    "No advertising or analytics cookie is set before consent is "
                    "recorded, and consent state is stored for 13 months with an "
                    "audit record. Consent mode is enforced server-side rather "
                    "than trusting the browser implementation, because a "
                    "client-side-only check has been bypassed in the past.",
                    "Where consent is refused, conversion modelling fills the gap "
                    "and is labelled as modelled in every report. Modelled and "
                    "observed conversions are never summed without the label, "
                    "because the combined figure is the most common source of "
                    "overstated performance in a board pack."
                ],
                "bullets": [
                    "No non-essential cookie before recorded consent.",
                    "Consent state retained 13 months with an audit record.",
                    "Server-side consent enforcement, not browser-only.",
                    "Modelled conversions always labelled as modelled.",
                ],
            },
            {
                "heading": "UTM Discipline",
                "paragraphs": [
                    "Every campaign URL uses the five standard parameters, built "
                    "from the Campaign Registry rather than typed by hand. "
                    "source, medium, and campaign are mandatory; term and "
                    "content are required for paid search and for split tests "
                    "respectively. Free-text values are rejected at ingestion.",
                    "Medium values come from a fixed list of 14, which is the "
                    "single most effective measurement fix the team has made. "
                    "Before the list existed, 61 distinct medium values were in "
                    "use for what was effectively four channels, which made "
                    "channel comparison meaningless."
                ],
                "table": [
                    ["Parameter", "Required", "Source of value", "Example"],
                    ["utm_source", "Yes", "Registry", "google, partner-agency-x"],
                    ["utm_medium", "Yes", "Fixed list of 14", "cpc, email, partner"],
                    ["utm_campaign", "Yes", "Registry", "2026-q3-insight-launch"],
                    ["utm_term", "Paid search only", "Registry", "headless-cms"],
                    ["utm_content", "For split tests", "Registry", "hero-b"],
                ],
            },
            {
                "heading": "Pipeline Attribution Rules",
                "paragraphs": [
                    "A lead is created when a person submits a form or starts a "
                    "trial and is matched to an account by domain and by CRM "
                    "record. Leads are deduplicated on email with a 90 day "
                    "window, and the first-touch and last-touch sources are both "
                    "stored permanently rather than overwritten, because "
                    "overwriting destroys the ability to re-run attribution.",
                    "Marketing-qualified lead status requires the contact to be "
                    "in the target segment, to have a verified business email, "
                    "and to have taken a qualifying action. Self-declared "
                    "interest alone does not qualify. MQL to opportunity "
                    "conversion is reported monthly and the current rate is 31 "
                    "percent."
                ],
            },
            {
                "heading": "Reporting and Quality Checks",
                "paragraphs": [
                    "Three reports run on a cadence: a daily anomaly check on "
                    "volume and conversion rate, a weekly channel performance "
                    "review, and a monthly full-funnel report to the Executive "
                    "Staff. The daily check compares yesterday against a 28-day "
                    "same-weekday baseline with a 30 percent tolerance.",
                    "Four quality checks run before any number is published: "
                    "tag health, UTM coverage above 95 percent of sessions, "
                    "CRM lead match rate above 85 percent, and duplicate rate "
                    "below 3 percent. A report published with a failed check must "
                    "state the failure on the report."
                ],
                "qa": [
                    {
                        "question": "Who may create or edit marketing tags?",
                        "answer": "Only the Marketing Operations team.",
                    },
                    {
                        "question": "How long is consent state retained?",
                        "answer": "13 months with an audit record.",
                    },
                    {
                        "question": "What is the minimum UTM coverage required before publishing?",
                        "answer": "95 percent of sessions.",
                    },
                ],
            },
        ],
        "qa": [
            {"question": "How long is consent state retained?",
             "answer": "13 months, with an audit record.",
             "evidence": "consent state is stored for 13 months with an audit record"},
            {"question": "How many distinct utm_medium values are permitted?",
             "answer": "A fixed list of 14.",
             "evidence": "Medium values come from a fixed list of 14"},
            {"question": "What is the current MQL to opportunity conversion rate?",
             "answer": "31 percent.",
             "evidence": "the current rate is 31 percent"},
            {"question": "What minimum UTM coverage is required before publishing a report?",
             "answer": "95 percent of sessions.",
             "evidence": "UTM coverage above 95 percent of sessions"},
            {"question": "What tolerance does the daily anomaly check use?",
             "answer": "30 percent against a 28-day same-weekday baseline.",
             "evidence": "compares yesterday against a 28-day same-weekday baseline with a 30 percent tolerance"},
        ],
    },
    {
        "id": "MKT-STD-026",
        "title": "Sales Enablement and Competitive Positioning Standard",
        "doc_type": "Standard",
        "category": "Marketing",
        "department": "Sales Enablement",
        "author": "Gabriel Moreau, Head of Sales Enablement",
        "owner": "Sales Enablement",
        "version": "3.1",
        "effective": "2026-05-15",
        "classification": "Confidential",
        "review": "Quarterly",
        "summary": (
            "How Northwind equips its sales team: the enablement curriculum and "
            "certification, the battlecard system and refresh rules, the "
            "competitive intelligence process, discovery and demo standards, and "
            "the content request workflow with service levels."
        ),
        "tags": ["sales enablement", "battlecard", "competitive", "certification", "demo", "discovery"],
        "sections": [
            {
                "heading": "Certification",
                "paragraphs": [
                    "Reps must be certified before carrying a quota. "
                    "Certification covers the value story for each of the four "
                    "products, the three primary competitive positions, the "
                    "discovery framework, and the pricing guardrails. The pass "
                    "mark is 80 percent, and certification expires after 12 "
                    "months or on any material product change, whichever comes "
                    "first.",
                    "Uncertified reps may shadow calls but may not run a "
                    "discovery call or present pricing. Managers may not waive "
                    "this, because an uncertified rep quoting an unsupported "
                    "commitment creates a contractual expectation the company "
                    "must later absorb."
                ],
                "table": [
                    ["Module", "Duration", "Pass mark", "Renewal"],
                    ["Value story, all products", "90 minutes", "80 percent", "Annual"],
                    ["Competitive positions", "60 minutes", "80 percent", "Quarterly"],
                    ["Discovery framework", "45 minutes", "85 percent", "Annual"],
                    ["Pricing guardrails", "30 minutes", "90 percent", "Semi-annual"],
                ],
            },
            {
                "heading": "Battlecards",
                "paragraphs": [
                    "A battlecard exists for each of the nine named competitors "
                    "and follows a fixed structure: their positioning, where they "
                    "genuinely win, where Northwind wins, the landmines to plant "
                    "as questions, the objection responses, and the proof points "
                    "with sources. The section admitting where the competitor "
                    "wins is mandatory, because a rep who denies a competitor's "
                    "strength loses credibility on everything else.",
                    "Battlecards are refreshed quarterly and immediately on any "
                    "competitor pricing or packaging change. A card older than "
                    "90 days is marked stale in the enablement library and is "
                    "hidden from search, which is more effective than asking reps "
                    "to check the date themselves."
                ],
                "bullets": [
                    "Nine competitor battlecards, refreshed quarterly.",
                    "Mandatory section on where the competitor wins.",
                    "Every claim carries a source and a date.",
                    "Cards older than 90 days are marked stale and hidden.",
                    "Objection responses are scripted and certified, not improvised.",
                ],
            },
            {
                "heading": "Competitive Intelligence",
                "paragraphs": [
                    "Intelligence is gathered from win-loss interviews, "
                    "competitive deal notes, public pricing pages, and partner "
                    "feedback. Win-loss interviews are conducted by a neutral "
                    "third party rather than the rep, because the rep's presence "
                    "suppresses honest feedback; the current completion rate is "
                    "38 percent of closed deals.",
                    "Claims about a competitor must be sourced and dated before "
                    "they enter a battlecard or a customer conversation. An "
                    "unsourced claim repeated to a customer is a conduct issue, "
                    "not a sales technique."
                ],
            },
            {
                "heading": "Discovery and Demo Standards",
                "paragraphs": [
                    "Discovery uses a documented framework of 12 questions across "
                    "four areas: current state, the trigger that started the "
                    "evaluation, the decision criteria, and the decision process "
                    "including budget authority and timeline. The last area is "
                    "the one most often skipped and the one most predictive of a "
                    "stalled deal.",
                    "Demos are tailored or not run. A demo must open with the "
                    "customer's stated pain, show no more than three capabilities, "
                    "and close with a mutual next step agreed on the call. "
                    "Feature tours correlate with longer cycles in the internal "
                    "data and are discouraged."
                ],
                "steps": [
                    "Confirm the stakeholder in the room and their personal stake in the outcome.",
                    "Establish the trigger event and the date it began.",
                    "Surface the decision criteria in the customer's own words.",
                    "Establish the decision process: who signs, budget authority, and the timeline.",
                    "Agree the specific mutual next step with a date before ending the call.",
                ],
            },
            {
                "heading": "Content Requests",
                "paragraphs": [
                    "Reps request content through the Enablement Portal, which "
                    "routes to Product Marketing with the deal context attached. "
                    "Standard requests, meaning an existing asset tailored, have "
                    "a two business day service level; new assets are scoped as "
                    "projects. Requests without deal context are returned.",
                    "Asset usage is measured so that production focuses on what "
                    "is actually used. Roughly 30 percent of the library has not "
                    "been opened in 180 days and is scheduled for retirement, "
                    "which frees capacity for the assets that close deals."
                ],
                "qa": [
                    {
                        "question": "What is the certification pass mark?",
                        "answer": "80 percent, rising to 90 percent for pricing guardrails.",
                    },
                    {
                        "question": "How many competitor battlecards exist?",
                        "answer": "Nine, refreshed quarterly.",
                    },
                    {
                        "question": "Who conducts win-loss interviews and why?",
                        "answer": "A neutral third party rather than the rep, because the rep's presence suppresses honest feedback.",
                    },
                ],
            },
        ],
        "qa": [
            {"question": "How many competitor battlecards does Northwind maintain?",
             "answer": "Nine.",
             "evidence": "A battlecard exists for each of the nine named competitors"},
            {"question": "What is the certification pass mark?",
             "answer": "80 percent, with 85 percent for discovery and 90 percent for pricing guardrails.",
             "evidence": "The pass mark is 80 percent, and certification expires after 12 months"},
            {"question": "Who conducts win-loss interviews?",
             "answer": "A neutral third party rather than the rep.",
             "evidence": "conducted by a neutral third party rather than the rep"},
            {"question": "What share of the enablement library is unused for 180 days?",
             "answer": "Roughly 30 percent.",
             "evidence": "Roughly 30 percent of the library has not been opened in 180 days"},
            {"question": "After how many days is a battlecard marked stale?",
             "answer": "90 days.",
             "evidence": "A card older than 90 days is marked stale in the enablement library"},
        ],
    },
]
