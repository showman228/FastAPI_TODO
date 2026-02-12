from sqlalchemy.orm import Session
from typing import List, Optional
from backend.app.models.tasks import Task
from backend.app.schemas.tasks import TaskCreate


class TaskRepository():
    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, id: int) -> Optional[Task]:
        return self.db.query(Task).filter(Task.id == id).first()

    def get_all(self) -> List[Task]:
        return self.db.query(Task).all()

    def get_by_user_id(self, user_id: int) -> List[Task]:
        return self.db.query(Task).filter(Task.user_id == user_id).all()

    def create(self, task: TaskCreate, user_id: int) -> Task:
        db_task = Task(
            name=task.name,
            description=task.description,
            user_id=user_id
        )
        self.db.add(db_task)
        self.db.commit()
        self.db.refresh(db_task)
        return db_task

    def update(self, id: int, task_data: TaskCreate) -> Optional[Task]:
        db_task = self.get_by_id(id)
        if db_task is None:
            return None

        db_task.name = task_data.name
        if task_data.description is not None:
            db_task.description = task_data.description

        self.db.commit()
        self.db.refresh(db_task)
        return db_task

    def delete(self, id: int) -> bool:
        db_task = self.get_by_id(id)
        if db_task is None:
            return False
        self.db.delete(db_task)
        self.db.commit()
        return True