from sqlalchemy import Column, Integer, String, Text, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime, UTC
from ..database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False, index=True)
    email = Column(String, nullable=False, index=True)
    full_name = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), default=datetime.now(UTC))
    priority_of_tasks = Column(Integer, nullable=True)

    task = relationship("Tasks", back_populates="users")

    def __repr__(self):
        return f"<User(id={self.id}, username={self.username}, email={self.email})>"