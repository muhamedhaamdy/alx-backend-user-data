#!/usr/bin/env python3
''' Authentication system '''
import bcrypt
from db import DB
from user import User


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()
    
    def register_user(self, email: str, password: str) -> User:
        ''' signup for the user with email and password '''
        find_user = self._db._session.query(User).filter_by(email=email).first()
        if find_user:
            raise ValueError(f'User {find_user.email} already exists')
        else:
            hash = _hash_password(password)
            new_user = User(email=email, hashed_password=hash)
            self._db._session.add(new_user)
            self._db._session.commit() 

def _hash_password(password: str) -> bytes:
    ''' return a hashed password '''
    bytes = password.encode()
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(bytes, salt)
