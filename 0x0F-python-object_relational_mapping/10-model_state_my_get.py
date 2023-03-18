#!/usr/bin/python3
"""prints the state oject with the name passed as argument from the db"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(State).filter(State.name == sys.argv[4]).all()
    if result == []:
        print("Not found")
    else:
        [print(row.id) for row in result]
    session.close()
