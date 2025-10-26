from fastapi import APIRouter, Depends, HTTPException, status, Response
from typing import Annotated
from sqlalchemy import select, update, delete
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from BackEnd.models import User
from BackEnd.schema import UserCreate
from BackEnd.models import User, Task, Active_Session
from BackEnd.schema import UserCreate, TaskOut, TaskCreate, TaskOutAll, TaskBase, TaskUpdate
from BackEnd.database import Session
from BackEnd.auth import auth 
from BackEnd.internal import utils, admin
from BackEnd.middleware import check_user


import uuid

   
router = APIRouter()


@router.get("/")
def root(): 
    return {"Hello": "World"}

@router.post("/register", status_code=status.HTTP_201_CREATED)
def register(user_data: UserCreate):
    data = user_data.model_dump()
    
    if not data["name"] or not data["password"]: 
        return HTTPException(status_code=400, detail="Invalid username or password")
    
    str_password = str(data["password"])
    hashed_pw = auth.hash_password(str_password)
    user_id  = uuid.uuid4()
    user_id = str(user_id)
    
    
   # Move check username out of session
    with Session() as session:
        check_username = session.scalars(select(User).where(User.username == data["username"])).first()
        
        if check_username: 
            raise HTTPException(status_code=400, detail="Username already taken")
        try:
            new_user = User(
                id=user_id,
                username=data["username"],
                hashed_password=hashed_pw,
            )
            session.add(new_user)
            session.commit()
            # result = UserCreateOut.model_validate(new_user)
            result = {"ID: ": user_id, "Username: ": data["username"]}
        except IntegrityError:
            session.rollback()
            raise HTTPException(status_code=400, detail="Error: User ID collision, please try again")

@router.post("/login", status_code=status.HTTP_200_OK)
def login(user_data: UserCreate):
    data = user_data.model_dump()
    
    str_password = str(data["password"])
    user = auth.check_user_id(data["username"])
    
    if not user: 
        raise HTTPException(401, "User does not exist")
    
    user = auth.get_user_data_at_login(data["username"])
    checked_pw = auth.check_password(str_password, user.hashed_password)
    
    if not checked_pw: 
       raise HTTPException(status_code=401, detail="User does not exist")

    
    with Session() as session: 
       try: 
            # stmt = (
            #     update(User)
            #     .where(User.username == data["username"])
            #     .values(logged_in=True)
                
            # )
            sess_id = str(uuid.uuid4())
            
            new_session = Active_Session(
                id = sess_id,
                user_id = user.id
            )
            #session.execute(stmt)
            session.add(new_session)
            
            session.commit()
            
       except IntegrityError: 
            session.rollback()
            raise HTTPException(status_code=400, detail="Bad login request")
            
    return {
        "session_id": sess_id, 
        "user_id: ": user.id, 
        "message": "Login successful" 
    }  
            
@router.post("/logout", status_code=status.HTTP_204_NO_CONTENT)
def logout(user_id: Annotated[str, Depends(check_user.check_user)]): 
    with Session as session: 
        try: 
            stmt = (
                session.scalars(
                    select(Active_Session)
                    .where(Active_Session.user_id == user_id))
                .first(
                )
            )
            session.execute(stmt)
            session.commit()
        except IntegrityError:
            session.rollback()
            raise HTTPException(status_code=400, detail="Unable to logout user")
            
    
@router.post("/task/create", status_code=status.HTTP_201_CREATED)
def create_task(task_data: TaskCreate, user_id: Annotated[str, Depends(check_user.check_user)]):
   
    data = task_data.model_dump()
    task_id = str(uuid.uuid4())
    
    with Session() as session:
        try: 
            task = Task(
                id = task_id,
                user_id = user_id,
                title = data["title"],
                description = data.get("description"),
                due_date = data.get("due_date")
            )
            session.add(task)
            session.commit()
            result = {
                "id -> ": task_id,
                "user_id -> ": user_id,
                "Title -> ": data["title"],
                "Description -> ": data.get("description")
                
            }    
        except IntegrityError: 
            session.rollback()
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Error adding task")
        
    return result



@router.get("/task/get/{task_id}", response_model=TaskOut)
def get_task(task_id: str, user_id: Annotated[str, Depends(check_user.check_user)]): 
    with Session() as session: 
        try: 
            task = session.scalars(
                select(Task)
                .where(Task.id == task_id)
                ).first()
            
            task_out = TaskOut.model_validate(task)
            return task_out 
        
        except IntegrityError: 
            session.rollback()
            raise HTTPException(status_code=400, detail="Error retrieving task")
    
@router.get("/task/get-all", response_model=TaskOutAll)
def get_all_tasks(user_id: Annotated[str, Depends(check_user.check_user)]):
     with Session() as session: 
        try: 
            tasks = session.scalars(
                select(Task)
                .where(Task.user_id == user_id)
                ).all()
            
            tasks_out = TaskOutAll(
                Tasks=[TaskBase.model_validate(t) for t in tasks]
            )
            return tasks_out 
        
        except IntegrityError: 
            session.rollback()
            raise HTTPException(status_code=400, detail="Error retrieving task")
   
   
@router.patch("/task/update/{task_id}", response_model=TaskOut)
def update_tasks(task_data: TaskUpdate, task_id: str, user_id: Annotated[str, Depends(check_user.check_user)]): 
    if not task_data: 
       raise HTTPException(status_code=400, detail="No new task data")
   
    with Session() as session: 
        try: 
            task = session.scalars(
                select(Task)
                .where(Task.id == task_id, Task.user_id == user_id)
                ).first()
            
            if not task: 
                raise HTTPException(status_code=400, detail="Error updating task")

            stmt = (
                update(Task)
                .where(Task.id == task_id, Task.user_id == user_id)
                .values(**task_data.model_dump(exclude_unset=True))
            )
            
            session.execute(stmt)
            session.commit()
                    
            new_task = TaskOut.model_validate(task)
            return new_task
        except IntegrityError: 
            session.rollback()
            raise HTTPException(status_code=400, detail="Error updating task")
                
    
@router.delete("/task/delete/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: str, user_id: Annotated[str, Depends(check_user.check_user)]): 
    with Session() as session: 
        try: 
            task = session.scalars(
                select(Task)
                .where(Task.id == task_id, Task.user_id == user_id)
                ).first()

            if not task: 
                raise HTTPException(status=400, detail="Task does not exist")
            
            stmt = delete(Task).where(Task.id == task_id, Task.user_id == user_id)
            
            session.execute(stmt)
            session.commit()
        except IntegrityError: 
            session.rollback()
            raise HTTPException(status_code=400, detail="Error deleting task")

    
     
    
