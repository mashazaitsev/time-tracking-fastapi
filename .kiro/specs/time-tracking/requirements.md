# Requirements Document

## Introduction

This feature adds time tracking to the full-stack-fastapi-template application. Users can create projects, log time entries against those projects, view and manage their time logs, and see a dashboard summary of hours worked. The implementation follows the existing Items pattern: SQLModel table definitions, FastAPI CRUD routes, pytest integration tests, and TanStack Router/Query frontend pages.

## Glossary

- **Project**: A named grouping entity that time entries are logged against. Owned by a User.
- **TimeEntry**: A record of time worked, associated with a Project and a User. Contains a duration in minutes, a date, and an optional description.
- **Time_Tracking_API**: The FastAPI backend service providing Projects and TimeEntries endpoints.
- **Time_Tracking_UI**: The React/TanStack frontend providing Projects, Time Entries, and Dashboard pages.
- **Dashboard**: The existing home page (`/_layout/`) extended with a time-tracking summary widget.
- **Summary**: Aggregated statistics — total hours logged, hours per project — computed from TimeEntry records.
- **Owner**: The authenticated User who created a Project or TimeEntry.
- **Superuser**: A User with `is_superuser = True`, who can access all records regardless of ownership.

---

## Requirements

### Requirement 1: Project Data Model

**User Story:** As a developer, I want a Project database model, so that time entries can be associated with named projects.

#### Acceptance Criteria

1. THE Time_Tracking_API SHALL store each Project with a UUID primary key, a name (1–255 characters), an optional description (up to 255 characters), a `created_at` UTC timestamp, and an `owner_id` foreign key referencing the User table.
2. WHEN a User is deleted, THE Time_Tracking_API SHALL cascade-delete all Projects owned by that User.
3. WHEN a Project is deleted, THE Time_Tracking_API SHALL cascade-delete all TimeEntries associated with that Project.
4. THE Time_Tracking_API SHALL expose `ProjectCreate`, `ProjectUpdate`, `ProjectPublic`, and `ProjectsPublic` Pydantic schemas following the same pattern as `ItemCreate`, `ItemUpdate`, `ItemPublic`, and `ItemsPublic`.

---

### Requirement 2: Time Entry Data Model

**User Story:** As a developer, I want a TimeEntry database model, so that users can record time worked against a project.

#### Acceptance Criteria

1. THE Time_Tracking_API SHALL store each TimeEntry with a UUID primary key, a `project_id` foreign key referencing the Project table, an `owner_id` foreign key referencing the User table, a `date` field (calendar date), a `duration_minutes` integer (minimum value 1), an optional description (up to 255 characters), and a `created_at` UTC timestamp.
2. THE Time_Tracking_API SHALL expose `TimeEntryCreate`, `TimeEntryUpdate`, `TimeEntryPublic`, and `TimeEntriesPublic` Pydantic schemas following the same pattern as the Item schemas.
3. THE Time_Tracking_API SHALL expose a `TimeSummary` schema containing `total_minutes` (integer) and a `by_project` list of `{ project_id, project_name, total_minutes }` records.

---

### Requirement 3: Projects CRUD API

**User Story:** As a user, I want to create, read, update, and delete projects, so that I can organise my time entries.

#### Acceptance Criteria

1. WHEN an authenticated User sends `POST /api/v1/projects/` with a valid `ProjectCreate` payload, THE Time_Tracking_API SHALL create the Project with `owner_id` set to the current user and return the created `ProjectPublic` with HTTP 200.
2. WHEN an authenticated User sends `GET /api/v1/projects/`, THE Time_Tracking_API SHALL return a paginated `ProjectsPublic` response containing only Projects owned by that User; WHILE the User is a Superuser, THE Time_Tracking_API SHALL return all Projects.
3. WHEN an authenticated User sends `GET /api/v1/projects/{id}` for a Project they own, THE Time_Tracking_API SHALL return the `ProjectPublic` with HTTP 200.
4. IF an authenticated User sends `GET /api/v1/projects/{id}` for a Project they do not own and the User is not a Superuser, THEN THE Time_Tracking_API SHALL return HTTP 403.
5. IF an authenticated User sends `GET /api/v1/projects/{id}` with a non-existent ID, THEN THE Time_Tracking_API SHALL return HTTP 404.
6. WHEN an authenticated User sends `PUT /api/v1/projects/{id}` with a valid `ProjectUpdate` payload for a Project they own, THE Time_Tracking_API SHALL apply the partial update and return the updated `ProjectPublic` with HTTP 200.
7. IF an authenticated User sends `PUT /api/v1/projects/{id}` with a non-existent ID, THEN THE Time_Tracking_API SHALL return HTTP 404 before performing any ownership check.
8. IF an authenticated User sends `PUT /api/v1/projects/{id}` for a Project they do not own and the User is not a Superuser, THEN THE Time_Tracking_API SHALL return HTTP 403.
9. WHEN an authenticated User sends `DELETE /api/v1/projects/{id}` for a Project they own, THE Time_Tracking_API SHALL delete the Project and return a `Message` confirmation with HTTP 200.
10. IF an authenticated User sends `DELETE /api/v1/projects/{id}` for a Project they do not own and the User is not a Superuser, THEN THE Time_Tracking_API SHALL return HTTP 403.

---

### Requirement 4: Time Entries CRUD API

**User Story:** As a user, I want to create, read, update, and delete time entries, so that I can log and correct my time records.

#### Acceptance Criteria

1. WHEN an authenticated User sends `POST /api/v1/time-entries/` with a valid `TimeEntryCreate` payload, THE Time_Tracking_API SHALL create the TimeEntry with `owner_id` set to the current user and return the created `TimeEntryPublic` with HTTP 200.
2. IF an authenticated User sends `POST /api/v1/time-entries/` referencing a `project_id` that does not exist, THEN THE Time_Tracking_API SHALL return HTTP 404.
3. IF an authenticated User sends `POST /api/v1/time-entries/` referencing a `project_id` owned by a different User and the User is not a Superuser, THEN THE Time_Tracking_API SHALL return HTTP 403.
4. WHEN an authenticated User sends `GET /api/v1/time-entries/`, THE Time_Tracking_API SHALL return a paginated `TimeEntriesPublic` response containing only TimeEntries owned by that User; WHILE the User is a Superuser, THE Time_Tracking_API SHALL return all TimeEntries.
5. WHEN an authenticated User sends `GET /api/v1/time-entries/{id}` for a TimeEntry they own, THE Time_Tracking_API SHALL return the `TimeEntryPublic` with HTTP 200.
6. IF an authenticated User sends `GET /api/v1/time-entries/{id}` for a TimeEntry they do not own and the User is not a Superuser, THEN THE Time_Tracking_API SHALL return HTTP 403.
7. IF an authenticated User sends `GET /api/v1/time-entries/{id}` with a non-existent ID, THEN THE Time_Tracking_API SHALL return HTTP 404.
8. WHEN an authenticated User sends `PUT /api/v1/time-entries/{id}` with a valid `TimeEntryUpdate` payload for a TimeEntry they own, THE Time_Tracking_API SHALL apply the partial update and return the updated `TimeEntryPublic` with HTTP 200.
9. IF an authenticated User sends `PUT /api/v1/time-entries/{id}` for a TimeEntry they do not own and the User is not a Superuser, THEN THE Time_Tracking_API SHALL return HTTP 403.
10. WHEN an authenticated User sends `DELETE /api/v1/time-entries/{id}` for a TimeEntry they own, THE Time_Tracking_API SHALL delete the TimeEntry and return a `Message` confirmation with HTTP 200.
11. IF an authenticated User sends `DELETE /api/v1/time-entries/{id}` for a TimeEntry they do not own and the User is not a Superuser, THEN THE Time_Tracking_API SHALL return HTTP 403.

---

### Requirement 5: Time Summary Endpoint

**User Story:** As a user, I want a summary of my logged hours, so that I can see total time worked and a breakdown by project.

#### Acceptance Criteria

1. WHEN an authenticated User sends `GET /api/v1/time-entries/summary`, THE Time_Tracking_API SHALL return a `TimeSummary` containing the sum of `duration_minutes` across all TimeEntries owned by that User and a `by_project` list with `project_id`, `project_name`, and `total_minutes` for every Project against which that User has ever logged a TimeEntry, including Projects whose current `total_minutes` sum is 0.
2. WHILE the User is a Superuser, THE Time_Tracking_API SHALL compute the summary across all TimeEntries in the system.
3. WHEN an authenticated User has no TimeEntries, THE Time_Tracking_API SHALL return a `TimeSummary` with `total_minutes` equal to 0 and an empty `by_project` list.

---

### Requirement 6: Backend Tests

**User Story:** As a developer, I want pytest tests for the Projects and Time Entries APIs, so that correctness is verified and regressions are caught.

#### Acceptance Criteria

1. THE Time_Tracking_API test suite SHALL include tests for create, read (single and list), update, and delete operations for both Projects and TimeEntries, following the pattern in `tests/api/routes/test_items.py`.
2. THE Time_Tracking_API test suite SHALL verify that HTTP 403 is returned when a non-owner, non-superuser attempts to read, update, or delete a Project or TimeEntry owned by another user.
3. THE Time_Tracking_API test suite SHALL verify that HTTP 404 is returned when a non-existent Project or TimeEntry ID is requested.
4. THE Time_Tracking_API test suite SHALL verify that the summary endpoint returns correct `total_minutes` and `by_project` aggregations for a known set of TimeEntries.
5. WHEN a Project is deleted, THE Time_Tracking_API test suite SHALL delete a Project via the API and then verify that all associated TimeEntries are no longer present in the database (cascade).

---

### Requirement 7: Projects Frontend Page

**User Story:** As a user, I want a Projects page in the UI, so that I can create and manage my projects.

#### Acceptance Criteria

1. THE Time_Tracking_UI SHALL provide a route at `/_layout/projects` that displays a data table of the current user's Projects with columns for name, description, and created date, with inline edit and delete actions on each row.
2. THE Time_Tracking_UI SHALL provide an "Add Project" dialog on the Projects page that accepts a name (required) and description (optional) and, on submit, creates the project and reflects the new entry in the projects list.
3. WHEN a project is successfully created, THE Time_Tracking_UI SHALL display a success toast, close the dialog, and refresh the projects list.
4. IF project creation fails, THE Time_Tracking_UI SHALL display an error toast with the server-provided message and keep the dialog open; success and error feedback are mutually exclusive.
5. THE Time_Tracking_UI SHALL provide an "Edit Project" dialog for each project row that accepts an updated name (required) and description (optional) and, on submit, applies the changes and reflects the updated entry in the projects list.
6. WHEN a project is successfully edited, THE Time_Tracking_UI SHALL display a success toast, close the dialog, and refresh the projects list.
7. IF project editing fails, THE Time_Tracking_UI SHALL display an error toast with the server-provided message and keep the dialog open; success and error feedback are mutually exclusive.
8. WHEN a project is successfully deleted, THE Time_Tracking_UI SHALL display a success toast and refresh the projects list.
9. WHEN the projects list is loading, THE Time_Tracking_UI SHALL display a spinner in place of the table.
10. WHEN the current user has no projects, THE Time_Tracking_UI SHALL display a single row containing the text "No projects" in place of data rows.

---

### Requirement 8: Time Entries Frontend Page

**User Story:** As a user, I want a Time Entries page in the UI, so that I can log and review my time records.

#### Acceptance Criteria

1. THE Time_Tracking_UI SHALL provide a route at `/_layout/time-entries` that displays a data table of the current user's TimeEntries with columns for project name, date, duration (formatted as hours and minutes), and description.
2. THE Time_Tracking_UI SHALL provide an "Add Time Entry" dialog that accepts a project (selected from the user's existing projects), a date, a duration in minutes (minimum 1, validated client-side before the API call is made), and an optional description, and calls `POST /api/v1/time-entries/` on submit.
3. WHEN a time entry is successfully created and the server returns HTTP 200, THE Time_Tracking_UI SHALL display a success toast, close the dialog, and refresh the time entries list.
4. IF time entry creation fails, THE Time_Tracking_UI SHALL display an error toast with the server-provided message and keep the dialog open; success and error feedback are mutually exclusive.
5. THE Time_Tracking_UI SHALL provide inline edit and delete actions for each time entry row.
6. WHEN a time entry is successfully deleted, THE Time_Tracking_UI SHALL display a success toast and refresh the time entries list.

---

### Requirement 9: Dashboard Summary Widget

**User Story:** As a user, I want to see a time tracking summary on the dashboard, so that I can quickly review my total hours and per-project breakdown.

#### Acceptance Criteria

1. THE Time_Tracking_UI Dashboard page SHALL display a summary widget that shows the current user's total hours logged (derived from `total_minutes` in the `TimeSummary` response) formatted as hours and minutes (e.g., "3h 45m"); WHEN `total_minutes` equals 0, THE Time_Tracking_UI Dashboard page SHALL display "No time logged yet" in place of the formatted total.
2. THE Time_Tracking_UI Dashboard page SHALL display a per-project breakdown list showing each project name and its total hours logged; WHEN the user has no time entries, THE Time_Tracking_UI Dashboard page SHALL display an empty breakdown list alongside the "No time logged yet" message.
3. WHEN the `GET /api/v1/time-entries/summary` request is in progress, THE Time_Tracking_UI Dashboard page SHALL display a loading skeleton within the summary widget structure.

---

### Requirement 10: Sidebar Navigation

**User Story:** As a user, I want Projects and Time Entries links in the sidebar, so that I can navigate to those pages from anywhere in the app.

#### Acceptance Criteria

1. THE Time_Tracking_UI sidebar SHALL include a "Projects" navigation link pointing to `/_layout/projects` for all authenticated users.
2. THE Time_Tracking_UI sidebar SHALL include a "Time Entries" navigation link pointing to `/_layout/time-entries` for all authenticated users.
3. THE Time_Tracking_UI sidebar SHALL display the active link in the highlighted state consistent with the existing sidebar navigation behaviour.
