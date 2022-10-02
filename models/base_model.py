#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """
    Base class
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize an instance of BaseModel
        """
        if kwargs:
            attr = kwargs
            if 'id' not in attr:
                attr['id'] = str(uuid4())
            if 'created_at' not in attr:
                attr['created_at'] = datetime.now()
            elif not isinstance(attr['created_at'], datetime):
                attr['created_at'] = datetime.strptime(
                    attr['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
            if 'updated_at' not in attr:
                attr['updated_at'] = datetime.now()
            elif not isinstance(attr['updated_at'], datetime):
                attr['updated_at'] = datetime.strptime(
                    attr['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')
            attr.pop('__class__', None)
            for key, value in attr.items():
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            # models.storage.new(self)

    def __str__(self):
        """
        Return a string representation of BaseModel
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates the updated_at public instance attribute with the current
        datetime
        """
        self.updated_at = datetime.now()
        # models.storage.save()

    def to_dict(self):
        """
        Return a dictionary containing all key/values of __dict__
        """
        dic = {}
        dic["__class__"] = self.__class__.__name__
        for k, v in self.__dict__.items():
            if isinstance(v, datetime):
                dic[k] = v.isoformat()
            else:
                dic[k] = v
        return dic
