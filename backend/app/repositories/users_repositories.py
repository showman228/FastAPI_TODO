from sqlalchemy.orm import Session
from typing import List, Optional
from backend.app.models.user import User
from backend.app.schemas.users import UserCreate, UserUpdate
from pydantic import EmailStr

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, id: int) -> Optional[User]:
        return self.db.query(User).filter(User.id == id).first()

    def get_all(self) -> List[User]:
        return self.db.query(User).all()

    def get_by_email(self, email: EmailStr) -> Optional[User]:
        return self.db.query(User).filter(User.email == email).first()

    def get_by_username(self, username: str) -> Optional[User]:
        return self.db.query(User).filter(User.username == username).first()

    def create(self, user: UserCreate) -> User:
        db_user = User(**user.model_dump())

        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def update(self, user: UserUpdate, user_id: int) -> Optional[User]:
        db_user = self.get_by_id(user_id)
        if not db_user:
            return None

        user.firstname = db_user.firstname
        user.lastname = db_user.lastname
        user.email = db_user.email
        user.username = db_user.username

        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def delete(self, user_id: int) -> bool:
        db_user = self.get_by_id(user_id)

        if not db_user:
            return False

        self.db.delete(db_user)
        self.db.commit()
        return True
