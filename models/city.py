#!/usr/bin/env python3
"""
a module for the City class
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    a class that inherits from BaseModel

    Attributes:
        state_id : string
        name : string
    """

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
