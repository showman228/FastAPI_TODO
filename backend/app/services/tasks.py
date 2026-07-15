from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from ..repositories.tasks_repositories import TaskRepository
from ..repositories.users_repositories import UserRepository
from ..schemas.tasks import TaskResponse, TaskCreate
from fastapi import HTTPException, status


class TaskService:
    def __init__(self, db: AsyncSession):
        self.task_repository = TaskRepository(db)
        self.user_repository = UserRepository(db)

    async def get_all_tasks_by_user(self, user_id: int) -> List[TaskResponse]:
        tasks = await self.task_repository.get_by_user_id(user_id)
        return [TaskResponse.model_validate(task) for task in tasks]

    async def get_task_by_id(self, id: int) -> TaskResponse:
        task = await self.task_repository.get_by_id(id)
        if not task:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Task with id {id} not found",
            )
        return TaskResponse.model_validate(task)

    async def get_all_tasks(self) -> List[TaskResponse]:
        tasks = await self.task_repository.get_all()
        return [TaskResponse.model_validate(task) for task in tasks]

    async def create_task(self, task_data: TaskCreate) -> TaskResponse:
        user = await self.user_repository.get_by_id(task_data.user_id)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"User with id {task_data.user_id} not found",
            )
        task = await self.task_repository.create(
            task=task_data,
            user_id=user.id
        )
        return TaskResponse.model_validate(task)

    async def update_task(self, task_id: int, task_data: TaskCreate) -> TaskResponse:
        task = await self.task_repository.get_by_id(task_id)
        if not task:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Task with id {task_id} not found",
            )
        task = await self.task_repository.update(task_id, task_data)
        return TaskResponse.model_validate(task)

    async def delete_task(self, task_id: int) -> bool:
        task = await self.task_repository.get_by_id(task_id)
        if not task:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Task with id {task_id} not found",
            )
        return await self.task_repository.delete(task_id)
