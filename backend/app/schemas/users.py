from pydantic import BaseModel, Field, EmailStr
from datetime import datetime

class UserBase(BaseModel):
    username: str = Field(..., min_length=5, max_length=25, description="Username")

class UserCreate(UserBase):
    email: EmailStr = Field(..., description="Email address")
    firstname: str = Field(..., max_length=20, description="Firstname")
    lastname: str = Field(..., max_length=20, description="Lastname")
    password: str = Field(..., min_length=8, max_length=20, description="Password")

class UserUpdate(UserCreate):
    username: str = Field(..., min_length=5, max_length=25, description="Username")

class UserResponse(UserBase):
    id: int = Field(..., description="User id")
    email: EmailStr = Field(..., description="Email address")
    firstname: str | None = Field(None, description="Firstname") # str | None вместо default="None" для опциональных полей
    lastname: str | None = Field(None, description="Lastname") # str | None вместо default="None" для опциональных полей
    created_at: datetime = Field(..., description="Creation timestamp")
    
    class Config:
        from_attributes = True # без этого Pydantic не сможет преобразовать SQLAlchemy модели в схемы