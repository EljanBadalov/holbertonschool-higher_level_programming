#!/usr/bin/python3
"""
14-model_city_fetch_by_state.py
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    usnm = sys.argv[1]
    pwd = sys.argv[2]
    db = sys.argv[3]

    engine = create_engine(
        f"mysql+mysqldb://{usnm}:{pwd}@localhost:3306/{db}"
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    states_cities = (session.query(State, City).
                     join(City, State.id == City.state_id).
                     order_by(City.id).all())

    for state, city in states_cities:
        print('{}: ({}) {}'.format(state.name, city.id, city.name))

    session.close()
