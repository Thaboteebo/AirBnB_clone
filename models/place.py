#!/usr/bin/pyhton3
"""This module crteates a Place class"""

from models.base_model import BaseModel

class Place(baseModel):
    """Class for managing place objects"""

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longititude = 0.0
    amenity_ids = []
