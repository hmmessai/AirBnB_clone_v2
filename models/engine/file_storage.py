#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls is not None:
            new_storage = {}
            for obj_key, objects in self.__objects.items():
                if cls == objects.__class__.__name__:
                    new_storage[obj_key] = objects
            return new_storage

        return self.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        temp = {}
        try:
            with open(self.__file_path, 'r') as f:
                temp = json.load(f)
                for key in temp.values():
                    name = key["__class__"]
                    del key["__class__"]
                    self.new(eval(name)(**key))
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
