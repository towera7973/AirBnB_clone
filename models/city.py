#!/usr/bin/python3
"""The City class WHICH is a module ."""
from models.base_model import BaseModel


class City(BaseModel):
    """Represent a city on the application 

    Attributes:
        state_id (str): The state id.
        name (str): The name of the city.
    """

    state_id = ""
    name = ""
