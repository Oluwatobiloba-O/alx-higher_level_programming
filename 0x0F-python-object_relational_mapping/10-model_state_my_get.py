
#!/usr/bin/python3
# Lists the State object with the name passed as argument
# from the database hbtn_0e_6_usa.
# Usage: ./10-model_state_my_get.py <mysql username> /
#                                   <mysql password> /
#                                   <database name>
#                                   <state name searched>
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3])),
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    instance = session.query(State).filter(State.name == (sys.argv[4],))
    try:
        print(instance[0].id)
    except IndexError:
        print("Not found")