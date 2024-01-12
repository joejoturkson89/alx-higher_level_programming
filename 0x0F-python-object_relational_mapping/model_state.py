#!/usr/bin/python3
"""
Defines a state model.
Inherit from SQLALchemy Base and links to the MySQL table state.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """Represents a state for a MySQl db.
    __tablename__(str): the name of the MySQl table to store states.
    id (sqlalchemy.integer): the state's id.
    name (sqlalchemy.string): the state's name.
    """

    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
