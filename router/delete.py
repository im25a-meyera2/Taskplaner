from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import database
from database import *
import model
import schema

router = APIRouter(
    prefix="/delete",
    tags=["Löschen"]
)

@router.delete("/material/{material_id}")
def material_delete(material_id: int, db: Session = Depends(get_db)):
    db_material = db.query(model.Material).filter(model.Material.MaterialID == material_id).first()
    if not db_material:
        raise HTTPException(status_code=404, detail="Material nicht gefunden!")
    db.query(model.AufgabeMaterial).filter(model.AufgabeMaterial.MaterialID == material_id).delete()
    db.delete(db_material)
    db.commit()
    return {"nachricht": f"Material mit ID {material_id} wurde gelöscht"}




@router.delete("/aufgabe/{aufgabe_id}")
def delete_aufgabe(aufgabe_id: int, db: Session = Depends(get_db)):
    db_aufgabe = db.query(model.Aufgabe).filter(model.Aufgabe.AufgabeID == aufgabe_id).first()
    if not db_aufgabe:
        raise HTTPException(status_code=404, detail="Aufgabe nicht gefunden!")
    db.query(model.AufgabeMaterial).filter(model.AufgabeMaterial.AufgabeID == aufgabe_id).delete()
    db.query(model.Datei).filter(model.Datei.AufgabeID == aufgabe_id).delete()
    db.delete(db_aufgabe)
    db.commit()
    return {"nachricht": f"Aufgabe mit ID {aufgabe_id} wurde gelöscht"}


@router.delete("/kategorie/{kategorie_id}")
def delete_kategorie(kategorie_id: int, db: Session = Depends(get_db)):
    db_kategorie = db.query(model.Kategorie).filter(model.Kategorie.KategorieID == kategorie_id).first()
    if not db_kategorie:
        raise HTTPException(status_code=404, detail="Kategorie nicht gefunden!")

    db_aufgaben = db.query(model.Aufgabe).filter(model.Aufgabe.KategorieID == kategorie_id).all()

    for aufgabe in db_aufgaben:
        delete_aufgabe(aufgabe_id=aufgabe.AufgabeID, db=db)

    db.delete(db_kategorie)
    db.commit()

    return {"nachricht": f"Kategorie {kategorie_id} und alle verknüpften Aufgaben wurden gelöscht"}


@router.delete("/benutzer/{benutzer_id}")
def delete_benutzer(benutzer_id: int, db: Session = Depends(get_db)):
    db_benutzer = db.query(model.Benutzer).filter(model.Benutzer.BenutzerID == benutzer_id).first()
    if not db_benutzer:
        raise HTTPException(status_code=404, detail="Benutzer nicht gefunden!")
    db_aufgaben = db.query(model.Aufgabe).filter(model.Aufgabe.BenutzerID == benutzer_id).all()

    for aufgabe in db_aufgaben:
        delete_aufgabe(aufgabe_id=aufgabe.AufgabeID, db=db)
    db.delete(db_benutzer)
    db.commit()
    return {"nachricht": f"Benutzer mit ID {benutzer_id} wurde gelöscht"}


@router.delete("/prioritaet/{prioritaet_id}")
def delete_prioritaet(prioritaet_id: int, db: Session = Depends(get_db)):
    db_priotaet = db.query(model.Prioritaet).filter(model.Prioritaet.PrioritaetID == prioritaet_id).first()
    if not db_priotaet:
        raise HTTPException(status_code=404, detail="Prioritaet nicht gefunden!")

    db_aufgaben = db.query(model.Aufgabe).filter(model.Aufgabe.PrioritaetID == prioritaet_id).all()

    for aufgabe in db_aufgaben:
        delete_aufgabe(aufgabe_id=aufgabe.AufgabeID, db=db)

    db.delete(db_priotaet)
    db.commit()
    return {"nachricht": f"Prioritaet mit ID {prioritaet_id} wurde gelöscht"}


@router.delete("/fortschritt/{fortschritt_id}")
def delete_fortschritt(fortschritt_id: int, db: Session = Depends(get_db)):
    db_fortschritt = db.query(model.Fortschritt).filter(model.Fortschritt.FortschrittID == fortschritt_id).first()
    if not db_fortschritt:
        raise HTTPException(status_code=404, detail="Fortschritt nicht gefunden!")
    db_aufgaben = db.query(model.Aufgabe).filter(model.Aufgabe.FortschrittID == fortschritt_id).all()

    for aufgabe in db_aufgaben:
        delete_aufgabe(aufgabe_id=aufgabe.AufgabeID, db=db)

    db.delete(db_fortschritt)
    db.commit()
    return {"nachricht": f"Fortschritt mit ID {fortschritt_id} wurde gelöscht"}


@router.delete("/aufgabe_material/{aufgabe_id}/{material_id}")
def delete_aufgabe_material(aufgabe_id: int, material_id: int, db: Session = Depends(get_db)):
    db_aufgabe_material = db.query(model.AufgabeMaterial).filter(model.AufgabeMaterial.AufgabeID == aufgabe_id, model.AufgabeMaterial.MaterialID == material_id).first()
    if not db_aufgabe_material:
        raise HTTPException(status_code=404, detail="AufgabeMaterial nicht gefunden!")
    db.delete(db_aufgabe_material)
    db.commit()
    return {"nachricht": f"AufgabeMaterial mit ID {aufgabe_id}, {material_id} wurde gelöscht"}

@router.delete("/datei/{datei_id}")
def delete_datei(datei_id: int, db: Session = Depends(get_db)):
    db_datei = db.query(model.Datei).filter(model.Datei.DateiID == datei_id).first()
    if not db_datei:
        raise HTTPException(status_code=404, detail="Datei nicht gefunden!")
    db.delete(db_datei)
    db.commit()
    return {"nachricht": f"Datei mit ID {datei_id} wurde gelöscht"}

