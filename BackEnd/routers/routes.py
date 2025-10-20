from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from BackEnd.models import User
from BackEnd.schema import UserCreate
from BackEnd.database import session
from BackEnd.auth import hash_password
from BackEnd.internal import utils

import uuid

  
router = APIRouter()


@router.get("/")
def root(): 
    return {"Hello": "World"}

@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register(user_data: UserCreate):
    data = user_data.model_dump()
    
    if not data["name"] or not data["password"]: 
        return HTTPException(status_code=400, detail="Invalid username or password")
    
    hashed_pw = hash_password(data["password"])
    user_id = uuid.uuid4()

    try:
        session.add(User(
            id=user_id,  
            name=data["name"],
            password=hashed_pw,
        ))
        session.commit()  
    except IntegrityError:
        session.rollback()  # Rollback the failed transaction
        raise HTTPException(status_code=400, detail="Error: User ID collision, please try again")

    session.close()
    
    return {"msg": "User registered successfully"}

@router.post("/tasks", status_code=status.HTTP_201_CREATED)
async def add_task(task_data: TaskCreate, db: Session = Depends(get_db)):
    data = task_data.model_dump()

    if not data["title"]:
        raise HTTPException(status_code=400, detail="Task title is required")

    new_task = Task(
        id=uuid.uuid4(),
        title=data["title"],
        description=data.get("description"),
        user_id=data.get("user_id"),
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return {
        "msg": "Task added successfully",
        "task": {
            "id": str(new_task.id),
            "title": new_task.title,
            "description": new_task.description,
            "completed": new_task.completed,
            "created_at": new_task.created_at,
        }
    }
