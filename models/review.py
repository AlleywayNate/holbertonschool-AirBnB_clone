#!/usr/bin/python3
"""
Module Review class
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    place_id:empty string
    user_id: empty string
    text: empty string
    """
    place_id = ""
    user_id = ""
    text = ""
