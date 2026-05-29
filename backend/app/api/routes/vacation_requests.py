"""
Purpose: Provide CRUD API endpoints for VacationRequest resources with owner-based access control

Structure:
    read_vacation_requests (GET /): endpoint - List all vacation requests (team visibility)
    create_vacation_request (POST /): endpoint - Create vacation request for current user
    read_vacation_request (GET /{id}): endpoint - Get single vacation request by ID
    update_vacation_request (PUT /{id}): endpoint - Update vacation request (owner or superuser only)
    delete_vacation_request (DELETE /{id}): endpoint - Delete vacation request (owner or superuser only)

Relationships:
    Consumes: models.VacationRequest, models.VacationRequestCreate, models.VacationRequestUpdate
    Consumes: models.VacationRequestPublic, models.VacationRequestsPublic, api.deps.CurrentUser
    Produces: VacationRequestPublic, VacationRequestsPublic, Message responses

Semantics:
    Domain: vacation-management
    Entity: VacationRequest
    Logic: [All authenticated users see all requests (team visibility),
            any authenticated user can read any single request,
            owner or superuser required for update/delete,
            PUT merges partial updates and validates resulting date range,
            limit > 100 returns 422]
"""

import uuid
from typing import Any

from fastapi import APIRouter, HTTPException, Query
from sqlmodel import col, func, select

from app.api.deps import CurrentUser, SessionDep
from app.models import (
    Message,
    VacationRequest,
    VacationRequestCreate,
    VacationRequestPublic,
    VacationRequestsPublic,
    VacationRequestUpdate,
)

router = APIRouter(prefix="/vacation-requests", tags=["vacation-requests"])


@router.get("/", response_model=VacationRequestsPublic)
def read_vacation_requests(
    session: SessionDep,
    current_user: CurrentUser,
    skip: int = 0,
    limit: int = Query(default=100, le=100),
) -> Any:
    """
    Purpose: Retrieve paginated list of all vacation requests (team visibility)

    Structure:
        session (SessionDep): input - Database session
        current_user (CurrentUser): input - Authenticated user
        skip (int): input - Pagination offset (default 0)
        limit (int): input - Max entries per page (default 100, max 100)
        requests (VacationRequestsPublic): output - Paginated vacation requests with count

    Relationships:
        Consumes: VacationRequest table, current user context
        Produces: VacationRequestsPublic response

    Flow:
        1. Count all vacation requests
        2. Fetch paginated results ordered by created_at descending
        3. Return VacationRequestsPublic with data and count
    """
    count_statement = select(func.count()).select_from(VacationRequest)
    count = session.exec(count_statement).one()
    statement = (
        select(VacationRequest)
        .order_by(col(VacationRequest.created_at).desc())
        .offset(skip)
        .limit(limit)
    )
    requests = session.exec(statement).all()
    return VacationRequestsPublic(data=requests, count=count)


@router.post("/", response_model=VacationRequestPublic)
def create_vacation_request(
    *, session: SessionDep, current_user: CurrentUser, request_in: VacationRequestCreate
) -> Any:
    """
    Purpose: Create a new vacation request owned by the current user

    Structure:
        session (SessionDep): input - Database session
        current_user (CurrentUser): input - Authenticated user
        request_in (VacationRequestCreate): input - Vacation request creation payload
        vacation_request (VacationRequestPublic): output - Created vacation request

    Relationships:
        Consumes: VacationRequestCreate schema, current user context
        Produces: VacationRequest table row, VacationRequestPublic response

    Flow:
        1. Create VacationRequest with owner_id = current_user.id, status = "pending"
        2. Persist and return created request
    """
    vacation_request = VacationRequest.model_validate(
        request_in, update={"owner_id": current_user.id}
    )
    session.add(vacation_request)
    session.commit()
    session.refresh(vacation_request)
    return vacation_request


@router.get("/{id}", response_model=VacationRequestPublic)
def read_vacation_request(
    session: SessionDep, current_user: CurrentUser, id: uuid.UUID
) -> Any:
    """
    Purpose: Retrieve a single vacation request by ID (any authenticated user)

    Structure:
        session (SessionDep): input - Database session
        current_user (CurrentUser): input - Authenticated user
        id (uuid.UUID): input - Vacation request ID
        vacation_request (VacationRequestPublic): output - Vacation request details

    Relationships:
        Consumes: VacationRequest table
        Produces: VacationRequestPublic response

    Flow:
        1. Fetch request by ID; raise 404 if not found
        2. Return request (no ownership check on read)
    """
    vacation_request = session.get(VacationRequest, id)
    if not vacation_request:
        raise HTTPException(status_code=404, detail="Vacation request not found")
    return vacation_request


@router.put("/{id}", response_model=VacationRequestPublic)
def update_vacation_request(
    *,
    session: SessionDep,
    current_user: CurrentUser,
    id: uuid.UUID,
    request_in: VacationRequestUpdate,
) -> Any:
    """
    Purpose: Partially update an existing vacation request with ownership check and date range validation

    Structure:
        session (SessionDep): input - Database session
        current_user (CurrentUser): input - Authenticated user
        id (uuid.UUID): input - Vacation request ID
        request_in (VacationRequestUpdate): input - Partial update payload
        vacation_request (VacationRequestPublic): output - Updated vacation request

    Relationships:
        Consumes: VacationRequest table, VacationRequestUpdate schema, current user context
        Produces: Updated VacationRequest table row, VacationRequestPublic response

    Flow:
        1. Fetch request by ID; raise 404 if not found
        2. Verify ownership or superuser role; raise 403 if denied
        3. If empty payload, return unchanged
        4. Merge update with existing values and validate resulting date range
        5. Apply update and persist
    """
    vacation_request = session.get(VacationRequest, id)
    if not vacation_request:
        raise HTTPException(status_code=404, detail="Vacation request not found")
    if not current_user.is_superuser and vacation_request.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not enough permissions")

    update_dict = request_in.model_dump(exclude_unset=True)
    if not update_dict:
        return vacation_request

    # Merge update with existing values to validate resulting date range
    resulting_start = update_dict.get("start_date", vacation_request.start_date)
    resulting_end = update_dict.get("end_date", vacation_request.end_date)
    if resulting_end < resulting_start:
        raise HTTPException(
            status_code=422,
            detail="end_date must be greater than or equal to start_date",
        )

    vacation_request.sqlmodel_update(update_dict)
    session.add(vacation_request)
    session.commit()
    session.refresh(vacation_request)
    return vacation_request


@router.delete("/{id}")
def delete_vacation_request(
    session: SessionDep, current_user: CurrentUser, id: uuid.UUID
) -> Message:
    """
    Purpose: Delete a vacation request with ownership check

    Structure:
        session (SessionDep): input - Database session
        current_user (CurrentUser): input - Authenticated user
        id (uuid.UUID): input - Vacation request ID
        message (Message): output - Deletion confirmation

    Relationships:
        Consumes: VacationRequest table, current user context
        Produces: Message response

    Flow:
        1. Fetch request by ID; raise 404 if not found
        2. Verify ownership or superuser role; raise 403 if denied
        3. Delete request and return confirmation
    """
    vacation_request = session.get(VacationRequest, id)
    if not vacation_request:
        raise HTTPException(status_code=404, detail="Vacation request not found")
    if not current_user.is_superuser and vacation_request.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not enough permissions")
    session.delete(vacation_request)
    session.commit()
    return Message(message="Vacation request deleted successfully")
