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
from models.amenity import Amenity


class TestFileStorageDocs(unittest.TestCase):
    '''Tests for documentation of class'''

    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.amenity_funcs = inspect.getmembers(Amenity, inspect.isfunction)

    def test_conformance_class(self):
        """Test that we conform to Pycodestyle."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/amenity.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_conformance_test(self):
        """Test that we conform to Pycodestyle."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.\
            check_files(['tests/test_models/test_amenity.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_docstr(self):
        """ Tests for docstring"""
        self.assertTrue(len(Amenity.__doc__) >= 1)

    def test_class_docstr(self):
        """ Tests for docstring"""
        self.assertTrue(len(Amenity.__doc__) >= 1)

    def test_func_docstr(self):
        """Tests for docstrings in all functions"""
        for func in self.amenity_funcs:
            self.assertTrue(len(func[1].__doc__) >= 1)


class TestState(unittest.TestCase):

    def test_is_subclass(self):
        self.assertTrue(issubclass(Amenity().__class__, BaseModel), True)

    def test_attr_str(self):
        self.assertEqual(type(Amenity().name), str)

    def test_has_attributes_in_to_dict(self):
        """check if attr is in to_dict"""
        amenity = Amenity()
        amenity.name = "garden"
        self.assertTrue('id' in amenity.to_dict())
        self.assertTrue('created_at' in amenity.to_dict())
        self.assertTrue('updated_at' in amenity.to_dict())
        self.assertTrue('name' in amenity.to_dict())

    def test_save(self):
        amenity = Amenity()
        amenity.save()
        self.assertNotEqual(amenity.created_at, amenity.updated_at)

    def test_to_dict(self):
        amenity = Amenity()
        self.assertTrue(dict, type(amenity.to_dict))
        self.assertEqual('to_dict' in dir(amenity), True)


if __name__ == "__main__":
    unittest.main()
