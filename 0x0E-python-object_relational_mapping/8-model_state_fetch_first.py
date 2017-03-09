#!/usr/bin/python3
"""
This is the '8-model_state_fetch_first' module.

8-model_state_fetch_first uses SQLalchemy and displays all state
objects from a given database.
"""


import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    eng = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(eng)
    session_maker = sessionmaker(bind=eng)
    session = session_maker()
    instance = session.query(State).first()
    if instance:
        print("{}: {}".format(instance.id, instance.name))
    else:
        print("Nothing")
