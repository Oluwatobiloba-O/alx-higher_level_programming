
#!/usr/bin/python3
# Lists all State objects that contain the letter a
# from the database hbtn_0e_6_usa.
# Usage: ./9-model_state_filter_a.py <mysql username> /
#                                    <mysql password> /
#                                    <database name>
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3])),
    engine = create_engine(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for instance in session.query(State).filter(State.name.like('%a%')):
        print(instance.id, instance.name, sep=": ")