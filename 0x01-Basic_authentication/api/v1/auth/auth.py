#!/usr/bin/env python3
""" Auth class """

from tabnanny import check
from flask import request
from typing import TypeVar, List
User = TypeVar('User')


class Auth:
    """
    A python class to manage the API authentication
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Returns Bool - path and excluded_paths
        """
        check = path
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True

        if path[-1] != "/":
            check += "/"

        if check.split("/")[-2][:-2] == "stat":
            check = check[:-3] + "*/"

        if check.split("/")[-2][:-1] == "stat":
            check = check[:-2] + "*/"

        if check in excluded_paths or path in excluded_paths:
            return False

        return True

    def authorization_header(self, request=None) -> str:
        """
        Returns None - request
        """
        if request is None:
            return None
        return request.headers.get("Authorization")

    def current_user(self, request=None) -> User:
        """
        Returns None - request
        """
        return None
