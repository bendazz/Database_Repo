from sqlmodel import Session, select   
from models import Faculty, engine   

with Session(engine) as session:
    statement = select(Faculty.first_name,Faculty.last_name,Faculty.age).where(Faculty.age == 60)
    records = session.exec(statement)
    
print(records.all())


