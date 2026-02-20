from sqlmodel import SQLModel, Field, create_engine

class Faculty(SQLModel, table = True):
    id: int | None = Field(default = None,primary_key = True)
    first_name: str
    last_name: str
    age: int | None = None

engine = create_engine('sqlite:///department.db')

SQLModel.metadata.create_all(engine)


