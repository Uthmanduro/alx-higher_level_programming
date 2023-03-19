#!/usr/bin/python3
"""Contains the class definition of a city"""


from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from model_state import Base, State
from sqlalchemy.orm import relationship
import sys


class City(Base):
    __tablename__ = 'cities'

    id = Column(Integer, nullable=False, autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    state = relationship('State', backref='cities')
