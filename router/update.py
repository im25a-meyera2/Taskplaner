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

