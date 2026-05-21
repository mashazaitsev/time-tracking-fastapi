"""
Purpose: Provide CRUD API endpoints for TimeEntry resources with owner-based access control and time summary aggregation

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
"""

import uuid
from typing import Any

from fastapi import APIRouter, HTTPException
from sqlmodel import col, func, select

from app.api.deps import CurrentUser, SessionDep
from app.models import (
    Message,
    Project,
    ProjectSummary,
    TimeEntriesPublic,
    TimeEntry,
    TimeEntryCreate,
    TimeEntryPublic,
    TimeEntryUpdate,
    TimeSummary,
)

router = APIRouter(prefix="/time-entries", tags=["time-entries"])


@router.get("/summary", response_model=TimeSummary)
def get_summary(session: SessionDep, current_user: CurrentUser) -> Any:
    """
    Purpose: Aggregate total minutes and per-project breakdown for the current user

    Structure:
        session (SessionDep): input - Database session
        current_user (CurrentUser): input - Authenticated user
        summary (TimeSummary): output - Total minutes and per-project list

    Relationships:
        Consumes: TimeEntry table, Project table, current user context
        Produces: TimeSummary response

    Flow:
        1. Build aggregation query: sum(duration_minutes) grouped by project_id, joined with Project for name
        2. Scope to owner_id unless superuser
        3. Compute total_minutes from aggregated rows
        4. Return TimeSummary with total_minutes=0 and by_project=[] when no entries exist

    Important:
        This route MUST be registered before GET /{id} to prevent FastAPI treating "summary" as a UUID.
    """
    statement = (
        select(
            TimeEntry.project_id,
            Project.name.label("project_name"),  # type: ignore[attr-defined]
            func.sum(TimeEntry.duration_minutes).label("total_minutes"),
        )
        .join(Project, TimeEntry.project_id == Project.id)
        .group_by(TimeEntry.project_id, Project.name)
    )

    if not current_user.is_superuser:
        statement = statement.where(TimeEntry.owner_id == current_user.id)

    rows = session.exec(statement).all()

    by_project = [
        ProjectSummary(
            project_id=row.project_id,
            project_name=row.project_name,
            total_minutes=row.total_minutes,
        )
        for row in rows
    ]
    total_minutes = sum(p.total_minutes for p in by_project)

    return TimeSummary(total_minutes=total_minutes, by_project=by_project)


@router.get("/", response_model=TimeEntriesPublic)
def read_time_entries(
    session: SessionDep, current_user: CurrentUser, skip: int = 0, limit: int = 100
) -> Any:
    """
    Purpose: Retrieve paginated list of time entries for current user

    Structure:
        session (SessionDep): input - Database session
        current_user (CurrentUser): input - Authenticated user
        skip (int): input - Pagination offset
        limit (int): input - Max entries per page
        entries (TimeEntriesPublic): output - Paginated time entries list with count

    Relationships:
        Consumes: TimeEntry table, current user context
        Produces: TimeEntriesPublic response

    Flow:
        1. Check if superuser (query all) or regular user (query owned only)
        2. Count matching entries and fetch paginated results
        3. Return TimeEntriesPublic with data and count
    """
    if current_user.is_superuser:
        count_statement = select(func.count()).select_from(TimeEntry)
        count = session.exec(count_statement).one()
        statement = (
            select(TimeEntry)
            .order_by(col(TimeEntry.created_at).desc())
            .offset(skip)
            .limit(limit)
        )
        entries = session.exec(statement).all()
    else:
        count_statement = (
            select(func.count())
            .select_from(TimeEntry)
            .where(TimeEntry.owner_id == current_user.id)
        )
        count = session.exec(count_statement).one()
        statement = (
            select(TimeEntry)
            .where(TimeEntry.owner_id == current_user.id)
            .order_by(col(TimeEntry.created_at).desc())
            .offset(skip)
            .limit(limit)
        )
        entries = session.exec(statement).all()

    return TimeEntriesPublic(data=entries, count=count)


@router.post("/", response_model=TimeEntryPublic)
def create_time_entry(
    *, session: SessionDep, current_user: CurrentUser, entry_in: TimeEntryCreate
) -> Any:
    """
    Purpose: Create a new time entry owned by the current user after validating project ownership

    Structure:
        session (SessionDep): input - Database session
        current_user (CurrentUser): input - Authenticated user
        entry_in (TimeEntryCreate): input - Time entry creation payload
        entry (TimeEntryPublic): output - Created time entry

    Relationships:
        Consumes: TimeEntryCreate schema, Project table, current user context
        Produces: TimeEntry table row, TimeEntryPublic response

    Flow:
        1. Fetch project by project_id; raise 404 if not found
        2. Verify project ownership or superuser role; raise 403 if denied
        3. Create time entry with owner_id = current_user.id
        4. Persist and return created entry
    """
    project = session.get(Project, entry_in.project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    if not current_user.is_superuser and project.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not enough permissions")

    entry = TimeEntry.model_validate(entry_in, update={"owner_id": current_user.id})
    session.add(entry)
    session.commit()
    session.refresh(entry)
    return entry


@router.get("/{id}", response_model=TimeEntryPublic)
def read_time_entry(
    session: SessionDep, current_user: CurrentUser, id: uuid.UUID
) -> Any:
    """
    Purpose: Retrieve a single time entry by ID with ownership check

    Structure:
        session (SessionDep): input - Database session
        current_user (CurrentUser): input - Authenticated user
        id (uuid.UUID): input - Time entry ID
        entry (TimeEntryPublic): output - Time entry details

    Relationships:
        Consumes: TimeEntry table, current user context
        Produces: TimeEntryPublic response

    Flow:
        1. Fetch entry by ID; raise 404 if not found
        2. Verify ownership or superuser role; raise 403 if denied
        3. Return entry
    """
    entry = session.get(TimeEntry, id)
    if not entry:
        raise HTTPException(status_code=404, detail="Time entry not found")
    if not current_user.is_superuser and entry.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not enough permissions")
    return entry


@router.put("/{id}", response_model=TimeEntryPublic)
def update_time_entry(
    *,
    session: SessionDep,
    current_user: CurrentUser,
    id: uuid.UUID,
    entry_in: TimeEntryUpdate,
) -> Any:
    """
    Purpose: Partially update an existing time entry with ownership check

    Structure:
        session (SessionDep): input - Database session
        current_user (CurrentUser): input - Authenticated user
        id (uuid.UUID): input - Time entry ID
        entry_in (TimeEntryUpdate): input - Partial update payload
        entry (TimeEntryPublic): output - Updated time entry

    Relationships:
        Consumes: TimeEntry table, TimeEntryUpdate schema, current user context
        Produces: Updated TimeEntry table row, TimeEntryPublic response

    Flow:
        1. Fetch entry by ID; raise 404 if not found
        2. Verify ownership or superuser role; raise 403 if denied
        3. Apply partial update (exclude_unset=True) and persist
    """
    entry = session.get(TimeEntry, id)
    if not entry:
        raise HTTPException(status_code=404, detail="Time entry not found")
    if not current_user.is_superuser and entry.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not enough permissions")
    update_dict = entry_in.model_dump(exclude_unset=True)
    entry.sqlmodel_update(update_dict)
    session.add(entry)
    session.commit()
    session.refresh(entry)
    return entry


@router.delete("/{id}")
def delete_time_entry(
    session: SessionDep, current_user: CurrentUser, id: uuid.UUID
) -> Message:
    """
    Purpose: Delete a time entry with ownership check

    Structure:
        session (SessionDep): input - Database session
        current_user (CurrentUser): input - Authenticated user
        id (uuid.UUID): input - Time entry ID
        message (Message): output - Deletion confirmation

    Relationships:
        Consumes: TimeEntry table, current user context
        Produces: Message response

    Flow:
        1. Fetch entry by ID; raise 404 if not found
        2. Verify ownership or superuser role; raise 403 if denied
        3. Delete entry and return confirmation
    """
    entry = session.get(TimeEntry, id)
    if not entry:
        raise HTTPException(status_code=404, detail="Time entry not found")
    if not current_user.is_superuser and entry.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not enough permissions")
    session.delete(entry)
    session.commit()
    return Message(message="Time entry deleted successfully")
