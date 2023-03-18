#!/usr/bin/python3
"""deletes all state objects with a name containing letter 'a' from the db"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    new_states = session.query(State).filter(State.name.like('%a%')).all()
    [session.delete(state) for state in new_states]
    session.commit()
    session.close()
