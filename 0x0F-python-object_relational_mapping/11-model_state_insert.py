#!/usr/bin/python3
"""adds the state object "Louisiana" tot the database"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == '__main__':
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
        sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    new_state = session.query(State).filter(State.id == 6).first()
    if new_state is None:
        new_state = State(id=6, name="Louisiana")
        session.add(new_state)
        session.commit()
    new_id = session.query(State).filter(State.name == "Louisiana").first()
    print(new_id.id)
    session.close()
