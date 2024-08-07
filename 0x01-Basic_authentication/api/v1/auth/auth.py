#!/usr/bin/env python3
""" Manage API authentication
"""
import re
from flask import request
from typing import List, TypeVar


class Auth:
    """Class to handle authentication
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Args:
            path (str): included path
            excluded_paths (List[str]): excluded paths

        Returns:
            bool: true or false
        """
        if path is not None and excluded_paths is not None:
            for exclusion_path in map(lambda x: x.strip(), excluded_paths):
                pattern = ''
                if exclusion_path[-1] == '*':
                    pattern = '{}.*'.format(exclusion_path[0:-1])
                elif exclusion_path[-1] == '/':
                    pattern = '{}/*'.format(exclusion_path[0:-1])
                else:
                    pattern = '{}/*'.format(exclusion_path)
                if re.match(pattern, path):
                    return False
        return True

    def authorization_header(self, request=None) -> str:
        """
        Args:
            request (_type_, optional): _description_. Defaults to None.

        Returns:
            authorization header
        """
        if request is not None:
            return request.headers.get('Authorization', None)
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Gets the current user
        """
        return None
