#!/usr/bin/python3
"""
This is the '11-model_state_insert' module.
11-model_state_insert uses SQLalchemy to add the state 'Louisiana'.
"""


from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    eng = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]))
    Base.metadata.create_all(eng)
    session_maker = sessionmaker(bind=eng)
    session = session_maker()
    session.add(State(name="Louisiana"))
    state_name = session.query(State.id).filter_by(name="Louisiana")
    if state_name:
        for row in state_name:
            print('{}'.format(row[0]))
    else:
        print("Not found")
    session.commit()
    session.close()
    eng.dispose()
