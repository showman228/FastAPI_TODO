from pydantic import BaseModel, Field, EmailStr

class User(BaseModel):
    username: str = Field(..., min_length=5, max_length=25, description="Username")
    password: str = Field(..., min_length=8, max_length=16, description="Password")


class UserCreate(User):
    email: EmailStr = Field(..., description="Email address")
    firstname: str = Field(..., max_length=20, description="Firstname")
    lastname: str = Field(..., max_length=20, description="Lastname")

class UserResponse(User):
    id: int = Field(..., description="User id")