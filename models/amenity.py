#!/usr/bin/python3
"""
Module maps class Amenity
to a Database Table.
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """
    Creates Table with one
    column for storing name.
    """
    __tablename__ = "amenities"

    name = Column(String(128), nullable=False)
    place_amenities = relationship(
        "Place", secondary="place_amenity",
        viewonly=False)
