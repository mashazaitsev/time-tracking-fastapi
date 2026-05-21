# Session Report: Full Stack FastAPI Template

request: I need to add a new resource type called 'projects' with the same patterns as items but with additional fields. What files do I need to modify and what patterns should I follow?

**Date:** 2026-03-24  
**Repository:** `/home/olegk/aila/z_practice_repos/full-stack-fastapi-template`

---

## 1. Codebase Analysis

### Overview

Full Stack FastAPI Template — a production-ready starter for building web applications with:

- **Backend:** Python/FastAPI, SQLModel ORM, PostgreSQL, JWT auth, Alembic migrations
- **Frontend:** React, TypeScript, Vite, Tailwind CSS, shadcn/ui, TanStack Router/Query
- **DevOps:** Docker Compose, Traefik proxy, GitHub Actions CI/CD, Copier scaffolding

### Codebase Stats

- **Total files:** 260
- **Lines of code:** ~12,666
- **Functions:** 333
- **Classes/Models:** 31

### Key Files Discovered

#### Backend — Core

| File | Purpose |
|---|---|
| `backend/app/models.py` | SQLModel models: User, Item, and all Pydantic schemas (UserBase, UserCreate, UserPublic, ItemBase, ItemCreate, ItemPublic, etc.) |
| `backend/app/crud.py` | CRUD operations: create_user, update_user, get_user_by_email, authenticate, create_item |
| `backend/app/main.py` | FastAPI app entry point, CORS config, OpenAPI customization |
| `backend/app/core/config.py` | Settings class (Pydantic), env var loading, CORS parsing, secret validation |
| `backend/app/core/security.py` | JWT token creation, password hashing (Argon2), password verification |
| `backend/app/core/db.py` | Database engine setup, init_db (creates first superuser) |
| `backend/app/utils.py` | Email utilities: send_email, render templates, password reset tokens |
| `backend/app/initial_data.py` | Seeds first superuser on startup |
| `backend/app/backend_pre_start.py` | Waits for DB readiness before starting |

#### Backend — API Routes

| File | Endpoints |
|---|---|
| `backend/app/api/main.py` | Router registration: login, users, utils, items, private |
| `backend/app/api/deps.py` | Dependencies: get_db, get_current_user, get_current_active_superuser |
| `backend/app/api/routes/login.py` | POST /login, POST /recover-password, POST /reset-password, POST /test-token |
| `backend/app/api/routes/users.py` | Full user CRUD: GET/POST/PUT/DELETE /users, /users/me, /users/{id} |
| `backend/app/api/routes/items.py` | Full item CRUD: GET/POST/PUT/DELETE /items, /items/{id} |
| `backend/app/api/routes/private.py` | Private admin endpoint (local env only) |
| `backend/app/api/routes/utils.py` | Health check, test email |

#### Backend — Migrations

| File | Migration |
|---|---|
| `e2412789c190_initialize_models.py` | Initial User + Item tables |
| `9c0a54914c78_add_max_length_...py` | String field max lengths |
| `d98dd8ec85a3_edit_replace_id_...py` | Integer IDs → UUIDs |
| `1a31ce608336_add_cascade_delete...py` | Cascade delete relationships |
| `fe56fa70289e_add_created_at_...py` | created_at timestamps |

#### Frontend — Core

| File | Purpose |
|---|---|
| `frontend/src/main.tsx` | React app entry, router setup, QueryClient |
| `frontend/src/routeTree.gen.ts` | Auto-generated route tree |
| `frontend/src/utils.ts` | Error message extraction |
| `frontend/src/hooks/useAuth.ts` | Auth hook: login, logout, current user |

#### Frontend — Routes (Pages)

| File | Page |
|---|---|
| `frontend/src/routes/login.tsx` | Login page |
| `frontend/src/routes/signup.tsx` | Sign up page |
| `frontend/src/routes/recover-password.tsx` | Password recovery |
| `frontend/src/routes/reset-password.tsx` | Password reset |
| `frontend/src/routes/_layout.tsx` | Authenticated layout wrapper |
| `frontend/src/routes/_layout/index.tsx` | Dashboard |
| `frontend/src/routes/_layout/items.tsx` | Items page (table + CRUD) |
| `frontend/src/routes/_layout/admin.tsx` | Admin page (user management) |
| `frontend/src/routes/_layout/settings.tsx` | User settings |

#### Frontend — Components

| Directory | Components |
|---|---|
| `frontend/src/components/Items/` | AddItem, EditItem, DeleteItem, columns, ItemActionsMenu |
| `frontend/src/components/Admin/` | AddUser, EditUser, DeleteUser, columns, UserActionsMenu |
| `frontend/src/components/UserSettings/` | UserInformation, ChangePassword, DeleteAccount, DeleteConfirmation |
| `frontend/src/components/Sidebar/` | AppSidebar, Main (nav), User (footer) |
| `frontend/src/components/Common/` | DataTable, Logo, Footer, AuthLayout, Appearance, NotFound, ErrorComponent |
| `frontend/src/components/Pending/` | PendingUsers, PendingItems (loading skeletons) |
| `frontend/src/components/ui/` | shadcn/ui components (button, dialog, form, table, sidebar, etc.) |

#### Frontend — Generated API Client

| File | Purpose |
|---|---|
| `frontend/src/client/sdk.gen.ts` | Auto-generated service classes: ItemsService, UsersService, LoginService, PrivateService, UtilsService |
| `frontend/src/client/types.gen.ts` | Auto-generated TypeScript types from OpenAPI schema |
| `frontend/src/client/schemas.gen.ts` | Auto-generated Zod schemas |
| `frontend/src/client/core/` | HTTP client core: request handling, error classes, interceptors, cancellable promises |

#### Configuration & Scripts

| File | Purpose |
|---|---|
| `.env` | All environment variables (DB, auth, SMTP, CORS, etc.) |
| `compose.yml` | Docker Compose main config |
| `compose.override.yml` | Dev overrides (volume mounts, live reload) |
| `compose.traefik.yml` | Traefik proxy config for production |
| `scripts/generate-client.sh` | Regenerates frontend API client from OpenAPI spec |
| `scripts/test.sh` | Runs backend tests |
| `scripts/test-local.sh` | Runs tests locally |
| `backend/scripts/prestart.sh` | Pre-start: runs migrations + initial data |
| `backend/scripts/lint.sh` | Ruff linting |
| `backend/scripts/format.sh` | Ruff formatting |

#### Tests

| Directory | Coverage |
|---|---|
| `backend/tests/api/routes/` | test_login, test_users (27 tests), test_items (11 tests), test_private |
| `backend/tests/crud/` | test_user (10 tests) |
| `backend/tests/scripts/` | test_backend_pre_start, test_test_pre_start |
| `frontend/tests/` | Playwright E2E: login, sign-up, admin, items, user-settings, reset-password |

---

## 2. Actions Performed

### 2.1 Local Environment Setup (No Docker)

#### System Check Results

| Tool | Status |
|---|---|
| `uv` | ✅ Installed (v0.9.26) |
| `node` / `npm` | ✅ Installed (v24.12.0 / v11.6.2) |
| `python3` | ✅ Installed (3.12.3) |
| `bun` | ❌ Not installed (npm used as alternative) |
| `PostgreSQL` | ❌ Not installed |

#### PostgreSQL Installation

```
$ sudo apt-get update -qq && sudo apt-get install -y -qq postgresql postgresql-client
Setting up postgresql (16+257build1.1) ...
```

#### Database Setup

```
$ sudo systemctl start postgresql
$ sudo -u postgres psql -c "CREATE DATABASE app;"
CREATE DATABASE
$ sudo -u postgres psql -c "ALTER USER postgres PASSWORD 'changethis';"
ALTER ROLE
```

PostgreSQL `pg_hba.conf` confirmed: host connections use `scram-sha-256` (password auth works).

#### Backend Dependencies

```
$ cd backend && uv sync
+ urllib3==2.6.3
+ uvicorn==0.40.0
+ uvloop==0.22.1
+ watchfiles==1.1.1
+ websockets==16.0
```

#### Database Migrations

```
$ uv run alembic upgrade head
INFO  [alembic.runtime.migration] Running upgrade  -> e2412789c190, Initialize models
INFO  [alembic.runtime.migration] Running upgrade e2412789c190 -> 9c0a54914c78, Add max length for string(varchar) fields
INFO  [alembic.runtime.migration] Running upgrade 9c0a54914c78 -> d98dd8ec85a3, Edit replace id integers to use UUID
INFO  [alembic.runtime.migration] Running upgrade d98dd8ec85a3 -> 1a31ce608336, Add cascade delete relationships
INFO  [alembic.runtime.migration] Running upgrade 1a31ce608336 -> fe56fa70289e, Add created_at to User and Item
```

#### Initial Data Seeding

```
$ uv run python app/initial_data.py
INFO:__main__:Creating initial data
INFO:__main__:Initial data created
```

#### Frontend Dependencies

```
$ cd frontend && npm install
(completed successfully)
```

#### Service Startup

```
Backend:  http://localhost:8000 ✅ (health check returned true)
Frontend: http://localhost:5173 ✅ (Vite v7.3.1 ready in 1188ms)
```

Note: Port 5173 was initially occupied by a stale process. Killed it and restarted frontend on correct port.

### 2.2 Files Created

#### `bootstrap.md` (project root)

Agent-friendly bootstrap instructions for workshop attendees covering:
- Prerequisites check (Python 3.10+, uv, Node.js 18+, PostgreSQL 14+)
- Install commands for each missing dependency
- PostgreSQL database creation
- Backend dependency install + migrations + seeding
- Frontend dependency install
- Start/stop via scripts
- Troubleshooting section

#### `scripts/start.sh`

Starts all services in order: PostgreSQL → Backend → Frontend

Features:
- Port conflict detection (kills stale processes on 8000/5173)
- Health check polling (up to 30s timeout per service)
- Logs to `/tmp/fastapi-template/`
- PID file tracking
- Clean status output with emoji indicators

Test output:
```
🚀 Starting Full Stack FastAPI Template...
📦 Starting PostgreSQL...
✅ PostgreSQL is running
📦 Starting Backend...
   Waiting for backend...
✅ Backend is running at http://localhost:8000
📦 Starting Frontend...
   Waiting for frontend...
✅ Frontend is running at http://localhost:5173

=========================================
  All services running!
=========================================
  Frontend:     http://localhost:5173
  Backend API:  http://localhost:8000
  Swagger Docs: http://localhost:8000/docs

  Login: admin@example.com / changethis

  Logs: /tmp/fastapi-template/
  Stop: bash scripts/stop.sh
=========================================
```

#### `scripts/stop.sh`

Stops all services in reverse order: Frontend → Backend → PostgreSQL

Test output:
```
🛑 Stopping Full Stack FastAPI Template...
✅ Frontend stopped
✅ Backend stopped
✅ PostgreSQL stopped

All services stopped.
```

### 2.3 Adding a "Projects" Resource — Analysis

Provided a complete blueprint for adding a new `projects` resource following the existing `items` pattern. No files were created — analysis only.

#### Backend changes (4 files + migration)

| File | Action |
|---|---|
| `backend/app/models.py` | Add 6 classes: ProjectBase, ProjectCreate, ProjectUpdate, Project (table), ProjectPublic, ProjectsPublic. Add `projects` relationship to User model. |
| `backend/app/api/routes/projects.py` | Create new file — 5 endpoints (list, get, create, update, delete) following items.py pattern |
| `backend/app/api/main.py` | Register `projects.router` |
| Alembic | `alembic revision --autogenerate` + `alembic upgrade head` |

#### Frontend changes (7 new files, 2 modified)

| File | Action |
|---|---|
| `frontend/src/components/Projects/AddProject.tsx` | Create (copy AddItem pattern + extra fields) |
| `frontend/src/components/Projects/EditProject.tsx` | Create (copy EditItem pattern) |
| `frontend/src/components/Projects/DeleteProject.tsx` | Create (copy DeleteItem pattern) |
| `frontend/src/components/Projects/columns.tsx` | Create (copy Items/columns + new columns) |
| `frontend/src/components/Projects/ProjectActionsMenu.tsx` | Create (copy ItemActionsMenu) |
| `frontend/src/components/Pending/PendingProjects.tsx` | Create (copy PendingItems) |
| `frontend/src/routes/_layout/projects.tsx` | Create (copy items.tsx route page) |
| `frontend/src/components/Sidebar/AppSidebar.tsx` | Modify — add Projects nav entry |
| Regenerate client | `bash scripts/generate-client.sh` |

---

## 3. Default Credentials

| Setting | Value |
|---|---|
| Superuser email | `admin@example.com` |
| Superuser password | `changethis` |
| PostgreSQL database | `app` |
| PostgreSQL user | `postgres` |
| PostgreSQL password | `changethis` |
| Secret key | `changethis` |

⚠️ All default to `changethis` — must be changed for any non-local deployment.

---

## 4. Service URLs

| Service | URL |
|---|---|
| Frontend | http://localhost:5173 |
| Backend API | http://localhost:8000 |
| Swagger Docs | http://localhost:8000/docs |
| ReDoc | http://localhost:8000/redoc |

(Adminer on :8080, Traefik on :8090, Mailcatcher on :1080 — Docker only)

---

## 5. Technology Stack

| Layer | Technology |
|---|---|
| Backend framework | FastAPI |
| ORM | SQLModel (SQLAlchemy + Pydantic) |
| Database | PostgreSQL 16 |
| Migrations | Alembic |
| Auth | JWT (python-jose), Argon2 password hashing |
| Frontend framework | React 19 |
| Frontend language | TypeScript |
| Build tool | Vite 7 |
| CSS | Tailwind CSS |
| UI components | shadcn/ui |
| Routing | TanStack Router |
| Data fetching | TanStack Query |
| API client | Auto-generated from OpenAPI spec |
| E2E tests | Playwright |
| Backend tests | Pytest |
| Package manager (backend) | uv |
| Package manager (frontend) | Bun / npm |
| Containerization | Docker Compose |
| Reverse proxy | Traefik |
| CI/CD | GitHub Actions |
| Scaffolding | Copier |

 ▸ Time: 57s