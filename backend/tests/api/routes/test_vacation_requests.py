import uuid
from datetime import date, timedelta

from fastapi.testclient import TestClient
from sqlmodel import Session, select

from app.core.config import settings
from app.models import User, VacationRequest
from tests.utils.user import create_random_user, user_authentication_headers
from tests.utils.vacation_request import create_random_vacation_request


def test_create_vacation_request(
    client: TestClient, superuser_token_headers: dict[str, str]
) -> None:
    data = {
        "start_date": "2024-06-01",
        "end_date": "2024-06-10",
        "reason": "Summer vacation",
    }
    response = client.post(
        f"{settings.API_V1_STR}/vacation-requests/",
        headers=superuser_token_headers,
        json=data,
    )
    assert response.status_code == 200
    content = response.json()
    assert content["start_date"] == data["start_date"]
    assert content["end_date"] == data["end_date"]
    assert content["reason"] == data["reason"]
    assert content["status"] == "pending"
    assert "id" in content
    assert "owner_id" in content
    assert "created_at" in content


def test_create_vacation_request_invalid_date_range(
    client: TestClient, superuser_token_headers: dict[str, str]
) -> None:
    data = {
        "start_date": "2024-06-10",
        "end_date": "2024-06-01",
        "reason": "Invalid range",
    }
    response = client.post(
        f"{settings.API_V1_STR}/vacation-requests/",
        headers=superuser_token_headers,
        json=data,
    )
    assert response.status_code == 422


def test_create_vacation_request_invalid_reason_length(
    client: TestClient, superuser_token_headers: dict[str, str]
) -> None:
    # Empty reason
    data = {
        "start_date": "2024-06-01",
        "end_date": "2024-06-10",
        "reason": "",
    }
    response = client.post(
        f"{settings.API_V1_STR}/vacation-requests/",
        headers=superuser_token_headers,
        json=data,
    )
    assert response.status_code == 422

    # Reason > 500 characters
    data = {
        "start_date": "2024-06-01",
        "end_date": "2024-06-10",
        "reason": "x" * 501,
    }
    response = client.post(
        f"{settings.API_V1_STR}/vacation-requests/",
        headers=superuser_token_headers,
        json=data,
    )
    assert response.status_code == 422


def test_create_vacation_request_missing_fields(
    client: TestClient, superuser_token_headers: dict[str, str]
) -> None:
    # Missing reason
    data = {
        "start_date": "2024-06-01",
        "end_date": "2024-06-10",
    }
    response = client.post(
        f"{settings.API_V1_STR}/vacation-requests/",
        headers=superuser_token_headers,
        json=data,
    )
    assert response.status_code == 422

    # Missing start_date
    data = {
        "end_date": "2024-06-10",
        "reason": "Vacation",
    }
    response = client.post(
        f"{settings.API_V1_STR}/vacation-requests/",
        headers=superuser_token_headers,
        json=data,
    )
    assert response.status_code == 422

    # Missing end_date
    data = {
        "start_date": "2024-06-01",
        "reason": "Vacation",
    }
    response = client.post(
        f"{settings.API_V1_STR}/vacation-requests/",
        headers=superuser_token_headers,
        json=data,
    )
    assert response.status_code == 422


def test_read_vacation_requests_all_users(
    client: TestClient, normal_user_token_headers: dict[str, str], db: Session
) -> None:
    # Create a request owned by a different user
    create_random_vacation_request(db)
    response = client.get(
        f"{settings.API_V1_STR}/vacation-requests/",
        headers=normal_user_token_headers,
    )
    assert response.status_code == 200
    content = response.json()
    assert "data" in content
    assert "count" in content
    assert len(content["data"]) >= 1


def test_read_vacation_requests_pagination(
    client: TestClient, superuser_token_headers: dict[str, str], db: Session
) -> None:
    # Create several requests to ensure we have enough data
    for _ in range(3):
        create_random_vacation_request(db)

    # Get with skip=0, limit=2
    response = client.get(
        f"{settings.API_V1_STR}/vacation-requests/",
        headers=superuser_token_headers,
        params={"skip": 0, "limit": 2},
    )
    assert response.status_code == 200
    content = response.json()
    assert len(content["data"]) <= 2
    total_count = content["count"]

    # Get with skip=1, limit=2
    response = client.get(
        f"{settings.API_V1_STR}/vacation-requests/",
        headers=superuser_token_headers,
        params={"skip": 1, "limit": 2},
    )
    assert response.status_code == 200
    content2 = response.json()
    assert content2["count"] == total_count
    assert len(content2["data"]) <= 2


def test_read_vacation_requests_limit_exceeds_max(
    client: TestClient, superuser_token_headers: dict[str, str]
) -> None:
    response = client.get(
        f"{settings.API_V1_STR}/vacation-requests/",
        headers=superuser_token_headers,
        params={"limit": 101},
    )
    assert response.status_code == 422


def test_read_vacation_request(
    client: TestClient, normal_user_token_headers: dict[str, str], db: Session
) -> None:
    # Any authenticated user can read any vacation request
    vacation_request = create_random_vacation_request(db)
    response = client.get(
        f"{settings.API_V1_STR}/vacation-requests/{vacation_request.id}",
        headers=normal_user_token_headers,
    )
    assert response.status_code == 200
    content = response.json()
    assert content["id"] == str(vacation_request.id)
    assert content["start_date"] == str(vacation_request.start_date)
    assert content["end_date"] == str(vacation_request.end_date)
    assert content["reason"] == vacation_request.reason
    assert content["owner_id"] == str(vacation_request.owner_id)
    assert content["status"] == vacation_request.status


def test_read_vacation_request_not_found(
    client: TestClient, superuser_token_headers: dict[str, str]
) -> None:
    response = client.get(
        f"{settings.API_V1_STR}/vacation-requests/{uuid.uuid4()}",
        headers=superuser_token_headers,
    )
    assert response.status_code == 404
    content = response.json()
    assert content["detail"] == "Vacation request not found"


def test_update_vacation_request_owner(
    client: TestClient, db: Session
) -> None:
    # Create a user and a vacation request owned by them
    user = create_random_user(db)
    vacation_request = create_random_vacation_request(db, owner_id=user.id)

    # Get auth headers for the owner
    from app import crud
    from app.models import UserUpdate

    password = "newpassword123"
    crud.update_user(session=db, db_user=user, user_in=UserUpdate(password=password))
    headers = user_authentication_headers(
        client=client, email=user.email, password=password
    )

    data = {"reason": "Updated reason for vacation"}
    response = client.put(
        f"{settings.API_V1_STR}/vacation-requests/{vacation_request.id}",
        headers=headers,
        json=data,
    )
    assert response.status_code == 200
    content = response.json()
    assert content["reason"] == data["reason"]
    assert content["id"] == str(vacation_request.id)
    assert content["start_date"] == str(vacation_request.start_date)
    assert content["end_date"] == str(vacation_request.end_date)


def test_update_vacation_request_superuser(
    client: TestClient, superuser_token_headers: dict[str, str], db: Session
) -> None:
    # Create a request owned by another user
    vacation_request = create_random_vacation_request(db)
    data = {"reason": "Superuser updated this"}
    response = client.put(
        f"{settings.API_V1_STR}/vacation-requests/{vacation_request.id}",
        headers=superuser_token_headers,
        json=data,
    )
    assert response.status_code == 200
    content = response.json()
    assert content["reason"] == data["reason"]
    assert content["id"] == str(vacation_request.id)


def test_update_vacation_request_not_owner(
    client: TestClient, normal_user_token_headers: dict[str, str], db: Session
) -> None:
    # Create a request owned by a different user
    vacation_request = create_random_vacation_request(db)
    data = {"reason": "Should not work"}
    response = client.put(
        f"{settings.API_V1_STR}/vacation-requests/{vacation_request.id}",
        headers=normal_user_token_headers,
        json=data,
    )
    assert response.status_code == 403
    content = response.json()
    assert content["detail"] == "Not enough permissions"


def test_update_vacation_request_not_found(
    client: TestClient, superuser_token_headers: dict[str, str]
) -> None:
    data = {"reason": "Does not matter"}
    response = client.put(
        f"{settings.API_V1_STR}/vacation-requests/{uuid.uuid4()}",
        headers=superuser_token_headers,
        json=data,
    )
    assert response.status_code == 404
    content = response.json()
    assert content["detail"] == "Vacation request not found"


def test_update_vacation_request_invalid_date_range(
    client: TestClient, superuser_token_headers: dict[str, str], db: Session
) -> None:
    # Create a request with start=2024-06-01, end=2024-06-10
    vacation_request = create_random_vacation_request(db)
    # Update only end_date to be before the existing start_date
    data = {"end_date": str(vacation_request.start_date - timedelta(days=1))}
    response = client.put(
        f"{settings.API_V1_STR}/vacation-requests/{vacation_request.id}",
        headers=superuser_token_headers,
        json=data,
    )
    assert response.status_code == 422


def test_update_vacation_request_empty_payload(
    client: TestClient, superuser_token_headers: dict[str, str], db: Session
) -> None:
    vacation_request = create_random_vacation_request(db)
    response = client.put(
        f"{settings.API_V1_STR}/vacation-requests/{vacation_request.id}",
        headers=superuser_token_headers,
        json={},
    )
    assert response.status_code == 200
    content = response.json()
    assert content["id"] == str(vacation_request.id)
    assert content["start_date"] == str(vacation_request.start_date)
    assert content["end_date"] == str(vacation_request.end_date)
    assert content["reason"] == vacation_request.reason
    assert content["status"] == vacation_request.status


def test_delete_vacation_request_owner(
    client: TestClient, db: Session
) -> None:
    # Create a user and a vacation request owned by them
    user = create_random_user(db)
    vacation_request = create_random_vacation_request(db, owner_id=user.id)

    # Get auth headers for the owner
    from app import crud
    from app.models import UserUpdate

    password = "newpassword123"
    crud.update_user(session=db, db_user=user, user_in=UserUpdate(password=password))
    headers = user_authentication_headers(
        client=client, email=user.email, password=password
    )

    response = client.delete(
        f"{settings.API_V1_STR}/vacation-requests/{vacation_request.id}",
        headers=headers,
    )
    assert response.status_code == 200
    content = response.json()
    assert content["message"] == "Vacation request deleted successfully"


def test_delete_vacation_request_superuser(
    client: TestClient, superuser_token_headers: dict[str, str], db: Session
) -> None:
    # Create a request owned by another user
    vacation_request = create_random_vacation_request(db)
    response = client.delete(
        f"{settings.API_V1_STR}/vacation-requests/{vacation_request.id}",
        headers=superuser_token_headers,
    )
    assert response.status_code == 200
    content = response.json()
    assert content["message"] == "Vacation request deleted successfully"


def test_delete_vacation_request_not_owner(
    client: TestClient, normal_user_token_headers: dict[str, str], db: Session
) -> None:
    # Create a request owned by a different user
    vacation_request = create_random_vacation_request(db)
    response = client.delete(
        f"{settings.API_V1_STR}/vacation-requests/{vacation_request.id}",
        headers=normal_user_token_headers,
    )
    assert response.status_code == 403
    content = response.json()
    assert content["detail"] == "Not enough permissions"


def test_delete_vacation_request_not_found(
    client: TestClient, superuser_token_headers: dict[str, str]
) -> None:
    response = client.delete(
        f"{settings.API_V1_STR}/vacation-requests/{uuid.uuid4()}",
        headers=superuser_token_headers,
    )
    assert response.status_code == 404
    content = response.json()
    assert content["detail"] == "Vacation request not found"


def test_cascade_delete_user_removes_requests(
    client: TestClient, superuser_token_headers: dict[str, str], db: Session
) -> None:
    # Create a user with vacation requests
    user = create_random_user(db)
    request_ids = []
    for _ in range(3):
        vr = create_random_vacation_request(db, owner_id=user.id)
        request_ids.append(vr.id)

    # Delete the user via API
    response = client.delete(
        f"{settings.API_V1_STR}/users/{user.id}",
        headers=superuser_token_headers,
    )
    assert response.status_code == 200

    # Verify vacation requests are gone from DB
    db.expire_all()
    for request_id in request_ids:
        result = db.exec(
            select(VacationRequest).where(VacationRequest.id == request_id)
        ).first()
        assert result is None
