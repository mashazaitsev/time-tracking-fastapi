# KNOW.md and Code Intelligence — How It Works

## The Problem

AI coding assistants need to understand your codebase to help effectively. There are three approaches to giving them that understanding, each with different tradeoffs.

---

## Approach 1: Traditional Tools (LSP, grep, file reads)

Tools like GitHub Copilot, Cursor, and standard IDE integrations rely on runtime exploration:

```
User asks question
  → Agent searches files (grep, glob)
  → Agent reads files one by one
  → Agent uses LSP for type info and references
  → Agent builds understanding incrementally
  → Agent answers
```

**What works:**
- LSP gives precise type information and symbol references
- grep finds exact text matches
- No setup required beyond the IDE

**What doesn't:**
- Every session starts from zero — no memory of codebase structure
- Agent reads files it doesn't need, wastes tokens and time
- Understanding is limited to what the agent happens to read
- No awareness of business logic, relationships between modules, or architectural patterns
- Slow for large codebases — 15-40+ file reads per question

---

## Approach 2: Manual Context (CLAUDE.md, Kiro Steering)

Claude Code uses `CLAUDE.md`, Kiro uses `.kiro/steering/` — hand-written context files that describe the project:

```
Developer writes CLAUDE.md or steering docs
  → Agent loads context at session start
  → Agent has project overview
  → Agent answers faster
```

**What works:**
- Agent starts with project understanding
- Faster responses — less exploration needed
- Can capture architectural decisions and conventions

**What doesn't:**
- Developer writes and maintains the docs — real time cost
- Docs drift from code — no automatic sync
- Coverage is whatever the developer chose to document
- Subjective — depends on what the developer thinks is important
- Doesn't scale — 50-file project is manageable, 500-file project is not

---

## Approach 3: Auto-Generated Metadata (KNOW.md)

AILA Code Intelligence extracts structured metadata directly from source code using AST parsing (Python) and tree-sitter (TypeScript, Terraform, Terragrunt):

```
Run one command: python -m skill_sdk_aila.metadata --document
  → Parser reads every source file
  → Extracts: functions, classes, signatures, parameters, return types
  → Extracts: docstrings → Purpose, Structure, Relationships, Flow
  → Extracts: imports, dependencies, module structure
  → Generates KNOW.md — structured JSON metadata
  → Agent loads KNOW.md at session start
  → Agent has complete codebase understanding
  → Agent answers immediately
```

**What works:**
- Zero manual writing — generated from code
- Always in sync — regenerate after changes
- 100% coverage — every function, class, and module
- Structured — not prose, but machine-readable metadata
- Scales to any codebase size

**What it produces:**
```json
{
  "file": "crud.py",
  "purpose": "Database CRUD operations for users and items",
  "functions": [
    {
      "name": "create_user",
      "line": 42,
      "signature": "create_user(*, session: Session, user_create: UserCreate) -> User",
      "purpose": "Create new user with hashed password in database",
      "structure": "session (Session): input - Database session\nuser_create (UserCreate): input - User creation data\nuser (User): output - Created user record",
      "relationships": "Consumes: UserCreate schema\nProduces: User record in database",
      "flow": "1. Hash password\n2. Create User model\n3. Persist to database\n4. Return created user"
    }
  ]
}
```

---

## Progressive Discovery: Metadata First, Code Second

The key insight is that agents don't need to read source files to understand a codebase. They need metadata — what exists, what it does, how it connects.

KNOW.md enables a two-phase approach:

**Phase 1: Metadata (instant)**
Agent reads KNOW.md → knows every function, class, relationship, and pattern in the codebase. No file I/O. This is enough to answer architecture questions, plan implementations, and generate pattern-accurate code.

**Phase 2: Code (on demand)**
When the agent needs exact implementation details (e.g., to modify a specific function), it reads that one file. Not 15 files — one file, because it already knows which file and which line.

```
Traditional:     Read 15 files → understand → answer     (slow, wasteful)
Manual context:  Read CLAUDE.md → read 5 files → answer  (faster, but manual)
KNOW.md:         Read metadata → answer                   (instant, automatic)
                 Read metadata → read 1 file → modify     (precise, targeted)
```

---

## Three Levels of Metadata Quality

KNOW.md works with any codebase, but quality improves with documentation:

### Level 1: Undocumented Code
Extracts from AST only — file paths, function names, signatures, parameters, imports, class structures.

Agent can: navigate to exact locations, understand structure, see dependencies.

### Level 2: Standard Docstrings
Extracts docstrings (Python), JSDoc (TypeScript), HCL comments (Terraform) in addition to AST.

Agent can: understand what code does, see usage examples, read parameter descriptions.

### Level 3: AILA Standard Documentation
Extracts structured sections: Purpose, Structure, Relationships, Semantics, Flow, Important.

Agent can: understand business context, see data flow across modules, identify critical requirements, generate pattern-accurate code for new features.

Each level is additive. You can start with Level 1 (zero effort) and improve incrementally.

---

## Measured Impact

From the workshop comparison on a full-stack FastAPI + React application:

| Metric | Without KNOW.md | With KNOW.md |
|---|---|---|
| Response time | 57 seconds | 10 seconds |
| Files read by agent | 15+ | 0 |
| Code examples in response | None | Full implementation |
| Pattern accuracy | Variable | Exact match |
| Comprehensive response | 57s, no code | 93s, 500 lines of code |

The 93-second comprehensive response was generated entirely from KNOW.md metadata with zero file access — complete backend models, API routes, React components, and a pattern reference table.

---

## How to Set Up

### 1. Install

```bash
pip install skill-sdk-aila
```

### 2. Configure

```bash
# Analyze codebase and generate config
python -m skill_sdk_aila.metadata --analyse
```

This creates:
- `.aila/documentation.json` — which languages and directories to scan
- `.aila/.docignore` — what to exclude (tests, generated code, dependencies)

### 3. Generate

```bash
python -m skill_sdk_aila.metadata --document
```

This creates KNOW.md files in the configured output directory.

### 4. Load into Agent

Add KNOW.md as a Kiro agent resource:
```json
{
  "resources": ["file://document-meta/python/KNOW.md"]
}
```

Or copy to steering:
```bash
cp document-meta/python/KNOW.md .kiro/steering/
```

### 5. Improve (Optional)

Add AILA-standard docstrings to source code for Level 3 quality:
```bash
# Ask Kiro agent to document files using the standard
"Re-document all Python files using AILA code documentation standard.
Use subagents in parallel. Skip test files."
```

Then regenerate:
```bash
python -m skill_sdk_aila.metadata --document
```

---

## Comparison Summary

| | Traditional (LSP/grep) | Manual (CLAUDE.md) | KNOW.md (auto-generated) |
|---|---|---|---|
| Setup cost | Zero | High (developer writes) | Low (one command) |
| Maintenance | Zero | High (developer updates) | Low (re-run command) |
| Coverage | What agent reads | What developer wrote | 100% of codebase |
| Accuracy | Depends on exploration | Depends on author | Always matches code |
| Speed | Slow (runtime discovery) | Fast (pre-loaded) | Fast (pre-loaded) |
| Scales | Poorly (more files = slower) | Poorly (more to write) | Well (automated) |
| Business logic | Not captured | If documented | If docstrings exist |

KNOW.md is not a replacement for LSP — it's a complement. LSP gives precise type information and references at specific code locations. KNOW.md gives the big picture — what exists, what it does, how it connects. Together, they give agents both the map and the magnifying glass.
