#!/usr/bin/env python3
"""Session Authentication Module"""
import uuid
from auth import Auth


class SessionAuth(Auth):
    """Handle Session Authentication

    Args:
        Auth: Authentication mother class
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Instance method to create a session"""
        if type(user_id) is str:
            session_id = str(uuid.uuid4())
            self.user_id_by_session_id[session_id] = user_id
            return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Returns user_id by session_id"""
        if type(session_id) is str:
            return self.user_id_by_session_id.get(session_id)            
