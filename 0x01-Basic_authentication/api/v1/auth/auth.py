#!/usr/bin/env python3
'''auth module'''
from flask import request
from typing import List, TypeVar
from models.user import User


class Auth:
    '''auth class'''
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        '''require_auth method'''
        if path and not path.endswith('/'):
            path += '/'
        if path is None or excluded_paths is None or len(excluded_paths) == 0\
                or path not in excluded_paths:
            return True
        return False

    def authorization_header(self, request=None) -> str:
        '''authorization_header method'''
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        '''current_user method'''
        return None
