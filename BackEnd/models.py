from typing import Optional, List
from sqlalchemy import ForeignKey, String, Boolean, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from datetime import datetime, timezone
from BackEnd.database import Base
import uuid


class User(Base): 
    __tablename__ = "users"
    
    id: Mapped[str] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(nullable=False, unique=True, index=True)
    hashed_password: Mapped[str] =  mapped_column(nullable=False)
    logged_in: Mapped[bool] = mapped_column(nullable=False, default=False)
    
    tasks: Mapped[List["Task"]] = relationship("Task", cascade="all, delete")
    
    @staticmethod
    def to_string(user_id, username):
       return f"ID: {user_id}, Username: {username}" 

class Task(Base):
    __tablename__ = "tasks"
    id: Mapped[int] = mapped_column(primary_key=True)
    task_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    description: Mapped[str] = mapped_column(nullable=False)
    created_at: Mapped[datetime]= mapped_column(default=lambda: datetime.now(timezone.utc))
    
    user: Mapped["User"] = relationship("User", back_populates="tasks")