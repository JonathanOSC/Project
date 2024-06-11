from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DATABASE_CONNECTION = "sqlite:///inventory.db"

engine = create_engine(DATABASE_CONNECTION)

Session = sessionmaker(bind=engine)

Base = declarative_base()



def get_database_session():
    db = Session()
    try:
      return db
    finally:
      db.close()