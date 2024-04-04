from pydantic import BaseModel


class User(BaseModel):
    id: str
    username: str
    password: str
    email: str
    is_superuser: bool = False
