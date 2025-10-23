from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlalchemy import select, delete
from sqlalchemy.exc import IntegrityError
from BackEnd.models import User
from BackEnd.schema import UserOut 
from BackEnd.database import Session


router = APIRouter()

# Admin Routers
@router.get("/admin/get-users", status_code=200)
def get_users(): 
    with Session() as session: 
        try:
            users = session.scalars(select(User)).all()
            
            print("PRINTING USERS---------------------------------------------------:")
            
            if not users: 
                print("NO USERS IN DATABASE")
            else: 
                for user in users: 
                    print(user.to_string(user.id, user.username))
                    
            print("---------------------------------------------------------------------")
            
        except IntegrityError:
            raise HTTPException(status_code=400, detail="Could not get users")

@router.delete("/admin/delete-users", status_code=status.HTTP_200_OK)
def delete_users(): 
    with Session() as session: 
        try: 
            session.execute(delete(User))
            session.commit()
        except IntegrityError:
            session.rollback()
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Error deleting all users") 
            
    
    
    