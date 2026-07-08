from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from backend.app.schemas.tasks import TaskResponse, TaskCreate
from backend.app.services.tasks import TaskService
from backend.app.database import get_db


router = APIRouter(
    prefix="/tasks",
    tags=["tasks"],
)

@router.get("", response_model=List[TaskResponse], status_code=status.HTTP_200_OK)
async def get_all_tasks(db: AsyncSession = Depends(get_db)):
    service = TaskService(db)
    return await service.get_all_tasks()

@router.get("/user/{user_id}", response_model=List[TaskResponse], status_code=status.HTTP_200_OK)
async def get_all_task_by_user(user_id: int, db: AsyncSession = Depends(get_db)):
    service = TaskService(db)
    return await service.get_all_tasks_by_user(user_id)

@router.get("/{task_id}", response_model=TaskResponse, status_code=status.HTTP_200_OK)
async def get_task_by_id(task_id: int, db: AsyncSession = Depends(get_db)):
    service = TaskService(db)
    return await service.get_task_by_id(task_id)

@router.post("", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
async def create_task(task: TaskCreate, db: AsyncSession = Depends(get_db)):
    service = TaskService(db)
    return await service.create_task(task)

@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(task_id: int, db: AsyncSession = Depends(get_db)):
    service = TaskService(db)
    await service.delete_task(task_id)
    return None

@router.put("/{task_id}", response_model=TaskResponse, status_code=status.HTTP_200_OK)
async def update_task(task_id: int, task: TaskCreate, db: AsyncSession = Depends(get_db)):
    service = TaskService(db)
    return await service.update_task(task_id, task)
