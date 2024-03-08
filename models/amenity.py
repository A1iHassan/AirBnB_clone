#!/usr/bin/env python3
"""
a module for the Amenity class
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    a class that inherits from BaseModel

    Attributes:
        name : string
    """

    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
