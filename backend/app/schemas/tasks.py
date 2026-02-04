from pydantic import BaseModel, Field
from datetime import datetime

class TaskBase(BaseModel):
    name: str = Field(..., min_length=5, max_length=100, description="Task name")
    description: str = Field(default="None", description="Task description", max_length=300)

class TaskCreate(TaskBase):
    pass

class TaskResponse(TaskBase):
    id: int = Field(..., description="Task id")
    user_id: int = Field(..., description="User id who created task")
    created_at: datetime = Field(..., description="Creation timestamp")

    class Config:
        from_attributes = True # без этого Pydantic не сможет преобразовать SQLAlchemy модели в схемы
