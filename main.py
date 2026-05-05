from fastapi import FastAPI
from sqlalchemy import create_engine, text

app = FastAPI()

DATENBANK_URL = "mysql+pymysql://root:hello12345@localhost/taskplaner"

engine = create_engine(DATENBANK_URL)

@app.get("/test")
def test_verbindung():
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
        return {"nachricht": "SQLAlchemy ist erfolgreich verbunden! 🚀"}
    except Exception as e:
        return {"fehler": f"Klappt noch nicht: {e}"}