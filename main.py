from fastapi import FastAPI
from pydantic import BaseModel
from sqlalchemy import create_engine, text
from database import engine
app = FastAPI()

from router import delete
app.include_router(delete.router)


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
