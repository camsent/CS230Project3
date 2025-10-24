from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from BackEnd.models import User
from BackEnd.schema import UserCreate, UserOut
from BackEnd.database import Session
from BackEnd.auth import auth 
from BackEnd.internal import utils, admin

import uuid

 
# TODO: Read session docs on SQLalchemy and get this session thing figured out
  
router = APIRouter()


@router.get("/")
def root(): 
    return {"Hello": "World"}

@router.post("/register", status_code=status.HTTP_201_CREATED)
def register(user_data: UserCreate):
    data = user_data.model_dump()
    
    if not data["username"] or not data["password"]: 
        return HTTPException(status_code=400, detail="Invalid username or password")
    
    
    str_password = str(data["password"])
    print(type(str_password))
    hashed_pw = auth.hash_password(str_password)
    user_id  = uuid.uuid4()
    user_id = str(user_id)
    
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
    return result