from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text

from database import get_db
from schema import BenutzerErstellen, MaterialErstellen, KategorieErstellen

router = APIRouter(

    prefix="/users",
    tags=["Hinzufügen"]
)

@router.post("/insert/user")
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

@router.post("/insert/material")
def create_user(material: MaterialErstellen, db: Session = Depends(get_db)):
    db.execute(
        text("""
             INSERT INTO Material (Material, IsAktiv)
             VALUES (:material, :isaktive)
             """),
        {
            "material": material.Material,
            "isaktive": material.IsAktive
        }
    )

@router.post("/insert/kategorie")
def create_kategorie(kategorie: KategorieErstellen, db: Session = Depends(get_db)):
    db.execute(
        text("""
             INSERT INTO Kategorie (Kategorie, IsAktiv)
             VALUES (:kategorie, :isaktive)
             """),
        {
            "material": kategorie.Kategorie,
            "isaktive": kategorie.IsAktive
        }
    )

@router.post("/insert/kategorie")
def create_kategorie(kategorie: KategorieErstellen, db: Session = Depends(get_db)):
    db.execute(
        text("""
             INSERT INTO Kategorie (Kategorie, IsAktiv)
             VALUES (:kategorie, :isaktive)
             """),
        {
            "material": kategorie.Kategorie,
            "isaktive": kategorie.IsAktive
        }
    )

    db.commit()
    return {"message": "Benutzer wurde erstellt ✅"}