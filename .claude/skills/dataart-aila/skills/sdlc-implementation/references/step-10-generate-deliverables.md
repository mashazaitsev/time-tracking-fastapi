# SOP_STEP: Generate Deliverable Documents

step_name: generate_deliverable_documents

## Overview

Generate standard organizational deliverable documents based on templates and project artifacts.

## Constraints

- You MUST present the list of supported deliverable documents from dimensional skill to the user
- You MUST ask the user to review and modify the list of deliverables to generate:
  - Select all (generate all standard deliverables)
  - Select specific deliverables (user chooses which ones)
  - Skip deliverables generation (user will create manually)
- You MUST create a generation plan listing selected deliverables in order
- You MUST generate deliverables one at a time in the planned order
- You MUST use templates provided by dimensional skill for each deliverable
- You MUST populate templates with information from project artifacts:
  - Requirements from {project_name}/clarification.md
  - Research findings from {project_name}/research/
  - Design from {project_name}/design/detailed-design.md
  - Implementation plan from {project_name}/implementation/plan.md
- You MUST save generated deliverables to {project_name}/deliverables/ directory
- You MUST create {project_name}/deliverables/ directory if it doesn't exist
- You MUST review each generated deliverable with the user before proceeding to next
- You MUST allow user to request modifications to generated deliverables
- You MUST update the generation plan checklist as deliverables are completed
- You SHOULD explain the purpose of each deliverable before generating it
- You SHOULD highlight any missing information needed for a deliverable
- You MAY suggest skipping deliverables that are not applicable to the project
- You MUST NOT proceed to next deliverable without user confirmation of current deliverable

## Troubleshooting

### Missing Information
If information needed for a deliverable is not available in project artifacts:
- You MUST inform the user about missing information
- You SHOULD suggest where to find or how to obtain the information
- You MAY suggest using placeholder text with clear markers (e.g., [TO BE DETERMINED])
- You MAY suggest returning to earlier steps to gather missing information
