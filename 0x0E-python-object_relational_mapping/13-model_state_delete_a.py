#!/usr/bin/python3
"""
This is the '13-model_state_delete' module.
13-model_state_delete uses SQLalchemy to delete State objects that
contain the letter 'a'.
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
    for instance in session.query(State).order_by(State.id).filter(
            State.name.like('%a%')):
        session.delete(instance)
    session.commit()
    session.close()
    eng.dispose()
