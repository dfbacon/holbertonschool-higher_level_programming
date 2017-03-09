#!/usr/bin/python3
"""
This is model_city module.
model_city defines one class 'City' and an instance Base = declarative_base()
"""


from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy as sq

Base = declarative_base()


class City(Base):
    __tablename__ = "cities"
    id = sq.Column(sq.Integer, primary_key=True, nullable=False)
    name = sq.Column(sq.String(128), nullable=False)
    state_id = sq.Column(sq.Integer, sq.ForeignKey('states.id'),
                         nullable=False)

    def __str__(self):
        return "{}: {}".format(self.id, self.name)

    def __repr__(self):
        return "City(name={}, id={}), state_id={}".format(
            self.name, self.id, self.state_id)
