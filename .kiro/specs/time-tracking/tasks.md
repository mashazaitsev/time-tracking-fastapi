# Implementation Plan: Time Tracking

## Overview

Implement time tracking end-to-end following the existing Items pattern: SQLModel models + Alembic migration, FastAPI CRUD routes, pytest integration tests, then React/TanStack frontend pages and components. Implementation proceeds in four phases: backend models → backend routes → backend tests → frontend.

---

## Tasks

- [x] 1. Backend models — SQLModel tables, schemas, and Alembic migration
  - [x] 1.1 Add `Project` and `TimeEntry` table classes and all schemas to `backend/app/models.py`
    - Append `ProjectBase`, `ProjectCreate`, `ProjectUpdate`, `Project` (table=True), `ProjectPublic`, `ProjectsPublic` following the Item pattern
    - Append `TimeEntryBase`, `TimeEntryCreate`, `TimeEntryUpdate`, `TimeEntry` (table=True), `TimeEntryPublic`, `TimeEntriesPublic`
    - Append `ProjectSummary` and `TimeSummary` response schemas (no table)
    - Add `projects` and `time_entries` relationships to the existing `User` model with `cascade_delete=True`
    - `Project.owner_id` FK → `user.id` with `ondelete="CASCADE"`; `TimeEntry.project_id` FK → `project.id` with `ondelete="CASCADE"`; `TimeEntry.owner_id` FK → `user.id` with `ondelete="CASCADE"`
    - Use `get_datetime_utc` factory and `DateTime(timezone=True)` for `created_at` fields, matching existing pattern
    - _Requirements: 1.1, 1.2, 1.3, 1.4, 2.1, 2.2, 2.3_

  - [ ]* 1.2 Write property test for Project creation round-trip (Property 1)
    - **Property 1: Project creation round-trip**
    - **Validates: Requirements 3.1, 3.3**
    - Use `hypothesis` or `pytest` parametrize with generated valid `ProjectCreate` payloads; assert returned `name`, `description`, and `owner_id` match input after create + fetch

  - [ ]* 1.3 Write property test for owner-scoped project list (Property 2)
    - **Property 2: Owner-scoped project list**
    - **Validates: Requirements 3.2**
    - Create projects under two distinct users; assert each user's list contains only their own `owner_id`

  - [x] 1.4 Generate Alembic migration for `project` and `timeentry` tables
    - Run `alembic revision --autogenerate -m "add_project_and_timeentry_tables"` inside `backend/`
    - Verify the generated migration in `backend/app/alembic/versions/` creates both tables with correct columns, FK constraints, and cascade rules
    - _Requirements: 1.1, 2.1_

- [x] 2. Backend routes — projects router, time entries router, register in main.py
  - [x] 2.1 Create `backend/app/api/routes/projects.py`
    - Implement `GET /` — paginated `ProjectsPublic`, owner-scoped for normal users, all for superusers
    - Implement `POST /` — create project with `owner_id = current_user.id`, return `ProjectPublic` HTTP 200
    - Implement `GET /{id}` — fetch by ID, raise 404 before 403
    - Implement `PUT /{id}` — partial update via `model_copy(update=...)`, raise 404 before 403
    - Implement `DELETE /{id}` — delete and return `Message`, raise 404 before 403
    - _Requirements: 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 3.8, 3.9, 3.10_

  - [ ]* 2.2 Write property test for 404-before-403 on project access (Property 3)
    - **Property 3: 404 before 403 on project access**
    - **Validates: Requirements 3.5, 3.7**
    - For any random UUID not in the DB, assert GET/PUT/DELETE returns 404 regardless of the requesting user

  - [x] 2.3 Create `backend/app/api/routes/time_entries.py`
    - Register `GET /summary` **first** (before `GET /{id}`) to prevent FastAPI treating `"summary"` as a UUID
    - `GET /summary` — aggregate `func.sum(duration_minutes)` + `group_by(project_id)` joined with Project for `project_name`; owner-scoped or all for superusers; return `TimeSummary` with `total_minutes=0` and `by_project=[]` when no entries exist
    - `GET /` — paginated `TimeEntriesPublic`, owner-scoped or all for superusers
    - `POST /` — validate `project_id` exists (404) and is owned by current user or user is superuser (403); create with `owner_id = current_user.id`; return `TimeEntryPublic` HTTP 200
    - `GET /{id}` — fetch by ID, raise 404 before 403
    - `PUT /{id}` — partial update, raise 404 before 403
    - `DELETE /{id}` — delete and return `Message`, raise 404 before 403
    - _Requirements: 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 4.8, 4.9, 4.10, 4.11, 5.1, 5.2, 5.3_

  - [ ]* 2.4 Write property test for time entry creation round-trip (Property 4)
    - **Property 4: Time entry creation round-trip**
    - **Validates: Requirements 4.1**
    - For generated valid `TimeEntryCreate` payloads, assert fetched entry fields match creation input exactly

  - [ ]* 2.5 Write property test for summary total equals sum of entries (Property 5)
    - **Property 5: Summary total equals sum of entries**
    - **Validates: Requirements 5.1, 5.2**
    - Create N entries with known `duration_minutes`; assert `summary.total_minutes == sum(duration_minutes)`

  - [ ]* 2.6 Write property test for summary by_project aggregation (Property 6)
    - **Property 6: Summary by_project aggregation correctness**
    - **Validates: Requirements 5.1**
    - Distribute entries across multiple projects; assert each `by_project` entry's `total_minutes` equals the per-project sum and every project with entries appears in the list

  - [ ]* 2.7 Write property test for project cascade deletes time entries (Property 7)
    - **Property 7: Project cascade deletes time entries**
    - **Validates: Requirements 1.3**
    - Create project + entries; delete project; assert all associated time entries are absent from DB

  - [x] 2.8 Register routers in `backend/app/api/main.py`
    - Add `from app.api.routes import projects, time_entries`
    - Add `api_router.include_router(projects.router, prefix="/projects", tags=["projects"])`
    - Add `api_router.include_router(time_entries.router, prefix="/time-entries", tags=["time-entries"])`
    - _Requirements: 3.1, 4.1_

- [x] 3. Checkpoint — backend routes complete
  - Ensure all tests pass, ask the user if questions arise.

- [x] 4. Backend tests — pytest integration tests
  - [x] 4.1 Create `backend/tests/api/routes/test_projects.py`
    - `test_create_project` — POST valid payload, assert 200 + all fields
    - `test_read_project` — GET by ID as superuser, assert fields
    - `test_read_project_not_found` — GET random UUID, assert 404
    - `test_read_project_not_enough_permissions` — GET by non-owner normal user, assert 403
    - `test_read_projects` — GET list as superuser, assert count ≥ created
    - `test_update_project` — PUT valid payload, assert 200 + updated fields
    - `test_update_project_not_found` — PUT random UUID, assert 404
    - `test_update_project_not_enough_permissions` — PUT by non-owner, assert 403
    - `test_delete_project` — DELETE as owner, assert 200 + message
    - `test_delete_project_not_found` — DELETE random UUID, assert 404
    - `test_delete_project_not_enough_permissions` — DELETE by non-owner, assert 403
    - Follow fixture and client patterns from `tests/api/routes/test_items.py`
    - _Requirements: 6.1, 6.2, 6.3_

  - [x] 4.2 Create `backend/tests/api/routes/test_time_entries.py`
    - Full CRUD matrix matching `test_projects.py` structure (create, read single, read list, update, delete — including 403 and 404 variants)
    - `test_create_time_entry_project_not_found` — POST with non-existent `project_id`, assert 404
    - `test_create_time_entry_project_not_owned` — POST with another user's `project_id`, assert 403
    - `test_get_summary_correct_totals` — create known entries, GET `/summary`, assert `total_minutes` and `by_project` values
    - `test_get_summary_empty` — user with no entries, assert `total_minutes=0` and `by_project=[]`
    - `test_delete_project_cascades_time_entries` — create project + entries, DELETE project, query DB directly and assert entries are gone
    - _Requirements: 6.1, 6.2, 6.3, 6.4, 6.5_

- [x] 5. Checkpoint — backend tests complete
  - Ensure all tests pass, ask the user if questions arise.

- [x] 6. Frontend — Projects components and route
  - [x] 6.1 Create `frontend/src/components/Projects/` directory with all six components
    - `columns.tsx` — `ColumnDef<ProjectPublic>[]` with name, description, created date (formatted), and actions column using `ProjectActionsMenu`
    - `PendingProjects.tsx` — skeleton table, 5 rows × 4 columns
    - `ProjectActionsMenu.tsx` — dropdown with Edit and Delete items, accepts `ProjectPublic` prop
    - `AddProject.tsx` — dialog with name (required, Zod min-length 1, max 255) and description (optional, max 255); calls `ProjectsService.createProject`; on success: success toast + close + invalidate query; on error: error toast via `handleError`, keep dialog open
    - `EditProject.tsx` — pre-populated dialog; calls `ProjectsService.updateProject`; same success/error pattern
    - `DeleteProject.tsx` — confirmation dialog; calls `ProjectsService.deleteProject`; success toast + refresh on success
    - _Requirements: 7.1, 7.2, 7.3, 7.4, 7.5, 7.6, 7.7, 7.8, 7.9, 7.10_

  - [x] 6.2 Create `frontend/src/routes/_layout/projects.tsx`
    - Use `useSuspenseQuery` for projects list with `ProjectsService.readProjects`
    - Render `<PendingProjects />` as Suspense fallback (loading spinner per Req 7.9)
    - Render data table using `columns.tsx`; when `data.length === 0` render single row with "No projects" (Req 7.10)
    - Render `<AddProject />` button in page header
    - _Requirements: 7.1, 7.9, 7.10_

- [x] 7. Frontend — Time Entries components and route
  - [x] 7.1 Create `frontend/src/components/TimeEntries/` directory with all six components
    - `columns.tsx` — `ColumnDef<TimeEntryPublic>[]` with project name, date, duration formatted as "Xh Ym", description, and actions column
    - `PendingTimeEntries.tsx` — skeleton table, 5 rows × 5 columns
    - `TimeEntryActionsMenu.tsx` — dropdown with Edit and Delete items
    - `AddTimeEntry.tsx` — dialog with project select (from user's projects), date picker, `duration_minutes` (integer input, Zod `min(1)` client-side validation before API call), optional description; calls `TimeEntriesService.createTimeEntry`; success/error pattern matching AddProject
    - `EditTimeEntry.tsx` — pre-populated dialog; calls `TimeEntriesService.updateTimeEntry`
    - `DeleteTimeEntry.tsx` — confirmation dialog; calls `TimeEntriesService.deleteTimeEntry`
    - Implement `formatDuration(minutes: number): string` utility (e.g. `"3h 45m"`) in a shared utils file or within `columns.tsx`
    - _Requirements: 8.1, 8.2, 8.3, 8.4, 8.5, 8.6_

  - [ ]* 7.2 Write property test for duration formatting lossless (Property 8)
    - **Property 8: Duration formatting is lossless**
    - **Validates: Requirements 8.2, 9.1**
    - Use `fast-check`: `fc.integer({ min: 1, max: 10000 })` → `formatDuration(minutes)` → `parseDuration(formatted)` → assert equals original `minutes`; `numRuns: 100`

  - [x] 7.3 Create `frontend/src/routes/_layout/time-entries.tsx`
    - Use `useSuspenseQuery` for time entries list with `TimeEntriesService.readTimeEntries`
    - Render `<PendingTimeEntries />` as Suspense fallback
    - Render data table using `columns.tsx`
    - Render `<AddTimeEntry />` button in page header
    - _Requirements: 8.1, 8.5_

- [x] 8. Frontend — Dashboard widget and sidebar navigation
  - [x] 8.1 Create `frontend/src/components/Dashboard/TimeSummaryWidget.tsx`
    - Use `useQuery` (not `useSuspenseQuery`) so widget failure does not crash the dashboard
    - Loading state: render skeleton matching widget structure (Req 9.3)
    - Empty state (`total_minutes === 0`): render "No time logged yet" + empty breakdown list (Req 9.1, 9.2)
    - Populated state: render formatted total as "Xh Ym" using `formatDuration`; render per-project breakdown list with project name and formatted hours (Req 9.1, 9.2)
    - _Requirements: 9.1, 9.2, 9.3_

  - [x] 8.2 Add sidebar navigation links in `frontend/src/components/Sidebar/AppSidebar.tsx`
    - Import `FolderOpen` and `Clock` icons from `lucide-react`
    - Add to `baseItems`: `{ icon: FolderOpen, title: "Projects", path: "/projects" }` and `{ icon: Clock, title: "Time Entries", path: "/time-entries" }`
    - Active link highlighting is handled by existing sidebar behaviour — no additional code needed
    - _Requirements: 10.1, 10.2, 10.3_

  - [x] 8.3 Mount `<TimeSummaryWidget />` in `frontend/src/routes/_layout/index.tsx`
    - Import `TimeSummaryWidget` and render it below the existing greeting section
    - _Requirements: 9.1, 9.2, 9.3_

  - [ ]* 8.4 Write unit tests for `TimeSummaryWidget`
    - Renders "No time logged yet" when `total_minutes === 0`
    - Renders formatted total and project list when populated
    - Renders skeleton during loading state
    - _Requirements: 9.1, 9.2, 9.3_

  - [ ]* 8.5 Write unit tests for `AddProject` and `AddTimeEntry` dialogs
    - `AddProject`: renders correctly, validates empty name, calls `createProject` on valid submit
    - `AddTimeEntry`: rejects `duration_minutes < 1` before API call
    - _Requirements: 7.2, 7.4, 8.2, 8.4_

- [x] 9. Final checkpoint — Ensure all tests pass
  - Ensure all tests pass, ask the user if questions arise.

---

## Notes

- Tasks marked with `*` are optional and can be skipped for a faster MVP
- Each task references specific requirements for traceability
- The `GET /summary` route **must** be registered before `GET /{id}` in `time_entries.py` to prevent FastAPI treating the literal string `"summary"` as a UUID path parameter
- Frontend client code (`ProjectsService`, `TimeEntriesService`) is auto-generated via `openapi-ts` after backend routes are registered — regenerate the client before starting task 6
- Property tests 1–7 are backend pytest tests (tasks 1.2, 1.3, 2.2, 2.4–2.7); Property 8 is a frontend fast-check test (task 7.2)
- Checkpoints at tasks 3, 5, and 9 ensure incremental validation between phases

---

## Task Dependency Graph

```json
{
  "waves": [
    { "id": 0, "tasks": ["1.1"] },
    { "id": 1, "tasks": ["1.2", "1.3", "1.4"] },
    { "id": 2, "tasks": ["2.1", "2.3"] },
    { "id": 3, "tasks": ["2.2", "2.4", "2.5", "2.6", "2.7", "2.8"] },
    { "id": 4, "tasks": ["4.1", "4.2"] },
    { "id": 5, "tasks": ["6.1", "7.1"] },
    { "id": 6, "tasks": ["6.2", "7.2", "7.3"] },
    { "id": 7, "tasks": ["8.1", "8.2", "8.3"] },
    { "id": 8, "tasks": ["8.4", "8.5"] }
  ]
}
```
