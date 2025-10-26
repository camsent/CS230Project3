from fastapi import HTTPException, Request, status
from sqlalchemy import select
from BackEnd.database import Session
from BackEnd.models import Active_Session




def check_user(request: Request): 
    token = request.headers.get("Authorization")
     
    if not token: 
         raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Must be logged in")       
    
    with Session() as session: 
       active = session.scalars(
            select(Active_Session)
            .where(Active_Session.id == token)
            ).first()
        
    if not active:
            raise HTTPException(status_code=403, detail="Not authorized")
        
    return active.user_id  # returned to your route    
    
     
     
     
        