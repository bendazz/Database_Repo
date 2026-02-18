from sqlmodel import create_engine, Session, select
from models import people,batting


engine = create_engine('sqlite:///baseball.db',echo = True)

with Session(engine) as session:
    query = (
        select(batting.playerID)
        #.where((batting.yearID == 1976)&(batting.teamID == 'PHI'))
    )
    records = session.exec(query)
    
print(records.all())

