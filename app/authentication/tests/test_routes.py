from fastapi import status
from fastapi.testclient import TestClient
from app.main import app

from ..requests import UserCreate
from ..services import UserService

client = TestClient(app)


class TestUserRoutes:
    def test_create_user(self):
        request = UserCreate(
            username="testuser", email="testuser@example.com", password="testpassword"
        )
        response = client.post("/auth/user/", json=request.dict())

        assert response.status_code == status.HTTP_201_CREATED

        UserService.delete_user(response.json().get("id"))
