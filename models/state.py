#!/usr/bin/python3
"""The `state` module

It defines one class, `State(),from  the `BaseModel()` class.`
"""
from models.base_model import BaseModel


class State(BaseModel):
    """A state in the application.

    Attributes:
        name
    """
    name = ""
