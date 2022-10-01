#!/usr/bin/python3
from models.base_model import BaseModel
""" Module for class User """


class User(BaseModel):
    """
    Class User that imports from BaseModel
    Attributes:
    email: email of User
    password: password of User
    first_name: first name of User
    last_name: last name of User
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""