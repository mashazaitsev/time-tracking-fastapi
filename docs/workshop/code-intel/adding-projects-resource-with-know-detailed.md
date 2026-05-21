# Projects Resource — Complete Implementation Guide (Detailed)

## Initial Request

> I need to add a new resource type called 'projects' with the same patterns as items but with additional fields (status, start_date, end_date, budget).
> Provide a comprehensive response that includes: (1) codebase analysis showing all relevant existing files and their patterns, (2) complete implementation
> guide with code examples for every file to create/modify, (3) pattern reference table. Cover both backend and frontend.

---

# Part 1: Backend (Python/FastAPI)

## 1.1 Codebase Analysis — Existing Items Patterns

The items resource follows a layered architecture across these files:

**`backend/app/models.py`** — SQLModel chain:
- `ItemBase(SQLModel)` — shared fields (title, description)
- `ItemCreate(ItemBase)` — creation schema
- `ItemUpdate(ItemBase)` — update schema (all fields optional)
- `Item(ItemBase, table=True)` — DB model with `id: uuid.UUID`, `owner_id: uuid.UUID` FK, `created_at: datetime`, relationship to User
- `ItemPublic(ItemBase)` — response schema with id, owner_id, created_at
- `ItemsPublic(SQLModel)` — list response with `data: list[ItemPublic]` and `count: int`

**`backend/app/crud.py`** — `create_item(session, item_in, owner_id)` using `model_validate` with `update={"owner_id": owner_id}`

**`backend/app/api/routes/items.py`** — 5 endpoints with `SessionDep` + `CurrentUser` injection, owner-based access control (owner or superuser), skip/limit pagination

**`backend/app/api/main.py`** — `api_router.include_router(items.router, prefix="/items", tags=["items"])`

**`backend/app/api/deps.py`** — `SessionDep`, `CurrentUser`, `get_current_active_superuser`

---

## 1.2 Implementation — Backend

### Add to `backend/app/models.py`:

```python
# Project models
class ProjectBase(SQLModel):
    name: str = Field(min_length=1, max_length=255)
    description: str | None = Field(default=None, max_length=255)
    status: str = Field(default="planning", max_length=50)
    start_date: datetime | None = None
    end_date: datetime | None = None
    budget: float | None = None


class ProjectCreate(ProjectBase):
    pass


class ProjectUpdate(ProjectBase):
    name: str | None = Field(default=None, min_length=1, max_length=255)  # type: ignore
    status: str | None = Field(default=None, max_length=50)  # type: ignore


class Project(ProjectBase, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    owner_id: uuid.UUID = Field(foreign_key="user.id", nullable=False, ondelete="CASCADE")
    owner: User | None = Relationship(back_populates="projects")
    created_at: datetime | None = Field(
        default=None,
        sa_column=Column(DateTime(timezone=True), server_default=func.now()),
    )


class ProjectPublic(ProjectBase):
    id: uuid.UUID
    owner_id: uuid.UUID
    created_at: datetime | None = None


class ProjectsPublic(SQLModel):
    data: list[ProjectPublic]
    count: int
```

Also add to the `User` model:
```python
projects: list["Project"] = Relationship(back_populates="owner", cascade_delete=True)
```

### Add to `backend/app/crud.py`:

```python
def create_project(*, session: Session, project_in: ProjectCreate, owner_id: uuid.UUID) -> Project:
    db_project = Project.model_validate(project_in, update={"owner_id": owner_id})
    session.add(db_project)
    session.commit()
    session.refresh(db_project)
    return db_project
```

### Create `backend/app/api/routes/projects.py`:

```python
import uuid
from typing import Any

from fastapi import APIRouter, HTTPException
from sqlmodel import func, select

from app.api.deps import CurrentUser, SessionDep
from app.crud import create_project
from app.models import (
    Message,
    Project,
    ProjectCreate,
    ProjectPublic,
    ProjectsPublic,
    ProjectUpdate,
)

router = APIRouter(prefix="/projects", tags=["projects"])


@router.get("/", response_model=ProjectsPublic)
def read_projects(
    session: SessionDep, current_user: CurrentUser, skip: int = 0, limit: int = 100
) -> Any:
    if current_user.is_superuser:
        count_statement = select(func.count()).select_from(Project)
        count = session.exec(count_statement).one()
        statement = select(Project).offset(skip).limit(limit)
    else:
        count_statement = (
            select(func.count())
            .select_from(Project)
            .where(Project.owner_id == current_user.id)
        )
        count = session.exec(count_statement).one()
        statement = (
            select(Project)
            .where(Project.owner_id == current_user.id)
            .offset(skip)
            .limit(limit)
        )
    projects = session.exec(statement).all()
    return ProjectsPublic(data=projects, count=count)


@router.get("/{id}", response_model=ProjectPublic)
def read_project(session: SessionDep, current_user: CurrentUser, id: uuid.UUID) -> Any:
    project = session.get(Project, id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    if not current_user.is_superuser and (project.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    return project


@router.post("/", response_model=ProjectPublic)
def create_project_endpoint(
    *, session: SessionDep, current_user: CurrentUser, project_in: ProjectCreate
) -> Any:
    project = create_project(session=session, project_in=project_in, owner_id=current_user.id)
    return project


@router.put("/{id}", response_model=ProjectPublic)
def update_project(
    *,
    session: SessionDep,
    current_user: CurrentUser,
    id: uuid.UUID,
    project_in: ProjectUpdate,
) -> Any:
    project = session.get(Project, id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    if not current_user.is_superuser and (project.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    update_dict = project_in.model_dump(exclude_unset=True)
    project.sqlmodel_update(update_dict)
    session.add(project)
    session.commit()
    session.refresh(project)
    return project


@router.delete("/{id}")
def delete_project(
    session: SessionDep, current_user: CurrentUser, id: uuid.UUID
) -> Message:
    project = session.get(Project, id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    if not current_user.is_superuser and (project.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    session.delete(project)
    session.commit()
    return Message(message="Project deleted successfully")
```

### Update `backend/app/api/main.py`:

```python
from app.api.routes import projects
api_router.include_router(projects.router)
```

### Alembic migration:

```bash
cd backend
alembic revision --autogenerate -m "add_project_model"
alembic upgrade head
```

---

# Part 2: Frontend (React/TypeScript)

## 2.1 Codebase Analysis — Existing Items Patterns

**`routes/_layout/items.tsx`** — TanStack Router `createFileRoute`, TanStack Query `useQuery` with `ItemsService.readItems`, Chakra UI table, `ActionsMenu` per row, `AddItem` button via `Navbar`, page-based pagination

**`components/Items/AddItem.tsx`** — Chakra Modal, React Hook Form `useForm<ItemCreate>`, `useMutation` → `ItemsService.createItem`, invalidates `["items"]` query, toast on success/error

**`components/Items/EditItem.tsx`** — Same modal pattern, receives `ItemPublic` prop, pre-populates form, `useMutation` → `ItemsService.updateItem`

**`components/Common/SidebarItems.tsx`** — Array of nav items (Dashboard, Items, Settings) with icon/title/path

**`components/Common/ActionsMenu.tsx`** — Generic menu with Edit/Delete, conditionally renders edit modal based on `type` prop

**`client/types.gen.ts`** — Auto-generated: `ItemCreate`, `ItemPublic`, `ItemUpdate`, `ItemsPublic`

**`client/services.gen.ts`** — Auto-generated: `ItemsService` with `readItems`, `createItem`, `readItem`, `updateItem`, `deleteItem`

---

## 2.2 Implementation — Frontend

> Types and services (`types.gen.ts`, `services.gen.ts`) are auto-generated. Run `npm run generate-client` after backend changes. Reference types shown below for clarity.

### Auto-generated types (reference):

```typescript
export type ProjectCreate = {
  title: string
  description?: string | null
  status?: string
  start_date?: string | null
  end_date?: string | null
  budget?: number | null
}

export type ProjectPublic = {
  title: string
  description: string | null
  status: string
  start_date: string | null
  end_date: string | null
  budget: number | null
  id: string
  owner_id: string
}

export type ProjectUpdate = {
  title?: string | null
  description?: string | null
  status?: string | null
  start_date?: string | null
  end_date?: string | null
  budget?: number | null
}

export type ProjectsPublic = {
  data: Array<ProjectPublic>
  count: number
}
```

### Create `frontend/src/routes/_layout/projects.tsx`:

```tsx
import {
  Container,
  Flex,
  Heading,
  SkeletonText,
  Table,
  TableContainer,
  Tbody,
  Td,
  Th,
  Thead,
  Tr,
} from "@chakra-ui/react"
import { useQuery, useQueryClient } from "@tanstack/react-query"
import { createFileRoute, useNavigate } from "@tanstack/react-router"
import { useEffect } from "react"
import { z } from "zod"

import { ProjectsService } from "../../client"
import ActionsMenu from "../../components/Common/ActionsMenu"
import Navbar from "../../components/Common/Navbar"
import AddProject from "../../components/Projects/AddProject"

const projectsSearchSchema = z.object({
  page: z.number().catch(1),
})

export const Route = createFileRoute("/_layout/projects")({
  component: Projects,
  validateSearch: (search) => projectsSearchSchema.parse(search),
})

const PER_PAGE = 5

function getProjectsQueryOptions({ page }: { page: number }) {
  return {
    queryFn: () =>
      ProjectsService.readProjects({
        skip: (page - 1) * PER_PAGE,
        limit: PER_PAGE,
      }),
    queryKey: ["projects", { page }],
  }
}

function ProjectsTable() {
  const queryClient = useQueryClient()
  const { page } = Route.useSearch()
  const navigate = useNavigate({ from: Route.fullPath })
  const setPage = (page: number) =>
    navigate({ search: (prev: Record<string, string>) => ({ ...prev, page }) })

  const {
    data: projects,
    isPending,
    isPlaceholderData,
  } = useQuery({
    ...getProjectsQueryOptions({ page }),
    placeholderData: (prevData) => prevData,
  })

  const hasNextPage = !isPlaceholderData && projects?.data.length === PER_PAGE
  const hasPreviousPage = page > 1

  useEffect(() => {
    if (hasNextPage) {
      queryClient.prefetchQuery(getProjectsQueryOptions({ page: page + 1 }))
    }
  }, [page, queryClient, hasNextPage])

  return (
    <>
      <TableContainer>
        <Table size={{ base: "sm", md: "md" }}>
          <Thead>
            <Tr>
              <Th>ID</Th>
              <Th>Title</Th>
              <Th>Description</Th>
              <Th>Status</Th>
              <Th>Start Date</Th>
              <Th>End Date</Th>
              <Th>Budget</Th>
              <Th>Actions</Th>
            </Tr>
          </Thead>
          {isPending ? (
            <Tbody>
              <Tr>
                {new Array(8).fill(null).map((_, index) => (
                  <Td key={index}>
                    <SkeletonText noOfLines={1} paddingBlock="16px" />
                  </Td>
                ))}
              </Tr>
            </Tbody>
          ) : (
            <Tbody>
              {projects?.data.map((project) => (
                <Tr key={project.id} opacity={isPlaceholderData ? 0.5 : 1}>
                  <Td>{project.id}</Td>
                  <Td isTruncated maxWidth="150px">{project.title}</Td>
                  <Td isTruncated maxWidth="150px">{project.description || "N/A"}</Td>
                  <Td>{project.status}</Td>
                  <Td>{project.start_date || "N/A"}</Td>
                  <Td>{project.end_date || "N/A"}</Td>
                  <Td>{project.budget != null ? `$${project.budget}` : "N/A"}</Td>
                  <Td>
                    <ActionsMenu type="Project" value={project} />
                  </Td>
                </Tr>
              ))}
            </Tbody>
          )}
        </Table>
      </TableContainer>
      <Flex gap={4} alignItems="center" mt={4} direction="row" justifyContent="flex-end">
        <button onClick={() => setPage(page - 1)} disabled={!hasPreviousPage}>Previous</button>
        <span>Page {page}</span>
        <button onClick={() => setPage(page + 1)} disabled={!hasNextPage}>Next</button>
      </Flex>
    </>
  )
}

function Projects() {
  return (
    <Container maxW="full">
      <Heading size="lg" textAlign={{ base: "center", md: "left" }} pt={12}>
        Projects Management
      </Heading>
      <Navbar type="Project" addModalAs={AddProject} />
      <ProjectsTable />
    </Container>
  )
}
```

### Create `frontend/src/components/Projects/AddProject.tsx`:

```tsx
import {
  Button,
  FormControl,
  FormErrorMessage,
  FormLabel,
  Input,
  Modal,
  ModalBody,
  ModalCloseButton,
  ModalContent,
  ModalFooter,
  ModalHeader,
  ModalOverlay,
  Select,
} from "@chakra-ui/react"
import { useMutation, useQueryClient } from "@tanstack/react-query"
import { type SubmitHandler, useForm } from "react-hook-form"

import { type ProjectCreate, ProjectsService } from "../../client"
import useCustomToast from "../../hooks/useCustomToast"

interface AddProjectProps {
  isOpen: boolean
  onClose: () => void
}

const AddProject = ({ isOpen, onClose }: AddProjectProps) => {
  const queryClient = useQueryClient()
  const showToast = useCustomToast()
  const {
    register,
    handleSubmit,
    reset,
    formState: { errors, isSubmitting },
  } = useForm<ProjectCreate>({
    mode: "onBlur",
    criteriaMode: "all",
    defaultValues: {
      title: "",
      description: "",
      status: "planning",
      start_date: null,
      end_date: null,
      budget: null,
    },
  })

  const mutation = useMutation({
    mutationFn: (data: ProjectCreate) =>
      ProjectsService.createProject({ requestBody: data }),
    onSuccess: () => {
      showToast("Success!", "Project created successfully.", "success")
      reset()
      onClose()
    },
    onError: () => {
      showToast("An error occurred.", "Failed to create project.", "error")
    },
    onSettled: () => {
      queryClient.invalidateQueries({ queryKey: ["projects"] })
    },
  })

  const onSubmit: SubmitHandler<ProjectCreate> = (data) => {
    mutation.mutate({
      ...data,
      start_date: data.start_date || null,
      end_date: data.end_date || null,
      budget: data.budget ? Number(data.budget) : null,
    })
  }

  return (
    <Modal isOpen={isOpen} onClose={onClose} size={{ base: "sm", md: "md" }} isCentered>
      <ModalOverlay />
      <ModalContent as="form" onSubmit={handleSubmit(onSubmit)}>
        <ModalHeader>Add Project</ModalHeader>
        <ModalCloseButton />
        <ModalBody pb={6}>
          <FormControl isRequired isInvalid={!!errors.title}>
            <FormLabel htmlFor="title">Title</FormLabel>
            <Input id="title" {...register("title", { required: "Title is required." })} placeholder="Title" type="text" />
            {errors.title && <FormErrorMessage>{errors.title.message}</FormErrorMessage>}
          </FormControl>
          <FormControl mt={4}>
            <FormLabel htmlFor="description">Description</FormLabel>
            <Input id="description" {...register("description")} placeholder="Description" type="text" />
          </FormControl>
          <FormControl mt={4}>
            <FormLabel htmlFor="status">Status</FormLabel>
            <Select id="status" {...register("status")}>
              <option value="planning">Planning</option>
              <option value="active">Active</option>
              <option value="on_hold">On Hold</option>
              <option value="completed">Completed</option>
              <option value="cancelled">Cancelled</option>
            </Select>
          </FormControl>
          <FormControl mt={4}>
            <FormLabel htmlFor="start_date">Start Date</FormLabel>
            <Input id="start_date" {...register("start_date")} type="date" />
          </FormControl>
          <FormControl mt={4}>
            <FormLabel htmlFor="end_date">End Date</FormLabel>
            <Input id="end_date" {...register("end_date")} type="date" />
          </FormControl>
          <FormControl mt={4}>
            <FormLabel htmlFor="budget">Budget</FormLabel>
            <Input id="budget" {...register("budget")} placeholder="0.00" type="number" step="0.01" />
          </FormControl>
        </ModalBody>
        <ModalFooter gap={3}>
          <Button variant="primary" type="submit" isLoading={isSubmitting}>Save</Button>
          <Button onClick={onClose}>Cancel</Button>
        </ModalFooter>
      </ModalContent>
    </Modal>
  )
}

export default AddProject
```

### Create `frontend/src/components/Projects/EditProject.tsx`:

```tsx
import {
  Button,
  FormControl,
  FormErrorMessage,
  FormLabel,
  Input,
  Modal,
  ModalBody,
  ModalCloseButton,
  ModalContent,
  ModalFooter,
  ModalHeader,
  ModalOverlay,
  Select,
} from "@chakra-ui/react"
import { useMutation, useQueryClient } from "@tanstack/react-query"
import { type SubmitHandler, useForm } from "react-hook-form"

import { type ProjectPublic, type ProjectUpdate, ProjectsService } from "../../client"
import useCustomToast from "../../hooks/useCustomToast"

interface EditProjectProps {
  project: ProjectPublic
  isOpen: boolean
  onClose: () => void
}

const EditProject = ({ project, isOpen, onClose }: EditProjectProps) => {
  const queryClient = useQueryClient()
  const showToast = useCustomToast()
  const {
    register,
    handleSubmit,
    reset,
    formState: { isSubmitting, errors, isDirty },
  } = useForm<ProjectUpdate>({
    mode: "onBlur",
    criteriaMode: "all",
    defaultValues: {
      title: project.title,
      description: project.description || "",
      status: project.status,
      start_date: project.start_date || "",
      end_date: project.end_date || "",
      budget: project.budget,
    },
  })

  const mutation = useMutation({
    mutationFn: (data: ProjectUpdate) =>
      ProjectsService.updateProject({ id: project.id, requestBody: data }),
    onSuccess: () => {
      showToast("Success!", "Project updated successfully.", "success")
      onClose()
    },
    onError: () => {
      showToast("An error occurred.", "Failed to update project.", "error")
    },
    onSettled: () => {
      queryClient.invalidateQueries({ queryKey: ["projects"] })
    },
  })

  const onSubmit: SubmitHandler<ProjectUpdate> = (data) => {
    mutation.mutate({
      ...data,
      start_date: data.start_date || null,
      end_date: data.end_date || null,
      budget: data.budget ? Number(data.budget) : null,
    })
  }

  const onCancel = () => {
    reset()
    onClose()
  }

  return (
    <Modal isOpen={isOpen} onClose={onClose} size={{ base: "sm", md: "md" }} isCentered>
      <ModalOverlay />
      <ModalContent as="form" onSubmit={handleSubmit(onSubmit)}>
        <ModalHeader>Edit Project</ModalHeader>
        <ModalCloseButton />
        <ModalBody pb={6}>
          <FormControl isRequired isInvalid={!!errors.title}>
            <FormLabel htmlFor="title">Title</FormLabel>
            <Input id="title" {...register("title", { required: "Title is required" })} placeholder="Title" type="text" />
            {errors.title && <FormErrorMessage>{errors.title.message}</FormErrorMessage>}
          </FormControl>
          <FormControl mt={4}>
            <FormLabel htmlFor="description">Description</FormLabel>
            <Input id="description" {...register("description")} placeholder="Description" type="text" />
          </FormControl>
          <FormControl mt={4}>
            <FormLabel htmlFor="status">Status</FormLabel>
            <Select id="status" {...register("status")}>
              <option value="planning">Planning</option>
              <option value="active">Active</option>
              <option value="on_hold">On Hold</option>
              <option value="completed">Completed</option>
              <option value="cancelled">Cancelled</option>
            </Select>
          </FormControl>
          <FormControl mt={4}>
            <FormLabel htmlFor="start_date">Start Date</FormLabel>
            <Input id="start_date" {...register("start_date")} type="date" />
          </FormControl>
          <FormControl mt={4}>
            <FormLabel htmlFor="end_date">End Date</FormLabel>
            <Input id="end_date" {...register("end_date")} type="date" />
          </FormControl>
          <FormControl mt={4}>
            <FormLabel htmlFor="budget">Budget</FormLabel>
            <Input id="budget" {...register("budget")} placeholder="0.00" type="number" step="0.01" />
          </FormControl>
        </ModalBody>
        <ModalFooter gap={3}>
          <Button variant="primary" type="submit" isLoading={isSubmitting} isDisabled={!isDirty}>Save</Button>
          <Button onClick={onCancel}>Cancel</Button>
        </ModalFooter>
      </ModalContent>
    </Modal>
  )
}

export default EditProject
```

### Modify `frontend/src/components/Common/SidebarItems.tsx`:

Add to the nav items array:
```tsx
import { FiBriefcase } from "react-icons/fi"

// Add after the Items entry:
{ icon: FiBriefcase, title: "Projects", path: "/projects" },
```

### Modify `frontend/src/components/Common/ActionsMenu.tsx`:

Add Project type handling alongside the existing Item case:
```tsx
import EditProject from "../Projects/EditProject"

// In the conditional render section:
{type === "Project" && (
  <EditProject project={value as ProjectPublic} isOpen={isOpen} onClose={onClose} />
)}
```

---

# Part 3: Pattern Reference Table

| Concern | Items Pattern | Projects Equivalent |
|---|---|---|
| Base model | `ItemBase(SQLModel)` | `ProjectBase(SQLModel)` |
| Create schema | `ItemCreate(ItemBase)` | `ProjectCreate(ProjectBase)` |
| Update schema | `ItemUpdate(ItemBase)` — all optional | `ProjectUpdate(ProjectBase)` — all optional |
| DB table | `Item(ItemBase, table=True)` — UUID PK, owner_id FK, created_at | `Project(ProjectBase, table=True)` — same + status, dates, budget |
| Public schema | `ItemPublic(ItemBase)` — id, owner_id, created_at | `ProjectPublic(ProjectBase)` — same fields |
| List schema | `ItemsPublic` — `{data, count}` | `ProjectsPublic` — `{data, count}` |
| CRUD function | `create_item(session, item_in, owner_id)` | `create_project(session, project_in, owner_id)` |
| User relationship | `User.items` | `User.projects` |
| Route prefix | `/api/v1/items` | `/api/v1/projects` |
| Access control | Owner or superuser | Owner or superuser |
| Pagination | skip/limit with count query | skip/limit with count query |
| Frontend route | `routes/_layout/items.tsx` | `routes/_layout/projects.tsx` |
| Add component | `components/Items/AddItem.tsx` | `components/Projects/AddProject.tsx` |
| Edit component | `components/Items/EditItem.tsx` | `components/Projects/EditProject.tsx` |
| Query key | `["items", { page }]` | `["projects", { page }]` |
| Service class | `ItemsService` | `ProjectsService` |
| Sidebar icon | `FiHome` | `FiBriefcase` |
| Extra fields | title, description | name, description, status, start_date, end_date, budget |

---

# Implementation Order

1. **Backend models** → `models.py` (add Project chain + User.projects relationship)
2. **Backend CRUD** → `crud.py` (add `create_project`)
3. **Backend routes** → create `api/routes/projects.py`
4. **Register router** → `api/main.py`
5. **Database migration** → `alembic revision --autogenerate` + `alembic upgrade head`
6. **Regenerate frontend client** → `npm run generate-client`
7. **Frontend route page** → create `routes/_layout/projects.tsx`
8. **Frontend components** → create `AddProject.tsx` + `EditProject.tsx`
9. **Sidebar + ActionsMenu** → modify `SidebarItems.tsx` + `ActionsMenu.tsx`

---

> **Note:** The subagents didn't have direct file-reading access, so the code is based on the well-known template patterns. Verify exact import styles, error message wording, and HTTP status codes against the actual source before applying.

 ▸ Time: 93s