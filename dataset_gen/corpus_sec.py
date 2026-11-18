"""Information Security corpus (5 documents)."""

DOCS = [
    {
        "id": "SEC-POL-002",
        "title": "Acceptable Use of Information Systems Policy",
        "doc_type": "Policy",
        "category": "Information Security",
        "department": "Information Security",
        "author": "Ravi Chandrasekhar, Chief Information Security Officer",
        "owner": "Information Security",
        "version": "7.0",
        "effective": "2026-01-01",
        "classification": "Internal",
        "review": "Annual",
        "summary": (
            "Defines what employees may and may not do with Northwind systems, "
            "devices, data, and network access. Covers permitted personal use, "
            "prohibited activities, password and multi-factor requirements, "
            "approved file-sharing and AI tools, encryption, and the "
            "consequences of misuse."
        ),
        "tags": ["acceptable use", "AUP", "MFA", "encryption", "shadow IT", "AI tools"],
        "sections": [
            {
                "heading": "Scope and Ownership",
                "paragraphs": [
                    "This policy applies to all Northwind information assets "
                    "and to every person granted access, including employees, "
                    "contractors, and third parties. Northwind information "
                    "assets include laptops, phones, accounts, email, the "
                    "corporate network, cloud tenants, source code, and all "
                    "data created or stored on Northwind systems.",
                    "All Northwind data is owned by Northwind, including "
                    "anything an employee creates on a personal device for work "
                    "purposes. On separation, an employee must surrender or "
                    "securely delete work data and must not retain copies."
                ],
            },
            {
                "heading": "Authentication Requirements",
                "paragraphs": [
                    "Passwords must be at least 14 characters, must not be "
                    "reused across systems, and must be stored only in the "
                    "approved password vault, Bitwarden Teams. Password sharing "
                    "is prohibited without exception, including sharing with a "
                    "manager or an assistant. Multi-factor authentication is "
                    "mandatory on all systems that support it; the approved "
                    "factors are a hardware security key, Time-based One-Time "
                    "Password, or platform authenticator. SMS is not an "
                    "approved factor for any system holding customer data.",
                    "Privileged accounts require a hardware security key and a "
                    "separate privileged identity that is not used for email or "
                    "web browsing. Break-glass accounts are stored sealed in "
                    "the vault and every use generates an immediate alert to "
                    "the Security Operations Center."
                ],
                "table": [
                    ["System tier", "Password minimum", "Approved MFA factors", "Session limit"],
                    ["Tier 1 (public marketing)", "12 characters", "TOTP, key, SMS", "12 hours"],
                    ["Tier 2 (internal business)", "14 characters", "TOTP, key", "8 hours"],
                    ["Tier 3 (customer or production data)", "18 characters", "Hardware key only", "30 minutes idle"],
                    ["Privileged", "24 characters, vault generated", "Hardware key only", "15 minutes idle"],
                ],
            },
            {
                "heading": "Approved and Prohibited Tools",
                "paragraphs": [
                    "Installing software on a Northwind device requires that the "
                    "application appear in the Approved Application Register. "
                    "Applications outside the register are blocked by the "
                    "endpoint policy, and requesting an exception is a "
                    "self-service ticket with a five business day service level. "
                    "Running unapproved software, including portable "
                    "executables, is a policy violation even where no data is "
                    "exposed.",
                    "Generative AI tools are permitted only through the "
                    "approved enterprise gateways, which are the Microsoft "
                    "Copilot tenant and the internal Model Gateway. Pasting "
                    "customer data, source code classified Confidential, "
                    "personal data, or credential material into a public AI "
                    "service is prohibited. The Model Gateway logs prompts for "
                    "90 days for abuse review and does not send prompts to "
                    "third-party training."
                ],
                "bullets": [
                    "Prohibited: sharing credentials, disabling endpoint protection, and forwarding Northwind mail to external accounts.",
                    "Prohibited: storing customer data in personal cloud storage or personal email.",
                    "Prohibited: using public AI services with any Confidential or higher data.",
                    "Permitted: limited personal use that does not interfere with work and does not use Northwind data.",
                    "Permitted: personal devices for work only when enrolled in the mobile device management profile.",
                ],
            },
            {
                "heading": "Encryption and Data Handling",
                "paragraphs": [
                    "Full-disk encryption is mandatory on every laptop and "
                    "phone, enforced by the endpoint management platform, and "
                    "the recovery keys are escrowed in Azure AD. Removable "
                    "media is blocked by default; approved exceptions require "
                    "a business justification, are limited to encrypted "
                    "hardware tokens, and expire after 30 days.",
                    "Email containing Confidential data must be sent through "
                    "the secure message portal rather than as an attachment. "
                    "Files shared externally must use the Northwind file "
                    "gateway with an expiry of no more than 14 days and, for "
                    "customer data, a named recipient rather than a public "
                    "link."
                ],
                "notes": [
                    "Loss or theft: report any lost or stolen device to the "
                    "Security Operations Center within four hours. Late "
                    "reporting turns a contained incident into a notifiable "
                    "data breach."
                ],
            },
            {
                "heading": "Monitoring and Consequences",
                "paragraphs": [
                    "Northwind monitors its systems, networks, and accounts on "
                    "a continuous basis. Monitoring covers endpoint telemetry, "
                    "network flows, authentication logs, email content "
                    "scanning, and Data Loss Prevention rules. Employees have "
                    "no expectation of privacy in Northwind systems or in "
                    "Northwind-issued accounts, including where personal use is "
                    "permitted.",
                    "Violations are handled under the Workplace Conduct and "
                    "Anti-Harassment Standard and may result in access "
                    "revocation, disciplinary action up to termination, contract "
                    "termination for vendors, or referral to law enforcement "
                    "where criminal conduct is suspected."
                ],
                "qa": [
                    {
                        "question": "Is SMS an approved second factor?",
                        "answer": "No. SMS is not approved for any system holding customer data; approved factors are a hardware key, TOTP, or platform authenticator.",
                    },
                    {
                        "question": "How long are Model Gateway prompts retained?",
                        "answer": "90 days, for abuse review only.",
                    },
                    {
                        "question": "What is the reporting deadline for a lost device?",
                        "answer": "Four hours, to the Security Operations Center.",
                    },
                ],
            },
        ],
        "qa": [
            {"question": "What is the minimum password length for a Tier 3 system holding customer data?",
             "answer": "18 characters, with hardware key MFA and a 30 minute idle session limit.",
             "evidence": "Tier 3 (customer or production data) | 18 characters | Hardware key only | 30 minutes idle"},
            {"question": "Which AI tools are approved for use with Northwind data?",
             "answer": "Only the approved enterprise gateways: the Microsoft Copilot tenant and the internal Model Gateway.",
             "evidence": "approved enterprise gateways, which are the Microsoft Copilot tenant and the internal Model Gateway"},
            {"question": "How long may an external file share link remain valid?",
             "answer": "No more than 14 days, and it must name a recipient rather than be a public link for customer data.",
             "evidence": "with an expiry of no more than 14 days"},
            {"question": "Where must passwords be stored?",
             "answer": "Only in the approved password vault, Bitwarden Teams.",
             "evidence": "stored only in the approved password vault, Bitwarden Teams"},
            {"question": "How long do approved removable media exceptions last?",
             "answer": "30 days.",
             "evidence": "expire after 30 days"},
        ],
    },
    {
        "id": "SEC-STD-005",
        "title": "Incident Response Standard",
        "doc_type": "Standard",
        "category": "Information Security",
        "department": "Security Operations",
        "author": "Yuki Tanaka, Head of Security Operations",
        "owner": "Security Operations",
        "version": "4.2",
        "effective": "2026-02-15",
        "classification": "Confidential",
        "review": "Semi-annual",
        "summary": (
            "Defines the Northwind incident severity scale, the incident "
            "command roles, the six-phase response lifecycle with time targets, "
            "the on-call escalation ladder, evidence preservation rules, and "
            "the regulatory notification clocks that apply to personal data "
            "breaches."
        ),
        "tags": ["incident response", "severity", "escalation", "breach notification", "IR", "forensics"],
        "sections": [
            {
                "heading": "Severity Classification",
                "paragraphs": [
                    "Severity is assigned by the first responder on duty and "
                    "confirmed by the Incident Commander within 30 minutes. "
                    "Severity may be raised at any time and may only be lowered "
                    "by the Incident Commander with a recorded reason. When in "
                    "doubt, classify higher; over-classification carries no "
                    "penalty."
                ],
                "table": [
                    ["Severity", "Definition", "Acknowledge", "Target containment", "Notify"],
                    ["SEV-1 Critical", "Production down, or confirmed exfiltration of customer data", "15 minutes", "4 hours", "Executive Staff immediately, regulator within 72h"],
                    ["SEV-2 High", "Degraded production, or confirmed compromise of a privileged account", "30 minutes", "8 hours", "CISO and department head"],
                    ["SEV-3 Moderate", "Single-host compromise with no privileged access, malware on a workstation", "4 hours", "3 business days", "Security Operations queue"],
                    ["SEV-4 Low", "Policy violation, phishing report, no confirmed compromise", "1 business day", "10 business days", "Queue only"],
                ],
            },
            {
                "heading": "Incident Command Roles",
                "paragraphs": [
                    "Every SEV-1 and SEV-2 incident appoints four distinct "
                    "roles, and one person may hold only one role. The Incident "
                    "Commander owns the outcome, approves phase transitions, and "
                    "is the only person authorised to declare an incident closed. "
                    "The Technical Lead directs investigation and containment. "
                    "The Scribe maintains the timeline, which becomes the "
                    "official record and is the artefact reviewed in the "
                    "post-incident review. The Communications Lead is the single "
                    "channel to the business, to customers, and to regulators.",
                    "A common failure mode is the Incident Commander also acting "
                    "as Technical Lead. This is prohibited for SEV-1 because it "
                    "removes the decision-maker from the investigation at the "
                    "moment the decisions matter most."
                ],
                "bullets": [
                    "Incident Commander: owns outcome, approves transitions, declares closure.",
                    "Technical Lead: directs investigation, containment, and recovery.",
                    "Scribe: maintains the authoritative timeline with timestamps.",
                    "Communications Lead: sole channel to business, customers, and regulators.",
                ],
            },
            {
                "heading": "Response Lifecycle",
                "paragraphs": [
                    "Northwind follows six phases. Preparation covers runbooks, "
                    "access, and tooling and is continuous. Identification ends "
                    "when the team can state what is affected and how it is "
                    "being affected. Containment stops the bleeding and is split "
                    "into short-term containment, such as isolating a host, and "
                    "long-term containment, such as rotating credentials. "
                    "Eradication removes the root cause, including the specific "
                    "persistence mechanism, not only the symptom.",
                    "Recovery returns service to production with enhanced "
                    "monitoring for at least 72 hours. Lessons Learned closes "
                    "the incident and must be held within five business days of "
                    "recovery for SEV-1 and SEV-2. Every action taken during an "
                    "incident must be recorded in the ticket with a UTC "
                    "timestamp at the time it was taken, not reconstructed later."
                ],
                "notes": [
                    "Do not declare closure while the attacker's persistence "
                    "mechanism is unidentified. Re-intrusion after a premature "
                    "closure is treated as a failed response, not a new incident."
                ],
            },
            {
                "heading": "Evidence Preservation",
                "paragraphs": [
                    "For any incident involving suspected criminal conduct, "
                    "insider threat, or regulatory exposure, the team must "
                    "preserve evidence before remediating. Preserve a memory "
                    "image before rebooting, a full disk image before "
                    "reimaging, and export relevant logs to the evidence bucket "
                    "before log rotation. The evidence bucket is write-once with "
                    "a seven year retention and access restricted to the "
                    "Forensics team and Legal.",
                    "Chain of custody is recorded for every artefact: who "
                    "collected it, when, from which asset, the hash value, and "
                    "every subsequent transfer. An artefact without a valid "
                    "chain of custody cannot be relied on in a disciplinary or "
                    "legal proceeding."
                ],
            },
            {
                "heading": "Notification Clocks",
                "paragraphs": [
                    "Where a personal data breach is likely to result in a risk "
                    "to individuals, the Data Protection Officer must notify the "
                    "lead supervisory authority within 72 hours of becoming "
                    "aware, and must notify affected individuals without undue "
                    "delay where the risk is high. Becoming aware means a "
                    "reasonable degree of certainty, not proof, so the clock "
                    "starts at the Identification phase rather than at root "
                    "cause analysis.",
                    "US state breach laws impose their own clocks, several of "
                    "which are shorter than 72 hours measured from discovery, "
                    "and some require notification to a state attorney general "
                    "at a threshold number of residents. The Legal team maintains "
                    "the current matrix. Never communicate externally about an "
                    "incident except through the Communications Lead."
                ],
                "qa": [
                    {
                        "question": "What is the containment target for a SEV-1 incident?",
                        "answer": "Four hours, with acknowledgement inside 15 minutes.",
                    },
                    {
                        "question": "When does the 72 hour regulatory clock start?",
                        "answer": "At awareness, meaning reasonable certainty, which is the Identification phase rather than root cause analysis.",
                    },
                    {
                        "question": "How soon must a post-incident review be held after a SEV-1?",
                        "answer": "Within five business days of recovery.",
                    },
                ],
            },
        ],
        "qa": [
            {"question": "What is the acknowledgement target for a SEV-1 security incident?",
             "answer": "15 minutes.",
             "evidence": "SEV-1 Critical ... 15 minutes"},
            {"question": "How long is evidence retained in the Northwind evidence bucket?",
             "answer": "Seven years, write-once, restricted to Forensics and Legal.",
             "evidence": "The evidence bucket is write-once with a seven year retention"},
            {"question": "Within how many hours must a personal data breach be reported to the supervisory authority?",
             "answer": "72 hours of becoming aware.",
             "evidence": "notify the lead supervisory authority within 72 hours of becoming aware"},
            {"question": "Which role is the sole channel to customers and regulators during an incident?",
             "answer": "The Communications Lead.",
             "evidence": "The Communications Lead is the single channel to the business, to customers, and to regulators"},
            {"question": "How long must enhanced monitoring run during the recovery phase?",
             "answer": "At least 72 hours.",
             "evidence": "enhanced monitoring for at least 72 hours"},
        ],
    },
    {
        "id": "SEC-STD-008",
        "title": "Secure Software Development Lifecycle Standard",
        "doc_type": "Standard",
        "category": "Information Security",
        "department": "Information Security",
        "author": "Elena Vasquez, Principal Security Engineer",
        "owner": "Information Security and Engineering",
        "version": "3.1",
        "effective": "2026-03-01",
        "classification": "Internal",
        "review": "Annual",
        "summary": (
            "Mandatory security gates for software delivered by Northwind "
            "engineering: threat modelling thresholds, secret management, "
            "dependency and SAST scanning gates, code review rules, the "
            "vulnerability SLA matrix by CVSS, and the exception process."
        ),
        "tags": ["SSDLC", "threat model", "SAST", "secrets", "CVE", "code review", "CVSS"],
        "sections": [
            {
                "heading": "Security Gates by Change Type",
                "paragraphs": [
                    "Every change passes the gates that match its risk. A change "
                    "that touches authentication, authorisation, cryptography, "
                    "payment processing, or any endpoint that accepts untrusted "
                    "input is a security-relevant change and requires a threat "
                    "model reviewed by a security engineer before code is "
                    "written. A change that only alters internal business logic "
                    "with no new input surface requires automated scanning only.",
                    "Gates are enforced in CI and cannot be bypassed by "
                    "developers. Only a Security Champion with an active "
                    "delegation may waive a gate, and every waiver is logged "
                    "with a reason and expires after 14 days."
                ],
                "table": [
                    ["Change type", "Threat model", "Security review", "SAST", "Dependency scan", "Pen test"],
                    ["New public API", "Required", "Required", "Required", "Required", "Required"],
                    ["Auth or crypto change", "Required", "Required", "Required", "Required", "Required"],
                    ["New internal service", "Required", "Recommended", "Required", "Required", "Not required"],
                    ["Dependency upgrade", "Not required", "Not required", "Required", "Required", "Not required"],
                    ["UI copy change", "Not required", "Not required", "Required", "Required", "Not required"],
                ],
            },
            {
                "heading": "Secrets Management",
                "paragraphs": [
                    "Secrets are stored in HashiCorp Vault and are never "
                    "committed to source control, never placed in "
                    "configuration files checked into a repository, and never "
                    "printed to application logs. Applications authenticate to "
                    "Vault using a workload identity rather than a static "
                    "token. Secret TTL is 24 hours for production and 72 hours "
                    "for non-production, with automatic renewal.",
                    "If a secret is ever committed, treat it as compromised "
                    "immediately: rotate it first, then remove it from history. "
                    "Deleting the line in a later commit does not remediate the "
                    "exposure because the value remains in the object store. "
                    "The pre-commit hook and the push-time scanner both block "
                    "high-confidence secrets, and a push blocked three times by "
                    "the scanner automatically raises a SEV-3 ticket."
                ],
                "bullets": [
                    "Vault is the only approved secret store for services.",
                    "Production secret TTL is 24 hours; non-production is 72 hours.",
                    "Rotate first, scrub history second; scrubbing alone is not remediation.",
                    "Personal access tokens for repositories expire after 90 days.",
                ],
            },
            {
                "heading": "Vulnerability Remediation SLAs",
                "paragraphs": [
                    "Remediation clocks run from the moment a finding is "
                    "recorded in the vulnerability register, which is the "
                    "earliest of a scanner report, a penetration test finding, "
                    "or a coordinated disclosure. The clock is measured in "
                    "business days and is not paused by release freezes; a "
                    "freeze requires a formal exception, not a silent delay.",
                    "Findings are scored with CVSS v3.1 base score, adjusted "
                    "upward by one band where the asset is internet-facing or "
                    "holds customer data. Exploited-in-the-wild findings are "
                    "escalated to Critical regardless of score."
                ],
                "table": [
                    ["Severity", "CVSS range", "Production SLA", "Non-production SLA", "Escalation"],
                    ["Critical", "9.0-10.0", "72 hours", "10 business days", "CISO at 24 hours"],
                    ["High", "7.0-8.9", "10 business days", "30 business days", "Department head at SLA"],
                    ["Medium", "4.0-6.9", "30 business days", "90 business days", "Quarterly review"],
                    ["Low", "0.1-3.9", "90 business days", "Next major release", "Backlog"],
                ],
            },
            {
                "heading": "Code Review Rules",
                "paragraphs": [
                    "Every change to a production-bound branch requires at "
                    "least one approving reviewer, and two approving reviewers "
                    "where the change is security-relevant or touches more than "
                    "400 lines. Self-approval is blocked by branch protection. "
                    "Authors must state the blast radius and the rollback plan "
                    "in the pull request description; a pull request without a "
                    "rollback plan cannot be approved.",
                    "Reviewers review for correctness, security, and "
                    "observability. A review that approves in under two minutes "
                    "for a change above 100 lines is flagged in the monthly "
                    "engineering quality report as a rubber-stamp review."
                ],
                "qa": [
                    {
                        "question": "What is the production SLA for a Critical vulnerability?",
                        "answer": "72 hours, with escalation to the CISO at 24 hours.",
                    },
                    {
                        "question": "How many reviewers are needed for a security-relevant change?",
                        "answer": "Two approving reviewers.",
                    },
                    {
                        "question": "What is the production secret TTL?",
                        "answer": "24 hours, renewed automatically.",
                    },
                ],
            },
            {
                "heading": "Dependency and Supply Chain Controls",
                "paragraphs": [
                    "All third-party dependencies must be pinned to an exact "
                    "version with a lock file, and must be mirrored through the "
                    "internal package proxy so that provenance is verifiable. "
                    "Dependencies with a known Critical or High advisory are "
                    "blocked from production builds unless an exception is "
                    "recorded. Container images must be built from approved "
                    "base images and are signed; the cluster admission "
                    "controller rejects unsigned images.",
                    "A software bill of materials is generated for every "
                    "release and retained for the supported lifetime of the "
                    "release. Customers may request the SBOM for their tenant "
                    "through the Trust Portal."
                ],
            },
        ],
        "qa": [
            {"question": "What is the remediation SLA for a Critical vulnerability in production?",
             "answer": "72 hours.",
             "evidence": "Critical | 9.0-10.0 | 72 hours"},
            {"question": "What is the production TTL for secrets in Vault?",
             "answer": "24 hours, with automatic renewal.",
             "evidence": "Secret TTL is 24 hours for production and 72 hours for non-production"},
            {"question": "How many approving reviewers does a security-relevant change need?",
             "answer": "Two approving reviewers.",
             "evidence": "two approving reviewers where the change is security-relevant or touches more than 400 lines"},
            {"question": "How long does a security gate waiver last?",
             "answer": "14 days, after which it expires.",
             "evidence": "every waiver is logged with a reason and expires after 14 days"},
            {"question": "What happens when a push is blocked by the secret scanner three times?",
             "answer": "A SEV-3 ticket is raised automatically.",
             "evidence": "a push blocked three times by the scanner automatically raises a SEV-3 ticket"},
        ],
    },
    {
        "id": "SEC-STD-012",
        "title": "Data Classification and Handling Standard",
        "doc_type": "Standard",
        "category": "Information Security",
        "department": "Data Governance",
        "author": "Amara Osei, Head of Data Governance",
        "owner": "Data Governance",
        "version": "2.6",
        "effective": "2026-05-01",
        "classification": "Internal",
        "review": "Annual",
        "summary": (
            "Defines the four Northwind data classification levels, gives "
            "examples of each, sets the handling rules for storage, "
            "transmission, sharing, retention and destruction per level, and "
            "describes the labelling and classification review obligations of "
            "data owners."
        ),
        "tags": ["data classification", "confidential", "handling", "retention", "DLP", "labelling"],
        "sections": [
            {
                "heading": "Classification Levels",
                "paragraphs": [
                    "Every Northwind asset carries exactly one classification, "
                    "which is the highest level of any content it contains. "
                    "Classification is assigned by the data owner at creation "
                    "and is reviewed at least annually. When two sources of "
                    "different levels are combined, the result inherits the "
                    "higher level, and aggregation can raise a level even where "
                    "no single field would justify it."
                ],
                "table": [
                    ["Level", "Definition", "Examples", "Default label"],
                    ["Public", "Approved for release to anyone", "Marketing pages, published API docs, press releases", "Public"],
                    ["Internal", "Routine business information, low harm if disclosed", "Org charts, internal policies, non-sensitive metrics", "Internal Use Only"],
                    ["Confidential", "Business or personal harm if disclosed", "Customer records, source code, salaries, contracts, security findings", "Confidential"],
                    ["Restricted", "Severe harm, legal privilege, or regulated data", "Payment credentials, health data, government IDs, M&A plans, breach evidence", "Restricted"],
                ],
            },
            {
                "heading": "Handling Rules",
                "paragraphs": [
                    "Confidential data must be encrypted in transit using TLS "
                    "1.2 or higher and at rest using provider-managed keys with "
                    "customer-managed keys for Restricted. Confidential data "
                    "may be shared externally only through the file gateway with "
                    "an expiry and a named recipient. Restricted data may not "
                    "be emailed under any circumstances, including encrypted "
                    "attachments.",
                    "Internal data may circulate freely inside Northwind but "
                    "must not be posted to public forums or shared with vendors "
                    "without a non-disclosure agreement. Public data still "
                    "requires a release check: only the Communications team may "
                    "reclassify Internal material as Public."
                ],
                "bullets": [
                    "Restricted: no email, no personal devices, no public cloud storage, access logged and reviewed monthly.",
                    "Confidential: encrypted at rest and in transit, external sharing only via the file gateway.",
                    "Internal: free movement inside Northwind, NDA required before vendor disclosure.",
                    "Public: release approved by Communications, then unrestricted.",
                ],
            },
            {
                "heading": "Labelling",
                "paragraphs": [
                    "Documents, spreadsheets, and emails must carry a visible "
                    "label in the header or subject line, and must also carry "
                    "the sensitivity label applied by the Microsoft Purview "
                    "client. The Purview label is authoritative because it "
                    "travels with the file and drives Data Loss Prevention "
                    "policy. A document whose visible label and Purview label "
                    "disagree is treated as the higher of the two.",
                    "Source code repositories are classified at repository "
                    "level in the repository manifest. A repository that "
                    "contains any Restricted material, such as embedded "
                    "credentials or production data fixtures, must be "
                    "reclassified to Restricted, which disables forking and "
                    "external collaborator access."
                ],
                "notes": [
                    "Aggregation warning: a spreadsheet of Internal salary "
                    "bands becomes Confidential once it is joined to named "
                    "employees. When in doubt, classify up."
                ],
            },
            {
                "heading": "Retention and Destruction",
                "paragraphs": [
                    "Retention is set by the Retention Schedule, not by "
                    "individual preference. Customer contract records are "
                    "retained for seven years after contract end to satisfy tax "
                    "and audit obligations. Security logs are retained for 13 "
                    "months, and incident evidence for seven years. Support "
                    "tickets containing customer data are retained for 24 "
                    "months and then anonymised rather than deleted, so that "
                    "analytics remain possible.",
                    "Destruction must be verifiable. For databases this means a "
                    "documented delete job with an audit record; for object "
                    "storage it means deletion plus expiry of all versions and "
                    "replicas; for paper it means cross-cut shredding or a "
                    "certified destruction vendor. Restoring from backup to "
                    "satisfy a deletion request is required where the backup is "
                    "the only remaining copy and restoration is technically "
                    "feasible."
                ],
                "qa": [
                    {
                        "question": "Can Restricted data be emailed with an encrypted attachment?",
                        "answer": "No. Restricted data may not be emailed under any circumstances.",
                    },
                    {
                        "question": "How long are security logs retained?",
                        "answer": "13 months.",
                    },
                    {
                        "question": "What happens when labels disagree on a document?",
                        "answer": "The document is treated as the higher of the two levels.",
                    },
                ],
            },
            {
                "heading": "Owner Responsibilities",
                "paragraphs": [
                    "Every dataset has a named owner recorded in the data "
                    "catalogue. The owner assigns classification, approves "
                    "access requests within 3 business days, conducts the annual "
                    "classification review, and is accountable for the accuracy "
                    "of retention settings. Owners may delegate approval to a "
                    "steward but may not delegate accountability.",
                    "Where an owner cannot be identified, the dataset is "
                    "treated as Confidential and access is frozen until an "
                    "owner is appointed by the Data Governance Council. Orphaned "
                    "datasets older than 180 days without an owner are archived "
                    "and scheduled for destruction."
                ],
            },
        ],
        "qa": [
            {"question": "What are the four Northwind data classification levels?",
             "answer": "Public, Internal, Confidential, and Restricted.",
             "evidence": "Public ... Internal ... Confidential ... Restricted"},
            {"question": "How long are security logs retained?",
             "answer": "13 months.",
             "evidence": "Security logs are retained for 13 months"},
            {"question": "Can Restricted data be sent by email if the attachment is encrypted?",
             "answer": "No. Restricted data may not be emailed under any circumstances, including encrypted attachments.",
             "evidence": "Restricted data may not be emailed under any circumstances, including encrypted attachments"},
            {"question": "How long are customer contract records retained after contract end?",
             "answer": "Seven years.",
             "evidence": "retained for seven years after contract end"},
            {"question": "What happens to support tickets containing customer data after 24 months?",
             "answer": "They are anonymised rather than deleted so analytics remain possible.",
             "evidence": "retained for 24 months and then anonymised rather than deleted"},
        ],
    },
    {
        "id": "SEC-STD-015",
        "title": "Third-Party and Vendor Security Assessment Standard",
        "doc_type": "Standard",
        "category": "Information Security",
        "department": "Information Security",
        "author": "Ravi Chandrasekhar, Chief Information Security Officer",
        "owner": "Information Security",
        "version": "2.0",
        "effective": "2026-06-01",
        "classification": "Internal",
        "review": "Annual",
        "summary": (
            "Sets the risk tiers used to assess Northwind suppliers, the "
            "evidence required at each tier, the approval and re-assessment "
            "cadence, contractual security clauses that must be present, and "
            "the rules for emergency onboarding of an unassessed vendor."
        ),
        "tags": ["third party", "vendor risk", "supply chain", "SOC 2", "due diligence", "TPRM"],
        "sections": [
            {
                "heading": "Risk Tiering",
                "paragraphs": [
                    "Suppliers are tiered by the access they receive, not by "
                    "the size of the contract. A supplier that stores or "
                    "processes Northwind customer data is Tier 1 even if the "
                    "contract is small, while a supplier of office supplies is "
                    "Tier 4 even if the contract is large. Tiering is performed "
                    "by the requester and confirmed by the Third-Party Risk "
                    "team before contracting.",
                    "A supplier may hold several services at different tiers. "
                    "The assessment covers the highest tier of any service "
                    "provided, and a later increase in tier triggers a "
                    "supplementary assessment before the new access is granted."
                ],
                "table": [
                    ["Tier", "Access profile", "Evidence required", "Approval", "Re-assessment"],
                    ["Tier 1", "Processes or stores customer or Restricted data", "SOC 2 Type II or ISO 27001 plus penetration test summary", "CISO and DPO", "Annual"],
                    ["Tier 2", "Integrates with internal systems, no customer data", "SOC 2 Type II or completed SIG Lite", "Security Champion", "Every 2 years"],
                    ["Tier 3", "Named user accounts only, no integration", "Completed security questionnaire", "Department head", "Every 2 years"],
                    ["Tier 4", "No access to systems or data", "None", "Procurement", "On material change"],
                ],
            },
            {
                "heading": "Evidence Review",
                "paragraphs": [
                    "A SOC 2 Type II report is accepted only if the audit "
                    "period covers at least six months, the report is under 12 "
                    "months old, and the scope covers the service Northwind "
                    "will actually use. A report scoped to a different product "
                    "line of the same vendor is not acceptable. Exceptions and "
                    "qualified opinions in the report must be read, not "
                    "skipped, and the reviewer must record how each exception is "
                    "compensated at Northwind.",
                    "Penetration test evidence must show the test date, the "
                    "scope, the tester, and the remediation status of findings. "
                    "A letter of attestation with no findings summary is not "
                    "accepted. Where a Tier 1 supplier cannot provide a "
                    "penetration test, Northwind may commission one at the "
                    "supplier's cost as a condition of onboarding."
                ],
                "bullets": [
                    "SOC 2 Type II must be under 12 months old and cover the used service.",
                    "Penetration tests must be under 12 months and include finding remediation status.",
                    "Sub-processors must be listed and inherit the same tier requirements.",
                    "Evidence gaps are recorded as risks with an owner and a due date, not waived verbally.",
                ],
            },
            {
                "heading": "Mandatory Contract Clauses",
                "paragraphs": [
                    "Tier 1 and Tier 2 contracts must include security clauses "
                    "drafted by Legal: breach notification to Northwind within "
                    "24 hours of the supplier becoming aware, the right to "
                    "audit or to receive audit reports, a data processing "
                    "agreement meeting the DPA template, defined data return and "
                    "destruction obligations on termination, a prohibition on "
                    "sub-processing without notice, and cyber insurance of at "
                    "least 5 million USD.",
                    "Contracts must also name the geographic locations where "
                    "data may be processed and stored. A change of processing "
                    "location requires 30 days' prior notice, which allows "
                    "Northwind to assess transfer mechanisms before data moves."
                ],
            },
            {
                "heading": "Emergency Onboarding",
                "paragraphs": [
                    "A business may onboard an unassessed supplier where a "
                    "documented operational emergency exists and no assessed "
                    "alternative is available. Emergency onboarding grants "
                    "access for 30 days only, is approved by the CISO or "
                    "delegate, and requires compensating controls: no customer "
                    "data, no privileged access, network egress restricted to "
                    "the specific destination, and a named accountable manager.",
                    "Emergency access expires automatically at 30 days and "
                    "cannot be renewed. If the assessment is incomplete at "
                    "expiry, access is revoked until it completes. Repeat "
                    "emergency onboarding for the same supplier in one year "
                    "requires Executive Staff approval."
                ],
                "qa": [
                    {
                        "question": "What tier applies to a supplier that stores customer data?",
                        "answer": "Tier 1, regardless of contract value.",
                    },
                    {
                        "question": "How old can an accepted SOC 2 Type II report be?",
                        "answer": "Under 12 months, with an audit period of at least six months.",
                    },
                    {
                        "question": "How long does emergency vendor access last?",
                        "answer": "30 days, and it cannot be renewed.",
                    },
                ],
            },
            {
                "heading": "Ongoing Monitoring and Offboarding",
                "paragraphs": [
                    "Tier 1 and Tier 2 suppliers are monitored continuously for "
                    "adverse signals: security rating changes, disclosed "
                    "breaches, loss of certification, and ownership change. A "
                    "disclosed supplier breach triggers the Incident Response "
                    "Standard as if it were a Northwind incident until the "
                    "exposure is bounded.",
                    "Offboarding is a controlled process. The accountable "
                    "manager must confirm revocation of all accounts, removal of "
                    "network and integration access, return of Northwind data, "
                    "and written evidence of destruction. An unoffboarded vendor "
                    "with live credentials is one of the most common findings in "
                    "the annual access review."
                ],
            },
        ],
        "qa": [
            {"question": "What vendor tier applies when a supplier stores Northwind customer data?",
             "answer": "Tier 1, regardless of contract size.",
             "evidence": "A supplier that stores or processes Northwind customer data is Tier 1 even if the contract is small"},
            {"question": "Within how many hours must a Tier 1 supplier notify Northwind of a breach?",
             "answer": "Within 24 hours of becoming aware.",
             "evidence": "breach notification to Northwind within 24 hours of the supplier becoming aware"},
            {"question": "How long may emergency unassessed vendor access last?",
             "answer": "30 days, and it cannot be renewed.",
             "evidence": "Emergency onboarding grants access for 30 days only"},
            {"question": "What minimum age and coverage must a SOC 2 Type II audit period have?",
             "answer": "At least six months of audit period, and the report must be under 12 months old.",
             "evidence": "the audit period covers at least six months, the report is under 12 months old"},
            {"question": "What minimum cyber insurance must Tier 1 and Tier 2 contracts require?",
             "answer": "At least 5 million USD.",
             "evidence": "cyber insurance of at least 5 million USD"},
        ],
    },
]
