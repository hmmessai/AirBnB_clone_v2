#!/usr/bin/python3
"""
Module maps class User
to a Database Table.
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """
    Creates Table 'users' with
    four Columns for storing
    email, password, first_name
    and last_name.
    """
    __tablename__ = 'users'

    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    places = relationship("Place", cascade='all, delete', backref="user")
    reviews = relationship("Review", cascade='all, delete', backref="user")
