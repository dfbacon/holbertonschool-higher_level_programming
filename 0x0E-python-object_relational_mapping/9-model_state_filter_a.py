#!/usr/bin/python3
"""
This is the '9-model_state_filter_a' module.
9-model_filter_a uses SQLalchemy to find all states containing the letter 'a'
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
    for instance in session.query(State).order_by(State.id).filter(
            State.name.like('%a%')):
        print("{}: {}".format(instance.id, instance.name))
