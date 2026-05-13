#!/usr/bin/python3
"""State model"""

from sqlalchemy import Column, Integer, String
from base import Base


class State(Base):
    """State class"""

    __tablename__ = "states"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)

