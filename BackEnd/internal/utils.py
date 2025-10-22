from sqlalchemy import select
from BackEnd.models import User



def check_user_id(user_id, session):
    user = session.scalars(select(User).where(User.id == user_id)).first()
    if user:
        return True
    return False



