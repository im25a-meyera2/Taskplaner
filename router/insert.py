from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text

from database import get_db
from schema import BenutzerErstellen

router = APIRouter()

@router.post("/users")
def create_user(user: BenutzerErstellen, db: Session = Depends(get_db)):
    db.execute(
        text("""
             INSERT INTO Benutzer (BenutzerName, BenutzerPWD)
             VALUES (:name, :pwd)
             """),
        {
            "name": user.BenutzerName,
            "pwd": user.BenutzerPWD
        }
    )

    db.commit()
    return {"message": "Benutzer wurde erstellt ✅"}