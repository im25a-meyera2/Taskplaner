# database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATENBANK_URL = "mysql+pymysql://root:hello12345@localhost:3306/taskplaner"

engine = create_engine(
    DATENBANK_URL,
    pool_pre_ping=True
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# In database.py ergänzen:

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
