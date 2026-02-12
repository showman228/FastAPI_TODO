from sqlalchemy.orm import Session
from typing import List
from backend.app.repositories.users_repositories import UserRepository
from backend.app.repositories.tasks_repositories import TaskRepository
from fastapi import HTTPException, status

class UserService:
    def __init__(self, db: Session):
        self.repository = UserRepository(db)


