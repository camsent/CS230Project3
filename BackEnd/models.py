from typing import List, Dict, Optional
from sqlalchemy import ForeignKey, String, DateTime, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from datetime import datetime, timezone
from BackEnd.database import Base
import uuid


class User(Base): 
    __tablename__ = "users"
    
    id: Mapped[str] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(nullable=False, unique=True, index=True)
    hashed_password: Mapped[str] =  mapped_column(nullable=False)
    #logged_in: Mapped[bool] = mapped_column(nullable=False, default=False)
    
    tasks: Mapped[List["Task"]] = relationship("Task", cascade="all, delete")
    
    @staticmethod
    def to_string(user_id, username):
       return f"ID: {user_id}, Username: {username}" 

class Task(Base):
    __tablename__ = "tasks"
    id: Mapped[int] = mapped_column(primary_key=True)
    task_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    description: Mapped[str] = mapped_column(nullable=False)
    due_date: Mapped[str] = mapped_column()
    created_at: Mapped[datetime]= mapped_column(DateTime(timezone=True), server_default=func.now())
    
    user: Mapped["User"] = relationship("User", back_populates="tasks")
     
class Active_Session(Base): 
    __tablename__ = "sessions"
    id: Mapped[str] = mapped_column(primary_key=True)
    user_id: Mapped[str] = mapped_column(primary_key=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    
    @staticmethod
    def to_string(id, user_id): 
        return f"ID: {id}, USER_ID: {user_id}"