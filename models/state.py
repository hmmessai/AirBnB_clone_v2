#!/usr/bin/python3
"""
Module maps class State to
a Database Table.
"""
from os import getenv
import models
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """
    Creates Table 'states' with
    one Column for storing name.
    """
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)

    if getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship("City", backref="state",
                              cascade='all, delete')

    else:
        @property
        def cities(self):
            """
            Method returns city
            instances.
            """
            all_cities = models.storage.all(City).values()
            city_states = []

            for city_item in all_cities:
                if city.state_id == self.id
                city_states.append(city_item)
            return city_states
