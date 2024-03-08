#!/usr/bin/env python3
"""
a module to contain the BaseModel class
"""
from uuid import uuid4
from datetime import datetime as dt
from models.__init__ import storage


class BaseModel:
    """a class that that defines all common
    attributes/methods for other classes

    Attributes:
        id: string - assign with an uuid when an
            instance is created
        created_at: datetime - assign with the current
            datetime when an instance is created
        updated_at: datetime - assign with the current
            datetime when an instance is created and it will
            be updated every time you change your object

    Methods:
        save: updates the public instance attribute
            updated_at with the current datetime
        to_dict: returns a dictionary containing all keys/values of
            __dict__ of the instance
    """

    def __init__(self, *args, **kwargs):
        """instantiates new BaseModel instances"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at":
                    self.created_at = dt.fromisoformat(value)
                elif key == "updated_at":
                    self.updated_at = dt.fromisoformat(value)
                elif key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = dt.now()
            self.updated_at = dt.now()
            storage.new(self)

    def __str__(self):
        """returns a human readable string

        Return:
            a type of str
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """updates the public instance attribute
        updated_at with the current datetime
        """
        self.updated_at = dt.now()
        storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values
        of __dict__ of the instance

        Return:
            a type of dict
        """
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = f"{self.__class__.__name__}"
        new_dict["created_at"] = dt.isoformat(new_dict["created_at"])
        new_dict["updated_at"] = dt.isoformat(new_dict["updated_at"])
        return new_dict
