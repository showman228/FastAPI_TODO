from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from ..repositories.users_repositories import UserRepository
from ..schemas.users import UserResponse, UserCreate, UserUpdate
from fastapi import HTTPException, status


class UserService:
    def __init__(self, db: AsyncSession):
        self.user_repository = UserRepository(db)

    async def get_all_users(self) -> List[UserResponse]:
        users = await self.user_repository.get_all()
        return [UserResponse.model_validate(user) for user in users]

    async def get_user_by_id(self, user_id: int) -> UserResponse:
        user = await self.user_repository.get_by_id(user_id)
        if user is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"User with id {user_id} not found",
            )
        return UserResponse.model_validate(user)

    async def get_user_by_email(self, user_data: UserCreate) -> UserResponse:
        user = await self.user_repository.get_by_email(user_data.email)
        if user is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"User with email {user_data.email} not found",
            )
        return UserResponse.model_validate(user)

    async def get_by_username(self, user_data: UserCreate) -> UserResponse:
        user = await self.user_repository.get_by_username(user_data.username)
        if user is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"User with username {user_data.username} not found",
            )
        return UserResponse.model_validate(user)

    async def create_user(self, user_data: UserCreate) -> UserResponse:
        check_user = await self.user_repository.get_by_email(user_data.email)
        if check_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"User with email {user_data.email} already exists",
            )

        check_user = await self.user_repository.get_by_username(user_data.username)
        if check_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"User with username {user_data.username} already exists",
            )

        user = await self.user_repository.create(user_data)
        return UserResponse.model_validate(user)

    async def update_user(self, user_data: UserUpdate, user_id: int) -> UserResponse:
        user = await self.user_repository.get_by_id(user_id)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"User with id {user_id} not found"
            )

        if user_data.email and user_data.email != user.email:
            existing = await self.user_repository.get_by_email(user_data.email)
            if existing:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="User with this email already exists"
                )

        if user_data.username and user_data.username != user.username:
            existing = await self.user_repository.get_by_username(user_data.username)
            if existing:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="User with this username already exists"
                )

        updated_user = await self.user_repository.update(user_data, user_id)
        return UserResponse.model_validate(updated_user)

    async def delete_user(self, user_id: int) -> bool:
        success = await self.user_repository.delete(user_id)
        if not success:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"User with id {user_id} not found"
            )
        return True
