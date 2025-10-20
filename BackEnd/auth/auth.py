from argon2 import PasswordHasher


ph = PasswordHasher()

def hash_password(pw: str): 
    return ph.hash(pw)


def check_password(pw: str, hashed_pw: str): 
    return ph.verify(hashed_pw, pw)
