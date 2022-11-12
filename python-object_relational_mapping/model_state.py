#!/usr/bin/python3
"""Creates the State class"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


"""create a Base class so that our class can have it's attributes"""
Base = declarative_base()


class State(Base):
    """
    Contains class definition of table states:

    id (int): the id of the state
    name (str): the name of the state
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128))
