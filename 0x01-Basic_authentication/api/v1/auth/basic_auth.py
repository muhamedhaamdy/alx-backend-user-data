#!/usr/bin/env python3
'''BasicAuth module'''
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    '''BasicAuth class'''
    def extract_base64_authorization_header(self, authorization_header):
        '''extract_base64_authorization_header method'''
        if authorization_header is None\
                or not isinstance(authorization_header, str)\
                or not authorization_header.startswith("Basic "):
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(self, base64_authorization_header):
        '''decode_base64_authorization_header method'''
        if base64_authorization_header is None\
                or not isinstance(base64_authorization_header, str):
            return None
        try:
            import base64
            return \
                base64.b64decode(base64_authorization_header).decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(self, decoded_base64_authorization_header):
        '''extract_user_credentials method'''
        if decoded_base64_authorization_header is None\
                or not isinstance(decoded_base64_authorization_header, str)\
                or ':' not in decoded_base64_authorization_header:
            return (None, None)
        return tuple(decoded_base64_authorization_header.split(':', 1))

    def user_object_from_credentials(self, user_email, user_pwd):
        '''user_object_from_credentials method'''
        if user_email is None or not isinstance(user_email, str)\
                or user_pwd is None or not isinstance(user_pwd, str):
            return None
        try:
            from models.user import User
            users = User.search({'email': user_email})
            for user in users:
                if user.is_valid_password(user_pwd):
                    return user
        except Exception:
            return None
        return None
