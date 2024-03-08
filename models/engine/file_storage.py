#!/usr/bin/env python3
"""
a module for the FileStorage class
"""
from json import dump, load
from datetime import datetime as dt


class FileStorage:
    """a class that serializes instances to a JSON
    file and deserializes JSON file to instances

    Attributes:
        __file_path: string - path to the JSON file
        __objects: dictionary - empty but will store
            all objects by <class name>.id

    Methods:
        all(self): returns the dictionary __objects
        new(self, obj): sets in __objects the obj
            with key <obj class name>.id
        save(self): serializes __objects to the JSON
            file (path: __file_path )
        reload(self): deserializes the JSON file to __objects
            (only if the JSON file ( __file_path ) exists)
    """

    __file_path = "file.json"
    __objects = dict()

    def all(self):
        """returns the dictionary of stored objects

        Return:
            a type of dict
        """
        return self.__objects

    def new(self, obj):
        """sets in the storage dictionary the obj
        with key <obj class name>.id

        Args:
            obj: user input
        """
        new_key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[new_key] = obj.to_dict()

    def save(self):
        """serializes storage dictionary to the JSON
        file
        """
        for key, value in self.__objects.items():
            if not isinstance(value["updated_at"], str):
                value["updated_at"] = dt.isoformat(value["updated_at"])

        with open(self.__file_path, 'w', encoding="utf-8") as f:
            dump(self.__objects, f, indent=4)

    def reload(self):
        """ deserializes the JSON file to the storage
        dictionary (only if the JSON file ( __file_path )
        exists)
        """
        try:
            with open(self.__file_path, 'r', encoding="utf-8") as f:
                self.__objects = load(f)
        except FileNotFoundError:
            pass
