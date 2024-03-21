#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship('City', cascade="all, delete", backref="state")

    def cities(self):
        """  """
        Cities = models.storage.all("City").values()
        List = []
        for city in Cities:
            if city.state_id == self.id:
                List.append(city)
        return List
