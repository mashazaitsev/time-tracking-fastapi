"""
Purpose: Provide authentication endpoints for login, token validation, and password recovery

Structure:
    login_access_token (POST /login/access-token): endpoint - OAuth2 token login
    test_token (POST /login/test-token): endpoint - Validate access token
    recover_password (POST /password-recovery/{email}): endpoint - Send password reset email
    reset_password (POST /reset-password/): endpoint - Reset password with token
    recover_password_html_content (POST /password-recovery-html-content/{email}): endpoint - Preview reset email HTML (superuser only)

Relationships:
    Consumes: crud.authenticate, crud.get_user_by_email, crud.update_user
    Consumes: utils.generate_password_reset_token, utils.generate_reset_password_email, utils.send_email
    Produces: Token, UserPublic, Message responses

Semantics:
    Domain: authentication
    Logic: [Password recovery returns same response regardless of email existence (prevents enumeration),
            Reset tokens expire per EMAIL_RESET_TOKEN_EXPIRE_HOURS setting]
"""

from datetime import timedelta
from typing import Annotated, Any

from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.security import OAuth2PasswordRequestForm

from app import crud
from app.api.deps import CurrentUser, SessionDep, get_current_active_superuser
from app.core import security
from app.core.config import settings
from app.models import Message, NewPassword, Token, UserPublic, UserUpdate
from app.utils import (
    generate_password_reset_token,
    generate_reset_password_email,
    send_email,
    verify_password_reset_token,
)

router = APIRouter(tags=["login"])


@router.post("/login/access-token")
def login_access_token(
    session: SessionDep, form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
) -> Token:
    """
    Purpose: Authenticate user via email/password and return JWT access token

    Structure:
        session (SessionDep): input - Database session
        form_data (OAuth2PasswordRequestForm): input - Username (email) and password
        token (Token): output - JWT access token

    Relationships:
        Consumes: crud.authenticate, core.security.create_access_token
        Produces: Token response

    Flow:
        1. Authenticate user via crud, raise 400 if invalid credentials
        2. Raise 400 if user is inactive
        3. Create and return JWT access token with configured expiry
    """
    user = crud.authenticate(
        session=session, email=form_data.username, password=form_data.password
    )
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    elif not user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    return Token(
        access_token=security.create_access_token(
            user.id, expires_delta=access_token_expires
        )
    )


@router.post("/login/test-token", response_model=UserPublic)
def test_token(current_user: CurrentUser) -> Any:
    """
    Purpose: Validate access token and return current user profile

    Structure:
        current_user (CurrentUser): input - Authenticated user from token
        user (UserPublic): output - Current user profile

    Relationships:
        Consumes: CurrentUser dependency (validates token implicitly)
        Produces: UserPublic response
    """
    return current_user


@router.post("/password-recovery/{email}")
def recover_password(email: str, session: SessionDep) -> Message:
    """
    Purpose: Send password recovery email if user exists

    Structure:
        email (str): input - User email address
        session (SessionDep): input - Database session
        message (Message): output - Generic confirmation message

    Relationships:
        Consumes: crud.get_user_by_email, utils.generate_password_reset_token, utils.send_email
        Produces: Message response, password reset email

    Flow:
        1. Look up user by email
        2. If found, generate reset token and send recovery email
        3. Return same message regardless of email existence (prevents enumeration)
    """
    user = crud.get_user_by_email(session=session, email=email)

    if user:
        password_reset_token = generate_password_reset_token(email=email)
        email_data = generate_reset_password_email(
            email_to=user.email, email=email, token=password_reset_token
        )
        send_email(
            email_to=user.email,
            subject=email_data.subject,
            html_content=email_data.html_content,
        )
    return Message(
        message="If that email is registered, we sent a password recovery link"
    )


@router.post("/reset-password/")
def reset_password(session: SessionDep, body: NewPassword) -> Message:
    """
    Purpose: Reset user password using a recovery token

    Structure:
        session (SessionDep): input - Database session
        body (NewPassword): input - Reset token and new password
        message (Message): output - Success confirmation

    Relationships:
        Consumes: utils.verify_password_reset_token, crud.get_user_by_email, crud.update_user
        Produces: Message response, updated password hash in User table

    Flow:
        1. Verify reset token and extract email, raise 400 if invalid
        2. Look up user by email, raise 400 if not found or inactive
        3. Update password hash and return confirmation
    """
    email = verify_password_reset_token(token=body.token)
    if not email:
        raise HTTPException(status_code=400, detail="Invalid token")
    user = crud.get_user_by_email(session=session, email=email)
    if not user:
        raise HTTPException(status_code=400, detail="Invalid token")
    elif not user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    user_in_update = UserUpdate(password=body.new_password)
    crud.update_user(
        session=session,
        db_user=user,
        user_in=user_in_update,
    )
    return Message(message="Password updated successfully")


@router.post(
    "/password-recovery-html-content/{email}",
    dependencies=[Depends(get_current_active_superuser)],
    response_class=HTMLResponse,
)
def recover_password_html_content(email: str, session: SessionDep) -> Any:
    """
    Purpose: Preview password recovery email HTML content (superuser only)

    Structure:
        email (str): input - Target user email
        session (SessionDep): input - Database session
        html (HTMLResponse): output - Rendered email HTML

    Relationships:
        Consumes: crud.get_user_by_email, utils.generate_password_reset_token, utils.generate_reset_password_email
        Produces: HTMLResponse with email content and subject header

    Flow:
        1. Look up user by email, raise 404 if not found
        2. Generate reset token and email content
        3. Return HTML response with subject in headers
    """
    user = crud.get_user_by_email(session=session, email=email)

    if not user:
        raise HTTPException(
            status_code=404,
            detail="The user with this username does not exist in the system.",
        )
    password_reset_token = generate_password_reset_token(email=email)
    email_data = generate_reset_password_email(
        email_to=user.email, email=email, token=password_reset_token
    )

    return HTMLResponse(
        content=email_data.html_content, headers={"subject:": email_data.subject}
    )
