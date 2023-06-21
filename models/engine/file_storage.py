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
        """serializes __objects to the JSON file"""
        json_obj = {}
        for key in self.__objects:
            json_obj[key] = self.__objects[key].to_dict()

        with open(self.__file_path, 'w', encoding='utf-8') as f:
            json.dump(json_obj, f)

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
                "BaseModel": BaseModel, "User": User, "State": State,
                "Place": Place, "City": City, "Amenity": Amenity,
                "Review": Review
                }

        deserialized = {}
        try:
            with open(self.__file_path, 'r', encoding="utf-8") as f:
                deserialized = json.load(f)
                for x in deserialized.values():
                    name = x["__class__"]
                    del x["__class__"]
                    self.new(eval(name)(**x))
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
