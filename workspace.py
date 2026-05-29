from skills_sdk.space import KiroWorkspace, KiroAgent
from skills_sdk.space.kiro.generator import KiroCatalogSkill

workspace = KiroWorkspace(
    name="time-tracking-fastapi",
    description="Full-stack FastAPI template with time tracking feature",
    agents=[
        KiroAgent(
            name="dev",
            description="Full-stack developer",
            prompt="file://prompts/dev.md",
            tools=["code", "bash", "browser"],
        ),
    ],
    skills=[
        KiroCatalogSkill(name="dataart-aila/skills/sdlc-discovery-design-business"),
        KiroCatalogSkill(name="dataart-aila/skills/sdlc-implementation"),
    ],
)

if __name__ == "__main__":
    workspace.run_cli()
