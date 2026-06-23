"""This File ist for all the updates"""


from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import *
import model
import schema

router = APIRouter(
    prefix="/update",
    tags=["Update"]
)

@router.put("/material/{material_id}")
def update_material(material_id: int, material: schema.MaterialBase, db: Session = Depends(get_db)):
    """This function update the material"""
    db_material = db.query(model.Material).filter(model.Material.MaterialID == material_id).first()
    if db_material is None:
        raise HTTPException(status_code=404, detail="Material not found")

    db_material.Material = material.Material
    db_material.IstAktiv = material.IstAktiv
    db.add(db_material)
    db.commit()
    return {"nachricht": f"Material mit ID {material_id} wurde erfolgrich geupdatet"}

@router.put("/kategorie/{kategorie_id}")
def update_kategorie(kategorie_id: int, kategorie: schema.KategorieBase, db: Session = Depends(get_db)):
    """This function updates the Kategorie"""
    db_kategorie = db.query(model.Kategorie).filter(model.Kategorie.KategorieID == kategorie_id).first()
    if db_kategorie is None:
        raise HTTPException(status_code=404, detail="Kategorie not found")

    db_kategorie.Kategorie = kategorie.Kategorie
    db_kategorie.IstAktiv = kategorie.IstAktiv
    db.add(db_kategorie)
    db.commit()
    return {"nachricht": f"Kategorie  mit ID {kategorie_id} wurde erfolgrich geupdatet"}

@router.put("/prioritaet/{prioritaet_id}")
def update_prioritaet(prioritaet_id: int, prioritaet: schema.PrioritaetBase, db: Session = Depends(get_db)):
    """This function update the Priotaet"""
    db_prioritaet = db.query(model.Material).filter(model.Prioritaet.PrioritaetID == prioritaet_id).first()
    if db_prioritaet is None:
        raise HTTPException(status_code=404, detail="Material not found")

    db_prioritaet.Prioritaet = prioritaet.Prioritaet
    db.add(db_prioritaet)
    db.commit()
    return {"nachricht": f"Priortaet mit ID {prioritaet_id} wurde erfolgrich geupdatet"}

@router.put("/fortschritt/{fortschritt_id}")
def update_fortschritt(fortschritt_id: int, fortschritt: schema.FortschrittBase, db: Session = Depends(get_db)):
    """This function update the fortschritt"""
    db_fortschritt = db.query(model.Fortschritt).filter(model.Fortschritt.FortschrittID == fortschritt_id).first()
    if db_fortschritt is None:
        raise HTTPException(status_code=404, detail="Material not found")

    db_fortschritt.Fortschritt = fortschritt.Fortschritt
    db.add(db_fortschritt)
    db.commit()
    return {"nachricht": f"Fortschritt mit ID {fortschritt_id} wurde erfolgrich geupdatet"}



@router.put("/benutzer/{benutzer_id}")
def update_benutzer(benutzer_id: int, benutzer: schema.BenutzerErstellen, db: Session = Depends(get_db)):
    """This function updates the benutzer (Name & Passwort)"""
    db_benutzer = db.query(model.Benutzer).filter(model.Benutzer.BenutzerID == benutzer_id).first()
    if db_benutzer is None:
        raise HTTPException(status_code=404, detail="Benutzer not found")

    db_benutzer.BenutzerName = benutzer.BenutzerName
    db_benutzer.BenutzerPWD = benutzer.BenutzerPWD
    db.add(db_benutzer)
    db.commit()
    return {"nachricht": f"Benutzer mit ID {benutzer_id} wurde erfolgreich geupdatet"}


@router.put("/aufgabe/{aufgabe_id}")
def update_aufgabe(aufgabe_id: int, aufgabe: schema.AufgabeBase, db: Session = Depends(get_db)):
    """This function updates a complete aufgabe"""
    db_aufgabe = db.query(model.Aufgabe).filter(model.Aufgabe.AufgabeID == aufgabe_id).first()
    if db_aufgabe is None:
        raise HTTPException(status_code=404, detail="Aufgabe not found")

    db_aufgabe.Titel = aufgabe.Titel
    db_aufgabe.Beginn = aufgabe.Beginn
    db_aufgabe.Ende = aufgabe.Ende
    db_aufgabe.Ort = aufgabe.Ort
    db_aufgabe.Koordinaten = aufgabe.Koordinaten
    db_aufgabe.Notiz = aufgabe.Notiz
    db_aufgabe.KategorieID = aufgabe.KategorieID
    db_aufgabe.PrioritaetID = aufgabe.PrioritaetID
    db_aufgabe.FortschrittID = aufgabe.FortschrittID
    db_aufgabe.BenutzerID = aufgabe.BenutzerID

    db.add(db_aufgabe)
    db.commit()
    return {"nachricht": f"Aufgabe mit ID {aufgabe_id} wurde erfolgreich geupdatet"}


@router.put("/datei/{datei_id}")
def update_datei(datei_id: int, datei: schema.DateiBase, db: Session = Depends(get_db)):
    """This function updates a datei link or blob"""
    db_datei = db.query(model.Datei).filter(model.Datei.DateiID == datei_id).first()
    if db_datei is None:
        raise HTTPException(status_code=404, detail="Datei not found")

    db_datei.AufgabeID = datei.AufgabeID
    db_datei.Dateipfad = datei.Dateipfad
    db_datei.DateiBLOB = datei.DateiBLOB

    db.add(db_datei)
    db.commit()
    return {"nachricht": f"Datei mit ID {datei_id} wurde erfolgreich geupdatet"}


@router.put("/aufgabe_material/{aufgabe_id}/{material_id}")
def update_aufgabe_material(aufgabe_id: int, material_id: int, aufgabe_material: schema.AufgabeMateriallBase,
                            db: Session = Depends(get_db)):
    """This function updates the count of a material inside a task"""
    db_am = db.query(model.AufgabeMaterial).filter(
        model.AufgabeMaterial.AufgabeID == aufgabe_id,
        model.AufgabeMaterial.MaterialID == material_id
    ).first()

    if db_am is None:
        raise HTTPException(status_code=404, detail="AufgabeMaterial entry not found")

    db_am.Anzahl = aufgabe_material.Anzahl

    db.add(db_am)
    db.commit()
    return {
        "nachricht": f"Material-Anzahl für Aufgabe {aufgabe_id} und Material {material_id} wurde erfolgreich geupdatet"}
