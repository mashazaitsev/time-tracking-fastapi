# Agent Assignment: Time Tracking Feature

## Epic

AWSP-114 — Time Tracking Feature for Full-Stack FastAPI Template

## Your Task

Read the epic and all linked stories from JIRA (AWSP-114 through AWSP-121). Plan and orchestrate implementation by delegating to specialist subagents.

## How to Work

You are the orchestrator. You do NOT implement code directly. You delegate to specialist subagents:

- **backend-py** — implements all Python/FastAPI code (models, routes, CRUD, tests)
- **frontend-ts** — implements all React/TypeScript code (components, routes, hooks)

For each story:
1. Read the JIRA acceptance criteria
2. Delegate to the appropriate subagent with clear instructions
3. Include the acceptance criteria in your delegation prompt
4. After subagent completes, verify the output (check files exist, run tests)
5. Move to next story

## Principles for Subagents

Include these in every delegation prompt:
- Follow existing codebase patterns exactly — KNOW.md is loaded, use it
- Do not invent new patterns — reuse what's already in the codebase
- Write unit tests for backend endpoints following existing test patterns
- Run tests after implementation to verify

## Implementation Order

1. Read all stories from JIRA epic AWSP-114
2. Create implementation plan
3. Delegate AWSP-115 to **backend-py** (models + migration)
4. Delegate AWSP-116 to **backend-py** (project routes + tests)
5. Delegate AWSP-117 to **backend-py** (time entry routes + tests)
6. Verify: run all backend tests
7. Delegate AWSP-121 to **frontend-ts** (sidebar navigation)
8. Delegate AWSP-118 to **frontend-ts** (projects page)
9. Delegate AWSP-119 to **frontend-ts** (time entry page)
10. Delegate AWSP-120 to **frontend-ts** (dashboard)

Backend stories (3-5) can be delegated sequentially — each depends on the previous.
Frontend stories (7-10) can be delegated in parallel after backend is complete.

## What Subagents Already Know

The subagents have KNOW.md loaded with complete codebase metadata. They know all patterns, file conventions, and import styles. You do not need to explain the codebase to them — just give them the acceptance criteria and tell them to implement.

## Start

Read JIRA epic AWSP-114 and begin.

---

## Post-Implementation Notes / Learnings

These notes are from actual execution of this assignment. Apply them to avoid known pitfalls.

### 1. Fix recover-password.tsx BEFORE Starting Frontend

`frontend/src/routes/recover-password.tsx` has a pre-existing bug — `z.object({` is unclosed. This crashes Vite's TanStack Router code-splitter and blocks ALL routes, not just recover-password. Fix it before any frontend work:

```typescript
// Line 33-35: Replace broken code
const formSchema = z.object({
  email: z.string().email(),
})
```

### 2. Backend Subagents Must NOT Run `alembic upgrade`

Tell backend-py to generate the migration only (`alembic revision --autogenerate`), NOT apply it (`alembic upgrade head`). Migrations should be applied once, manually, after all models are in place. If a subagent runs upgrade and it fails, the migration state gets corrupted.

### 3. Regenerate Frontend Client BEFORE Frontend Stories

After all backend stories are complete, run `npm run generate-client` in the frontend directory ONCE. This generates TypeScript types and service classes from the OpenAPI spec. Frontend subagents need these types to exist. Include this instruction in the first frontend delegation.

### 4. IPv6 localhost Issue

On systems where `localhost` resolves to `::1` (IPv6), the browser cannot reach uvicorn (which binds IPv4 only). Symptoms: browser shows 404, but `curl http://localhost:8000/...` works fine.

**Fix before starting the app:**
- `frontend/.env`: change `VITE_API_URL=http://127.0.0.1:8000`
- `.env`: add `http://127.0.0.1:5173` to `BACKEND_CORS_ORIGINS`
- Access the app at `http://127.0.0.1:5173`, not `http://localhost:5173`

**Detection:** `getent hosts localhost` — if it shows `::1`, apply the fix.

### 5. Run `init_db` After Migrations

Outside Docker, the superuser is not created automatically. After running `alembic upgrade head`, also run:
```bash
cd backend && uv run python app/initial_data.py
```
Without this, login will fail with "Incorrect email or password".

### 6. Kill Stale Processes Before Starting

Repeated starts/stops leave orphan processes. Always clean up first:
```bash
lsof -ti:8000 -ti:5173 | xargs kill -9 2>/dev/null
```

### 7. Clear Vite Cache If Errors Don't Match Code

If Vite shows errors for code you've already fixed, the TanStack Router generator cached the old version at startup:
```bash
cd frontend && rm -rf node_modules/.vite
```
Then restart Vite.

### 8. Verify Backend Routes Before Frontend

After starting the backend, confirm all routes are registered:
```bash
curl -s http://127.0.0.1:8000/api/v1/openapi.json | python3 -c "import sys,json; print(len(json.load(sys.stdin)['paths']), 'routes')"
```
Expected: 20 routes (including projects and time-entries). If 0, the backend loaded an old version — kill and restart.
