#!/usr/bin/python3
"""
State model
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from base import Base


class State(Base):
    """
    class
    """
    __tablename__ = "states"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)

    cities = relationship("City", back_populates="state", cascade="all, delete")
