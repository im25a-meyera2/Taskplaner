from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import model
from sqlalchemy import text
from database import get_db

router = APIRouter(

    prefix="/select",
    tags=["Abfragen"]
)

# ================================================== Auf alle Datensätze ===============================================


@router.get("/material/alle")
def get_all_material(db: Session = Depends(get_db)):
    db_material = db.query(model.Material).all()
    counter = 0
    for material in db_material:
        counter += 1
    if counter == 0:
        raise HTTPException(status_code=404, detail="Schüler nicht gefunden")
    return db_material


@router.get("/benutzer/alle")
def get_all_user(db: Session = Depends(get_db)):
    db_benutzer = db.query(model.Benutzer).all()
    counter = 0
    for benutzer in db_benutzer:
        counter += 1
    if counter == 0:
        raise HTTPException(status_code=404, detail="Benutzer nicht gefunden")
    return db_benutzer


@router.get("/kategorie/alle")
def get_all_kategory(db: Session = Depends(get_db)):
    db_kategorie = db.query(model.Kategorie).all()
    counter = 0
    for kategorie in db_kategorie:
        counter += 1
    if counter == 0:
        raise HTTPException(status_code=404, detail="Kategorie nicht gefunden")
    return db_kategorie

@router.get("/prioritaet/alle")
def get_all_priority(db: Session = Depends(get_db)):
    db_prioritaet = db.query(model.Prioritaet).all()
    counter = 0
    for prioritaet in db_prioritaet:
        counter += 1
    if counter == 0:
        raise HTTPException(status_code=404, detail="Prioritaet nicht gefunden")
    return db_prioritaet

@router.get("/fortschritt/alle")
def get_all_progress(db: Session = Depends(get_db)):
    db_fortschritt = db.query(model.Fortschritt).all()
    counter = 0
    for fortschritt in db_fortschritt:
        counter += 1
    if counter == 0:
        raise HTTPException(status_code=404, detail="Fortschritt nicht gefunden")
    return db_fortschritt

@router.get("/aufgabe/alle")
def get_all_task(db: Session = Depends(get_db)):
    db_aufgabe = db.query(model.Aufgabe)\
    .join(model.Kategorie)\
    .join(model.Benutzer)\
    .join(model.Fortschritt)\
    .join(model.Prioritaet)\
    .all()
    counter = 0
    for aufgabe in db_aufgabe:
        counter += 1
    if counter == 0:
        raise HTTPException(status_code=404, detail="Aufgabe nicht gefunden")
    return db_aufgabe

@router.get("/aufgabe_material/alle")
def get_all_taskt_material(db: Session = Depends(get_db)):
    db_aufgabe_material = db.query(model.AufgabeMaterial)\
    .join(model.Aufgabe)\
    .join(model.Material)\
    .all()
    counter = 0
    for aufgabe_material in db_aufgabe_material:
        counter += 1
    if counter == 0:
        raise HTTPException(status_code=404, detail="AufgabeMaterial nicht gefunden")
    return db_aufgabe_material


@router.get("/datei/alle")
def get_all_file(db: Session = Depends(get_db)):
    db_datei = (db.query(model.Datei).all())
    counter = 0
    for datei in db_datei:
        counter += 1
    if counter == 0:
        raise HTTPException(status_code=404, detail="Datei nicht gefunden")
    return db_datei

# ====================================== Auf einen Datensatz ==========================================

@router.get("/material/{material_id}")
def get_one_material(material_id: int, db: Session = Depends(get_db)):
    db_material = db.query(model.Material).filter(model.Material.MaterialID == material_id).first()

    if db_material is None:
        raise HTTPException(status_code=404, detail="Material nicht gefunden")
    return db_material


@router.get("/benutzer/{benutzer_id}")
def get_one_user(benutzer_id: int, db: Session = Depends(get_db)):
    db_benutzer = db.query(model.Benutzer).filter(model.Benutzer.BenutzerID == benutzer_id).first()
    if db_benutzer is None:
        raise HTTPException(status_code=404, detail="Benutzer nicht gefunden")
    return db_benutzer


@router.get("/kategorie/{kategorie_id}")
def get_one_kategory(kategorie_id: int, db: Session = Depends(get_db)):
    db_kategorie = db.query(model.Kategorie).filter(model.Kategorie.KategorieID == kategorie_id).first()
    if db_kategorie is None:
        raise HTTPException(status_code=404, detail="Kategorie nicht gefunden")
    return db_kategorie

@router.get("/prioritaet/{prioritaet_id}")
def get_one_priority(prioritaet_id: int, db: Session = Depends(get_db)):
    db_prioritaet = db.query(model.Prioritaet).filter(model.Prioritaet.PrioritaetID == prioritaet_id).first()
    if db_prioritaet is None:
        raise HTTPException(status_code=404, detail="Prioritaet nicht gefunden")
    return db_prioritaet

@router.get("/fortschritt/{fortschritt_id}")
def get_one_progress(fortschritt_id: int, db: Session = Depends(get_db)):
    db_fortschritt = db.query(model.Fortschritt).filter(model.Fortschritt.FortschrittID == fortschritt_id).first()
    if db_fortschritt is None:
        raise HTTPException(status_code=404, detail="Fortschritt nicht gefunden")
    return db_fortschritt

@router.get("/aufgabe/{aufgabe_id}")
def get_one_task(aufgabe_id: int, db: Session = Depends(get_db)):
    db_aufgabe = db.query(model.Aufgabe)\
    .join(model.Kategorie)\
    .join(model.Benutzer)\
    .join(model.Fortschritt)\
    .join(model.Prioritaet)\
    .filter(model.Aufgabe.AufgabeID == aufgabe_id) .first()
    if db_aufgabe is None:
        raise HTTPException(status_code=404, detail="Aufgabe nicht gefunden")
    return db_aufgabe

@router.get("/aufgabe_material/{aufgabe_id}/{material_id}")
def get_one_taskt_material(aufgabe_id: int, material_id: int, db: Session = Depends(get_db)):
    db_aufgabe_material = db.query(model.AufgabeMaterial)\
    .join(model.Aufgabe)\
    .join(model.Material)\
    .filter(model.AufgabeMaterial.AufgabeID == aufgabe_id, model.AufgabeMaterial.MaterialID == material_id) .first()
    if db_aufgabe_material is None:
        raise HTTPException(status_code=404, detail="AufgabeMaterial nicht gefunden")
    return db_aufgabe_material


@router.get("/datei/{datei_id}")
def get_one_file(datei_id: int, db: Session = Depends(get_db)):
    db_datei = (db.query(model.Datei).filter(model.Datei.DateiID == datei_id).first())
    if db_datei is None:
        raise HTTPException(status_code=404, detail="Datei nicht gefunden")
    return db_datei





# ======================================================= View ======================================
@router.get("/aufgabe/view/alle")
def view_task(db: Session = Depends(get_db)):
    task_view = (
        "create or replace view user_task "
        "as select Titel, Beginn, Ende, Ort, Koordinaten, Notiz, BenutzerName from Aufgabe "
        "left join Benutzer on Aufgabe.BenutzerID = Benutzer.BenutzerID;"
    )
    db.execute(text(task_view))
    task_select = "select * from user_task "
    select_task_result = db.execute(text(task_select)).mappings().all()
    return select_task_result

