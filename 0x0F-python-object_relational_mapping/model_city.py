#!/usr/bin/python3
"""Contains the class definition of a city"""


from sqlalchemy import create_engine, Column, Integer, String, Foriegnkey
from model_state import Base, State

class City(Base):
    __tablename__ = 'cities'

    id = Column(Integer, nullable=False, autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, nullable=False, ForeignKey()
