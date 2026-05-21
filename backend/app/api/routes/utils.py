"""
Purpose: Provide utility endpoints for health checks and email testing

Structure:
    test_email (POST /utils/test-email/): endpoint - Send test email (superuser only)
    health_check (GET /utils/health-check/): endpoint - Application health check

Relationships:
    Consumes: utils.generate_test_email, utils.send_email
    Produces: Message response, bool response
"""

from fastapi import APIRouter, Depends
from pydantic.networks import EmailStr

from app.api.deps import get_current_active_superuser
from app.models import Message
from app.utils import generate_test_email, send_email

router = APIRouter(prefix="/utils", tags=["utils"])


@router.post(
    "/test-email/",
    dependencies=[Depends(get_current_active_superuser)],
    status_code=201,
)
def test_email(email_to: EmailStr) -> Message:
    """
    Purpose: Send test email to verify SMTP configuration (superuser only)

    Structure:
        email_to (EmailStr): input - Recipient email address
        message (Message): output - Success confirmation

    Relationships:
        Consumes: utils.generate_test_email, utils.send_email
        Produces: Message response, test email
    """
    email_data = generate_test_email(email_to=email_to)
    send_email(
        email_to=email_to,
        subject=email_data.subject,
        html_content=email_data.html_content,
    )
    return Message(message="Test email sent")


@router.get("/health-check/")
async def health_check() -> bool:
    """
    Purpose: Return true if application is running

    Structure:
        result (bool): output - Always True

    Relationships:
        Consumes: None
        Produces: bool response
    """
    return True
