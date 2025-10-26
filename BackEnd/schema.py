from uuid import UUID
from click import Option
from pydantic import BaseModel, ConfigDict, EmailStr
<<<<<<< HEAD
from typing import List, Optional
from datetime import date, datetime, time
from sqlalchemy import UUID 
=======
from typing import List, Union
from datetime import date, datetime, time 
>>>>>>> 7c466b8ab26d1daa7a1f3efbd646360460f7b86c


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
<<<<<<< HEAD
    user_ids: List[UUID] = []
=======
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