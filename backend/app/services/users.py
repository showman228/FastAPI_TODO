from sqlalchemy.orm import Session
from typing import List
from backend.app.repositories.users_repositories import UserRepository
from backend.app.schemas.users import UserResponse, UserCreate
from fastapi import HTTPException, status

class UserService:
    def __init__(self, db: Session):
        self.user_repository = UserRepository(db)

    def get_all_users(self) -> List[UserResponse]:
        users = self.user_repository.get_all()
        return [UserResponse.model_validate(user) for user in users]

    def get_user_by_id(self, user_id: int) -> UserResponse:
        user = self.user_repository.get_by_id(user_id)
        if user is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"User with id {user_id} not found",
            )
        return UserResponse.model_validate(user)

    def get_user_by_email(self, user_data: UserCreate) -> UserResponse:
        user = self.user_repository.get_by_email(user_data.email)
        if user is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"User with email {user_data.email} not found",
            )
        return UserResponse.model_validate(user)

    def get_by_username(self, user_data: UserCreate) -> UserResponse:
        user = self.user_repository.get_by_username(user_data.username)
        if user is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"User with username {user_data.username} not found",
            )
        return UserResponse.model_validate(user)

    def create_user(self, user_data: UserCreate) -> UserResponse:
        user = self.user_repository.create(user_data)
        return UserResponse.model_validate(user)

    def update_user(self, user_data: UserCreate, user_id: int) -> UserResponse:
        user = self.user_repository.get_by_id(user_id)
        if user is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"User with id {user_id} not found",
            )
        user = self.user_repository.update(user_data)
        return UserResponse.model_validate(user)

    def delete_user(self, user_id: int) -> bool:
        user = self.user_repository.delete(user_id)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"User with id {user_id} not found",
            )
        return True
