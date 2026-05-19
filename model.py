from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text, ForeignKey, LargeBinary
from main import engine
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Material(Base):
    __tablename__ = "Material"

    MaterialID = Column(Integer, primary_key=True, autoincrement=True, index=True, nullable=False)
    Material = Column(String(100), nullable=False)
    IstAktiv = Column(Boolean, nullable=False, default=True)

class Kategorie(Base):
    __tablename__ = "Kategorie"

    KategorieID = Column(Integer, primary_key=True, autoincrement=True, index=True, nullable=False)
    Kategorie = Column(String(100), nullable=False)
    IstAktiv = Column(Boolean, nullable=False, default=True)

class Prioritaet(Base):
    __tablename__ = "Prioritaet"

    PrioritaetID = Column(Integer, primary_key=True, autoincrement=True, index=True, nullable=False)
    Prioritaet = Column(String(100), nullable=False)

class Fortschritt(Base):
    __tablename__ = "Fortschritt"

    FortschrittID = Column(Integer, primary_key=True, autoincrement=True, index=True, nullable=False)
    Fortschritt = Column(String(100), nullable=False)

class Benutzer(Base):
    __tablename__ = "Benutzer"

    BenutzerID = Column(Integer, primary_key=True, autoincrement=True, index=True, nullable=False)
    BenutzerName = Column(String(100), nullable=False)
    BenutzerPWD = Column(String(100), nullable=False)

class Aufgabe(Base):
    __tablename__ = "Aufgabe"

    AufgabeID = Column(Integer, primary_key=True, autoincrement=True, index=True, nullable=False)
    Titel = Column(String(100), nullable=False)
    Beginn = Column(DateTime, nullable=False)
    Ende = Column(DateTime, nullable=True)
    Ort = Column(String(250), nullable=True)
    Koordinaten = Column(String(100), nullable=True)
    Notiz = Column(Text, nullable=True)
    KategorieID = Column(Integer,ForeignKey("Kategorie.KategorieID"), nullable=False)
    PrioritaetID = Column(Integer,ForeignKey("Prioritaet.PrioritaetID"), nullable=False)
    FortschrittID = Column(Integer, ForeignKey("Fortschritt.FortschrittID"), nullable=False)
    BenutzerID = Column(Integer, ForeignKey("Benutzer.BenutzerID"), nullable=False)

    kategorie = relationship("Kategorie")
    prioritaet = relationship("Prioritaet")
    fortschritt = relationship("Fortschritt")
    benutzer = relationship("Benutzer")

class Datei(Base):
    __tablename__ = "Datei"

    DateiID = Column(Integer, primary_key=True, autoincrement=True, index=True, nullable=False)
    AufgabeID = Column(Integer, ForeignKey("Aufgabe.AufgabeID"), nullable=False)
    Dateipfad = Column(String(250))
    DateiBLOB = Column(LargeBinary)

class AufgabeMaterial(Base):
    __tablename__ = "AufgabeMaterial"

    AufgabeID = Column(Integer, ForeignKey("Aufgabe.AufgabeID"), primary_key=True, nullable=False)
    MaterialID = Column(Integer, ForeignKey("Material.MaterialID"), primary_key=True, nullable=False)
    Anzahl = Column(Integer, nullable=True)

