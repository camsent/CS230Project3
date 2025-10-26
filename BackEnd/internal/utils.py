from sqlalchemy import select
from BackEnd.models import User
from BackEnd.database import Session



def check_user_id(user_name):
    
    with Session() as session:
        user = session.scalars(select(User).where(User.username == user_name)).first()
        if user:
            return True
        return False



