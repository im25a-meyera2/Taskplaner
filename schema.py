# schema.py
from datetime import datetime
from pydantic import BaseModel
from typing import Optional

# ====================================

class MaterialBase(BaseModel):
    Material: str
    IstAktiv: bool = True
    class Config:
        from_attributes = True

class MaterialErstellen(MaterialBase):
    pass

class MaterialAntworten(MaterialBase):
    MaterialID: int

# ======================================

class KategorieBase(BaseModel):
    Kategorie: str
    IstAktiv: bool = True
    class Config:
        from_attributes = True

class KategorieErstellen(KategorieBase):
    pass

class KategorieAntworten(KategorieBase):
    KategorieID: int

# =================================

class PrioritaetBase(BaseModel):
    Prioritaet: str
    class Config:
        from_attributes = True

class PrioritaetErstellen(PrioritaetBase):
    pass

class PrioritaetAntworten(PrioritaetBase):
    PrioritaetID: int

# ====================================

class FortschrittBase(BaseModel):
    Fortschritt: str
    class Config:
        from_attributes = True

class FortschrittErstellen(FortschrittBase):
    pass

class FortschrittAntworten(FortschrittBase):
    FortschrittID: int

# ===========================================

class BenutzerBase(BaseModel):
    BenutzerName: str
    class Config:
        from_attributes = True

class BenutzerAntworten(BenutzerBase):
    BenutzerID: int

class BenutzerErstellen(BenutzerBase):
    BenutzerPWD: str

# =====================================

class AufgabeBase(BaseModel):
    Titel: str
    Beginn: datetime
    Ende: Optional[datetime] = None
    Ort: Optional[str] = None
    Koordinaten: Optional[str] = None
    Notiz: Optional[str] = None
    KategorieID: int
    PrioritaetID: int
    FortschrittID: int
    BenutzerID: int
    class Config:
        from_attributes = True

class AufgabeErstellen(AufgabeBase):
    pass

class AufgabeAntworten(AufgabeBase):
    AufgabeID: int

class AufgabeUpdate(BaseModel):
    Titel: Optional[str] = None
    Beginn: Optional[datetime] = None
    Ende: Optional[datetime] = None
    Notiz: Optional[str] = None
    Ort: Optional[str] = None
    Koordinaten: Optional[str] = None
    FortschrittID: Optional[int] = None
    PrioritaetID: Optional[int] = None

# ===================================

class DateiBase(BaseModel):
    AufgabeID: int
    Dateipfad: Optional[str] = None
    DateiBLOB: Optional[bytes] = None
    class Config:
        from_attributes = True

class DateiErstellen(DateiBase):
    pass

class DateiAntworten(DateiBase):
    DateiID: int

# ==============================

class AufgabeMateriallBase(BaseModel):
    Anzahl: Optional[int]
    MaterialID: int
    AufgabeID: int
    class Config:
        from_attributes = True
class AufgabeMaterialErstellen(AufgabeMateriallBase):
    pass

class AufgabeMaterialAntworten(AufgabeMateriallBase):
    MaterialID: int
    AufgabeID: int


