#!/usr/bin/python3
"""
Unittest to test FileStorage class
"""
import unittest
import inspect
import json
import os
import pycodestyle
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine import file_storage
FileStorage = file_storage.FileStorage


class TestFileStorageDocs(unittest.TestCase):
    '''Tests for documentation of class'''

    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.file_funcs = inspect.getmembers(FileStorage, inspect.isfunction)

    def test_conformance_class(self):
        """Test that we conform to Pycodestyle."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_conformance_test(self):
        """Test that we conform to Pycodestyle."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.\
            check_files(['tests/test_models/test_engine/test_file_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_docstr(self):
        """ Tests for docstring"""
        self.assertTrue(len(FileStorage.__doc__) >= 1)

    def test_class_docstr(self):
        """ Tests for docstring"""
        self.assertTrue(len(FileStorage.__doc__) >= 1)

    def test_func_docstr(self):
        """Tests for docstrings in all functions"""
        for func in self.file_funcs:
            self.assertTrue(len(func[1].__doc__) >= 1)


class TestFileStorage(unittest.TestCase):
    '''testing file storage'''

    def test_all(self):
        """check if returns dic<class>.<id> : {obj instance}"""
        storage = FileStorage()
        all_objs = storage.all()
        self.assertIsNotNone(all_objs)
        self.assertEqual(dict, type(all_objs))
        self.assertIs(all_objs, storage._FileStorage__objects)

    def test_new(self):
        """check if it has created new object"""
        storage = FileStorage()
        all_objs = storage.all()
        jacqueline = User()
        jacqueline.id = 00000
        jacqueline.first_name = "Jacqueline"
        jacqueline.last_name = "lu"
        storage.new(jacqueline)
        key = jacqueline.__class__.__name__ + "." + str(jacqueline.id)
        self.assertIsNotNone(all_objs[key])

    def test_save(self):
        storage = FileStorage()
        storage.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_reload(self):
        storage1 = FileStorage()
        all_objs = storage1.all()
        for obj_id in all_objs.keys():
            obj = all_objs[obj_id]
        print(obj)
        self.assertIsNotNone(obj)

    def test_create(self):
        """ happy pass instance creation """
        all_objs = FileStorage()
        self.assertTrue(type(all_objs) == FileStorage)
        self.assertTrue(isinstance(all_objs, FileStorage))

    def test_new(self):
        """ happy pass new method """
        all_objs = FileStorage()
        all_objs.new(BaseModel())
        self.assertTrue(all_objs.all())

    def test_new_arg(self):
        """ new method - pass an argument """
        all_objs = FileStorage()
        with self.assertRaises(AttributeError):
            all_objs.new(123)

    def test_save_arg(self):
        """ save method - pass an argument """
        all_objs = FileStorage()
        with self.assertRaises(TypeError):
            all_objs.save(123)

    def test_reload_arg(self):
        """ reload method - pass an argument """
        all_objs = FileStorage()
        with self.assertRaises(TypeError):
            all_objs.reload(123)


if __name__ == "__main__":
    unittest.main()
