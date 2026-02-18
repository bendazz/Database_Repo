from sqlmodel import Session, select
from sqlalchemy import func
from models import Batting,People,Teams
from engine import engine
import pandas as pd

total_hr = func.sum(Batting.HR).label('total_hr')

statement = (
    select(People.nameFirst, People.nameLast, total_hr)
    .join(People, People.playerID == Batting.playerID)
    .where(Batting.teamID == 'PHI')
    .group_by(People.playerID, People.nameFirst, People.nameLast)
    .having(total_hr >= 50)
    .order_by(total_hr.desc())
)

with Session(engine) as session:
    results = session.exec(statement).all()

records_df = pd.DataFrame(results, columns=['nameFirst', 'nameLast', 'total_hr'])
print(records_df)