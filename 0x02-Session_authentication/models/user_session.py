#!/usr/bin/env python3
"""User Session Model MOdule
"""
from models.base import Base


class UserSession(Base):
    """class t handle user session
    """
    def __init__(self, *args: list, **kwargs: dict):
        """Initializes the class
        """
        super().__init__(*args, *kwargs)
        self.user_id = kwargs.get('user_id')
        self.session_id = kwargs.get('session_id')
