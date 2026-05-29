# Kiro Engine Capabilities

What `python3 workspace.py generate --agent kiro` produces and supports.

## Generated Structure

```
.kiro/
├── agents/{name}.json              # Agent configs (JSON)
├── skills/{skill-name}/            # Deployed catalog skills
│   ├── SKILL.md
│   └── references/
├── steering/                       # Steering symlinks + inline files
│   └── wsg-agent-guide.md
├── settings/
│   ├── mcp.json                    # MCP server configs
│   └── lsp.json                    # Language server configs
└── hooks/                          # Event-driven hooks (future)

prompts/
├── wsg-agent-guide.md              # Auto-generated: agent list + delegation
└── wsg-subagent-delegation.md      # Auto-generated: subagent rules

external-links/                     # Symlinks to external repos
README_WORKSPACE.md                 # Workspace overview
WORKSPACE_SELFTEST.md               # Verification prompts
WORKSPACE_BOOTSTRAP.md              # Setup guide for new users
```

## KiroAgent Fields

```python
KiroAgent(
    name="dev",                     # Required. Kebab-case identifier.
    description="...",              # Required. When to use this agent.
    prompt="...",                   # Required. Inline string or file:// URI.
                                    #   file:// resolves from .kiro/agents/ dir
    tools=["code", "bash"],         # Available tools for this agent.
    allowedTools=["*"],             # Tool patterns (glob). Default: all.
    resources=[                     # Loaded into agent context.
        "file://path/**/*.md",      #   file:// resolves from workspace root
        "skill://skills/name/**/*", #   skill:// resolves from .kiro/skills/
    ],
    steering="path/to/dir",         # Directory of steering .md files (glob loaded)
    skills="skills/skill-name",     # Skill directory (SKILL.md + references/)
    subagents=["other-agent"],      # Agents this one can delegate to
    includeMcpJson=True,            # Include MCP servers (default: True)
    model=None,                     # LLM model override (optional)
)
```

## KiroWorkspace Fields

```python
KiroWorkspace(
    name="my-project",              # Required. Kebab-case.
    description="...",              # Workspace purpose.
    agents=[...],                   # List of KiroAgent definitions.
    skills=[                        # Catalog skills to fetch and deploy.
        KiroCatalogSkill(name="dataart-aila/skills/sdlc-discovery-design"),
    ],
    prompts=[                       # Prompt file declarations (for README).
        KiroPrompt(name="dev.md", description="Dev agent prompt"),
    ],
    steering_symlinks=["path"],     # Paths to symlink into .kiro/steering/
    steering_inline={"name.md": "content"},  # Inline steering files
    hooks=[KiroHook(...)],          # Local hook definitions
    catalog_hooks=["hook-id"],      # Catalog hooks to fetch
    settings=KiroSettings(          # MCP + LSP config
        mcp=KiroMcpSettings(servers={"catalog": KiroMcpServer(command="catalog-mcp", env={...})}),
    ),
    external_links=[                # Symlinks to external repos
        KiroExternalLink(name="repo", target="../path", description="..."),
    ],
    prompts_dir="prompts",          # Where prompt files live (default: prompts/)
)
```

## Supported Tools

Kiro agents can use these tool identifiers:
- `code` — read/write/edit files
- `bash` / `execute_bash` — run shell commands
- `fs_read` / `fs_write` — file operations
- `grep` / `glob` — search
- `browser` — web browsing
- `jira` — Jira integration (via MCP)
- `use_subagent` — delegate to other agents

## MCP Configuration

```python
settings=KiroSettings(
    mcp=KiroMcpSettings(servers={
        "catalog": KiroMcpServer(
            command="catalog-mcp",
            env={"MCP_URL": "...", "MCP_CLIENT_ID": "...", "MCP_COGNITO_DOMAIN": "..."},
        ),
        "jira": KiroMcpServer(
            command="npx",
            args=["-y", "@anthropic/mcp-jira"],
            env={"JIRA_URL": "...", "JIRA_TOKEN": "..."},
        ),
    }),
)
```

## Hooks (Event-Driven)

```python
from skills_sdk.space.kiro.steering import KiroHook, HookEvent, HookAction

hooks=[
    KiroHook(
        event=HookEvent.FILE_WRITTEN,
        pattern="**/*.py",
        action=HookAction.VALIDATE,
        agent="validator",
        prompt="Check this file for...",
    ),
]
```

## Path Resolution

| Field | Resolves from | Example |
|-------|--------------|---------|
| `prompt` (file://) | `.kiro/agents/` directory | `file://../../prompts/dev.md` |
| `resources` (file://) | Workspace root | `file://external-links/repo/KNOW.md` |
| `resources` (skill://) | `.kiro/skills/` | `skill://skills/sdlc-discovery-design/**/*.md` |
| `steering` | Workspace root | `steering-docs/methodology` |
| `skills` | `.kiro/` | `skills/pm-expert-large-agile` |
