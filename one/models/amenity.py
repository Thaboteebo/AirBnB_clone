#!/usr/bin/python3
"""This module create a Amenity class"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Class for managing ameity objects"""
    name = ''

    def __init__(self, args, **kwargs):
        """Initializes attributes for the Anemity class"""
        super().__init__(*args, **kwargs)
