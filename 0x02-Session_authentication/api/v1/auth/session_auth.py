#!/usr/bin/env python3
''' session_auth module '''
from api.v1.auth.auth import Auth
import uuid
from models.user import User


class SessionAuth(Auth):
    ''' session_auth module '''
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        '''creating session'''
        if user_id is None or not isinstance(user_id, str):
            return None
        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        '''return the user id based on session id'''
        if session_id is None or not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        '''Session ID for identifying a User'''
        cookie_value = self.session_cookie(request)
        user_id = self.user_id_for_session_id(cookie_value)
        return User().get(user_id)

    def destroy_session(self, request=None):
        '''ends up a session'''
        session_id = self.session_cookie(request)
        user_id = self.user_id_for_session_id(session_id)
        if not request or not session_id or not user_id:
            return None
        del self.user_id_by_session_id[session_id]
        return True
