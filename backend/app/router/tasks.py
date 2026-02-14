from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List
from backend.app.schemas.tasks import TaskResponse, TaskCreate
from backend.app.services.tasks import TaskService
from backend.app.database import get_db


router = APIRouter(
    prefix="/tasks",
    tags=["tasks"],
)
# написать так, что при переходе на адрес, выводится все пользователи и их задачи (скорее всего можно это будет реализовать через фронтенд)
@router.get("", response_model=List[TaskResponse], status_code=status.HTTP_200_OK)
def get_all_tasks(db: Session = Depends(get_db)):
    service = TaskService(db)
    return service.get_all_tasks()

@router.get("/user/{user_id}", response_model=List[TaskResponse], status_code=status.HTTP_200_OK)
def get_all_task_by_user(user_id: int, db: Session = Depends(get_db)):
    service = TaskService(db)
    return service.get_all_tasks_by_user(user_id)

@router.get("/{task_id}", response_model=TaskResponse, status_code=status.HTTP_200_OK)
def get_task_by_id(task_id: int, db: Session = Depends(get_db)):
    service = TaskService(db)
    return service.get_task_by_id(task_id)

@router.post("/users/{user_id}", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
def create_task(user_id: int, task: TaskCreate, db: Session = Depends(get_db)):
    service = TaskService(db)
    return service.create_task(user_id, task)

@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    service = TaskService(db)
    service.delete_task(task_id)
    return None

@router.put("/{task_id}", response_model=TaskResponse, status_code=status.HTTP_200_OK)
def update_task(task_id: int, task: TaskCreate, db: Session = Depends(get_db)):
    service = TaskService(db)
    return service.update_task(task_id, task)