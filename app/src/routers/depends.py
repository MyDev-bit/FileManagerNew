from sqlalchemy.orm import Session
from typing import Annotated
from sqlalchemy import create_engine
from fastapi import Depends



def engine_connect():
    with engine.connect() as conn:
        yield conn



DepDB = Annotated[Session,Depends(engine_connect)]

