#!/usr/bin/python3
'''
    Implementation of the State class
'''
import os
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base


class State(BaseModel, Base):
    '''
        Implementation for the State.
        Create relationship between class State (parent) to City (child)
    '''
    if os.environ.get("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state",
                              cascade="all, delete, delete-orphan")
    else:
        name = ""

    if os.environ.get("HBNB_TYPE_STORAGE") == "fs":
        @property
        def cities:
            '''
                Return list of city instances if City.state_id==current State.id
                FileStorage relationship between State and City
            '''
            list_cities = []
            for city in models.storage.all(City).values():
                if city.state_id == self.id:
                    list_cities.append(city)
            return list_cities
