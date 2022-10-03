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
from models.city import City


class TestFileStorageDocs(unittest.TestCase):
    '''Tests for documentation of class'''

    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.city_funcs = inspect.getmembers(City, inspect.isfunction)

    def test_conformance_class(self):
        """Test that we conform to Pycodestyle."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/city.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_conformance_test(self):
        """Test that we conform to Pycodestyle."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.\
            check_files(['tests/test_models/test_city.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_docstr(self):
        """ Tests for docstring"""
        self.assertTrue(len(City.__doc__) >= 1)

    def test_class_docstr(self):
        """ Tests for docstring"""
        self.assertTrue(len(City.__doc__) >= 1)

    def test_func_docstr(self):
        """Tests for docstrings in all functions"""
        for func in self.city_funcs:
            self.assertTrue(len(func[1].__doc__) >= 1)


class TestState(unittest.TestCase):

    def test_is_subclass(self):
        self.assertTrue(issubclass(City().__class__, BaseModel), True)

    def test_attr_str(self):
        self.assertEqual(type(City().name), str)
        self.assertEqual(type(City().state_id), str)

    def test_has_attributes_in_to_dict(self):
        """check if attr is in to_dict"""
        melbourne = City()
        melbourne.name = "Melbourne"
        melbourne.state_id = "vic"
        self.assertTrue('id' in melbourne.to_dict())
        self.assertTrue('created_at' in melbourne.to_dict())
        self.assertTrue('updated_at' in melbourne.to_dict())
        self.assertTrue('name' in melbourne.to_dict())
        self.assertTrue('state_id' in melbourne.to_dict())

    def test_save(self):
        melbourne = City()
        melbourne.name = "Melbourne"
        melbourne.save()
        self.assertNotEqual(melbourne.created_at, melbourne.updated_at)

    def test_to_dict(self):
        melbourne = City()
        self.assertTrue(dict, type(melbourne.to_dict))
        self.assertEqual('to_dict' in dir(melbourne), True)


if __name__ == "__main__":
    unittest.main()
