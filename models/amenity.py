#!/usr/bin/python3
"""The `amenity` module
It defines one class, `Amenity(),sub-class of  `BaseModel()` class.`
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """An amenity provided by a place/house. e,g river ,games etc 

    Attributes:
        name
    """

    name = ""
