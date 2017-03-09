#!/usr/bin/python3
"""
This is the '10-model_state_my_get' module.
10-model_state_my_get uses SQLalchemy to find all states containing
the letter  'a'
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
    found = 0
    if ';' not in argv[4]:
        for instance in session.query(State).order_by(State.id).filter(
                State.name == argv[4]):
            print("{}".format(instance.id))
            if found == 0:
                found = 1
        if found == 0:
            print("Not found")
