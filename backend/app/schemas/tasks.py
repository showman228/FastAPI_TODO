from pydantic import BaseModel, Field

class Task(BaseModel):
    name: str = Field(..., min_length=5, max_length=100, description="Task name")
    description: str = Field(default="None", description="Task description", max_length=300)

class TaskCreate(Task):
    pass

class TaskResponse(Task):
    id: int = Field(..., description="Task id")

