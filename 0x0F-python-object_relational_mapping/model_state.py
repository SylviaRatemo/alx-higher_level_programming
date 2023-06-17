#!/usr/bin/python3
"""State class definition"""


import sys
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()


class State(Base):
    """State class inherits from Base"""

    table = 'states'
    id = Column(Integer, primary_keys=True, autoincrement=True)
    name = Column(String(128), nullable=False)


if __name__ == "___main__":
    engine = create_engine('mysql+mysqldb : //{} : {}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
