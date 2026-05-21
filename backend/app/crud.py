"""
Purpose: Provide CRUD operations for User and Item database entities

Structure:
    create_user (func): output - Create user with hashed password
    update_user (func): output - Update user fields, re-hash if password changed
    get_user_by_email (func): output - Look up user by email
    authenticate (func): output - Verify email/password, upgrade hash if needed
    create_item (func): output - Create item with owner assignment

Relationships:
    Consumes: models.User, models.Item, models.UserCreate, models.UserUpdate, models.ItemCreate
    Consumes: core.security.get_password_hash, core.security.verify_password
    Produces: User rows, Item rows

Semantics:
    Domain: identity, content
    Logic: [Timing-attack prevention via dummy hash on failed lookup,
            Auto-upgrade bcrypt→argon2 on successful login]

Important:
    authenticate() MUST run verify_password even when user not found
    to prevent timing-based email enumeration attacks.
"""

import uuid
from typing import Any

from sqlmodel import Session, select

from app.core.security import get_password_hash, verify_password
from app.models import Item, ItemCreate, User, UserCreate, UserUpdate


def create_user(*, session: Session, user_create: UserCreate) -> User:
    """
    Purpose: Create user with hashed password

    Relationships:
        Consumes: UserCreate schema
        Produces: user table row
    """
    db_obj = User.model_validate(
        user_create, update={"hashed_password": get_password_hash(user_create.password)}
    )
    session.add(db_obj)
    session.commit()
    session.refresh(db_obj)
    return db_obj


def update_user(*, session: Session, db_user: User, user_in: UserUpdate) -> Any:
    """
    Purpose: Update user fields, re-hashing password if changed

    Relationships:
        Consumes: UserUpdate schema, existing User
        Produces: updated user table row
    """
    user_data = user_in.model_dump(exclude_unset=True)
    extra_data = {}
    if "password" in user_data:
        password = user_data["password"]
        hashed_password = get_password_hash(password)
        extra_data["hashed_password"] = hashed_password
    db_user.sqlmodel_update(user_data, update=extra_data)
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user


def get_user_by_email(*, session: Session, email: str) -> User | None:
    """Purpose: Look up user by email address"""
    statement = select(User).where(User.email == email)
    session_user = session.exec(statement).first()
    return session_user


# Argon2 dummy hash for timing-attack prevention when user not found
DUMMY_HASH = "$argon2id$v=19$m=65536,t=3,p=4$MjQyZWE1MzBjYjJlZTI0Yw$YTU4NGM5ZTZmYjE2NzZlZjY0ZWY3ZGRkY2U2OWFjNjk"


def authenticate(*, session: Session, email: str, password: str) -> User | None:
    """
    Purpose: Verify email/password credentials and auto-upgrade legacy bcrypt hashes

    Flow:
        1. Look up user by email
        2. If not found, verify against dummy hash (timing-attack prevention)
        3. Verify password against stored hash
        4. If hash algorithm upgraded (bcrypt→argon2), persist new hash

    Important:
        MUST run verify_password even when user not found to prevent
        timing-based email enumeration.
    """
    db_user = get_user_by_email(session=session, email=email)
    if not db_user:
        verify_password(password, DUMMY_HASH)
        return None
    verified, updated_password_hash = verify_password(password, db_user.hashed_password)
    if not verified:
        return None
    if updated_password_hash:
        db_user.hashed_password = updated_password_hash
        session.add(db_user)
        session.commit()
        session.refresh(db_user)
    return db_user


def create_item(*, session: Session, item_in: ItemCreate, owner_id: uuid.UUID) -> Item:
    """
    Purpose: Create item assigned to owner

    Relationships:
        Consumes: ItemCreate schema, owner UUID
        Produces: item table row
    """
    db_item = Item.model_validate(item_in, update={"owner_id": owner_id})
    session.add(db_item)
    session.commit()
    session.refresh(db_item)
    return db_item
