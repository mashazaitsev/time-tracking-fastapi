# Workshop: KNOW.md Impact on AI Agent Code Quality

## Overview

This workshop demonstrates how pre-extracted code metadata (KNOW.md) impacts AI agent response speed, quality, and accuracy compared to agents that explore codebases at runtime.

**Duration:** ~45 min in-session + home assignment
**Prerequisites:** Kiro CLI installed, Python 3.12+, `skill-sdk-aila` installed

---

## Part 1: Hands-On with Knowledge Agents (In-Session)

### Setup (5 min)

Clone the pre-documented repository:

```bash
git clone https://github.com/okomissarov/full-stack-fastapi-template.git
cd full-stack-fastapi-template
```

Verify workspace:
```bash
python3 workspace.py validate
```

You should see two agents available:
- `backend-py` — FastAPI backend expert (Python KNOW.md loaded)
- `frontend-ts` — React frontend expert (TypeScript KNOW.md loaded)

### Exercise 1: Ask Questions (15 min)

Open Kiro in the repo and try these prompts. Observe how fast and detailed the responses are:

**Architecture questions:**
- "What authentication flow does this app use? Trace from login form to JWT token."
- "How does the User model relate to Items? Show the full schema chain."
- "What dependencies does the items route use and how are they injected?"

**Implementation questions:**
- "Add a new 'projects' resource following the items pattern with fields: status, start_date, end_date, budget."
- "Add a 'tags' field to items — what files need to change?"
- "How would I add email notification when a new user registers?"

**Debugging questions:**
- "If a user gets 403 on DELETE /items/{id}, what are the possible causes?"
- "What happens if the database is down when the app starts?"

Notice:
- ⚡ Responses come in seconds, not minutes
- 📋 Code examples match actual project patterns
- 🔗 Agents reference specific files, functions, and relationships

### Exercise 2: Observe Subagent Delegation (10 min)

Ask a cross-domain question to the default agent:
- "Add a 'projects' resource — cover both backend and frontend."

Watch how it delegates to `backend-py` and `frontend-ts` subagents in parallel.

### Part 1 Debrief (15 min)

Review the pre-generated comparison report: `docs/workshop/know-md-impact-analysis.md`

Key findings:
| | No KNOW.md | With KNOW.md (focused) | With KNOW.md (comprehensive) |
|---|---|---|---|
| Time | 57s | 10s | 93s |
| Code examples | None | CRUD + router | Full BE + FE (500 lines) |
| File reads | 15+ | 0 | 0 |
| Accuracy | Variable | Pattern-accurate | Pattern-accurate |

The "without KNOW.md" response (`docs/session-report.md`) spent most of its time exploring the codebase and produced a broad report with no code. The "with KNOW.md" responses produced actionable implementation guides with working code — generated entirely from metadata.

---

## Part 2: Home Assignment — Verify It Yourself

### Objective

Experience the difference firsthand. Clone the ORIGINAL undocumented repo, ask questions without KNOW.md, then compare with the workshop results.

### Step 1: Clone Original Repo

```bash
git clone https://github.com/fastapi/full-stack-fastapi-template.git full-stack-fastapi-original
cd full-stack-fastapi-original
```

### Step 2: Set Up Kiro and Code Intelligence

```bash
kiro
# Initialize code intelligence (LSP)
/code init
```

No workspace, no KNOW.md, no steering — just Kiro with code tools.

### Step 3: Ask Questions Without KNOW.md

Try these prompts and record your observations:

1. "What authentication flow does this app use? Trace from login form to JWT token."
2. "Add a new 'projects' resource following the items pattern with fields: status, start_date, end_date, budget."
3. "How does the User model relate to Items? Show the full schema chain."

**Record for each question:**
- ⏱ Response time
- 📄 Response length
- 💻 Did it include code examples?
- 🔍 How many files did the agent read?
- ✅ Was the code accurate to the actual patterns?

### Step 4: Review the Comparison Report

Open the impact analysis from the workshop repo:

```
https://github.com/okomissarov/full-stack-fastapi-template/blob/master/docs/workshop/know-md-impact-analysis.md
```

Compare your "without KNOW.md" results against the documented findings:
- Did your agent also spend time exploring before answering?
- Were your responses missing code examples?
- Did the agent read 15+ files to answer?

### Step 5: Understand KNOW.md and AILA Metadata Generation

Review these files in the workshop repo to understand how the metadata is generated:

| File | What It Shows |
|---|---|
| `.aila/documentation.json` | Configuration — which languages, which directories to scan |
| `.aila/.docignore` | Exclusion patterns — what to skip (tests, generated code, boilerplate) |
| `document-meta/python/KNOW.md` | Generated output — Python AST-extracted metadata (functions, classes, signatures, purposes, relationships) |
| `document-meta/typescript/KNOW.md` | Generated output — TypeScript tree-sitter-extracted metadata |
| `workspace.py` | How agents are configured to use KNOW.md as resources |
| `.kiro/agents/backend-py.json` | Agent config — `resources: ["file://document-meta/python/KNOW.md"]` |

Key concepts:
- **KNOW.md is auto-generated** — `python -m skill_sdk_aila.metadata --document` extracts metadata from source code via AST/tree-sitter parsing
- **No manual writing** — unlike CLAUDE.md or hand-written steering docs
- **Always in sync** — regenerate after code changes, metadata matches code
- **Structured metadata** — function signatures, purposes, flows, relationships, dependencies — not just file listings

### Step 6 (Optional): Generate KNOW.md for the Original Repo

If you have `skill-sdk-aila` installed, try generating KNOW.md yourself:

```bash
cd full-stack-fastapi-original
pip install skill-sdk-aila

mkdir -p .aila
cat > .aila/documentation.json << 'EOF'
{
  "output_dir": "document-meta",
  "providers": [
    {"type": "python", "enabled": true, "roots": ["."], "output": "python"},
    {"type": "typescript", "enabled": true, "roots": ["."], "output": "typescript"}
  ]
}
EOF

python -m skill_sdk_aila.metadata --document
```

Then add to Kiro steering and ask the same questions again:
```bash
mkdir -p .kiro/steering
cp document-meta/python/KNOW.md .kiro/steering/KNOW-python.md
cp document-meta/typescript/KNOW.md .kiro/steering/KNOW-typescript.md
```

You should see immediate improvement in response speed and quality — even without the AILA-standard docstrings that were added in the workshop repo.

### Deliverable

Write a short summary (3-5 sentences) of your findings:
- Did you observe the same speed/quality differences as the workshop demo?
- What surprised you?
- How does auto-generated KNOW.md compare to manually written context docs?

---

## Reference Materials

| File | Description |
|---|---|
| `docs/workshop/know-md-impact-analysis.md` | Full comparison report with metrics |
| `docs/workshop/adding-projects-resource-with-know.md` | Knowledge agent output (focused, 10s) |
| `docs/workshop/adding-project-resources.md` | Code-only agent output (no KNOW.md, 57s) |
| `docs/workshop/adding-projects-resource-with-know-detailed.md` | Knowledge agent output (comprehensive, 93s) |
| `document-meta/python/KNOW.md` | Auto-generated Python metadata |
| `document-meta/typescript/KNOW.md` | Auto-generated TypeScript metadata |
| `workspace.py` | Workspace definition with two agents |
