# Workshop Agenda: AI-Assisted Development with KNOW.md

## What We're Building

We're working with a **full-stack web application** — a FastAPI + React template that includes:
- **Backend:** Python/FastAPI REST API with SQLModel ORM, PostgreSQL, JWT authentication, Alembic migrations
- **Frontend:** React/TypeScript with TanStack Router, TanStack Query, shadcn/ui components, Vite

The app currently has user management and a simple "Items" CRUD feature. During this workshop, we'll **add a Time Tracking feature** — projects, time entries, and a dashboard — using AI agents that understand the codebase through auto-generated metadata.

The JIRA epic (AWSP-114) with 7 stories and acceptance criteria is already created. The agents will read the requirements from JIRA and implement them following existing codebase patterns.

---

## Prerequisites (Complete Before Workshop)

### 1. Development Environment

#### Python 3.10+

macOS:
```bash
brew install python
```

Windows:
```bash
winget install Python.Python.3
```

Linux:
```bash
sudo apt update
sudo apt install python3 python3-pip
```

Verify:
```bash
python3 --version  # Should be 3.10 or higher
```

#### Node.js 18+

macOS:
```bash
brew install node
```

Windows:
```bash
winget install OpenJS.NodeJS
```

Linux:
```bash
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
sudo apt install nodejs
```

Verify:
```bash
node --version  # Should be 18 or higher
npm --version
```

#### Git

Verify:
```bash
git --version
```

### 2. Kiro CLI

Install Kiro CLI following the official instructions. Verify:
```bash
kiro --version
```

### 3. Access Verification

Verify you can access:
- [ ] https://gitlab.dataart.com/da/dalf — GitLab repository access
- [ ] https://github.com/okomissarov/full-stack-fastapi-template — workshop repo (public)
- [ ] https://github.com/fastapi/full-stack-fastapi-template — original repo for comparison (public)

### 4. Clone Workshop Repo

```bash
git clone https://github.com/okomissarov/full-stack-fastapi-template.git
cd full-stack-fastapi-template
```

### 5. Install skill-sdk-aila (Optional, for home assignment)

```bash
pip install skill-sdk-aila
```

---

## Agenda

### Part 0: AILA SDK Bootstrap (15 min)

**Goal:** Set up the AILA development environment and verify all dependencies.

#### 0.1 Clone aila-kiro-home
```bash
git clone git@gitlab.dataart.com:da/dalf/aila-kiro-home.git
cd aila-kiro-home
```

#### 0.2 Bootstrap AILA SDK
Follow the bootstrap instructions to install and verify dependencies:
```bash
cat AILA-SKILLS-BOOTSTRAP.md
```

This sets up:
- `skill-sdk-aila` — AILA Catalog SDK (metadata extraction, skill discovery)
- `aila-catalog-schema` — workspace and agent configuration types
- Global Kiro steering and settings

#### 0.3 Verify
```bash
python3 -c "from skill_sdk_aila import aila_self_diagnostics; print(aila_self_diagnostics())"
```

#### 0.4 Clone Workshop Repo
```bash
cd ..
git clone https://github.com/okomissarov/full-stack-fastapi-template.git
cd full-stack-fastapi-template
python3 workspace.py validate
```

---

### Part 1: KNOW.md and Code Knowledge (30 min)

**Goal:** Understand how auto-generated code metadata makes AI agents faster and more accurate.

#### 1.1 Introduction (5 min)
- What is KNOW.md — auto-generated AST/tree-sitter metadata from source code
- How it differs from manual context (CLAUDE.md, hand-written steering docs)
- One command to generate: `python -m skill_sdk_aila.metadata --document`

#### 1.2 Setup (5 min)
Clone the pre-documented repository:
```bash
git clone https://github.com/okomissarov/full-stack-fastapi-template.git
cd full-stack-fastapi-template
python3 workspace.py validate
```

#### 1.3 Hands-On: Ask the Knowledge Agents (10 min)
Open Kiro in the repo. The workspace has two specialist agents with KNOW.md loaded:
- `backend-py` — knows all Python/FastAPI patterns
- `frontend-ts` — knows all React/TypeScript patterns

Try these prompts and observe speed + quality:
- "What authentication flow does this app use?"
- "How does the User model relate to Items? Show the full schema chain."
- "Add a new 'projects' resource following the items pattern."

#### 1.4 Comparison Review (10 min)
Review `docs/workshop/know-md-impact-analysis.md` — pre-generated comparison:

| | No KNOW.md | With KNOW.md |
|---|---|---|
| Response time | 57s | 10s |
| Code examples | None | Full implementation |
| File reads needed | 15+ | 0 |
| Pattern accuracy | Variable | Exact match |

Key takeaway: KNOW.md is auto-generated, zero maintenance, and makes agents both faster and more capable.

---

### Part 2: Feature Implementation with AI Agents (30 min)

**Goal:** Implement a real feature using AI agents that read JIRA requirements and generate pattern-accurate code.

#### 2.1 The Feature: Time Tracking (5 min)
- JIRA Epic: AWSP-114 — Time Tracking Feature
- 7 stories with acceptance criteria:
  - Backend: Models, Project API, Time Entry API (with summary endpoint)
  - Frontend: Projects page, Time Entries page, Dashboard, Sidebar navigation
- Implementation order: backend models → routes → tests → frontend components

#### 2.2 Agent-Driven Implementation (20 min)
Feed the agent assignment to the default agent:
```
Read docs/workshop/agent-assignment.md and execute it.
```

Watch the orchestration:
1. Default agent reads JIRA epic and creates a plan
2. Delegates backend stories to `backend-py` subagent
3. `backend-py` implements models, routes, tests — following patterns from KNOW.md
4. Delegates frontend stories to `frontend-ts` subagent
5. `frontend-ts` implements components, routes, dashboard

We'll get as far as we can in 20 minutes — likely through backend + some frontend.

#### 2.3 Review Results (5 min)
- Check generated files
- Run backend tests
- Review the reference implementation: `feature/time-tracking-implementation` branch
- Screenshots of the working UI: `docs/workshop/screenshots/`

---

### Part 3: Continue Offline (Home Assignment)

**Goal:** Complete the implementation and verify the KNOW.md impact yourself.

#### Assignment A: Finish the Feature
Continue implementing remaining stories from AWSP-114. The agents have the JIRA acceptance criteria and KNOW.md — just keep delegating.

Reference implementation available on the `feature/time-tracking-implementation` branch.

#### Assignment B: Verify KNOW.md Impact
1. Clone the original undocumented repo: `https://github.com/fastapi/full-stack-fastapi-template.git`
2. Set up Kiro with `/code init` — no KNOW.md, no workspace
3. Ask the same questions from Part 1
4. Compare your results with the workshop findings
5. Optionally: generate KNOW.md yourself and see the difference

Full instructions: `docs/workshop/workshop.md`

---

## Repository Structure

```
full-stack-fastapi-template/
├── workspace.py                    # Kiro workspace with 2 agents
├── document-meta/
│   ├── python/KNOW.md              # Auto-generated Python metadata (78 KB)
│   └── typescript/KNOW.md          # Auto-generated TypeScript metadata (180 KB)
├── .kiro/agents/
│   ├── backend-py.json             # Backend agent (resources: python KNOW.md)
│   └── frontend-ts.json            # Frontend agent (resources: typescript KNOW.md)
├── docs/workshop/
│   ├── workshop.md                 # Detailed workshop guide
│   ├── agent-assignment.md         # Agent implementation instructions
│   ├── know-md-impact-analysis.md  # With vs without KNOW.md comparison
│   ├── adding-projects-resource-with-know.md      # 10s focused response
│   ├── adding-project-resources.md                # 57s code-only response
│   ├── adding-projects-resource-with-know-detailed.md  # 93s comprehensive response
│   ├── pir-time-tracking-feature.md               # Post-implementation review
│   └── screenshots/                # Working UI screenshots
├── backend/app/                    # FastAPI backend
└── frontend/src/                   # React frontend
```

## Key Links

- **Workshop repo:** https://github.com/okomissarov/full-stack-fastapi-template
- **Implementation branch:** `feature/time-tracking-implementation`
- **JIRA Epic:** AWSP-114
- **Original repo (for comparison):** https://github.com/fastapi/full-stack-fastapi-template
