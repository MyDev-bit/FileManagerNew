from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine("mysql+mysqlconnector://root:root123@localhost:3306/mydb")
session = sessionmaker(bind=engine)

