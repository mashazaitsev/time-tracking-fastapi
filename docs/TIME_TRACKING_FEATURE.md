# Time Tracking Feature — Documentation

## Overview

This feature adds **Projects** and **Time Entries** to the FastAPI template. Users can create projects, log time against them, and see a summary of hours worked per project on the dashboard.

---

## What Was Added

### Backend (Python/FastAPI)

#### 1. Data Models (`backend/app/models.py`)

Added two new database tables and their schemas:

**Project** — a named container for time entries
- Fields: id, name, description, owner_id, created_at
- Belongs to a User (owner)
- Has many Time Entries (cascade delete — deleting a project removes its entries)

**TimeEntry** — a record of time spent on a project
- Fields: id, project_id, owner_id, date, duration_minutes, description, created_at
- Belongs to a User (owner) AND a Project
- project_id must reference an existing project owned by the same user

**Summary schemas** (no database table):
- `ProjectSummary` — one project's total minutes
- `TimeSummary` — total minutes + list of per-project breakdowns

#### 2. API Endpoints

**Projects** (`backend/app/api/routes/projects.py`):
| Method | URL | What it does |
|--------|-----|-------------|
| GET | /api/v1/projects/ | List user's projects (paginated) |
| POST | /api/v1/projects/ | Create a project |
| GET | /api/v1/projects/{id} | Get one project |
| PUT | /api/v1/projects/{id} | Update a project |
| DELETE | /api/v1/projects/{id} | Delete a project (cascades to time entries) |

**Time Entries** (`backend/app/api/routes/time_entries.py`):
| Method | URL | What it does |
|--------|-----|-------------|
| GET | /api/v1/time-entries/summary | Total hours per project (aggregated) |
| GET | /api/v1/time-entries/ | List user's time entries (paginated) |
| POST | /api/v1/time-entries/ | Log a new time entry |
| GET | /api/v1/time-entries/{id} | Get one time entry |
| PUT | /api/v1/time-entries/{id} | Update a time entry |
| DELETE | /api/v1/time-entries/{id} | Delete a time entry |

All endpoints enforce ownership — regular users only see/modify their own data. Superusers see everything.

#### 3. Database Migration (`backend/app/alembic/versions/3a8f2c1d4e5b_...py`)

Creates the `project` and `timeentry` tables in PostgreSQL with proper foreign keys and cascade delete rules.

#### 4. Router Registration (`backend/app/api/main.py`)

Two lines added to plug in the new routers:
```python
api_router.include_router(projects.router)
api_router.include_router(time_entries.router)
```

#### 5. Tests (`backend/tests/`)

- `tests/api/routes/test_projects.py` — 11 tests covering all CRUD + permission checks
- `tests/api/routes/test_time_entries.py` — 16 tests covering CRUD + validation + summary + cascade delete
- `tests/utils/project.py` — helper to create test projects
- `tests/utils/time_entry.py` — helper to create test time entries

---

### Frontend (TypeScript/React)

#### 1. Projects Page (`frontend/src/routes/_layout/projects.tsx`)

A data table showing the user's projects with add/edit/delete actions.

Components in `frontend/src/components/Projects/`:
- `columns.tsx` — table column definitions
- `AddProject.tsx` — create dialog (name + description)
- `EditProject.tsx` — edit dialog
- `DeleteProject.tsx` — delete confirmation
- `ProjectActionsMenu.tsx` — dropdown menu per row
- `PendingProjects.tsx` — loading skeleton

#### 2. Time Entries Page (`frontend/src/routes/_layout/time-entries.tsx`)

A data table showing the user's time entries with add/edit/delete actions.

Components in `frontend/src/components/TimeEntries/`:
- `columns.tsx` — table columns + `formatDuration()` utility (converts minutes to "Xh Ym")
- `AddTimeEntry.tsx` — create dialog (project dropdown, date, duration, description)
- `EditTimeEntry.tsx` — edit dialog
- `DeleteTimeEntry.tsx` — delete confirmation
- `TimeEntryActionsMenu.tsx` — dropdown menu per row
- `PendingTimeEntries.tsx` — loading skeleton

#### 3. Dashboard Widget (`frontend/src/components/Dashboard/TimeSummaryWidget.tsx`)

Shows total hours logged and per-project breakdown on the home page. Handles loading, empty, and populated states.

#### 4. Sidebar Navigation (`frontend/src/components/Sidebar/AppSidebar.tsx`)

Added "Projects" and "Time Entries" links with icons.

#### 5. API Client (`frontend/src/client/`)

Added `ProjectsService` and `TimeEntriesService` with TypeScript types matching the backend schemas.

---

## How It All Connects

```
User clicks "Add Time Entry"
    → AddTimeEntry.tsx validates the form (Zod)
    → Calls TimeEntriesService.createTimeEntry() (SDK)
    → HTTP POST to /api/v1/time-entries/ (network)
    → time_entries.py create_time_entry() runs (backend)
    → Checks project exists + user owns it (validation)
    → Saves to PostgreSQL (database)
    → Returns the new entry as JSON (response)
    → Frontend shows success toast + refreshes table
```

---

## Key Design Decisions

1. **Projects are required** — every time entry must belong to a project. This enables grouping and the summary endpoint.
2. **Cascade delete** — deleting a project automatically deletes all its time entries. No orphaned data.
3. **Owner-scoped** — regular users only see their own data. Superusers see everything.
4. **Summary endpoint** — aggregates time at the database level (SQL GROUP BY) rather than fetching all entries and summing in Python. More efficient for large datasets.
5. **Same patterns as Items** — follows the existing codebase conventions exactly so the code is consistent and predictable.
