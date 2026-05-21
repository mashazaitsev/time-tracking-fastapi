# System Design — Time Tracking Application

## 1. High-Level System Architecture

```mermaid
graph TB
    subgraph "Frontend Layer (Browser)"
        UI[React UI<br/>Port 5173]
        SDK[API Client SDK<br/>sdk.gen.ts]
        RQ[TanStack Query<br/>Cache + Fetch]
    end

    subgraph "Backend Layer (Server)"
        APP[FastAPI App<br/>Port 8000]
        AUTH[Auth Middleware<br/>JWT Token Validation]
        ROUTES[Route Handlers<br/>items, projects, time_entries, users]
        MODELS[SQLModel ORM<br/>models.py]
    end

    subgraph "Database Layer"
        PG[(PostgreSQL<br/>Port 5432)]
    end

    UI --> SDK
    SDK --> RQ
    RQ -->|HTTP Requests| APP
    APP --> AUTH
    AUTH --> ROUTES
    ROUTES --> MODELS
    MODELS -->|SQL Queries| PG
```

---

## 2. Logical Components by Layer

### Frontend (React/TypeScript)

```mermaid
graph LR
    subgraph "Pages (routes/_layout/)"
        P1[Dashboard]
        P2[Items]
        P3[Projects]
        P4[Time Entries]
        P5[Admin]
    end

    subgraph "Components"
        C1[AddItem / EditItem / DeleteItem]
        C2[AddProject / EditProject / DeleteProject]
        C3[AddTimeEntry / EditTimeEntry / DeleteTimeEntry]
        C4[TimeSummaryWidget]
        C5[AppSidebar]
        C6[DataTable]
    end

    subgraph "Services (client/)"
        S1[ItemsService]
        S2[ProjectsService]
        S3[TimeEntriesService]
        S4[UsersService]
        S5[LoginService]
    end

    subgraph "Hooks"
        H1[useAuth]
        H2[useSuspenseQuery]
        H3[useMutation]
    end

    P2 --> C1
    P3 --> C2
    P4 --> C3
    P1 --> C4
    C1 --> S1
    C2 --> S2
    C3 --> S3
    C4 --> S3
    H1 --> S4
    H1 --> S5
```

### Backend (Python/FastAPI)

```mermaid
graph LR
    subgraph "Entry Point"
        MAIN[main.py<br/>Creates FastAPI app]
    end

    subgraph "API Layer (api/)"
        APIMAIN[api/main.py<br/>Router registry]
        LOGIN[routes/login.py]
        USERS[routes/users.py]
        ITEMS[routes/items.py]
        PROJECTS[routes/projects.py]
        TIMEENTRIES[routes/time_entries.py]
    end

    subgraph "Core Layer (core/)"
        CONFIG[config.py<br/>Settings from .env]
        DB[db.py<br/>Engine + init_db]
        SECURITY[security.py<br/>JWT + password hashing]
    end

    subgraph "Data Layer"
        MODELSFILE[models.py<br/>Tables + Schemas]
        DEPS[deps.py<br/>SessionDep, CurrentUser]
    end

    MAIN --> APIMAIN
    APIMAIN --> LOGIN
    APIMAIN --> USERS
    APIMAIN --> ITEMS
    APIMAIN --> PROJECTS
    APIMAIN --> TIMEENTRIES
    LOGIN --> SECURITY
    DEPS --> DB
    DEPS --> SECURITY
    ITEMS --> DEPS
    PROJECTS --> DEPS
    TIMEENTRIES --> DEPS
    ITEMS --> MODELSFILE
    PROJECTS --> MODELSFILE
    TIMEENTRIES --> MODELSFILE
    DB --> CONFIG
```

### Database (PostgreSQL)

```mermaid
graph TB
    subgraph "Tables"
        USER[user]
        ITEM[item]
        PROJECT[project]
        TIMEENTRY[timeentry]
    end

    USER -->|owns many| ITEM
    USER -->|owns many| PROJECT
    USER -->|owns many| TIMEENTRY
    PROJECT -->|has many| TIMEENTRY
```

---

## 3. Data Model (Entity Relationship Diagram)

```mermaid
erDiagram
    USER {
        uuid id PK
        string email UK
        string hashed_password
        string full_name
        boolean is_active
        boolean is_superuser
        datetime created_at
    }

    ITEM {
        uuid id PK
        string title
        string description
        uuid owner_id FK
        datetime created_at
    }

    PROJECT {
        uuid id PK
        string name
        string description
        uuid owner_id FK
        datetime created_at
    }

    TIMEENTRY {
        uuid id PK
        uuid project_id FK
        uuid owner_id FK
        date date
        int duration_minutes
        string description
        datetime created_at
    }

    USER ||--o{ ITEM : "owns"
    USER ||--o{ PROJECT : "owns"
    USER ||--o{ TIMEENTRY : "owns"
    PROJECT ||--o{ TIMEENTRY : "contains"
```

### Relationship Rules

| Relationship | Type | Cascade |
|---|---|---|
| User → Items | One-to-Many | Delete user → delete all their items |
| User → Projects | One-to-Many | Delete user → delete all their projects |
| User → TimeEntries | One-to-Many | Delete user → delete all their time entries |
| Project → TimeEntries | One-to-Many | Delete project → delete all its time entries |

---

## 4. Major Flows

### Flow 1: User Login

```mermaid
sequenceDiagram
    participant B as Browser
    participant FE as Frontend
    participant BE as Backend
    participant DB as Database

    B->>FE: User types email + password, clicks Login
    FE->>BE: POST /api/v1/login/access-token (email, password)
    BE->>DB: SELECT user WHERE email = ?
    DB-->>BE: User row (with hashed_password)
    BE->>BE: Verify password against hash
    BE->>BE: Create JWT token (contains user ID)
    BE-->>FE: { access_token: "eyJhbG..." }
    FE->>FE: Save token in localStorage
    FE->>B: Redirect to Dashboard
```

### Flow 2: Load Projects Page

```mermaid
sequenceDiagram
    participant B as Browser
    participant FE as Frontend
    participant BE as Backend
    participant DB as Database

    B->>FE: User clicks "Projects" in sidebar
    FE->>FE: Show loading skeleton (PendingProjects)
    FE->>BE: GET /api/v1/projects/ (+ JWT token in header)
    BE->>BE: Decode JWT → identify user
    BE->>DB: SELECT * FROM project WHERE owner_id = user_id
    DB-->>BE: List of project rows
    BE-->>FE: { data: [...], count: 5 }
    FE->>B: Render DataTable with projects
```

### Flow 3: Create a Time Entry

```mermaid
sequenceDiagram
    participant B as Browser
    participant FE as Frontend
    participant BE as Backend
    participant DB as Database

    B->>FE: User fills form (project, date, duration, description)
    FE->>FE: Validate with Zod (duration >= 1, project selected)
    FE->>BE: POST /api/v1/time-entries/ (+ JWT token)
    BE->>BE: Decode JWT → identify user
    BE->>DB: SELECT project WHERE id = project_id
    DB-->>BE: Project row
    BE->>BE: Check: does user own this project?
    alt Project not found
        BE-->>FE: 404 "Project not found"
        FE->>B: Show error toast
    else User doesn't own project
        BE-->>FE: 403 "Not enough permissions"
        FE->>B: Show error toast
    else Valid
        BE->>DB: INSERT INTO timeentry (...)
        DB-->>BE: New row with generated id
        BE-->>FE: { id, project_id, date, duration_minutes, ... }
        FE->>FE: Show success toast, close dialog
        FE->>FE: Invalidate "time-entries" cache → re-fetch list
        FE->>B: Table updates with new entry
    end
```

### Flow 4: Dashboard Summary Widget

```mermaid
sequenceDiagram
    participant B as Browser
    participant FE as Frontend
    participant BE as Backend
    participant DB as Database

    B->>FE: User lands on Dashboard
    FE->>BE: GET /api/v1/time-entries/summary (+ JWT token)
    BE->>BE: Decode JWT → identify user
    BE->>DB: SELECT project_id, SUM(duration_minutes)<br/>FROM timeentry WHERE owner_id = user_id<br/>GROUP BY project_id
    DB-->>BE: Aggregated rows
    BE-->>FE: { total_minutes: 450, by_project: [...] }
    FE->>FE: Format as "7h 30m"
    FE->>B: Render summary card with per-project breakdown
```

### Flow 5: Delete Project (Cascade)

```mermaid
sequenceDiagram
    participant B as Browser
    participant FE as Frontend
    participant BE as Backend
    participant DB as Database

    B->>FE: User clicks Delete on a project, confirms
    FE->>BE: DELETE /api/v1/projects/{id} (+ JWT token)
    BE->>BE: Decode JWT → identify user
    BE->>DB: SELECT project WHERE id = ?
    DB-->>BE: Project row
    BE->>BE: Check ownership
    BE->>DB: DELETE FROM project WHERE id = ?
    Note over DB: CASCADE: all timeentry rows<br/>with this project_id are<br/>automatically deleted too
    DB-->>BE: Done
    BE-->>FE: { message: "Project deleted successfully" }
    FE->>FE: Show success toast, refresh project list
    FE->>B: Project disappears from table
```

---

## 5. API Endpoint Map

```mermaid
graph LR
    subgraph "/api/v1"
        subgraph "/login"
            L1[POST /access-token]
        end
        subgraph "/users"
            U1[GET /me]
            U2[PATCH /me]
            U3[DELETE /me]
        end
        subgraph "/items"
            I1[GET /]
            I2[POST /]
            I3[GET /:id]
            I4[PUT /:id]
            I5[DELETE /:id]
        end
        subgraph "/projects"
            P1[GET /]
            P2[POST /]
            P3[GET /:id]
            P4[PUT /:id]
            P5[DELETE /:id]
        end
        subgraph "/time-entries"
            T0[GET /summary]
            T1[GET /]
            T2[POST /]
            T3[GET /:id]
            T4[PUT /:id]
            T5[DELETE /:id]
        end
    end
```
