#!/usr/bin/python3
"""contains the class definition of a state and an instance Base"""


from sqlalchemy import create_engine, Table, Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """inherits from base and links to the mysql table 'states'"""

    __tablename__ = 'states'
    id = Column(Integer, nullable=False, autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state', cascade='all, delete,\
                          save-update, merge')
