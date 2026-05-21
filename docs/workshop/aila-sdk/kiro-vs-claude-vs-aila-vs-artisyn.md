# Kiro Runtime vs Claude Runtime vs AILA SDK vs Artisyn Cloud Runtime

**Date:** 2026-03-23
**Purpose:** Show how local development best practices (Kiro, Claude Code) translate seamlessly to cloud runtimes via AILA SDK, and what the Artisyn Cloud Runtime adds for production deployment.
**Positioning:** AILA SDK is the cross-runtime layer. Artisyn Cloud Runtime is where the same workspace definitions execute at enterprise scale.

---

## Core Principle

**Your primary interface is Kiro and Claude. We don't change that.**

Both local runtimes work exactly as designed. AILA SDK adds a layer that defines, generates, validates, and catalogs workspace configuration. The **Artisyn Cloud Runtime** then executes those same workspace definitions in production — same agents, same steering, same skills, same tools — but with enterprise infrastructure (sessions, security, multi-user, streaming).

What Artisyn adds on top of Kiro and Claude:
1. **DataArt shared skills** (60+ skills today) encoding delivery expertise (Anthropic standard) — ready to use, extensible with external skills from any provider
2. **Workspace bootstrap** — auto-bootstrap Kiro/Claude workspace settings with pre-configured defaults and best practices, without manual edits (deterministically)
3. **Skill/agent portability** — create once in Claude or Kiro, use everywhere
4. **Agentic Catalog** — universal discovery across clouds (exists nowhere else)
5. **Advanced code intelligence** — structured metadata extraction that improves accuracy
6. **Multi-cloud execution** — agents run on AWS, Azure, GCP from one catalog
7. **Enterprise workspaces** — same project context available to PMs, DMs, AMs via web portal
8. **Self-learning loop** — skills improve through organizational usage and PIRs
9. **Data platform integration** — enterprise data lake agents natively understand

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                     Technical User (Engineer)                                │
│                                                                             │
│         writes workspace.py (typed KiroWorkspace definition)                │
│         creates skills, agents, steering, prompts                           │
│                                                                             │
└────────────────────────────────┬────────────────────────────────────────────┘
                                 │
                                 ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                        AILA SDK / Type System                               │
│                                                                             │
│   • aila-catalog-schema (types, validation, converter)                      │
│   • skill-sdk-aila (catalog API, providers, workspace resolution)           │
│   • skill-library-aila (60+ shared skills)                                  │
│   • workspace.py generate / validate / catalog / publish                    │
│                                                                             │
└──────┬──────────────────────┬──────────────────────┬────────────────────────┘
       │                      │                      │
       ▼                      ▼                      ▼
┌──────────────┐   ┌──────────────┐   ┌────────────────────────────────┐
│ Kiro Runtime │   │Claude Runtime│   │   Artisyn Cloud Runtime        │
│              │   │              │   │                                │
│.kiro/steering│   │ CLAUDE.md    │   │  AWS: AgentCore + Strands SDK  │
│.kiro/agents/ │   │.claude/agents│   │  Azure: (planned)              │
│.kiro/skills/ │   │.claude/skills│   │  GCP: (planned)                │
│.kiro/settings│   │.claude/      │   │                                │
│              │   │  settings/   │   │  WORKSPACE.json + AGENT.json   │
│ Local dev ✅ │   │ Local dev ✅ │   │  Cloud production ✅           │
└──────────────┘   └──────────────┘   └──────────────┬─────────────────┘
                                                     │
       ┌─────────────────────────────────────────────┘
       │
       ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                  Business User (PM, DM, AM, Stakeholder)                     │
│                                                                             │
│   • Accesses via Artisyn Web Portal — no CLI, no IDE required               │
│   • Uses workspaces, agents, skills created by technical users              │
│   • Can extend: create workspace skills, add steering, configure agents     │
│   • Cannot modify: core workspace definitions, SDK types, infrastructure    │
│                                                                             │
│   Kiro/Claude = Factory (complex skills, workspaces, agents)                │
│   Artisyn Cloud = Runtime (business users consume + extend)                 │
│   Catalog = Shared layer (both technical and business users discover)       │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Feature Comparison: Four Columns

### 1. Project Context

| Aspect | Kiro Runtime | Claude Runtime | AILA SDK | Artisyn Cloud Runtime |
|---|---|---|---|---|
| **Context files** | `.kiro/steering/*.md` | `CLAUDE.md` | Generates both from `workspace.py` | `WORKSPACE.json.default_agent.steering[]` — catalog resource references |
| **Auto-generation** | Manual | `/init` generates starter | `workspace.py generate` | N/A — consumes published workspace |
| **Loading** | Files loaded at session start | CLAUDE.md read at session start | Generates files for local runtimes | `ContextSystemPromptHook` injects steering at every agent invocation |
| **Context management** | `/compact`, `/context show` (usage %), `/context add/remove/clear`, `@path` file refs, knowledge bases | `/compact`, `/clear`, `/btw`, checkpoints, Auto Memory | N/A | Managed by cloud runtime |
| **Inheritance** | Agent > Project > Global (3-scope priority) | Workspace > Global | `parent_workspace` field | `resolve_workspace()` walks parent chain, merges steering parent-first |
| **Validation** | N/A | N/A | `validate()` checks symlinks resolve | Catalog publish validates before upload |
| **Naming** | User-defined | User-defined | `wsg-*` / `wsc-*` / custom | Catalog resource references (provider/skill/path) |

**How it translates to cloud:** Steering files authored locally become `CatalogResourceReference` entries in `WORKSPACE.json`. The `ContextSystemPromptHook` resolves them from S3/DynamoDB at invocation time and appends to `agent._system_prompt_content`. Parent chain inheritance works automatically — root org steering → team steering → project steering, all concatenated.

### 2. Skills

| Aspect | Kiro Runtime | Claude Runtime | AILA SDK | Artisyn Cloud Runtime |
|---|---|---|---|---|
| **Skill format** | `SKILL.md` in `.kiro/skills/` | `SKILL.md` in `.claude/skills/` | Agent Skills standard | Same skills in S3 catalog |
| **Skill sources** | Local filesystem | Local filesystem | Multi-provider (local + AWS + API) | AWS S3/DynamoDB provider |
| **Discovery** | Scan local dirs | Scan local dirs | `aila_list_skills()` across providers | Same SDK API via MCP server or direct |
| **Skill library** | N/A | N/A | `skill-library-aila` — DataArt shared skills (60+ today: SDLC, deployment, PM/DM/EM delivery, PMBOK, Scrum, SAFe, RAIN frameworks); extensible with external skills | Same library accessible from cloud |
| **Activation** | Description match; `/context show` to inspect | Description match; `/skill-name` manual invocation | Description match | Skills listed in `WORKSPACE.json.default_agent.skills[]` |

**How it translates to cloud:** Skills published to catalog are available to cloud agents via the same `skill-sdk-aila` API. The `WORKSPACE.json` lists skills as catalog references; the cloud runtime resolves them on demand.

### 3. Custom Agents

| Aspect | Kiro Runtime | Claude Runtime | AILA SDK | Artisyn Cloud Runtime |
|---|---|---|---|---|
| **Config format** | JSON in `.kiro/agents/` | Markdown in `.claude/agents/` | `KiroAgent` Python objects | `AGENT.json` in catalog (declarative-agent-management skill) |
| **Validation** | Informal | N/A | Pydantic `AgentConfig` with reference resolution | Same Pydantic validation at publish time |
| **Tool mapping** | Kiro tool names | Claude tool names | `CatalogConverter.TOOL_MAP` maps between formats | `TOOLS_CONFIG` registry maps names → Python module paths |
| **Prompt** | `file://` URI to `.md` file | Inline markdown | `prompt_ref()` helper | Prompt inlined into `AGENT.json.system_prompt` by `CatalogConverter` |
| **Subagents** | `use_subagent` (parallel execution, live progress, `availableAgents`/`trustedAgents` access control) | Subagents in `.claude/agents/` (up to 10 parallel, background execution) | `subagents` field in `KiroAgent` | `catalog_execute_agent` / `execute_strands_swarm` tools |
| **Session management** | `/chat resume/save/load`, `--resume-picker`, custom scripts (git/cloud) | `--continue` / `--resume` | N/A | DynamoDB sessions; child: `{parent}__{agent_name}` |
| **Multi-agent teams** | N/A | N/A | `AgentTeam` type | `catalog_execute_team` → Strands swarm with coordinator |

**How it translates to cloud:** `CatalogConverter` transforms `KiroAgent` → `AGENT.json` with tool mapping (`fs_read`→`read_workspace_file`, `use_subagent`→`catalog_execute_agent`, `execute_bash`→dropped). Prompts are inlined. The cloud runtime loads `AGENT.json` from catalog, resolves tools via `TOOLS_CONFIG`, and creates a Strands `Agent` instance.

**Production example:** A working project workspace has 17+ agents coordinating delivery — Delivery Manager delegates to Project Manager, Jira Analytics, and Code Expert agents per service. Multi-agent teams (30+ agents for Data Lake operations) are in production today.

### 4. Hooks / Automation

| Aspect | Kiro Runtime | Claude Runtime | AILA SDK | Artisyn Cloud Runtime |
|---|---|---|---|---|
| **Hook system** | `.kiro/hooks/` | `.claude/settings.json` | Generation/validation pipeline | `ContextSystemPromptHook` (BeforeInvocationEvent) |
| **Trigger** | File save, tool use, etc. | File save, tool use, etc. | `workspace.py generate/validate` | Every agent invocation (automatic) |
| **Purpose** | Automate dev tasks | Automate dev tasks | Validate workspace integrity | Inject workspace context, resolve steering, set org/user context |
| **Hook discovery** | Manual config | Manual config | N/A | Auto-discovery via `pkgutil` on `agentic_sdk.hooks` package |

**How it translates to cloud:** Local hooks are dev-time automation. Cloud hooks are runtime hooks — `ContextSystemPromptHook` fires before every agent invocation to inject workspace steering, context hierarchy, and catalog resources. This is the cloud equivalent of Kiro loading `.kiro/steering/` at session start.

### 5. MCP Servers

| Aspect | Kiro Runtime | Claude Runtime | AILA SDK | Artisyn Cloud Runtime |
|---|---|---|---|---|
| **Configuration** | `.kiro/settings/mcp.json` | `claude mcp add` | `KiroMcpServer` typed objects | AgentCore runtimes with SigV4 auth |
| **Protocol** | stdio / HTTP (with OAuth) | stdio / SSE / HTTP | Generates `mcp.json` | Streamable HTTP with IAM per-agent |
| **Security** | Local process | Local process + sandbox | Type validation | IAM roles, KMS encryption, VPC isolation |
| **Discovery** | Manual | Manual | Typed in `workspace.py` | SSM parameters: `/agentcore/.../agents/{name}/mcp_url` |

**How it translates to cloud:** Local MCP servers (stdio processes) become AgentCore-deployed containers with enterprise security. The AILA SDK MCP server (`skill-sdk-aila`) runs as both a local stdio server and a cloud AgentCore runtime — same code, different transport.

### 6. Structured Development

| Aspect | Kiro Runtime | Claude Runtime | AILA SDK | Artisyn Cloud Runtime |
|---|---|---|---|---|
| **Planning** | Specs | Plan Mode | SDLC skills | N/A — cloud agents execute, not plan |
| **Workflow skills** | N/A | N/A | `generic-sdlc`, `workspace-management` | Same skills available via catalog |

**How it translates to cloud:** Structured development is a local activity. Cloud agents consume the results (published workspace, agents, skills) — they don't do planning.

### 7. Resource Catalog

| Aspect | Kiro Runtime | Claude Runtime | AILA SDK | Artisyn Cloud Runtime |
|---|---|---|---|---|
| **Resource types** | N/A | N/A | 15 types (RESOURCE_CONFIG) | Same 15 types in S3/DynamoDB |
| **Discovery** | N/A | N/A | `aila_list_resources()` | Same API via Lambda / MCP server |
| **Access** | N/A | N/A | `aila_get_resource()` | Same API; also direct S3 read |
| **Storage** | N/A | N/A | File provider (local) | AWS: S3 (content) + DynamoDB (metadata) |
| **Multi-cloud** | N/A | N/A | Provider abstraction | AWS ✅ · Azure 🔲 · GCP 🔲 |

**How it translates to cloud:** The catalog is the bridge. Resources published locally via `workspace.py publish` land in S3/DynamoDB. Cloud agents read from the same catalog. The `skill-sdk-aila` API works identically in both environments — only the provider changes (FileProvider → AWSProvider).

**Important:** This is not a skill catalog — it is an Agentic Catalog that goes far beyond skills and agents. It catalogs skills, agents, knowledge, data sources, data catalogs, prompts, workspaces, workshops, PIRs, models, and applications across clouds in one system. Nothing like this exists in Kiro, Claude Code, or any other vendor tool.

### 8. Workspace Inheritance

| Aspect | Kiro Runtime | Claude Runtime | AILA SDK | Artisyn Cloud Runtime |
|---|---|---|---|---|
| **Hierarchy** | N/A | N/A | 4 levels (Org → Workspace → Project → User) | Same hierarchy, resolved at runtime |
| **Resolution** | N/A | N/A | `resolve_workspace()` | Same function, called by `ContextSystemPromptHook` |
| **Merge** | N/A | N/A | Parent-first concat (steering/skills); dedup (tools); leaf-only (prompt) | Identical merge strategy |
| **Context injection** | N/A | N/A | N/A | `agent.state["contexts"]` = `{aila.org, aila.workspace, aila.project, aila.user}` |

**How it translates to cloud:** Workspace inheritance is fully automatic in cloud. When an agent starts, `ContextSystemPromptHook` calls `resolve_workspace()`, walks the parent chain in the catalog, merges steering/skills/tools, and injects everything into the agent's system prompt. The developer defines the hierarchy in `workspace.py`; the cloud runtime applies it.

### 9. Code Knowledge

| Aspect | Kiro Runtime | Claude Runtime | AILA SDK | Artisyn Cloud Runtime |
|---|---|---|---|---|
| **Code understanding** | LSP + Tree-sitter | Code reading + grep | `KNOW.md` extraction | `KNOW.md` from catalog as steering/knowledge resource |
| **Cross-repo** | `external-links/` symlinks + `@path` file refs | `@` file references | `KiroExternalLink` + `KNOW.md` | Knowledge resources in S3 catalog |
| **Sharing** | Local only | Local only | Catalog (multi-provider) | Same catalog — any cloud agent can access any team's knowledge |

**How it translates to cloud:** Cloud agents can't run LSP or read local filesystems. Instead, `KNOW.md` files (AST-extracted code metadata) are published to the catalog. Cloud agents load them as knowledge resources — same information, different access pattern.

### 10. Team Onboarding

| Aspect | Kiro Runtime | Claude Runtime | AILA SDK | Artisyn Cloud Runtime |
|---|---|---|---|---|
| **Setup docs** | Manual | Manual | Auto-generated `WORKSPACE_BOOTSTRAP.md` | N/A — cloud agents are pre-configured |
| **Verification** | Manual | Manual | Auto-generated `WORKSPACE_SELFTEST.md` | Health checks via AgentCore runtime status |
| **Overview** | Manual | Manual | Auto-generated `README_WORKSPACE.md` | Catalog UI shows workspace summary |

**How it translates to cloud:** Onboarding docs are for local development. Cloud agents don't need bootstrapping — they're deployed with full configuration from the catalog. The Catalog UI provides the cloud equivalent of `README_WORKSPACE.md`.

### 11. Security & Governance

| Aspect | Kiro Runtime | Claude Runtime | AILA SDK | Artisyn Cloud Runtime |
|---|---|---|---|---|
| **Permissions** | `allowedTools` per agent | `/permissions` + sandbox | Type validation | IAM role per agent, KMS encryption, VPC isolation |
| **Authentication** | Local user | Local user | N/A | Cognito SSO → JWT with workspace claims |
| **Authorization** | N/A | N/A | N/A | Workspace filtering: JWT workspace → catalog visibility |
| **Audit** | N/A | N/A | N/A | CloudWatch logs, DynamoDB session history |
| **Multi-tenant** | N/A | N/A | N/A | Workspace isolation — users see only their workspace resources |
| **Encryption** | N/A | N/A | N/A | KMS keys per service (S3, DynamoDB, SQS, Lambda, CloudWatch) |

**What cloud adds:** Enterprise security that doesn't exist in local runtimes. IAM per agent, KMS encryption at rest, VPC network isolation, Cognito authentication, workspace-based authorization, and full audit trails.

### 12. Streaming & Transport

| Aspect | Kiro Runtime | Claude Runtime | AILA SDK | Artisyn Cloud Runtime |
|---|---|---|---|---|
| **Transport** | Local process | Local process | N/A | AppSync Events (WebSocket) + EventBridge + SQS FIFO |
| **Streaming** | IDE renders | Terminal renders | N/A | `stream_start` → `stream_chunk` → `stream_complete` events |
| **Multi-user** | Single user | Single user | N/A | Concurrent users via session isolation |
| **Session persistence** | SQLite DB (`~/.kiro/`), `/chat save/load`, custom scripts | Checkpoints (local) | N/A | DynamoDB (3-table: session, agent, message) + S3 artifacts |

**What cloud adds:** Real-time streaming to web UIs, persistent sessions across browser refreshes, multi-user concurrent access, and event-driven architecture for agent routing.

---

### 13. Self-Learning Loop

| Aspect | Kiro Runtime | Claude Runtime | AILA SDK | Artisyn Cloud Runtime |
|---|---|---|---|---|
| **Feedback mechanism** | N/A | N/A | PIR (Post-Implementation Review) skill generates review after execution | Full cycle: execute → PIR → human approval → skill update |
| **Skill improvement** | Manual editing | Manual editing | PIR identifies problems + opportunities | Self-correcting: usage data feeds back into skill refinement |
| **Maturity levels** | N/A | N/A | Skill definitions support maturity metadata | Manual → Assisted → Supervised → Autonomous (progressive trust) |
| **Usage tracking** | N/A | N/A | N/A | Telemetry per user, per workspace: token consumption, skill effectiveness, error rates |

**What cloud adds:** The self-learning loop is a production capability. Skills improve through organizational usage — every execution generates a PIR, human reviews approve improvements, and the skill is updated in the catalog. This creates compounding organizational IP that no vendor provides. The correct approach: start by reviewing everything (Manual), gradually increase trust as skills prove reliable (Assisted → Supervised), never fully remove human oversight (Autonomous still has guardrails).

### 14. Business Application Workspaces

| Aspect | Kiro Runtime | Claude Runtime | AILA SDK | Artisyn Cloud Runtime |
|---|---|---|---|---|
| **Target users** | Engineers | Engineers | Engineers (workspace authors) | Engineers + PMs + DMs + AMs + business stakeholders |
| **Design environment** | ✅ Prototype agents, skills, steering locally | ✅ Prototype agents, skills, steering locally | Typed workspace definitions; local runtimes serve as design/prototyping environment | Enterprise web portal with same workspace context |
| **Delivery agents** | N/A | N/A | DM, PM, EM agent definitions with PMBOK/Scrum/SAFe/RAIN steering | Production delivery agents: 45+ PM skills, 20+ steering docs, risk management, sprint execution |
| **Non-technical access** | N/A | N/A | N/A | Same workspace context accessible via web UI — no CLI or IDE required |
| **Use case** | Code development | Code development | Define business workspaces using same best practices as code workspaces | PMs walk through SDLC, DMs assess risks, EMs plan accounts — all agent-assisted |

**How it works:** Kiro and Claude best practices (steering, skills, agents, workspace structure) apply equally to business application design. Engineers use Kiro/Claude as the design and prototyping environment — more agile and convenient than cloud for iteration. Once validated, the same workspace definition publishes to the Artisyn Cloud Runtime where non-technical users access it via web portal. The architecture is identical; only the audience and interface change.

### 15. Data Platform Integration

| Aspect | Kiro Runtime | Claude Runtime | AILA SDK | Artisyn Cloud Runtime |
|---|---|---|---|---|
| **Data access** | Local filesystem | Local filesystem | Data source/catalog/query resource types in catalog | Enterprise data lake (open-source, no Snowflake license) |
| **Agent understanding** | Code reading | Code reading | `DATA_SOURCE.md`, `DATA_CATALOG.md`, `DATA_QUERY.md` resource types | Agents natively understand data lake structure, can deploy lakes, generate ingestion code |
| **Data processing** | N/A | N/A | N/A | Agents process any data type automatically; PySpark, Hadoop, Glue |

**What cloud adds:** AI agents need data to reason about. The Artisyn data platform is built entirely on open-source formats that AI models are trained on — agents understand it natively without proprietary format translation. Agents can deploy data lakes, generate ingestion code, and process data automatically.

---

## What AILA SDK Does NOT Do

| Area | Position |
|---|---|
| **Replace Kiro Runtime or Claude Runtime** | No — both runtimes work as designed; AILA SDK generates files they consume |
| **Replace steering/CLAUDE.md** | No — generates steering files; runtimes load them natively |
| **Replace skills** | No — provides catalog; runtimes discover via standard `SKILL.md` |
| **Replace hooks** | No — uses native hook systems; provides generation/validation pipeline |
| **Replace Kiro Specs / Claude Plan Mode** | No — provides SDLC skills, not a planning replacement |
| **Require cloud** | No — works locally with file providers; cloud is optional |
| **Lock you in** | No — all outputs are standard formats (JSON, markdown, SKILL.md) |

---

## What Artisyn Cloud Runtime Adds Beyond Local

| Capability | Local (Kiro/Claude) | Cloud (Artisyn) |
|---|---|---|
| **Session persistence** | SQLite DB, file export, custom scripts | DynamoDB — survives restarts, accessible from any client |
| **Multi-user** | Single developer | Concurrent users with workspace isolation |
| **Authentication** | Local user context | Cognito SSO → JWT → workspace claims |
| **Authorization** | File permissions | Workspace-based catalog filtering |
| **Streaming** | Terminal/IDE | AppSync WebSocket to web UIs |
| **Agent deployment** | Local process | AgentCore containers (ECR + IAM + VPC) |
| **MCP in production** | stdio process | AgentCore runtime with SigV4 auth |
| **Monitoring** | Console output | CloudWatch dashboards, alarms, log groups |
| **Encryption** | OS-level | KMS per service (S3, DynamoDB, SQS, Lambda) |
| **Event routing** | Direct invocation | EventBridge → SQS FIFO → Lambda → AgentCore |
| **Scaling** | Single machine | Serverless (AgentCore auto-scales) |

---

## Cloud Provider Support

| Provider | Status | Runtime | Storage | Auth |
|---|---|---|---|---|
| **AWS** | ✅ Production | Bedrock AgentCore + Strands SDK | S3 + DynamoDB | Cognito + IAM + SigV4 |
| **Azure** | 🔲 Planned | Azure AI Agent Service | Blob Storage + Cosmos DB | Entra ID + Managed Identity |
| **GCP** | 🔲 Planned | Vertex AI Agent Builder | Cloud Storage + Firestore | Google IAM + Workload Identity |

The AILA SDK is cloud-agnostic by design — the provider abstraction (`SkillsProvider` base class) supports any storage backend. The catalog API (`aila_list_skills()`, `aila_get_resource()`, etc.) works identically regardless of provider.

---

## The Full Pipeline: Local → Cloud

```
workspace.py (typed definition)
    │
    ├── workspace.py generate ──→ .kiro/steering/, .kiro/agents/, .kiro/skills/
    │                              (Kiro Runtime consumes these)
    │
    ├── workspace.py generate ──→ CLAUDE.md, .claude/agents/, .claude/skills/
    │                              (Claude Runtime consumes these — planned)
    │
    ├── workspace.py catalog  ──→ .aila/catalog/skills/
    │                              declarative-agent-management/artifacts/{agent}/AGENT.json
    │                              workspace-management/artifacts/{ws}/WORKSPACE.json
    │                              aila-knowledge/artifacts/{name}/KNOW.md
    │
    └── workspace.py publish  ──→ S3 + DynamoDB (AWS)
                                   │
                                   ▼
                          Artisyn Cloud Runtime
                                   │
                          ContextSystemPromptHook
                                   │
                          resolve_workspace() → parent chain
                                   │
                          Steering + Skills + Tools + Context
                                   │
                    ┌──────────────┴──────────────┐
                    │                             │
                    ▼                             ▼
           Technical Users                Business Users
           (engineers via CLI/API)        (PMs/DMs/AMs via Web Portal)
           • Extend workspaces            • Use published workspaces
           • Create complex skills        • Extend with workspace skills
           • Debug and iterate            • Add steering and context
           • Publish improvements         • Discover via Catalog UI
```

Same `workspace.py`. Same agents. Same steering. Same skills. Kiro and Claude are the factory — where complex skills, agents, and workspaces are designed and prototyped. The Artisyn Cloud Runtime is where they execute at scale, accessible to both technical and business users. The Agentic Catalog is the shared discovery layer across all users and runtimes.
