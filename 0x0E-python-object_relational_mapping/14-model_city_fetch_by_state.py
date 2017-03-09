#!/usr/bin/python3
"""
This is the '14-model_city_fetch_by_state' module.
14-model_city_fetch_by_state imports from model_city and contains
the class definition of 'City'.
"""


from sys import argv
from model_state import Base, State
from model_city import cities
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    eng = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]))
    Base.metadata.create_all(eng)
    session_maker = sessionmaker(bind=eng)
    session = session_maker()
    for instance in session.query(State.name, cities.id, cities.name).filter(
            State.id == cities.state_id).order_by(cities.id):
        print("{}: ({}) {}".format(instance[0], instance[1], instance[2]))
    session.close()
    eng.dispose()
