# app/Acta/domain/entities.py
from dataclasses import dataclass

@dataclass
class Acta:
    id: int
    titulo: str
    contenido: str
