from sqlalchemy import Column, Integer, String, Text, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime, UTC
from ..database import Base
# нужно придумать как связать с пользователем его задачу 
class Task:
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, index=True)
    description = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), default=datetime.now(UTC))

    user = relationship("User", back_populates="tasks")

    def __repr__(self):
        return f"<Task(id={self.id}, name={self.name}, description={self.description}, created_at={self.created_at})>"
