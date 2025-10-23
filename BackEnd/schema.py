from uuid import UUID
from click import Option
from pydantic import BaseModel, ConfigDict, EmailStr
from typing import List, Union
from datetime import date, datetime, time 


class UserBase(BaseModel): 
    username: str
    
class UserCreate(UserBase): 
    password: Union[str, int]

class UserOutBase(UserBase):
    id: UUID
    
class AdminUserOut(UserOutBase): 
    Users: List[UserOutBase]
    
class TaskBase(BaseModel): 
    title: str
    description: str | None
    due_date: str
    

class UserOut(UserBase): 
    id: UUID
    Tasks: List[TaskBase]
    
    model_config = ConfigDict(from_attributes=True)