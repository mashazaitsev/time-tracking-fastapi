"""
Purpose: Provide private admin endpoint for user creation (local environment only)

Structure:
    PrivateUserCreate (class): schema - User creation without SQLModel validation
    create_user (POST /private/users/): endpoint - Create user directly

Relationships:
    Consumes: models.User, core.security.get_password_hash
    Produces: UserPublic response, User table row

Note:
    Only registered when ENVIRONMENT=local (see api/main.py).
"""

from typing import Any

from fastapi import APIRouter
from pydantic import BaseModel

from app.api.deps import SessionDep
from app.core.security import get_password_hash
from app.models import (
    User,
    UserPublic,
)

router = APIRouter(tags=["private"], prefix="/private")


class PrivateUserCreate(BaseModel):
    """
    Purpose: Schema for private user creation (bypasses SQLModel validation)

    Structure:
        email (str): input - User email
        password (str): input - Plain text password
        full_name (str): input - User display name
        is_verified (bool): input - Verification status (default False)
    """
    email: str
    password: str
    full_name: str
    is_verified: bool = False


@router.post("/users/", response_model=UserPublic)
def create_user(user_in: PrivateUserCreate, session: SessionDep) -> Any:
    """
    Purpose: Create user directly without email uniqueness check (local dev only)

    Structure:
        user_in (PrivateUserCreate): input - User creation payload
        session (SessionDep): input - Database session
        user (UserPublic): output - Created user

    Relationships:
        Consumes: PrivateUserCreate schema, core.security.get_password_hash
        Produces: User table row, UserPublic response

    Flow:
        1. Build User model with hashed password
        2. Persist to database
        3. Return created user
    """

    user = User(
        email=user_in.email,
        full_name=user_in.full_name,
        hashed_password=get_password_hash(user_in.password),
    )

    session.add(user)
    session.commit()

    return user
