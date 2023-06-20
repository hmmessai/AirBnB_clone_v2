#!/usr/bin/python3
"""
Module maps class Amenity
to a Database Table.
"""
import models
from models.base_model import BaseModel, Base
from models.place import Place, place_amenity
from sqlalchemy import Column, String
from sqlalchemy.ord import relationship


class Amenity(BaseModel, Base):
    """
    Creates Table with one
    column for storing name.
    """
    __tablename__ = "amenities"

    name = Column(String(128), nullable=False)
    place_amenities = relationship(
        "Place", secondary=place_amenity,
        viewonly=False)
