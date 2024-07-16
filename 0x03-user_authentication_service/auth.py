#!/usr/bin/env python3
''' Authentication system '''
import bcrypt


def _hash_password(password: str) -> bytes:
    ''' return a hashed password '''
    bytes = password.encode()
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(bytes, salt)
