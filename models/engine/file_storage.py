#!/usr/bin/python3
"""
Module: file_storage.py ,this is the name of tis fie 

Defines a `FileStorage` class.
"""
import os
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.review import Review
from models.amenity import Amenity
from models.place import Place

class FileStorage():
    """
    this class serializes instances to a JSON file called file.json which is in__ file_path 
    and  deserializes JSON file to instances called __objects 
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        returns the dictionary of object/instances called  __objects as seen above 
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        if an instance is new this methid put the instance name 
        in dictonary  __objects the obj with key <obj class name>.id e.g myobject.123
        """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        """ eg an  obj of class MyClass with an id of 123 (obj=myclass.123) 
        is assigned to the key 'MyClass.123' in the dictionary FileStorage.__objects. bellow"""
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""

        ''' create empty dictionary'''
        json_object = {}
        """ fill dictionary with elements __objects """
        for key in self.__objects:
            json_object[key] = self.__objects[key].to_dict()

        with open(self.__file_path, 'w', encoding ="utf-8") as f:
            json.dump(json_object, f)

    def reload(self):
        """ deserializes the JSON file to __objects """
        try:
            with open(self.__file_path, 'r', encoding="utf-8") as f:
                # jlo = json.load(f)
                for key, value in json.load(f).items():
                    attri_value = eval(value["__class__"])(**value)
                    self.__objects[key] = attri_value
        except FileNotFoundError:
            pass
