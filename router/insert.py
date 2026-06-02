from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text

from database import get_db
from schema import BenutzerErstellen, MaterialErstellen, KategorieErstellen, AufgabeErstellen, PrioritaetErstellen, \
    FortschrittErstellen, DateiErstellen, AufgabeMaterialErstellen

router = APIRouter(
    prefix="/insert",
    tags=["Hinzufügen"]
)

@router.post("/material")
def create_material(material: MaterialErstellen, db: Session = Depends(get_db)):
    db.execute(
        text("""
             INSERT INTO Material (Material, IstAktiv)
             VALUES (:material, :istaktiv)
             """),
        {
            "material": material.Material,
            "istaktiv": material.IstAktiv
        }
    )
    db.commit()
    return {"message": "Material inserted successfully"}

@router.post("/kategorie")
def create_kategorie(kategorie: KategorieErstellen, db: Session = Depends(get_db)):
    db.execute(
        text("""
             INSERT INTO Kategorie (Kategorie, IstAktiv)
             VALUES (:kategorie, :istaktiv)
             """),
        {
            "kategorie": kategorie.Kategorie,
            "istaktiv": kategorie.IstAktiv
        }
    )
    db.commit()
    return {"message": "Material inserted successfully"}

@router.post("/prioritaet")
def create_prioritaet(prioritaet: PrioritaetErstellen, db: Session = Depends(get_db)):
    db.execute(
        text("""
             INSERT INTO Prioritaet (Prioritaet)
             VALUES (:prioritaet)
             """),
        {
            "prioritaet": prioritaet.Prioritaet,
        }
    )
    db.commit()
    return {"message": "Prioritaet inserted successfully"}

@router.post("/Fortschritt")
def create_fortschritt(fortschritt: FortschrittErstellen, db: Session = Depends(get_db)):
    db.execute(
        text("""
             INSERT INTO Fortschritt (Fortschritt)
             VALUES (:fortschritt)
             """),
        {
            "fortschritt": fortschritt.Fortschritt,
        }
    )
    db.commit()
    return {"message": "Fortschritt inserted successfully"}

@router.post("/benutzer")
def create_user(benutzer: BenutzerErstellen, db: Session = Depends(get_db)):
    db.execute(
        text("""
             INSERT INTO Benutzer (BenutzerName, BenutzerPWD)
             VALUES (:name, :pwd)
             """),
        {
            "name": benutzer.BenutzerName,
            "pwd": benutzer.BenutzerPWD
        }
    )
    db.commit()
    return {"message": "User inserted successfully"}

@router.post("/aufgabe")
def create_aufgabe(aufgabe: AufgabeErstellen, db: Session = Depends(get_db)):
    db.execute(
        text("""
             INSERT INTO Aufgabe (Titel, Beginn, Ende, Ort, Koordinaten, 
                                  Notiz, KategorieID, PrioritaetID, 
                                  FortschrittID, BenutzerID)
                 
             VALUES (:titel, :beginn, :ende, :ort, :koordinaten, 
                     :notiz, :kategorieid, :prioritaetid, 
                     :fortschrittid, :benutzerid)
             """),
        {
            "titel": aufgabe.Titel,
            "beginn": aufgabe.Beginn,
            "ende": aufgabe.Ende,
            "ort": aufgabe.Ort,
            "koordinaten": aufgabe.Koordinaten,
            "notiz": aufgabe.Notiz,
            "kategorieid": aufgabe.KategorieID,
            "prioritaetid": aufgabe.PrioritaetID,
            "fortschrittid": aufgabe.FortschrittID,
            "benutzerid": aufgabe.BenutzerID
        }
    )
    db.commit()
    return {"message": "Aufgabe inserted successfully"}

@router.post("/datei")
def create_datei(datei: DateiErstellen, db: Session = Depends(get_db)):
    db.execute(
        text("""
             INSERT INTO Datei (AufgabeID, Dateipfad, DateiBLOB)
             VALUES (:aufgabeid, :pfad, :blob)
             """),
        {
            "aufgabeid": datei.AufgabeID,
            "pfad": datei.Dateipfad,
            "blob": datei.DateiBLOB
        }
    )
    db.commit()
    return {"message": "Datei inserted successfully"}

@router.post("/aufgabe_material")
def create_aufgabe_material(aufgabe_material: AufgabeMaterialErstellen, db: Session = Depends(get_db)):
    db.execute(
        text("""
             INSERT INTO AufgabeMaterial (AufgabeID, MaterialID, Anzahl)
             VALUES (:aufgabeid, :materialid, :anzahl)
             """),
        {
            "aufgabeid": aufgabe_material.AufgabeID,
            "materialid": aufgabe_material.MaterialID,
            "anzahl": aufgabe_material.Anzahl
        }
    )
    db.commit()
    return {"message": "AufgabeMaterial inserted successfully"}