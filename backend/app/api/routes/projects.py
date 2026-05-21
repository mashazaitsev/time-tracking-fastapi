"""
Purpose: Provide CRUD API endpoints for Project resources with owner-based access control

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
"""

import uuid
from typing import Any

from fastapi import APIRouter, HTTPException
from sqlmodel import col, func, select

from app.api.deps import CurrentUser, SessionDep
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
    """
    Purpose: Retrieve paginated list of projects for current user

    Structure:
        session (SessionDep): input - Database session
        current_user (CurrentUser): input - Authenticated user
        skip (int): input - Pagination offset
        limit (int): input - Max projects per page
        projects (ProjectsPublic): output - Paginated projects list with count

    Flow:
        1. Check if superuser (query all) or regular user (query owned only)
        2. Count matching projects and fetch paginated results
        3. Return ProjectsPublic with data and count
    """
    if current_user.is_superuser:
        count_statement = select(func.count()).select_from(Project)
        count = session.exec(count_statement).one()
        statement = (
            select(Project)
            .order_by(col(Project.created_at).desc())
            .offset(skip)
            .limit(limit)
        )
        projects = session.exec(statement).all()
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
            .order_by(col(Project.created_at).desc())
            .offset(skip)
            .limit(limit)
        )
        projects = session.exec(statement).all()

    return ProjectsPublic(data=projects, count=count)


@router.post("/", response_model=ProjectPublic)
def create_project(
    *, session: SessionDep, current_user: CurrentUser, project_in: ProjectCreate
) -> Any:
    """
    Purpose: Create a new project owned by the current user

    Structure:
        session (SessionDep): input - Database session
        current_user (CurrentUser): input - Authenticated user
        project_in (ProjectCreate): input - Project creation payload
        project (ProjectPublic): output - Created project

    Flow:
        1. Validate input and set owner_id to current user
        2. Persist project to database
        3. Return created project
    """
    project = Project.model_validate(project_in, update={"owner_id": current_user.id})
    session.add(project)
    session.commit()
    session.refresh(project)
    return project


@router.get("/{id}", response_model=ProjectPublic)
def read_project(
    session: SessionDep, current_user: CurrentUser, id: uuid.UUID
) -> Any:
    """
    Purpose: Retrieve a single project by ID with ownership check

    Structure:
        session (SessionDep): input - Database session
        current_user (CurrentUser): input - Authenticated user
        id (uuid.UUID): input - Project ID
        project (ProjectPublic): output - Project details

    Flow:
        1. Fetch project by ID, raise 404 if not found
        2. Verify ownership or superuser role, raise 403 if denied
        3. Return project
    """
    project = session.get(Project, id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    if not current_user.is_superuser and (project.owner_id != current_user.id):
        raise HTTPException(status_code=403, detail="Not enough permissions")
    return project


@router.put("/{id}", response_model=ProjectPublic)
def update_project(
    *,
    session: SessionDep,
    current_user: CurrentUser,
    id: uuid.UUID,
    project_in: ProjectUpdate,
) -> Any:
    """
    Purpose: Update an existing project with ownership check

    Structure:
        session (SessionDep): input - Database session
        current_user (CurrentUser): input - Authenticated user
        id (uuid.UUID): input - Project ID
        project_in (ProjectUpdate): input - Partial update payload
        project (ProjectPublic): output - Updated project

    Flow:
        1. Fetch project by ID, raise 404 if not found
        2. Verify ownership or superuser role, raise 403 if denied
        3. Apply partial update and persist
    """
    project = session.get(Project, id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    if not current_user.is_superuser and (project.owner_id != current_user.id):
        raise HTTPException(status_code=403, detail="Not enough permissions")
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
    """
    Purpose: Delete a project with ownership check

    Structure:
        session (SessionDep): input - Database session
        current_user (CurrentUser): input - Authenticated user
        id (uuid.UUID): input - Project ID
        message (Message): output - Deletion confirmation

    Flow:
        1. Fetch project by ID, raise 404 if not found
        2. Verify ownership or superuser role, raise 403 if denied
        3. Delete project and return confirmation
    """
    project = session.get(Project, id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    if not current_user.is_superuser and (project.owner_id != current_user.id):
        raise HTTPException(status_code=403, detail="Not enough permissions")
    session.delete(project)
    session.commit()
    return Message(message="Project deleted successfully")
