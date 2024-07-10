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
