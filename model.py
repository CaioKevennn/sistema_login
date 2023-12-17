from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


def returnsession_or_engine(typ):
    user = "root"
    password = ""
    HOST = "localhost"
    db = "login"
    PORT = "3306"
    CONN = f"mysql+pymysql://{user}:{password}@{HOST}:{PORT}/{db}"
    engine = create_engine(CONN, echo=True)
    Session = sessionmaker(bind=engine)
    if typ == "session":
        return Session()
    elif typ == "engine":
        return engine


base = declarative_base()
session = returnsession_or_engine("session")


class Login(base):
    __tablename__ = "login"
    name = Column(String(50))
    id = Column(Integer, primary_key=True)
    email = Column(String(50))
    passw = Column(String(50))


base.metadata.create_all(returnsession_or_engine("engine"))
