"""
Purpose: Provide FastAPI dependency injection for database sessions and authentication

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
"""

from collections.abc import Generator
from typing import Annotated

import jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jwt.exceptions import InvalidTokenError
from pydantic import ValidationError
from sqlmodel import Session

from app.core import security
from app.core.config import settings
from app.core.db import engine
from app.models import TokenPayload, User

reusable_oauth2 = OAuth2PasswordBearer(
    tokenUrl=f"{settings.API_V1_STR}/login/access-token"
)


def get_db() -> Generator[Session, None, None]:
    """
    Purpose: Yield a database session per request, auto-closed on completion

    Structure:
        session (Session): output - SQLModel database session

    Relationships:
        Consumes: core.db.engine
        Produces: Session (via SessionDep alias)
    """
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_db)]
TokenDep = Annotated[str, Depends(reusable_oauth2)]


def get_current_user(session: SessionDep, token: TokenDep) -> User:
    """
    Purpose: Decode JWT token and return the authenticated active User

    Structure:
        session (SessionDep): input - Database session
        token (TokenDep): input - JWT bearer token
        user (User): output - Authenticated user

    Relationships:
        Consumes: JWT token, User table, core.security.ALGORITHM, settings.SECRET_KEY
        Produces: Authenticated User object (via CurrentUser alias)

    Flow:
        1. Decode JWT with SECRET_KEY and validate payload
        2. Look up user by token subject (user ID)
        3. Raise 404 if not found, 400 if inactive
    """
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[security.ALGORITHM]
        )
        token_data = TokenPayload(**payload)
    except (InvalidTokenError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
        )
    user = session.get(User, token_data.sub)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    if not user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    return user


CurrentUser = Annotated[User, Depends(get_current_user)]


def get_current_active_superuser(current_user: CurrentUser) -> User:
    """
    Purpose: Enforce superuser role on authenticated user

    Structure:
        current_user (CurrentUser): input - Authenticated user
        user (User): output - Verified superuser

    Relationships:
        Consumes: CurrentUser dependency
        Produces: Verified superuser (used as route dependency)
    """
    if not current_user.is_superuser:
        raise HTTPException(
            status_code=403, detail="The user doesn't have enough privileges"
        )
    return current_user
