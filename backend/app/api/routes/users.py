"""
Purpose: Provide CRUD API endpoints for User management with role-based access control

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
"""

import uuid
from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import col, delete, func, select

from app import crud
from app.api.deps import (
    CurrentUser,
    SessionDep,
    get_current_active_superuser,
)
from app.core.config import settings
from app.core.security import get_password_hash, verify_password
from app.models import (
    Item,
    Message,
    UpdatePassword,
    User,
    UserCreate,
    UserPublic,
    UserRegister,
    UsersPublic,
    UserUpdate,
    UserUpdateMe,
)
from app.utils import generate_new_account_email, send_email

router = APIRouter(prefix="/users", tags=["users"])


@router.get(
    "/",
    dependencies=[Depends(get_current_active_superuser)],
    response_model=UsersPublic,
)
def read_users(session: SessionDep, skip: int = 0, limit: int = 100) -> Any:
    """
    Purpose: Retrieve paginated list of all users (superuser only)

    Structure:
        session (SessionDep): input - Database session
        skip (int): input - Pagination offset
        limit (int): input - Max users per page
        users (UsersPublic): output - Paginated users list with count

    Relationships:
        Consumes: User table
        Produces: UsersPublic response
    """

    count_statement = select(func.count()).select_from(User)
    count = session.exec(count_statement).one()

    statement = (
        select(User).order_by(col(User.created_at).desc()).offset(skip).limit(limit)
    )
    users = session.exec(statement).all()

    return UsersPublic(data=users, count=count)


@router.post(
    "/", dependencies=[Depends(get_current_active_superuser)], response_model=UserPublic
)
def create_user(*, session: SessionDep, user_in: UserCreate) -> Any:
    """
    Purpose: Create a new user (superuser only), send welcome email if SMTP configured

    Structure:
        session (SessionDep): input - Database session
        user_in (UserCreate): input - User creation payload
        user (UserPublic): output - Created user

    Relationships:
        Consumes: crud.get_user_by_email, crud.create_user, utils.send_email
        Produces: User table row, UserPublic response, welcome email

    Flow:
        1. Check email uniqueness, raise 400 if duplicate
        2. Create user via crud
        3. Send welcome email if SMTP enabled
    """
    user = crud.get_user_by_email(session=session, email=user_in.email)
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this email already exists in the system.",
        )

    user = crud.create_user(session=session, user_create=user_in)
    if settings.emails_enabled and user_in.email:
        email_data = generate_new_account_email(
            email_to=user_in.email, username=user_in.email, password=user_in.password
        )
        send_email(
            email_to=user_in.email,
            subject=email_data.subject,
            html_content=email_data.html_content,
        )
    return user


@router.patch("/me", response_model=UserPublic)
def update_user_me(
    *, session: SessionDep, user_in: UserUpdateMe, current_user: CurrentUser
) -> Any:
    """
    Purpose: Update own profile (name and email)

    Structure:
        session (SessionDep): input - Database session
        user_in (UserUpdateMe): input - Partial profile update
        current_user (CurrentUser): input - Authenticated user
        user (UserPublic): output - Updated user profile

    Relationships:
        Consumes: crud.get_user_by_email, User table
        Produces: Updated User table row, UserPublic response

    Flow:
        1. If email changing, check uniqueness (raise 409 if taken)
        2. Apply partial update to current user
        3. Persist and return updated user
    """

    if user_in.email:
        existing_user = crud.get_user_by_email(session=session, email=user_in.email)
        if existing_user and existing_user.id != current_user.id:
            raise HTTPException(
                status_code=409, detail="User with this email already exists"
            )
    user_data = user_in.model_dump(exclude_unset=True)
    current_user.sqlmodel_update(user_data)
    session.add(current_user)
    session.commit()
    session.refresh(current_user)
    return current_user


@router.patch("/me/password", response_model=Message)
def update_password_me(
    *, session: SessionDep, body: UpdatePassword, current_user: CurrentUser
) -> Any:
    """
    Purpose: Change own password with current password verification

    Structure:
        session (SessionDep): input - Database session
        body (UpdatePassword): input - Current and new passwords
        current_user (CurrentUser): input - Authenticated user
        message (Message): output - Success confirmation

    Relationships:
        Consumes: core.security.verify_password, core.security.get_password_hash
        Produces: Updated password hash in User table, Message response

    Flow:
        1. Verify current password, raise 400 if incorrect
        2. Reject if new password equals current, raise 400
        3. Hash new password, persist, and return confirmation
    """
    verified, _ = verify_password(body.current_password, current_user.hashed_password)
    if not verified:
        raise HTTPException(status_code=400, detail="Incorrect password")
    if body.current_password == body.new_password:
        raise HTTPException(
            status_code=400, detail="New password cannot be the same as the current one"
        )
    hashed_password = get_password_hash(body.new_password)
    current_user.hashed_password = hashed_password
    session.add(current_user)
    session.commit()
    return Message(message="Password updated successfully")


@router.get("/me", response_model=UserPublic)
def read_user_me(current_user: CurrentUser) -> Any:
    """
    Purpose: Get current authenticated user profile

    Structure:
        current_user (CurrentUser): input - Authenticated user
        user (UserPublic): output - Current user profile

    Relationships:
        Consumes: CurrentUser dependency
        Produces: UserPublic response
    """
    return current_user


@router.delete("/me", response_model=Message)
def delete_user_me(session: SessionDep, current_user: CurrentUser) -> Any:
    """
    Purpose: Delete own account (superusers cannot delete themselves)

    Structure:
        session (SessionDep): input - Database session
        current_user (CurrentUser): input - Authenticated user
        message (Message): output - Deletion confirmation

    Relationships:
        Consumes: User table
        Produces: Message response
    """
    if current_user.is_superuser:
        raise HTTPException(
            status_code=403, detail="Super users are not allowed to delete themselves"
        )
    session.delete(current_user)
    session.commit()
    return Message(message="User deleted successfully")


@router.post("/signup", response_model=UserPublic)
def register_user(session: SessionDep, user_in: UserRegister) -> Any:
    """
    Purpose: Public self-registration (no auth required)

    Structure:
        session (SessionDep): input - Database session
        user_in (UserRegister): input - Registration payload
        user (UserPublic): output - Created user

    Relationships:
        Consumes: crud.get_user_by_email, crud.create_user
        Produces: User table row, UserPublic response

    Flow:
        1. Check email uniqueness, raise 400 if duplicate
        2. Convert to UserCreate and create user via crud
        3. Return created user
    """
    user = crud.get_user_by_email(session=session, email=user_in.email)
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this email already exists in the system",
        )
    user_create = UserCreate.model_validate(user_in)
    user = crud.create_user(session=session, user_create=user_create)
    return user


@router.get("/{user_id}", response_model=UserPublic)
def read_user_by_id(
    user_id: uuid.UUID, session: SessionDep, current_user: CurrentUser
) -> Any:
    """
    Purpose: Get user by ID (own profile or superuser only)

    Structure:
        user_id (uuid.UUID): input - Target user ID
        session (SessionDep): input - Database session
        current_user (CurrentUser): input - Authenticated user
        user (UserPublic): output - User profile

    Relationships:
        Consumes: User table, current user context
        Produces: UserPublic response

    Flow:
        1. Fetch user by ID
        2. Return immediately if requesting own profile
        3. Raise 403 if not superuser, raise 404 if user not found
    """
    user = session.get(User, user_id)
    if user == current_user:
        return user
    if not current_user.is_superuser:
        raise HTTPException(
            status_code=403,
            detail="The user doesn't have enough privileges",
        )
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.patch(
    "/{user_id}",
    dependencies=[Depends(get_current_active_superuser)],
    response_model=UserPublic,
)
def update_user(
    *,
    session: SessionDep,
    user_id: uuid.UUID,
    user_in: UserUpdate,
) -> Any:
    """
    Purpose: Update a user by ID (superuser only)

    Structure:
        session (SessionDep): input - Database session
        user_id (uuid.UUID): input - Target user ID
        user_in (UserUpdate): input - Partial update payload
        user (UserPublic): output - Updated user

    Relationships:
        Consumes: crud.get_user_by_email, crud.update_user, User table
        Produces: Updated User table row, UserPublic response

    Flow:
        1. Fetch user by ID, raise 404 if not found
        2. If email changing, check uniqueness (raise 409 if taken)
        3. Update user via crud and return
    """

    db_user = session.get(User, user_id)
    if not db_user:
        raise HTTPException(
            status_code=404,
            detail="The user with this id does not exist in the system",
        )
    if user_in.email:
        existing_user = crud.get_user_by_email(session=session, email=user_in.email)
        if existing_user and existing_user.id != user_id:
            raise HTTPException(
                status_code=409, detail="User with this email already exists"
            )

    db_user = crud.update_user(session=session, db_user=db_user, user_in=user_in)
    return db_user


@router.delete("/{user_id}", dependencies=[Depends(get_current_active_superuser)])
def delete_user(
    session: SessionDep, current_user: CurrentUser, user_id: uuid.UUID
) -> Message:
    """
    Purpose: Delete a user and their items (superuser only, cannot self-delete)

    Structure:
        session (SessionDep): input - Database session
        current_user (CurrentUser): input - Authenticated superuser
        user_id (uuid.UUID): input - Target user ID
        message (Message): output - Deletion confirmation

    Relationships:
        Consumes: User table, Item table
        Produces: Message response

    Flow:
        1. Fetch user by ID, raise 404 if not found
        2. Raise 403 if attempting self-deletion
        3. Delete user's items, then delete user
    """
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    if user == current_user:
        raise HTTPException(
            status_code=403, detail="Super users are not allowed to delete themselves"
        )
    statement = delete(Item).where(col(Item.owner_id) == user_id)
    session.exec(statement)
    session.delete(user)
    session.commit()
    return Message(message="User deleted successfully")
