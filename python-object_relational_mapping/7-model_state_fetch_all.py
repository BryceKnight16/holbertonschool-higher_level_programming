#!/usr/bin/python3
"""lists all State objects of the database hbtn_0e_6_usa"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                                                                sys.argv[1],
                                                                sys.argv[2],
                                                                sys.argv[3]),
                           echo=False)
    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(State).all()

    for state in result:
        print(f"{state.id}: {state.name}")

    session.close()
