from typing import Optional
from app.core.database import MongoDb

from .models import User
from .requests import UserCreate


class UserRepository:
    @staticmethod
    def create_user(data: UserCreate) -> User:
        inserted_id = MongoDb.insert_one("users", data.dict())

        if not inserted_id:
            return None

        user = UserRepository.find_user(id=inserted_id)
        return user

    @staticmethod
    def create_superuser(data: UserCreate) -> User:
        inserted_id = MongoDb.insert_one("users", {**data.dict(), "is_superuser": True})

        if not inserted_id:
            return None

        user = UserRepository.find_user(id=inserted_id)
        return user

    @staticmethod
    def find_user(
        query: Optional[dict] = None, id: Optional[str] = None
    ) -> Optional[User]:
        result = MongoDb.find_one("users", query, id)
        if not result:
            return None
        return User(**result)

    @staticmethod
    def delete_user(user_id: str) -> bool:
        return MongoDb.delete_one("users", user_id)
