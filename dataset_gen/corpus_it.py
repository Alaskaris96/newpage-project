"""IT operations, platform and DevOps corpus (5 documents)."""

DOCS = [
    {
        "id": "IT-STD-003",
        "title": "IT Service Management and Incident Priorities Standard",
        "doc_type": "Standard",
        "category": "IT Operations",
        "department": "IT Service Delivery",
        "author": "Tomas Bergqvist, IT Service Delivery Manager",
        "owner": "IT Service Delivery",
        "version": "5.1",
        "effective": "2026-01-10",
        "classification": "Internal",
        "review": "Annual",
        "summary": (
            "Describes the Northwind service desk, the request and incident "
            "workflows, the priority matrix derived from impact and urgency, "
            "response and resolution targets by priority, the change advisory "
            "board cadence, and the escalation ladder for breached targets."
        ),
        "tags": ["ITSM", "service desk", "priority matrix", "SLA", "change management", "escalation"],
        "sections": [
            {
                "heading": "Service Desk Coverage",
                "paragraphs": [
                    "The Northwind service desk is staffed 24 hours, 7 days from "
                    "the Columbus hub, with follow-the-sun coverage from Manila "
                    "and Krakow. The primary intake channel is the Service "
                    "Portal, which creates a ticket automatically. Email to "
                    "servicedesk@northwind.example is also accepted and creates "
                    "a ticket. Telephone intake is reserved for Priority 1 "
                    "incidents and for users who cannot access the portal.",
                    "Every ticket must name the affected user, the affected "
                    "service from the service catalogue, and the business "
                    "impact in the user's own words. Tickets created by "
                    "monitoring are auto-tagged with the alert source so that "
                    "duplicate user reports can be correlated to one incident."
                ],
            },
            {
                "heading": "Priority Matrix",
                "paragraphs": [
                    "Priority is derived from impact and urgency. Impact counts "
                    "the number of affected users or the criticality of the "
                    "service; urgency counts the business consequence of delay. "
                    "The service desk assigns priority at intake and the "
                    "assigned engineer may adjust it once, recording the reason."
                ],
                "table": [
                    ["Impact \\ Urgency", "High", "Medium", "Low"],
                    ["Large (whole site or revenue service)", "P1", "P2", "P3"],
                    ["Medium (team or single service)", "P2", "P3", "P4"],
                    ["Small (single user)", "P3", "P4", "P4"],
                ],
            },
            {
                "heading": "Response and Resolution Targets",
                "paragraphs": [
                    "Response means a qualified engineer has acknowledged and "
                    "begun work. Resolution means the user can resume work, "
                    "which may be through a workaround. A permanent fix is "
                    "tracked as a problem record and does not keep the incident "
                    "open. Targets for P1 and P2 are measured in real time; "
                    "targets for P3 and P4 are measured in business hours."
                ],
                "table": [
                    ["Priority", "Response target", "Resolution target", "Update cadence", "Escalation if breached"],
                    ["P1", "10 minutes", "4 hours", "Every 30 minutes", "IT Director at 1 hour, CIO at 2 hours"],
                    ["P2", "30 minutes", "1 business day", "Every 4 hours", "IT Director at 4 hours"],
                    ["P3", "4 business hours", "5 business days", "Every 2 business days", "Service Manager weekly"],
                    ["P4", "1 business day", "20 business days", "On request", "None"],
                ],
            },
            {
                "heading": "Change Management",
                "paragraphs": [
                    "Changes are normal, standard, or emergency. Standard "
                    "changes are pre-authorised, appear in the Standard Change "
                    "Catalogue, and need no board approval; there are currently "
                    "142 standard changes in the catalogue. Normal changes "
                    "require approval at the Change Advisory Board, which meets "
                    "Tuesday and Thursday at 14:00 Eastern. Emergency changes "
                    "require the Emergency Advisory Board, which is three named "
                    "people who can be convened within 30 minutes.",
                    "Every change record must include the implementation plan, "
                    "the test evidence, the rollback plan with a rollback "
                    "decision point, and the named approver. Changes without a "
                    "tested rollback plan are rejected at the board. The change "
                    "freeze window runs from 20 December to 2 January and "
                    "through the last five business days of each quarter."
                ],
                "bullets": [
                    "Standard changes: pre-authorised, catalogue listed, no board.",
                    "Normal changes: CAB approval Tuesday and Thursday 14:00 Eastern.",
                    "Emergency changes: three-person EAB, convenable in 30 minutes.",
                    "Freeze: 20 December to 2 January, plus last five business days of each quarter.",
                ],
            },
            {
                "heading": "Problem Management",
                "paragraphs": [
                    "A problem record is opened when three or more incidents "
                    "share a root cause, or when a single P1 or P2 incident "
                    "closes without an identified cause. Problem records are "
                    "owned by the service's technical owner, not by the service "
                    "desk. A known error record is published once a workaround "
                    "is validated, and the service desk must offer the "
                    "workaround before investigating from scratch.",
                    "Monthly, the Service Manager reviews the top ten problems "
                    "by incident volume and by downtime minutes. Any problem "
                    "open longer than 90 days without a plan is escalated to "
                    "the IT Director."
                ],
                "qa": [
                    {
                        "question": "What is the P1 resolution target?",
                        "answer": "Four hours, with acknowledgement inside 10 minutes and updates every 30 minutes.",
                    },
                    {
                        "question": "When does the change freeze apply?",
                        "answer": "20 December to 2 January, and the last five business days of each quarter.",
                    },
                    {
                        "question": "When must a problem record be opened?",
                        "answer": "When three or more incidents share a root cause, or when a P1 or P2 closes without an identified cause.",
                    },
                ],
            },
        ],
        "qa": [
            {"question": "What is the response target for a P1 IT incident?",
             "answer": "10 minutes.",
             "evidence": "P1 | 10 minutes | 4 hours"},
            {"question": "When does the quarterly change freeze occur?",
             "answer": "20 December to 2 January, plus the last five business days of each quarter.",
             "evidence": "The change freeze window runs from 20 December to 2 January and through the last five business days of each quarter"},
            {"question": "How many standard changes are in the Northwind catalogue?",
             "answer": "142.",
             "evidence": "there are currently 142 standard changes in the catalogue"},
            {"question": "When does the Change Advisory Board meet?",
             "answer": "Tuesday and Thursday at 14:00 Eastern.",
             "evidence": "meets Tuesday and Thursday at 14:00 Eastern"},
            {"question": "At what age is an unresolved problem record escalated to the IT Director?",
             "answer": "90 days without a plan.",
             "evidence": "Any problem open longer than 90 days without a plan is escalated to the IT Director"},
        ],
    },
    {
        "id": "IT-RBK-006",
        "title": "Kubernetes Platform Runbook",
        "doc_type": "Runbook",
        "category": "IT Operations",
        "department": "Platform Engineering",
        "author": "Sofia Marchetti, Staff Platform Engineer",
        "owner": "Platform Engineering",
        "version": "8.3",
        "effective": "2026-06-15",
        "classification": "Internal",
        "review": "Quarterly",
        "summary": (
            "Operational runbook for the Northwind Kubernetes platform, Atlas. "
            "Covers cluster topology, node pools, common incident playbooks "
            "including node NotReady and CrashLoopBackOff, resource quotas, "
            "the ingress and DNS path, and the commands used during a live "
            "investigation."
        ),
        "tags": ["kubernetes", "atlas", "nodes", "pods", "ingress", "runbook", "platform"],
        "sections": [
            {
                "heading": "Platform Overview",
                "paragraphs": [
                    "Atlas is Northwind's Kubernetes platform, running version "
                    "1.31 across three regions: us-east-1, eu-west-1, and "
                    "ap-southeast-1. Each region runs three control plane "
                    "nodes managed by the cloud provider and a set of worker "
                    "node pools. Application teams do not own clusters; they "
                    "own namespaces within a shared cluster and deploy through "
                    "the GitOps repository, which is the only supported path to "
                    "production. Direct kubectl apply against production is "
                    "blocked by admission policy.",
                    "Namespaces follow the pattern team-service-environment. "
                    "Resource quotas are applied per namespace by default at 8 "
                    "CPU and 32 GiB memory for production and 2 CPU and 4 GiB "
                    "for non-production. Teams needing more file a quota "
                    "increase request in the Platform Portal, which has a "
                    "two business day service level."
                ],
                "table": [
                    ["Node pool", "Instance type", "Min", "Max", "Purpose"],
                    ["general", "m6i.xlarge", "6", "40", "Default application workloads"],
                    ["memory-optimised", "r6i.2xlarge", "2", "16", "Cache and in-memory stores"],
                    ["spot-batch", "m6i.2xlarge spot", "0", "60", "Batch and CI runners"],
                    ["gpu", "g5.xlarge", "0", "8", "Inference workloads"],
                ],
            },
            {
                "heading": "Playbook: Node NotReady",
                "paragraphs": [
                    "A node reports NotReady when the kubelet stops sending "
                    "heartbeats. Start by confirming the node name and the time "
                    "the condition first appeared, then check whether the node "
                    "is reachable at all. If the node responds to SSH, inspect "
                    "the kubelet and container runtime logs; if it does not "
                    "respond, the fault is at the infrastructure layer and the "
                    "cloud provider console will usually show an impaired "
                    "instance status.",
                    "The most common causes, in observed order, are disk "
                    "pressure on the ephemeral volume, a container runtime "
                    "hang, a failed node upgrade, and cloud provider "
                    "maintenance. Disk pressure is fixed by draining and "
                    "replacing the node. Never cordon a node without first "
                    "confirming that the pool has enough capacity to absorb the "
                    "evicted pods, because the cluster autoscaler needs two to "
                    "four minutes to add a replacement."
                ],
                "steps": [
                    "Confirm scope: kubectl get nodes -o wide and note the age of the NotReady condition.",
                    "Check instance status in the cloud console for impaired system or network reachability.",
                    "If reachable, inspect kubelet logs: journalctl -u kubelet --since '-30 min'.",
                    "Check for disk or memory pressure conditions on the node.",
                    "Cordon the node: kubectl cordon <node>, then drain with kubectl drain <node> --ignore-daemonsets --delete-emptydir-data.",
                    "Replace the node through the node group rather than deleting the instance manually.",
                    "Confirm the pods rescheduled and that the service recovered, then record the timeline in the incident ticket.",
                ],
            },
            {
                "heading": "Playbook: CrashLoopBackOff",
                "paragraphs": [
                    "CrashLoopBackOff means the container exits and Kubernetes "
                    "is applying exponential backoff, capped at five minutes. "
                    "The overwhelming majority of cases are one of four things: "
                    "a failed liveness probe, a missing or misconfigured "
                    "environment variable, a dependency that is unreachable at "
                    "startup, or an out-of-memory kill.",
                    "Read the previous container's logs, because the current "
                    "container may not have started yet. Check the exit code: "
                    "137 means the container was killed, usually by the OOM "
                    "killer, and 1 means the application exited on its own "
                    "error path. An exit code of 126 or 127 indicates the "
                    "entrypoint or command is wrong, which typically appears "
                    "immediately after an image change."
                ],
                "steps": [
                    "kubectl describe pod <pod> and read Last State, Reason, and Exit Code.",
                    "kubectl logs <pod> --previous to see why the last attempt died.",
                    "For exit code 137, compare limits.memory against actual usage and check for a recent change.",
                    "For exit code 1, verify configuration and secrets mounted into the pod.",
                    "For exit codes 126 or 127, inspect the image entrypoint and recent Dockerfile changes.",
                    "Confirm the fix in a non-production namespace before promoting.",
                ],
                "notes": [
                    "Do not raise memory limits to silence an OOM kill without "
                    "checking for a leak. Three Northwind incidents in the last "
                    "year were masked by a limit increase and later returned as "
                    "a P1."
                ],
            },
            {
                "heading": "Ingress and DNS Path",
                "paragraphs": [
                    "External traffic reaches a service through Cloudflare, "
                    "then the internal load balancer, then the ingress "
                    "controller in the platform namespace, then the service. "
                    "TLS terminates at Cloudflare for edge caching and again at "
                    "the ingress controller for cluster-internal routing, so a "
                    "certificate problem can exist at either hop. Certificates "
                    "at the ingress are managed by cert-manager and renew "
                    "automatically 30 days before expiry.",
                    "A 502 from the edge usually means the ingress cannot reach "
                    "a ready pod, so check endpoints before checking "
                    "application logs. A 503 with a retry-after header usually "
                    "means the pod is alive but its readiness probe is failing. "
                    "Internal service discovery uses cluster DNS; a stale "
                    "record after a deploy is almost always a readiness probe "
                    "that passes too early."
                ],
                "table": [
                    ["Symptom", "Most likely cause", "First check"],
                    ["502 from edge", "No ready endpoints behind the service", "kubectl get endpoints <svc>"],
                    ["503 with retry-after", "Readiness probe failing", "kubectl describe pod and probe config"],
                    ["504 gateway timeout", "Application slower than the 30s ingress timeout", "Ingress timeout annotation and p99 latency"],
                    ["TLS handshake failure", "Expired cert at ingress or Cloudflare", "cert-manager Certificate status"],
                ],
            },
            {
                "heading": "Escalation and Contacts",
                "paragraphs": [
                    "Platform on-call rotates weekly and is reachable through "
                    "the PagerDuty service Atlas Primary. The first escalation "
                    "is the Platform staff engineer on second call, the second "
                    "is the Platform Engineering Manager, and the third is the "
                    "Director of Engineering. For anything suspected to be a "
                    "security incident, engage Security Operations in parallel "
                    "rather than escalating within Platform first.",
                    "Cluster upgrades run on the second Tuesday of each month "
                    "at 09:00 Eastern, region by region, with a 24 hour soak "
                    "between regions. Rollback of a control plane is not "
                    "supported; a bad upgrade is remediated forward, which is "
                    "why the soak period is mandatory and may not be shortened "
                    "to meet a deadline."
                ],
                "qa": [
                    {
                        "question": "What does exit code 137 indicate in a pod?",
                        "answer": "The container was killed, usually by the OOM killer.",
                    },
                    {
                    "question": "What is the default production namespace quota?",
                        "answer": "8 CPU and 32 GiB memory.",
                    },
                    {
                        "question": "When do Atlas cluster upgrades run?",
                        "answer": "The second Tuesday of each month at 09:00 Eastern, region by region with a 24 hour soak.",
                    },
                ],
            },
        ],
        "qa": [
            {"question": "What Kubernetes version does the Atlas platform run?",
             "answer": "Version 1.31.",
             "evidence": "running version 1.31 across three regions"},
            {"question": "What does pod exit code 137 usually mean?",
             "answer": "The container was killed, usually by the OOM killer.",
             "evidence": "137 means the container was killed, usually by the OOM killer"},
            {"question": "What is the default production resource quota per namespace on Atlas?",
             "answer": "8 CPU and 32 GiB memory.",
             "evidence": "8 CPU and 32 GiB memory for production and 2 CPU and 4 GiB for non-production"},
            {"question": "How long is the soak period between Atlas region upgrades?",
             "answer": "24 hours, and it may not be shortened.",
             "evidence": "with a 24 hour soak between regions"},
            {"question": "Where does a 502 from the edge usually originate?",
             "answer": "The ingress cannot reach a ready pod, so endpoints should be checked first.",
             "evidence": "A 502 from the edge usually means the ingress cannot reach a ready pod"},
        ],
    },
    {
        "id": "IT-STD-014",
        "title": "Backup and Disaster Recovery Standard",
        "doc_type": "Standard",
        "category": "IT Operations",
        "department": "Infrastructure",
        "author": "Grace Adeyemi, Infrastructure Architect",
        "owner": "Infrastructure",
        "version": "4.0",
        "effective": "2026-04-15",
        "classification": "Internal",
        "review": "Annual",
        "summary": (
            "Defines the recovery objective tiers applied to Northwind services, "
            "the backup schedules and retention per tier, encryption and "
            "immutability requirements, the quarterly restore test obligation, "
            "and the annual disaster recovery exercise format."
        ),
        "tags": ["backup", "disaster recovery", "RPO", "RTO", "restore test", "immutability"],
        "sections": [
            {
                "heading": "Recovery Objective Tiers",
                "paragraphs": [
                    "Every production service is assigned a recovery tier by "
                    "its service owner during service onboarding, and the tier "
                    "is recorded in the service catalogue. Tier assignment is a "
                    "business decision about acceptable loss and downtime, not "
                    "an engineering convenience, and must be signed off by the "
                    "service's business owner. Untiered services default to "
                    "Tier 3.",
                    "The recovery point objective is the maximum acceptable "
                    "data loss measured in time. The recovery time objective is "
                    "the maximum acceptable downtime measured from declaration "
                    "to restored service. Both are measured on a real restore, "
                    "not on a theoretical capability."
                ],
                "table": [
                    ["Tier", "RPO", "RTO", "Backup frequency", "Retention", "Example services"],
                    ["Tier 1", "15 minutes", "2 hours", "Continuous replication plus hourly snapshot", "35 days plus 12 monthly", "Payments, customer identity, order management"],
                    ["Tier 2", "4 hours", "8 hours", "Every 4 hours", "30 days plus 6 monthly", "Reporting warehouse, CRM"],
                    ["Tier 3", "24 hours", "3 business days", "Nightly", "30 days", "Internal wikis, non-critical tooling"],
                    ["Tier 4", "Best effort", "5 business days", "Weekly", "90 days", "Development and sandbox environments"],
                ],
            },
            {
                "heading": "Backup Requirements",
                "paragraphs": [
                    "Backups must be encrypted with a key held separately from "
                    "the backup data, must be copied to a second region within "
                    "one hour of creation, and must be immutable for Tier 1 and "
                    "Tier 2 for the full retention period using object lock in "
                    "compliance mode. Immutability in governance mode is not "
                    "sufficient because a privileged account can revoke it.",
                    "Backup jobs are monitored as first-class services. A "
                    "failed Tier 1 backup is a P2 incident raised automatically "
                    "and must be remediated before the next scheduled run. "
                    "Three consecutive failed Tier 1 backups is a P1. Backups "
                    "must never be writable by the production identity; the "
                    "backup vault is accessed only by the dedicated backup "
                    "service principal."
                ],
                "bullets": [
                    "Encryption keys stored separately from backup data.",
                    "Cross-region copy within one hour of backup creation.",
                    "Object lock in compliance mode for Tier 1 and Tier 2.",
                    "Failed Tier 1 backup raises P2 automatically; three consecutive failures raise P1.",
                ],
            },
            {
                "heading": "Restore Testing",
                "paragraphs": [
                    "A backup that has never been restored is not a backup. "
                    "Tier 1 services must have a full restore tested every "
                    "quarter and a point-in-time restore tested every month. "
                    "Tier 2 is tested every six months and Tier 3 annually. "
                    "Tests are run into an isolated account, never into "
                    "production, and must validate row counts and application "
                    "level referential integrity rather than only that the "
                    "database starts.",
                    "Each test produces a restore record containing the source "
                    "backup identifier, the restore duration against the RTO, "
                    "the data loss against the RPO, and any defects found. A "
                    "test that exceeds the RTO is a failed test even if the "
                    "restore eventually completes, and creates a remediation "
                    "item owned by the service owner."
                ],
                "notes": [
                    "Ransomware note: the last known-good immutable snapshot is "
                    "identified by the Security Operations Center, not by the "
                    "service team, during a ransomware event, because the "
                    "attacker's dwell time determines which snapshot is safe."
                ],
            },
            {
                "heading": "Annual Disaster Recovery Exercise",
                "paragraphs": [
                    "Northwind runs one full disaster recovery exercise each "
                    "year in October, alternating between a tabletop and a live "
                    "failover. A live exercise fails over all Tier 1 services to "
                    "the secondary region for a minimum of four hours of real "
                    "traffic. The exercise is announced to customers 10 business "
                    "days in advance and is scheduled outside quarter end and "
                    "outside the peak season for the affected business.",
                    "The exercise is scored against four criteria: whether the "
                    "declaration and communication ran on script, whether every "
                    "Tier 1 service met its RTO, whether data loss stayed within "
                    "RPO, and whether failback completed within the planned "
                    "window. Failures create remediation items that must close "
                    "before the next exercise."
                ],
                "qa": [
                    {
                        "question": "What RPO and RTO apply to Tier 1 services?",
                        "answer": "A 15 minute RPO and a 2 hour RTO.",
                    },
                    {
                        "question": "How often must Tier 1 services be restore tested?",
                        "answer": "A full restore quarterly and a point-in-time restore monthly.",
                    },
                    {
                        "question": "When does the annual DR exercise take place?",
                        "answer": "In October, alternating between a tabletop and a live failover.",
                    },
                ],
            },
        ],
        "qa": [
            {"question": "What are the RPO and RTO for Tier 1 services?",
             "answer": "15 minute RPO and 2 hour RTO.",
             "evidence": "Tier 1 | 15 minutes | 2 hours"},
            {"question": "How often must Tier 1 services undergo a full restore test?",
             "answer": "Every quarter, with a monthly point-in-time restore test.",
             "evidence": "Tier 1 services must have a full restore tested every quarter and a point-in-time restore tested every month"},
            {"question": "What object lock mode is required for Tier 1 and Tier 2 backups?",
             "answer": "Compliance mode; governance mode is not sufficient.",
             "evidence": "immutable for Tier 1 and Tier 2 for the full retention period using object lock in compliance mode"},
            {"question": "How many consecutive failed Tier 1 backups trigger a P1?",
             "answer": "Three consecutive failures.",
             "evidence": "Three consecutive failed Tier 1 backups is a P1"},
            {"question": "How much real traffic must a live DR failover carry?",
             "answer": "A minimum of four hours of real traffic for all Tier 1 services.",
             "evidence": "fails over all Tier 1 services to the secondary region for a minimum of four hours of real traffic"},
        ],
    },
    {
        "id": "IT-HBK-018",
        "title": "Endpoint Device Management Handbook",
        "doc_type": "Handbook",
        "category": "IT Operations",
        "department": "End User Computing",
        "author": "Kevin Nowak, End User Computing Lead",
        "owner": "End User Computing",
        "version": "3.7",
        "effective": "2026-05-20",
        "classification": "Internal",
        "review": "Annual",
        "summary": (
            "Covers the Northwind managed device estate: standard build, "
            "operating system support windows, patch and reboot policy, "
            "software deployment rings, self-service options, lost device "
            "handling, and the process for requesting non-standard hardware."
        ),
        "tags": ["endpoint", "MDM", "patching", "Intune", "laptop", "device lifecycle"],
        "sections": [
            {
                "heading": "Standard Build",
                "paragraphs": [
                    "The standard Northwind build is Windows 11 Enterprise 24H2 "
                    "on a Dell Latitude 7450 or Lenovo ThinkPad T14s Gen 6 for "
                    "the majority of roles, with Apple MacBook Pro 14 inch M4 "
                    "for engineering and design roles that request it. All "
                    "devices are enrolled in Microsoft Intune on first boot "
                    "through autopilot or automated device enrolment, and an "
                    "unmanaged device cannot obtain a Northwind certificate.",
                    "The standard build includes full-disk encryption, "
                    "endpoint detection and response, the password vault, the "
                    "VPN profile, the print and scanner drivers, and the "
                    "approved application set. Devices are refreshed on a "
                    "42-month cycle for laptops and 48 months for desktops."
                ],
                "table": [
                    ["Role group", "Standard device", "Refresh cycle", "Monitor entitlement"],
                    ["General staff", "Dell Latitude 7450", "42 months", "One 27 inch monitor"],
                    ["Engineering", "MacBook Pro 14 M4 or Latitude 7450", "36 months", "Two 27 inch monitors"],
                    ["Design", "MacBook Pro 14 M4", "36 months", "Two colour-calibrated monitors"],
                    ["Executive", "Latitude 7450 or MacBook Pro", "30 months", "Two 32 inch monitors"],
                ],
            },
            {
                "heading": "Patch and Reboot Policy",
                "paragraphs": [
                    "Security patches are deployed in four rings. Ring 1 is the "
                    "IT pilot group and receives patches on release day. Ring 2 "
                    "is the wider IT population at day 2. Ring 3 is all "
                    "voluntary users at day 4. Ring 4 is mandatory enforcement "
                    "at day 7, after which the device cannot reach internal "
                    "network resources until patched and rebooted.",
                    "Reboots are required within 24 hours of a mandatory patch "
                    "and are scheduled to avoid the user's calendar. Active "
                    "Hours are read from the user's Outlook calendar and are "
                    "never overridden. A device that has not rebooted for 14 "
                    "days is flagged in the compliance report and its owner "
                    "receives a reminder from the service desk."
                ],
                "bullets": [
                    "Ring 1 day 0, Ring 2 day 2, Ring 3 day 4, Ring 4 mandatory day 7.",
                    "Unpatched devices lose internal network access at day 7.",
                    "Reboot required within 24 hours of a mandatory patch.",
                    "Out-of-band emergency patches deploy to all rings within 6 hours.",
                ],
            },
            {
                "heading": "Self-Service and Software Requests",
                "paragraphs": [
                    "The Company Portal offers 380 approved applications for "
                    "self-service install with no approval needed. Applications "
                    "outside the portal require a software request ticket, which "
                    "is assessed for licence cost, security risk, and "
                    "duplication against existing tools. The service level is "
                    "five business days, and requests that duplicate an existing "
                    "approved tool are rejected with a pointer to the "
                    "alternative.",
                    "Local administrator rights are not granted by default. "
                    "Developers who need them apply for elevated rights, which "
                    "are granted for 180 days, require manager approval, are "
                    "logged, and are revoked automatically at expiry unless "
                    "renewed. Just-in-time elevation through the approved tool "
                    "is preferred and grants rights for eight hours with a "
                    "mandatory reason."
                ],
            },
            {
                "heading": "Lost, Stolen, or Damaged Devices",
                "paragraphs": [
                    "Report a lost or stolen device to the service desk and the "
                    "Security Operations Center within four hours. The SOC "
                    "issues a remote lock immediately and a remote wipe once the "
                    "device is confirmed missing. Because all data is encrypted "
                    "and cached credentials are limited, a lost device that is "
                    "reported on time rarely becomes a notifiable breach.",
                    "Damage within the first 12 months is repaired at "
                    "Northwind's cost. Damage after 12 months caused by "
                    "negligence may be charged to the requesting department's "
                    "cost centre. A loaner device is issued within one business "
                    "day, and data is migrated from the cloud profile rather "
                    "than from the damaged device."
                ],
                "qa": [
                    {
                        "question": "When does an unpatched device lose network access?",
                        "answer": "At day 7, when Ring 4 enforcement applies.",
                    },
                    {
                        "question": "How long do granted local administrator rights last?",
                        "answer": "180 days, revoked automatically at expiry unless renewed.",
                    },
                    {
                        "question": "How quickly must a lost device be reported?",
                        "answer": "Within four hours, to the service desk and the Security Operations Center.",
                    },
                ],
            },
        ],
        "qa": [
            {"question": "What is the laptop refresh cycle for engineering roles?",
             "answer": "36 months.",
             "evidence": "Engineering | MacBook Pro 14 M4 or Latitude 7450 | 36 months"},
            {"question": "At which patch ring does a device lose internal network access if unpatched?",
             "answer": "Ring 4, at day 7.",
             "evidence": "Ring 4 is mandatory enforcement at day 7, after which the device cannot reach internal network resources"},
            {"question": "How many applications are available for self-service install?",
             "answer": "380 approved applications in the Company Portal.",
             "evidence": "The Company Portal offers 380 approved applications"},
            {"question": "How long are granted local administrator rights valid?",
             "answer": "180 days, with automatic revocation at expiry.",
             "evidence": "granted for 180 days, require manager approval, are logged, and are revoked automatically at expiry"},
            {"question": "What is the standard device for general staff at Northwind?",
             "answer": "A Dell Latitude 7450 running Windows 11 Enterprise 24H2.",
             "evidence": "Windows 11 Enterprise 24H2 on a Dell Latitude 7450"},
        ],
    },
    {
        "id": "IT-STD-021",
        "title": "Identity and Access Management Standard",
        "doc_type": "Standard",
        "category": "IT Operations",
        "department": "Identity and Access Management",
        "author": "Nadia Haddad, IAM Program Manager",
        "owner": "Identity and Access Management",
        "version": "6.2",
        "effective": "2026-07-01",
        "classification": "Internal",
        "review": "Annual",
        "summary": (
            "Defines identity lifecycle from joiner to leaver, role-based "
            "access bundles, privileged access management rules, the quarterly "
            "access review obligation, single sign-on requirements, and the "
            "handling of orphaned and shared accounts."
        ),
        "tags": ["IAM", "RBAC", "joiner mover leaver", "privileged access", "access review", "SSO"],
        "sections": [
            {
                "heading": "Identity Lifecycle",
                "paragraphs": [
                    "Identities are created from the requisition system, never "
                    "manually. A start date creates the identity at 00:01 on "
                    "the first working day, applies the role bundle for the "
                    "hired role, and sends credentials to the manager for "
                    "handover. Contractor identities are created with an "
                    "explicit end date and expire automatically; there is no "
                    "manual extension path, only a new request.",
                    "A mover, meaning a role change or a manager change, "
                    "triggers a recalculation of bundles. The old bundle is "
                    "removed after a 14 day transition window so the employee "
                    "can hand over work, and the new bundle is applied "
                    "immediately. A leaver's accounts are disabled at the "
                    "termination timestamp, which for involuntary exits is set "
                    "by HR in coordination with Security before the meeting."
                ],
                "table": [
                    ["Event", "Action", "Timing", "Owner"],
                    ["Joiner", "Create identity, apply role bundle", "00:01 on day 1", "Automated from requisition"],
                    ["Contractor start", "Create identity with end date", "00:01 on day 1", "Sponsoring manager"],
                    ["Mover", "Apply new bundle, remove old after 14 days", "Effective date", "Automated from HR system"],
                    ["Voluntary leaver", "Disable at termination timestamp", "End of last working day", "Automated"],
                    ["Involuntary leaver", "Immediate disable", "Before exit meeting", "HR with Security"],
                ],
            },
            {
                "heading": "Role-Based Access",
                "paragraphs": [
                    "Access is granted through bundles, never as individual "
                    "entitlements, because individual grants cannot be reviewed "
                    "meaningfully. There are 214 bundles covering the standard "
                    "roles, each owned by a named business owner and a named "
                    "technical owner. A request for access outside the role's "
                    "bundles requires a business justification and expires "
                    "after 90 days unless marked as permanent, which requires "
                    "the bundle owner's approval.",
                    "Segregation of duties rules block toxic combinations. The "
                    "current rule set contains 38 conflicts, the most important "
                    "being that no identity may hold both payment initiation "
                    "and payment approval, and no identity may hold both source "
                    "code write access and production deployment approval for "
                    "the same service."
                ],
                "bullets": [
                    "214 role bundles, each with a business and a technical owner.",
                    "Ad hoc grants expire after 90 days.",
                    "38 segregation of duties conflicts enforced at request time.",
                    "Contractor identities cannot hold privileged bundles.",
                ],
            },
            {
                "heading": "Privileged Access Management",
                "paragraphs": [
                    "Privileged access is never standing. Production "
                    "administrator rights are requested through the privileged "
                    "access portal, approved by the service owner, and granted "
                    "for a maximum of four hours with a mandatory ticket "
                    "reference. Sessions are recorded and the recordings are "
                    "retained for 13 months. Break-glass credentials bypass "
                    "approval but generate an immediate alert and require a "
                    "retrospective ticket within 24 hours.",
                    "The number of identities holding production administrator "
                    "rights is a reported metric and is capped at 3 percent of "
                    "engineering headcount. Standing access exists only for the "
                    "three named platform engineers who operate the identity "
                    "system itself, and their accounts are monitored by a "
                    "second-person rule."
                ],
            },
            {
                "heading": "Access Reviews",
                "paragraphs": [
                    "Access reviews run quarterly. Bundle owners certify every "
                    "member of every bundle they own, and application owners "
                    "certify local administrators and service accounts. "
                    "Reviewers who do not respond within the 15 day window have "
                    "their own access removed, which reliably improves response "
                    "rates. Certifying a reviewer may not certify their own "
                    "access.",
                    "Orphaned accounts, meaning accounts with no identifiable "
                    "owner, are disabled within 5 business days of discovery. "
                    "Shared and generic accounts are prohibited except for "
                    "service accounts, which must be non-interactive, "
                    "credential-vaulted, and owned by a team rather than a "
                    "person."
                ],
                "qa": [
                    {
                        "question": "How long may production administrator access be granted for?",
                        "answer": "A maximum of four hours, with a mandatory ticket reference.",
                    },
                    {
                        "question": "What happens to a reviewer who ignores an access review?",
                        "answer": "Their own access is removed at the end of the 15 day window.",
                    },
                    {
                        "question": "When does a contractor identity expire?",
                        "answer": "Automatically at its explicit end date; extensions require a new request.",
                    },
                ],
            },
        ],
        "qa": [
            {"question": "What is the maximum duration of a production administrator access grant?",
             "answer": "Four hours.",
             "evidence": "granted for a maximum of four hours with a mandatory ticket reference"},
            {"question": "How many role bundles exist in the Northwind IAM model?",
             "answer": "214 bundles.",
             "evidence": "There are 214 bundles covering the standard roles"},
            {"question": "How long do ad hoc access grants last before expiring?",
             "answer": "90 days, unless marked permanent with bundle owner approval.",
             "evidence": "expires after 90 days unless marked as permanent"},
            {"question": "What is the cap on identities holding production administrator rights?",
             "answer": "3 percent of engineering headcount.",
             "evidence": "capped at 3 percent of engineering headcount"},
            {"question": "What happens to reviewers who do not complete a quarterly access review?",
             "answer": "Their own access is removed at the end of the 15 day window.",
             "evidence": "Reviewers who do not respond within the 15 day window have their own access removed"},
        ],
    },
]
