from typing import Optional
from sqlalchemy import ForeignKey, String, Boolean, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from datetime import datetime, timezone
<<<<<<< HEAD
import uuid
=======
from BackEnd.database import Base
import uuid

>>>>>>> 7c466b8ab26d1daa7a1f3efbd646360460f7b86c



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
<<<<<<< HEAD

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    completed: Mapped[bool] = mapped_column(Boolean, default=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=lambda: datetime.now(timezone.utc))
    user_id: Mapped[Optional[uuid.UUID]] = mapped_column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=True)

    # Relationship back to User
    user = relationship("User", back_populates="tasks")
=======
    id: Mapped[int] = mapped_column(primary_key=True)
    task_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    description: Mapped[str] = mapped_column(nullable=False)
    created_at: Mapped[datetime]= mapped_column(default=lambda: datetime.now(timezone.utc))
    
    user: Mapped["User"] = relationship("User", back_populates="tasks")
     
>>>>>>> 7c466b8ab26d1daa7a1f3efbd646360460f7b86c
