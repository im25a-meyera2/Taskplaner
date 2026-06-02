# app/routers/aufgaben.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from procedures import offene_aufgaben  # Unsere neue Python-Funktion

router = APIRouter(
    prefix="/procedures",
    tags=["Stored Procedures"]
)
@router.get("/benutzer/{benutzer_id}/offene-aufgaben")
def get_offene_aufgaben_python_route(benutzer_id: int, db: Session = Depends(get_db)):
    # Ruft die Python-Abfrage auf
    daten = offene_aufgaben(db, benutzer_id)

    return {
        "benutzer_id": benutzer_id,
        "anzahl_offen": len(daten),
        "aufgaben": daten
    }