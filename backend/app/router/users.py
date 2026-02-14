from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List
from backend.app.database import get_db
from backend.app.schemas.users import UserResponse, UserCreate, UserUpdate
from backend.app.services.users import UserService

router = APIRouter(
    prefix="/users",
    tags=["users"],
)

@router.get("", response_model=List[UserResponse], status_code=status.HTTP_200_OK)
def get_users(db: Session = Depends(get_db)):
    service = UserService(db)
    return service.get_all_users()

@router.get("/{user_id}", response_model=UserResponse, status_code=status.HTTP_200_OK)
def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    service = UserService(db)
    return service.get_user_by_id(user_id)

@router.post("", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(user_data: UserCreate, db: Session = Depends(get_db)):
    service = UserService(db)
    return service.create_user(user_data)

@router.put("/{user_id}", response_model=UserResponse, status_code=status.HTTP_200_OK)
def update_user(user_id: int, user_data: UserUpdate, db: Session = Depends(get_db)):
    service = UserService(db)
    return service.update_user(user_data, user_id)

@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    service = UserService(db)
    service.delete_user(user_id)
    return None
