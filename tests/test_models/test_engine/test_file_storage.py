#!/usr/bin/env python3
"""
a module that tests
"""
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from os import rename, remove
from json import load, dump


class Test_file_storage(unittest.TestCase):
    """
    a class for testing the FileStorage class
    inheritting from the TestCase class
    """

    def test_FileStorage_constructor(self):
        """
        tests the FileStorage class constructor
        """
        self.assertEqual(FileStorage, type(FileStorage()))

    def test_constructor_with_args(self):
        """
        tests the constructor of the FileStorage class
        when some arguments are passed to it
        """
        with self.assertRaises(TypeError):
            x = FileStorage(None)


class Test_all(unittest.TestCase):
    """
    a class that tests the .all() method
    """

    def test_all_method(self):
        """
        tests the .all() method return type
        """
        self.assertEqual(dict, type(FileStorage().all()))

    def test_all_method_with_args(self):
        """
        tests .all() with args
        """
        with self.assertRaises(TypeError):
            FileStorage().all(None)


class Test_new(unittest.TestCase):
    """
    a class for testing .new() method
    """

    def test_new_with_correct_args(self):
        """
        tests the .new() method with the correct type and
        number of args
        """
        x = BaseModel()
        y = FileStorage()
        y.new(x)
        self.assertIn(x.to_dict(), y.all().values())

    def test_new_with_wrong_args_num(self):
        """
        tests .new() with more args than needed
        """
        x = BaseModel()
        y = User()
        z = FileStorage()
        with self.assertRaises(TypeError):
            z.new(x, y)

    def test_new_with_wrong_args_val(self):
        """
        tests .nwe() with arguments of an incorrect nature
        """
        x = {'a': 1, 'b': 2}
        y = FileStorage()
        with self.assertRaises(AttributeError):
            y.new(x)

    def test_new_with_no_args(self):
        """
        tests .new() with more args than needed
        """
        z = FileStorage()
        with self.assertRaises(TypeError):
            z.new()

    def test_new_operation_key(self):
        """
        tests if .new() saves the new key correctly
        """
        x = City()
        y = FileStorage()
        y.new(x)
        self.assertIn(f"{x.__class__.__name__}.{x.id}", y.all().keys())

    def test_new_operation_value(self):
        """
        tests if .new() saves the new value correctly
        """
        x = City()
        y = FileStorage()
        y.new(x)
        self.assertIn(x.to_dict(), y.all().values())


class Test_save_file_storage(unittest.TestCase):
    """
    tests the .save() method of FileStorage class
    """

    @classmethod
    def setUp(self):
        try:
            rename("file.json", "temp")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            remove("file.json")
        except IOError:
            pass

        try:
            rename("temp", "file.json")
        except IOError:
            pass

    def test_save_with_arg(self):
        """
        tests .save() with args given
        """
        with self.assertRaises(TypeError):
            FileStorage().save(None)

    def test_save_correctly(self):
        """
        tests the correct save process
        """
        x = Place()
        y = FileStorage()
        y.new(x)
        y.save()
        with open("file.json", 'r', encoding="utf-8") as f:
            z = load(f)
            self.assertEqual(y.all(), z)

    def test_empty_save(self):
        """
        tests saving an empty dictionary
        """
        x = FileStorage()
        x.save()
        with open("file.json", 'r', encoding="utf-8") as f:
            z = load(f)
            self.assertEqual(x.all(), z)

    def test_double_save(self):
        """
        tests that saving more than once doesn't
        lose data
        """
        x = State()
        y = FileStorage()
        y.new(x)
        y.save()
        z = Review()
        y.new(z)
        y.save()
        with open("file.json", 'r', encoding="utf-8") as f:
            a = load(f)
            self.assertIn(x.to_dict(), a.values())
            self.assertIn(z.to_dict(), a.values())


class Test_reload_FileStorage(unittest.TestCase):
    """
    tests the .reload() method of the FileStorage class
    """

    @classmethod
    def setUp(self):
        try:
            rename("file.json", "temp")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            remove("file.json")
        except IOError:
            pass
        try:
            rename("temp", "file.json")
        except IOError:
            pass

    def test_reload_with_args(self):
        """
        tests the reload with given args
        """
        x = FileStorage()
        with self.assertRaises(TypeError):
            x.reload(None)

    def test_reload_without_args(self):
        """
        tests a correct .reload() process
        """
        x = Amenity()
        y = FileStorage()
        y.new(x)
        y.save()
        y.reload()
        self.assertIn(x.to_dict(), y.all().values())

    def test_double_reload(self):
        """
        tests that double reloading doesn't lose data
        """
        x = State()
        y = FileStorage()
        y.new(x)
        y.save()
        y.reload()
        z = Review()
        y.new(z)
        y.save()
        y.reload()
        self.assertIn(x.to_dict(), y.all().values())
        self.assertIn(z.to_dict(), y.all().values())
