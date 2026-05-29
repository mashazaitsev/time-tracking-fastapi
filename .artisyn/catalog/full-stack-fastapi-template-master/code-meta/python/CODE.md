# Python Documentation (46 files)


## .

**workspace.py**

- **Imports:** skills_sdk.space, skills_sdk.space.kiro.generator

## .copier

**.copier/update_dotenv.py**

- **Imports:** json, pathlib

## backend/app

**backend/app/__init__.py**

**backend/app/backend_pre_start.py** — Purpose: Wait for database readiness before application startup with retry logic

Structure:
    init (func): setup - Attempt DB connection with tenacity retry
    main (func): entry - Script entry point

Relationships:
    Consumes: core.db.engine
    Produces: (blocks until DB is ready)

Semantics:
    Logic: [Retries every 1 second for up to 5 minutes (300 attempts)]

Note:
    Run via scripts/prestart.sh before alembic migrations and initial_data.


### init(db_engine) [line 40] — Purpose: Attempt single DB connection, raising on failure (retried by tenacity)

### main() [line 56] — Purpose: Entry point — wait for database readiness with retry logging
- **Imports:** app.core.db, logging, sqlalchemy, sqlmodel, tenacity
**backend/app/crud.py** — Purpose: Provide CRUD operations for User and Item database entities

Structure:
    create_user (func): output - Create user with hashed password
    update_user (func): output - Update user fields, re-hash if password changed
    get_user_by_email (func): output - Look up user by email
    authenticate (func): output - Verify email/password, upgrade hash if needed
    create_item (func): output - Create item with owner assignment

Relationships:
    Consumes: models.User, models.Item, models.UserCreate, models.UserUpdate, models.ItemCreate
    Consumes: core.security.get_password_hash, core.security.verify_password
    Produces: User rows, Item rows

Semantics:
    Domain: identity, content
    Logic: [Timing-attack prevention via dummy hash on failed lookup,
            Auto-upgrade bcrypt→argon2 on successful login]

Important:
    authenticate() MUST run verify_password even when user not found
    to prevent timing-based email enumeration attacks.


### create_user() [line 35] — Purpose: Create user with hashed password
- **Relationships:** Consumes: UserCreate schema
    Produces: user table row

### update_user() [line 52] — Purpose: Update user fields, re-hashing password if changed
- **Relationships:** Consumes: UserUpdate schema, existing User
    Produces: updated user table row

### get_user_by_email() [line 73] — Purpose: Look up user by email address

### authenticate() [line 84] — Purpose: Verify email/password credentials and auto-upgrade legacy bcrypt hashes
- **Flow:** 1. Look up user by email
    2. If not found, verify against dummy hash (timing-attack prevention)
    3. Verify password against stored hash
    4. If hash algorithm upgraded (bcrypt→argon2), persist new hash

### create_item() [line 113] — Purpose: Create item assigned to owner
- **Relationships:** Consumes: ItemCreate schema, owner UUID
    Produces: item table row
- **Imports:** app.core.security, app.models, sqlmodel, typing, uuid
**backend/app/initial_data.py** — Purpose: Seed initial database data (first superuser) on application startup

Structure:
    init (func): setup - Open session and call init_db
    main (func): entry - Script entry point with logging

Relationships:
    Consumes: core.db.engine, core.db.init_db
    Produces: first superuser in user table

Note:
    Run via: python app/initial_data.py (or uv run python app/initial_data.py)
    Also called by scripts/prestart.sh before app starts.


### init() [line 27] — Purpose: Open database session and seed initial data via init_db

### main() [line 33] — Purpose: Entry point — log and run initial data seeding
- **Imports:** app.core.db, logging, sqlmodel
**backend/app/main.py** — Purpose: Initialize FastAPI application with CORS, Sentry, and API router

Structure:
    app (FastAPI): output - Configured FastAPI application instance
    custom_generate_unique_id (func): config - Generate OpenAPI operation IDs from route tag + name

Relationships:
    Consumes: core.config.settings, api.main.api_router
    Produces: FastAPI app (consumed by uvicorn)

Semantics:
    Domain: application
    Logic: [Sentry enabled only in non-local environments, CORS origins from settings]


### custom_generate_unique_id(route) [line 26] — Purpose: Generate OpenAPI operation ID as '{tag}-{name}' for client codegen
- **Imports:** app.api.main, app.core.config, fastapi, fastapi.routing, sentry_sdk, starlette.middleware.cors
**backend/app/models.py** — Purpose: Define all SQLModel database tables and Pydantic API schemas for User, Item, Project, and TimeEntry entities

Structure:
    User (table): entity - User account with auth and profile data
    Item (table): entity - User-owned content item
    Project (table): entity - Named grouping for time entries, owned by a User
    TimeEntry (table): entity - Time record against a Project, owned by a User
    UserBase, UserCreate, UserUpdate, UserRegister, UserUpdateMe, UpdatePassword: schema - User API schemas
    UserPublic, UsersPublic: schema - User response schemas
    ItemBase, ItemCreate, ItemUpdate: schema - Item API schemas
    ItemPublic, ItemsPublic: schema - Item response schemas
    ProjectBase, ProjectCreate, ProjectUpdate: schema - Project API schemas
    ProjectPublic, ProjectsPublic: schema - Project response schemas
    TimeEntryBase, TimeEntryCreate, TimeEntryUpdate: schema - TimeEntry API schemas
    TimeEntryPublic, TimeEntriesPublic: schema - TimeEntry response schemas
    ProjectSummary, TimeSummary: schema - Aggregated time summary response schemas
    Token, TokenPayload, NewPassword, Message: schema - Auth and utility schemas

Relationships:
    Produces: user table, item table, project table, timeentry table
    Consumes: (consumed by) api.routes, crud, core.db

Semantics:
    Domain: identity, content, time-tracking
    Entity: User, Item, Project, TimeEntry
    Logic: [Items cascade-delete with owner, Projects cascade-delete with owner, TimeEntries cascade-delete with project and owner, UUIDs as primary keys, created_at auto-set to UTC]

Important:
    All SQLModel table classes MUST be imported before Alembic or init_db runs,
    otherwise relationships fail to initialize. See core/db.py comment.


### UserBase [class, line 49]
- **Purpose:** Purpose: Shared user fields for all user schemas

### UserCreate [class, line 57]
- **Purpose:** Purpose: Schema for admin user creation (includes role flags from UserBase)

### UserRegister [class, line 62]
- **Purpose:** Purpose: Schema for public self-registration (no role flags)

### UserUpdate [class, line 69]
- **Purpose:** Purpose: Schema for admin user update (all fields optional)

### UserUpdateMe [class, line 75]
- **Purpose:** Purpose: Schema for self-profile update (name and email only)

### UpdatePassword [class, line 81]
- **Purpose:** Purpose: Schema for authenticated password change

### User [class, line 87]
- **Purpose:** Purpose: User database table with auth credentials and owned items, projects, and time entries

### UserPublic [class, line 100]
- **Purpose:** Purpose: User response schema (excludes hashed_password)

### UsersPublic [class, line 106]
- **Purpose:** Purpose: Paginated user list response

### ItemBase [class, line 112]
- **Purpose:** Purpose: Shared item fields for all item schemas

### ItemCreate [class, line 118]
- **Purpose:** Purpose: Schema for item creation

### ItemUpdate [class, line 123]
- **Purpose:** Purpose: Schema for item update (all fields optional)

### Item [class, line 128]
- **Purpose:** Purpose: Item database table owned by a User (cascade-deletes with owner)

### ItemPublic [class, line 141]
- **Purpose:** Purpose: Item response schema with owner reference

### ItemsPublic [class, line 148]
- **Purpose:** Purpose: Paginated item list response

### Message [class, line 154]
- **Purpose:** Purpose: Generic API message response

### Token [class, line 159]
- **Purpose:** Purpose: JWT access token response

### TokenPayload [class, line 165]
- **Purpose:** Purpose: Decoded JWT token payload (sub = user ID)

### NewPassword [class, line 170]
- **Purpose:** Purpose: Schema for token-based password reset

### ProjectBase [class, line 181]
- **Purpose:** Purpose: Shared project fields for all project schemas

### ProjectCreate [class, line 187]
- **Purpose:** Purpose: Schema for project creation

### ProjectUpdate [class, line 192]
- **Purpose:** Purpose: Schema for project update (all fields optional)

### Project [class, line 197]
- **Purpose:** Purpose: Project database table owned by a User; cascade-deletes time entries

Relationships:
    Consumes: user.id (FK owner_id)
    Produces: project table; back-populates User.projects and TimeEntry.project

### ProjectPublic [class, line 218]
- **Purpose:** Purpose: Project response schema with owner reference

### ProjectsPublic [class, line 225]
- **Purpose:** Purpose: Paginated project list response

### TimeEntryBase [class, line 236]
- **Purpose:** Purpose: Shared time entry fields for all time entry schemas

### TimeEntryCreate [class, line 244]
- **Purpose:** Purpose: Schema for time entry creation

### TimeEntryUpdate [class, line 249]
- **Purpose:** Purpose: Schema for time entry update (all fields optional)

### TimeEntry [class, line 257]
- **Purpose:** Purpose: TimeEntry database table owned by a User and associated with a Project

Relationships:
    Consumes: user.id (FK owner_id), project.id (FK project_id)
    Produces: timeentry table; back-populates User.time_entries and Project.time_entries

### TimeEntryPublic [class, line 279]
- **Purpose:** Purpose: TimeEntry response schema with owner reference

### TimeEntriesPublic [class, line 286]
- **Purpose:** Purpose: Paginated time entry list response

### ProjectSummary [class, line 297]
- **Purpose:** Purpose: Per-project aggregated time summary

### TimeSummary [class, line 304]
- **Purpose:** Purpose: Aggregated time summary across all projects for a user

### get_datetime_utc() [line 44] — Purpose: Return current UTC datetime for default timestamps
- **Imports:** datetime, pydantic, sqlalchemy, sqlmodel, typing, uuid
**backend/app/tests_pre_start.py** — Purpose: Wait for database readiness before test suite execution with retry logic

Structure:
    init (func): setup - Attempt DB connection with tenacity retry
    main (func): entry - Script entry point

Relationships:
    Consumes: core.db.engine
    Produces: (blocks until DB is ready)

Semantics:
    Logic: [Retries every 1 second for up to 5 minutes (300 attempts)]

Note:
    Run via scripts/tests-start.sh before pytest.


### init(db_engine) [line 40] — Purpose: Attempt single DB connection, raising on failure (retried by tenacity)

### main() [line 56] — Purpose: Entry point — wait for database readiness with retry logging
- **Imports:** app.core.db, logging, sqlalchemy, sqlmodel, tenacity
**backend/app/utils.py** — Purpose: Provide email rendering, sending, and password reset token utilities

Structure:
    EmailData (dataclass): schema - Email content container (html_content, subject)
    render_email_template (func): output - Render Jinja2 HTML email from template file
    send_email (func): output - Send email via SMTP
    generate_test_email (func): output - Build test email content
    generate_reset_password_email (func): output - Build password reset email with token link
    generate_new_account_email (func): output - Build new account welcome email
    generate_password_reset_token (func): output - Create JWT token for password reset
    verify_password_reset_token (func): output - Decode and validate password reset JWT

Relationships:
    Consumes: core.config.settings (SMTP_*, EMAILS_*, FRONTEND_HOST, SECRET_KEY)
    Consumes: email-templates/build/*.html (Jinja2 templates)
    Produces: EmailData, JWT tokens (consumed by api.routes.login)

Semantics:
    Domain: communication
    Logic: [Reset tokens expire per EMAIL_RESET_TOKEN_EXPIRE_HOURS,
            SMTP TLS/SSL configured from settings, templates in email-templates/build/]


### EmailData [class, line 44]
- **Purpose:** Purpose: Container for rendered email content and subject

### render_email_template() [line 50] — Purpose: Render Jinja2 HTML email template from email-templates/build/

### send_email() [line 59] — Purpose: Send email via configured SMTP server

### generate_test_email(email_to) [line 90] — Purpose: Build test email content for SMTP verification

### generate_reset_password_email(email_to, email, token) [line 101] — Purpose: Build password reset email with frontend reset link

### generate_new_account_email(email_to, username, password) [line 119] — Purpose: Build welcome email for newly created accounts

### generate_password_reset_token(email) [line 138] — Purpose: Create JWT token for password reset with configured expiration

### verify_password_reset_token(token) [line 152] — Purpose: Decode and validate password reset JWT, returning email if valid
- **Imports:** 11 external dependencies

## backend/app/alembic

**backend/app/alembic/env.py** — Purpose: Configure Alembic migration environment for online and offline modes

Structure:
    get_url (func): config - Return database URL from settings
    run_migrations_offline (func): migration - Run migrations without DB connection
    run_migrations_online (func): migration - Run migrations with live DB connection

Relationships:
    Consumes: app.models.SQLModel.metadata, app.core.config.settings.SQLALCHEMY_DATABASE_URI
    Produces: Database schema migrations

Important:
    app.models MUST be imported before target_metadata is set,
    otherwise Alembic won't detect model changes for autogenerate.


### get_url() [line 41] — Purpose: Return database connection URL from application settings
- **Relationships:** Consumes: settings.SQLALCHEMY_DATABASE_URI
    Produces: Database URL string

### run_migrations_offline() [line 55] — Purpose: Run migrations in offline mode (emit SQL without DB connection)
- **Relationships:** Consumes: get_url(), target_metadata
    Produces: SQL migration statements
- **Flow:** 1. Get database URL
    2. Configure Alembic context with URL and metadata
    3. Run migrations within transaction

### run_migrations_online() [line 80] — Purpose: Run migrations in online mode with live database connection
- **Relationships:** Consumes: get_url(), config section, target_metadata
    Produces: Applied database migrations
- **Flow:** 1. Build engine config with database URL
    2. Create connectable engine with NullPool
    3. Configure context with connection and run migrations
- **Imports:** alembic, app.core.config, app.models, logging.config, os, sqlalchemy

## backend/app/alembic/versions

**backend/app/alembic/versions/1a31ce608336_add_cascade_delete_relationships.py** — Add cascade delete relationships

Revision ID: 1a31ce608336
Revises: d98dd8ec85a3
Create Date: 2024-07-31 22:24:34.447891


### upgrade() [line 20]

### downgrade() [line 30]
- **Imports:** alembic, sqlalchemy, sqlmodel.sql.sqltypes
**backend/app/alembic/versions/3a8f2c1d4e5b_add_project_and_timeentry_tables.py** — Add project and timeentry tables

Revision ID: 3a8f2c1d4e5b
Revises: fe56fa70289e
Create Date: 2026-01-24 10:00:00.000000


### upgrade() [line 20]

### downgrade() [line 49]
- **Imports:** alembic, sqlalchemy, sqlmodel.sql.sqltypes
**backend/app/alembic/versions/9c0a54914c78_add_max_length_for_string_varchar_.py** — Add max length for string(varchar) fields in User and Items models

Revision ID: 9c0a54914c78
Revises: e2412789c190
Create Date: 2024-06-17 14:42:44.639457


### upgrade() [line 20]

### downgrade() [line 46]
- **Imports:** alembic, sqlalchemy, sqlmodel.sql.sqltypes
**backend/app/alembic/versions/d98dd8ec85a3_edit_replace_id_integers_in_all_models_.py** — Edit replace id integers in all models to use UUID instead

Revision ID: d98dd8ec85a3
Revises: 9c0a54914c78
Create Date: 2024-07-19 04:08:04.000976


### upgrade() [line 21]

### downgrade() [line 57]
- **Imports:** alembic, sqlalchemy, sqlalchemy.dialects, sqlmodel.sql.sqltypes
**backend/app/alembic/versions/e2412789c190_initialize_models.py** — Initialize models

Revision ID: e2412789c190
Revises:
Create Date: 2023-11-24 22:55:43.195942


### upgrade() [line 19]

### downgrade() [line 49]
- **Imports:** alembic, sqlalchemy, sqlmodel.sql.sqltypes
**backend/app/alembic/versions/fe56fa70289e_add_created_at_to_user_and_item.py** — Add created_at to User and Item

Revision ID: fe56fa70289e
Revises: 1a31ce608336
Create Date: 2026-01-23 15:50:37.171462


### upgrade() [line 20]

### downgrade() [line 27]
- **Imports:** alembic, sqlalchemy, sqlmodel.sql.sqltypes

## backend/app/api

**backend/app/api/__init__.py**

**backend/app/api/deps.py** — Purpose: Provide FastAPI dependency injection for database sessions and authentication

Structure:
    get_db (func): dependency - Yield SQLModel session per request
    get_current_user (func): dependency - Decode JWT and return authenticated User
    get_current_active_superuser (func): dependency - Enforce superuser role
    SessionDep (type alias): shorthand - Annotated[Session, Depends(get_db)]
    TokenDep (type alias): shorthand - Annotated[str, Depends(reusable_oauth2)]
    CurrentUser (type alias): shorthand - Annotated[User, Depends(get_current_user)]

Relationships:
    Consumes: core.security.ALGORITHM, core.config.settings.SECRET_KEY, core.db.engine
    Consumes: models.TokenPayload, models.User
    Produces: Session, User (injected into route handlers)


### get_db() [line 38] — Purpose: Yield a database session per request, auto-closed on completion
- **Relationships:** Consumes: core.db.engine
    Produces: Session (via SessionDep alias)

### get_current_user(session, token) [line 57] — Purpose: Decode JWT token and return the authenticated active User
- **Relationships:** Consumes: JWT token, User table, core.security.ALGORITHM, settings.SECRET_KEY
    Produces: Authenticated User object (via CurrentUser alias)
- **Flow:** 1. Decode JWT with SECRET_KEY and validate payload
    2. Look up user by token subject (user ID)
    3. Raise 404 if not found, 400 if inactive

### get_current_active_superuser(current_user) [line 96] — Purpose: Enforce superuser role on authenticated user
- **Relationships:** Consumes: CurrentUser dependency
    Produces: Verified superuser (used as route dependency)
- **Imports:** 12 external dependencies
**backend/app/api/main.py** — Purpose: Register all API route modules into the main API router

Structure:
    api_router (APIRouter): output - Combined router with all route modules

Relationships:
    Consumes: api.routes.login, api.routes.users, api.routes.utils, api.routes.items, api.routes.projects, api.routes.time_entries, api.routes.private
    Produces: api_router (consumed by app.main)

Note:
    Private routes only registered when ENVIRONMENT=local.

- **Imports:** app.api.routes, app.core.config, fastapi

## backend/app/api/routes

**backend/app/api/routes/__init__.py**

**backend/app/api/routes/items.py** — Purpose: Provide CRUD API endpoints for Item resources with owner-based access control

Structure:
    read_items (GET /): endpoint - List items (all for superuser, own for regular user)
    read_item (GET /{id}): endpoint - Get single item by ID
    create_item (POST /): endpoint - Create item owned by current user
    update_item (PUT /{id}): endpoint - Update item (owner or superuser only)
    delete_item (DELETE /{id}): endpoint - Delete item (owner or superuser only)

Relationships:
    Consumes: models.Item, models.ItemCreate, models.ItemUpdate, api.deps.CurrentUser
    Produces: ItemPublic, ItemsPublic, Message responses

Semantics:
    Domain: content
    Entity: Item
    Logic: [Superusers see all items, regular users see only their own,
            owner or superuser required for read/update/delete of specific items]


### read_items(session, current_user, skip, limit) [line 35] — Purpose: Retrieve paginated list of items for current user
- **Relationships:** Consumes: Item table, current user context
    Produces: ItemsPublic response
- **Flow:** 1. Check if superuser (query all) or regular user (query owned only)
    2. Count matching items and fetch paginated results
    3. Return ItemsPublic with data and count

### read_item(session, current_user, id) [line 85] — Purpose: Retrieve a single item by ID with ownership check
- **Relationships:** Consumes: Item table, current user context
    Produces: ItemPublic response
- **Flow:** 1. Fetch item by ID, raise 404 if not found
    2. Verify ownership or superuser role, raise 403 if denied
    3. Return item

### create_item() [line 113] — Purpose: Create a new item owned by the current user
- **Relationships:** Consumes: ItemCreate schema, current user context
    Produces: Item table row, ItemPublic response
- **Flow:** 1. Validate input and set owner_id to current user
    2. Persist item to database
    3. Return created item

### update_item() [line 142] — Purpose: Update an existing item with ownership check
- **Relationships:** Consumes: Item table, ItemUpdate schema, current user context
    Produces: Updated Item table row, ItemPublic response
- **Flow:** 1. Fetch item by ID, raise 404 if not found
    2. Verify ownership or superuser role, raise 403 if denied
    3. Apply partial update and persist

### delete_item(session, current_user, id) [line 182] — Purpose: Delete an item with ownership check
- **Relationships:** Consumes: Item table, current user context
    Produces: Message response
- **Flow:** 1. Fetch item by ID, raise 404 if not found
    2. Verify ownership or superuser role, raise 403 if denied
    3. Delete item and return confirmation
- **Imports:** app.api.deps, app.models, fastapi, sqlmodel, typing, uuid
**backend/app/api/routes/login.py** — Purpose: Provide authentication endpoints for login, token validation, and password recovery

Structure:
    login_access_token (POST /login/access-token): endpoint - OAuth2 token login
    test_token (POST /login/test-token): endpoint - Validate access token
    recover_password (POST /password-recovery/{email}): endpoint - Send password reset email
    reset_password (POST /reset-password/): endpoint - Reset password with token
    recover_password_html_content (POST /password-recovery-html-content/{email}): endpoint - Preview reset email HTML (superuser only)

Relationships:
    Consumes: crud.authenticate, crud.get_user_by_email, crud.update_user
    Consumes: utils.generate_password_reset_token, utils.generate_reset_password_email, utils.send_email
    Produces: Token, UserPublic, Message responses

Semantics:
    Domain: authentication
    Logic: [Password recovery returns same response regardless of email existence (prevents enumeration),
            Reset tokens expire per EMAIL_RESET_TOKEN_EXPIRE_HOURS setting]


### login_access_token(session, form_data) [line 45] — Purpose: Authenticate user via email/password and return JWT access token
- **Relationships:** Consumes: crud.authenticate, core.security.create_access_token
    Produces: Token response
- **Flow:** 1. Authenticate user via crud, raise 400 if invalid credentials
    2. Raise 400 if user is inactive
    3. Create and return JWT access token with configured expiry

### test_token(current_user) [line 81] — Purpose: Validate access token and return current user profile
- **Relationships:** Consumes: CurrentUser dependency (validates token implicitly)
    Produces: UserPublic response

### recover_password(email, session) [line 97] — Purpose: Send password recovery email if user exists
- **Relationships:** Consumes: crud.get_user_by_email, utils.generate_password_reset_token, utils.send_email
    Produces: Message response, password reset email
- **Flow:** 1. Look up user by email
    2. If found, generate reset token and send recovery email
    3. Return same message regardless of email existence (prevents enumeration)

### reset_password(session, body) [line 133] — Purpose: Reset user password using a recovery token
- **Relationships:** Consumes: utils.verify_password_reset_token, crud.get_user_by_email, crud.update_user
    Produces: Message response, updated password hash in User table
- **Flow:** 1. Verify reset token and extract email, raise 400 if invalid
    2. Look up user by email, raise 400 if not found or inactive
    3. Update password hash and return confirmation

### recover_password_html_content(email, session) [line 173] — Purpose: Preview password recovery email HTML content (superuser only)
- **Relationships:** Consumes: crud.get_user_by_email, utils.generate_password_reset_token, utils.generate_reset_password_email
    Produces: HTMLResponse with email content and subject header
- **Flow:** 1. Look up user by email, raise 404 if not found
    2. Generate reset token and email content
    3. Return HTML response with subject in headers
- **Imports:** 11 external dependencies
**backend/app/api/routes/private.py** — Purpose: Provide private admin endpoint for user creation (local environment only)

Structure:
    PrivateUserCreate (class): schema - User creation without SQLModel validation
    create_user (POST /private/users/): endpoint - Create user directly

Relationships:
    Consumes: models.User, core.security.get_password_hash
    Produces: UserPublic response, User table row

Note:
    Only registered when ENVIRONMENT=local (see api/main.py).


### PrivateUserCreate [class, line 31]
- **Purpose:** Purpose: Schema for private user creation (bypasses SQLModel validation)

Structure:
    email (str): input - User email
    password (str): input - Plain text password
    full_name (str): input - User display name
    is_verified (bool): input - Verification status (default False)

### create_user(user_in, session) [line 48] — Purpose: Create user directly without email uniqueness check (local dev only)
- **Relationships:** Consumes: PrivateUserCreate schema, core.security.get_password_hash
    Produces: User table row, UserPublic response
- **Flow:** 1. Build User model with hashed password
    2. Persist to database
    3. Return created user
- **Imports:** app.api.deps, app.core.security, app.models, fastapi, pydantic, typing
**backend/app/api/routes/projects.py** — Purpose: Provide CRUD API endpoints for Project resources with owner-based access control

Structure:
    read_projects (GET /): endpoint - List projects (all for superuser, own for regular user)
    create_project (POST /): endpoint - Create project owned by current user
    read_project (GET /{id}): endpoint - Get single project by ID
    update_project (PUT /{id}): endpoint - Update project (owner or superuser only)
    delete_project (DELETE /{id}): endpoint - Delete project (owner or superuser only)

Relationships:
    Consumes: models.Project, models.ProjectCreate, models.ProjectUpdate, api.deps.CurrentUser
    Produces: ProjectPublic, ProjectsPublic, Message responses

Semantics:
    Domain: time-tracking
    Entity: Project
    Logic: [Superusers see all projects, regular users see only their own,
            owner or superuser required for read/update/delete of specific projects,
            404 is raised before 403 on all single-resource endpoints]


### read_projects(session, current_user, skip, limit) [line 43] — Purpose: Retrieve paginated list of projects for current user
- **Flow:** 1. Check if superuser (query all) or regular user (query owned only)
    2. Count matching projects and fetch paginated results
    3. Return ProjectsPublic with data and count

### create_project() [line 91] — Purpose: Create a new project owned by the current user
- **Flow:** 1. Validate input and set owner_id to current user
    2. Persist project to database
    3. Return created project

### read_project(session, current_user, id) [line 116] — Purpose: Retrieve a single project by ID with ownership check
- **Flow:** 1. Fetch project by ID, raise 404 if not found
    2. Verify ownership or superuser role, raise 403 if denied
    3. Return project

### update_project() [line 142] — Purpose: Update an existing project with ownership check
- **Flow:** 1. Fetch project by ID, raise 404 if not found
    2. Verify ownership or superuser role, raise 403 if denied
    3. Apply partial update and persist

### delete_project(session, current_user, id) [line 178] — Purpose: Delete a project with ownership check
- **Flow:** 1. Fetch project by ID, raise 404 if not found
    2. Verify ownership or superuser role, raise 403 if denied
    3. Delete project and return confirmation
- **Imports:** app.api.deps, app.models, fastapi, sqlmodel, typing, uuid
**backend/app/api/routes/time_entries.py** — Purpose: Provide CRUD API endpoints for TimeEntry resources with owner-based access control and time summary aggregation

Structure:
    get_summary (GET /summary): endpoint - Aggregate total and per-project minutes (registered before /{id})
    read_time_entries (GET /): endpoint - List time entries (all for superuser, own for regular user)
    create_time_entry (POST /): endpoint - Create time entry with project ownership validation
    read_time_entry (GET /{id}): endpoint - Get single time entry by ID
    update_time_entry (PUT /{id}): endpoint - Update time entry (owner or superuser only)
    delete_time_entry (DELETE /{id}): endpoint - Delete time entry (owner or superuser only)

Relationships:
    Consumes: models.TimeEntry, models.TimeEntryCreate, models.TimeEntryUpdate, models.Project
    Consumes: models.TimeSummary, models.ProjectSummary, api.deps.CurrentUser
    Produces: TimeEntryPublic, TimeEntriesPublic, TimeSummary, Message responses

Semantics:
    Domain: time-tracking
    Entity: TimeEntry
    Logic: [Superusers see all entries, regular users see only their own,
            owner or superuser required for read/update/delete of specific entries,
            project_id must exist and be owned by current user (or user is superuser) on create,
            GET /summary MUST be registered before GET /{id} to prevent FastAPI treating "summary" as UUID]

Important:
    GET /summary is registered FIRST to prevent FastAPI treating the literal string "summary" as a UUID path parameter.


### get_summary(session, current_user) [line 52] — Purpose: Aggregate total minutes and per-project breakdown for the current user
- **Relationships:** Consumes: TimeEntry table, Project table, current user context
    Produces: TimeSummary response
- **Flow:** 1. Build aggregation query: sum(duration_minutes) grouped by project_id, joined with Project for name
    2. Scope to owner_id unless superuser
    3. Compute total_minutes from aggregated rows
    4. Return TimeSummary with total_minutes=0 and by_project=[] when no entries exist

### read_time_entries(session, current_user, skip, limit) [line 103] — Purpose: Retrieve paginated list of time entries for current user
- **Relationships:** Consumes: TimeEntry table, current user context
    Produces: TimeEntriesPublic response
- **Flow:** 1. Check if superuser (query all) or regular user (query owned only)
    2. Count matching entries and fetch paginated results
    3. Return TimeEntriesPublic with data and count

### create_time_entry() [line 155] — Purpose: Create a new time entry owned by the current user after validating project ownership
- **Relationships:** Consumes: TimeEntryCreate schema, Project table, current user context
    Produces: TimeEntry table row, TimeEntryPublic response
- **Flow:** 1. Fetch project by project_id; raise 404 if not found
    2. Verify project ownership or superuser role; raise 403 if denied
    3. Create time entry with owner_id = current_user.id
    4. Persist and return created entry

### read_time_entry(session, current_user, id) [line 191] — Purpose: Retrieve a single time entry by ID with ownership check
- **Relationships:** Consumes: TimeEntry table, current user context
    Produces: TimeEntryPublic response
- **Flow:** 1. Fetch entry by ID; raise 404 if not found
    2. Verify ownership or superuser role; raise 403 if denied
    3. Return entry

### update_time_entry() [line 221] — Purpose: Partially update an existing time entry with ownership check
- **Relationships:** Consumes: TimeEntry table, TimeEntryUpdate schema, current user context
    Produces: Updated TimeEntry table row, TimeEntryPublic response
- **Flow:** 1. Fetch entry by ID; raise 404 if not found
    2. Verify ownership or superuser role; raise 403 if denied
    3. Apply partial update (exclude_unset=True) and persist

### delete_time_entry(session, current_user, id) [line 261] — Purpose: Delete a time entry with ownership check
- **Relationships:** Consumes: TimeEntry table, current user context
    Produces: Message response
- **Flow:** 1. Fetch entry by ID; raise 404 if not found
    2. Verify ownership or superuser role; raise 403 if denied
    3. Delete entry and return confirmation
- **Imports:** app.api.deps, app.models, fastapi, sqlmodel, typing, uuid
**backend/app/api/routes/users.py** — Purpose: Provide CRUD API endpoints for User management with role-based access control

Structure:
    read_users (GET /): endpoint - List users (superuser only)
    create_user (POST /): endpoint - Create user (superuser only)
    update_user_me (PATCH /me): endpoint - Update own profile
    update_password_me (PATCH /me/password): endpoint - Change own password
    read_user_me (GET /me): endpoint - Get own profile
    delete_user_me (DELETE /me): endpoint - Delete own account (non-superuser only)
    register_user (POST /signup): endpoint - Public self-registration
    read_user_by_id (GET /{user_id}): endpoint - Get user by ID
    update_user (PATCH /{user_id}): endpoint - Update user (superuser only)
    delete_user (DELETE /{user_id}): endpoint - Delete user (superuser only)

Relationships:
    Consumes: crud (create_user, update_user, get_user_by_email), models (User, Item, schemas)
    Consumes: utils.generate_new_account_email, utils.send_email
    Produces: UserPublic, UsersPublic, Message responses

Semantics:
    Domain: identity
    Entity: User
    Logic: [Superusers cannot delete themselves, email uniqueness enforced,
            new account email sent if SMTP configured, items cascade-deleted with user]


### read_users(session, skip, limit) [line 64] — Purpose: Retrieve paginated list of all users (superuser only)
- **Relationships:** Consumes: User table
    Produces: UsersPublic response

### create_user() [line 93] — Purpose: Create a new user (superuser only), send welcome email if SMTP configured
- **Relationships:** Consumes: crud.get_user_by_email, crud.create_user, utils.send_email
    Produces: User table row, UserPublic response, welcome email
- **Flow:** 1. Check email uniqueness, raise 400 if duplicate
    2. Create user via crud
    3. Send welcome email if SMTP enabled

### update_user_me() [line 132] — Purpose: Update own profile (name and email)
- **Relationships:** Consumes: crud.get_user_by_email, User table
    Produces: Updated User table row, UserPublic response
- **Flow:** 1. If email changing, check uniqueness (raise 409 if taken)
    2. Apply partial update to current user
    3. Persist and return updated user

### update_password_me() [line 169] — Purpose: Change own password with current password verification
- **Relationships:** Consumes: core.security.verify_password, core.security.get_password_hash
    Produces: Updated password hash in User table, Message response
- **Flow:** 1. Verify current password, raise 400 if incorrect
    2. Reject if new password equals current, raise 400
    3. Hash new password, persist, and return confirmation

### read_user_me(current_user) [line 205] — Purpose: Get current authenticated user profile
- **Relationships:** Consumes: CurrentUser dependency
    Produces: UserPublic response

### delete_user_me(session, current_user) [line 221] — Purpose: Delete own account (superusers cannot delete themselves)
- **Relationships:** Consumes: User table
    Produces: Message response

### register_user(session, user_in) [line 244] — Purpose: Public self-registration (no auth required)
- **Relationships:** Consumes: crud.get_user_by_email, crud.create_user
    Produces: User table row, UserPublic response
- **Flow:** 1. Check email uniqueness, raise 400 if duplicate
    2. Convert to UserCreate and create user via crud
    3. Return created user

### read_user_by_id(user_id, session, current_user) [line 274] — Purpose: Get user by ID (own profile or superuser only)
- **Relationships:** Consumes: User table, current user context
    Produces: UserPublic response
- **Flow:** 1. Fetch user by ID
    2. Return immediately if requesting own profile
    3. Raise 403 if not superuser, raise 404 if user not found

### update_user() [line 313] — Purpose: Update a user by ID (superuser only)
- **Relationships:** Consumes: crud.get_user_by_email, crud.update_user, User table
    Produces: Updated User table row, UserPublic response
- **Flow:** 1. Fetch user by ID, raise 404 if not found
    2. If email changing, check uniqueness (raise 409 if taken)
    3. Update user via crud and return

### delete_user(session, current_user, user_id) [line 356] — Purpose: Delete a user and their items (superuser only, cannot self-delete)
- **Relationships:** Consumes: User table, Item table
    Produces: Message response
- **Flow:** 1. Fetch user by ID, raise 404 if not found
    2. Raise 403 if attempting self-deletion
    3. Delete user's items, then delete user
- **Imports:** app, app.api.deps, app.core.config, app.core.security, app.models, app.utils, fastapi, sqlmodel, typing, uuid
**backend/app/api/routes/utils.py** — Purpose: Provide utility endpoints for health checks and email testing

Structure:
    test_email (POST /utils/test-email/): endpoint - Send test email (superuser only)
    health_check (GET /utils/health-check/): endpoint - Application health check

Relationships:
    Consumes: utils.generate_test_email, utils.send_email
    Produces: Message response, bool response


### test_email(email_to) [line 28] — Purpose: Send test email to verify SMTP configuration (superuser only)
- **Relationships:** Consumes: utils.generate_test_email, utils.send_email
    Produces: Message response, test email
- **Imports:** app.api.deps, app.models, app.utils, fastapi, pydantic.networks

## backend/app/core

**backend/app/core/__init__.py**

**backend/app/core/config.py** — Purpose: Load and validate all application settings from environment variables and .env file

Structure:
    Settings (class): config - Pydantic settings with validation for DB, auth, email, CORS
    parse_cors (func): config - Parse CORS origins from comma-separated string or list
    settings (Settings): output - Singleton settings instance

Relationships:
    Consumes: ../.env file, environment variables
    Produces: settings (consumed by all backend modules)

Semantics:
    Domain: configuration
    Logic: [Warns on default secrets in local, raises in staging/production,
            SQLALCHEMY_DATABASE_URI computed from POSTGRES_* fields,
            emails_enabled computed from SMTP_HOST + EMAILS_FROM_EMAIL]

Important:
    SECRET_KEY, POSTGRES_PASSWORD, and FIRST_SUPERUSER_PASSWORD MUST NOT be
    "changethis" in staging/production — validation will raise ValueError.


### Settings [class, line 50]
- **Purpose:** Purpose: Centralized application configuration with env var loading and validation

Structure:
    API_V1_STR (str): config - API version prefix
    SECRET_KEY (str): config - JWT signing key
    SQLALCHEMY_DATABASE_URI (computed): config - Full PostgreSQL connection URI
    emails_enabled (computed): config - Whether email sending is configured
    all_cors_origins (computed): config - Combined CORS + frontend origins

Important:
    env_file points to "../.env" (one level above backend/).
    Default secrets trigger warnings locally, errors in staging/production.
- **Methods:**
  - all_cors_origins: line 84
  - SQLALCHEMY_DATABASE_URI: line 100
  - _set_default_emails_from: line 121
  - emails_enabled: line 131
  - _check_default_secret: line 139
  - _enforce_non_default_secrets: line 152

### parse_cors(v) [line 41] — Purpose: Parse CORS origins from comma-separated string or list

### all_cors_origins(self) [line 84] — Purpose: Combine BACKEND_CORS_ORIGINS and FRONTEND_HOST into unified origin list

### SQLALCHEMY_DATABASE_URI(self) [line 100] — Purpose: Build PostgreSQL connection URI from individual POSTGRES_* settings

### _set_default_emails_from(self) [line 121] — Purpose: Default EMAILS_FROM_NAME to PROJECT_NAME if not set

### emails_enabled(self) [line 131] — Purpose: Check if SMTP is configured (SMTP_HOST and EMAILS_FROM_EMAIL both set)

### _check_default_secret(self, var_name, value) [line 139] — Purpose: Warn (local) or raise (staging/production) if secret is still 'changethis'

### _enforce_non_default_secrets(self) [line 152] — Purpose: Validate SECRET_KEY, POSTGRES_PASSWORD, and FIRST_SUPERUSER_PASSWORD are not defaults
- **Imports:** pydantic, pydantic_settings, secrets, typing, typing_extensions, warnings
**backend/app/core/db.py** — Purpose: Initialize database engine and seed first superuser on startup

Structure:
    engine (Engine): config - SQLAlchemy engine from settings
    init_db (func): output - Create first superuser if not exists

Relationships:
    Consumes: core.config.settings (SQLALCHEMY_DATABASE_URI, FIRST_SUPERUSER, FIRST_SUPERUSER_PASSWORD)
    Consumes: crud.create_user
    Produces: first superuser row in user table

Important:
    All SQLModel models MUST be imported (via app.models) before init_db runs,
    otherwise SQLModel fails to initialize relationships.
    Tables are created by Alembic migrations, NOT by init_db.


### init_db(session) [line 28] — Purpose: Seed first superuser if not already present
- **Flow:** 1. Check if FIRST_SUPERUSER email exists
    2. If not, create superuser via crud.create_user
- **Imports:** app, app.core.config, app.models, sqlmodel
**backend/app/core/security.py** — Purpose: Provide JWT token creation and password hashing/verification

Structure:
    create_access_token (func): output - Create signed JWT with expiration
    verify_password (func): output - Verify password and return upgraded hash if applicable
    get_password_hash (func): output - Hash password with Argon2
    password_hash (PasswordHash): config - Multi-hasher supporting Argon2 and bcrypt
    ALGORITHM (str): config - JWT signing algorithm (HS256)

Relationships:
    Consumes: core.config.settings.SECRET_KEY
    Produces: JWT tokens, password hashes (consumed by crud, api.deps)

Semantics:
    Domain: security
    Logic: [Argon2 is primary hasher, bcrypt supported for legacy upgrade,
            verify_and_update returns new hash when bcrypt→argon2 upgrade needed]


### create_access_token(subject, expires_delta) [line 42] — Purpose: Create signed JWT with subject (user ID) and expiration

### verify_password(plain_password, hashed_password) [line 50] — Purpose: Verify password against hash, returning upgraded hash if algorithm changed

### get_password_hash(password) [line 63] — Purpose: Hash password using Argon2 (primary hasher)
- **Imports:** app.core.config, datetime, jwt, pwdlib, pwdlib.hashers.argon2, pwdlib.hashers.bcrypt, typing

## backend/tests

**backend/tests/__init__.py**

**backend/tests/conftest.py**


### db() [line 16]

### client() [line 28]

### superuser_token_headers(client) [line 34]

### normal_user_token_headers(client, db) [line 39]
- **Imports:** app.core.config, app.core.db, app.main, app.models, collections.abc, fastapi.testclient, pytest, sqlmodel, tests.utils.user, tests.utils.utils

## backend/tests/api

**backend/tests/api/__init__.py**


## backend/tests/api/routes

**backend/tests/api/routes/__init__.py**


## backend/tests/crud

**backend/tests/crud/__init__.py**


## backend/tests/scripts

**backend/tests/scripts/__init__.py**


## backend/tests/utils

**backend/tests/utils/__init__.py**

**backend/tests/utils/item.py**


### create_random_item(db) [line 9]
- **Imports:** app, app.models, sqlmodel, tests.utils.user, tests.utils.utils
**backend/tests/utils/project.py**


### create_random_project(db) [line 8]
- **Imports:** app.models, sqlmodel, tests.utils.user, tests.utils.utils
**backend/tests/utils/time_entry.py**


### create_random_time_entry(db) [line 11] — Create a random time entry, optionally reusing an existing project/owner.
- **Imports:** app.models, datetime, sqlmodel, tests.utils.user, tests.utils.utils, uuid
**backend/tests/utils/user.py**


### user_authentication_headers() [line 10]

### create_random_user(db) [line 22]

### authentication_token_from_email() [line 30] — Return a valid token for the user with given email.
- **Imports:** app, app.core.config, app.models, fastapi.testclient, sqlmodel, tests.utils.utils
**backend/tests/utils/utils.py**


### random_lower_string() [line 9]

### random_email() [line 13]

### get_superuser_token_headers(client) [line 17]
- **Imports:** app.core.config, fastapi.testclient, random, string

## full_stack_fastapi_template

**full_stack_fastapi_template/__init__.py** — Skills provider for full-stack-fastapi-template


### get_skills_directory() [line 5] — Return path to skills directory for AILA skill discovery.
- **Imports:** pathlib

## hooks

**hooks/post_gen_project.py**

- **Imports:** pathlib
