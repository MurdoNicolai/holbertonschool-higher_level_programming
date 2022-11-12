#!/usr/bin/python3
"""Creates the State class"""

from model_state import Base, State
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class City(Base):
    """
    Contains class definition of table states:

    id (int): the id of the state
    name (str): the name of the state
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    state_id = Column(Integer, ForeignKey('states.id'))
    name = Column(String(128))

    state = relationship("State", back_populates="cities")

State.cities = relationship(
    "City", order_by=City.id, back_populates="state")
