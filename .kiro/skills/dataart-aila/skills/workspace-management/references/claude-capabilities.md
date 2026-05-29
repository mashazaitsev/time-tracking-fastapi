# Claude Code Engine Capabilities

What `python3 workspace.py generate --agent claude` produces and supports.

## Generated Structure

```
.claude/
├── agents/{name}.md                # Agent configs (YAML frontmatter + prompt)
├── skills/{skill-name}/            # Deployed catalog skills
│   ├── SKILL.md
│   └── references/
├── rules/
│   ├── delegation.md               # Auto-generated: agent delegation guide
│   └── skills.md                   # Auto-generated: skills reference
├── commands/                       # Slash commands
│   ├── generate.md
│   ├── validate.md
│   └── info.md
├── settings.json                   # Permissions + PostToolUse hooks
└── lsp-plugin/.lsp.json            # Language server config

CLAUDE.md                           # Project memory (auto-read by Claude Code)
external-links/                     # Symlinks to external repos
README_WORKSPACE.md
WORKSPACE_SELFTEST.md
WORKSPACE_BOOTSTRAP.md
```

## Agent Format (.claude/agents/{name}.md)

```yaml
---
name: dev
description: "Development agent: code implementation, testing, debugging"
tools:
  - Read
  - Write
  - Edit
  - Bash
  - Grep
  - Glob
model: sonnet
---

You are a development agent...

## Available Knowledge

- [SDLC workflow](../../.claude/skills/dataart-aila/skills/sdlc-discovery-design/SKILL.md)
- [PM methodology](../../.claude/skills/dataart-aila/skills/pm-expert-large-agile/SKILL.md)
```

## Tool Mapping (Kiro → Claude Code)

| Kiro tool | Claude Code tool |
|-----------|-----------------|
| `code` | `Read`, `Write`, `Edit` |
| `bash` / `execute_bash` | `Bash` |
| `fs_read` | `Read` |
| `fs_write` | `Write`, `Edit` |
| `grep` | `Grep` |
| `glob` | `Glob` |
| `browser` | `WebFetch`, `WebSearch` |
| `use_subagent` | `Subagent` |

## Model Auto-Selection

| Agent role | Model |
|-----------|-------|
| Advisory (dm, pm, em, am) | `opus` |
| Code agents | `sonnet` |
| Fast/simple tasks | `haiku` |

Advisory agents get `Edit` and `Write` tools stripped (read-only enforcement).

## CLAUDE.md (Project Memory)

Auto-generated file read by Claude Code on every session start. Contains:
- Organization identity
- Compact agent index (who does what)
- CLI commands reference
- Workspace structure overview

## Rules

**delegation.md** — tells Claude Code which agent to use for which task:
```markdown
## Agent Delegation
- Sprint planning → @pm
- Architecture decisions → @dm
- Client communication → @em
```

**skills.md** — tells Claude Code what skills are available and how to use them.

## Commands (Slash Commands)

Generated in `.claude/commands/`:
- `/generate` — regenerate workspace
- `/validate` — validate workspace structure
- `/info` — show workspace metadata

## Settings (.claude/settings.json)

```json
{
  "permissions": {
    "allow": ["Read", "Grep", "Glob"],
    "deny": []
  },
  "hooks": {
    "PostToolUse": [...]
  }
}
```

**Note:** `settings.json` is NEVER overwritten if it exists (preserves user customization).

## Differences from Kiro

| Feature | Kiro | Claude Code |
|---------|------|-------------|
| Agent format | JSON | Markdown (YAML frontmatter) |
| Prompt | Separate file or inline | Inlined in agent .md |
| Steering | Symlinks in .kiro/steering/ | .claude/rules/*.md |
| Skills | .kiro/skills/ | .claude/skills/ |
| MCP config | .kiro/settings/mcp.json | .mcp.json (project root) |
| Project memory | — | CLAUDE.md (auto-read) |
| Slash commands | — | .claude/commands/*.md |
| Tool names | code, bash, fs_read | Read, Write, Edit, Bash |
