# app/procedures_routes.py
from sqlalchemy.orm import Session
from sqlalchemy import text
from fastapi import HTTPException


def offene_aufgaben(db: Session, benutzer_id: int):
    try:
        sql = text("""
                   SELECT AufgabeID,
                          Titel,
                          Beginn,
                          Ende,
                          Ort,
                          Notiz
                   FROM Aufgabe
                   WHERE BenutzerID = :b_id
                     AND FortschrittID != 3
                   """)

        result = db.execute(sql, {"b_id": benutzer_id})

        aufgaben_liste = result.mappings().all()

        return aufgaben_liste

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Fehler bei der Abfrage: {str(e)}")