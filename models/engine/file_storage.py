#!/usr/bin/python3
""" `FileStorage` class used for
serialization and deserialization
"""
import json
import os
from models.base_model import BaseModel
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User
from models.state import State


objs = {"BaseModel": BaseModel,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review,
        "User": User,
        "State": State,
        }


class FileStorage():
    """ file storage engine module
    """
    __file_path = "file.json"
    __objects = dict()

    def all(self):
        """returns the `__objects` class variable
        """
        return FileStorage.__objects

    def new(self, obj):
        """  sets in __objects the obj with key <obj class name>.id
        """
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """Serialization of objects to JSON
        """
        output = dict()
        for k, v in FileStorage.__objects.items():
            output[k] = v.to_dict()

        with open(FileStorage.__file_path, mode="w", encoding="utf-8") as f:
            json.dump(output, f)

    def reload(self):
        """Deserialization from JSON to objects
        """
        if os.path.exists(FileStorage.__file_path) is False:
            return

        with open(FileStorage.__file_path, mode="r", encoding="utf-8") as f:
            json_objs = json.load(f)

        for k in json_objs:
            inst = objs[json_objs[k]["__class__"]]
            self.__objects[k] = inst(**(json_objs[k]))
