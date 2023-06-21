#!/usr/bin/python3
"""
Module transitions FileStorage
to DBStorage and adds attributes
for SQLAlchemy.
"""
import os
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
import models
from models.base_model import Base, BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.user import User
from models.state import State


class DBStorage():
    """
    Creates Database Storage.
    """
    __engine = None
    __session = None

    def __init__(self):
        """
        Extracts user, passwd, host,
        and database values from env
        variables then creates engine.
        """
        user = os.environ['HBNB_MYSQL_USER']
        password = os.environ['HBNB_MYSQL_PWD']
        host = os.environ['HBNB_MYSQL_HOST']
        database = os.environ['HBNB_MYSQL_DB']

        self.__engine = create_engine(f'mysql+mysqldb://{user}:'
                              f'{password}@{host}:3306/'
                              f'{database}',
                              pool_pre_ping=True)

        if getenv('HBNB_ENV') == 'test':
            """
            Drop all tables for env
            variable 'test'.
            """
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Method returns objects
        and their classes.
        """
        child_classes = {
                "User": User, "State": State, "Place": Place,
                "City": City, "Amenity": Amenity, "Review": Review
                }

        class_objects = {}
        for key in child_classes:
            if cls is key:
                obj_query = self.__session.query(child_classes[key]).all()
            if cls is child_classes[key]:
                obj_query = self.__session.query(child_classes[key]).all()
            if cls is None:
                obj_query = self.__session.query(child_classes[key]).all()
                for value in obj_query:
                    key = value.__class__.__name__ + '.' + value.id
                    class_objects[key] = value

        return class_objects

    def new(self, obj):
        """
        Method adds new object
        to current DB session.
        """
        self.__session.add(obj)

    def save(self):
        """
        Method saves all changes
        made to current DB session.
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        Method object from
        current DB session.
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """
        Method creates all DB tables
        and current database sessions.
        """
        Base.metadata.create_all(self.__engine)

        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """
        Close current active session.
        """
        self.__session.close()
