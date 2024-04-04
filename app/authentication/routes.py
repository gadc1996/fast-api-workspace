from fastapi import APIRouter, status
from fastapi.exceptions import HTTPException


from .requests import UserCreate
from .responses import UserResponse
from .services import UserService

router = APIRouter()


@router.post("/user/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def create_user(request: UserCreate):
    user = UserService.create_user(request)
    if user is None:
        raise HTTPException(status_code=201)
    return UserResponse(**user.dict())
