from typing import List, Dict, Optional
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from datetime import datetime, timezone


class Base(DeclarativeBase):
    pass

class User(Base): 
    __tablename__ = "users"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False, unique=True, index=True)
    hashed_password: Mapped[str] =  mapped_column(String, nullable=False)
    
    tasks: Mapped[List["Task"]] = relationship(
        "Task", back_populates='user', cascade="all, delete"
    )

class Task(Base): 
    __tablename__ = "tasks"
    id: Mapped[int] = mapped_column(primary_key=True)
    description: Mapped[str] = mapped_column(nullable=False)
    created_at: Mapped[datetime]= mapped_column(default=lambda: datetime.now(timezone.utc))
    
    user: Mapped["User"] = relationship(back_populates="tasks")
     