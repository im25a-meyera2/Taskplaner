# main.py
from fastapi import FastAPI, Depends

from pydantic import BaseModel

from sqlalchemy import text
from sqlalchemy.orm import Session
from websockets.version import commit

from database import get_db
from database import engine


from router.insert import router as insert_router
from router.delete import router as delete_router
from router.update import router as update_router

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: bool

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}
@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/test")
def test_verbindung():
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
        return {"nachricht": "SQLAlchemy ist erfolgreich verbunden! 🚀"}
    except Exception as e:
        return {"fehler": f"Klappt noch nicht: {e}"}

# Taskplaner Routen

class Benutzer(BaseModel):
    benutzer_id: int
    benutzer_name: str
    benutzer_pwd: str


@app.get("/users")
def get_users(db: Session = Depends(get_db)):
    result = db.execute(text("SELECT * FROM Benutzer"))
    return result.mappings().all()

app.include_router(insert_router)
app.include_router(delete_router)
app.include_router(update_router)
