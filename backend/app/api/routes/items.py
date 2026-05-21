"""
Purpose: Provide CRUD API endpoints for Item resources with owner-based access control

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
"""

import uuid
from typing import Any

from fastapi import APIRouter, HTTPException
from sqlmodel import col, func, select

from app.api.deps import CurrentUser, SessionDep
from app.models import Item, ItemCreate, ItemPublic, ItemsPublic, ItemUpdate, Message

router = APIRouter(prefix="/items", tags=["items"])


@router.get("/", response_model=ItemsPublic)
def read_items(
    session: SessionDep, current_user: CurrentUser, skip: int = 0, limit: int = 100
) -> Any:
    """
    Purpose: Retrieve paginated list of items for current user

    Structure:
        session (SessionDep): input - Database session
        current_user (CurrentUser): input - Authenticated user
        skip (int): input - Pagination offset
        limit (int): input - Max items per page
        items (ItemsPublic): output - Paginated items list with count

    Relationships:
        Consumes: Item table, current user context
        Produces: ItemsPublic response

    Flow:
        1. Check if superuser (query all) or regular user (query owned only)
        2. Count matching items and fetch paginated results
        3. Return ItemsPublic with data and count
    """

    if current_user.is_superuser:
        count_statement = select(func.count()).select_from(Item)
        count = session.exec(count_statement).one()
        statement = (
            select(Item).order_by(col(Item.created_at).desc()).offset(skip).limit(limit)
        )
        items = session.exec(statement).all()
    else:
        count_statement = (
            select(func.count())
            .select_from(Item)
            .where(Item.owner_id == current_user.id)
        )
        count = session.exec(count_statement).one()
        statement = (
            select(Item)
            .where(Item.owner_id == current_user.id)
            .order_by(col(Item.created_at).desc())
            .offset(skip)
            .limit(limit)
        )
        items = session.exec(statement).all()

    return ItemsPublic(data=items, count=count)


@router.get("/{id}", response_model=ItemPublic)
def read_item(session: SessionDep, current_user: CurrentUser, id: uuid.UUID) -> Any:
    """
    Purpose: Retrieve a single item by ID with ownership check

    Structure:
        session (SessionDep): input - Database session
        current_user (CurrentUser): input - Authenticated user
        id (uuid.UUID): input - Item ID
        item (ItemPublic): output - Item details

    Relationships:
        Consumes: Item table, current user context
        Produces: ItemPublic response

    Flow:
        1. Fetch item by ID, raise 404 if not found
        2. Verify ownership or superuser role, raise 403 if denied
        3. Return item
    """
    item = session.get(Item, id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    if not current_user.is_superuser and (item.owner_id != current_user.id):
        raise HTTPException(status_code=403, detail="Not enough permissions")
    return item


@router.post("/", response_model=ItemPublic)
def create_item(
    *, session: SessionDep, current_user: CurrentUser, item_in: ItemCreate
) -> Any:
    """
    Purpose: Create a new item owned by the current user

    Structure:
        session (SessionDep): input - Database session
        current_user (CurrentUser): input - Authenticated user
        item_in (ItemCreate): input - Item creation payload
        item (ItemPublic): output - Created item

    Relationships:
        Consumes: ItemCreate schema, current user context
        Produces: Item table row, ItemPublic response

    Flow:
        1. Validate input and set owner_id to current user
        2. Persist item to database
        3. Return created item
    """
    item = Item.model_validate(item_in, update={"owner_id": current_user.id})
    session.add(item)
    session.commit()
    session.refresh(item)
    return item


@router.put("/{id}", response_model=ItemPublic)
def update_item(
    *,
    session: SessionDep,
    current_user: CurrentUser,
    id: uuid.UUID,
    item_in: ItemUpdate,
) -> Any:
    """
    Purpose: Update an existing item with ownership check

    Structure:
        session (SessionDep): input - Database session
        current_user (CurrentUser): input - Authenticated user
        id (uuid.UUID): input - Item ID
        item_in (ItemUpdate): input - Partial update payload
        item (ItemPublic): output - Updated item

    Relationships:
        Consumes: Item table, ItemUpdate schema, current user context
        Produces: Updated Item table row, ItemPublic response

    Flow:
        1. Fetch item by ID, raise 404 if not found
        2. Verify ownership or superuser role, raise 403 if denied
        3. Apply partial update and persist
    """
    item = session.get(Item, id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    if not current_user.is_superuser and (item.owner_id != current_user.id):
        raise HTTPException(status_code=403, detail="Not enough permissions")
    update_dict = item_in.model_dump(exclude_unset=True)
    item.sqlmodel_update(update_dict)
    session.add(item)
    session.commit()
    session.refresh(item)
    return item


@router.delete("/{id}")
def delete_item(
    session: SessionDep, current_user: CurrentUser, id: uuid.UUID
) -> Message:
    """
    Purpose: Delete an item with ownership check

    Structure:
        session (SessionDep): input - Database session
        current_user (CurrentUser): input - Authenticated user
        id (uuid.UUID): input - Item ID
        message (Message): output - Deletion confirmation

    Relationships:
        Consumes: Item table, current user context
        Produces: Message response

    Flow:
        1. Fetch item by ID, raise 404 if not found
        2. Verify ownership or superuser role, raise 403 if denied
        3. Delete item and return confirmation
    """
    item = session.get(Item, id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    if not current_user.is_superuser and (item.owner_id != current_user.id):
        raise HTTPException(status_code=403, detail="Not enough permissions")
    session.delete(item)
    session.commit()
    return Message(message="Item deleted successfully")
