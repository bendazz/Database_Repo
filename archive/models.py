from sqlmodel import Field,SQLModel

class people(SQLModel,table = True):
    playerID: str = Field(primary_key = True)
    nameFirst: str | None = None
    nameLast: str | None = None

class batting(SQLModel,table = True):
    playerID: str = Field(primary_key = True)
    yearID: int = Field(primary_key = True)
    stint: int = Field(primary_key = True)
    teamID: str | None = None
    HR: int | None = None




