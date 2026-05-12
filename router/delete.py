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

@router.delete("/{material_id}")
def material_delete(material_id: int, db: Session = Depends(get_db)):
    db_material = db.query(model.Material).filter(model.Material.MaterialID == material_id).first()
    if not db_material:
        raise HTTPException(status_code=404, detail="Material nicht gefunden!")
    db.delete(db_material)
    db.commit()
    return {"nachricht": f"Material mit ID {material_id} wurde gelöscht"}
