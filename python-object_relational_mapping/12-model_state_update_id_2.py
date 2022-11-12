#!/usr/bin/python3
"""
Change the name of the State where id = 2 to New Mexico in hbtn_0e_0_usa.
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

    """modify state"""
    query = session.query(State)
    try:
        state = query.filter(State.id == 2)[0]
        state.name = "New Mexico"
    except IndexError:
        print("Not found")
    session.commit()


if __name__ == '__main__':
    main()
