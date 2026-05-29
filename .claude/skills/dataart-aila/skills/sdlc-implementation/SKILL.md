# SDLC Implementation

Continuation of `sdlc-discovery-design`. Takes the project artifacts produced by the discovery-design phase and delivers working code with documentation.

## Prerequisites

This skill requires input from a prior `sdlc-discovery-design` execution:

- `{project}/design/detailed-design.md` — detailed design document
- `{project}/implementation/plan.md` — implementation plan
- `{project}/requirements/` — requirements context
- `{project}/research/` — research findings

**Or** equivalent Jira artifacts produced from the design phase (epics, stories with acceptance criteria, technical specs in attachments).

## Quick Start

**What it does:** Design → code tasks → TDD implementation → validated documentation

**When to use:**
- "Implement this design"
- "Create tasks from the implementation plan"
- "Execute implementation"
- "Generate deliverables"

**Inputs:**
- Project directory from `sdlc-discovery-design` (or Jira stories/epics derived from it)
- Codebase context (existing patterns, conventions)

**Outputs:**
- Deliverable documents (from templates)
- Structured code task files (`.code-task.md`)
- Working code via TDD (Explore → Plan → Code → Commit)
- Documentation (AGENTS.md, README.md, architecture docs)

---

## Core Workflow

### Step 10: Generate Deliverables

See [step-10-generate-deliverables.md](references/step-10-generate-deliverables.md)

Generate standard deliverable documents from templates:
- Present available deliverable types to user
- User selects which to generate (all, specific, or skip)
- Populate templates from project artifacts (requirements, research, design)
- Save to `{project}/deliverables/`
- Review each with user before proceeding

### Step 11: Create Implementation Tasks

See [step-11-create-implementation-tasks.md](references/step-11-create-implementation-tasks.md)

Break implementation plan into structured code tasks:
- Parse plan into actionable units
- Generate `.code-task.md` files with requirements, acceptance criteria, dependencies
- Process one step at a time (allows learning between steps)
- Support multiple input methods (text, file path, plan path)

### Step 12: Execute Implementation

See [step-12-execute-implementation.md](references/step-12-execute-implementation.md)

Implement code tasks using TDD:
- **Explore** — understand codebase patterns, existing code, conventions
- **Plan** — define approach, test strategy, implementation sequence
- **Code** — write tests first, then implementation, following existing patterns
- **Commit** — validate, format, commit with meaningful message

Modes:
- `interactive` — user confirms at each phase
- `auto` — runs end-to-end after initial setup

### Step 13: Validate & Document

See [step-13-validate-and-document.md](references/step-13-validate-and-document.md)

Validate implementation and generate documentation:
- Analyze codebase structure and patterns
- Generate AGENTS.md (AI-readable system overview)
- Generate/update README.md, CONTRIBUTING.md
- Check consistency across documentation
- Identify areas lacking detail
- Support update mode for incremental changes

---

## Execution Pattern

**Before starting:**
Load the project from `sdlc-discovery-design` output: `design/detailed-design.md` and `implementation/plan.md`. Or load Jira epic/stories with acceptance criteria.

**For each step:**
1. Load step reference file
2. Gather required parameters (ask upfront, not one at a time)
3. Execute step
4. Save artifacts
5. Review with user at checkpoints

**Completion:**
All code tasks implemented, tests passing, documentation generated and validated.

---

## Usage

```
"Implement the design from project-x/design/detailed-design.md"
"Create code tasks from the implementation plan"
"Execute task authentication-module in auto mode"
"Generate AGENTS.md for this codebase"
```

---

## Integration

- **Requires:** Output from `sdlc-discovery-design` or Jira artifacts derived from it
- **Output to:** `post-implementation-review` for documenting the delivery process
- **Extensible:** Domain-specific implementation skills can override steps (e.g., data lake adds pipeline testing, Glue job validation)
