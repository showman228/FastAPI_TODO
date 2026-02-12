from sqlalchemy.orm import Session
from typing import List
from backend.app.repositories.tasks_repositories import TaskRepository
from backend.app.repositories.users_repositories import UserRepository
from backend.app.schemas.tasks import TaskResponse, TaskCreate
from fastapi import HTTPException, status

class TaskService:
    def __init__(self, db: Session):
        self.task_repository = TaskRepository(db)
        self.user_repository = UserRepository(db)

    def get_all_tasks_by_user(self, user_id: int) -> List[TaskResponse]:
        tasks = self.task_repository.get_by_user_id(user_id)
        tasks_response = [TaskResponse.model_validate(task) for task in tasks]
        return tasks_response

    def get_task_by_id(self, id: int) -> TaskResponse:
        task = self.task_repository.get_by_id(id)
        if not task:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Task with id {id} not found",
            )
        return TaskResponse.model_validate(task)

    def get_all_tasks(self) -> List[TaskResponse]:
        tasks = self.task_repository.get_all()
        tasks_response = [TaskResponse.model_validate(task) for task in tasks]
        return tasks_response


    def create_task(self, task_data: TaskCreate) -> TaskResponse:
        user = self.user_repository.get_by_id(task_data.user_id)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"User with id {task_data.user_id} not found",
            )
        task = self.task_repository.create(
            task=task_data,
            user_id=user.id
        )

        return TaskResponse.model_validate(task)

    def update_task(self, task_id: int, task_data: TaskCreate) -> TaskResponse:
        task = self.task_repository.get_by_id(task_id)
        if not task:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Task with id {task_id} not found",
            )
        task = self.task_repository.update(task_id, task_data)
        return TaskResponse.model_validate(task)


    def delete_task(self, task_id: int) -> bool:
        task = self.task_repository.get_by_id(task_id)
        if not task:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Task with id {task_id} not found",
            )
        return self.task_repository.delete(task_id)