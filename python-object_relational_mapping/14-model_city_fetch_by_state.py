#!/usr/bin/python3
"""
lists all cities from the database hbtn_0e_0_usa.
arguments:
    mysql username (string)
    mysql password (string)
    database name (string)
"""


from model_state import Base, State
from model_city import Base, City

from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

import sys


def main():
    """ Does the entire script when not imported """

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    """create engine that will use our database"""
    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost/{database}",
        pool_pre_ping=True)
    Base.metadata.create_all(engine)

    """ create session object"""
    Session = sessionmaker()

    """ use Session """
    session = Session(bind=engine)

    """print cities"""
    for city in session.query(City).order_by(City.id):
        query = session.query(State)
        state = query.filter(State.id == city.state_id)[0]
        print(state.name, end="")
        print(f": ({city.id}): {city.name}")


if __name__ == '__main__':
    main()
