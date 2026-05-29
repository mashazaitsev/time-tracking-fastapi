# SDLC Discovery & Design — Business

Business stakeholder extension of `sdlc-discovery-design`. Adds business dimension overlays to requirements, design, planning, and deliverables.

## Relationship to sdlc-discovery-design

**This skill extends `sdlc-discovery-design`** with business-specific focus:
- Stakeholder-centric requirements clarification
- Business design patterns (ROI, process integration, organizational impact)
- Change management and readiness planning
- Business deliverable templates (business case, stakeholder comms)

**Use together:** Load `sdlc-discovery-design` from the Artisyn Catalog as the base process, then apply business overlays from this skill at the relevant steps.

## Quick Start

**What it does:** Adds business dimension to the 9-step discovery-design process

**When to use:**
- "Run business SDLC for [project]"
- "Design [project] with business focus"
- "Business requirements for [initiative]"

---

## Business Overlays

Apply these at the corresponding `sdlc-discovery-design` steps:

### Step 3: Requirements Clarification → Business Focus

See [requirements-clarification-business.md](references/requirements-clarification-business.md)

**Adds:**
- Stakeholder-centric questions (who decides, who benefits, who's impacted)
- Business objectives and success metrics
- Value proposition and ROI framing
- Organizational constraints and dependencies

### Step 6: Detailed Design → Business Focus

See [create-detailed-design-business.md](references/create-detailed-design-business.md)

**Adds:**
- Business process integration design
- Stakeholder value mapping
- Organizational impact assessment
- Business continuity considerations

### Step 8: Implementation Plan → Business Focus

See [develop-implementation-plan-business.md](references/develop-implementation-plan-business.md)

**Adds:**
- Stakeholder readiness and change management
- Business value realization timeline
- Training and adoption planning
- Risk assessment from business perspective

### Step 10: Generate Deliverables → Business Focus

See [generate-deliverable-documents-business.md](references/generate-deliverable-documents-business.md)

**Adds:**
- Business case document
- Stakeholder communication plan
- Executive summary / decision brief
- ROI projection and success criteria

---

## Execution Pattern

**Before starting:**
**ALWAYS** Load parent skill `sdlc-discovery-design` from the Artisyn Catalog. This skill is an extension and MUST be used together with the parent skill.

**For each step:**
1. Follow `sdlc-discovery-design` step instructions
2. At steps 3, 6, 8, 10 — additionally load the business overlay reference
3. Apply business-specific questions/templates alongside the generic process
4. Save business-focused artifacts to project directory

---

## Usage

```
"Run business SDLC for project customer-analytics-dashboard"
"Apply business requirements focus to step 3"
"Generate business deliverables for this project"
```
