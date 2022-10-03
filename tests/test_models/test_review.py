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
from models.review import Review


class TestFileStorageDocs(unittest.TestCase):
    '''Tests for documentation of class'''

    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.review_funcs = inspect.getmembers(Review, inspect.isfunction)

    def test_conformance_class(self):
        """Test that we conform to Pycodestyle."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/review.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_conformance_test(self):
        """Test that we conform to Pycodestyle."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.\
            check_files(['tests/test_models/test_review.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_docstr(self):
        """ Tests for docstring"""
        self.assertTrue(len(Review.__doc__) >= 1)

    def test_class_docstr(self):
        """ Tests for docstring"""
        self.assertTrue(len(Review.__doc__) >= 1)

    def test_func_docstr(self):
        """Tests for docstrings in all functions"""
        for func in self.review_funcs:
            self.assertTrue(len(func[1].__doc__) >= 1)


class TestState(unittest.TestCase):

    def test_is_subclass(self):
        self.assertTrue(issubclass(Review().__class__, BaseModel), True)

    def test_attr_str(self):
        self.assertEqual(type(Review().place_id), str)
        self.assertEqual(type(Review().user_id), str)
        self.assertEqual(type(Review().text), str)

    def test_has_attributes_in_to_dict(self):
        """check if attr is in to_dict"""
        review = Review()
        review.place_id = "melb"
        review.user_id = "jacq"
        review.text = "hello"
        self.assertTrue('id' in review.to_dict())
        self.assertTrue('created_at' in review.to_dict())
        self.assertTrue('updated_at' in review.to_dict())
        self.assertTrue('place_id' in review.to_dict())
        self.assertTrue('user_id' in review.to_dict())
        self.assertTrue('text' in review.to_dict())

    def test_save(self):
        review = Review()
        review.save()
        self.assertNotEqual(review.created_at, review.updated_at)

    def test_to_dict(self):
        review = Review()
        self.assertTrue(dict, type(review.to_dict))
        self.assertEqual('to_dict' in dir(review), True)


if __name__ == "__main__":
    unittest.main()
