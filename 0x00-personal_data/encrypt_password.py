#!/usr/bin/env python3
''' Encrypting passwords '''
import bcrypt


def hash_password(password: str) -> bytes:
    ''' Returns a salted, hashed password '''
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    ''' Validates a password '''
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
