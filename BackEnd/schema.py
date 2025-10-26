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
    id: str 
    title: str
    description: str | None
    due_date: str
    
    model_config = ConfigDict(from_attributes=True)


# class UserOut(UserBase): 
#     id: UUID
#     Tasks: List[TaskBase]
    
#     model_config = ConfigDict(from_attributes=True)
    
    
class TaskCreate(TaskBase): 
    model_config = ConfigDict(from_attributes=True)
    
    
class TaskOut(TaskBase): 
    model_config = ConfigDict(from_attributes=True)
    

class TaskOutAll(BaseModel): 
    Tasks: List[TaskBase]
    
    model_config = ConfigDict(from_attributes=True)
    
class TaskUpdate(BaseModel):
    title: str | None
    description: str | None
    due_date: str | None
    