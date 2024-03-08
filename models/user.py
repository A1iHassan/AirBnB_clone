#!/usr/bin/env python3
"""
a module for the User class
"""
from models.base_model import BaseModel
from datetime import datetime as dt


class User(BaseModel):
    """
    a class that inherits from BaseModel

    Attributes:
        email : string - empty string
        password : string - empty string
        first_name : string - empty string
        last_name : string - empty string
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
