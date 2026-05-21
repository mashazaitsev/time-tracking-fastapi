import uuid
from datetime import date

from fastapi.testclient import TestClient
from sqlmodel import Session, select

from app.core.config import settings
from app.models import Project, ProjectCreate, TimeEntry, TimeEntryCreate
from tests.utils.project import create_random_project
from tests.utils.time_entry import create_random_time_entry
from tests.utils.user import create_random_user


def test_create_time_entry(
    client: TestClient, superuser_token_headers: dict[str, str], db: Session
) -> None:
    project = create_random_project(db)
    data = {
        "project_id": str(project.id),
        "date": "2024-01-15",
        "duration_minutes": 90,
        "description": "Working on feature",
    }
    response = client.post(
        f"{settings.API_V1_STR}/time-entries/",
        headers=superuser_token_headers,
        json=data,
    )
    assert response.status_code == 200
    content = response.json()
    assert content["project_id"] == data["project_id"]
    assert content["date"] == data["date"]
    assert content["duration_minutes"] == data["duration_minutes"]
    assert content["description"] == data["description"]
    assert "id" in content
    assert "owner_id" in content
    assert "created_at" in content


def test_read_time_entry(
    client: TestClient, superuser_token_headers: dict[str, str], db: Session
) -> None:
    entry = create_random_time_entry(db)
    response = client.get(
        f"{settings.API_V1_STR}/time-entries/{entry.id}",
        headers=superuser_token_headers,
    )
    assert response.status_code == 200
    content = response.json()
    assert content["id"] == str(entry.id)
    assert content["project_id"] == str(entry.project_id)
    assert content["owner_id"] == str(entry.owner_id)
    assert content["duration_minutes"] == entry.duration_minutes
    assert content["description"] == entry.description


def test_read_time_entry_not_found(
    client: TestClient, superuser_token_headers: dict[str, str]
) -> None:
    response = client.get(
        f"{settings.API_V1_STR}/time-entries/{uuid.uuid4()}",
        headers=superuser_token_headers,
    )
    assert response.status_code == 404
    content = response.json()
    assert content["detail"] == "Time entry not found"


def test_read_time_entry_not_enough_permissions(
    client: TestClient, normal_user_token_headers: dict[str, str], db: Session
) -> None:
    entry = create_random_time_entry(db)
    response = client.get(
        f"{settings.API_V1_STR}/time-entries/{entry.id}",
        headers=normal_user_token_headers,
    )
    assert response.status_code == 403
    content = response.json()
    assert content["detail"] == "Not enough permissions"


def test_read_time_entries(
    client: TestClient, superuser_token_headers: dict[str, str], db: Session
) -> None:
    create_random_time_entry(db)
    create_random_time_entry(db)
    response = client.get(
        f"{settings.API_V1_STR}/time-entries/",
        headers=superuser_token_headers,
    )
    assert response.status_code == 200
    content = response.json()
    assert len(content["data"]) >= 2


def test_update_time_entry(
    client: TestClient, superuser_token_headers: dict[str, str], db: Session
) -> None:
    entry = create_random_time_entry(db)
    data = {"duration_minutes": 120, "description": "Updated description"}
    response = client.put(
        f"{settings.API_V1_STR}/time-entries/{entry.id}",
        headers=superuser_token_headers,
        json=data,
    )
    assert response.status_code == 200
    content = response.json()
    assert content["duration_minutes"] == data["duration_minutes"]
    assert content["description"] == data["description"]
    assert content["id"] == str(entry.id)
    assert content["owner_id"] == str(entry.owner_id)


def test_update_time_entry_not_found(
    client: TestClient, superuser_token_headers: dict[str, str]
) -> None:
    data = {"duration_minutes": 120, "description": "Updated description"}
    response = client.put(
        f"{settings.API_V1_STR}/time-entries/{uuid.uuid4()}",
        headers=superuser_token_headers,
        json=data,
    )
    assert response.status_code == 404
    content = response.json()
    assert content["detail"] == "Time entry not found"


def test_update_time_entry_not_enough_permissions(
    client: TestClient, normal_user_token_headers: dict[str, str], db: Session
) -> None:
    entry = create_random_time_entry(db)
    data = {"duration_minutes": 120, "description": "Updated description"}
    response = client.put(
        f"{settings.API_V1_STR}/time-entries/{entry.id}",
        headers=normal_user_token_headers,
        json=data,
    )
    assert response.status_code == 403
    content = response.json()
    assert content["detail"] == "Not enough permissions"


def test_delete_time_entry(
    client: TestClient, superuser_token_headers: dict[str, str], db: Session
) -> None:
    entry = create_random_time_entry(db)
    response = client.delete(
        f"{settings.API_V1_STR}/time-entries/{entry.id}",
        headers=superuser_token_headers,
    )
    assert response.status_code == 200
    content = response.json()
    assert content["message"] == "Time entry deleted successfully"


def test_delete_time_entry_not_found(
    client: TestClient, superuser_token_headers: dict[str, str]
) -> None:
    response = client.delete(
        f"{settings.API_V1_STR}/time-entries/{uuid.uuid4()}",
        headers=superuser_token_headers,
    )
    assert response.status_code == 404
    content = response.json()
    assert content["detail"] == "Time entry not found"


def test_delete_time_entry_not_enough_permissions(
    client: TestClient, normal_user_token_headers: dict[str, str], db: Session
) -> None:
    entry = create_random_time_entry(db)
    response = client.delete(
        f"{settings.API_V1_STR}/time-entries/{entry.id}",
        headers=normal_user_token_headers,
    )
    assert response.status_code == 403
    content = response.json()
    assert content["detail"] == "Not enough permissions"


def test_create_time_entry_project_not_found(
    client: TestClient, superuser_token_headers: dict[str, str]
) -> None:
    data = {
        "project_id": str(uuid.uuid4()),
        "date": "2024-01-15",
        "duration_minutes": 60,
        "description": "Test entry",
    }
    response = client.post(
        f"{settings.API_V1_STR}/time-entries/",
        headers=superuser_token_headers,
        json=data,
    )
    assert response.status_code == 404
    content = response.json()
    assert content["detail"] == "Project not found"


def test_create_time_entry_project_not_owned(
    client: TestClient, normal_user_token_headers: dict[str, str], db: Session
) -> None:
    # Create a project owned by a different user
    project = create_random_project(db)
    data = {
        "project_id": str(project.id),
        "date": "2024-01-15",
        "duration_minutes": 60,
        "description": "Test entry",
    }
    response = client.post(
        f"{settings.API_V1_STR}/time-entries/",
        headers=normal_user_token_headers,
        json=data,
    )
    assert response.status_code == 403
    content = response.json()
    assert content["detail"] == "Not enough permissions"


def test_get_summary_correct_totals(
    client: TestClient, superuser_token_headers: dict[str, str], db: Session
) -> None:
    # Create a project owned by the superuser
    from app import crud

    superuser = crud.get_user_by_email(
        session=db, email=settings.FIRST_SUPERUSER
    )
    assert superuser is not None

    project_in = ProjectCreate(name="Summary Test Project", description="For summary")
    project = Project.model_validate(project_in, update={"owner_id": superuser.id})
    db.add(project)
    db.commit()
    db.refresh(project)

    # Create known time entries
    for minutes in [30, 45, 60]:
        entry_in = TimeEntryCreate(
            project_id=project.id,
            date=date(2024, 1, 15),
            duration_minutes=minutes,
            description="summary test",
        )
        entry = TimeEntry.model_validate(entry_in, update={"owner_id": superuser.id})
        db.add(entry)
    db.commit()

    response = client.get(
        f"{settings.API_V1_STR}/time-entries/summary",
        headers=superuser_token_headers,
    )
    assert response.status_code == 200
    content = response.json()
    # Superuser sees all entries, so total_minutes >= our 135
    assert content["total_minutes"] >= 135
    # Find our project in by_project
    project_entry = next(
        (p for p in content["by_project"] if p["project_id"] == str(project.id)),
        None,
    )
    assert project_entry is not None
    assert project_entry["total_minutes"] == 135
    assert project_entry["project_name"] == "Summary Test Project"


def test_get_summary_empty(
    client: TestClient, db: Session
) -> None:
    # Create a fresh user with no time entries
    from tests.utils.user import user_authentication_headers

    from app import crud
    from app.models import UserCreate
    from tests.utils.utils import random_email, random_lower_string

    email = random_email()
    password = random_lower_string()
    user_in = UserCreate(email=email, password=password)
    crud.create_user(session=db, user_create=user_in)

    headers = user_authentication_headers(client=client, email=email, password=password)

    response = client.get(
        f"{settings.API_V1_STR}/time-entries/summary",
        headers=headers,
    )
    assert response.status_code == 200
    content = response.json()
    assert content["total_minutes"] == 0
    assert content["by_project"] == []


def test_delete_project_cascades_time_entries(
    client: TestClient, superuser_token_headers: dict[str, str], db: Session
) -> None:
    # Create a project owned by superuser
    from app import crud

    superuser = crud.get_user_by_email(
        session=db, email=settings.FIRST_SUPERUSER
    )
    assert superuser is not None

    project_in = ProjectCreate(name="Cascade Test", description="Will be deleted")
    project = Project.model_validate(project_in, update={"owner_id": superuser.id})
    db.add(project)
    db.commit()
    db.refresh(project)

    # Create time entries for this project
    entry_ids = []
    for i in range(3):
        entry_in = TimeEntryCreate(
            project_id=project.id,
            date=date(2024, 1, i + 1),
            duration_minutes=30,
            description=f"cascade test {i}",
        )
        entry = TimeEntry.model_validate(entry_in, update={"owner_id": superuser.id})
        db.add(entry)
        db.commit()
        db.refresh(entry)
        entry_ids.append(entry.id)

    # Delete the project via API
    response = client.delete(
        f"{settings.API_V1_STR}/projects/{project.id}",
        headers=superuser_token_headers,
    )
    assert response.status_code == 200

    # Verify time entries are gone from DB
    db.expire_all()
    for entry_id in entry_ids:
        result = db.exec(select(TimeEntry).where(TimeEntry.id == entry_id)).first()
        assert result is None
