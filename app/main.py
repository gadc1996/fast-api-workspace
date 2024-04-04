from fastapi import FastAPI
from app.authentication.services import UserService
from app.authentication.routes import router as auth_router

app = FastAPI()

app.include_router(auth_router, prefix="/auth")

# @app.on_event("startup")
# async def startup_event():
    # admin_user = UserService.find_user({"username": "admin"})
    # print(admin_user)
    # if admin_user is None:
    #     UserService.create_superuser(
    #         {"username": "admin", "password": "admin", "email": "admin@example.com"}
    #     )
