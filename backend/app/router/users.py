from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List
from backend.app.database import get_db
from backend.app.schemas.users import UserResponse
from backend.app.services.users import UserService

router = APIRouter(
    prefix="/users",
    tags=["users"],
)

@router.get("", response_model=List[UserResponse], status_code=status.HTTP_200_OK)
def get_users(db: Session = Depends(get_db)):
    service = UserService(db)
    return service.get_all_users()

@router.get("/{user_id", response_model=UserResponse, status_code=status.HTTP_200_OK)
def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    service = UserService(db)
    return service.get_user_by_id(user_id)




