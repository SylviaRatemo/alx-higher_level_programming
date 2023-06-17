#!/usr/bin/python3
"""State class definition"""


import sys
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """State class inherits from Base"""

    __table__ = 'states'
    id = Column(Integer, primary_keys=True, autoincrement=True,
                nullable=False, unique=True)
    name = Column(String(128), nullable=False)
