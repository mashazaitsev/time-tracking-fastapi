# Requirements Document

## Introduction

This feature adds vacation request management to the full-stack-fastapi-template application. Users can create vacation requests specifying a date range and reason, update or cancel their own requests, and view all vacation requests across the organization. Approval workflows are explicitly out of scope and will be handled by a separate feature. The implementation follows the existing patterns: SQLModel table definitions, FastAPI CRUD routes, pytest integration tests, and TanStack Router/Query frontend pages.

## Glossary

- **VacationRequest**: A record representing a user's request for time off, containing a start date, end date, reason, and status. Owned by a User.
- **Vacation_Request_API**: The FastAPI backend service providing VacationRequest endpoints at `/api/v1/vacation-requests/`.
- **Vacation_Request_UI**: The React/TanStack frontend providing the Vacation Requests page and related dialogs.
- **Owner**: The authenticated User who created a VacationRequest.
- **Superuser**: A User with `is_superuser = True`, who can modify or delete any VacationRequest regardless of ownership.
- **Status**: The current state of a VacationRequest. For this feature, the only valid status is `"pending"`. Additional statuses (approved, rejected) will be introduced by the future approval feature.

---

## Requirements

### Requirement 1: Vacation Request Data Model

**User Story:** As a developer, I want a VacationRequest database model, so that users can persist vacation request records.

#### Acceptance Criteria

1. THE Vacation_Request_API SHALL store each VacationRequest with a UUID primary key, a `start_date` (calendar date), an `end_date` (calendar date), a `reason` (1–500 characters), a `status` string (maximum 20 characters) constrained to the values `"pending"`, `"approved"`, and `"rejected"` and defaulting to `"pending"`, a `created_at` UTC timestamp, and an `owner_id` foreign key referencing the User table.
2. THE Vacation_Request_API SHALL enforce that `end_date` is greater than or equal to `start_date` at the schema validation level.
3. IF a VacationRequest is submitted with `end_date` earlier than `start_date`, THEN THE Vacation_Request_API SHALL reject the request with a validation error indicating that end_date must be greater than or equal to start_date.
4. WHEN a User is deleted, THE Vacation_Request_API SHALL cascade-delete all VacationRequests owned by that User.
5. THE Vacation_Request_API SHALL expose `VacationRequestCreate`, `VacationRequestUpdate`, `VacationRequestPublic`, and `VacationRequestsPublic` Pydantic schemas following the same pattern as `TimeEntryCreate`, `TimeEntryUpdate`, `TimeEntryPublic`, and `TimeEntriesPublic`, where `VacationRequestCreate` accepts `start_date`, `end_date`, and `reason`; `VacationRequestUpdate` accepts all fields as optional; and `VacationRequestPublic` includes all stored fields.

---

### Requirement 2: Create Vacation Request API

**User Story:** As a user, I want to create a vacation request, so that I can formally record my planned time off.

#### Acceptance Criteria

1. WHEN an authenticated User sends `POST /api/v1/vacation-requests/` with a valid `VacationRequestCreate` payload containing `start_date`, `end_date`, and `reason`, THE Vacation_Request_API SHALL create the VacationRequest with `owner_id` set to the current user, `status` set to `"pending"`, `created_at` set to the current UTC timestamp, and return the created `VacationRequestPublic` (including `id`, `owner_id`, `start_date`, `end_date`, `reason`, `status`, and `created_at`) with HTTP 200.
2. IF an authenticated User sends `POST /api/v1/vacation-requests/` with `end_date` earlier than `start_date`, THEN THE Vacation_Request_API SHALL return HTTP 422 with a validation error message indicating that `end_date` must be greater than or equal to `start_date`.
3. IF an authenticated User sends `POST /api/v1/vacation-requests/` with a `reason` shorter than 1 character or longer than 500 characters, THEN THE Vacation_Request_API SHALL return HTTP 422 with a validation error message indicating the length constraint violation.
4. IF an authenticated User sends `POST /api/v1/vacation-requests/` with any required field (`start_date`, `end_date`, or `reason`) missing from the payload, THEN THE Vacation_Request_API SHALL return HTTP 422 with a validation error message indicating the missing field.

---

### Requirement 3: List Vacation Requests API

**User Story:** As a user, I want to view all vacation requests, so that I can see when colleagues are planning time off.

#### Acceptance Criteria

1. WHEN an authenticated User sends `GET /api/v1/vacation-requests/` without `skip` or `limit` query parameters, THE Vacation_Request_API SHALL return a `VacationRequestsPublic` response containing all VacationRequests in the system regardless of ownership, ordered by `created_at` descending, paginated with default `skip` of 0 and default `limit` of 100, and including a `count` field representing the total number of VacationRequests in the system.
2. WHEN an authenticated User sends `GET /api/v1/vacation-requests/` with `skip` (minimum 0) and `limit` (minimum 1, maximum 100) query parameters, THE Vacation_Request_API SHALL return the `VacationRequestsPublic` response offset by `skip` records and containing at most `limit` records, ordered by `created_at` descending, with the `count` field representing the total number of VacationRequests in the system.
3. IF an authenticated User sends `GET /api/v1/vacation-requests/` with a `limit` value exceeding 100, THEN THE Vacation_Request_API SHALL return HTTP 422 with a validation error message indicating the maximum allowed limit is 100.
4. IF an unauthenticated request is sent to `GET /api/v1/vacation-requests/`, THEN THE Vacation_Request_API SHALL return HTTP 401.

---

### Requirement 4: Read Single Vacation Request API

**User Story:** As a user, I want to view a specific vacation request by ID, so that I can see its full details.

#### Acceptance Criteria

1. WHEN an authenticated User sends `GET /api/v1/vacation-requests/{id}`, THE Vacation_Request_API SHALL return the `VacationRequestPublic` with HTTP 200 regardless of ownership.
2. IF an authenticated User sends `GET /api/v1/vacation-requests/{id}` with a non-existent ID, THEN THE Vacation_Request_API SHALL return HTTP 404.

---

### Requirement 5: Update Vacation Request API

**User Story:** As a user, I want to update my vacation request, so that I can correct dates or reason before approval is implemented.

#### Acceptance Criteria

1. WHEN an authenticated User sends `PUT /api/v1/vacation-requests/{id}` with a valid `VacationRequestUpdate` payload for a VacationRequest they own, THE Vacation_Request_API SHALL apply the partial update and return the updated `VacationRequestPublic` with HTTP 200; WHILE the User is a Superuser, THE Vacation_Request_API SHALL allow updating any VacationRequest regardless of ownership.
2. IF an authenticated User sends `PUT /api/v1/vacation-requests/{id}` for a VacationRequest they do not own and the User is not a Superuser, THEN THE Vacation_Request_API SHALL return HTTP 403.
3. IF an authenticated User sends `PUT /api/v1/vacation-requests/{id}` with a non-existent ID, THEN THE Vacation_Request_API SHALL return HTTP 404 before performing any ownership check.
4. IF an authenticated User sends `PUT /api/v1/vacation-requests/{id}` and the resulting `end_date` (after merging the update payload with existing values) is earlier than the resulting `start_date`, THEN THE Vacation_Request_API SHALL return HTTP 422 with a validation error message indicating the date range is invalid.
5. IF an authenticated User sends `PUT /api/v1/vacation-requests/{id}` with a `VacationRequestUpdate` payload where all fields are unset (no changes provided), THEN THE Vacation_Request_API SHALL return the existing `VacationRequestPublic` unchanged with HTTP 200.

---

### Requirement 6: Delete (Cancel) Vacation Request API

**User Story:** As a user, I want to cancel my vacation request, so that I can withdraw a request I no longer need.

#### Acceptance Criteria

1. WHEN an authenticated User sends `DELETE /api/v1/vacation-requests/{id}` for a VacationRequest they own, THE Vacation_Request_API SHALL delete the VacationRequest and return a `Message` confirmation with HTTP 200.
2. IF an authenticated User sends `DELETE /api/v1/vacation-requests/{id}` for a VacationRequest they do not own and the User is not a Superuser, THEN THE Vacation_Request_API SHALL return HTTP 403.
3. IF an authenticated User sends `DELETE /api/v1/vacation-requests/{id}` with a non-existent ID, THEN THE Vacation_Request_API SHALL return HTTP 404 regardless of the requesting User's ownership or Superuser status.
4. WHILE the User is a Superuser, WHEN the User sends `DELETE /api/v1/vacation-requests/{id}` for an existing VacationRequest owned by another User, THE Vacation_Request_API SHALL delete the VacationRequest and return a `Message` confirmation with HTTP 200.

---

### Requirement 7: Backend Tests

**User Story:** As a developer, I want pytest tests for the Vacation Requests API, so that correctness is verified and regressions are caught.

#### Acceptance Criteria

1. THE Vacation_Request_API test suite SHALL include tests for create, read (single and list), update, and delete operations for VacationRequests, using the same pytest fixtures (`client`, `superuser_token_headers`, `normal_user_token_headers`, `db`), assertion style, and file location conventions as `tests/api/routes/test_time_entries.py`.
2. THE Vacation_Request_API test suite SHALL verify that HTTP 403 is returned when a non-owner, non-superuser attempts to update or delete a VacationRequest owned by another user.
3. THE Vacation_Request_API test suite SHALL verify that HTTP 404 is returned when a non-existent VacationRequest UUID is requested for read, update, or delete.
4. THE Vacation_Request_API test suite SHALL verify that a non-owner, non-superuser authenticated user can list all VacationRequests via `GET /api/v1/vacation-requests/` and read any single VacationRequest via `GET /api/v1/vacation-requests/{id}` regardless of ownership, receiving HTTP 200 in both cases.
5. THE Vacation_Request_API test suite SHALL verify that `end_date` earlier than `start_date` returns HTTP 422 on both create and update operations.
6. THE Vacation_Request_API test suite SHALL verify that a Superuser can update and delete any VacationRequest regardless of ownership, receiving HTTP 200 in both cases.
7. THE Vacation_Request_API test suite SHALL verify that a `reason` shorter than 1 character or longer than 500 characters returns HTTP 422 on create.

---

### Requirement 8: Vacation Requests Frontend Page

**User Story:** As a user, I want a Vacation Requests page in the UI, so that I can create, view, and manage vacation requests.

#### Acceptance Criteria

1. THE Vacation_Request_UI SHALL provide a route at `/_layout/vacation-requests` that displays a data table of all VacationRequests across all users with columns for requester name, start date, end date, reason, status, and created date, ordered by created date descending.
2. THE Vacation_Request_UI SHALL provide an "Add Vacation Request" dialog that accepts a start date (required), end date (required), and reason (required, 1–500 characters), and calls `POST /api/v1/vacation-requests/` on submit.
3. WHEN a vacation request is successfully created, THE Vacation_Request_UI SHALL display a success toast, close the dialog, and refresh the vacation requests list.
4. IF vacation request creation fails, THE Vacation_Request_UI SHALL display an error toast with the server-provided message and keep the dialog open with form values preserved.
5. THE Vacation_Request_UI SHALL display inline edit and delete actions only for VacationRequests whose `owner_id` matches the current authenticated user; VacationRequests owned by other users SHALL be displayed without edit or delete actions.
6. THE Vacation_Request_UI SHALL provide an "Edit Vacation Request" dialog that accepts updated start date, end date, and reason (1–500 characters), pre-populated with the existing values, and calls `PUT /api/v1/vacation-requests/{id}` on submit.
7. WHEN a vacation request is successfully edited, THE Vacation_Request_UI SHALL display a success toast, close the dialog, and refresh the vacation requests list.
8. IF vacation request editing fails, THE Vacation_Request_UI SHALL display an error toast with the server-provided message and keep the dialog open with form values preserved.
9. WHEN the user confirms deletion of a vacation request and the server returns a success response, THE Vacation_Request_UI SHALL display a success toast and refresh the vacation requests list.
10. IF vacation request deletion fails, THE Vacation_Request_UI SHALL display an error toast with the server-provided message.
11. WHEN the vacation requests list is loading, THE Vacation_Request_UI SHALL display a spinner in place of the table.
12. WHEN there are no vacation requests, THE Vacation_Request_UI SHALL display a single row containing the text "No vacation requests" in place of data rows.
13. THE Vacation_Request_UI SHALL validate client-side that `end_date` is greater than or equal to `start_date` before submitting the form, and IF validation fails, THEN THE Vacation_Request_UI SHALL display an inline validation error message below the end date field and prevent form submission.

---

### Requirement 9: Sidebar Navigation

**User Story:** As a user, I want a Vacation Requests link in the sidebar, so that I can navigate to the page from anywhere in the app.

#### Acceptance Criteria

1. THE Vacation_Request_UI sidebar SHALL include a "Vacation Requests" navigation link pointing to `/_layout/vacation-requests` that is visible to all authenticated users regardless of role and hidden from unauthenticated users.
2. WHEN the current route path equals `/_layout/vacation-requests`, THE Vacation_Request_UI sidebar SHALL display the "Vacation Requests" link with the `isActive` state set to true, matching the exact-path highlighting used by other sidebar navigation items.
3. THE Vacation_Request_UI sidebar SHALL display the "Vacation Requests" link with an associated icon, positioned among the base navigation items visible to all authenticated users.
