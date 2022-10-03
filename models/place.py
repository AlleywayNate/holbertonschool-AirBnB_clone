#!/usr/bin/python3
from models.base_model import BaseModel
""" Module for class Place """


class Place(BaseModel):
    """
    Class Place that imports from BaseModel
    Attributes:
    city_id: string - City id
    user_id: string - User id
    name: name of Place
    description: description of Place
    number_rooms: number of rooms in Place
    number_bathrooms: number of bathrooms in Place
    max_guest: maximum number of guests in Place
    price_by_night: price by night of Place
    latitude: latitude of Place
    longitude: longitude of Place
    amenity_ids: Amenity id
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
