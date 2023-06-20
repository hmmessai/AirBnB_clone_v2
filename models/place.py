#!/usr/bin/python3
"""
Module maps class Place
to a Database Table.
"""
from os import getenv
import models
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from models.review import Review
from sqlalchemy import Table, Column, String
from sqlalchemy import Integer, Float, ForeignKey
from sqlalchemy.orm import relationship


place_amenity = Table("place_amenity", Base.metadata,
                      Column("place_id", String(60),
                             ForeignKey("places.id"),
                             primary_key=True, nullable=False),
                      Column("amenity_id", String(60),
                             ForeignKey("amenities.id"),
                             primary_key=True, nullable=False,)
                      )


class Place(BaseModel, Base):
    """
    Creates Table 'places' with
    eleven columns for storing
    ids, name, description, number
    of rooms + bathrooms, maximum
    guests, price, and location.
    """
    __tablename__ = 'places'

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    if getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship("Review", cascade='all, delete',
                               backref="place")
        amenities = relationship("Amenity", secondary=place_amenity,
                                 viewonly=False)

    else:
        @property
        def reviews(self):
            """Method returns reviews
            for an AirBnB, if any.
            """
            place_review = []
            all_reviews = models.storage.all(Review).values()

            for review_item in all_review:
                if review.place_id == self.id:
                    place_review.append(review_item)
            return place_review

        @property
        def amenities(self):
            """Method returns amenities
            linked to an AirBnB, if any.
            """
            place_amenity = []
            all_amenities = models.storage.all(Amenity).values()

            for amenity_item in all_amenities:
                if amenity.id in self.amenity_ids:
                    place_amenity.append(amenity_item)
            return place_amenity

        @amenities.setter
        def amenities(self, amenity_obj):
            """
            Method appends ids of amenities linked
            to an AirBnB, into amenities_id.
            """
            if type(amenity_obj) == Amenity:
                self.amenity_ids.append(amenity_obj.id)
