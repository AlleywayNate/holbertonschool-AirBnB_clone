#!/usr/bin/python3
""" Unit tests for BaseModel """

import unittest
from models.base_model import BaseModel
from datetime import datetime
from time import sleep


class TestBaseModel(unittest.TestCase):
    """ Unit tests for BaseModel """

    def test_instantiate(self):
        """ Happy pass instantiate"""
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_id(self):
        """ Happy pass public id string format """
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at(self):
        """ Happy pass created at datetime """
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at(self):
        """ Happy pass updated at datetime """
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_uid(self):
        """ UID created at each instantiation """
        base1 = BaseModel()
        base2 = BaseModel()
        self.assertNotEqual(base1.id, base2.id)

    def test_instantiate_attrs(self):
        """ Single instantiate and check attributes """
        base1 = BaseModel()
        self.assertEqual(type(base1.id), str)
        self.assertEqual(type(base1.created_at), datetime)
        self.assertEqual(type(base1.updated_at), datetime)

    def test_instantiate_kwargs(self):
        """ Single instantiate with kwargs """
        dt = datetime.today()
        base1 = BaseModel(
            id="123", created_at=dt.isoformat(), updated_at=dt.isoformat()
        )
        self.assertEqual(base1.id, "123")
        self.assertEqual(base1.created_at, dt)
        self.assertEqual(base1.updated_at, dt)

    def test_str(self):
        """ ___str__ method is string """
        base1 = BaseModel()
        self.assertEqual(type(str(base1)), str)

    def test_instantiate_arg(self):
        """ invalid arg when instantiating """
        with self.assertRaises(NameError) as e:
            b1 = BaseModel(hello)
        self.assertEqual(str(e.exception), "name 'hello' is not defined")

    def test_save(self):
        """ save method """
        base1 = BaseModel()
        sleep(2)
        update = base1.updated_at
        base1.save()
        self.assertNotEqual(update, base1.updated_at)

    def test_to_dict(self):
        """ Happy pass to_dict method """
        base1 = BaseModel()
        self.assertTrue(dict, type(base1.to_dict))

    def test_to_dict_add_attr(self):
        """ add attribute to dict """
        base1 = BaseModel()
        base1.city = "LA"
        base1.state = "California"
        self.assertIn("city", base1.to_dict())
        self.assertIn("state", base1.to_dict())

    def test_to_dict_wrong_arg(self):
        """ add an undefined arg """
        base1 = BaseModel()
        with self.assertRaises(NameError):
            base1.to_dict(hello)


if __name__ == "__main__":
    unittest.main()