from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import List, Optional
from ..models.tasks import Task
from ..schemas.tasks import TaskCreate


class TaskRepository():
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_by_id(self, id: int) -> Optional[Task]:
        result = await self.db.execute(select(Task).filter(Task.id == id))
        return result.scalar_one_or_none()

    async def get_all(self) -> List[Task]:
        result = await self.db.execute(select(Task))
        return list(result.scalars().all())

    async def get_by_user_id(self, user_id: int) -> List[Task]:
        result = await self.db.execute(select(Task).filter(Task.user_id == user_id))
        return list(result.scalars().all())

    async def create(self, task: TaskCreate, user_id: int) -> Task:
        db_task = Task(
            name=task.name,
            description=task.description,
            user_id=user_id
        )
        self.db.add(db_task)
        await self.db.commit()
        await self.db.refresh(db_task)
        return db_task

    async def update(self, id: int, task_data: TaskCreate) -> Optional[Task]:
        db_task = await self.get_by_id(id)
        if db_task is None:
            return None

        db_task.name = task_data.name
        if task_data.description is not None:
            db_task.description = task_data.description

        await self.db.commit()
        await self.db.refresh(db_task)
        return db_task

    async def delete(self, id: int) -> bool:
        db_task = await self.get_by_id(id)
        if db_task is None:
            return False
        await self.db.delete(db_task)
        await self.db.commit()
        return True
