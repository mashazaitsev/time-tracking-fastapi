import uuid
from datetime import date, timedelta

from sqlmodel import Session

from app.models import VacationRequest, VacationRequestCreate
from tests.utils.user import create_random_user
from tests.utils.utils import random_lower_string


def create_random_vacation_request(
    db: Session,
    *,
    owner_id: uuid.UUID | None = None,
) -> VacationRequest:
    """Create a random vacation request, optionally reusing an existing owner."""
    if owner_id is None:
        user = create_random_user(db)
        owner_id = user.id
    assert owner_id is not None

    start_date = date.today() + timedelta(days=1)
    end_date = start_date + timedelta(days=5)

    request_in = VacationRequestCreate(
        start_date=start_date,
        end_date=end_date,
        reason=random_lower_string(),
    )
    vacation_request = VacationRequest.model_validate(
        request_in, update={"owner_id": owner_id}
    )
    db.add(vacation_request)
    db.commit()
    db.refresh(vacation_request)
    return vacation_request
