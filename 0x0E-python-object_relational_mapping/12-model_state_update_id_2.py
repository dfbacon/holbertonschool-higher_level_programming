#!/usr/bin/python3
"""
This is the '12-model_state_update_id_2' module.
12-model_state_update_id_2 uses SQLalchemy to alter the name of a given
State object.
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
    query = session.query(State).filter_by(id=2).first()
    query.name = "New Mexico"
    session.commit()
    session.close()
    eng.dispose()
