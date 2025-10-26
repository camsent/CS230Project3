from fastapi import APIRouter, HTTPException, status
from sqlalchemy import select, update, delete
from sqlalchemy.exc import IntegrityError
from BackEnd.database import Session
from BackEnd.models import Task, User
from BackEnd.schema import TaskCreate
from datetime import datetime, timezone

router = APIRouter(prefix="/tasks", tags=["Tasks"])

# CREATE
@router.post("/", status_code=status.HTTP_201_CREATED)
def create_task(task: TaskCreate, user_id: str):
    with Session() as session:
        user = session.scalars(select(User).where(User.id == user_id)).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        try:
            new_task = Task(
                task_id=user_id,
                description=task.description,
                created_at=datetime.now(timezone.utc)
            )
            session.add(new_task)
            session.commit()
            return {"message": "Task created", "task_id": new_task.id}
        except IntegrityError:
            session.rollback()
            raise HTTPException(status_code=400, detail="Could not create task")

# READ ALL
@router.get("/", status_code=200)
def get_all_tasks():
    with Session() as session:
        tasks = session.scalars(select(Task)).all()
        return [
            {"id": t.id, "user_id": t.task_id, "description": t.description, "created_at": t.created_at}
            for t in tasks
        ]

# READ BY USER
@router.get("/user/{user_id}", status_code=200)
def get_user_tasks(user_id: str):
    with Session() as session:
        tasks = session.scalars(select(Task).where(Task.task_id == user_id)).all()
        if not tasks:
            raise HTTPException(status_code=404, detail="No tasks found for this user")
        return [
            {"id": t.id, "description": t.description, "created_at": t.created_at}
            for t in tasks
        ]

# UPDATE
@router.put("/{task_id}", status_code=200)
def update_task(task_id: int, description: str):
    with Session() as session:
        task = session.get(Task, task_id)
        if not task:
            raise HTTPException(status_code=404, detail="Task not found")
        task.description = description
        session.commit()
        return {"message": "Task updated", "task_id": task_id}

# DELETE
@router.delete("/{task_id}", status_code=200)
def delete_task(task_id: int):
    with Session() as session:
        task = session.get(Task, task_id)
        if not task:
            raise HTTPException(status_code=404, detail="Task not found")
        session.delete(task)
        session.commit()
        return {"message": "Task deleted", "task_id": task_id}
