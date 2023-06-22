#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls is not None:
            new_storage = {}
            for obj_key, objects in FileStorage.__objects.items():
                if objects.__class__ == cls:
                    new_storage[obj_key] = objects
                if objects.__class__.__name__ == cls:
                    new_storage[obj_key] = objects
            return new_storage

        return (FileStorage.__objects)

    def new(self, obj):
        """Adds new object to storage dictionary"""
        FileStorage.__objects.update({obj.to_dict()
            ['__class__'] + '.' + obj.id: obj})
        self.save()

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            for key, val in FileStorage.__objects.items():
                temp[key] = val.to_dict()
            f.write(json.dumps(temp))

    def reload(self):
        """Loads storage dictionary from file"""
        classes = {
                "BaseModel": BaseModel, "User": User, "State": State,
                "Place": Place, "City": City, "Amenity": Amenity,
                "Review": Review
                }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.loads(f.read())
                for key, val in temp.items():
                    obj = val['__class__']
                    eval(obj)(**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """
        Method deletes object from
        __objects, if it exists.
        """
        if obj is not None:
            obj_key = obj.__class__.__name__ + '.' + obj.id

            if obj_key in self.__objects:
                del self.__objects[obj_key]
                self.save()

    def close(self):
        """
        Method reload called.
        """
        self.reload()
