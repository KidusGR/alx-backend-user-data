#!/usr/bin/env python3

""" Encrypt passwords """


import bcrypt


def hash_password(password: str) -> bytes:
    """ Salted password generator """

    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """ Validation """

    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
