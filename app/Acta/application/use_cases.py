# app/Acta/application/use_cases.py
from app.Acta.domain.entities import Acta
from app.Acta.domain.repositories import ActaRepository


class CrearActa:
    def __init__(self, repo: ActaRepository):
        self.repo = repo

    def ejecutar(self, titulo: str, contenido: str) -> Acta:
        # pyrefly: ignore  # bad-argument-type
        acta = Acta(id=None, titulo=titulo, contenido=contenido)
        return self.repo.save(acta)
