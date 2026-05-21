"""
Purpose: Provide JWT token creation and password hashing/verification

Structure:
    create_access_token (func): output - Create signed JWT with expiration
    verify_password (func): output - Verify password and return upgraded hash if applicable
    get_password_hash (func): output - Hash password with Argon2
    password_hash (PasswordHash): config - Multi-hasher supporting Argon2 and bcrypt
    ALGORITHM (str): config - JWT signing algorithm (HS256)

Relationships:
    Consumes: core.config.settings.SECRET_KEY
    Produces: JWT tokens, password hashes (consumed by crud, api.deps)

Semantics:
    Domain: security
    Logic: [Argon2 is primary hasher, bcrypt supported for legacy upgrade,
            verify_and_update returns new hash when bcrypt→argon2 upgrade needed]
"""

from datetime import datetime, timedelta, timezone
from typing import Any

import jwt
from pwdlib import PasswordHash
from pwdlib.hashers.argon2 import Argon2Hasher
from pwdlib.hashers.bcrypt import BcryptHasher

from app.core.config import settings

password_hash = PasswordHash(
    (
        Argon2Hasher(),
        BcryptHasher(),
    )
)


ALGORITHM = "HS256"


def create_access_token(subject: str | Any, expires_delta: timedelta) -> str:
    """Purpose: Create signed JWT with subject (user ID) and expiration"""
    expire = datetime.now(timezone.utc) + expires_delta
    to_encode = {"exp": expire, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_password(
    plain_password: str, hashed_password: str
) -> tuple[bool, str | None]:
    """
    Purpose: Verify password against hash, returning upgraded hash if algorithm changed

    Returns:
        tuple: (verified: bool, updated_hash: str | None) — updated_hash is non-None
        when bcrypt hash was verified and needs upgrade to argon2
    """
    return password_hash.verify_and_update(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    """Purpose: Hash password using Argon2 (primary hasher)"""
    return password_hash.hash(password)
