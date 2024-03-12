#!/usr/bin/python3
"""Defines the BaseModel class."""
import models
from uuid import uuid4
from datetime import datetime

class BaseModel:
    """Represents the BaseModel of the AirBnB project."""
    def __init__(self, *args, **kwargs):
        """
        instatiates an object with it's
        attributes
        """
        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key == "created_at" or key == "updated_at":
                    value = datetime.fromisoformat(value)
                setattr(self, key, value)
            return

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        models.storage.new(self)

    def save(self):
        """ method updates the updated_at attribute with the current date and time.
        which presumably saves the current state of the object to some form of storage ."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Return the dictionary of the BaseModel instance.
        Includes the key/value pair and __class__ representing the class name of the object.
        with dates when the BaseModel was created and then later update
        here the __class__ ,created_at and updated_at are keys e.g __class__: mymodel
        """
        inst_dict = self.__dict__.copy()
        '''we are making a copy of dictionary representation of any instanca of a class that holds attributese'''
        inst_dict["__class__"] = self.__class__.__name__
        inst_dict["created_at"] = self.created_at.isoformat()
        inst_dict["updated_at"] = self.updated_at.isoformat()
        return inst_dict

    def __str__(self):
        """Return the print/str representation of the BaseModel instance.
            this should return the name of the class (instance ) ,then id of class 
            then the __dict__ created above 
        """
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
