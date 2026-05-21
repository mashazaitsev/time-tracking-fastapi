import uuid
from datetime import date

from sqlmodel import Session

from app.models import Project, ProjectCreate, TimeEntry, TimeEntryCreate
from tests.utils.user import create_random_user
from tests.utils.utils import random_lower_string


def create_random_time_entry(
    db: Session,
    *,
    project_id: uuid.UUID | None = None,
    owner_id: uuid.UUID | None = None,
) -> TimeEntry:
    """Create a random time entry, optionally reusing an existing project/owner."""
    if owner_id is None:
        user = create_random_user(db)
        owner_id = user.id
    assert owner_id is not None

    if project_id is None:
        project_in = ProjectCreate(
            name=random_lower_string(), description=random_lower_string()
        )
        project = Project.model_validate(project_in, update={"owner_id": owner_id})
        db.add(project)
        db.commit()
        db.refresh(project)
        project_id = project.id

    entry_in = TimeEntryCreate(
        project_id=project_id,
        date=date.today(),
        duration_minutes=60,
        description=random_lower_string(),
    )
    entry = TimeEntry.model_validate(entry_in, update={"owner_id": owner_id})
    db.add(entry)
    db.commit()
    db.refresh(entry)
    return entry
