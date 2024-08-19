#!/usr/bin/env python3
"""Authentication Module
"""
import bcrypt
from sqlalchemy.orm.exc import NoResultFound

from user import Base, User
from db import DB


def _hash_password(password: str) -> bytes:
    """takes in a password string arguments and returns bytes
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Method to register user
        """
        try:
            user = self._db.find_user(email=email)
        except NoResultFound:
            return self._db.add_user(email, _hash_password(password))
        raise ValueError("User {} already exists".format(email))
