# Artisyn Platform — Challenges, Solutions & Use Cases

**Date:** 2026-03-23
**Purpose:** Explain what challenges the Artisyn platform (AILA SDK + Artisyn Cloud Runtime) solves, how the factory/SDK model works, and what use cases it enables.
**Audience:** Engineers, managers, sales, business stakeholders

---

## The Problem: Why Best Practices Fail at Scale

Every organization knows what good looks like. The challenge is making it happen consistently, across teams, across projects, across time.

### Challenges in Agentic Development Today

| Challenge | Description | Impact |
|---|---|---|
| **Knowledge fragmentation** | Best practices exist in wikis, Confluence, Slack threads, people's heads — never in one place | Every new project starts from scratch; knowledge walks out the door when people leave |
| **Inconsistent application** | Even when best practices are documented, each team applies them differently | Code quality varies; onboarding takes weeks; reviews catch the same issues repeatedly |
| **Configuration drift** | Agent configs, steering files, MCP settings diverge across projects and developers | "Works on my machine" for AI agents; new team members get broken setups |
| **No sharing mechanism** | Skills, prompts, agents created by one team are invisible to others | Duplicate effort; 5 teams build the same Jira integration independently |
| **Local-only knowledge** | Kiro and Claude Code keep everything on the developer's machine | PMs, DMs, stakeholders can't access agent capabilities; no organizational learning |
| **No quality feedback loop** | Skills are created and used, but never systematically improved | Same mistakes repeated; no mechanism to capture what worked and what didn't |
| **Manual setup** | Every new project requires manual configuration of agents, steering, MCP, skills | Hours of setup per project; error-prone; inconsistent results |
| **Tool lock-in** | Skills created in Kiro don't work in Claude Code and vice versa | Teams on different tools can't share work; migration is painful |
| **No governance** | Anyone can create any agent with any tools — no visibility into what's running | Security risks; no audit trail; no way to enforce organizational standards |
| **Scaling knowledge** | One expert's knowledge helps one team; no way to multiply it across the organization | Bottleneck on senior people; juniors learn slowly; organizational expertise doesn't compound |

---

## How the Platform Solves These Challenges

### Layer 1: AILA SDK — The Factory

The SDK is the cross-runtime layer that turns best practices into typed, validated, shareable configuration.

| Challenge | SDK Solution |
|---|---|
| **Knowledge fragmentation** | Agentic Catalog — universal discovery system cataloging skills, agents, knowledge, prompts, workspaces, data sources, workshops, PIRs, best practices across all providers. 15 resource types, single API. |
| **Inconsistent application** | Typed workspace definitions (`KiroWorkspace` Pydantic models) — configuration is validated, not just documented. Generation enforces conventions; validation catches errors before deployment. |
| **Configuration drift** | `workspace.py` is the single source of truth. `generate` produces identical files for every developer. `validate` catches broken references. Idempotent — safe to run repeatedly. |
| **No sharing mechanism** | Multi-provider catalog: local filesystem + AWS S3/DynamoDB + API gateway + Git repos. `aila_list_skills()` discovers 89+ skills across all providers. `aila_get_resource()` reads any resource by type and name. |
| **Manual setup** | Workspace bootstrap: `python3 workspace.py generate` creates all agents, steering, skills, MCP settings, README, selftest, and bootstrap docs in seconds. New team members bootstrap in <5 minutes. |
| **Tool lock-in** | `CatalogConverter` transforms workspace definitions between formats. Same `workspace.py` generates `.kiro/` for Kiro, `.claude/` for Claude Code (planned), and `AGENT.json`/`WORKSPACE.json` for cloud. Skills follow the open Agent Skills standard (agentskills.io). |
| **Scaling knowledge** | DataArt shared skills (60+ today) encoding delivery expertise (PMBOK, Scrum, SAFe, RAIN, DevOps, data engineering); extensible with external skills from any provider. Skills are catalog resources — create once, use everywhere. |

**What the SDK provides today:**

| Component | What It Does |
|---|---|
| `aila-catalog-schema` | Types: `KiroWorkspace`, `KiroAgent`, `KiroSettings`, `CatalogConverter`, `AgenticContext`, `CatalogResourceReference` — Pydantic models with validation |
| `skill-sdk-aila` | API: 13 public functions (`aila_list_skills`, `aila_get_resource`, `aila_list_resources`, etc.), multi-provider discovery, workspace resolution with parent chain inheritance |
| `skill-library-aila` | Content: DataArt shared skills (60+ today), 19 PIRs, 6 workshops, 15 best practices — ready to use; extensible with external skills |
| `workspace.py` | Pipeline: generate → validate → catalog → publish — deterministic, idempotent, CI/CD friendly |

### Layer 2: Artisyn Cloud Runtime — Enterprise Execution

The cloud runtime is where workspace definitions execute at scale, accessible to both technical and business users.

| Challenge | Cloud Solution |
|---|---|
| **Local-only knowledge** | Enterprise web portal — same workspace context accessible to PMs, DMs, AMs, stakeholders. No CLI or IDE required. |
| **No quality feedback loop** | Self-learning loop: Skill executes → PIR generated → Human reviews → Skill updated. 19 PIRs in production today, each capturing problems, opportunities, and automation candidates. |
| **No governance** | IAM role per agent, Cognito SSO with workspace claims, KMS encryption, VPC isolation, CloudWatch audit trails. Workspace-based authorization — users see only their workspace resources. |
| **Scaling knowledge** | Workspace inheritance: Org standards → Team conventions → Project specifics. Define once at org level, automatically inherited by all child workspaces. |
| **Multi-user access** | Concurrent users via session isolation (DynamoDB). Real-time streaming via AppSync WebSocket. |
| **Production deployment** | AgentCore containers (ECR + IAM + VPC). Same agent definition from local dev runs in production — no translation, no rewriting. |

---

## The Self-Learning Loop

The most unique capability: skills improve through organizational usage.

```
Engineer uses skill (with human review)
         │
         ▼
Skill executes → produces result
         │
         ▼
PIR generated automatically
  • What happened (timeline, decisions, outcomes)
  • What worked (✅) and what didn't (❌)
  • Automation opportunities (💡)
         │
         ▼
Human reviews and approves improvements
         │
         ▼
Skill updated in catalog
         │
         ▼
All teams get improved skill automatically
```

**Skill maturity levels:**

| Level | Description | Human Role |
|---|---|---|
| **Manual** | You do the work. Agent watches and learns from the session. | Full control |
| **Assisted** | You work WITH the agent, step by step. Agent suggests, you decide. | Decision maker |
| **Supervised** | Agent does the work. You review before it takes effect. | Reviewer |
| **Autonomous** | Agent executes independently within guardrails. Human oversight on exceptions. | Oversight |

You cannot skip levels. Start manual, build trust, progressively automate.

**PIRs in production today (19 examples):**

| PIR | Duration | What It Captured |
|---|---|---|
| skills-standardization | 8h | Migrated 10 key system skills; captured migration patterns |
| personal-assistant-automation | 10h | Teams integration + AILA skills; identified automation opportunities |
| steering-mcp-implementation | 4h | Config-based steering; documented 4 bugs fixed |
| infrastructure-recovery | 4h | GitLab runner EC2 recovery; captured recovery playbook |
| knowledge-library-integration | 4h | Centralized code documentation; identified gaps |
| dataset-security-remediation | 4h | Security Hub findings; captured remediation patterns |

---

## Best Practices as Catalog Resources

The platform doesn't just document best practices — it catalogs them as discoverable, searchable resources that agents can apply.

**15 best practices in catalog today:**

| Best Practice | What It Encodes |
|---|---|
| skill-first-problem-solving | Search existing skills before building new ones |
| automation-first | Build the tools that build the tools |
| kiss-principle | Simplest solution that works |
| reuse-over-build | Prefer existing tools over custom |
| bootstrap-first | Build skill creation infrastructure first |
| ai-agent-code-change-process | 6-step structured workflow for code changes |
| skills-vs-agents-vs-prompts | Decision framework: when to use which AILA pattern |
| ai-agent-template-first-configuration | Check templates before generating configs |
| prompt-management | Centralized reusable prompts |
| aila-git-workflow | Git workflow with AI assistance |

**6 workshops for progressive onboarding:**

| Workshop | Level | Duration | What It Teaches |
|---|---|---|---|
| kiro-onboarding | 00 | 1h | Kiro CLI basics, 6 micro labs |
| skills-framework-onboarding | 01 | 4-5h | AILA skills framework |
| aila-sdk-onboarding | 02 | 90min | SDK catalog, agents, skill management |
| sa-agentic-onboarding | 01 | 4-5h | AILA Agentic stack deployment |
| best-practices-management | beginner | 30min | MCP tools for best practices |
| workshop-creation | 000 | varies | Meta: how to create workshops |

---

## From Development Workspaces to Business Workspaces — Same Architecture

### The Stereotype vs Reality

The common stereotype: "There's an agent or group of agents that create business functionality." This implies business applications need a fundamentally different architecture from development tools.

**Reality: Business workspaces follow the exact same rules as development workspaces.**

| Principle | Development Workspace | Business Workspace |
|---|---|---|
| **Steering** | Coding standards, API conventions, testing patterns | PMBOK governance, Scrum framework, SAFe portfolio, billing models |
| **Skills** | SDLC, deployment, troubleshooting, documentation | Risk management, acceptance criteria, sprint execution, stakeholder engagement |
| **Agents** | SDK expert, infrastructure expert, code reviewer | Delivery Manager, Project Manager, Engagement Manager, Jira Analytics |
| **Knowledge** | Code intelligence (`KNOW.md`), architecture docs | Organizational policies, role definitions, process documentation |
| **Context hierarchy** | Org standards → team conventions → project specifics | Org governance → account conventions → project delivery specifics |
| **Subagent orchestration** | Default agent delegates to code experts | DM delegates to PM, PM delegates to Jira Analytics and Code Experts |
| **Self-learning** | PIRs capture development patterns | PIRs capture delivery patterns, process improvements |

The architecture is identical. The content is different. This means:

1. **We don't reinvent** — we convert Kiro/Claude best practices and workspace architecture to business and cloud workspaces
2. **Same SDK** — `workspace.py` defines a DM workspace the same way it defines a code development workspace
3. **Same catalog** — business skills live alongside development skills, discoverable by the same API
4. **Same inheritance** — org-level PMBOK steering inherited by all delivery workspaces automatically
5. **Same validation** — `workspace.py validate` catches broken references in business workspaces too

### System Skills That Enable This

The platform provides fundamental system skills that automate workspace and skill lifecycle — making it a self-service platform:

| System Skill | What It Automates |
|---|---|
| **workspace-management** | End-to-end workspace lifecycle: define in Python → generate local structure → convert to catalog format → publish to cloud. Works for both dev and business workspaces. |
| **skill-management-aila** | Discover, search, create, validate, and migrate skills using catalog tools. Centralized skill write operations across providers. |
| **aila-catalog-sdk** | Complete API reference for all catalog operations — skill discovery, resource management, publishing. The "how to use the platform" skill. |
| **generic-sdlc** | Structured software development lifecycle from idea to implementation. Prompt-Driven Design (PDD) process with knowledge discovery and compliance audit. |
| **business-sdlc** | Business SDLC orchestrator — 10-step PDD process with business dimension focus. Transforms rough project ideas into structured deliverables. |
| **best-practices** | Create and manage best practice documents. Standardized format, catalog integration, organizational sharing. |
| **post-implementation-review** | Generate PIR documents from work sessions. Analyze objectives, actions, issues, automation opportunities. Feeds the self-learning loop. |
| **aila-knowledge-extraction** | Extract, structure, and package knowledge from any source for zero-token agent access. Creates discoverable knowledge artifacts. |
| **knowledge-mining** | Extract structured knowledge from unstructured sources — documents, code, conversations. Identify patterns, issues, opportunities. |
| **steering-assessment** | Discover and configure relevant skills and resources for `.kiro/steering/`. Matches project needs to available catalog resources. |
| **create-repo-expert** | Create read-only expert agents for repositories with code documentation and metadata. One command to make any codebase agent-accessible. |
| **external-skill-integration** | Integrate external skill packages from third-party sources (GitHub, GitLab) into the catalog discovery system. |
| **template-creation-validation** | Create and validate code/config templates from real files. Auto-detect parameters, validate against schemas. |
| **repo-documentation** | Automated code documentation generation with AST-parsed metadata for AI agent understanding. |

These skills are not just for engineers. A PM can use `business-sdlc` to structure a project. A DM can use `post-implementation-review` to capture lessons learned. A new team member can use `steering-assessment` to discover what's available for their project.

### Self-Service Platform

The combination of system skills + catalog + workspace inheritance creates a self-service platform:

```
┌─────────────────────────────────────────────────────────────────┐
│                    SELF-SERVICE CYCLE                             │
│                                                                 │
│   1. DISCOVER — What skills/agents/knowledge exist?             │
│      skill-management-aila, aila-catalog-sdk, steering-assessment│
│                                                                 │
│   2. USE — Apply existing skills to your work                   │
│      generic-sdlc, business-sdlc, knowledge-mining              │
│                                                                 │
│   3. CREATE — Build new skills from your experience             │
│      best-practices, template-creation-validation               │
│                                                                 │
│   4. REVIEW — Capture what worked and what didn't               │
│      post-implementation-review                                 │
│                                                                 │
│   5. SHARE — Publish to catalog for the organization            │
│      workspace-management, skill-management-aila                │
│                                                                 │
│   6. IMPROVE — Skills get better through organizational usage   │
│      Self-learning loop: PIR → review → update → republish      │
│                                                                 │
│   Automated knowledge and artifact sharing across organization  │
└─────────────────────────────────────────────────────────────────┘
```

Every step is supported by a system skill. No manual process required. The platform bootstraps itself — the skills that manage skills are themselves skills in the catalog.

---

## Use Cases

The platform is use-case agnostic — the same workspace/agent/skill architecture applies to any domain. Examples in production or active development:

### 1. Accelerated Code Development

AILA itself is built with AILA — the platform is its own best proof point.

- **17+ agents** coordinating in a single workspace (SDK experts, infrastructure experts, UI experts, domain experts)
- **DataArt shared skills** (60+ today) encoding development patterns (SDLC, deployment, troubleshooting, documentation); extensible with external skills
- **Code intelligence** — AST-extracted `KNOW.md` metadata for every codebase, enabling agents to navigate code without reading every file
- **Workspace inheritance** — org coding standards inherited by all project workspaces automatically

### 2. DevOps Automation

- **Infrastructure agents** — Terraform/Terragrunt experts that understand module patterns, dependency chains, deployment order
- **Deployment skills** — Lambda container deployment, ECR Docker troubleshooting, cross-account CI/CD, GitLab runner operations
- **Data Lake operations** — 30+ agents for data lake management (domain, team, dataset, pipeline, VPC infrastructure)
- **Security remediation** — Security Hub findings analysis and automated remediation

### 3. Business Process Automation

- **Delivery Manager agent** — PMBOK governance, risk management, value delivery, stakeholder engagement (20+ steering docs, 45+ skills)
- **Project Manager agent** — Sprint execution, acceptance criteria, resource planning, metrics definitions (45+ skills, 20+ steering docs)
- **Engagement Manager agent** — RAIN/SAM account planning, relationship assessment, outreach tactics (14 skills, 9 steering docs)
- **Jira Analytics agent** — Extraction, tracking, knowledge mining from project management data

### 4. New Business Functionality Development

- **Underwriting workbench** — Document processing, risk analysis, pricing, quote issuance (PnC insurance domain)
- **Dynamic applications** — Agent-generated Streamlit UIs deployed on demand
- **Workspace-as-code** — Parameterized workspace generation: `create_data_lake_workspace("lake-ops", 3 domains, 2 teams)` produces complete workspace with all agents, steering, skills

### 5. Data Governance Automation

- **Data catalog agents** — Semantic data catalog with business context, not just technical metadata
- **Compliance agents** — Map PII across services to GDPR/CCPA/SOX requirements
- **Data quality agents** — Monitor data pipelines, detect drift, alert on anomalies
- **Data source/catalog/query management** — 3 dedicated resource types in the Agentic Catalog

### 6. Data Lake / Data Ingestion

- **Data Lake infrastructure** — Agents deploy S3, Glue, Lake Formation, DynamoDB, KMS from workspace definitions
- **ETL pipeline agents** — Step Functions, Lambda, SQS, Glue job orchestration
- **Healthcare data** — EMIS XML, FHIR R4, NHS standards processing
- **Insurance data** — PySpark, policy calculations, risk assessment
- **Music industry data** — CWR format parsing, royalty management
- **Open-source stack** — No Snowflake license; Hadoop, PySpark, Glue — AI models understand natively

### 7. Knowledge Management & Organizational Learning

- **Knowledge extraction** — Automated `KNOW.md` generation from any codebase (AST-based metadata extraction)
- **Knowledge mining** — Extract patterns from Jira, Git, Confluence across projects
- **Workshop system** — Progressive onboarding from Level 00 (basics) to Level 02 (advanced)
- **PIR system** — Every skill execution generates a review; improvements feed back into skills
- **Best practices catalog** — 15 codified best practices discoverable by any agent

---

## Uniqueness: What Exists Nowhere Else

Based on comprehensive market analysis (uniqueness score: 9/10 overall):

| Capability | Score | Why It's Unique |
|---|---|---|
| **Agentic Catalog** | 9/10 | Universal discovery across clouds — catalogs skills, agents, knowledge, data, workspaces, PIRs, workshops, models, applications. Existing catalogs (Acceldata, Promethium) are data-only. |
| **Bidirectional knowledge flow** | 10/10 | Agentic insights → human curation → deterministic knowledge → drift detection → feedback. No vendor has this with human governance. |
| **Auto-generated enterprise architecture** | 10/10 | TOGAF views generated from live system analysis, not manual documentation. |
| **Knowledge quality governance** | 10/10 | Human-in-the-loop curation with drift detection. Knowledge doesn't go stale. |
| **Cross-system agentic reasoning** | 9/10 | Synthesize across code + Jira + DB + Confluence simultaneously. Not fragmented search — holistic understanding. |
| **Workspace-as-code** | 9/10 | Typed, validated, parameterized workspace definitions that generate for any runtime. |
| **Three-tier progressive discovery** | 8/10 | Metadata → full metadata → on-demand content. Optimized for LLM context windows. |
| **Infinite extensibility** | 8/10 | `ResourceTypeRegistry` — add new resource types without code changes. |

Closest competitor combination (Acceldata + Arthur + Kong) still misses ~60% of capabilities.

---

## The Factory Model

```
┌─────────────────────────────────────────────────────────────────┐
│                        THE FACTORY                               │
│                                                                 │
│   Kiro Runtime + Claude Runtime + AILA SDK                      │
│                                                                 │
│   Engineers design, prototype, and validate:                    │
│   • Workspaces (typed Python definitions)                       │
│   • Agents (specialized AI configurations)                      │
│   • Skills (portable instruction packages)                      │
│   • Steering (project/org/team conventions)                     │
│   • Knowledge (code intelligence, documentation)                │
│   • Best practices (codified organizational patterns)           │
│                                                                 │
│   Output: Published to Agentic Catalog                          │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│                    AGENTIC CATALOG                               │
│                                                                 │
│   15 resource types · Multi-provider · Cross-cloud              │
│   Skills · Agents · Knowledge · Prompts · Workspaces            │
│   Workshops · PIRs · Best Practices · Data Sources              │
│   Models · Applications · Data Catalogs · Data Queries          │
│                                                                 │
│   Discovery: aila_list_skills(), aila_list_resources()          │
│   Access: aila_get_skill(), aila_get_resource()                 │
│   Search: aila_search_skills(query, category, tags)             │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│                   ARTISYN CLOUD RUNTIME                          │
│                                                                 │
│   Technical Users          Business Users                       │
│   (CLI, API, IDE)          (Web Portal, Catalog UI)             │
│                                                                 │
│   • Execute agents         • Use published workspaces           │
│   • Extend workspaces      • Walk through SDLC processes        │
│   • Debug and iterate      • Assess risks, plan sprints         │
│   • Publish improvements   • Discover via Catalog UI            │
│                                                                 │
│   Self-Learning Loop:                                           │
│   Execute → PIR → Review → Improve → Republish                  │
│                                                                 │
│   AWS ✅ · Azure 🔲 · GCP 🔲                                    │
└─────────────────────────────────────────────────────────────────┘
```

---

## Summary

### Platform Goal

Apply industry and agentic AI best practices to:
- **Create new agentic applications** — business functionality, automation, data processing
- **Support changing ways of working** — IT, engineering, architecture, project management, delivery
- **Accelerate future workspace automation** — each workspace gets better through usage and PIRs

### Approach: Deliver First

The platform operates on a "deliver first" principle:

- **No presentations or talking** — practical implementations, working code, real workspaces
- **Fail fast** — try things, capture what works in PIRs, improve, repeat
- **Platform is not a product** — it's a constantly evolving shared environment
- **Everyone contributes** — engineers, PMs, DMs, architects — it's a joint workspace, not a vendor deliverable
- **Not ideal, not finished** — and that's by design. The self-learning loop means it gets better with every use

### What Matters Now

The platform itself is in working shape. The goal has shifted from building the platform to **producing on top of it**:

- Business functionality and skills
- Delivery automation workspaces
- Domain-specific agent teams
- Knowledge artifacts that compound organizational expertise

### Long-Term Perspective

Over time — years from now — all platforms and tools will converge. Capabilities that are unique today will become commodity. Most components of this platform will eventually be retired as vendor tools catch up. There is no desire to build more platform — we want to support the most optimal flows now.

**What will NOT converge:**
- The number of business applications, agents, and skills an organization has built
- How proven and self-corrected those skills are through real usage and PIRs
- How deep the organizational expertise is captured in agentic form

This is why the platform exists today: **to build and deliver now, without waiting for other platforms to be ready.** It's based on established standards (Agent Skills, MCP, AGENTS.md) and best practices (Kiro, Claude Code) that will evolve — and the platform will evolve with them. But the skills, knowledge, and expertise accumulated in the catalog are permanent organizational assets that transfer to whatever platform comes next.

The competitive advantage is not the tooling — it's the organizational IP that accumulates in the catalog. The tooling is a means — the IP is the asset.
