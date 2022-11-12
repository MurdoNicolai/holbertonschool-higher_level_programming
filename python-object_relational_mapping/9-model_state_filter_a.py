#!/usr/bin/python3
"""
lists states containing a from the database hbtn_0e_0_usa.
arguments:
    mysql username (string)
    mysql password (string)
    database name (string)
"""


from model_state import Base, State

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

    """use query to do stuff involving selecting specific states"""
    query = session.query(State).order_by(State.id)
    for state in query.filter(State.name.like('%a%')):
        print(f"{state.id}: {state.name}")


if __name__ == '__main__':
    main()
