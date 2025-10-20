from click import Option
from pydantic import BaseModel, ConfigDict, EmailStr
from typing import List, Optional
from datetime import date, datetime, time 


class UserBase(BaseModel): 
    name: str
    
class UserCreate(UserBase): 
    password: str
    
class TaskBase(BaseModel): 
    title: str
    description: str | None