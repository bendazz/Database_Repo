from sqlmodel import Field, SQLModel

class Batting(SQLModel,table = True):
    playerID:str = Field(primary_key = True)
    yearID:int = Field(primary_key = True)
    stint:int = Field(primary_key = True)
    teamID:str|None = None
    HR:int|None = None

class People(SQLModel,table = True):
    playerID:str = Field(primary_key = True)
    nameFirst:str|None = None
    nameLast:str|None = None

class Teams(SQLModel,table = True):
    teamID:str = Field(primary_key = True)
    yearID:str = Field(primary_key = True)
    name:str|None = None
    HR:int|None = None