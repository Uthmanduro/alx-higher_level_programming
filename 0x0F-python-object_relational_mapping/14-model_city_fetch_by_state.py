#!/usr/bin/python3
"""prints all city objects from the database"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    new_cities = session.query(City).order_by(asc(city.id))all()
    for city in new_cities:
        print(f'{city.state.name}: ({city.id}) {city.name}')
