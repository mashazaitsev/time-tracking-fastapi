# AILA Code Intelligence & Skills

## MANDATORY: Code Navigation Protocol

This project has pre-extracted code metadata. You MUST use it before searching files.

**KNOW.md files** contain function names, file paths, line numbers, purposes, and relationships for all code.

  - `.claude/aila-code-doc/python/KNOW.md` — python (40 files)
  - `.claude/aila-code-doc/typescript/KNOW.md` — typescript (89 files)

### How to Navigate Code

1. **Read KNOW.md FIRST** — read the relevant `.claude/aila-code-doc/{language}/KNOW.md` file
2. **Find the function/class** — locate it in the JSON metadata (has exact `path` and `line`)
3. **Open the file directly** — use the exact path and line number from metadata
4. **Only search as fallback** — use grep/glob ONLY if metadata doesn't have what you need

### Example

User asks: "Show me the get_skill function"

Correct:
1. Read `.claude/aila-code-doc/python/KNOW.md`
2. Find `get_skill` → path: `skill_sdk_aila/providers/base.py`, line: 297
3. Read that file at that line — 1 tool call, instant

Wrong:
1. Grep for "get_skill" across the codebase — slow, noisy, wasteful

### Important Sections

When KNOW.md metadata contains an `important` field for a function, read it FIRST. It contains critical requirements, breaking changes, and mandatory constraints that must not be ignored.

---

## Skills System

This project uses AILA skills — reusable instruction packages that teach you specific workflows.

### Discovering Skills

Read `.claude/skill_catalog.json` for the full list of available skills with names, descriptions, and tags.

### Using a Skill

```python
from skill_sdk_aila import aila_get_skill

# Load skill instructions
skill = aila_get_skill("skill-name")
print(skill['instructions'])  # SKILL.md content — follow these instructions
```

Or read directly:
```python
from skill_sdk_aila import aila_get_skill_resource
content = aila_get_skill_resource("skill-name", "SKILL.md")
```

### Searching Skills

```python
from skill_sdk_aila import aila_search_skills

# Search by keyword
results = aila_search_skills(query="documentation")

# Filter by category or tags
results = aila_search_skills(category="automation", tags=["python"])
```

### Listing All Skills

```python
from skill_sdk_aila import aila_list_skills
skills = aila_list_skills()
print(f"Found {skills['count']} skills")
```

### When to Use Skills

- When the user asks about a workflow that matches a skill name/description
- When you need step-by-step guidance for a repeatable task
- Load the skill with `aila_get_skill()` and follow its `instructions`

---

## SDK API Quick Reference

All functions auto-initialize from `~/.aila/settings.json`. No manual setup needed.

| Function | Purpose |
|---|---|
| `aila_list_skills()` | List all available skills |
| `aila_search_skills(query, category, tags)` | Search skills with filters |
| `aila_get_skill(name)` | Get skill with full instructions |
| `aila_get_skill_resource(name, path)` | Read a specific skill resource file |
| `aila_describe_providers()` | Show provider discovery details |
| `aila_self_diagnostics()` | System health check |

Import from: `from skill_sdk_aila import aila_list_skills, aila_get_skill, ...`

---

## Documentation Standard

When writing or reviewing code documentation, follow the standard at:
`.claude/aila-code-doc/code-documentation-standard.md`

---

## Regenerate After Changes

```bash
aila-meta --document
```
