#!/usr/bin/python3
"""Contains the class definition of a city"""


from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from relationship_state import Base, State
from sqlalchemy.orm import relationship
import sys


class City(Base):
    """inheirts from cities and links to the mysql table cities"""
    __tablename__ = 'cities'

    id = Column(Integer, nullable=False, autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
