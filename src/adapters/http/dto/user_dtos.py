from pydantic import BaseModel


class UserRequest(BaseModel):
    first_name: str
    last_name: str


class UserResponse(BaseModel):
    first_name: str
    last_name: str
