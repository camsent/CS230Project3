from click import Option
from pydantic import BaseModel, ConfigDict, EmailStr
from typing import List, Optional
from datetime import date, datetime, time
from sqlalchemy import UUID 


class UserBase(BaseModel): 
    name: str
    
class UserCreate(UserBase): 
    password: str
    
class TaskCreate(BaseModel): 
    title: str
    description: str | None
    user_ids: List[UUID] = []