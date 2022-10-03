#!/usr/bin/python3
"""
Unittest to test state class
"""
import unittest
import inspect
import json
import os
import pycodestyle
from models.base_model import BaseModel
from models.state import State


class TestFileStorageDocs(unittest.TestCase):
    '''Tests for documentation of class'''

    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.state_funcs = inspect.getmembers(State, inspect.isfunction)

    def test_conformance_class(self):
        """Test that we conform to Pycodestyle."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/state.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_conformance_test(self):
        """Test that we conform to Pycodestyle."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.\
            check_files(['tests/test_models/test_state.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_docstr(self):
        """ Tests for docstring"""
        self.assertTrue(len(State.__doc__) >= 1)

    def test_class_docstr(self):
        """ Tests for docstring"""
        self.assertTrue(len(State.__doc__) >= 1)

    def test_func_docstr(self):
        """Tests for docstrings in all functions"""
        for func in self.state_funcs:
            self.assertTrue(len(func[1].__doc__) >= 1)


class TestState(unittest.TestCase):

    def test_is_subclass(self):
        self.assertTrue(issubclass(State().__class__, BaseModel), True)

    def test_attr_str(self):
        self.assertEqual(type(State().name), str)

    def test_has_attributes(self):
        Victoria = State()
        Victoria.name = "Victoria"
        self.assertTrue('id' in Victoria.to_dict())
        self.assertTrue('created_at' in Victoria.to_dict())
        self.assertTrue('updated_at' in Victoria.to_dict())
        self.assertTrue('name' in Victoria.to_dict())

    def test_save(self):
        Victoria = State()
        Victoria.name = "Victoria"
        Victoria.save()
        self.assertNotEqual(Victoria.created_at, Victoria.updated_at)

    def test_to_dict(self):
        Victoria = State()
        self.assertTrue(dict, type(Victoria.to_dict))
        self.assertEqual('to_dict' in dir(Victoria), True)


if __name__ == "__main__":
    unittest.main()
