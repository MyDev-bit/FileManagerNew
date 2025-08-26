from sqlalchemy import String,func
from datetime import datetime
from sqlalchemy.orm import MappedAsDataclass, Mapped, mapped_column, DeclarativeBase
from typing import Annotated
from app.src.databace import engine
default_len = Annotated[str,mapped_column(String(200))]


class Base(MappedAsDataclass,DeclarativeBase):
    pass




class Users(Base,MappedAsDataclass):
    __tablename__ = "users"
    id:Mapped[int] = mapped_column(primary_key=True)
    user_id:Mapped[str] = mapped_column(String(200))
    name:Mapped[default_len]
    password:Mapped[default_len]


class Files(Base,MappedAsDataclass):
    __tablename__ = "files"
    id:Mapped[int] = mapped_column(primary_key=True)
    file_id:Mapped[str] = mapped_column(String(200))
    user_load:Mapped[default_len]
    file_name:Mapped[default_len]
    file_extension:Mapped[default_len]


class Logging(Base,MappedAsDataclass):
    __tablename__ = "logs"
    id:Mapped[int] = mapped_column(primary_key=True)
    log_id:Mapped[default_len]
    log_status:Mapped[default_len]
    who_load_value:Mapped[default_len] = mapped_column(nullable=True)
    log_value:Mapped[default_len]
    log_time:Mapped[datetime] = mapped_column(default=func.now())

def create_tables():
    """Создание таблиц в базе данных"""
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)






