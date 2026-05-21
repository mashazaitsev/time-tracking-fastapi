"""
Purpose: Kiro workspace for full-stack-fastapi-template

Two specialist agents:
  - backend-py: FastAPI backend (Python KNOW.md)
  - frontend-ts: React frontend (TypeScript KNOW.md)
"""
from pathlib import Path
import sys

# Add aila-catalog-schema to path
schema_path = Path(__file__).parent.parent / "aila-catalog-schema"
if schema_path.exists():
    sys.path.insert(0, str(schema_path))
else:
    # Try workspace-agentic-squad external-links
    alt = Path.home() / "aila/agentic_aila/workspace-agentic-squad/external-links/aila-catalog-schema"
    if alt.exists():
        sys.path.insert(0, str(alt))

from aila_catalog_schema.kiro_workspace import KiroWorkspace, KiroPrompt, KiroCatalogSkill, prompt_ref
from aila_catalog_schema.kiro_agent import KiroAgent

workspace = KiroWorkspace(
    name="full-stack-fastapi",
    description="Full-stack FastAPI + React template with two specialist agents for backend and frontend code.",
    agents=[
        KiroAgent(
            name="backend-py",
            description="Expert in FastAPI backend: models, CRUD, API routes, auth, config, database, email utilities.",
            prompt=prompt_ref("backend-py.md"),
            tools=["code", "fs_read", "fs_write", "execute_bash", "grep", "glob"],
            resources=[
                "file://document-meta/python/KNOW.md",
            ],
        ),
        KiroAgent(
            name="frontend-ts",
            description="Expert in React frontend: components, routes, hooks, state management, API integration.",
            prompt=prompt_ref("frontend-ts.md"),
            tools=["code", "fs_read", "fs_write", "execute_bash", "grep", "glob"],
            resources=[
                "file://document-meta/typescript/KNOW.md",
            ],
        ),
    ],
    prompts=[
        KiroPrompt(name="backend-py.md", description="Backend agent system prompt"),
        KiroPrompt(name="frontend-ts.md", description="Frontend agent system prompt"),
    ],
    steering=[],
    skills=[
        KiroCatalogSkill(name="generic-sdlc", description="Structured software development lifecycle from idea to implementation"),
        KiroCatalogSkill(name="workspace-management", description="Kiro workspace lifecycle — define, generate, catalog, publish"),
    ],
    skill_provider=False,
)

if __name__ == "__main__":
    workspace.run_cli()
