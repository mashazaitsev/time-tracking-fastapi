# Adding 'Projects' Resource — Implementation Guide

request: I need to add a new resource type called 'projects' with the same patterns as items but with additional fields. What files do I need to modify and what patterns should I follow?

Follow the existing `items` patterns to add a new `projects` resource with additional fields.

---

## Backend (Python/FastAPI)

### Files to Create

#### `backend/app/api/routes/projects.py`

New route file for all project CRUD endpoints.

**Pattern from items:**
- `SessionDep` + `CurrentUser` dependency injection
- Owner-based access control: owner or superuser can access
- Skip/limit pagination on list endpoint
- Returns `Public` Pydantic schemas

**Endpoints:**
- `GET /` — list projects (superusers see all, users see own); returns `ProjectsPublic`
- `GET /{id}` — get single project; owner or superuser; returns `ProjectPublic`
- `POST /` — create project; sets `current_user.id` as `owner_id`; returns `ProjectPublic`
- `PUT /{id}` — update project; owner or superuser; uses `model_dump(exclude_unset=True)` + `setattr` loop; returns `ProjectPublic`
- `DELETE /{id}` — delete project; owner or superuser; returns `Message`

### Files to Modify

#### `backend/app/models.py`

Add the following models following the items schema inheritance chain:

- `ProjectBase(SQLModel)` — shared fields (title, description, plus additional fields like status, start_date, end_date, budget, etc.)
- `ProjectCreate(ProjectBase)` — creation schema (inherits base, required fields)
- `ProjectUpdate(ProjectBase)` — update schema (all fields `Optional`)
- `Project(ProjectBase, table=True)` — DB table model with:
  - `id: uuid.UUID` (primary key, `default_factory=uuid.uuid4`)
  - `owner_id: uuid.UUID` (FK to `user.id`, `ondelete="CASCADE"`)
  - `created_at: datetime`
  - Relationship to `User`
- `ProjectPublic(ProjectBase)` — single project response with `id`, `owner_id`, `created_at`
- `ProjectsPublic(SQLModel)` — list response with `data: list[ProjectPublic]` and `count: int`

#### `backend/app/crud.py`

Add project CRUD function:

```python
def create_project(*, session: Session, project_in: ProjectCreate, owner_id: uuid.UUID) -> Project:
    db_project = Project.model_validate(project_in, update={"owner_id": owner_id})
    session.add(db_project)
    session.commit()
    session.refresh(db_project)
    return db_project
```

#### `backend/app/api/main.py`

Register the new router:

```python
from app.api.routes import projects

api_router.include_router(projects.router, prefix="/projects", tags=["projects"])
```

#### Alembic Migration

After adding models, generate and apply migration:

```bash
cd backend
alembic revision --autogenerate -m "Add project table"
alembic upgrade head
```

---

## Frontend (React/TypeScript)

### Files to Create

#### `frontend/src/routes/_layout/projects.tsx`

Projects list/table route page.

**Pattern from items:**
- Uses TanStack Router's `createFileRoute`
- Fetches data with `useQuery` calling generated service (`ProjectsService.readProjects`)
- Renders table with columns for each field
- Each row has `ActionsMenu` for edit/delete
- "Add" button opens `AddProject` modal
- Pagination with skip/limit query params
- Query key: `["projects"]`

#### `frontend/src/components/Projects/AddProject.tsx`

Create project modal/form.

**Pattern from items:**
- `useDisclosure` from Chakra for modal open/close
- `react-hook-form` with field validation
- `useMutation` with generated `ProjectsService.createProject`
- On success: invalidate `["projects"]` query key, show success toast, close modal, reset form

#### `frontend/src/components/Projects/EditProject.tsx`

Edit project modal/form.

**Pattern from items:**
- Receives existing project as prop (typed as `ProjectPublic`)
- Pre-populates form fields with current values
- `useMutation` with generated `ProjectsService.updateProject`
- On success: invalidate `["projects"]` query key, show success toast, close modal

### Files to Modify

#### `frontend/src/components/Common/SidebarItems.tsx`

Add "Projects" navigation link alongside the existing "Items" link.

#### Regenerate API Client

After backend changes, regenerate the frontend client so `ProjectsService`, `ProjectCreate`, `ProjectUpdate`, `ProjectPublic`, `ProjectsPublic` types are available:

```bash
cd frontend
npm run generate-client
```

This updates:
- `frontend/src/client/services.gen.ts`
- `frontend/src/client/types.gen.ts`
- `frontend/src/client/schemas.gen.ts`

---

## Service Call Patterns (after client regeneration)

```typescript
// List
ProjectsService.readProjects({ skip, limit })
// Create
ProjectsService.createProject({ requestBody: data })
// Update
ProjectsService.updateProject({ id: projectId, requestBody: data })
// Delete
ProjectsService.deleteProject({ id: projectId })
```

---

## Implementation Order

1. **Backend models** — Add all Project models/schemas to `models.py`
2. **Backend CRUD** — Add `create_project()` to `crud.py`
3. **Backend routes** — Create `api/routes/projects.py` with all endpoints
4. **Register router** — Add to `api/main.py`
5. **Database migration** — `alembic revision --autogenerate` + `alembic upgrade head`
6. **Regenerate frontend client** — `npm run generate-client`
7. **Frontend route page** — Create `routes/_layout/projects.tsx`
8. **Frontend components** — Create `AddProject.tsx` and `EditProject.tsx`
9. **Sidebar navigation** — Add "Projects" link to `SidebarItems.tsx`

---

## Key Patterns Summary

| Concern | Pattern |
|---|---|
| Primary keys | UUID (`uuid.uuid4`) |
| Access control | Owner-based: owner or superuser |
| Pagination | `skip`/`limit` with count query |
| Schema inheritance | Base → Create / Update / Public / ListPublic |
| Dependency injection | `SessionDep`, `CurrentUser` |
| Frontend data fetching | TanStack Query (`useQuery` / `useMutation`) |
| Frontend routing | TanStack Router (`createFileRoute`) |
| Frontend forms | React Hook Form + Chakra UI |
| Delete confirmation | Reusable `ActionsMenu` + `DeleteAlert` |
| Notifications | `useCustomToast` hook |

▸ Time: 10s
