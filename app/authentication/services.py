import pytest
from typing import Optional
from .models import User
from .requests import UserCreate
from .repositories import UserRepository


class UserService:
    @staticmethod
    def create_user(request: UserCreate) -> User:
        if UserRepository.find_user({"email": request.email}):
            return None

        try:
            user = UserRepository.create_user(request)
        except Exception as e:
            # replace with your actual error handling code
            pass

        return user

    @staticmethod
    def create_superuser(request: UserCreate) -> User:
        if UserRepository.find_user({"email": request.email}):
            return None

        try:
            user = UserRepository.create_superuser(request)
        except Exception as e:
            # replace with your actual error handling code
            return None

        return user

    @staticmethod
    def delete_user(user_id: str) -> bool:
        user = UserRepository.find_user(id=user_id)
        if not user:
            return False

        try:
            UserRepository.delete_user(user_id)
        except Exception as e:
            # replace with your actual error handling code
            return False

        return True
        
    @staticmethod
    def find_user(
        query: Optional[dict] = None, id: Optional[str] = None
        ) -> User:
        return UserRepository.find_user(query=query, id=id)
