#!/usr/bin/python3
"""Start link class to table in database """


import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    arg = sys.argv[4]
    orm = session.query(State).filter(State.name == arg)
    orm = orm.order_by(State.id).all()
    if not orm:
        print("Not found")
    else:
        for state in orm:
            print(state.id)
    session.close()
