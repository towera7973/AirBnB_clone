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
        """
        serializes or converts the dictonary data __objects to the JSON file (path: __file_path)
        """
        with open(FileStorage.__file_path, 'w') as f:
            json.dump({key_index: value.to_dict() for key_index, value in FileStorage.__objects.items()}, f)

    def reload(self):
        """
        deserializes the JSON file to __objects only if the JSON
        file exists; otherwise, does nothing
        """
        All_classes = {'BaseModel': BaseModel, 'User': User,
                           'Amenity': Amenity, 'City': City, 'State': State,
                           'Place': Place, 'Review': Review}

        if not os.path.exists(FileStorage.__file_path):
            return

        with open(FileStorage.__file_path, 'r') as f:
            From_Json = None

            try:
                From_Json = json.load(f)
            except json.JSONDecodeError:
                pass

            if From_Json is None:
                return

            FileStorage.__objects = {
                i: All_classes[i.split('.')[0]](**j)
                for i, j in From_Json.items()}
