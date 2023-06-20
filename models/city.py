#!/usr/bin/python3
"""
Module maps class City
to a Database Table.
"""
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """
    Creates Table 'cities' with
    two Columns for storing name,
    and reference to State table.
    """
    __tablename__ = 'cities'

    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    places = relationship("Place", cascade='all, delete', backref="cities")
