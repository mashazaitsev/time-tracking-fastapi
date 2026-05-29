# Workspace Management

Define, generate, and manage Kiro and Claude Code workspaces with catalog skill integration.

## Quick Start

**Create workspace.py:**
```python
from skills_sdk.space import KiroWorkspace, KiroAgent
from skills_sdk.space.kiro.generator import KiroCatalogSkill

workspace = KiroWorkspace(
    name="my-project",
    description="My project workspace",
    skills=[
        KiroCatalogSkill(name="dataart-aila/skills/sdlc-discovery-design"),
    ],
    agents=[
        KiroAgent(
            name="dev",
            description="Development agent",
            prompt="You are a development agent...",
            skills="skills/sdlc-discovery-design",
            tools=["code", "bash", "browser"],
        ),
    ],
)

if __name__ == "__main__":
    workspace.run_cli()
```

**Generate:**
```bash
python3 workspace.py generate --agent kiro    # For Kiro
python3 workspace.py generate --agent claude  # For Claude Code
```

**Validate:**
```bash
python3 workspace.py validate --agent kiro
```

## What Generate Produces

**For Kiro (`--agent kiro`):**
```
.kiro/
├── agents/{name}.json          # Agent configs
├── skills/{skill-name}/        # Deployed catalog skills
│   ├── SKILL.md
│   └── references/
├── steering/wsg-agent-guide.md # Auto-generated agent guide
└── settings/mcp.json           # MCP config (if defined)
```

**For Claude Code (`--agent claude`):**
```
.claude/
├── agents/{name}.md            # Agent configs (YAML frontmatter + prompt)
├── skills/{skill-name}/        # Deployed catalog skills
└── rules/delegation.md         # Auto-generated delegation rules
```

## Key Types

| Type | Purpose |
|------|---------|
| `KiroWorkspace` | Workspace definition + generation engine |
| `KiroAgent` | Agent config (name, prompt, tools, skills, resources) |
| `KiroCatalogSkill` | Reference to a catalog skill (fetched during generate) |

## Agent Configuration

```python
KiroAgent(
    name="pm",                              # Agent identifier
    description="Project Manager...",       # When to delegate to this agent
    prompt="You are a PM...",               # Inline prompt (or file:// URI)
    skills="skills/pm-expert-large-agile",  # Skill directory (loaded on demand)
    tools=["jira", "browser"],              # Available tools
    resources=[                             # Additional resources
        "skill://skills/sdlc-discovery-design/**/*.md",
    ],
)
```

**Prompt options:**
- Inline string: `prompt="You are a PM..."`
- File reference: `prompt="file://prompts/pm.md"` (relative to .kiro/agents/)

**Skills vs Resources:**
- `skills=` — directory path, agent reads SKILL.md + follows links to references/
- `resources=` — glob patterns, loaded into agent context

## Catalog Skills

Skills are fetched from the Artisyn Catalog during `generate`:

```python
skills=[
    KiroCatalogSkill(name="dataart-aila/skills/sdlc-discovery-design"),
    KiroCatalogSkill(name="dataart-aila/skills/pm-expert-large-agile"),
]
```

**Requirements:**
- MCP configured (`.kiro/settings/mcp.json`, `.mcp.json`, or env vars)
- Authenticated (token cached from first `catalog-mcp` login)

## MCP Configuration

Place in project root or globally:

```json
{
  "mcpServers": {
    "catalog": {
      "command": "catalog-mcp",
      "env": {
        "MCP_URL": "https://...",
        "MCP_CLIENT_ID": "...",
        "MCP_COGNITO_DOMAIN": "..."
      }
    }
  }
}
```

SDK reads from (in order): env vars → `.kiro/settings/mcp.json` → `.mcp.json` → `~/.kiro/settings/mcp.json` → `~/.claude/settings.json`

## Workflow

1. **Discover** — use Catalog MCP tools to find available skills and experts
2. **Define** — write workspace.py with agents and catalog skill references
3. **Generate** — `python3 workspace.py generate --agent kiro` (fetches skills, creates structure)
4. **Validate** — `python3 workspace.py validate --agent kiro` (checks all files exist)
5. **Use** — open Kiro/Claude in the directory, agents are ready
6. **Iterate** — edit workspace.py, re-generate (idempotent)

## Discovering Available Skills

Before writing workspace.py, use Catalog MCP tools to find relevant skills:

```
"List all skills in catalog"           → browse available experts and workflows
"Search catalog for project management" → find domain-specific skills
"Get skill dataart-aila/skills/sdlc-discovery-design" → read what it provides
```

Match skills to project needs, then assemble workspace.py with the selected skills and agents.

## Engine-Specific Capabilities

Each engine (Kiro, Claude Code) has different features and file formats:

- [Kiro capabilities](references/kiro-capabilities.md) — agent JSON, tools, MCP, hooks, path resolution
- [Claude Code capabilities](references/claude-capabilities.md) — agent .md, CLAUDE.md, rules, commands, model selection
