#!/usr/bin/python3
"""Defines the BaseModel class."""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Represents the BaseModel of the AirBnB project."""

    def __init__(self, *args, **kwargs):
        """constructor that Initialize a new BaseModel.
        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        string_T_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for i, j in kwargs.items():
                if i == "created_at" or i == "updated_at":
                    self.__dict__[i] = datetime.strptime(j, string_T_format)
                else:
                    self.__dict__[i] = j
        else:
            models.storage.new(self)

    def save(self):
        """This method updates the updated_at attribute with the current date and time.
        It then calls models.storage.save(), which presumably saves the current state of the object 
        to some form of persistent storage (like a database)."""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Return the dictionary of the BaseModel instance.
        Includes the key/value pair and __class__ representing the class name of the object.
        """
        Storage_dict = self.__dict__.copy()
        Storage_dict["created_at"] = self.created_at.isoformat()
        Storage_dict["updated_at"] = self.updated_at.isoformat()
        Storage_dict["__class__"] = self.__class__.__name__
        return Storage_dict

    def __str__(self):
        """Return the print/str representation of the BaseModel instance."""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
